# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact and numerical checks of the n = 2 rank-0 case (Section 3 of the
revised "hitch-hiker's guide to the metaplectic trace formula for SL(2)").

Checks:
  * the 1995 cocycle (3.2) on A equals (t1, t2)_v, the restriction of beta;
  * the Weil index gamma_psi(a), computed from Gauss sums over Q_p and in closed
    form over R, is an 8th root of unity, depends only on a mod squares, equals 1
    on units at odd p, and satisfies
        gamma(ab) gamma(1) = gamma(a) gamma(b) (a, b)_v           (Weil);
    hence chi_psi(a(t), zeta) = zeta * gamma(t)/gamma(1) is a genuine character;
  * the product formula prod_v gamma_v(t) = 1 for t in Q^x, with the standard
    character psi of A/Q (psi_p(x) = e^{2 pi i {x}_p}, psi_oo(x) = e^{-2 pi i x}),
    so chi_psi is trivial on A(Q) (Example 3.B);
  * genuine characters take the values +-i on the order-4 element of A(A)^1
    over k = Q (Example 3.A).
"""
import cmath
import random
import sys
from fractions import Fraction as Fr

from padic_lib import hilbert, vp, INF, unit_mod

random.seed(20261110)
FAILS = []


def report(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- (3.2)
def beta_1995_A(t1, t2, v):
    """1995 formula (3.2) with n = 2: (g1^-1, g2^-1)(-g1 g2^-1, g1^-1 g2^-1)."""
    return hilbert(1 / t1, 1 / t2, v) * hilbert(-t1 / t2, 1 / (t1 * t2), v)


def rand_rat(big=60):
    while True:
        a, b = random.randint(-big, big), random.randint(1, big)
        if a:
            return Fr(a, b)


for v in [INF, 2, 3, 5, 7]:
    ok = all(beta_1995_A(t1, t2, v) == hilbert(t1, t2, v)
             for t1, t2 in ((rand_rat(), rand_rat()) for _ in range(300)))
    report("(3.1): the 1995 cocycle (3.2) on A equals (t1,t2)_v, v=%s" % v, ok)


# ---------------------------------------------------------------- Weil index
def gamma(a, v, M=None):
    """Weil index gamma_psi(a) of x -> psi_v(a x^2), defined by
    int_F psi_v(a x^2) dx = gamma(a) |2a|^{-1/2} (self-dual measure)."""
    a = Fr(a)
    if v == INF:
        # psi_oo(x) = exp(-2 pi i x)
        return cmath.exp(-1j * cmath.pi / 4 * (1 if a > 0 else -1))
    p = v
    al = vp(a, p)
    a = a / Fr(p) ** (2 * (al // 2))   # reduce mod squares: valuation 0 or 1
    al = vp(a, p)
    if p != 2:
        # replace the unit part by 1 or the least quadratic nonresidue
        u0 = unit_mod(a, p, 1)
        nr = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) == p - 1)
        a = Fr(p) ** al * (1 if pow(u0, (p - 1) // 2, p) == 1 else nr)
    ordtwo = 1 if p == 2 else 0
    # integrate over p^{-M} Z_p; M = 1 suffices for odd p (checked below
    # against larger M), the dyadic case needs more
    if M is None:
        M = 1 if p != 2 else (al + 3 + 2 * ordtwo) // 2 + 1
    e = 2 * M - al                      # a y^2 p^{-2M} = u y^2 / p^e
    R = e + ordtwo                      # integrand depends on y mod p^R
    mod = p ** e
    u = unit_mod(a, p, e)
    s = 0
    for y in range(p ** R):
        s += cmath.exp(2j * cmath.pi * ((u * y * y) % mod) / mod)
    integral = p ** M * s / p ** R
    absval = float(Fr(p) ** (-vp(2 * a, p)))   # |2a|_p
    return integral * absval ** 0.5


def close(z, w, eps=1e-9):
    return abs(z - w) < eps


for p in [3, 5, 7]:
    report("Weil index: the Gauss sum has stabilized at M = 1, p=%d" % p,
           all(abs(gamma(r, p) - gamma(r, p, M=3)) < 1e-9 for r in (Fr(1), Fr(2), Fr(p), Fr(2 * p))))


PL = [INF, 2, 3, 5, 7]
reps = {INF: [Fr(1), Fr(-1)], 2: [Fr(x) for x in (1, 3, 5, 7, 2, 6, 10, 14)],
        3: [Fr(x) for x in (1, 2, 3, 6)], 5: [Fr(x) for x in (1, 2, 5, 10)],
        7: [Fr(x) for x in (1, 3, 7, 21)]}
G = {v: {r: gamma(r, v) for r in reps[v]} for v in PL}
for v in PL:
    vals = list(G[v].values())
    report("Weil index: |gamma|=1, gamma^8=1, v=%s" % v,
           all(close(abs(z), 1) and close(z ** 8, 1) for z in vals),
           ", ".join("%s:%s" % (r, complex(round(z.real, 6), round(z.imag, 6))) for r, z in G[v].items()))
    # dependence only on the square class
    ok = all(close(gamma(r * s * s, v), G[v][r]) for r in reps[v] for s in [Fr(3), Fr(-5, 7), Fr(2, 3)])
    report("Weil index depends only on a mod squares, v=%s" % v, ok)
    ok = True
    for r1 in reps[v]:
        for r2 in reps[v]:
            lhs = gamma(r1 * r2, v) * G[v][Fr(1)]
            rhs = G[v][r1] * G[v][r2] * hilbert(r1, r2, v)
            ok &= close(lhs, rhs)
    report("Weil: gamma(ab)gamma(1) = gamma(a)gamma(b)(a,b)_v, v=%s" % v, ok)
for p in [3, 5, 7]:
    report("Weil index: gamma(u) = gamma(1) for units, p=%d" % p,
           all(close(gamma(u, p), G[p][Fr(1)]) for u in [Fr(x) for x in range(1, 3 * p) if x % p]))


def mu(t, v):
    return gamma(t, v) / gamma(1, v)


# genuine character chi_psi(a(t), zeta) = zeta mu(t): check on the group law
for v in PL:
    ok = True
    for _ in range(60):
        t1, t2 = rand_rat(), rand_rat()
        # (a(t1),1)(a(t2),1) = (a(t1 t2), (t1,t2))
        ok &= close(mu(t1, v) * mu(t2, v), hilbert(t1, t2, v) * mu(t1 * t2, v))
    report("Lemma 3.3: chi_psi(a(t),zeta) = zeta*gamma(t)/gamma(1) is a genuine character, v=%s" % v, ok)


# Example 3.B: closed form at odd p for the standard psi_p
def jac(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


ok = True
for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
    eps = 1 if p % 4 == 1 else 1j
    for u in range(1, p):
        ok &= close(gamma(Fr(u), p), 1) and close(gamma(Fr(p * u), p), jac(u, p) * eps)
report("Example 3.B: gamma_p(u) = 1, gamma_p(pu) = (u/p) eps_p for odd p <= 31", ok)
report("Example 3.B: chi_psi,oo(a(-1),1) = gamma_oo(-1)/gamma_oo(1) = i", close(mu(-1, INF), 1j))

# product formula over Q
def primes_of(t):
    from sympy import primefactors
    t = Fr(t)
    return set(primefactors(abs(t.numerator))) | set(primefactors(t.denominator))


ok = True
for _ in range(200):
    t = rand_rat(200)
    S = {INF, 2} | primes_of(t)
    prod = 1
    for v in S:
        prod *= mu(t, v)
    ok &= close(prod, 1)
report("Example 3.B: prod_v gamma_v(t)/gamma_v(1) = 1 for t in Q^x (chi_psi automorphic)", ok)

# Example 3.A: order-4 element; genuine characters take values +-i on it
sq = hilbert(-1, -1, INF)
report("Example 3.A: (a(-1)_oo, 1)^2 = (1, -1), so a genuine character is +-i there",
       sq == -1 and close(mu(-1, INF) ** 2, -1), "mu_oo(-1) = %s" % mu(-1, INF))

print()
if FAILS:
    print("%d check(s) FAILED: %s" % (len(FAILS), ", ".join(FAILS)))
    sys.exit(1)
print("All Section 3 (n = 2) checks passed.")

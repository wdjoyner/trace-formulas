# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact checks of local formulas in "Direct comparison of SL(2) with its metaplectic cover", Draft 5.

Checked:
  * Lemma 4.3 (cocycle on the split torus; conjugation by w), over Q_3,
    Q_5, Q_2 and R, on sample rational/real elements.
  * Lemma 4.4 (genuine characters of the cover of A), over Q_3 and Q_5.
  * The examples (3,3)_3 = -1, (5,5)_5 = 1, (-1,-1)_2 = -1, and the
    Q_3 example after Proposition 4.14.
  * Lemma 4.17 (real torus matching factor -i) via the character relations.
  * Lemma 4.31 (real discrete-series matchings): the table of integrands.
  * The fixed-point counts and the Fresnel integral used in two examples.
Run: python3 local_formulas_check.py   (needs SymPy; exits nonzero on failure)
"""
import itertools
import sys
from fractions import Fraction as Q

import sympy as sp

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)


# ---------------------------------------------------------------- Hilbert symbols
def split(a, p):
    a = Q(a)
    v = 0
    n, d = a.numerator, a.denominator
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v, Q(n, d)


def unit_mod(u, m):
    return (u.numerator * pow(u.denominator, -1, m)) % m


def legendre(u, p):
    r = pow(unit_mod(u, p), (p - 1) // 2, p)
    return -1 if r == p - 1 else 1


def hilbert(a, b, p):
    """Quadratic Hilbert symbol (a,b)_p for nonzero rationals a, b."""
    if p == "R":
        return -1 if (a < 0 and b < 0) else 1
    al, u = split(a, p)
    be, v = split(b, p)
    if p != 2:
        e = (p - 1) // 2
        return (-1) ** (al * be * e) * legendre(u, p) ** be * legendre(v, p) ** al
    u8, v8 = unit_mod(u, 8), unit_mod(v, 8)
    eps = lambda x: ((x - 1) // 2) % 2
    om = lambda x: ((x * x - 1) // 8) % 2
    return (-1) ** ((eps(u8) * eps(v8) + al * om(v8) + be * om(u8)) % 2)


# ---------------------------------------------------------------- the cover
def mat_mul(g, h):
    return ((g[0][0] * h[0][0] + g[0][1] * h[1][0], g[0][0] * h[0][1] + g[0][1] * h[1][1]),
            (g[1][0] * h[0][0] + g[1][1] * h[1][0], g[1][0] * h[0][1] + g[1][1] * h[1][1]))


def mat_inv(g):
    (a, b), (c, d) = g
    return ((d, -b), (-c, a))  # determinant 1


def xg(g):
    return g[1][0] if g[1][0] != 0 else g[1][1]


def beta(g1, g2, p):
    g = mat_mul(g1, g2)
    return hilbert(Q(xg(g)) / Q(xg(g1)), Q(xg(g)) / Q(xg(g2)), p)


def mul(e1, e2, p):
    return (mat_mul(e1[0], e2[0]), beta(e1[0], e2[0], p) * e1[1] * e2[1])


def inv(e, p):
    g = e[0]
    gi = mat_inv(g)
    return (gi, beta(g, gi, p) * e[1])


def a_(x):
    x = Q(x)
    return ((x, Q(0)), (Q(0), 1 / x))


W = ((Q(0), Q(-1)), (Q(1), Q(0)))

SAMPLES = [Q(n, d) for n in (1, -1, 2, -2, 3, -3, 5, -5, 6, -7, 10, -15, 45) for d in (1, 2, 3, 5)]

for p in (3, 5, 2, "R"):
    for x, y in itertools.product(SAMPLES[:20], SAMPLES[:20]):
        check(beta(a_(x), a_(y), p) == hilbert(x, y, p), f"Lemma 5.3(a) p={p} x={x} y={y}")
    for x in SAMPLES:
        c = mul(mul((W, 1), (a_(x), 1), p), inv((W, 1), p), p)
        check(c[0] == a_(1 / x) and c[1] == 1, f"Lemma 5.3(b) p={p} x={x}")

check(hilbert(3, 3, 3) == -1, "(3,3)_3 = -1")
check(hilbert(5, 5, 5) == 1, "(5,5)_5 = 1")
check(hilbert(-1, -1, 2) == -1, "(-1,-1)_2 = -1")
I2 = ((Q(1), Q(0)), (Q(0), Q(1)))
mI = ((Q(-1), Q(0)), (Q(0), Q(-1)))
check(mul((mI, 1), (mI, 1), 2) == (I2, -1), "(-I,1)^2 = (I,-1) over Q_2")

# ---------------------------------------------------------------- Lemma 5.4
for p in (3, 5):
    vp = Q(p)
    for eps in (1j, -1j, 1, -1):
        # chi_1 = 1, so (5.x) requires eps^2 = (p,p)^{-1}
        if abs(eps * eps - hilbert(p, p, p)) > 1e-12:
            continue

        def psi(x):
            v, _ = split(x, p)
            return 1 if v % 2 == 0 else eps * hilbert(x, vp, p)

        for x, y in itertools.product(SAMPLES, SAMPLES):
            lhs = psi(x * y)
            rhs = hilbert(x, y, p) * psi(x) * psi(y)
            check(abs(lhs - rhs) < 1e-12, f"Lemma 5.4 p={p} eps={eps} x={x} y={y}")

# Q_3 example: eta_3 = i, phibar(a(3u),1) = eta^{-1} (3u,3) = i (u/3)
for u in (Q(1), Q(2), Q(4), Q(5), Q(7, 2)):
    val = (1 / 1j) * hilbert(3 * u, 3, 3)
    check(abs(val - 1j * legendre(u, 3)) < 1e-12, f"Q_3 example u={u}")
    # Fourier term: eps * phibar * (x,varpi) with eps = i*vartheta, vartheta = 1
    term = 1j * val * hilbert(3 * u, 3, 3)
    check(abs(term - 1) < 1e-12, f"Q_3 Fourier term u={u}")

# ---------------------------------------------------------------- Lemma 5.15
# second terms: eps*phi = eta*phibar with eta = eps*i  =>  phibar = -i*phi
for eps in (1, -1):
    eta = eps * 1j
    check(abs(eps / eta - (-1j)) < 1e-12, f"Lemma 5.15 eps={eps}")
check(all(abs((e * 1j) ** 2 + 1) < 1e-12 for e in (1, -1)), "real genuine characters: eta^2 = -1")

# ---------------------------------------------------------------- Lemma 5.29
th, k = sp.symbols("theta k", real=True)
E = sp.exp
D = lambda t: E(sp.I * t) - E(-sp.I * t)
hol = lambda t: -E(sp.I * (k / 2 - 1) * t) / D(t)
anti = lambda t: E(-sp.I * (k / 2 - 1) * t) / D(t)
c = E(sp.I * th) + E(-sp.I * th)
pim = lambda m: -sp.sign(m) * E(sp.I * m * th) / D(th)
pi0 = lambda e: -e / D(th)
facs = {"even": 1, "+odd": E(-sp.I * th), "-odd": E(sp.I * th)}
expected = {("even", "hol"): lambda kk: pim(kk - 2), ("even", "anti"): lambda kk: pim(-(kk - 2)),
            ("+odd", "hol"): lambda kk: pim(kk - 3) if kk > 3 else pi0(1),
            ("+odd", "anti"): lambda kk: pim(-(kk - 1)),
            ("-odd", "hol"): lambda kk: pim(kk - 1),
            ("-odd", "anti"): lambda kk: pim(-(kk - 3)) if kk > 3 else pi0(-1)}
for (name, lab), exp in expected.items():
    rep = hol if lab == "hol" else anti
    for kk in (3, 5, 7, 13):
        integrand = (rep(2 * th) * c * facs[name]).subs(k, kk)
        diff = sp.simplify(sp.expand(integrand - exp(kk)))
        check(diff == 0, f"Lemma 5.29 {name} {lab} k={kk}")

# ---------------------------------------------------------------- small examples
for q in (3, 5, 7, 9, 25):
    check(Q(q + 1 - 2, q - 1) == 1, f"fixed points m=0 q={q}")
    check(Q(q * q + q - 2, q - 1) == q + 2, f"fixed points m=1 q={q}")
x = sp.symbols("x", real=True)
fres = sp.integrate(sp.exp(sp.I * x ** 2), (x, -sp.oo, sp.oo))
check(sp.simplify(fres - sp.exp(sp.pi * sp.I / 4) * sp.sqrt(sp.pi)) == 0, "Fresnel integral")

print("local_formulas_check: %d failure(s)" % len(FAIL))
sys.exit(1 if FAIL else 0)

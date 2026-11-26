# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Checks of Chapter 8 (the direct comparison with SL(2)) of the revised
"hitch-hiker's guide to the metaplectic trace formula for SL(2)", for k = Q.

Checks (exact Hilbert symbols; Weil indices as finite Gauss sums):
  * Lemma 8.1: Delta_psi(a(t), 1) = chi_psi(a(t), 1)^-1 at v = oo, 2, 3, 5, 7,
    for random rational t (this is Lemma 7.3(c) again, in the form used);
  * Lemma 8.4 (product formula): for random regular gamma in SL(2,Q) with
    lower left entry c != 0, the product over all places of
    Delta_{psi_v}(gamma, 1) (beta_v-model) is 1;
  * Proposition 8.6(a), (d): for odd p, gamma in SL(2,Z_p) regular and u a nonsquare unit,
    Ad(d_u) carries the K*-lift (gamma, kappa(gamma)) to the K*-lift of
    d_u gamma d_u^-1; if ord_p(2 + tr gamma) is odd, then
    Delta(K*-lift of d_u gamma d_u^-1) = - Delta(K*-lift of gamma), and the
    value is +-i for p = 3 mod 4 and +-1 for p = 1 mod 4; if 2 + tr gamma is
    a unit, the value is 1;
  * Examples 8.D and 8.E: gamma = [[2,-1],[3,-1]], S = {oo, 2}: the values
    1, i, -i of Delta_v(gamma, 1) at v = oo, 2, 3, kappa_3(gamma) = -1, the
    value i of Delta_3 on the K*-lift, and so epsilon^S(gamma) = -i; for
    gamma' = d_{-1} gamma d_{-1}^-1 the value is -i and epsilon^S = i.
"""
import cmath
import random
import sys
from fractions import Fraction as Fr

from padic_lib import hilbert, vp, INF
from cover_lib import M2, mul, inv, a_, n_, W, I2, beta, gamma, kappa, chi_psi, in_K

random.seed(20261126)
FAILS = []


def report(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def close(u, w, tol=1e-9):
    return abs(u - w) < tol


def tr(g):
    return g[0][0] + g[1][1]


def bmul(x, y, v):
    (g, z), (h, e) = x, y
    return (mul(g, h), beta(g, h, v) * z * e)


def binv(x, v):
    g, z = x
    gi = inv(g)
    return (gi, beta(g, gi, v) * z)


def bconj(y, x, v):
    return bmul(bmul(y, x, v), binv(y, v), v)


def Ad_delta(a, x, v):
    """Lemma 7.1(c)."""
    g, z = x
    c, d = g[1]
    va = hilbert(a, d, v) if c == 0 else 1
    return (mul(mul(M2(a, 0, 0, 1), g), M2(Fr(1) / a, 0, 0, 1)), z * va)


def Delta(x, v):
    """Formula (7.4), for lower left entry c != 0."""
    g, z = x
    c = g[1][0]
    D = 2 + tr(g)
    assert c != 0 and D != 0
    return z * hilbert(c, D, v) * gamma(D, v) / gamma(1, v)


def Delta_any(x, v):
    """Delta_psi on any regular element: conjugate until c != 0."""
    g, z = x
    if g[1][0] != 0:
        return Delta(x, v)
    for y in [(n_(1), 1), (W, 1), (mul(W, n_(1)), 1), (mul(n_(2), W), 1)]:
        x2 = bconj(y, x, v)
        if x2[0][1][0] != 0:
            return Delta(x2, v)
    raise ValueError


def primes_of(*nums):
    ps = set()
    for q in nums:
        q = Fr(q)
        for m in (abs(q.numerator), q.denominator):
            d = 2
            while d * d <= m:
                while m % d == 0:
                    ps.add(d)
                    m //= d
                d += 1
            if m > 1:
                ps.add(m)
    return ps


def rr(big=7):
    while True:
        r = Fr(random.randint(-big, big), random.randint(1, big))
        if r != 0:
            return r


def rand_sl2():
    g = I2
    for _ in range(random.randint(2, 3)):
        g = mul(mul(mul(g, n_(rr())), W), a_(rr()))
    return mul(g, n_(rr()))


# ------------------------------------------------------------ Lemma 8.1
ok = True
for v in [INF, 2, 3, 5, 7]:
    for _ in range(25):
        t = rr(30)
        if t * t == 1:
            continue
        ok &= close(Delta_any((a_(t), 1), v), 1 / chi_psi(t, 1, v))
report("Lemma 8.1: Delta_psi(a(t),1) = chi_psi(a(t),1)^-1 at oo, 2, 3, 5, 7", ok)

# ------------------------------------------------------------ Lemma 8.3
ok, count = True, 0
while count < 60:
    g = rand_sl2()
    c, D = g[1][0], 2 + tr(g)
    if c == 0 or D == 0 or tr(g) ** 2 == 4:
        continue
    ps = sorted(primes_of(c, D, 2))
    if max(ps) > 43:   # keep the Gauss sums small
        continue
    count += 1
    prod = Delta((g, 1), INF)
    for p in ps:
        prod *= Delta((g, 1), p)
    ok &= close(prod, 1)
report("Lemma 8.4: prod_v Delta_v(gamma,1) = 1 for 60 regular gamma in SL(2,Q) (primes up to 43)", ok)

# ------------------------------------------------------------ Lemma 8.5
def nonsquare_unit(p):
    return next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) == p - 1)


def rand_K(p, cond):
    """Random element of SL(2,Z) (hence of K_p) satisfying cond."""
    while True:
        g = I2
        for _ in range(random.randint(2, 4)):
            g = mul(mul(g, n_(random.randint(-6, 6))), W)
        g = mul(g, n_(random.randint(-6, 6)))
        if cond(g):
            return g


for p in [3, 5, 7, 11, 13]:
    u = nonsquare_unit(p)
    ok_lift, ok_sign, ok_val, ok_unit = True, True, True, True
    n_odd = 0
    while n_odd < 40:
        g = rand_K(p, lambda g: g[1][0] != 0 and 2 + tr(g) != 0 and tr(g) ** 2 != 4)
        D = 2 + tr(g)
        x = (g, kappa(g, p))
        y = Ad_delta(u, x, p)
        ok_lift &= (y[1] == kappa(y[0], p)) and in_K(y[0], p)
        if vp(D, p) == 0:
            ok_unit &= close(Delta(x, p), 1)
        if vp(D, p) % 2 == 1:
            n_odd += 1
            d0, d1 = Delta(x, p), Delta(y, p)
            ok_sign &= close(d1, -d0)
            if p % 4 == 3:
                ok_val &= close(d0 * d0, -1)
            else:
                ok_val &= close(d0 * d0, 1)
    report("Proposition 8.6, p = %d: Ad(d_u) preserves K*" % p, ok_lift)
    report("Proposition 8.6, p = %d: Delta = 1 on K* when 2 + tr is a unit" % p, ok_unit)
    report("Proposition 8.6, p = %d: Delta changes sign under d_u when ord(2 + tr) is odd" % p, ok_sign)
    report("Proposition 8.6, p = %d: the value is %s" % (p, "+-i" if p % 4 == 3 else "+-1"), ok_val)

# ------------------------------------------------------------ Example 8.B
g = M2(2, -1, 3, -1)
vals = {v: Delta((g, 1), v) for v in [INF, 2, 3]}
report("Example 8.D: Delta_oo(gamma,1) = 1", close(vals[INF], 1), str(vals[INF]))
report("Example 8.D: Delta_2(gamma,1) = i", close(vals[2], 1j), str(vals[2]))
report("Example 8.D: Delta_3(gamma,1) = -i", close(vals[3], -1j), str(vals[3]))
report("Example 8.E: kappa_3(gamma) = -1", kappa(g, 3) == -1)
lift3 = Delta((g, kappa(g, 3)), 3)
report("Example 8.E: Delta_3 on the K*-lift is i, so epsilon^S = -i", close(lift3, 1j), str(lift3))
g2 = Ad_delta(-1, (g, kappa(g, 3)), 3)
report("Example 8.E: Ad(d_-1) of the K*-lift is the K*-lift of gamma'", g2[1] == kappa(g2[0], 3))
report("Example 8.E: Delta_3 on the K*-lift of gamma' is -i, so epsilon^S = i", close(Delta(g2, 3), -1j))
report("Example 8.E: (-1,-3)_3 = -1", hilbert(-1, -3, 3) == -1)
report("Example 8.D: product over oo, 2, 3 is 1", close(vals[INF] * vals[2] * vals[3], 1))

print()
print("%d check(s) failed" % len(FAILS))
sys.exit(1 if FAILS else 0)

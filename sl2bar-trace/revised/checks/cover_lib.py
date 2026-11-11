# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Shared helpers for the sl2bar-trace checks from Section 6 on: exact 2x2
rational matrices, Kubota's cocycle beta_v and the cocycle sigma_v of (2.10),
the product in the sigma_v-model of the double cover, the Weil index gamma_v,
Weil's character chi_psi, and the value of the K*-spherical vector of
I(chi_psi chi, lambda) on (w,1)^-1 (n(y),1).

These are the functions of sec5_n2_check.py, copied here unchanged so that
later scripts can import them without re-running the Section 5 checks."""
import cmath
import random
from fractions import Fraction as Fr

from padic_lib import hilbert, vp, unit_mod, legendre, INF

random.seed(20261113)


# ---------------------------------------------------------------- matrices
def M2(a, b, c, d):
    return ((Fr(a), Fr(b)), (Fr(c), Fr(d)))


def mul(g, h):
    return ((g[0][0] * h[0][0] + g[0][1] * h[1][0], g[0][0] * h[0][1] + g[0][1] * h[1][1]),
            (g[1][0] * h[0][0] + g[1][1] * h[1][0], g[1][0] * h[0][1] + g[1][1] * h[1][1]))


def inv(g):
    (a, b), (c, d) = g
    return ((d, -b), (-c, a))


def a_(t):
    return M2(t, 0, 0, Fr(1) / Fr(t))


def n_(u):
    return M2(1, u, 0, 1)


W = M2(0, -1, 1, 0)
I2 = M2(1, 0, 0, 1)


def xg(g):
    c, d = g[1]
    return c if c != 0 else d


def beta(g1, g2, v):
    x1, x2, x3 = xg(g1), xg(g2), xg(mul(g1, g2))
    return hilbert(x3 / x1, x3 / x2, v)


def in_K(g, p):
    return all(e == 0 or vp(e, p) >= 0 for row in g for e in row)


def kappa(g, v):
    if v == INF or v == 2 or not in_K(g, v):
        return 1
    c, d = g[1]
    if c != 0 and vp(c, v) > 0:
        return hilbert(c, d, v)
    return 1


def sigma(g1, g2, v):
    """The cocycle sigma_v = beta_v * kappa_v(g1) kappa_v(g2) kappa_v(g1 g2) of (2.10)."""
    return beta(g1, g2, v) * kappa(g1, v) * kappa(g2, v) * kappa(mul(g1, g2), v)


def cmul(x, y, v):
    """Product in the sigma_v-model of the cover."""
    (g, z), (h, e) = x, y
    return (mul(g, h), sigma(g, h, v) * z * e)


def cinv(x, v):
    g, z = x
    gi = inv(g)
    return (gi, sigma(g, gi, v) * z)


def rand_rat(big=60):
    while True:
        r = Fr(random.randint(-big, big), random.randint(1, big))
        if r != 0 and r * r != 1:
            return r


# ---------------------------------------------------------------- Weil index
def gamma(a, v):
    """Weil index of x -> psi_v(a x^2) (psi_oo(x) = exp(-2 pi i x), psi_p
    standard), normalized as in (3.5); computed as a finite Gauss sum. Same
    algorithm as checks/sec3_n2_check.py."""
    a = Fr(a)
    if v == INF:
        return cmath.exp(-1j * cmath.pi / 4 * (1 if a > 0 else -1))
    p = v
    al = vp(a, p)
    a = a / Fr(p) ** (2 * (al // 2))
    al = vp(a, p)
    if p != 2:
        u0 = unit_mod(a, p, 1)
        nr = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) == p - 1)
        a = Fr(p) ** al * (1 if pow(u0, (p - 1) // 2, p) == 1 else nr)
    ordtwo = 1 if p == 2 else 0
    M = 1 if p != 2 else (al + 3 + 2 * ordtwo) // 2 + 1
    e = 2 * M - al
    R = e + ordtwo
    mod = p ** e
    u = unit_mod(a, p, e)
    s = 0
    for y in range(p ** R):
        s += cmath.exp(2j * cmath.pi * ((u * y * y) % mod) / mod)
    integral = p ** M * s / p ** R
    absval = float(Fr(p) ** (-vp(2 * a, p)))
    return integral * absval ** 0.5


def chi_psi(t, z, v):
    """chi_{psi,v}(a(t), z) = z gamma_v(t) / gamma_v(1)."""
    return z * gamma(t, v) / gamma(1, v)


# ---------------------------------------------------------------- Lemma 5.6(b)
def iwasawa_value(y, p, lam, z, cover=True):
    """phi_0((w,1)^-1 (n(y),1)) for the K*-spherical vector phi_0 of
    I(chi_psi chi, lambda) on the double cover (cover=True), or of
    I(chi, lambda) on SL(2) (cover=False); chi unramified, chi(p) = z.
    phi((n,1)(a(t),e)(k,1)) = e mu(a(t),1) |t|^(lambda+1)."""
    y = Fr(y)
    if cover:
        g = cmul(cinv((W, 1), p), (n_(y), 1), p)
    else:
        g = (mul(inv(W), n_(y)), 1)
    mat, eps = g
    if vp(y, p) >= 0:
        assert in_K(mat, p)
        return eps  # (k, eps) = (1, eps)(k, 1)
    t = -Fr(1) / y
    n0, a0, k0 = n_(t), a_(t), M2(1, 0, Fr(1) / y, 1)
    assert mul(mul(n0, a0), k0) == mat and in_K(k0, p)
    if cover:
        prod = cmul(cmul((n0, 1), (a0, 1), p), (k0, 1), p)
        corr = eps * prod[1]          # g = (n0,1)(a0,1)(k0,1) * (1, corr)
        muval = chi_psi(t, 1, p) * z ** vp(t, p)
    else:
        corr = 1
        muval = z ** vp(t, p)
    absval = float(Fr(p) ** (-vp(t, p)))
    return corr * muval * absval ** (lam + 1)

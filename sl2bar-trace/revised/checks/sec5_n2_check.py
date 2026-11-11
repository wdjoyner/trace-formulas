# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Checks of Section 5 (the spectral side) of the revised "hitch-hiker's guide
to the metaplectic trace formula for SL(2)", for k = Q.

Checks:
  * the Weyl element acts on the cover of A by (a(t), z) -> (a(1/t), z):
    (w,1)(a(t),z)(w,1)^-1 = (a(1/t), z) in the sigma_v-model at v = oo, 2, 3,
    5, 7, on random t (Lemma 5.3(a));
  * the group inverse is (a(t),z)^-1 = (a(1/t), (t,-1)_v z), so w-conjugation
    is not inversion; and Weil's character satisfies chi_psi^w = chi_psi, i.e.
    gamma_v(1/t) = gamma_v(t), at v = oo, 2, 3, 5, 7 (Lemma 5.3(b)-(c));
  * for mu = chi_psi * chi, mu^w = chi_psi * chi^-1 (Lemma 5.3(c)), checked
    on the local components at v = 3, 5, 7 for unramified chi;
  * the unramified intertwining integral on the double cover at p = 3, 5, 7:
    for the K*-spherical vector of I(chi_psi chi, lambda), chi unramified
    with chi(p) = z,
        M(lambda) phi_0 = (1 - z^2 p^(-1-2 lambda)) / (1 - z^2 p^(-2 lambda)) phi_0,
    i.e. L(2 lambda, chi^2) / L(2 lambda + 1, chi^2); computed by an explicit
    Iwasawa decomposition of w^-1 n(y) in the cover, shell by shell
    (Lemma 5.6(b)): on an even shell the integrand is chi(p)^m |y|^(-l-1), on
    an odd shell it is a constant times the Legendre symbol of the unit part
    of y, so the odd shells cancel;
  * for comparison, the same integral for SL(2) itself (no cover, character
    chi of A): L(lambda, chi) / L(lambda + 1, chi);
  * the limit defining M_B^T (Arthur's formula, Theorem 5.14): with
    vol(a / Z alpha^v) = d and theta(zeta) = zeta(alpha^v) = d zeta,
        d * lim [e^{zeta T} - e^{-zeta T} M(l)^-1 M(l + zeta)] / (d zeta)
          = 2T - M(l)^-1 M'(l)
    for d = 1, 2, 3 (symbolic, M(l) = exp(l X) for a generic matrix X); the
    1995 identification (zeta(T) = 2 zeta T, zeta(alpha^v) = 2 zeta, vol 1)
    gives 2T - (1/2) M^-1 dM/dzeta, not 4T - M^-1 M' (referee item II.11);
  * the diagonal limit of the Maass-Selberg relation (Lemma 5.13/Thm 5.14) at
    lambda' -> lambda on i R, for a unitary M(it) = exp(i t X), X Hermitian:
    the limit is 2T <phi, phi'> - <phi, M^-1 M' phi'> (numerical);
  * the cross terms for a ramified class (Theorem 5.14(c)): with
    F(t) = exp(-t^2)(1 + t/3), the integral
        (1/2)(1/2 pi) PV int [F(-t) e^{2itT} - F(t) e^{-2itT}] / (2it) dt
    tends to F(0)/4 as T -> oo (numerical);
  * the residue 2/pi^2 at lambda = 1/2 of m^S(lambda) = (1 - 2^-2l) zeta(2l) /
    ((1 - 2^(-1-2l)) zeta(2l+1)) for S = {oo, 2} (Example 5.B);
  * the two local facts behind Proposition 5.17 (the T-coefficients of the
    two sides agree), at v = R for f = exp(-pi ||g||^2): the Abel transform
    satisfies |t| F(a(t)) = |1/t| F(a(1/t)), and the orbital integral of
    a(t) is |1 - t^-2|^-1 F(a(t)).
"""
import cmath
import math
import random
import sys
from fractions import Fraction as Fr

import mpmath as mp
import sympy as sp

from padic_lib import hilbert, vp, unit_mod, legendre, INF

random.seed(20261112)
mp.mp.dps = 30
FAILS = []


def report(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


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


PLACES = [INF, 2, 3, 5, 7]

# ---------------------------------------------------------------- Lemma 5.3(a)
for v in PLACES:
    wt = (W, 1)
    ok = True
    for _ in range(300):
        t = rand_rat()
        for z in (1, -1):
            lhs = cmul(cmul(wt, (a_(t), z), v), cinv(wt, v), v)
            ok &= lhs == (a_(Fr(1) / t), z)
    report("Lemma 5.3(a): (w,1)(a(t),z)(w,1)^-1 = (a(1/t),z), v=%s" % v, ok)

for v in PLACES:
    ok = True
    for _ in range(300):
        t = rand_rat()
        ok &= cinv((a_(t), 1), v) == (a_(Fr(1) / t), hilbert(t, -1, v))
    report("Lemma 5.3(b): (a(t),1)^-1 = (a(1/t),(t,-1)_v), v=%s" % v, ok)


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


for v in PLACES:
    ok = True
    for _ in range(40):
        t = rand_rat(30)
        ok &= abs(gamma(Fr(1) / t, v) - gamma(t, v)) < 1e-9
        # mu^w(a(t),1) = mu(a(1/t),1) equals mu(a(t),1)^-1 (t,-1)_v for mu = chi_psi
        lhs = chi_psi(Fr(1) / t, 1, v)
        rhs = hilbert(t, -1, v) / chi_psi(t, 1, v)
        ok &= abs(lhs - rhs) < 1e-9
    report("Lemma 5.3(c): chi_psi^w = chi_psi (gamma_v(1/t) = gamma_v(t)), v=%s" % v, ok)

for p in (3, 5, 7):
    ok = True
    zc = cmath.exp(0.7j)   # chi(p) for an unramified chi
    for _ in range(40):
        t = rand_rat(30)
        mu = lambda s: chi_psi(s, 1, p) * zc ** vp(s, p)
        muw = mu(Fr(1) / t)
        target = chi_psi(t, 1, p) * zc ** (-vp(t, p))
        ok &= abs(muw - target) < 1e-9
    report("Lemma 5.3(c): (chi_psi chi)^w = chi_psi chi^-1, p=%d" % p, ok)


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


def intertwining(p, lam, z, cover=True, mmax=40):
    """int_{Q_p} phi_0(w^-1 n(y)) dy, shell by shell (exact average of the
    integrand over each shell |y| = p^m, which depends only on u mod p)."""
    total = iwasawa_value(Fr(1, 1), p, lam, z, cover)   # the region |y| <= 1 (vol 1)
    shells = []
    for m in range(1, mmax + 1):
        avg = sum(iwasawa_value(Fr(u, p ** m), p, lam, z, cover) for u in range(1, p)) / (p - 1)
        shells.append(avg)
        total += avg * p ** m * (1 - 1 / p)
    return total, shells


for p in (3, 5, 7):
    lam, z = 0.37 + 0.21j, cmath.exp(0.9j) * 0.8
    val, shells = intertwining(p, lam, z)
    expect = (1 - z ** 2 * p ** (-1 - 2 * lam)) / (1 - z ** 2 * p ** (-2 * lam))
    report("Lemma 5.6(b): unramified M(lambda) on the cover = L(2l,chi^2)/L(2l+1,chi^2), p=%d" % p,
           abs(val - expect) < 1e-9, "%.12f%+.12fj" % (val.real, val.imag))
    odd_zero = all(abs(shells[m]) < 1e-12 for m in range(0, len(shells), 2))
    report("Lemma 5.6(b): the odd shells cancel, p=%d" % p, odd_zero)
    # the region |y| <= 1 contributes exactly 1 (the lift of w^-1 n(y) is in K*)
    ok = all(iwasawa_value(Fr(u, 1) * p ** j, p, lam, z) == 1 for u in range(1, 2 * p) for j in range(3))
    report("Lemma 5.6(b): integrand = 1 on |y| <= 1, p=%d" % p, ok)
    # shell structure: on |y| = p^m the integrand is z^m |y|^(-lambda-1) times
    # 1 (m even) or a constant times the Legendre symbol of the unit part (m odd)
    ok = True
    for m in range(1, 6):
        vals = [iwasawa_value(Fr(u, p ** m), p, lam, z) / (z ** m * p ** (-m * (lam + 1)))
                for u in range(1, p)]
        if m % 2 == 0:
            ok &= all(abs(x - 1) < 1e-12 for x in vals)
        else:
            c0 = vals[0]
            ok &= abs(abs(c0) - 1) < 1e-12 and all(
                abs(vals[u - 1] - c0 * legendre(u, p)) < 1e-12 for u in range(1, p))
    report("Lemma 5.6(b): even shells give z^m |y|^(-l-1), odd shells c (u/p) z^m |y|^(-l-1), p=%d" % p, ok)
    val0, _ = intertwining(p, lam, z, cover=False)
    expect0 = (1 - z * p ** (-1 - lam)) / (1 - z * p ** (-lam))
    report("comparison: SL(2), no cover: L(l,chi)/L(l+1,chi), p=%d" % p, abs(val0 - expect0) < 1e-9)


# ---------------------------------------------------------------- Theorem 5.14
zeta, T, l = sp.symbols("zeta T l")
# Work with M(l + zeta) = M(l) (1 + zeta Y + O(zeta^2)) where Y = M^-1 M'(l).
Y = sp.Matrix(2, 2, sp.symbols("y0:4"))
MinvM = lambda s: sp.eye(2) + s * Y + s ** 2 * sp.Matrix(2, 2, sp.symbols("q0:4"))
for d in (1, 2, 3):
    vol = d
    theta = lambda s: d * s
    expr = vol * (sp.exp(zeta * T) * sp.eye(2) / theta(zeta)
                  + sp.exp(-zeta * T) * MinvM(zeta) / theta(-zeta))
    lim = expr.applyfunc(lambda e: sp.limit(e, zeta, 0))
    report("Theorem 5.14: Arthur's limit = 2T - M^-1 M' (vol = d, theta = d zeta), d=%d" % d,
           sp.simplify(lim - (2 * T * sp.eye(2) - Y)) == sp.zeros(2))
# 1995 identification: zeta(T) = 2 zeta T, zeta(alpha^v) = 2 zeta, vol(R/Z) = 1;
# M(l + zeta) with l in the 1995 coordinate, derivative d/dzeta.
expr95 = (sp.exp(2 * zeta * T) * sp.eye(2) / (2 * zeta)
          + sp.exp(-2 * zeta * T) * MinvM(zeta) / (-2 * zeta))
lim95 = expr95.applyfunc(lambda e: sp.limit(e, zeta, 0))
report("item II.11: the 1995 normalization gives 2T - (1/2) M^-1 dM/dzeta",
       sp.simplify(lim95 - (2 * T * sp.eye(2) - Y / 2)) == sp.zeros(2))
report("item II.11: ... and not 4T - M^-1 M'",
       sp.simplify(lim95 - (4 * T * sp.eye(2) - Y)) != sp.zeros(2))

# ---------------------------------------------------------------- Lemma 5.13/Thm 5.14
# Diagonal limit of the Maass-Selberg expression with a unitary M(it) = exp(i t X).
mp.mp.dps = 30
Xh = mp.matrix([[0.3, 0.2 - 0.5j], [0.2 + 0.5j, -0.7]])  # Hermitian


def Munit(lam):
    """M(lambda) = expm(lambda X): unitary on i R, with M(-lambda) M(lambda) = 1."""
    return mp.expm(lam * Xh)


def ip(u, v):
    return sum(u[i] * mp.conj(v[i]) for i in range(len(u)))


def ms(lam, lamp, phi, phip, Tv):
    """Right-hand side of the Maass-Selberg relation of Lemma 5.13 for a
    ramified class (mu = mu^w), all four terms; inner products in C^2."""
    Ml, Mlp = Munit(lam), Munit(lamp)
    a = lam + mp.conj(lamp)
    b = -lam + mp.conj(lamp)
    return (ip(phi, phip) * mp.e ** (a * Tv) / a
            - ip(Ml * phi, Mlp * phip) * mp.e ** (-a * Tv) / a
            + ip(Ml * phi, phip) * mp.e ** (b * Tv) / b
            - ip(phi, Mlp * phip) * mp.e ** (-b * Tv) / b)


phi = mp.matrix([0.4 + 0.1j, -0.3 + 0.8j])
phip = mp.matrix([1.1 - 0.2j, 0.5j])
t0, Tv, h = mp.mpf("0.6"), mp.mpf("1.3"), mp.mpf("1e-12")
val = ms(1j * t0, 1j * (t0 + h), phi, phip, Tv)
Minv = Munit(1j * t0) ** -1
Mder = Xh * Munit(1j * t0)
diag = 2 * Tv * ip(phi, phip) - ip(phi, Minv * Mder * phip)
cross = (ip(phi, Munit(1j * t0) * phip) * mp.e ** (2j * t0 * Tv)
         - ip(Munit(1j * t0) * phi, phip) * mp.e ** (-2j * t0 * Tv)) / (2j * t0)
report("Lemma 5.13/Thm 5.14: diagonal limit = 2T<phi,phi'> - <phi, M^-1 M' phi'> + cross terms",
       abs(val - (diag + cross)) < 1e-8, mp.nstr(abs(val - (diag + cross)), 3))
herm = Minv * Mder
report("Lemma 5.13/Thm 5.14: M(it)^-1 M'(it) is self-adjoint",
       mp.mnorm(herm - herm.transpose_conj(), 1) < 1e-20)

# ---------------------------------------------------------------- cross terms
F = lambda t: mp.e ** (-t * t) * (1 + t / 3)


def cross_integral(Tv):
    g = lambda t: (F(-t) * mp.e ** (2j * t * Tv) - F(t) * mp.e ** (-2j * t * Tv)) / (2j * t)
    # g is even and regular at 0, so the PV integral is 2 int_0^oo g;
    # tanh-sinh never evaluates the endpoint 0
    pts = [mp.mpf(j) / 4 for j in range(0, 49)]
    val = 2 * mp.quad(g, pts)
    return val / 2 / (2 * mp.pi)


vals = [cross_integral(mp.mpf(Tv)) for Tv in (2, 4, 8)]
report("Theorem 5.14(c): cross terms -> F(0)/4 as T -> oo",
       abs(vals[-1] - F(0) / 4) < 1e-10 and abs(vals[-1].imag) < 1e-12,
       ", ".join(mp.nstr(v.real, 12) for v in vals))

# ---------------------------------------------------------------- Prop. 5.17
# Abel transform at R: F(a(t)) = int_K int_N f(k^-1 a(t) n k) dn dk for the
# bi-K-invariant f(g) = exp(-pi ||g||^2) on SL(2,R) (K-average is trivial).
# Locally |t| F(a(t)) is w-symmetric; for t in k^x, |t|_A = 1, so globally
# F(a(t)) = F(a(1/t)).
def abel(t):
    t = mp.mpf(t)
    return mp.quad(lambda u: mp.e ** (-mp.pi * (t * t + 1 / (t * t) + (t * u) ** 2)), [-mp.inf, mp.inf])


ok = all(abs(mp.mpf(t) * abel(t) - abel(1 / mp.mpf(t)) / mp.mpf(t)) < 1e-20 for t in ("1.7", "0.4", "3.1"))
report("Prop. 5.17: |t| F(a(t)) = |1/t| F(a(1/t)) (w-symmetry of the Abel transform, v=R)", ok)
# and int_{A\G} f(y^-1 mu y) dy = |1 - t^-2|^-1 F(a(t)) locally (product formula globally)
t = mp.mpf("1.7")
orb = mp.quad(lambda z: mp.e ** (-mp.pi * (t * t + 1 / (t * t) + ((t - 1 / t) * z) ** 2)), [-mp.inf, mp.inf])
report("Prop. 5.17: local orbital integral = |1 - t^-2|^-1 F(a(t)) (v=R)",
       abs(orb - abel(t) / abs(1 - t ** -2)) < 1e-20)

# ---------------------------------------------------------------- Example 5.B
mS = lambda l: (1 - mp.mpf(2) ** (-2 * l)) * mp.zeta(2 * l) / ((1 - mp.mpf(2) ** (-1 - 2 * l)) * mp.zeta(2 * l + 1))
eps = mp.mpf("1e-12")
res = (mS(mp.mpf(1) / 2 + eps) * eps - mS(mp.mpf(1) / 2 - eps) * eps) / 2
report("Example 5.B: Res_{l=1/2} m^S(l) = 2/pi^2 for S = {oo,2}", abs(res - 2 / mp.pi ** 2) < 1e-10,
       mp.nstr(res, 15))
# the formula of Lemma 5.6(c): Res_{s=1} zeta^S(s) / (2 zeta^S(2))
report("Lemma 5.6(c): residue = Res zeta^S(1) / (2 zeta^S(2)) for S = {oo,2}",
       abs(res - (mp.mpf(1) / 2) / (2 * (1 - mp.mpf(1) / 4) * mp.zeta(2))) < 1e-10)

# ---------------------------------------------------------------- Lemma 5.7 (Weil representation on A)
# (2026 referee report, table item on b versus b').  In the beta-model, with the unipotent lifts
# (n,1), (nbar,1): (n(t),1)(nbar(-1/t),1)(n(t),1) = (w(t),1) and (w(t),1)(w(1),1)^{-1} = (a(t),(-1,t)).
def nbar_(c):
    return M2(1, 0, c, 1)


def bmul(x, y, v):
    (g, z), (h, e) = x, y
    return (mul(g, h), beta(g, h, v) * z * e)


ok = True
for v in PLACES:
    for _ in range(60):
        t = rand_rat()
        wt = bmul(bmul((n_(t), 1), (nbar_(-1 / t), 1), v), (n_(t), 1), v)
        w1 = bmul(bmul((n_(1), 1), (nbar_(-1), 1), v), (n_(1), 1), v)
        ok &= wt == (M2(0, t, -1 / t, 0), 1) and w1 == (M2(0, 1, -1, 0), 1)
        w1inv = (inv(w1[0]), beta(w1[0], inv(w1[0]), v))
        ok &= bmul(w1, w1inv, v) == (I2, 1)
        ok &= bmul(wt, w1inv, v) == (a_(t), hilbert(-1, t, v))
report("Lemma 5.7: (w(t),1)(w(1),1)^-1 = (a(t), (-1,t)_v) for the unipotent lifts, all v", ok)
ok = True
for v in PLACES:
    for _ in range(40):
        t = rand_rat()
        r = gamma(t, v) / gamma(1, v)
        ok &= abs(r * r - hilbert(t, -1, v)) < 1e-9
        # hence (-1,t) gamma(t)/gamma(1) = gamma(1)/gamma(t) = chi_psi(a(t),1)^-1
        ok &= abs(hilbert(-1, t, v) * r - 1 / r) < 1e-9
        # and chi_psi^-1 = chi_{psi_{-1}}: gamma(-t)/gamma(-1) = gamma(1)/gamma(t)
        ok &= abs(gamma(-t, v) / gamma(-1, v) - 1 / r) < 1e-9
report("Lemma 5.7: (gamma(t)/gamma(1))^2 = (t,-1)_v and chi_psi^-1 = chi_{psi_-1}, all v", ok)
# the real place: for psi'(x) = exp(2 pi i a x), dω(X - Y) = i(2 pi a x^2 - D^2/(8 pi a)); for a = 1
# the even ground state exp(-2 pi x^2) has eigenvalue i/2, so the lowest K-type of r^+ is +1/2
xs = sp.symbols("x", real=True)
g0 = sp.exp(-2 * sp.pi * xs ** 2)
op = lambda h, a: sp.I * (2 * sp.pi * a * xs ** 2 * h - sp.diff(h, xs, 2) / (8 * sp.pi * a))
report("Lemma 5.7 at v = R: exp(-2 pi x^2) has weight +1/2 for psi' = exp(+2 pi i x)",
       sp.simplify(op(g0, 1) / g0 - sp.I / 2) == 0)
report("Lemma 5.7 at v = R: and weight -1/2 for psi' = exp(-2 pi i x)",
       sp.simplify(op(g0, -1) / g0 + sp.I / 2) == 0)
# with psi_oo = exp(-2 pi i x): chi_psi(a(-1),1) = i = exp(i pi/2), so m_0 = +1/2 goes with b' = -b
report("Lemma 5.7 at v = R: chi_psi(a(-1),1) = i, i.e. m_0 = 1/2 for psi_oo = exp(-2 pi i x)",
       abs(chi_psi(-1, 1, INF) - 1j) < 1e-12)

print()
print("%d check(s) failed" % len(FAILS) if FAILS else "all checks passed")
sys.exit(1 if FAILS else 0)

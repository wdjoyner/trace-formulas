# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Checks of Section 7 (the stable(r) form) of the revised "hitch-hiker's
guide to the metaplectic trace formula for SL(2)", for k = Q.

Checks (v runs over oo, 2, 3, 5, 7; random elements of SL(2,Q), GL(2,Q)):
  * Lemma 7.1: (g, z) -> (d_a g d_a^-1, z v_a(g)), d_a = diag(a, 1),
    v_a(g) = (a, d)_v if c = 0 and 1 otherwise, is a homomorphism for
    Kubota's cocycle; it is conjugation by (d_a, 1) in the cover of GL(2)
    of Section 2.3; its values on N, A, the center and w;
  * Lemma 7.2: if h in GL(2,Q) commutes with a semisimple gamma != -1 of
    SL(2,Q), then Ad(h)(gamma, z) = (gamma, (det h, det(1+gamma))_v z), on
    anisotropic tori T_theta and on the split torus; Ad(h)(-1, z) =
    (-1, (det h, -1)_v z); Example 7.A(d) (Q_3, theta = 3);
  * Lemma 7.3: Delta_psi(g, z) = z (c, D)_v gamma_v(D)/gamma_v(1),
    D = 2 + tr g, is invariant under conjugation in the cover (whenever both
    lower left entries are nonzero), transforms by (a, D)_v under Ad(d_a),
    takes the value gamma_v(1)/gamma_v(t) on the class of (a(t), 1), and
    is 1 on (k_theta, 1), 0 < theta < pi, at v = oo (Example 7.B);
  * Lemma 7.4: the kernels gamma(c)^-1 |c|^(-1/2) psi((a x^2 - 2xy + d y^2)/c)
    compose with Kubota's cocycle: gamma(c3/(c1 c2)) gamma(c3)
    = beta(g1, g2) gamma(c1) gamma(c2);
  * Lemma 7.5' (used for Proposition 7.5): the truncated Gauss integrals over
    p^-M Z_p of psi(a x^2) do not depend on M beyond the stated bound
    (p = 2, 3, 5); Example 7.A(e); formula (7.6) for
    the character of r+ - r- equals gamma(1)^-2 times formula (7.7) for
    the character of omega at (-1,1) x; (7.7) agrees with Thomas's
    gamma(1) gamma(det(g-1)) up to sign;
  * Example 7.C (Proposition 7.5 in a model that can be computed exactly):
    for the Weil representation of SL(2, F_p) on functions on F_p
    (p = 3, 5, 7, 11), the trace of omega(g) P, which is the character of
    (even part) - (odd part), is (det(1+g) / p) when det(1+g) != 0;
  * Lemma 7.5': (a, det(1+gamma)) (a, det(1-gamma)) = (a, -theta) on T_theta;
  * Lemma 7.8: v_A(d^-1 x d) = v_A(x) - H_1(k(x) d) - H_1(k(wx) d);
  * Proposition 7.10 for k = Q, S = {oo, 2}: the local identity
    int h(xi t^2) d*t = (1/2) sum_kappa kappa(xi) int h kappa d*y; the
    identity Z(f, s) = (1/2) sum_b L^S(s, kappa_b) Z_S(Phi_S, kappa_b, s)
    at s = 3 for a test function that is neither even nor unramified; the
    constants rho_S, c_S and L^S(1, kappa_b), and the table of a^G(S, u_xi)
    (Example 7.E), which is invariant under xi -> xi * (unit of Z[1/2]);
  * Proposition 7.12: prod_v gamma_v(b)^2 = 1, so omega(s(-1)) is the
    parity operator, and the count of sign patterns with product +1;
  * Proposition 7.8' (normalizing factors): for F = Q_2 (all characters of
    conductor dividing 32) and F = Q_3, Q_5 (tamely ramified characters),
    the product of the Tate-type integrals that give the inverse local
    coefficients (Szpruch) for (chi, s) and (chi^-1, -s) is a constant times
    L(2s,chi^2) L(-2s,chi^-2) / (L(1+2s,chi^2) L(1-2s,chi^-2)); at the real
    place, the adjoint relation M(pi,it)^* = omega M(pi^w,-it) and the shape
    r = c(omega) h of the explicit factors;
  * the paragraph after Proposition 7.12: for the discrete series of
    Mp(2,R) with weights m, m+2, ... and -m, -m-2, ..., the sum of the
    characters on k_theta is even in theta and the difference is odd.
"""
import cmath
import itertools
import math
import random
import sys
from fractions import Fraction as Fr

import mpmath as mp

from padic_lib import hilbert, vp, legendre, unit_mod, INF
from cover_lib import M2, mul, inv, a_, n_, W, I2, xg, beta, gamma

random.seed(20261111)
mp.mp.dps = 25
FAILS = []
PLACES = [INF, 2, 3, 5, 7]


def report(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


# ------------------------------------------------------------------ helpers
def rr(big=9):
    while True:
        r = Fr(random.randint(-big, big), random.randint(1, big))
        if r != 0:
            return r


def rand_sl2():
    g = I2
    for _ in range(random.randint(2, 4)):
        g = mul(g, n_(rr()))
        g = mul(g, W)
        g = mul(g, a_(rr()))
    return mul(g, n_(rr()))


def det(g):
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


def tr(g):
    return g[0][0] + g[1][1]


def scal(l, g):
    return ((l * g[0][0], l * g[0][1]), (l * g[1][0], l * g[1][1]))


def dl(a):
    return M2(a, 0, 0, 1)


def bmul(x, y, v):
    (g, z), (h, e) = x, y
    return (mul(g, h), beta(g, h, v) * z * e)


def binv(x, v):
    g, z = x
    gi = inv(g)
    return (gi, beta(g, gi, v) * z)


def bconj(y, x, v):
    return bmul(bmul(y, x, v), binv(y, v), v)


def v_a(a, g, v):
    c, d = g[1]
    return hilbert(a, d, v) if c == 0 else 1


def Ad_delta(a, x, v):
    g, z = x
    d = dl(a)
    di = M2(Fr(1) / a, 0, 0, 1)
    return (mul(mul(d, g), di), z * v_a(a, g, v))


def Ad(h, x, v):
    """Ad(h) on the cover of SL(2), h in GL(2,Q): h = d_a h0, h0 in SL(2)."""
    a = det(h)
    h0 = mul(M2(Fr(1) / a, 0, 0, 1), h)
    return Ad_delta(a, bconj((h0, 1), x, v), v)


def sigma_gl2(g1, g2, v):
    x1, x2, x3 = xg(g1), xg(g2), xg(mul(g1, g2))
    return hilbert(x3 / x1, x3 / (x2 * det(g1)), v)


def torus(theta, p, q):
    """z/zbar for z = p + q sqrt(theta), as an element of T_theta(Q)."""
    nz = p * p - theta * q * q
    return M2((p * p + theta * q * q) / nz, 2 * p * q * theta / nz, 2 * p * q / nz, (p * p + theta * q * q) / nz)


def torus1(theta, r, s):
    return M2(r, s * theta, s, r)


def Delta(x, v):
    (g, z) = x
    c = g[1][0]
    D = 2 + tr(g)
    assert c != 0 and D != 0
    return z * hilbert(c, D, v) * gamma(D, v) / gamma(1, v)


def close(u, w, tol=1e-9):
    return abs(u - w) < tol


# ------------------------------------------------------------------ Lemma 7.1
ok_hom = ok_gl2 = True
for v in PLACES:
    for _ in range(150):
        g1, g2, a = rand_sl2(), rand_sl2(), rr()
        if random.random() < 0.3:
            g1 = mul(n_(rr()), a_(rr()))          # c = 0
        if random.random() < 0.3:
            g2 = mul(inv(g1), mul(n_(rr()), a_(rr())))   # g1 g2 upper triangular
        x, y = (g1, 1), (g2, 1)
        lhs = Ad_delta(a, bmul(x, y, v), v)
        rhs = bmul(Ad_delta(a, x, v), Ad_delta(a, y, v), v)
        ok_hom &= lhs == rhs
        d, di = dl(a), M2(Fr(1) / a, 0, 0, 1)
        s = sigma_gl2(d, g1, v) * sigma_gl2(mul(d, g1), di, v) * sigma_gl2(d, di, v)
        ok_gl2 &= s == v_a(a, g1, v)
report("Lemma 7.1(c): (g,z) -> (d_a g d_a^-1, z v_a(g)) is a homomorphism for beta_v", ok_hom)
report("Lemma 7.1(c): it is conjugation by (d_a,1) in the cover of GL(2) (cocycle (2.13))", ok_gl2)

ok = True
for v in PLACES:
    for _ in range(40):
        a, t, u = rr(), rr(), rr()
        ok &= Ad_delta(a, (n_(u), 1), v) == (n_(a * u), 1)
        ok &= Ad_delta(a, (a_(t), 1), v) == (a_(t), hilbert(a, t, v))
        ok &= Ad_delta(a, (scal(-1, I2), 1), v) == (scal(-1, I2), hilbert(a, -1, v))
        ok &= Ad_delta(a, (W, 1), v) == bmul((a_(a), 1), (W, 1), v)
report("Lemma 7.1(d): Ad(d_a) on N, on A (sign (a,t)), on -1 (sign (a,-1)), and on w", ok)

# ------------------------------------------------------------------ Lemma 7.2
ok_t = ok_s = ok_c = True
for v in PLACES:
    for _ in range(120):
        theta = random.choice([-1, 2, -2, 3, -3, 5, 6, -7, 10])
        p, q, r, s = rr(), rr(), rr(), rr()
        if p * p == theta * q * q or r * r == theta * s * s:
            continue
        gam = torus(theta, p, q)
        e = torus1(theta, r, s)
        if gam[1][0] == 0:
            continue
        assert mul(e, gam) == mul(gam, e) and det(gam) == 1
        res = Ad(e, (gam, 1), v)
        ok_t &= res == (gam, hilbert(det(e), 2 + tr(gam), v))
        # split torus
        t, y1, y2 = rr(), rr(), rr()
        if t * t == 1:
            continue
        res = Ad(M2(y1, 0, 0, y2), (a_(t), 1), v)
        ok_s &= res == (a_(t), hilbert(y1 * y2, 2 + t + 1 / t, v)) and \
            hilbert(y1 * y2, 2 + t + 1 / t, v) == hilbert(y1 * y2, t, v)
        # the central element
        h = mul(dl(rr()), rand_sl2())
        ok_c &= Ad(h, (scal(-1, I2), 1), v) == (scal(-1, I2), hilbert(det(h), -1, v))
report("Lemma 7.2: Ad(h)(gamma,z) = (gamma, (det h, det(1+gamma)) z) on anisotropic tori", ok_t)
report("Lemma 7.2: the same on the split torus, where the sign is (det h, t)", ok_s)
report("Lemma 7.2: Ad(h)(-1,z) = (-1, (det h,-1) z) for all h in GL(2,Q)", ok_c)

e = torus1(3, 0, 1)      # sqrt(3) in Q_3(sqrt 3), of norm -3
res = Ad(e, (scal(-1, I2), 1), 3)
report("Example 7.A(d): over Q_3, Ad(sqrt 3)(-1,1) = (-1,-1), and (-3,-3)_3 = -1",
       res == (scal(-1, I2), -1) and hilbert(-3, -3, 3) == -1)

# ------------------------------------------------------------------ Lemma 7.3
ok_cl = ok_tw = ok_A = True
for v in PLACES:
    for _ in range(120):
        g, y = rand_sl2(), rand_sl2()
        if g[1][0] == 0 or tr(g) == -2:
            continue
        x = (g, random.choice([1, -1]))
        x2 = bconj((y, 1), x, v)
        if x2[0][1][0] != 0:
            ok_cl &= close(Delta(x, v), Delta(x2, v))
        a = rr()
        ok_tw &= close(Delta(Ad_delta(a, x, v), v), hilbert(a, 2 + tr(g), v) * Delta(x, v))
        t = rr()
        if t * t == 1:
            continue
        x3 = bconj((W, 1), bconj((n_(1), 1), (a_(t), 1), v), v)
        ok_A &= close(Delta(x3, v), gamma(1, v) / gamma(t, v))
report("Lemma 7.3(a): Delta_psi is invariant under conjugation in the cover", ok_cl)
report("Lemma 7.3(b): Delta_psi(Ad(d_a) x) = (a, det(1+x)) Delta_psi(x)", ok_tw)
report("Lemma 7.3(c): Delta_psi = gamma(1)/gamma(t) on the class of (a(t),1)", ok_A)

ok = True
for m in [Fr(1, 3), Fr(2, 5), Fr(3, 2), Fr(7, 1), Fr(1, 9)]:
    co, si = (1 - m * m) / (1 + m * m), 2 * m / (1 + m * m)     # 0 < theta < pi
    ok &= close(Delta((M2(co, si, -si, co), 1), INF), 1)
report("Example 7.B: Delta_psi(k_theta, 1) = 1 for 0 < theta < pi at the real place", ok)
th = 0.7
ser = cmath.exp(0.5j * th) / (1 + cmath.exp(1j * th))
report("Example 7.B: sum e^{i(1/2+2j)theta} - sum e^{i(3/2+2j)theta} = 1/(2 cos(theta/2)) (Abel sum)",
       close(ser, 1 / (2 * math.cos(th / 2))))

# ------------------------------------------------------------------ Prop. 7.5
def theta_omega_unit(x, v):
    """Unit part of (7.7): z (c, D-) gamma(D-)/gamma(1), D- = tr g - 2."""
    (g, z) = x
    c = g[1][0]
    Dm = tr(g) - 2
    assert c != 0 and Dm != 0
    return z * hilbert(c, Dm, v) * gamma(Dm, v) / gamma(1, v)


ok_center = ok_thomas = True
MINUS1 = (scal(-1, I2), 1)
for v in PLACES:
    for _ in range(120):
        g = rand_sl2()
        if g[1][0] == 0 or tr(g) in (2, -2):
            continue
        x = (g, random.choice([1, -1]))
        # (7.6) at x  ==  gamma(1)^-2 * (7.7) at (-1,1) x     (|D-(-g)| = |D+(g)|)
        ok_center &= close(Delta(x, v), theta_omega_unit(bmul(MINUS1, x, v), v) / gamma(1, v) ** 2)
        # (7.7) = +- gamma(1) gamma(det(g-1)), det(g-1) = 2 - tr g   (Thomas, Thm 1C)
        th = theta_omega_unit(x, v)
        ref = gamma(1, v) * gamma(2 - tr(g), v)
        ok_thomas &= close(th, ref) or close(th, -ref)
report("Prop. 7.5: (7.6) at x equals gamma(1)^-2 times (7.7) at (-1,1)x", ok_center)
report("Prop. 7.5: (7.7) = +-gamma(1) gamma(det(g-1)), the formula of Thomas up to sign", ok_thomas)


def gauss_trunc(a, p, M):
    """int over p^-M Z_p of psi_p(a x^2) dx, psi_p(x) = exp(2 pi i {x}_p), dx(Z_p) = 1.
    With x = p^-M y: a x^2 = u p^val y^2, val = ord(a) - 2M, which modulo Z_p
    depends on y modulo p^R, R = max(0, -val)."""
    a = Fr(a)
    val = vp(a, p) - 2 * M
    R = max(0, -val)
    u = a / Fr(p) ** vp(a, p)
    tot = 0
    for y in range(p ** R):
        frac = (u * y * y * Fr(p) ** val) % 1
        tot += cmath.exp(2j * cmath.pi * float(frac))
    return p ** M * tot / p ** R


ok = True
for p in (2, 3, 5):
    e = 1 if p == 2 else 0                      # ord(2); psi_p has n_0 = 0
    for a in (1, 2, p, 2 * p, Fr(1, p), Fr(2, p * p)):
        va = vp(Fr(a), p)
        M0 = max(-((-(va + 2 * e)) // 2), -4)   # smallest M with 2(M+1) >= ord(a) + 2 + 2e
        ref = gauss_trunc(a, p, M0)
        ok &= abs(ref) > 1e-6 and all(close(gauss_trunc(a, p, M0 + j), ref) for j in (1, 2))
        # the shells with 2j >= ord(a) + 2 + 2e contribute 0 (Lemma 7.5')
        ok &= close(abs(ref) ** 2, float(Fr(p) ** va) * (2 if p == 2 else 1))  # |2a|^(-1) * |2|... = p^ord(a) * 2^e
report("Lemma 7.5': int over p^-M Z_p of psi(a x^2) is independent of M once 2(M+1) >= ord(a)+2+2 ord(2) (p = 2, 3, 5)", ok)
ok = close(gauss_trunc(1, 2, 1), 1 + 1j) and close(gauss_trunc(2, 2, 2), 2 ** 0.5 * (1 + 1j))
ok &= not close(gauss_trunc(1, 2, 0), 1 + 1j) and not close(gauss_trunc(2, 2, 1), 2 ** 0.5 * (1 + 1j))
report("Lemma 7.5' at 2: the values are 1+i (a = 1, from M = 1) and sqrt2 (1+i) (a = 2, from M = 2), and not earlier", ok)

# Example 7.A(e): the referee's example
gam = ((Fr(3, 5), Fr(-4, 5)), (Fr(4, 5), Fr(3, 5)))
hh = ((Fr(1), Fr(-1)), (Fr(1), Fr(1)))
ok = mul(gam, hh) == mul(hh, gam) and det(hh) == 2 and 2 + tr(gam) == Fr(16, 5)
ok &= hilbert(2, Fr(16, 5), 2) == -1 and hilbert(2, Fr(16, 5), INF) == 1 and hilbert(2, Fr(16, 5), 5) == -1
for v in (INF, 2, 5):
    for z in (1, -1):
        y = Ad(hh, (gam, z), v)
        ok &= y == (gam, hilbert(2, Fr(16, 5), v) * z)
report("Example 7.A(e): h = [[1,-1],[1,1]] commutes with gamma = [[3/5,-4/5],[4/5,3/5]] and "
       "Ad(h) multiplies its lifts by (2,16/5)_v = -1, +1, -1 at v = 2, oo, 5", ok)

# ------------------------------------------------------------------ Lemma 7.4
ok = True
for v in PLACES:
    for _ in range(150):
        g1, g2 = rand_sl2(), rand_sl2()
        c1, c2, c3 = g1[1][0], g2[1][0], mul(g1, g2)[1][0]
        if c1 * c2 * c3 == 0:
            continue
        lhs = gamma(c3 / (c1 * c2), v) * gamma(c3, v)
        rhs = beta(g1, g2, v) * gamma(c1, v) * gamma(c2, v)
        ok &= close(lhs, rhs)
report("Lemma 7.4: the kernels gamma(c)^-1 |c|^-1/2 psi((ax^2-2xy+dy^2)/c) compose with beta_v", ok)

# ------------------------------------------------------------------ Example 7.C, finite model


def weil_finite(p):
    """Weil representation of SL(2,F_p) on C[F_p]: n(u) -> psi(u x^2),
    a(t) -> (t/p) phi(t x), w -> gamma(-1) * Fourier transform with kernel
    psi(-2xy)/sqrt(p); psi(x) = exp(2 pi i x/p). Returns a function g -> matrix."""
    zeta = cmath.exp(2j * cmath.pi / p)
    G = sum(zeta ** ((x * x) % p) for x in range(p))        # Gauss sum
    g1 = G / math.sqrt(p)                                    # "gamma(1)"

    def gam(a):
        return legendre(a, p) * g1

    def kernel(g):
        a, b, c, d = g
        if c % p != 0:
            ci = pow(c, -1, p)
            return [[zeta ** (((a * x * x - 2 * x * y + d * y * y) * ci) % p) / (gam(c) * math.sqrt(p))
                     for y in range(p)] for x in range(p)]
        # g = n(ab) a(a): phi -> psi(ab x^2) (a/p) phi(a x)
        return [[(legendre(a, p) * zeta ** ((a * b * x * x) % p)) if (a * x - y) % p == 0 else 0
                 for y in range(p)] for x in range(p)]
    return kernel


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


for p in (3, 5, 7, 11):
    ker = weil_finite(p)
    els = [(a, b, c, d) for a in range(p) for b in range(p) for c in range(p) for d in range(p)
           if (a * d - b * c) % p == 1]
    # homomorphism on a sample of pairs
    hom = True
    for _ in range(60):
        g, h = random.choice(els), random.choice(els)
        gh = ((g[0] * h[0] + g[1] * h[2]) % p, (g[0] * h[1] + g[1] * h[3]) % p,
              (g[2] * h[0] + g[3] * h[2]) % p, (g[2] * h[1] + g[3] * h[3]) % p)
        A, B, C = ker(g), ker(h), ker(gh)
        AB = matmul(A, B)
        hom &= all(abs(AB[i][j] - C[i][j]) < 1e-9 for i in range(p) for j in range(p))
    good = True
    for g in els:
        D = (g[0] + g[3] + 2) % p
        if D == 0:
            continue
        K = ker(g)
        tP = sum(K[x][(-x) % p] for x in range(p))          # tr(omega(g) P)
        good &= abs(tP - legendre(D, p)) < 1e-9
    report("Example 7.C, finite model p = %d: omega is a representation of SL(2,F_p), and "
           "tr(omega(g)P) = (det(1+g)/p)" % p, hom and good)

# ------------------------------------------------------------------ Lemma 7.5'
ok = True
for v in PLACES:
    for _ in range(150):
        theta = random.choice([-1, 2, -2, 3, -3, 5, 6, -7, 10])
        p, q, a = rr(), rr(), rr()
        if p * p == theta * q * q:
            continue
        gam = torus(theta, p, q)
        if gam[1][0] == 0:
            continue
        ok &= (2 + tr(gam)) * (2 - tr(gam)) == -4 * theta * gam[1][0] ** 2
        ok &= hilbert(a, 2 + tr(gam), v) * hilbert(a, 2 - tr(gam), v) == hilbert(a, -theta, v)
report("Lemma 7.5': det(1+g) det(1-g) = -4 theta y^2, so eta_g eta_{-g} = kappa_E (.,-1)", ok)

# ------------------------------------------------------------------ Lemma 7.8


def norm_row(row, v):
    c, d = row
    if v == INF:
        return math.sqrt(float(c * c + d * d))
    vals = [vp(e, v) for e in (c, d) if e != 0]
    return float(v) ** (-min(vals))


def absv(x, v):
    return abs(float(x)) if v == INF else float(v) ** (-vp(x, v))


def H1(g, v):
    return -math.log(norm_row(g[1], v)) + 0.5 * math.log(absv(det(g), v))


def vA(g, v):
    return -H1(g, v) - H1(mul(W, g), v)


ok = True
for v in PLACES:
    for _ in range(100):
        x, a = rand_sl2(), rr()
        d, di = dl(a), M2(Fr(1) / a, 0, 0, 1)
        lhs = vA(mul(mul(di, x), d), v)
        Hk = H1(mul(x, d), v) - H1(x, v)                       # H_1(k(x) d)
        Hk2 = H1(mul(mul(W, x), d), v) - H1(mul(W, x), v)      # H_1(k(wx) d)
        ok &= abs(lhs - (vA(x, v) - Hk - Hk2)) < 1e-9
report("Lemma 7.8(a): v_A(d^-1 x d) = v_A(x) - H_1(k(x)d) - H_1(k(wx)d), d = diag(a,1)", ok)

# ------------------------------------------------------------------ Prop. 7.10
# local identity (7.14) at p = 3 and p = 2


def is_square(x, p):
    x = Fr(x)
    if vp(x, p) % 2:
        return False
    if p == 2:
        return unit_mod(x, 2, 3) == 1
    return legendre(unit_mod(x, p, 1), p) == 1


# h = indicator of y0 U, with U = 1 + 3 Z_3 (volume 1/2) or 1 + 8 Z_2 (volume 1/4),
# and vol(O^x) = 1. The set {t : xi t^2 in y0 U} is empty unless y0/xi = s^2 is a
# square; then it is s^-1 {u : u^2 in U}, which is +-s^-1 U for p = 3 (volume 1)
# and s^-1 Z_2^x for p = 2 (volume 1).
ok = True
for p, reps, volU in ((3, [1, 2, 3, 6], Fr(1, 2)), (2, [1, 3, 5, 7, 2, 6, 10, 14], Fr(1, 4))):
    for xi in reps:
        for y0 in reps:
            lhs = Fr(1) if is_square(Fr(y0, xi), p) else Fr(0)
            rhs = Fr(1, 2) * sum(hilbert(b, xi, p) * hilbert(b, y0, p) for b in reps) * volU
            ok &= lhs == rhs
report("Prop. 7.10, local step: int h(xi t^2) d*t = (1/2) sum_kappa kappa(xi) int h kappa d*y (p = 2, 3)", ok)

# global identity for k = Q, S = {oo, 2}, at s = 3:
# Phi_oo(y) = exp(-pi (y - 1/3)^2), Phi_2 = indicator of 6 + 16 Z_2, Phi_p = indicator of Z_p
s = mp.mpf(3)
Aplus = mp.quad(lambda y: mp.exp(-mp.pi * (y - mp.mpf(1) / 3) ** 2) * y ** (s - 1), [0, 1, 4, 12])
Aminus = mp.quad(lambda y: mp.exp(-mp.pi * (-y - mp.mpf(1) / 3) ** 2) * y ** (s - 1), [0, 1, 4, 12])
MAXM = 200000
mu_sq = [1] * (MAXM + 1)        # squarefree indicator
for i in range(2, int(MAXM ** 0.5) + 1):
    for j in range(i * i, MAXM + 1, i * i):
        mu_sq[j] = 0
sum3 = mp.fsum(mp.mpf(m) ** (-s) for m in range(1, MAXM + 1, 2) if mu_sq[m] and m % 8 == 3)
sum5 = mp.fsum(mp.mpf(m) ** (-s) for m in range(1, MAXM + 1, 2) if mu_sq[m] and m % 8 == 5)
# xi = +-2m', m' odd squarefree, with xi in 6 Q_2^{x2}:  +2m' with m' = 3 mod 8, -2m' with m' = 5 mod 8
lhs = mp.mpf(1) / 2 * mp.zeta(2 * s) * (1 - mp.mpf(2) ** (-2 * s)) * mp.mpf(2) ** (-s) * (Aplus * sum3 + Aminus * sum5)


def chi_b(b, m):
    """kappa_b at odd m > 0: prod over p | m of (b, p)_p^{ord_p m} (a Kronecker symbol)."""
    r, mm, p = 1, m, 3
    while p * p <= mm:
        while mm % p == 0:
            r *= legendre(b, p)
            mm //= p
        p += 2
    if mm > 1:
        r *= legendre(b, mm)
    return r


def LS(b, s_, N=40001):
    return mp.fsum(chi_b(b, m) * mp.mpf(m) ** (-s_) for m in range(1, N, 2))


rhs = 0
for b in (1, -1, 2, -2):
    Zinf = Aplus + (1 if b > 0 else -1) * Aminus
    Z2 = hilbert(b, 6, 2) * mp.mpf(2) ** (-s) / 4
    rhs += mp.mpf(1) / 2 * LS(b, s) * Zinf * Z2
report("Prop. 7.10(a), k = Q, S = {oo,2}, s = 3: Z(f,s) = (1/2) sum_b L^S(s,kappa_b) Z_S(Phi_S,kappa_b,s)",
       abs(lhs - rhs) < 1e-8, "%s vs %s" % (mp.nstr(lhs, 12), mp.nstr(rhs, 12)))

# constants for S = {oo, 2}
zS = lambda z: mp.zeta(z) * (1 - mp.mpf(2) ** (-z))
h = mp.mpf(10) ** (-8)
rho_S = h * (zS(1 + h) - zS(1 - h)) / 2
c_S = (zS(1 + h) + zS(1 - h)) / 2
report("Example 7.E: rho_S = 1/2 and c_S = (gamma_E + log 2)/2 for zeta^S(s) = zeta(s)(1 - 2^-s)",
       abs(rho_S - 0.5) < 1e-6 and abs(c_S - (mp.euler + mp.log(2)) / 2) < 1e-6,
       "c_S = %s" % mp.nstr(c_S, 10))
Lm1 = mp.nsum(lambda j: (-1) ** j / (2 * j + 1), [0, mp.inf])
L2 = mp.nsum(lambda j: 1 / (8 * j + 1) - 1 / (8 * j + 3) - 1 / (8 * j + 5) + 1 / (8 * j + 7), [0, mp.inf])
Lm2 = mp.nsum(lambda j: 1 / (8 * j + 1) + 1 / (8 * j + 3) - 1 / (8 * j + 5) - 1 / (8 * j + 7), [0, mp.inf])
report("Example 7.E: L^S(1,kappa_-1) = pi/4, L^S(1,kappa_2) = log(1+sqrt2)/sqrt2, L^S(1,kappa_-2) = pi/(2 sqrt2)",
       abs(Lm1 - mp.pi / 4) < 1e-12 and abs(L2 - mp.log(1 + mp.sqrt(2)) / mp.sqrt(2)) < 1e-12
       and abs(Lm2 - mp.pi / (2 * mp.sqrt(2))) < 1e-12)
ok = all(chi_b(-1, m) == (1 if m % 4 == 1 else -1) and chi_b(2, m) == (1 if m % 8 in (1, 7) else -1)
         and chi_b(-2, m) == (1 if m % 8 in (1, 3) else -1) for m in range(1, 400, 2))
report("Example 7.E: kappa_-1, kappa_2, kappa_-2 are the characters of conductor 4, 8, 8", ok)
Lval = {1: None, -1: Lm1, 2: L2, -2: Lm2}
classes = [(sg, u) for sg in (1, -1) for u in (1, 3, 5, 7, 2, 6, 10, 14)]       # Q_S^x / squares


def coeff(sg, u):
    tot = c_S_exact
    for b in (-1, 2, -2):
        tot += hilbert(b, sg, INF) * hilbert(b, u, 2) * Lval[b]
    return tot / 2


c_S_exact = (mp.euler + mp.log(2)) / 2
vals = {cl: coeff(*cl) for cl in classes}
report("Example 7.E: the 16 coefficients a^G(S,u_xi) average to c_S/2",
       abs(mp.fsum(vals.values()) / 16 - c_S_exact / 2) < 1e-15,
       "xi=(+,1): %s, xi=(-,1): %s, xi=(+,3): %s" % (mp.nstr(vals[(1, 1)], 8), mp.nstr(vals[(-1, 1)], 8),
                                                     mp.nstr(vals[(1, 3)], 8)))
report("Prop. 7.10: 4^{|S|} = |Q_S^x / Q_S^{x2}| = 16 and [O_S^x : O_S^{x2}] = 2^{|S|} = 4 for S = {oo,2}",
       len(classes) == 16 == 4 ** 2)


def cls(sg, u):
    """Class of (sign, 2-adic number u) in R^x/squares x Q_2^x/squares."""
    u = Fr(u)
    e = vp(u, 2) % 2
    w0 = unit_mod(u / Fr(2) ** vp(u, 2), 2, 3) % 8
    return (sg, w0 * 2 ** e)


ok = True
for (sg, u) in classes:
    for eps in (-1, 2, -2):                    # units of Z[1/2] modulo squares
        ok &= abs(vals[cls(sg * (1 if eps > 0 else -1), u * eps)] - vals[(sg, u)]) < 1e-15
distinct = sorted({mp.nstr(x, 12) for x in vals.values()})
table = {(1, 1): 1.57726, (1, 3): 0.16864, (1, 5): -0.15668, (-1, 1): -0.31886}
ok &= all(abs(float(vals[k]) - x) < 5e-6 for k, x in table.items())
ok &= abs(sum(float(vals[k]) for k in table) - (float(mp.euler) + math.log(2))) < 1e-12
report("Example 7.E: a^G(S,u_xi) is invariant under xi -> xi*eps, eps in {-1, 2, -2}; four distinct values (the table)",
       ok and len(distinct) == 4 and abs(vals[cls(-1, -1)] - vals[(1, 1)]) < 1e-15,
       "values: " + ", ".join(mp.nstr(mp.mpf(x), 6) for x in distinct))

# ------------------------------------------------------------------ Prop. 7.12
ok = True
for b in (1, -1, 2, -2, 3, -6, 5, 10, -7):
    prod = 1
    for v in [INF, 2] + [p for p in (3, 5, 7) if vp(b, p) != 0]:
        prod *= gamma(b, v) ** 2
    ok &= close(prod, 1)
report("Prop. 7.12: prod_v gamma_v(b)^2 = 1, so omega_{psi_b}(s(-1)) is the parity operator", ok)
n = 5
cnt = sum(1 for eps in itertools.product((1, -1), repeat=n) if math.prod(eps) == 1)
# sum over patterns with product +1 of prod x_v^{eps}:  (prod(p_v + m_v) + prod(p_v - m_v)) / 2
pv = [random.random() for _ in range(n)]
mv = [random.random() for _ in range(n)]
direct = sum(math.prod(pv[i] if e == 1 else mv[i] for i, e in enumerate(eps))
             for eps in itertools.product((1, -1), repeat=n) if math.prod(eps) == 1)
half = (math.prod(p_ + m_ for p_, m_ in zip(pv, mv)) + math.prod(p_ - m_ for p_, m_ in zip(pv, mv))) / 2
report("Prop. 7.12: sum over sign patterns with product +1 = (prod(tr+ + tr-) + prod(tr+ - tr-))/2",
       cnt == 2 ** (n - 1) and abs(direct - half) < 1e-12)

# ------------------------------------------------- after Prop. 7.12 (real packets)
ok = True
r_ = 1 - 1e-7                                  # Abel summation
for m in (1.5, 2.5, 4.5):
    for th in (0.4, 1.3, 2.6):
        def hol(t):
            return cmath.exp(1j * m * t) / (1 - r_ * cmath.exp(2j * t))

        def anti(t):
            return cmath.exp(-1j * m * t) / (1 - r_ * cmath.exp(-2j * t))
        s_p, s_m = hol(th) + anti(th), hol(-th) + anti(-th)
        d_p, d_m = hol(th) - anti(th), hol(-th) - anti(-th)
        ok &= close(s_p, s_m, 1e-5) and close(d_p, -d_m, 1e-5)
        ok &= close(s_p, -math.sin((m - 1) * th) / math.sin(th), 1e-5)
        ok &= close(d_p, 1j * math.cos((m - 1) * th) / math.sin(th), 1e-5)
report("after Prop. 7.12: for weights {m+2j} and {-m-2j}, the sum of the characters is "
       "-sin((m-1)t)/sin t (even), the difference i cos((m-1)t)/sin t (odd)", ok)

# ------------------------------------------- Prop. 7.8' (normalizing factors)
# (c) Szpruch: the inverse local coefficient of I(chi_psi chi, s) is the
# Tate-type integral  T(chi, s) = int_{F^x} gamma_psi(u)^{-1} chi(u) psi(u) |u|^s d^x u,
# gamma_psi(u) = gamma(u)/gamma(1).  With chi = chi0 on the units and
# z = chi(p) p^{-s}, the shell ord(u) = k contributes a_k z^k, a_k the mean of
# gamma_psi(p^k u)^{-1} chi0(u) psi(p^k u) over the units; a_k = 0 for k << 0,
# and a_k depends only on the parity of k for k >= 0.  Claim checked:
#   T(chi, s) T(chi^{-1}, -s) = const * L(2s,chi^2) L(-2s,chi^-2) / (L(1+2s,chi^2) L(1-2s,chi^-2)),
# i.e. const * (1 - z^2/p)(1 - z^-2/p) / ((1 - z^2)(1 - z^-2)) if chi0^2 = 1, and const otherwise.
def psi_p(x, p):
    x = Fr(x)
    d, k = x.denominator, 0
    while d % p == 0:
        d //= p
        k += 1
    if k == 0:
        return 1.0
    return cmath.exp(2j * cmath.pi * ((x.numerator * pow(d, -1, p ** k)) % p ** k) / p ** k)


def tate_coeffs(p, chi0, N, K, inverse=False):
    U = [u for u in range(1, p ** N) if u % p]
    gtab = {}
    out = {}
    for k in range(-K, 2):
        tot = 0
        for u in U:
            key = (k % 2, u % (8 if p == 2 else p))
            if key not in gtab:
                gtab[key] = gamma(Fr(p) ** (k % 2) * u, p) / gamma(1, p)
            c = chi0(u)
            tot += (c.conjugate() if inverse else c) * psi_p(Fr(p) ** k * u, p) / gtab[key]
        out[k] = tot / len(U)
    return out


def tate(z, a, K):
    return sum(a[k] * z ** k for k in range(-K, 0)) + (a[0] + a[1] * z) / (1 - z * z)


def dirichlet(p, N, gens, vals):
    """Character of (Z/p^N)^x with given values on generators (by brute-force logs)."""
    mod = p ** N
    table = {}
    orders = []
    for g_ in gens:
        o, x = 1, g_ % mod
        while x != 1:
            x = x * g_ % mod
            o += 1
        orders.append(o)
    for exps in itertools.product(*[range(o) for o in orders]):
        x, v = 1, 1
        for g_, e_, val in zip(gens, exps, vals):
            x = x * pow(g_, e_, mod) % mod
            v *= val ** e_
        table[x] = complex(v)
    return lambda u: table[u % mod]


def planch_spread(p, chi0, sq_trivial, N, K):
    a, b = tate_coeffs(p, chi0, N, K), tate_coeffs(p, chi0, N, K, inverse=True)
    vals = []
    for z in (0.3 + 0.4j, 1.7 - 0.2j, cmath.exp(0.7j), cmath.exp(2.1j), -0.6 + 1.1j):
        L = (1 - z * z / p) * (1 - z ** -2 / p) / ((1 - z * z) * (1 - z ** -2)) if sq_trivial else 1
        vals.append(tate(z, a, K) * tate(1 / z, b, K) / L)
    c0 = vals[0]
    return max(abs(v - c0) for v in vals), c0


ok, consts, n_chars = True, [], 0
for e1 in (1, -1):                               # (Z/32)^x = <-1> x <5>, 5 of order 8
    for j in range(8):
        chi0 = dirichlet(2, 5, (31, 5), (e1, cmath.exp(2j * cmath.pi * j / 8)))
        spread, c0 = planch_spread(2, chi0, j % 4 == 0, 8, 7)
        ok &= spread < 1e-10 and abs(c0) > 1e-6 and close(c0 ** 4, abs(c0) ** 4)
        consts.append(c0)
        n_chars += 1
report("Prop. 7.8'(c) at v = 2: T(chi,s) T(chi^-1,-s) = const * L-quotient in chi^2, all 16 characters of "
       "conductor | 32; the constant is a positive number times a 4th root of unity", ok and n_chars == 16,
       "constants for chi0 = 1, (-1,.): %s, %s" % (mp.nstr(mp.mpc(consts[0]), 4), mp.nstr(mp.mpc(consts[8]), 4)))
ok = True
for p in (3, 5):
    g_ = 2                                       # primitive root mod 3 and mod 5
    for j in range(p - 1):
        chi0 = dirichlet(p, 1, (g_,), (cmath.exp(2j * cmath.pi * j / (p - 1)),))
        spread, c0 = planch_spread(p, chi0, (2 * j) % (p - 1) == 0, 3, 3)
        ok &= spread < 1e-10 and abs(c0) > 1e-6
report("Prop. 7.8'(c) at v = 3, 5: the same for all tamely ramified characters", ok)

# (a), (b) at the real place, from (6.x) eq:real-M: on the weight m,
# M(lam) = e^{i pi m/2} pi 2^{1-lam} Gamma(lam) / (Gamma((lam+1+m)/2) Gamma((lam+1-m)/2)).
def M_real(m, lam):
    return mp.e ** (1j * mp.pi * m / 2) * mp.pi * 2 ** (1 - lam) * mp.gamma(lam) / (
        mp.gamma((lam + 1 + m) / 2) * mp.gamma((lam + 1 - m) / 2))


ok = True
for m0 in (mp.mpf(1) / 2, -mp.mpf(1) / 2):
    omega = mp.e ** (-1j * mp.pi * m0)           # pi((w,1)^2), since (w,1)^-2 = k_pi
    Lq = lambda lam: mp.pi ** (-lam) * mp.gamma(lam) / (mp.pi ** (-(2 * lam + 1) / 2) * mp.gamma(lam + mp.mpf(1) / 2))
    cfac = mp.sqrt(2) * mp.e ** (1j * mp.pi * m0 / 2)
    ok &= close(complex((cfac / mp.sqrt(2)) ** 2), complex(mp.conj(omega)))
    for t in (0.37, 1.9):
        lam = mp.mpc(0, t)
        for j in (-2, -1, 0, 1, 3):
            m = m0 + 2 * j
            # adjoint relation: conj(M(pi, lam)) = omega * M(pi^w, -lam) on each weight
            ok &= close(complex(mp.conj(M_real(m, lam))), complex(omega * M_real(m, -lam)), 1e-9)
        rho = M_real(m0, -lam) * M_real(m0, lam)  # the scalar, read on the weight m0
        r = cfac * Lq(lam)
        ok &= close(complex(rho), complex(mp.conj(omega) * abs(r) ** 2), 1e-9)
        ok &= close(complex(cfac * Lq(-lam) * r), complex(rho), 1e-9)
report("Prop. 7.8' at the real place: M(pi,it)^* = omega M(pi^w,-it); rho = conj(omega)|r|^2 and "
       "r(pi^w,-it) r(pi,it) = rho for r = sqrt2 e^{i pi m0/2} L(2 lam)/L(2 lam+1), (e^{i pi m0/2})^2 = conj(omega)", ok)

print()
print("%d check(s) failed" % len(FAILS) if FAILS else "all checks passed")
sys.exit(1 if FAILS else 0)

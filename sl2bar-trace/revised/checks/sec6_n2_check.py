# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Checks of Section 6 (the invariant form) of the revised "hitch-hiker's
guide to the metaplectic trace formula for SL(2)", for k = Q.

Checks:
  * the sign of the ramified term +1/4 tr(M(w,0) I(mu_0, f)) of Theorem
    5.13(c), from first principles: for the Eisenstein series E(z, s) of
    SL(2, Z), the integral of |Lambda^Y E(z, 1/2 + ir)|^2 over the modular
    surface (computed from the Fourier expansion) equals
        2 log Y - phi'/phi(s) + [conj(phi(s)) Y^{2ir} - phi(s) Y^{-2ir}] / (2ir),
    i.e. the Maass-Selberg relation (5.9) with the cross terms as stated;
    with the opposite sign of the cross terms the two sides differ by O(1).
    Also phi(1/2) = -1, the classical case of Proposition 6.13;
  * Lemma 6.1(a), u'_B(k, y) = -H(ky) (referee item II.15): the integral over X of
    1{X > 0} - 1{X > Y} is Y for both signs of Y, and at v = R the function
    k -> u'_B(k, a(s)) changes sign, so it is not |H(ky)| (Example 6.A);
  * Lemma 6.3(a): v_A(xy) = v_A(x) - H(k(x) y) - H(k(wx) y) at v = R, with
    k(x) taken from an explicit Iwasawa decomposition;
  * Lemma 6.3(b): J_A(gamma, f^y) = J_A(gamma, f) + f_{B,y}(gamma)
    + f_{B,y}(w gamma w^-1) at v = R, for f = exp(-||g||^2) (quadrature);
  * Lemma 6.4: for the principal series of SL(2, R) in the compact picture,
    with M(lambda) diagonal on the K-types e^{im theta},
        I(y) M^-1 M' I(y)^-1 = M^-1 M' + H_y + M^-1 H_y M
    as matrices on Fourier modes (and M(l) I_l(y) = I_{-l}(y) M(l));
  * Lemma 6.6(b): the real intertwining integral on the weight-m line,
        int (1+u^2)^(-(l+1)/2) e^{im arctan u} du
          = pi 2^(1-l) Gamma(l) / (Gamma((l+1+m)/2) Gamma((l+1-m)/2)),
    for half-integral and integral m; with r(l) = sqrt(pi) Gamma(l) /
    Gamma(l + 1/2) = L_R(2l)/L_R(2l+1) the quotient is constant on the weights
    +-1/2, has absolute value sqrt(2) on i R for every half-integral m, and
    satisfies R_{m+2}/R_m = (1 + m - l)/(1 + m + l); the resulting formula
    for R^-1 R' on the weight 5/2 (Example 6.B), and the Fourier transform
    (1/2 pi) int 2a/(a^2 + t^2) e^{-itX} dt = e^{-a|X|} (Example 6.C);
  * Lemma 6.12: the unramified Whittaker integral on the double cover at
    p = 3, 5, 7, 11,
        int phi_0(w^-1 n(u)) psi_p(-a u) du = 1 + (-a/p) chi(p) p^(-l-1/2)
          = L(l + 1/2, chi eta_a) / L(2l + 1, chi^2),
    shell by shell (only the shell |u| = p contributes); for SL(2) itself
    the integral is 1 - chi(p) p^(-l-1) = 1 / L(l + 1, chi);
  * Proposition 6.13, M(w, 0) = -1, for k = Q and mu = chi_{psi_b},
    b = 1, -1, 2, -2, by a computation independent of its proof: the
    leading coefficient -4 log 2 of m^S at 0 for S = {oo, 2}, the residue
    1 + e^{i pi m_0} of the real operator, and the residue of the 2-adic
    operator, computed from shell averages in the cover;
  * the completed factor xi(2l)/xi(2l+1) tends to -1 at l = 0 (Example 6.D).
"""
import cmath
import math
import random
import sys
from fractions import Fraction as Fr

import mpmath as mp

from padic_lib import hilbert, legendre
from cover_lib import iwasawa_value

random.seed(20261113)
mp.mp.dps = 20
FAILS = []


def report(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def gauss_legendre(n):
    """Nodes and weights on [-1, 1], by Newton iteration on Legendre polynomials."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-15:
                break
        xs.append(x)
        ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws


# ------------------------------------------------- sign of the ramified term
def xi(s):
    return mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def phi_scatt(s):
    return xi(2 * s - 1) / xi(2 * s)


def truncated_norm(r, Y, nterms=6, nx=12, ny=22):
    """int over SL(2,Z)\\H of |Lambda^Y E(z, 1/2 + ir)|^2 dx dy / y^2."""
    s = mp.mpf(1) / 2 + 1j * mp.mpf(r)
    sc, ph = complex(s), complex(phi_scatt(s))
    coef = []
    for n in range(1, nterms + 1):
        sig = sum(mp.mpf(d) ** (1 - 2 * s) for d in range(1, n + 1) if n % d == 0)
        coef.append(complex(4 / xi(2 * s) * mp.mpf(n) ** (s - mp.mpf(1) / 2) * sig))
    gx, wx = gauss_legendre(nx)
    gy, wy = gauss_legendre(ny)
    total = 0.0
    for xk, wk in zip(gx, wx):
        x = 0.25 * (xk + 1)
        y0 = math.sqrt(1 - x * x)
        for a, b, below in ((y0, Y, True), (Y, Y + 1.2, False), (Y + 1.2, Y + 5, False)):
            for yk, vk in zip(gy, wy):
                y = 0.5 * (b - a) * yk + 0.5 * (a + b)
                nc = 0
                for n in range(1, nterms + 1):
                    if 2 * math.pi * n * y < 45:
                        nc += coef[n - 1] * complex(mp.besselk(s - mp.mpf(1) / 2, 2 * mp.pi * n * y)) \
                            * math.cos(2 * math.pi * n * x)
                val = math.sqrt(y) * nc + ((y ** sc + ph * y ** (1 - sc)) if below else 0)
                total += wk * 0.25 * vk * 0.5 * (b - a) * abs(val) ** 2 / y ** 2
    return 2 * total


r0, Y0 = 0.7, 1.5
s0 = mp.mpf(1) / 2 + 1j * mp.mpf(r0)
lhs = truncated_norm(r0, Y0)
dlog = mp.diff(phi_scatt, s0) / phi_scatt(s0)
cross = (mp.conj(phi_scatt(s0)) * mp.mpf(Y0) ** (2j * r0) - phi_scatt(s0) * mp.mpf(Y0) ** (-2j * r0)) / (2j * r0)
plus = complex(2 * mp.log(Y0) - dlog + cross)
minus = complex(2 * mp.log(Y0) - dlog - cross)
report("Thm 5.13(c): Maass-Selberg for SL(2,Z), cross terms with the sign of (5.9)",
       abs(lhs - plus) < 1e-7, "lhs %.9f, formula %.9f" % (lhs, plus.real))
report("Thm 5.13(c): ... and the opposite sign fails by O(1)", abs(lhs - minus) > 1,
       "opposite sign gives %.4f" % minus.real)
report("phi(1/2) = -1 for SL(2,Z) (the classical case of Prop. 6.13)",
       abs(phi_scatt(mp.mpf(1) / 2 + mp.mpf(10) ** (-9)) + 1) < 1e-7)


# ------------------------------------------------- real matrices
def mat(a, b, c, d):
    return ((a, b), (c, d))


def mm(g, h):
    return ((g[0][0] * h[0][0] + g[0][1] * h[1][0], g[0][0] * h[0][1] + g[0][1] * h[1][1]),
            (g[1][0] * h[0][0] + g[1][1] * h[1][0], g[1][0] * h[0][1] + g[1][1] * h[1][1]))


def minv(g):
    (a, b), (c, d) = g
    return ((d, -b), (-c, a))


def kth(t):
    return mat(math.cos(t), math.sin(t), -math.sin(t), math.cos(t))


WR = mat(0.0, -1.0, 1.0, 0.0)


def Hreal(g):
    """H(g) = -log ||e_2 g|| (Section 4)."""
    return -math.log(math.hypot(g[1][0], g[1][1]))


def angle(g):
    """theta with g in N A^+ k_theta."""
    return math.atan2(-g[1][0], g[1][1])


def kpart(g):
    return kth(angle(g))


def vA(g):
    return -Hreal(g) - Hreal(mm(WR, g))


def rand_sl2():
    a, n, t = math.exp(random.uniform(-1, 1)), random.uniform(-2, 2), random.uniform(0, 2 * math.pi)
    return mm(mm(mat(1.0, n, 0.0, 1.0), mat(a, 0.0, 0.0, 1 / a)), kth(t))


# ------------------------------------------------- u'_B (item II.15)
def gamma_prime_integral(Yv, lo=-50.0, hi=50.0, n=200000):
    """int (1{X>0} - 1{X>Y}) dX by a Riemann sum."""
    h = (hi - lo) / n
    tot = 0
    for i in range(n):
        X = lo + (i + 0.5) * h
        tot += (1 if X > 0 else 0) - (1 if X > Yv else 0)
    return tot * h


ok = all(abs(gamma_prime_integral(Yv) - Yv) < 1e-3 for Yv in (3.7, -2.2, 0.4, -11.0))
report("item II.15: int (tau_B(X) - tau_B(X - Y)) dX = Y for both signs of Y, so u'_B(k,y) = -H(ky)", ok)
s = 1.8
u0 = -Hreal(mm(kth(0.0), mat(s, 0.0, 0.0, 1 / s)))
u1 = -Hreal(mm(kth(math.pi / 2), mat(s, 0.0, 0.0, 1 / s)))
report("item II.15: u'_B(k, a(s)) changes sign with k (it is not |H(ky)|)",
       abs(u0 + math.log(s)) < 1e-12 and abs(u1 - math.log(s)) < 1e-12, "%.4f, %.4f" % (u0, u1))

# ------------------------------------------------- Lemma 6.3(a)
ok = True
for _ in range(200):
    x, y = rand_sl2(), rand_sl2()
    lhs_ = vA(mm(x, y))
    rhs_ = vA(x) - Hreal(mm(kpart(x), y)) - Hreal(mm(kpart(mm(WR, x)), y))
    ok &= abs(lhs_ - rhs_) < 1e-9
report("Lemma 6.3(a): v_A(xy) = v_A(x) - H(k(x)y) - H(k(wx)y) at v = R", ok)


# ------------------------------------------------- Lemma 6.3(b)
def fgauss(g):
    return math.exp(-(g[0][0] ** 2 + g[0][1] ** 2 + g[1][0] ** 2 + g[1][1] ** 2))


NK = 128
THETAS = [2 * math.pi * j / NK for j in range(NK)]
GU, GW = gauss_legendre(240)
ULIM = 10.0


def JA(t, y):
    """J_A(a(t), f^y) = |D|^(1/2) int_N int_K f(y k^-1 n^-1 a(t) n k y^-1) v_A(n) dk dn."""
    yi = minv(y)
    g0 = mat(t, 0.0, 0.0, 1 / t)
    tot = 0.0
    for uk, wk in zip(GU, GW):
        u = ULIM * uk
        n = mat(1.0, u, 0.0, 1.0)
        core = mm(mm(minv(n), g0), n)
        w = 0.5 * math.log(1 + u * u)
        for th in THETAS:
            k = kth(th)
            tot += wk * ULIM * w * fgauss(mm(mm(y, mm(mm(minv(k), core), k)), yi)) / NK
    return abs(t - 1 / t) * tot


def fBy(t, y):
    """f_{B,y}(a(t)) = |t| int_K int_N f(k^-1 a(t) n(u) k) (-H(ky)) du dk."""
    g0 = mat(t, 0.0, 0.0, 1 / t)
    tot = 0.0
    for uk, wk in zip(GU, GW):
        u = ULIM * uk
        core = mm(g0, mat(1.0, u, 0.0, 1.0))
        for th in THETAS:
            k = kth(th)
            tot += wk * ULIM * (-Hreal(mm(k, y))) * fgauss(mm(mm(minv(k), core), k)) / NK
    return abs(t) * tot


t0 = 1.4
yv = mm(mm(mat(1.0, 0.3, 0.0, 1.0), mat(1.25, 0.0, 0.0, 0.8)), kth(0.5))
diff = JA(t0, yv) - JA(t0, mat(1.0, 0.0, 0.0, 1.0))
corr = fBy(t0, yv) + fBy(1 / t0, yv)
report("Lemma 6.3(b): J_A(g, f^y) - J_A(g, f) = f_{B,y}(g) + f_{B,y}(w g w^-1) at v = R",
       abs(diff - corr) < 1e-7 * abs(diff) and abs(diff) > 1e-3, "%.9f vs %.9f" % (diff, corr))


# ------------------------------------------------- Lemma 6.6(b), Examples 6.B-6.C
def c_num(m, lam):
    return mp.quad(lambda u: (1 + u * u) ** (-(lam + 1) / 2) * mp.e ** (1j * m * mp.atan(u)),
                   [-mp.inf, -5, 0, 5, mp.inf])


def c_formula(m, lam):
    return mp.pi * 2 ** (1 - lam) * mp.gamma(lam) / (mp.gamma((lam + 1 + m) / 2) * mp.gamma((lam + 1 - m) / 2))


lam1 = mp.mpf("1.3") + 0.4j
ok = all(abs(c_num(m, lam1) - c_formula(m, lam1)) < 1e-10 for m in (mp.mpf(1) / 2, mp.mpf(-3) / 2, mp.mpf(5) / 2, 2))
report("Lemma 6.6(b): real intertwining integral on the weight m = pi 2^(1-l) G(l)/(G((l+1+m)/2) G((l+1-m)/2))", ok)


def r_real(lam):
    return mp.sqrt(mp.pi) * mp.gamma(lam) / mp.gamma(lam + mp.mpf(1) / 2)


def R_real(m, lam):
    """Normalized operator on the weight m (including the phase e^{i m pi/2})."""
    return mp.e ** (1j * mp.pi * m / 2) * c_formula(m, lam) / r_real(lam)


half = mp.mpf(1) / 2
ok = all(abs(R_real(half, lam) - mp.sqrt(2) * mp.e ** (1j * mp.pi / 4)) < 1e-12
         and abs(R_real(-half, lam) - mp.sqrt(2) * mp.e ** (-1j * mp.pi / 4)) < 1e-12
         for lam in (0.3j, 2.1j, mp.mpf("0.4") + 1j))
report("Lemma 6.6(b): with r = L_R(2l)/L_R(2l+1) the operator is constant on the weights +-1/2", ok)
ok = all(abs(abs(R_real(m, 1j * t)) - mp.sqrt(2)) < 1e-12
         for m in (half, 3 * half, 5 * half, -7 * half, 9 * half) for t in (0.2, 1.1, 5.0))
report("Lemma 6.6(b): |R_m(it)| is constant (unitarity on i R) for half-integral m", ok)
ok = all(abs(R_real(m + 2, lam1) / R_real(m, lam1) - (1 + m - lam1) / (1 + m + lam1)) < 1e-12
         for m in (half, 5 * half, -3 * half, -half))
report("Lemma 6.6(b): R_{m+2}/R_m = (1 + m - l)/(1 + m + l)", ok)
lam2 = 0.9j
a32 = mp.mpf(3) / 2
ld = mp.diff(lambda l: R_real(5 * half, l), lam2) / R_real(5 * half, lam2)
report("Example 6.B: R^-1 R' on the weight 5/2 is -2a/(a^2 - l^2), a = 3/2",
       abs(ld + 2 * a32 / (a32 ** 2 - lam2 ** 2)) < 1e-10)
ok = True
for X in (0.0, 0.7, -1.9):
    ft = mp.quad(lambda t: 2 * a32 / (a32 ** 2 + t * t) * mp.cos(t * X), [0, mp.inf]) / mp.pi \
        if X == 0 else mp.quadosc(lambda t: 2 * a32 / (a32 ** 2 + t * t) * mp.cos(t * X), [0, mp.inf],
                                  omega=abs(X)) / mp.pi
    ok &= abs(ft - mp.e ** (-a32 * abs(X))) < 1e-8
report("Example 6.C: (1/2pi) int 2a/(a^2+t^2) e^{-itX} dt = e^{-a|X|}", ok)

# ------------------------------------------------- Lemma 6.4
lamc = complex(0.9, 0.5)
NS = 256
SAMPLE = [2 * math.pi * j / NS for j in range(NS)]
MODES = list(range(-44, 45, 2))


def dft_coeff(vals, m):
    return sum(v * cmath.exp(-1j * m * th) for v, th in zip(vals, SAMPLE)) / NS


def I_matrix(y, lam):
    """Matrix of I(lam, y) on the modes e^{im theta}: (I phi)(theta) =
    phi(theta') e^{(lam+1) H(k_theta y)}, k_theta y in N A k_theta'."""
    gs = [mm(kth(th), y) for th in SAMPLE]
    hp = [Hreal(g) for g in gs]
    tp = [angle(g) for g in gs]
    A = mp.matrix(len(MODES), len(MODES))
    for j, m in enumerate(MODES):
        vals = [cmath.exp(1j * m * t_) * cmath.exp((lam + 1) * h_) for t_, h_ in zip(tp, hp)]
        for i, mmode in enumerate(MODES):
            A[i, j] = dft_coeff(vals, mmode)
    return A, hp


ymat = mm(mat(1.3, 0.25, 0.0, 1 / 1.3), kth(0.4))
mp.mp.dps = 15
I1, hp = I_matrix(ymat, lamc)
I1inv, _ = I_matrix(minv(ymat), lamc)
Iminus, _ = I_matrix(ymat, -lamc)
nm = len(MODES)
Mdiag = [complex(mp.e ** (1j * mp.pi * m / 2) * c_formula(m, lamc)) for m in MODES]
dMdiag = [complex(mp.e ** (1j * mp.pi * m / 2) * mp.diff(lambda l: c_formula(m, l), lamc)) for m in MODES]
Hy = mp.matrix(nm, nm)
hcoef = {d: dft_coeff(hp, d) for d in range(-2 * 44, 2 * 44 + 1, 2)}
for i, mi in enumerate(MODES):
    for j, mj in enumerate(MODES):
        Hy[i, j] = hcoef[mi - mj]
Mm = mp.diag(Mdiag)
Lm = mp.diag([d / c for d, c in zip(dMdiag, Mdiag)])
mid = range(nm // 2 - 5, nm // 2 + 6)


def block_err(A, B):
    return max(abs(A[i, j] - B[i, j]) for i in mid for j in mid)


report("Lemma 6.4: M(l) I_l(y) = I_{-l}(y) M(l) in the compact picture of SL(2,R)",
       block_err(Mm * I1, Iminus * Mm) < 1e-9)
lhs_m = I1 * Lm * I1inv
rhs_m = Lm + Hy + mp.diag([1 / c for c in Mdiag]) * Hy * Mm
wrong = Lm - Hy - mp.diag([1 / c for c in Mdiag]) * Hy * Mm
report("Lemma 6.4: I(y) M^-1 M' I(y)^-1 = M^-1 M' + H_y + M^-1 H_y M",
       block_err(lhs_m, rhs_m) < 1e-9 and block_err(lhs_m, wrong) > 0.1,
       "error %.1e" % float(block_err(lhs_m, rhs_m)))
mp.mp.dps = 20


# ------------------------------------------------- Lemma 6.12 (Whittaker)
def whittaker(p, lam, z, a, cover=True, mmax=3):
    """int_{Q_p} phi_0(w^-1 n(u)) psi_p(-a u) du, shell by shell; psi_p(x) =
    exp(2 pi i {x}_p). The region |u| <= 1 contributes 1."""
    total, shells = 1.0, []
    for m in range(1, mmax + 1):
        sh = 0
        for u in range(1, p ** m):
            if u % p:
                sh += iwasawa_value(Fr(u, p ** m), p, lam, z, cover) \
                    * cmath.exp(-2j * cmath.pi * ((a * u) % p ** m) / p ** m)
        shells.append(sh)
        total += sh
    return total, shells


for p in (3, 5, 7, 11):
    lam, z = 0.37 + 0.21j, cmath.exp(0.9j) * 0.8
    ok, ok_shell, ok0 = True, True, True
    for a in (1, 2, -1, 4, -3 if p != 3 else -5):
        val, shells = whittaker(p, lam, z, a)
        eps = legendre(-a, p)
        target = 1 + eps * z * p ** (-lam - 0.5)
        lratio = (1 - z ** 2 * p ** (-2 * lam - 1)) / (1 - eps * z * p ** (-lam - 0.5))
        ok &= abs(val - target) < 1e-10 and abs(val - lratio) < 1e-10
        ok_shell &= all(abs(x) < 1e-10 for x in shells[1:])
        val0, _ = whittaker(p, lam, z, a, cover=False)
        ok0 &= abs(val0 - (1 - z * p ** (-lam - 1))) < 1e-10
    report("Lemma 6.12: unramified Whittaker integral = L(l+1/2, chi eta_a)/L(2l+1, chi^2), "
           "eta_a(p) = (-a/p), p=%d" % p, ok)
    report("Lemma 6.12: only the shell |u| = p contributes, p=%d" % p, ok_shell)
    report("comparison: SL(2), no cover: 1/L(l+1, chi), p=%d" % p, ok0)


# ------------------------------------------------- Proposition 6.13
def mS(lam):
    return (1 - 2 ** (-2 * lam)) * mp.zeta(2 * lam) / ((1 - 2 ** (-1 - 2 * lam)) * mp.zeta(2 * lam + 1))


eps_ = mp.mpf(10) ** (-6)
lead = mS(eps_) / eps_ ** 2
report("Prop. 6.13: m^S(l) = -4 log 2 * l^2 + O(l^3) for S = {oo,2} (a zero of order |S|)",
       abs(lead + 4 * mp.log(2)) < 1e-4, mp.nstr(lead, 10))


def two_adic_shell_average(m, b, R=6):
    """Average over units u of the integrand of the 2-adic intertwining
    integral at y = u/2^m (m >= 3), times |y|, at lambda = 0, for
    mu = chi_{psi_b} = chi_psi (b, .)_2."""
    tot, cnt = 0, 0
    for u in range(1, 2 ** R, 2):
        y = Fr(u, 2 ** m)
        tot += iwasawa_value(y, 2, 0.0, 1.0) * hilbert(b, -1 / y, 2) * 2 ** m
        cnt += 1
    return tot / cnt


for b in (1, -1, 2, -2):
    av = [two_adic_shell_average(m, b) for m in range(3, 9)]
    periodic = all(abs(av[i] - av[i + 2]) < 1e-12 for i in range(4))
    # Res_{l=0} M_2(l) = (even + odd shell averages) * (1/2) / (2 log 2)
    res2 = (av[0] + av[1]) / (4 * mp.log(2))
    # Res_{l=0} M_oo(l) = 1 + e^{i pi m_0}, e^{i pi m_0} = mu_oo(a(-1), 1) = i sgn(b)
    resinf = 1 + (1j if b > 0 else -1j)
    Mw0 = complex(-4 * mp.log(2) * resinf * res2)
    report("Prop. 6.13: M(w,0) = -1 on H_B(chi_{psi_b}) for k = Q, b = %d (local residues)" % b,
           periodic and abs(Mw0 + 1) < 1e-10, "M(w,0) = %.6f%+.6fj" % (Mw0.real, Mw0.imag))

lim = xi(2 * eps_) / xi(2 * eps_ + 1)
report("Example 6.D: xi(2l)/xi(2l+1) -> -1 at l = 0", abs(lim + 1) < 1e-4, mp.nstr(lim, 10))

print()
print("%d check(s) failed" % len(FAILS) if FAILS else "all checks passed")
sys.exit(1 if FAILS else 0)

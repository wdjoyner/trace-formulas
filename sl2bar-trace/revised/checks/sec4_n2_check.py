# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Checks of Section 4 (the geometric side) of the revised "hitch-hiker's guide
to the metaplectic trace formula for SL(2)", for k = Q.

Checks:
  * the Iwasawa height H_v, computed by an explicit decomposition g = n a k
    (exact over Q_p, floating point over R), equals -log ||(c, d)||_v, the
    norm of the bottom row (Lemma 4.3(a));
  * H(x) + H(gamma x) <= 0 for random adelic x and gamma in SL(2,Q) - B(Q),
    and H(gamma x) = H(x) for gamma in B(Q) (Lemma 4.3(b));
  * H(a x) = H(a) + H(x) and H(w a x) = -H(a) + H(w x), so the weight
    v_A(x) = -H(x) - H(w x) is left A-invariant and >= 0 (Lemma 4.3(c));
  * v_{A,v}(n(y)) = log ||(1, y)||_v: log max(1,|y|_p) at p, (1/2)log(1+y^2)
    at R (Lemma 4.9; referee item II.22);
  * the weight integral of Proposition 4.6:
    int (1 - 1[X + h1 > T] - 1[-X + h2 > T]) dX = 2T - h1 - h2;
  * the conjugation identities n(-nu) a(t) n(nu) = a(t) n((1 - t^-2) nu) and
    a(t)^-1 n(z) a(t) = n(t^-2 z) (symbolic);
  * Lemma 4.10 (J_A at a central element): with the correction term
    r(t) J_G(a(t), f), r(t) = log|t^2 - t^-2|, the limit t -> 1 exists and
    equals int Phi(y) log|2y| dy; without it, J_A(a(t), f) diverges like
    -log|1 - t^-2| Phi^(0). Checked at v = R (quadrature, test function
    exp(-pi ||g - 1||^2)) and at v = 3 (exact, f = char. function of K_1);
  * w-symmetry J_A(mu^-1, f) = J_A(mu, f) at v = R;
  * Example 4.A: for k = Q and Phi = exp(-pi y^2) (x) 1_Zhat, the constant
    term of the unipotent contribution, computed from the truncated integrals of
    Proposition 4.8 at several T, is independent of T and equals
    FP_{s=1} zeta(s) M(s) = gamma_E/4 - log(4 pi)/4.
"""
import math
import random
import sys
from fractions import Fraction as Fr

import mpmath as mp

from padic_lib import vp, INF

random.seed(20261111)
mp.mp.dps = 30
FAILS = []


def report(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def mul(g, h):
    return ((g[0][0] * h[0][0] + g[0][1] * h[1][0], g[0][0] * h[0][1] + g[0][1] * h[1][1]),
            (g[1][0] * h[0][0] + g[1][1] * h[1][0], g[1][0] * h[0][1] + g[1][1] * h[1][1]))


def inv(g):
    (a, b), (c, d) = g
    return ((d, -b), (-c, a))


def det(g):
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


def absv(x, v):
    """Normalized absolute value of a rational at v (v = INF or a prime)."""
    if x == 0:
        return 0
    if v == INF:
        return abs(float(x))
    return Fr(1, v) ** vp(x, v) if vp(x, v) >= 0 else Fr(v) ** (-vp(x, v))


def logabs(x, v):
    if v == INF:
        return math.log(abs(float(x)))
    return -vp(x, v) * math.log(v)


# ---------------------------------------------------------------- Iwasawa H_v
def iwasawa_H(g, v):
    """Compute g = n a(t) k with k in K_v by an explicit construction, verify it,
    and return H_v(g) = log|t|_v."""
    (a, b), (c, d) = g
    if v == INF:
        a, b, c, d = map(float, (a, b, c, d))
        r = math.hypot(c, d)
        k = ((d / r, -c / r), (c / r, d / r))          # in SO(2), bottom row (c,d)/r
        u = mul(((a, b), (c, d)), inv(k))
        assert abs(u[1][0]) < 1e-9 and abs(u[1][1] - r) < 1e-9 * max(1, r)
        t = u[0][0]
        assert abs(t * r - 1) < 1e-9
        return math.log(abs(t))
    p = v
    if c == 0 or (d != 0 and vp(c, p) >= vp(d, p)):
        s = d
        k = ((Fr(1), Fr(0)), (c / d, Fr(1)))
    else:
        s = c
        k = ((Fr(0), Fr(-1)), (Fr(1), d / c))
    assert det(k) == 1
    assert all(x == 0 or vp(x, p) >= 0 for row in k for x in row)   # k in SL(2, Z_p)
    u = mul(g, inv(k))
    assert u[1][0] == 0 and u[1][1] == s
    t = u[0][0]
    return logabs(t, p)


def bottom_row_H(g, v):
    (a, b), (c, d) = g
    if v == INF:
        return -0.5 * math.log(float(c) ** 2 + float(d) ** 2)
    m = max(absv(c, v), absv(d, v))
    return -math.log(m)


def rand_rat(big=40):
    while True:
        a, b = random.randint(-big, big), random.randint(1, big)
        if a:
            return Fr(a, b)


def rand_sl2(big=40, lower_nonzero=None):
    """Random element of SL(2,Q). lower_nonzero: None (any), True (c != 0) or
    False (c = 0)."""
    while True:
        if lower_nonzero is False:
            t, u = rand_rat(big), rand_rat(big)
            return ((t, u), (Fr(0), 1 / t))
        a, c = rand_rat(big), rand_rat(big)
        b = rand_rat(big)
        d = (1 + b * c) / a
        g = ((a, b), (c, d))
        if det(g) == 1:
            return g


PLACES = [INF, 2, 3, 5, 7]
ok = True
for _ in range(400):
    g = rand_sl2()
    for v in PLACES:
        h1, h2 = iwasawa_H(g, v), bottom_row_H(g, v)
        if abs(h1 - h2) > 1e-9:
            ok = False
report("Lemma 4.3(a): Iwasawa height H_v(g) = -log||(c,d)||_v, v = inf,2,3,5,7", ok)


def primes_of(*xs):
    ps = set()
    for x in xs:
        for n in (abs(x.numerator), x.denominator):
            q = 2
            while q * q <= n:
                while n % q == 0:
                    ps.add(q)
                    n //= q
                q += 1
            if n > 1:
                ps.add(n)
    return ps


def H_adelic(gamma, xloc):
    """H(gamma x) for x = (x_v) with x_v = xloc[v] on a finite set of places and
    x_v = 1 elsewhere; gamma in SL(2,Q). Sums H_v over every place where
    gamma x_v can fail to lie in K_v."""
    ents = [e for row in gamma for e in row]
    for g in xloc.values():
        ents += [e for row in g for e in row if isinstance(e, Fr)]
    places = {INF} | primes_of(*[e for e in ents if e != 0]) | {p for p in xloc if p != INF}
    tot = 0.0
    I = ((Fr(1), Fr(0)), (Fr(0), Fr(1)))
    for v in places:
        xv = xloc.get(v, I)
        tot += iwasawa_H(mul(gamma, xv), v)
    return tot


I2 = ((Fr(1), Fr(0)), (Fr(0), Fr(1)))
ok_ineq, ok_B, worst = True, True, -1e9
for _ in range(300):
    xloc = {v: rand_sl2(25) for v in random.sample(PLACES, 3)}
    g = rand_sl2(25, lower_nonzero=True)
    s = H_adelic(I2, xloc) + H_adelic(g, xloc)
    worst = max(worst, s)
    if s > 1e-9:
        ok_ineq = False
    b = rand_sl2(25, lower_nonzero=False)
    if abs(H_adelic(b, xloc) - H_adelic(I2, xloc)) > 1e-9:
        ok_B = False
report("Lemma 4.3(b): H(x) + H(gamma x) <= 0 for gamma not in B(Q) (k = Q)", ok_ineq,
       "max over 300 samples = %.3g" % worst)
report("Lemma 4.3(b): H(gamma x) = H(x) for gamma in B(Q) (product formula)", ok_B)

# H(ax) = H(a) + H(x), H(wax) = -H(a) + H(wx), v_A >= 0
W = ((Fr(0), Fr(-1)), (Fr(1), Fr(0)))
ok1, ok2, ok3 = True, True, True
for _ in range(300):
    x = rand_sl2()
    t = rand_rat()
    a = ((t, Fr(0)), (Fr(0), 1 / t))
    for v in PLACES:
        Ha = logabs(t, v)
        if abs(iwasawa_H(mul(a, x), v) - Ha - iwasawa_H(x, v)) > 1e-9:
            ok1 = False
        if abs(iwasawa_H(mul(W, mul(a, x)), v) + Ha - iwasawa_H(mul(W, x), v)) > 1e-9:
            ok2 = False
    xloc = {v: rand_sl2(25) for v in random.sample(PLACES, 2)}
    vA = -H_adelic(I2, xloc) - H_adelic(W, xloc)
    if vA < -1e-9:
        ok3 = False
report("Lemma 4.3(c): H(a x) = H(a) + H(x) at v = inf,2,3,5,7", ok1)
report("Lemma 4.3(c): H(w a x) = -H(a) + H(w x) at v = inf,2,3,5,7", ok2)
report("Lemma 4.3(c): v_A(x) = -H(x) - H(w x) >= 0 on random adelic x", ok3)

# v_{A,v}(n(y)) = log ||(1,y)||_v
ok = True
for _ in range(300):
    y = rand_rat(200)
    ny = ((Fr(1), y), (Fr(0), Fr(1)))
    for v in PLACES:
        vA = -iwasawa_H(ny, v) - iwasawa_H(mul(W, ny), v)
        if v == INF:
            ref = 0.5 * math.log(1 + float(y) ** 2)
        else:
            ref = math.log(max(1, float(absv(y, v))))
        if abs(vA - ref) > 1e-9:
            ok = False
report("Lemma 4.9: v_{A,v}(n(y)) = log max(1,|y|_p), (1/2)log(1+y^2) at R", ok)


# ---------------------------------------------------------------- weight integral
def bracket_integral(h1, h2, T):
    """int_R (1 - 1[X + h1 > T] - 1[-X + h2 > T]) dX, computed exactly by
    splitting R at the two break points (the integrand vanishes outside)."""
    p1, p2 = T - h1, h2 - T          # 1st indicator: X > p1; 2nd: X < p2
    pts = sorted([p1, p2])
    tot = Fr(0)
    for lo, hi in ((pts[0], pts[1]),):
        mid = (lo + hi) / 2
        val = 1 - (1 if mid + h1 > T else 0) - (1 if -mid + h2 > T else 0)
        tot += val * (hi - lo)
    # outside [pts[0], pts[1]] the integrand is 0: check at two sample points
    for X in (pts[0] - 1, pts[1] + 1):
        assert 1 - (1 if X + h1 > T else 0) - (1 if -X + h2 > T else 0) == 0
    return tot


ok = all(bracket_integral(h1, h2, T) == 2 * T - h1 - h2
         for h1, h2, T in ((rand_rat(), rand_rat(), rand_rat()) for _ in range(500)))
report("Prop. 4.6: int (1 - 1[X+h1>T] - 1[-X+h2>T]) dX = 2T - h1 - h2", ok)

# ---------------------------------------------------------------- conjugations
import sympy as sp
tt, nu, zz = sp.symbols("t nu z", nonzero=True)
A_ = sp.Matrix([[tt, 0], [0, 1 / tt]])
Nm = lambda u: sp.Matrix([[1, u], [0, 1]])
ok1 = sp.simplify(Nm(-nu) * A_ * Nm(nu) - A_ * Nm((1 - tt ** -2) * nu)) == sp.zeros(2)
ok2 = sp.simplify(A_.inv() * Nm(zz) * A_ - Nm(tt ** -2 * zz)) == sp.zeros(2)
report("conjugation: n(-nu) a(t) n(nu) = a(t) n((1-t^-2) nu)", ok1)
report("conjugation: a(t)^-1 n(z) a(t) = n(t^-2 z)", ok2)


# ---------------------------------------------------------------- Lemma 4.10, v = R
def f_real(g):
    """Test function exp(-pi ||g - 1||_F^2): conjugation invariant under SO(2)."""
    return mp.e ** (-mp.pi * ((g[0][0] - 1) ** 2 + g[0][1] ** 2 + g[1][0] ** 2 + (g[1][1] - 1) ** 2))


def JA_real(t, weight=True):
    """J_A(a(t), f) = |t - 1/t| int_R f(n(-y) a(t) n(y)) v_A(n(y)) dy (the K-integral
    is trivial for this f); weight=False gives J_G."""
    t = mp.mpf(t)
    def integrand(y):
        g = [[t, t * y - y / t], [0, 1 / t]]          # n(-y) a(t) n(y), multiplied out
        g2 = [[t, t * y], [0, 1 / t]]
        g3 = [[1, -y], [0, 1]]
        prod = [[g3[0][0] * g2[0][0] + g3[0][1] * g2[1][0], g3[0][0] * g2[0][1] + g3[0][1] * g2[1][1]],
                [g3[1][0] * g2[0][0] + g3[1][1] * g2[1][0], g3[1][0] * g2[0][1] + g3[1][1] * g2[1][1]]]
        assert abs(prod[0][1] - g[0][1]) <= mp.mpf(10) ** -20 * (1 + abs(y))
        w = mp.log(1 + y * y) / 2 if weight else 1
        return f_real(prod) * w
    s = 1 / abs(t - 1 / t)                               # width of the integrand in y
    pts = sorted(set([-10 * s, -s, -1, 0, 1, s, 10 * s]))
    return abs(t - 1 / t) * mp.quad(integrand, [-mp.inf] + pts + [mp.inf])


def phi_real(y):
    return f_real([[1, y], [0, 1]])


target = mp.quad(lambda y: phi_real(y) * mp.log(abs(2 * y)), [-mp.inf, 0, mp.inf])
Phi0 = mp.quad(phi_real, [-mp.inf, mp.inf])
vals, raw = [], []
for e in (3, 5, 7):
    t = 1 + mp.mpf(10) ** -e
    r = mp.log(abs(t ** 2 - t ** -2))
    JA, JG = JA_real(t), JA_real(t, weight=False)
    vals.append(JA + r * JG)
    raw.append(JA + mp.log(abs(1 - t ** -2)) * Phi0)
ok = abs(vals[-1] - target) < 1e-5 and abs(vals[-1] - target) < abs(vals[0] - target) + 1e-12
report("Lemma 4.10 (v=R): J_A(a(t),f) + r(t) J_G(a(t),f) -> int Phi log|2y| dy", ok,
       "t=1+1e-7: %s vs %s" % (mp.nstr(vals[-1], 10), mp.nstr(target, 10)))
# uncorrected J_A grows like -log|1 - t^-2| Phi^(0): J_A + log|1-t^-2| Phi^(0) stays bounded
ok = abs(raw[-1] - raw[-2]) < 1e-3 and abs(JA_real(1 + mp.mpf(10) ** -7)) > 10
report("Lemma 4.10 (v=R): without r(t), J_A(a(t),f) ~ -log|1-t^-2| Phi^(0) diverges", ok)

# w-symmetry J_A(mu^-1) = J_A(mu) at R for a regular mu
for t in (mp.mpf("1.7"), mp.mpf("0.6")):
    a, b = JA_real(t), JA_real(1 / t)
    report("J_A(mu^-1, f) = J_A(mu, f) at R, t = %s" % mp.nstr(t, 3), abs(a - b) < 1e-15,
           "%s" % mp.nstr(a, 12))


# ---------------------------------------------------------------- Lemma 4.10, v = 3
def corrected_3adic(e):
    """f = char. function of K_1 (conjugation invariant under K), t = 1 + 3^e u,
    e >= 1. J_A = 3^-e int_{ord y >= 1-e} log max(1,|y|) dy, J_G = 1/3,
    r = log|t^2 - t^-2|_3 = -e log 3. Returns J_A + r J_G (exact in log 3)."""
    L = sp.log(3)
    JA = sp.Rational(1, 3 ** e) * sum((-m) * L * sp.Rational(2, 3) * sp.Rational(3) ** (-m)
                                     for m in range(1 - e, 0))
    JG = sp.Rational(1, 3 ** e) * sp.Rational(3) ** (e - 1)
    assert JG == sp.Rational(1, 3)
    return sp.nsimplify(JA - e * L * JG), JA


target3 = -sp.log(3) / 2      # int_{3Z_3} log|2y|_3 dy
ok = True
for e in (5, 10, 20):
    val, JA = corrected_3adic(e)
    err = abs(float(val - target3))
    ok = ok and err < 3.0 ** (-e) * 10
report("Lemma 4.10 (v=3): J_A + r J_G -> int_{3Z_3} log|2y| dy = -(1/2) log 3", ok,
       "error at e=20: %.2e" % err)


# ---------------------------------------------------------------- Example 4.A
def G_unip(u):
    """G(t) = |t|^-2 sum_{nu in Q^x} Phi(t^-2 nu) at t = (u, unit), u > 0, for
    Phi = exp(-pi y^2) (x) 1_Zhat: u^-2 sum_{nu != 0} exp(-pi nu^2 / u^4)."""
    u = mp.mpf(u)
    if u <= 1:
        return u ** -2 * (mp.jtheta(3, 0, mp.e ** (-mp.pi / u ** 4)) - 1)
    # for u > 1 use Poisson summation over Z (Jacobi's theta transformation)
    return mp.jtheta(3, 0, mp.e ** (-mp.pi * u ** 4)) - u ** -2


# the two expressions agree near u = 1 (Poisson summation over Z)
_u = mp.mpf("0.999999")
report("Example 4.A: theta transformation at u = 1",
       abs(_u ** -2 * (mp.jtheta(3, 0, mp.e ** (-mp.pi / _u ** 4)) - 1)
           - (mp.jtheta(3, 0, mp.e ** (-mp.pi * _u ** 4)) - _u ** -2)) < 1e-20)


def constant_term(T):
    """int_{u <= e^T} G du/u + int_{u > e^T} (G - Phi^(0)) du/u - c Phi^(0) T,
    with c = vol(Zhat^x) = 1, Phi^(0) = 1."""
    eT = mp.e ** T
    i1 = mp.quad(lambda u: G_unip(u) / u, [mp.mpf("0.05"), mp.mpf("0.5"), eT]) if eT > 0.05 else 0
    i2 = mp.quad(lambda u: (G_unip(u) - 1) / u, [eT, 10 * eT, mp.inf])
    return i1 + i2 - T


FP = mp.euler / 4 - mp.log(4 * mp.pi) / 4
cts = [constant_term(mp.mpf(T)) for T in ("0", "0.5", "-0.3", "1.2")]
ok = all(abs(c - FP) < 1e-12 for c in cts)
report("Example 4.A: J^T_unip - f(1) - c Phi^(0) T is independent of T", ok,
       ", ".join(mp.nstr(c, 14) for c in cts))
report("Example 4.A: it equals FP_{s=1} zeta(s)M(s) = gamma/4 - log(4 pi)/4", ok,
       mp.nstr(FP, 14))
# Mellin form: Z(s) = zeta(s) M(s), M(s) = (1/2) pi^{-s/2} Gamma(s/2), at s = 2
s0 = mp.mpf(2)
Zs = mp.quad(lambda u: u ** (2 - 2 * s0) * G_unip(u) / u, [mp.mpf("0.05"), 1, mp.inf])
ok = abs(Zs - mp.zeta(s0) * mp.pi ** (-s0 / 2) * mp.gamma(s0 / 2) / 2) < 1e-15
report("Example 4.A: Z(f,2) = zeta(2) M(2) (Mellin form of (4.9))", ok)

print()
print("%d check(s) failed" % len(FAILS) if FAILS else "all checks passed")
sys.exit(1 if FAILS else 0)

# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""
Rank-two test of Hypothesis (R): PGL(3), an unramified elliptic element of depth 0.
See README.md and Appendix B of the revised paper.  Prepared by Claude (Anthropic), 2026.

Checks
  1. Building: the displacement table N(lambda, mu) = #{v : d(v0,v)=lambda, d(v,gamma v)=mu}
     agrees with the closed form (B.2) (q=2, radius 4; q=3, radius 3).
  2. Orbital integrals O_gamma(f_nu) counted on the building agree with (B.2).
  3. The T-independent part I(chi,gamma) of the truncated kernel equals the closed form (B.4)
     (sum over the full cone, at random characters).
  4. Spectral identity: int f_nu^vee I dmu = O_gamma(f_nu) for nu_1 <= 6, q = 2, 3
     (no singular part).
  5. The truncated kernel I^T is a single exponential polynomial in T (19 frequencies
     T -> wT - w'T, as in (4.7A)); its constant term is I(chi,gamma).
  6. Hypothesis (R) in the stated form fails: grouped oscillatory coefficients times rho
     grow like 1/eps near the non-root subtorus z_3^3 = 1; they cancel in pairs whose
     frequencies coincide on that subtorus.
"""
import collections
import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np

import building as B

FAIL = []


def check(name, ok, info=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + info if info else ""))
    if not ok:
        FAIL.append(name)


GAMMA = {2: [[0, 0, 1], [1, 0, 1], [0, 1, 0]],     # x^3 + x + 1 mod 2
         3: [[0, 0, -1], [1, 0, 1], [0, 1, 0]]}    # x^3 - x + 1 mod 3
ID = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


# ---------------------------------------------------------------- closed forms
def Qf(q):
    return (1 + Fr(1, q)) * (1 + Fr(1, q) + Fr(1, q * q))


def vol(l1, l2, q):
    """vol(K a_lambda K) for lambda = (l1, l2, 0), l1 >= l2 >= 0."""
    a, b = l1 - l2, l2
    if l1 == 0:
        return Fr(1)
    if a > 0 and b > 0:
        return Qf(q) * q ** (2 * l1)
    return Qf(q) / (1 + Fr(1, q)) * q ** (2 * l1)


def N_closed(l1, l2, q):
    """(B.2): distribution of d(v, gamma v) over the vertices v with d(v0, v) = (l1, l2)."""
    a, b, k = l1 - l2, l2, l1
    s = min(a, b)
    V = vol(l1, l2, q)
    out = collections.Counter()
    if k == 0:
        out[(0, 0)] = 1
        return out
    if s == 0:
        out[(2 * k, k)] = V
        return out
    P0 = Fr(q - 1, q + 1)
    out[(2 * k, k)] += P0 * V
    for j in range(1, s):
        out[(2 * k - j, k + j)] += P0 * V / q ** j
        out[(2 * k - j, k - 2 * j)] += P0 * V / q ** j
    r = Fr(q, q + 1) / Fr(q) ** s
    out[(2 * k - s, k + s)] += r * V
    out[(2 * k - s, k - 2 * s)] += r * V
    return out


def O_closed(nu, q):
    tot = Fr(0)
    for l1 in range(nu[0] + 1):
        for l2 in range(l1 + 1):
            tot += N_closed(l1, l2, q).get(nu, 0)
    return tot


# ---------------------------------------------------------------- 1, 2: building
def building_checks():
    for p, R in ((2, 4), (3, 3)):
        t0 = time.time()
        S = B.ball(R, p)
        g = GAMMA[p]
        tab = collections.defaultdict(collections.Counter)
        for H in S.values():
            tab[B.vdist(ID, H, p)][B.vdist(H, B.matmul(g, H), p)] += 1
        bad = [lam for lam, c in tab.items() if dict(c) != dict(N_closed(*lam, p))]
        check("N(lambda,mu) = (B.2), q=%d, radius %d (%d vertices, %.0fs)"
              % (p, R, len(S), time.time() - t0), not bad, str(bad))
        # orbital integrals: all v with d(v, gamma v) = nu lie at l1 <= 2 nu_1/3 (by B.2)
        disp = collections.Counter()
        for lam, c in tab.items():
            for mu, n in c.items():
                disp[mu] += n
        nus = [nu for nu in disp if 2 * nu[0] / 3 <= R]
        bad = [nu for nu in nus if disp[nu] != O_closed(nu, p)]
        check("O_gamma(f_nu) on building = (B.2), q=%d, %d values of nu" % (p, len(nus)), not bad, str(bad))


# ---------------------------------------------------------------- spectral side
def cfun(zz, q):
    r = 1
    for i in range(3):
        for j in range(i + 1, 3):
            x = zz[i] / zz[j]
            r = r * (1 - x / q) / (1 - x)
    return r


def F0(u, v, q):
    """Sum over the full dominant cone, per Weyl element (u = (wz)^{a1}, v = (wz)^{a2})."""
    P0, R = (q - 1) / (q + 1), q / (q + 1)
    X = u * v
    geo = lambda r: r / (1 - r)
    A = P0 * (1 + geo(1 / u) + geo(1 / v))
    return (2 * R * X / (1 - X)
            + (1 + X) / (1 - X) * (A * geo(X * X)
                                   + (R - P0 / (1 - 1 / u)) * geo(X * X / u)
                                   + (R - P0 / (1 - 1 / v)) * geo(X * X / v)))


def I_closed(z, q):
    """(B.4)."""
    z1, z2, z3 = z
    roots = [z1 / z2, z2 / z3, z1 / z3]
    S = sum(r + 1 / r for r in roots)
    den = np.prod([abs(1 - r) ** 2 for r in roots], axis=0)
    return 3 * (q - 1) ** 2 / (q ** 3 * (q + 1)) * (2 * (q * q + q + 1) - q * S) / den


def Irho_closed(z, q):
    z1, z2, z3 = z
    roots = [z1 / z2, z2 / z3, z1 / z3]
    S = sum(r + 1 / r for r in roots)
    den = np.prod([abs(1 - r / q) ** 2 for r in roots], axis=0)
    return (q - 1) ** 2 * (q * q + q + 1) / (2 * q ** 6) * (2 * (q * q + q + 1) - q * S) / den


def rho(z, q):
    Q = (1 + 1 / q) * (1 + 1 / q + 1 / q ** 2)
    return Q / 6 / abs(cfun(z, q)) ** 2


def I_from_cone(z, q):
    tot = 1.0
    for p in itertools.permutations(range(3)):
        w = [z[i] for i in p]
        tot = tot + cfun([1 / x for x in w], q) * F0(w[0] / w[1], w[1] / w[2], q)
    return tot


def spherical_poly(m1, m2):
    """Macdonald's Gamma_chi(a_mu) for PGL(3) as an explicit Laurent polynomial (sympy)."""
    import sympy as sp
    z1, z2, q = sp.symbols('z1 z2 q')
    Z = (z1, z2, 1 / (z1 * z2))
    Q = (1 + 1 / q) * (1 + 1 / q + 1 / q ** 2)
    tot = 0
    for p in itertools.permutations(range(3)):
        w = [Z[i] for i in p]
        tot += cfun([1 / x for x in w], q) * w[0] ** m1 * w[1] ** m2
    return sp.lambdify((z1, z2, q), sp.cancel(sp.together(tot * q ** (-m1) / Q)))


def spectral_checks():
    rng = np.random.default_rng(1)
    for q in (2.0, 3.0):
        th = rng.uniform(0, 2 * np.pi, (2, 20))
        z = (np.exp(1j * th[0]), np.exp(1j * th[1]), np.exp(-1j * (th[0] + th[1])))
        err = np.max(abs(I_from_cone(z, q) - I_closed(z, q)) / abs(I_closed(z, q)))
        check("I(chi,gamma) = full-cone sum = (B.4), q=%d" % q, err < 1e-9, "rel err %.1e" % err)
        err = np.max(abs(I_closed(z, q) * rho(z, q) - Irho_closed(z, q)))
        check("I*rho closed form, q=%d" % q, err < 1e-9, "err %.1e" % err)
    nus = [(0, 0), (1, 0), (2, 1), (2, 0), (3, 0), (3, 1), (4, 2), (4, 1), (5, 1), (5, 4), (6, 3), (6, 0)]
    M = 160
    t1 = 2 * np.pi * (np.arange(M) + 1 / 3) / M
    t2 = 2 * np.pi * (np.arange(M) + 1 / 7) / M
    A, Bm = np.meshgrid(t1, t2, indexing='ij')
    Z1, Z2 = np.exp(1j * A), np.exp(1j * Bm)
    Zg = (Z1, Z2, 1 / (Z1 * Z2))
    polys = {nu: spherical_poly(*nu) for nu in nus}
    for q in (2, 3):
        W0 = Irho_closed(Zg, float(q))
        worst = 0
        for nu in nus:
            fv = float(vol(*nu, q)) * polys[nu](Z1, Z2, float(q))
            spec = np.mean(fv * W0)
            worst = max(worst, abs(spec - float(O_closed(nu, q))))
        check("int f_nu^vee I dmu = O_gamma(f_nu), q=%d, %d values of nu" % (q, len(nus)),
              worst < 1e-7, "max err %.1e" % worst)


# ---------------------------------------------------------------- 5, 6: the expansion in T
def Kw(u, v, ta, tb, q):
    """Truncated per-Weyl-element kernel: sum over lambda in A_A(T), lambda != 0."""
    P0, R = (q - 1) / (q + 1), q / (q + 1)
    X = u * v
    n = 3 * max(ta, tb) + 3
    a, b = np.meshgrid(np.arange(n), np.arange(n), indexing='ij')
    m = (2 * a + b < 2 * ta + tb) & (a + 2 * b < ta + 2 * tb) & ((a > 0) | (b > 0))
    a, b = a[m], b[m]
    k, s = a + b, np.minimum(a, b)
    geo = lambda r, n2: np.where(n2 >= 1, (r - r ** (n2 + 1)) / (1 - r), 0)
    sf = s.astype(float)
    t = np.where(s == 0, R * X ** k,
                 X ** k * (P0 * (1 + geo(1 / u, s - 1) + geo(1 / v, s - 1)) + R * (u ** -sf + v ** -sf)))
    return t.sum()


def freqs_lo(ta, tb):      # cone <T,a1> <= <T,a2>
    c = (2 * ta + tb) / 3
    return [(0, 0), (ta + tb, ta + tb), (tb, ta + tb), (ta + tb, tb), (c, 2 * c), (2 * c, c)]


def freqs_hi(ta, tb):      # cone <T,a1> >= <T,a2>
    c = (ta + 2 * tb) / 3
    return [(0, 0), (ta + tb, ta + tb), (ta, ta + tb), (ta + tb, ta), (c, 2 * c), (2 * c, c)]


def zexp(p, m, n):
    """Exponent of z for the monomial u^m v^n of the Weyl term p (u=(wz)^{a1}, v=(wz)^{a2})."""
    e = np.zeros(3)
    e[p[0]] += m; e[p[1]] += n - m; e[p[2]] -= n
    return e - e.mean()


def candidate_maps():
    """Linear maps T -> exponent of z, read off from the vertices of the truncated cone."""
    maps = {}
    for fr in (freqs_lo, freqs_hi):
        E1, E2 = fr(1, 0), fr(0, 1)
        for p in itertools.permutations(range(3)):
            for k in range(6):
                e1, e2 = zexp(p, *E1[k]), zexp(p, *E2[k])
                maps[tuple(np.round(np.concatenate([e1, e2]), 6) + 0.0)] = (e1, e2)
    return maps


def I_T(z, T, q):
    """The truncated kernel I^T(chi, gamma), T = (<T,a1>, <T,a2>)."""
    tot = 1.0
    for p in itertools.permutations(range(3)):
        w = z[list(p)]
        tot = tot + cfun(1 / w, q) * Kw(w[0] / w[1], w[1] / w[2], *T, q)
    return tot


TS = [(2 * x, 2 * y) for x in range(2, 16) for y in range(2, 16) if (x - y) % 3 == 0]


def expansion(z, q, maps, Ts=TS):
    keys = list(maps)
    D = np.array([[np.prod(z ** (maps[k][0] * T[0] + maps[k][1] * T[1])) for k in keys] for T in Ts])
    y = np.array([I_T(z, T, q) for T in Ts])
    sol = np.linalg.lstsq(D, y, rcond=None)[0]
    return dict(zip(keys, sol)), np.max(abs(D @ sol - y)), D, y


def expansion_checks():
    q = 2.0
    maps = candidate_maps()
    zero = tuple([0.0] * 6)
    z = np.exp(1j * np.array([0.37, 1.21, -1.58]))
    coef, res, D, y = expansion(z, q, maps)
    check("I^T is one exponential polynomial on the whole cone (%d candidate frequencies)" % len(maps),
          res < 1e-10, "resid %.1e on %d values of T" % (res, len(TS)))
    check("its constant term is I(chi,gamma) of (B.4)", abs(coef[zero] - I_closed(z, q)) < 1e-10)
    cwt = lambda ta, tb: np.array([2 * ta + tb, -ta + tb, -ta - 2 * tb]) / 3     # T as a coweight
    W = list(itertools.permutations(range(3)))
    diffs = {tuple(np.round(np.concatenate([cwt(1, 0)[list(s)] - cwt(1, 0)[list(t)],
                                            cwt(0, 1)[list(s)] - cwt(0, 1)[list(t)]]), 6) + 0.0)
             for s in W for t in W}
    nz = [k for k, c in coef.items() if abs(c) > 1e-8]
    check("the %d frequencies with non-zero coefficient are all T -> wT - w'T (Q = B)" % len(nz),
          all(k in diffs for k in nz))
    lo = [i for i, T in enumerate(TS) if T[0] <= T[1]]
    hi = [i for i, T in enumerate(TS) if T[0] > T[1]]
    s_lo = np.linalg.lstsq(D[lo], y[lo], rcond=None)[0]
    err = np.max(abs(D[hi] @ s_lo - y[hi]))
    check("fit on <T,a1> <= <T,a2> predicts the other cone", err < 1e-10, "err %.1e" % err)

    grows = []
    for eps in (1e-2, 1e-3, 1e-4):
        z3 = np.exp(1j * eps); z1 = np.exp(0.9j)
        z = np.array([z1, 1 / (z1 * z3), z3])
        coef, res, _, _ = expansion(z, q, maps)
        r = rho(z, q)
        big = [(k, c) for k, c in coef.items() if abs(c) * r > 10]
        grows.append(max(abs(c) for c in coef.values()) * r)
        zH = np.array([z1, 1 / z1, 1.0])          # the point of H = {z3^3 = 1} nearest z
        chH = lambda k: np.prod(zH ** (maps[k][0] * 7.3 + maps[k][1] * 11.1))
        pairs = [abs(c1 + c2) * r for i, (k1, c1) in enumerate(big) for j, (k2, c2) in enumerate(big)
                 if j > i and abs(chH(k1) - chH(k2)) < 1e-9]
        if eps == 1e-4:
            check("(R) fails: %d coefficients x rho of size ~1/eps near z3^3=1 (rho != 0 there)" % len(big),
                  len(big) == 8 and grows[-1] > 1000, "max %.0f at eps=1e-4, fit resid %.1e" % (grows[-1], res))
            check("they cancel in pairs whose frequencies coincide on z3^3=1",
                  len(pairs) == 4 and max(pairs) < 1, "max |a+a'|rho = %.3f" % max(pairs))
    check("growth rate ~ 1/eps", 8 < grows[1] / grows[0] < 12 and 8 < grows[2] / grows[1] < 12,
          "%.0f, %.0f, %.0f" % tuple(grows))


def perturbation_check():
    """The table N does not change when gamma is replaced by other elements of gamma K_1."""
    p, R = 2, 4
    S = B.ball(R, p)
    ok = True
    for g in ([[0, 0, 1], [1, 2, 1], [0, 1, 0]], [[0, 4, 1], [1, 0, 1], [2, 1, 8]], [[0, 0, 1], [1, 0, 3], [0, 1, 2]]):
        tab = collections.defaultdict(collections.Counter)
        for H in S.values():
            tab[B.vdist(ID, H, p)][B.vdist(H, B.matmul(g, H), p)] += 1
        ok &= all(dict(c) == dict(N_closed(*lam, p)) for lam, c in tab.items())
    check("same table for three other elements of gamma K_1 (q=2, radius 4)", ok)


if __name__ == "__main__":
    t0 = time.time()
    building_checks()
    spectral_checks()
    perturbation_check()
    expansion_checks()
    print("total %.0fs" % (time.time() - t0))
    sys.exit(1 if FAIL else 0)

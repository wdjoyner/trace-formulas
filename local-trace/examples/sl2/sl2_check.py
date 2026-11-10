# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""
SL(2) check for D. Joyner, "Simple local trace formulas for unramified
p-adic groups" (1997), revised 2026.  Companion to ../pgl2/pgl2_check.py.

For G = SL(2, Q_p), K = SL(2, Z_p), the vertices of G/K are the vertices of
the Bruhat-Tits tree at even distance from v0 = K, and

    O_gamma(1_{K a_n K}) = #{ v at even distance from v0 : d(v, gamma v) = 2n },

with a_n = diag(p^n, p^-n), vol K = 1, vol T_gamma = 1.

What is checked (q = 3):
  (1) Plancherel inversion for SL(2) with Q = 1 + 1/q.
  (2) For the unramified elliptic gamma = [[0,-1],[1,0]] and the other SL(2)-class
      gamma' in its stable class (conjugate by diag(p,1) in GL(2)):
          O_gamma(f)  = 1/2 int f^vee I_st dmu + 1/2 f^vee(chi_0),
          O_gamma'(f) = 1/2 int f^vee I_st dmu - 1/2 f^vee(chi_0),
      where chi_0 is the unramified quadratic character (z = -1) and
      I_st = 1 + sum_{n>=1} (c(chi^-1) z^n + c(chi) z^-n)  (Abel sum).
      So the spectral measure of O_gamma has an ATOM at chi_0, a non-regular
      unitary character at which the Plancherel density does not vanish.
  (3) The atom-free Abel limit I = sum_n O_gamma(f_n) Gamma_chi(a_n) gives only
      1/2 int f^vee I_st dmu: it misses exactly the atom 1/2 f^vee(chi_0).
  (4) For a ramified elliptic gamma there is no atom.
Prepared by Claude (Anthropic) for D. Joyner, 2026.
"""
import pathlib
import sys
from fractions import Fraction as Fr

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "pgl2"))
import pgl2_check as T  # tree utilities (q = 3)  # noqa: E402

q = T.p
Q = 1 + 1 / q
V0 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]


def counts_even(gamma, R):
    """Histogram of d(v, gamma v) over vertices v with d(v0, v) even and <= R."""
    c = {}
    for g in T.tree_ball(R):
        if T.dist(V0, g) % 2:
            continue
        d = T.dist(g, T.mat_mul(gamma, g))
        c[d] = c.get(d, 0) + 1
    return c


def cfun(z):
    """c_alpha(chi) = (1 - q^-1 z)/(1 - z), z = chi(a_alpha) = chi(a_1)."""
    return (1 - z / q) / (1 - z)


def Gamma(z, n):
    """Macdonald on A^- = {a_n : n >= 0}: Q^-1 delta^{1/2}(a_n) sum_w c((w chi)^-1) (w chi)(a_n)."""
    return q ** (-n) / Q * (cfun(1 / z) * z**n + cfun(z) * z ** (-n))


def vol(n):
    return 1 if n == 0 else (q + 1) * q ** (2 * n - 1)


def fvee(z, n):
    return vol(n) * Gamma(z, n)


def rho(z):
    return Q / 2 * abs(1 - z) ** 2 / abs(1 - z / q) ** 2


if __name__ == "__main__":
    np.seterr(all="ignore")
    N = 400000
    z = np.exp(1j * (np.arange(N) + 0.5) / N * 2 * np.pi)
    integ = lambda F: np.mean(F * rho(z)).real  # noqa: E731

    print("Check (1): Plancherel inversion for SL(2)")
    for n in range(4):
        row = [integ(fvee(z, n) * Gamma(z, m)) for m in range(4)]
        print("  n=%d:" % n, " ".join("%7.4f" % x for x in row))
        for m in range(4):
            assert abs(row[m] - (n == m)) < 1e-6, ("inversion", n, m)

    I_st = 1 + cfun(1 / z) * z / (1 - z) + cfun(z) / z / (1 - 1 / z)
    I_kappa = 1 + cfun(1 / z) * (-z) / (1 + z) + cfun(z) * (-1 / z) / (1 + 1 / z)
    I_naive = (I_st + I_kappa) / 2  # = Abel sum of sum_n O_gamma(f_n) Gamma(a_n)

    R = 7
    gam = [[Fr(0), Fr(-1)], [Fr(1), Fr(0)]]
    h = [[Fr(q), Fr(0)], [Fr(0), Fr(1)]]
    gam2 = T.mat_mul(T.mat_mul(h, gam), T.mat_inv(h))
    c1, c2 = counts_even(gam, R), counts_even(gam2, R)
    print("\nCheck (2)-(3): gamma = [[0,-1],[1,0]] (unramified, depth 0) and gamma' = its GL(2)-conjugate")
    print("   n  O_gamma  O_gamma'   1/2 int f^v I_st   1/2 f^v(chi_0)   atom-free int f^v I")
    for n in range(4):
        st = integ(fvee(z, n) * I_st) / 2
        atom = fvee(np.array([-1.0 + 0j]), n)[0].real / 2
        nv = integ(fvee(z, n) * I_naive)
        O1, O2 = c1.get(2 * n, 0), c2.get(2 * n, 0)
        print("  %2d  %6d  %7d   %16.6f   %14.6f   %18.6f" % (n, O1, O2, st, atom, nv))
        assert abs(O1 - (st + atom)) < 1e-6, ("atom formula, gamma", n)
        assert abs(O2 - (st - atom)) < 1e-6, ("atom formula, gamma'", n)
        assert abs(O1 - nv - atom) < 1e-6, ("atom-free limit misses the atom", n)

    print("\nCheck (4): ramified gamma = [[2,3],[1,2]] (E = Q_3(sqrt 3)), no atom")
    gr = [[Fr(2), Fr(3)], [Fr(1), Fr(2)]]
    cr = counts_even(gr, R)
    I_r = 1 + (cfun(1 / z) * z / (1 - z) + cfun(z) / z / (1 - 1 / z)) / Q
    for n in range(4):
        s = integ(fvee(z, n) * I_r)
        print("  n=%d: tree %4d   spectral %10.6f" % (n, cr.get(2 * n, 0), s))
        assert abs(s - cr.get(2 * n, 0)) < 1e-6, ("ramified", n)

    print("\nALL CHECKS PASSED")

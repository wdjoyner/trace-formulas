# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""
PGL(2) worked example for D. Joyner, "Simple local trace formulas for
unramified p-adic groups" (1997), revised 2026.

Checks, for G = PGL(2, Q_p) and K = PGL(2, Z_p):
  (1) elliptic orbital integrals O_gamma(1_{K a_n K}) by counting vertices v of the
      Bruhat-Tits tree with d(v, gamma v) = n   (measures: vol K = 1, vol T_gamma = 1);
  (2) the Plancherel inversion f(a_n) = int f^vee(z) Gamma_z(a_n) dmu(z)
      with Macdonald's constant Q = 1 + 1/q;
  (3) the spectral formula  O_gamma(f) = int f^vee(z) I(z,gamma) dmu(z)
      with the closed forms for I(z, gamma) derived in the note;
  (4) the truncation statement: for M >= deg f the truncated I^M gives the same
      integral exactly.
Prepared by Claude (Anthropic) for D. Joyner, 2026.
"""
from fractions import Fraction as Fr
import numpy as np

p = 3
q = p


def vp(x):
    """p-adic valuation of a nonzero rational."""
    x = Fr(x)
    if x == 0:
        return 10**9
    n, d, v = x.numerator, x.denominator, 0
    while n % p == 0:
        n //= p; v += 1
    while d % p == 0:
        d //= p; v -= 1
    return v


def mat_mul(A, B):
    return [[sum(Fr(A[i][k]) * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def mat_inv(A):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    det = Fr(a) * d - Fr(b) * c
    return [[d / det, -b / det], [-c / det, a / det]]


def dist(g, h):
    """Tree distance between vertices gK and hK: v(det M) - 2 min v(M_ij), M = g^-1 h."""
    M = mat_mul(mat_inv(g), h)
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    return vp(det) - 2 * min(vp(M[i][j]) for i in range(2) for j in range(2))


def canon(g):
    """Canonical label of the vertex gK: lattice spanned by the columns of g, up to scalars.
    Column-reduce to [[p^e, b],[0,1]] form, b taken mod p^e."""
    a, b = Fr(g[0][0]), Fr(g[0][1])
    c, d = Fr(g[1][0]), Fr(g[1][1])
    # make lower-left entry zero by column operations over Z_p (use the column with smaller v)
    if c != 0 and (d == 0 or vp(c) < vp(d)):
        a, b, c, d = b, a, d, c  # swap columns
    if c != 0:
        t = c / d  # v(t) >= 0, so this is a Z_p column operation
        a, c = a - t * b, Fr(0)
        # columns now (a,0) and (b,d)
    # scale second column by unit to get d = p^{v(d)}, then scale lattice so d = 1
    vd = vp(d)
    u = d / Fr(p) ** vd
    b, d = b / u, Fr(p) ** vd
    a, b = a / Fr(p) ** vd, b / Fr(p) ** vd
    e = vp(a)
    # reduce b mod p^e Z_p (b has p-power denominator after the scaling)
    modulus = Fr(p) ** e
    # b in Z[1/p] localized: represent b = n / m with m prime to p after removing p-part
    num, den = b.numerator, b.denominator
    pd = 0
    while den % p == 0:
        den //= p; pd += 1
    # b = (num * den^{-1} mod p^{e+pd+K}) / p^pd ; keep enough digits
    K = 40
    md = p ** (e + pd + K) if e + pd + K > 0 else 1
    bb = (num * pow(den, -1, md)) % md if md > 1 else 0
    bfr = Fr(bb, p ** pd)
    if e + pd > 0:
        bfr = Fr(bb % (p ** (e + pd)), p ** pd)
    else:
        bfr = Fr(0)
    return (e, bfr)


def tree_ball(R):
    """All vertices within distance R of v0 = K, as matrices."""
    v0 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    nbrs = [[[Fr(p), Fr(b)], [Fr(0), Fr(1)]] for b in range(p)] + [[[Fr(1), Fr(0)], [Fr(0), Fr(p)]]]
    seen = {canon(v0): v0}
    frontier = [v0]
    for _ in range(R):
        new = []
        for g in frontier:
            for n in nbrs:
                h = mat_mul(g, n)
                key = canon(h)
                if key not in seen:
                    seen[key] = h
                    new.append(h)
        frontier = new
    return list(seen.values())


def orbital_counts(gamma, R):
    verts = tree_ball(R)
    counts = {}
    for g in verts:
        d = dist(g, mat_mul(gamma, g))
        counts[d] = counts.get(d, 0) + 1
    return counts, len(verts)


# ---------- spectral side ----------
Q = 1 + 1 / q  # corrected Macdonald constant  sum_w q^{-l(w)}


def Gamma(z, n):
    """Macdonald spherical function at a_n = diag(pi^n,1), n >= 0, unramified char z."""
    y = z * z
    c1 = (1 - y**-1 / q) / (1 - y**-1)
    c2 = (1 - y / q) / (1 - y)
    return q ** (-n / 2) / Q * (z**n * c1 + z**(-n) * c2)


def vol(n):
    return 1 if n == 0 else (q + 1) * q ** (n - 1)


def fvee(z, n):  # Satake/Fourier transform of 1_{K a_n K}
    return vol(n) * Gamma(z, n)


def rho(z):  # Plancherel density w.r.t. normalized dtheta/2pi on |z|=1
    y = z * z
    return Q / 2 * abs(1 - y) ** 2 / abs(1 - y / q) ** 2


def I_unram(z, r):
    y = z * z
    B = 1 + (q + 1) * (q**r - 1) / (q - 1)
    return B - q**r * (y * y - 2 * y / q + 1) / (1 - y) ** 2


def I_ram_unit(z, r):
    y = z * z
    B = 2 * (q ** (r + 1) - 1) / (q - 1)
    return B - 2 * q ** (r + 1) / (q + 1) * (y * y - 2 * y / q + 1) / (1 - y) ** 2


def I_ram_odd(z):
    y = z * z
    return -2 * q**0.5 / (q + 1) * (1 - 1 / q) * z * (1 + y) / (1 - y) ** 2


def spectral(fn_n, Ifun, N=400000):
    th = (np.arange(N) + 0.5) / N * 2 * np.pi  # midpoint rule avoids z = +-1 exactly
    z = np.exp(1j * th)
    return np.mean(fvee(z, fn_n) * Ifun(z) * rho(z)).real


if __name__ == "__main__":
    np.seterr(all="ignore")
    print("Check (2): Plancherel inversion  f_n(a_m) = int f_n^vee Gamma(a_m) dmu")
    th = (np.arange(200000) + 0.5) / 200000 * 2 * np.pi
    z = np.exp(1j * th)
    for n in range(4):
        row = [np.mean(fvee(z, n) * Gamma(z, m) * rho(z)).real for m in range(4)]
        print("  n=%d:" % n, " ".join("%7.4f" % x for x in row))
        for m in range(4):
            assert abs(row[m] - (1.0 if n == m else 0.0)) < 1e-6, ("Plancherel inversion", n, m)

    R = 7
    cases = [
        ("unramified, depth 0", [[0, -1], [1, 0]], lambda z: I_unram(z, 0)),
        ("unramified, depth 1", [[1, -3], [3, 1]], lambda z: I_unram(z, 1)),
        ("ramified unit, depth 0", [[1, 3], [1, 1]], lambda z: I_ram_unit(z, 0)),
        ("ramified, odd (pi_E)", [[0, 3], [1, 0]], I_ram_odd),
    ]
    for name, gam, Ifun in cases:
        gamma = [[Fr(x) for x in row] for row in gam]
        counts, nv = orbital_counts(gamma, R)
        print("\nCheck (1)+(3): gamma =", gam, "(%s); ball of radius %d has %d vertices" % (name, R, nv))
        print("   n   tree count O(f_n)   spectral int f_n^vee I dmu")
        for n in range(0, 8):
            s = spectral(n, Ifun)
            print("  %2d   %10d          %14.6f" % (n, counts.get(n, 0), s))
            assert abs(s - counts.get(n, 0)) < 1e-5, ("spectral identity", name, n)

    print("\nCheck (4): truncation. For f = f_4 and gamma unramified depth 0,")
    print("I^M(z) = sum_{n<=2M} O(f_n) Gamma_z(a_n); compare int f^vee I^M dmu with O(f_4) = %d" % ((q + 1) * q))
    for M in range(0, 5):
        def IM(z, M=M):
            tot = 1.0 * Gamma(z, 0)
            for m in range(1, M + 1):
                tot = tot + (q + 1) * q ** (m - 1) * Gamma(z, 2 * m)
            return tot
        val = spectral(4, IM)
        print("  M=%d: %10.6f" % (M, val))
        assert abs(val - (12 if M >= 2 else 0)) < 1e-6, ("truncation", M)

    print("\nALL CHECKS PASSED")

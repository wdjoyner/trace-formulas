# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Running example of "On the twisted adjoint lifting for p-adic PGL(3)" (F = Q_3).

For B in GL_2(Z_3) put C = -B w, w = [[0,1],[-1,0]], and A_a = diag(a, C).
The normalized twisted action on vertices of the building of PGL_3(Q_3) is

    T_A [L] = [A L^vee],   L^vee = dual lattice for the standard dot product.

The script lists the vertices fixed by T_{A_a}, a = 1 and a = 3, inside the
ball of a given radius about [Z_3^3], and compares the counts with the
fixed vertices of h = C (C^T)^{-1} and of h' = 1 + h on the tree of
PGL_2(Q_3).  Everything is exact integer arithmetic; a lattice is stored by
its Hermite normal form modulo a high power of 3.
"""
from fractions import Fraction
from itertools import product
import sys

P = 3
N = 14                      # working precision: lattices contain P^N Z^n
MOD = P ** N


def val(x):
    """3-adic valuation of an integer mod 3^N (N for zero)."""
    x %= MOD
    if x == 0:
        return N
    v = 0
    while x % P == 0:
        x //= P
        v += 1
    return v


def hnf(cols):
    """Canonical basis of the Z_3-lattice spanned by integer columns.

    Returns a tuple of rows of a lower triangular matrix with diagonal
    3^{e_i} and reduced entries to the left of each pivot.  The lattice is
    assumed to have full rank and to contain 3^N Z^n.
    """
    n = len(cols[0])
    cols = [[x % MOD for x in c] for c in cols]
    for i in range(n):
        j = min(range(i, len(cols)), key=lambda t: val(cols[t][i]))
        cols[i], cols[j] = cols[j], cols[i]
        v = val(cols[i][i])
        assert v < N, "precision too low"
        u = (cols[i][i] // P ** v) % MOD
        uinv = pow(u, -1, MOD)
        cols[i] = [(x * uinv) % MOD for x in cols[i]]
        for t in range(len(cols)):
            if t != i and t > i:
                m = (cols[t][i] // P ** v) % MOD
                cols[t] = [(x - m * y) % MOD for x, y in zip(cols[t], cols[i])]
    cols = cols[:n]
    # reduce entries to the left of each pivot
    for i in range(n):
        piv = cols[i][i]
        for t in range(i):
            m = cols[t][i] // piv
            cols[t] = [(x - m * y) for x, y in zip(cols[t], cols[i])]
    # entries below the pivots are only defined modulo the later pivots;
    # the loop above has reduced them.  Normalize the homothety class.
    g = min(val(x) for c in cols for x in c if x % MOD)
    cols = [[x // P ** g for x in c] for c in cols]
    # after dividing, reduce once more
    for i in range(n):
        piv = cols[i][i]
        for t in range(i):
            m = cols[t][i] // piv
            cols[t] = [(x - m * y) for x, y in zip(cols[t], cols[i])]
    return tuple(tuple(cols[j][i] for j in range(n)) for i in range(n))


def columns(M):
    n = len(M)
    return [[M[i][j] for i in range(n)] for j in range(len(M[0]))]


def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y)))
             for j in range(len(Y[0]))] for i in range(len(X))]


def inverse_transpose(M):
    """(M^T)^{-1} with Fraction entries (M lower triangular or general)."""
    n = len(M)
    A = [[Fraction(M[j][i]) for j in range(n)] +
         [Fraction(int(i == k)) for k in range(n)] for i in range(n)]
    for i in range(n):
        p = next(r for r in range(i, n) if A[r][i] != 0)
        A[i], A[p] = A[p], A[i]
        A[i] = [x / A[i][i] for x in A[i]]
        for r in range(n):
            if r != i and A[r][i] != 0:
                A[r] = [x - A[r][i] * y for x, y in zip(A[r], A[i])]
    return [row[n:] for row in A]


def clear(M):
    """Scale a rational matrix by a power of 3 and by 3-adic units to integers."""
    den = 1
    for row in M:
        for x in row:
            d = x.denominator
            while d % P == 0:
                d //= P
                den = max(den, x.denominator // d)
    out = []
    for row in M:
        r = []
        for x in row:
            y = x * den
            # y has denominator prime to 3: invert it modulo 3^N
            r.append((y.numerator * pow(y.denominator, -1, MOD)) % MOD)
        out.append(r)
    return out


def act(G, L):
    """Class of G L for an integer matrix G."""
    return hnf(columns(matmul(G, [list(r) for r in L])))


def twisted(A, L):
    """Class of A L^vee."""
    D = clear(inverse_transpose([list(r) for r in L]))
    return hnf(columns(matmul(A, D)))


def neighbors(L):
    """Vertices adjacent to [L]: lattices strictly between L and 3L."""
    n = len(L)
    M = [list(r) for r in L]
    base = columns(M)
    out = set()
    for coeffs in product(range(P), repeat=n):
        if not any(coeffs):
            continue
        lead = next(c for c in coeffs if c)
        if lead != 1:
            continue
        v = [sum(coeffs[j] * base[j][i] for j in range(n)) for i in range(n)]
        # line: 3L + <v>
        out.add(hnf([[P * x for x in c] for c in base] + [v]))
        if n == 3:
            # plane: kernel of the functional coeffs on L/3L
            gens = [[P * x for x in c] for c in base]
            for w in product(range(P), repeat=n):
                if sum(a * b for a, b in zip(coeffs, w)) % P == 0 and any(w):
                    gens.append([sum(w[j] * base[j][i] for j in range(n))
                                 for i in range(n)])
            out.add(hnf(gens))
    return out


def ball(n, radius):
    """Vertices within the given distance of [Z_3^n], with their distances."""
    L0 = hnf([[int(i == j) for i in range(n)] for j in range(n)])
    dist = {L0: 0}
    frontier = [L0]
    for d in range(1, radius + 1):
        new = []
        for L in frontier:
            for M in neighbors(L):
                if M not in dist:
                    dist[M] = d
                    new.append(M)
        frontier = new
    return dist


W = [[0, 1], [-1, 0]]


def setup(B):
    C = [[-x for x in row] for row in matmul(B, W)]
    detC = C[0][0] * C[1][1] - C[0][1] * C[1][0]
    # h = C (C^T)^{-1};  (C^T)^{-1} = adj / det
    CTinv = [[Fraction(C[1][1], detC), Fraction(-C[1][0], detC)],
             [Fraction(-C[0][1], detC), Fraction(C[0][0], detC)]]
    h = [[sum(C[i][k] * CTinv[k][j] for k in range(2)) for j in range(2)]
         for i in range(2)]
    return C, h


def in_Z(L):
    """Is [L] of the form [3^n Z e_0 + Lambda]?"""
    return L[1][0] == 0 and L[2][0] == 0


def run(name, B, radius, expect):
    """expect = (|Fix h|, |Fix h'|, |Fix B|, {a: (total, in Z)})."""
    C, h = setup(B)
    hint = clear(h)
    hprime = clear([[h[i][j] + int(i == j) for j in range(2)] for i in range(2)])
    tree = ball(2, radius + 1)
    fix_h = [L for L in tree if act(hint, L) == L]
    fix_hp = [L for L in tree if act(hprime, L) == L]
    fix_B = [L for L in tree if act(B, L) == L]
    bldg = ball(3, radius)
    print("-" * 70)
    print(name, " B =", B, " C =", C)
    print("  h =", [[str(x) for x in r] for r in h])
    print("  tree: |Fix(h)| = %d, |Fix(h')| = %d, |Fix(B)| = %d"
          % (len(fix_h), len(fix_hp), len(fix_B)))
    counts = {}
    for a in sorted(expect[3]):
        A = [[a, 0, 0], [0, C[0][0], C[0][1]], [0, C[1][0], C[1][1]]]
        fixed = sorted(L for L in bldg if twisted(A, L) == L)
        inside = [L for L in fixed if in_Z(L)]
        counts[a] = (len(fixed), len(inside))
        print("  a = %d: %d fixed vertices (%d in Z, %d outside), "
              "max distance from [Z_3^3] = %s"
              % (a, len(fixed), len(inside), len(fixed) - len(inside),
                 max([bldg[L] for L in fixed], default="-")))
        if len(fixed) <= 6:
            for L in fixed:
                # columns of the printed matrix are a Z_3-basis of the lattice
                print("      ", [list(r) for r in L],
                      "in Z" if in_Z(L) else "leaf", " dist", bldg[L])
    got = (len(fix_h), len(fix_hp), len(fix_B), counts)
    ok = got == expect
    print("  expected", expect, "->", "OK" if ok else "MISMATCH %s" % (got,))
    return ok


def alternating_sphere_check(q, mmax):
    """sum_{j<=m} (-1)^j |S_j| = (-1)^m q^m on the (q+1)-regular tree."""
    ok = True
    for m in range(mmax + 1):
        spheres = [1] + [(q + 1) * q ** (j - 1) for j in range(1, m + 1)]
        alt = sum((-1) ** j * x for j, x in enumerate(spheres))
        big = sum(x for j, x in enumerate(spheres) if (m - j) % 2 == 0)
        small = sum(spheres) - big
        ok &= alt == (-1) ** m * q ** m
        ok &= big == (q ** (m + 1) - 1) // (q - 1)
        ok &= small == (q ** m - 1) // (q - 1)
    return ok


if __name__ == "__main__":
    radius = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    ok = True
    ok &= run("Specimen I    (unramified, k'=0, m=0)", [[1, -1], [1, 1]],
              radius, (1, 1, 1, {1: (1, 1), 3: (0, 0)}))
    ok &= run("Specimen II   (unramified, k'=1, m=0)", [[3, -1], [1, 0]],
              radius, (5, 5, 1, {1: (5, 1), 2: (5, 1), 3: (0, 0)}))
    ok &= run("Specimen III  (unramified, k'=0, m=1)", [[1, -3], [3, 1]],
              radius, (5, 1, 5, {1: (1, 1), 3: (4, 4)}))
    ok &= run("Specimen III' (unramified, k'=0, m=2)", [[1, -9], [9, 1]],
              radius, (17, 1, 17, {1: (13, 13), 3: (4, 4)}))
    ok &= run("Specimen IV   (ramified)", [[1, 3], [1, 1]],
              radius, (2, 0, 2, {1: (1, 1), 2: (1, 1), 3: (1, 1), 6: (1, 1)}))
    print("-" * 70)
    alt = all(alternating_sphere_check(q, 8) for q in (2, 3, 4, 5, 7, 9))
    print("alternating sphere sums:", "OK" if alt else "MISMATCH")
    ok &= alt
    print("all checks passed" if ok else "SOME CHECKS FAILED")
    sys.exit(0 if ok else 1)

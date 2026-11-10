# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""
Bruhat-Tits building of PGL(3, Q_p): vertices = homothety classes of Z_p-lattices in Q_p^3.
A lattice L = H Z_p^3 is stored by a canonical upper-triangular integer matrix H
(column Hermite normal form over Z_p, primitive).  Vector distance d(L, L') is the
dominant coweight (l1 >= l2 >= 0) given by the elementary divisors of H^{-1} H'.
Prepared by Claude (Anthropic) for D. Joyner, 2026.
"""
from fractions import Fraction as Fr


def vp(x, p):
    if x == 0:
        return 10**9
    x = Fr(x)
    n, d, v = x.numerator, x.denominator, 0
    while n % p == 0:
        n //= p; v += 1
    while d % p == 0:
        d //= p; v -= 1
    return v


def residue(x, p, e):
    """x in Z_(p) (a Fraction with p-free denominator), returned as an integer in [0, p^e)."""
    if e <= 0:
        return 0
    m = p ** e
    x = Fr(x)
    return (x.numerator * pow(x.denominator, -1, m)) % m


def canon(cols, p):
    """cols: list of 3 column vectors (Fractions) spanning a lattice. Returns canonical key and matrix."""
    c = [list(map(Fr, col)) for col in cols]
    # bottom row: pick column of minimal valuation in row 2, move to position 2
    for row, last in ((2, 2), (1, 1)):
        cand = range(0, last + 1)
        j = min(cand, key=lambda k: vp(c[k][row], p))
        c[j], c[last] = c[last], c[j]
        piv = c[last][row]
        e = vp(piv, p)
        u = piv / Fr(p) ** e
        c[last] = [x / u for x in c[last]]          # now c[last][row] = p^e
        for k in range(0, last):
            if c[k][row] != 0:
                t = c[k][row] / c[last][row]        # in Z_(p)
                c[k] = [a - t * b for a, b in zip(c[k], c[last])]
    piv = c[0][0]
    e = vp(piv, p)
    c[0] = [x / (piv / Fr(p) ** e) for x in c[0]]
    e1, e2, e3 = vp(c[0][0], p), vp(c[1][1], p), vp(c[2][2], p)
    # reduce off-diagonal entries: H = [[p^e1, x12, x13], [0, p^e2, x23], [0, 0, p^e3]]
    x23 = c[2][1]
    # subtract multiple of column 1 (index 1) to bring x23 into [0, p^e2)
    t = (x23 - residue(x23, p, e2)) / Fr(p) ** e2 if e2 > 0 else x23
    c[2] = [a - t * b for a, b in zip(c[2], c[1])]
    for k in (1, 2):
        x = c[k][0]
        t = (x - residue(x, p, e1)) / Fr(p) ** e1 if e1 > 0 else x
        c[k] = [a - t * b for a, b in zip(c[k], c[0])]
    H = [[c[j][i] for j in range(3)] for i in range(3)]
    m = min(vp(H[i][j], p) for i in range(3) for j in range(3) if H[i][j] != 0)
    H = [[x / Fr(p) ** m for x in row] for row in H]
    for row in H:
        for x in row:
            assert x.denominator == 1
    key = tuple(int(H[i][j]) for i in range(3) for j in range(i, 3))
    return key, [[int(x) for x in row] for row in H]


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def adj3(A):
    C = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            r = [x for x in range(3) if x != i]
            s = [x for x in range(3) if x != j]
            m = A[r[0]][s[0]] * A[r[1]][s[1]] - A[r[0]][s[1]] * A[r[1]][s[0]]
            C[j][i] = (-1) ** (i + j) * m
    return C


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def elem_div(M, p):
    """Valuations e1<=e2<=e3 of elementary divisors of an integer matrix M (det != 0)."""
    v1 = min(vp(x, p) for row in M for x in row if x != 0)
    minors = adj3(M)
    v12 = min(vp(x, p) for row in minors for x in row if x != 0)
    v123 = vp(det3(M), p)
    return v1, v12 - v1, v123 - v12


def vdist(H1, H2, p):
    """Vector distance (l1, l2), l1 >= l2 >= 0, between lattices H1 Z^3 and H2 Z^3."""
    M = matmul(adj3(H1), H2)          # = det(H1) * H1^{-1} H2
    e = elem_div(M, p)
    return (e[2] - e[0], e[1] - e[0])


def neighbors(H, p):
    """All lattices L' with pL < L' < L (proper), as column lists, for L = H Z^3."""
    import itertools
    cols = [[H[i][j] for i in range(3)] for j in range(3)]
    out = []
    # L' = pL + span of a subspace of L/pL = F_p^3 (dimension 1 or 2)
    vecs = [v for v in itertools.product(range(p), repeat=3) if any(v)]
    lines = set()
    for v in vecs:
        # normalize projective point
        k = next(i for i in range(3) if v[i])
        inv = pow(v[k], -1, p)
        lines.add(tuple((x * inv) % p for x in v))
    lines = sorted(lines)
    def comb(v):
        return [sum(v[j] * cols[j][i] for j in range(3)) for i in range(3)]
    pL = [[p * x for x in col] for col in cols]
    for v in lines:                         # dim 1 subspaces
        out.append(pL + [comb(v)])
    for v in lines:                         # dim 2 subspaces = kernels of linear forms v
        basis = [w for w in lines if sum(a * b for a, b in zip(v, w)) % p == 0]
        # pick two independent vectors in the kernel
        b1 = basis[0]
        b2 = next(w for w in basis[1:] if any((w[i] * b1[j] - w[j] * b1[i]) % p for i in range(3) for j in range(3)))
        out.append(pL + [comb(b1), comb(b2)])
    return out


def ball(R, p):
    """Vertices at graph distance <= R from v0 = Z_p^3, as dict key -> H."""
    I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    k0, H0 = canon([[1, 0, 0], [0, 1, 0], [0, 0, 1]], p)
    seen = {k0: H0}
    frontier = [H0]
    for _ in range(R):
        new = []
        for H in frontier:
            for gens in neighbors(H, p):
                # reduce generating set (4 or 5 vectors) to a basis via canon on 3 vectors:
                # use HNF of the integer span by successive canonicalization
                key, Hn = canon_span(gens, p)
                if key not in seen:
                    seen[key] = Hn
                    new.append(Hn)
        frontier = new
    return seen


def canon_span(gens, p):
    """Canonical form of the Z_p-span of >=3 integer vectors spanning a full lattice."""
    vecs = [list(map(Fr, g)) for g in gens]
    # column-reduce: for row 2,1,0 choose minimal valuation pivot among remaining vectors
    basis = []
    rest = vecs
    for row in (2, 1, 0):
        j = min(range(len(rest)), key=lambda k: vp(rest[k][row], p))
        piv = rest[j]
        others = [r for k, r in enumerate(rest) if k != j]
        newrest = []
        for r in others:
            if r[row] != 0:
                t = r[row] / piv[row]
                r = [a - t * b for a, b in zip(r, piv)]
            newrest.append(r)
        basis.append(piv)
        rest = [r for r in newrest if any(x != 0 for x in r)]
    cols = [basis[2], basis[1], basis[0]]
    return canon(cols, p)

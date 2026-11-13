# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Complete saturation check for the semigroup S of Z (G_2).

Every generator of S has lam-degree 0 or 1, so for any simplicial subcone spanned by 7
linearly independent generators the half-open fundamental parallelepiped contains only
lattice points of lam-degree <= 6, with z-coordinates <= 0 and w-coordinates <= degree.
S is saturated iff all lattice points of cone(S) in that range lie in S.
Cone membership uses the facet inequalities (computed in g2_toric_divisors.py).
"""
import itertools
import numpy as np

E = np.eye(7, dtype=int)
roots = {'a': (1, 0), 'b': (0, 1), 'g': (1, 1), 'd': (2, 1), 'e': (3, 1), 'z': (3, 2)}
widx = {'g': 3, 'd': 4, 'e': 5, 'z': 6}


def xvec(r):
    ma, mb = roots[r]
    v = E[0] - ma * E[1] - mb * E[2]
    if r in widx:
        v = v + E[widx[r]]
    return v


gens = [E[i] for i in range(7)] + [xvec(r) for r in roots]
facets = np.array([
    (1, 1, 1, 1, 2, 3, 4), (1, 0, 1, 0, 0, 0, 1), (1, 1, 0, 0, 1, 2, 2), (2, 1, 0, 0, 0, 1, 1),
    (3, 1, 0, 0, 0, 0, 0), (2, 0, 1, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 1, 0, 0, 0)])
G = np.array(gens)
assert np.all(G @ facets.T >= 0)
# every facet must contain 6 linearly independent generators
for u in facets:
    on = G[G @ u == 0]
    assert np.linalg.matrix_rank(on) == 6, u

deg1 = np.array([xvec(r) for r in roots] + [E[0]])  # lam-degree-1 generators
total_bad = 0
for k in range(1, 7):
    # all sums of k degree-1 generators (multisets); S at degree k = these + nonneg (coords 1..6)
    sums = np.array([sum(deg1[list(c)]) for c in
                     itertools.combinations_with_replacement(range(len(deg1)), k)])
    grid = np.array(np.meshgrid(np.arange(-3 * k, 1), np.arange(-2 * k, 1),
                                *[np.arange(0, k + 1)] * 4, indexing='ij')).reshape(6, -1).T
    pts = np.hstack([np.full((len(grid), 1), k), grid])
    incone = np.all(pts @ facets.T >= 0, axis=1)
    pts = pts[incone]
    inS = np.zeros(len(pts), dtype=bool)
    for s in sums:
        inS |= np.all(pts[:, 1:] >= s[1:], axis=1)
    bad = pts[~inS]
    total_bad += len(bad)
    print(f"degree {k}: {len(pts)} lattice points in cone, {len(bad)} not in S")
print("S saturated (Z normal):", total_bad == 0)

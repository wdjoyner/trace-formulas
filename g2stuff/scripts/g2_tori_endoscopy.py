# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Elliptic tori of split G_2 over a p-adic field: H^1(F,T) and endoscopic root systems.

Tate-Nakayama: for T split by K/F with Gamma = Gal(K/F) acting on X_*(T) through a subgroup
of the Weyl group W, and T elliptic (X_*^Gamma = 0),
    H^1(F,T) = H^{-1}(Gamma, X_*) = X_* / I_Gamma X_*,   I_Gamma X_* = span{(g-1)x}.
A character kappa of this group gives s in hat T^Gamma; the roots of the endoscopic group H
(transported to T) are the roots a of G with kappa(a^vee) = 1.

Coroot lattice basis: a^vee (long coroot of the short simple root a), b^vee.
"""
import itertools
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

# pairings <root, coroot>
# roots in basis (a, b); coroots in basis (a^vee, b^vee)
roots = {'a': (1, 0), 'b': (0, 1), 'g': (1, 1), 'd': (2, 1), 'e': (3, 1), 'z': (3, 2)}
cartan = np.array([[2, -1], [-3, 2]])  # <a,a^v>=2, <a,b^v>=-1, <b,a^v>=-3, <b,b^v>=2
coroots = {'a': (1, 0), 'b': (0, 1), 'g': (1, 3), 'd': (2, 3), 'e': (1, 1), 'z': (1, 2)}


def pair(root, cor):
    r = np.array(root); c = np.array(cor)
    return int(r @ cartan @ c)


for k in roots:
    assert pair(roots[k], coroots[k]) == 2


def refl(k):
    """matrix of s_k on coroot lattice, columns = images of a^v, b^v"""
    cols = []
    for v in [(1, 0), (0, 1)]:
        img = np.array(v) - pair(roots[k], v) * np.array(coroots[k])
        cols.append(img)
    return np.array(cols).T


sa, sb = refl('a'), refl('b')
M = sb @ sa
print("s_b s_a on coroots (columns images of a^v, b^v):\n", M, " trace", np.trace(M), " det", round(np.linalg.det(M)))
print("paper's formula (2m-n, m-n) has matrix [[2,-1],[1,-1]], det", round(np.linalg.det(np.array([[2, -1], [1, -1]]))))
print("paper's cubic formula (-3n, m-3n): matrix [[0,-3],[1,-3]], det",
      round(np.linalg.det(np.array([[0, -3], [1, -3]]))))
print("(s_b s_a)^2 =\n", M @ M)

# generate W
W = {tuple(np.eye(2, dtype=int).flatten())}
frontier = [np.eye(2, dtype=int)]
while frontier:
    g = frontier.pop()
    for s in (sa, sb):
        h = s @ g
        t = tuple(h.flatten())
        if t not in W:
            W.add(t); frontier.append(h)
W = [np.array(t).reshape(2, 2) for t in W]
assert len(W) == 12


def subgroup(gens):
    S = {tuple(np.eye(2, dtype=int).flatten())}
    fr = [np.eye(2, dtype=int)]
    while fr:
        g = fr.pop()
        for s in gens:
            h = s @ g
            t = tuple(h.flatten())
            if t not in S:
                S.add(t); fr.append(h)
    return frozenset(S)


subs = set()
for r in range(1, 3):
    for gens in itertools.combinations(W, r):
        subs.add(subgroup(gens))


def name_of(m):
    for k in roots:
        if np.array_equal(m, refl(k)):
            return 's_' + k
    if np.array_equal(m, -np.eye(2, dtype=int)):
        return '-1'
    if np.array_equal(m, np.eye(2, dtype=int)):
        return '1'
    o = 1; p = m.copy()
    while not np.array_equal(p, np.eye(2, dtype=int)):
        p = p @ m; o += 1
    return f'rot{o}'


print("\nElliptic Galois images Gamma in W (no nonzero fixed coroots), H^1(F,T), endoscopic roots:")
for S in sorted(subs, key=len):
    mats = [np.array(t).reshape(2, 2) for t in S]
    fixed = sp.Matrix.vstack(*[sp.Matrix(m - np.eye(2, dtype=int)) for m in mats]).nullspace()
    if fixed:
        continue
    cols = [ (m - np.eye(2, dtype=int)) for m in mats]
    A = sp.Matrix(np.hstack(cols))
    snf = smith_normal_form(A, domain=sp.ZZ)
    inv = [abs(snf[i, i]) for i in range(2)]
    elts = sorted(name_of(m) for m in mats)
    print(f"|Gamma|={len(S)} {elts}: H^1 = " + " x ".join(f"Z/{d}" for d in inv if d != 1) or "0")
    if all(d == 1 for d in inv):
        print("   H^1 trivial")
        continue
    # enumerate characters of X_*/I : test kappa on coroots via a basis of the quotient
    Ivecs = [np.array(c[:, j]) for c in cols for j in range(2)]
    # brute force: characters of Z^2 trivial on I, values in roots of unity of order dividing 6
    for p in range(6):
        for q in range(6):
            ok = all((p * v[0] + q * v[1]) % 6 == 0 for v in Ivecs)
            if not ok or (p, q) == (0, 0):
                continue
            Hroots = [k for k, c in coroots.items() if (p * c[0] + q * c[1]) % 6 == 0]
            print(f"   kappa(a^v,b^v)=exp(2 pi i ({p},{q})/6): H positive roots {Hroots}")

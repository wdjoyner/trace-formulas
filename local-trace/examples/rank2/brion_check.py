# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""
Rank-two check of the vertex decomposition (Lemma 3.5A) of the revised paper
"Simple local trace formulas for unramified p-adic groups" (2026).

For G = SL(3) (X_*(A) = coroot lattice) and G = PGL(3) (X_*(A) = coweight lattice,
where the dominant cone is NOT unimodular in the root coordinates) we compute, by
brute-force enumeration of lattice points, the truncated sums

    S(T) = sum_{lambda in A_A(T)} c(lambda) psi(lambda),
    A_A(T) = {lambda : <lambda,alpha> >= 0, <lambda - T, varpi_alpha> < 0  (alpha simple)},

for a fixed character psi(lambda) = x^a y^b (x, y rational, exact arithmetic) and
weights c = 1 or c(lambda) = Q_lambda (Macdonald's weights (3.7), q = 3).
Lemma 3.5A predicts S(T) = sum_Q psi(T_Q) R_Q with R_Q independent of T, the sum over the
four standard parabolics Q = B, P1, P2, G of SL(3)/PGL(3).

Check: solve for R_B, R_P1, R_P2, R_G from four values of T and verify the prediction
exactly on many further T in the lattice L_0; also check R_G against the (convergent)
sum over the whole dominant cone.  Also checks the strict/non-strict (half-open) faces:
changing "<" to "<=" in the truncation must break the identity with the same R_Q.
For the degenerate character psi = 1 it checks that S(T) is a polynomial on L_0
(Lemma 3.5B(ii): vertex terms become psi(T_Q) times polynomials in T).
Prepared by Claude (Anthropic) for D. Joyner, 2026.
"""
from fractions import Fraction as Fr
import itertools

q = 3
QG = (1 + Fr(1, q)) * (1 + Fr(1, q) + Fr(1, q * q))
Q2 = 1 + Fr(1, q)


def weight(r1, r2, weighted):
    """Q_lambda = Q_G / Q_{W_lambda}, from the face of the dominant cone; r_i = <lambda, alpha_i>."""
    if not weighted:
        return 1
    if r1 == 0 and r2 == 0:
        return 1
    if r1 == 0 or r2 == 0:
        return QG / Q2
    return QG


def setup(group):
    """Return (pairing data) for lattice coords (a,b):
    roots(a,b) -> (<lam,a1>,<lam,a2>), weights(a,b) -> (<lam,w1>,<lam,w2>) times 3,
    and the projections T_Q in lattice coordinates."""
    if group == "SL3":   # lambda = a a1v + b a2v
        roots = lambda a, b: (2 * a - b, 2 * b - a)
        wts3 = lambda a, b: (3 * a, 3 * b)
        # T_Q: Q=P1 has alpha1 in its Levi: <x,a1>=0, <x,w2>=<T,w2>  -> (T2/2, T2)
        proj = {"B": lambda t: t, "G": lambda t: (0, 0),
                "P1": lambda t: (Fr(t[1], 2), t[1]), "P2": lambda t: (t[0], Fr(t[0], 2))}
    else:                # PGL3: lambda = a w1v + b w2v
        roots = lambda a, b: (a, b)
        wts3 = lambda a, b: (2 * a + b, a + 2 * b)
        proj = {"B": lambda t: t, "G": lambda t: (0, 0),
                "P1": lambda t: (0, Fr(t[0] + 2 * t[1], 2)), "P2": lambda t: (Fr(2 * t[0] + t[1], 2), 0)}
    return roots, wts3, proj


def S(group, T, x, y, weighted, strict=True):
    roots, wts3, _ = setup(group)
    WT = wts3(*T)
    tot = Fr(0)
    R = 4 * (abs(T[0]) + abs(T[1])) + 4
    for a in range(-R, R + 1):
        for b in range(-R, R + 1):
            r1, r2 = roots(a, b)
            if r1 < 0 or r2 < 0:
                continue
            w1, w2 = wts3(a, b)
            ok = (w1 < WT[0] and w2 < WT[1]) if strict else (w1 <= WT[0] and w2 <= WT[1])
            if ok:
                tot += weight(r1, r2, weighted) * x ** a * y ** b
    return tot


def psi_at(pt, x, y):
    a, b = pt
    assert Fr(a).denominator == 1 and Fr(b).denominator == 1, "T_Q not a lattice point"
    return x ** int(a) * y ** int(b)


def solve(Mat, rhs):
    n = len(rhs)
    A = [row[:] + [rhs[i]] for i, row in enumerate(Mat)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c] / A[c][c]
                A[r] = [u - f * v for u, v in zip(A[r], A[c])]
    return [A[i][n] / A[i][i] for i in range(n)]


def rank(M):
    A = [r[:] for r in M]
    rk, cols = 0, len(A[0])
    for c in range(cols):
        p = next((r for r in range(rk, len(A)) if A[r][c] != 0), None)
        if p is None:
            continue
        A[rk], A[p] = A[p], A[rk]
        for r in range(len(A)):
            if r != rk and A[r][c] != 0:
                f = A[r][c] / A[rk][c]
                A[r] = [u - f * v for u, v in zip(A[r], A[rk])]
        rk += 1
    return rk


def regular_T(group, t):
    roots, _, _ = setup(group)
    r1, r2 = roots(*t)
    return r1 > 0 and r2 > 0


if __name__ == "__main__":
    x, y = Fr(2, 3), Fr(5, 7)
    Qs = ["B", "P1", "P2", "G"]
    for group in ["SL3", "PGL3"]:
        _, _, proj = setup(group)
        # lattice L_0: all T_Q integral; take even coordinates
        Ts = [t for t in itertools.product(range(2, 15, 2), repeat=2) if regular_T(group, t)]
        for weighted in (False, True):
            # choose four T giving an invertible system, test on all the others
            fit = []
            for t in Ts:
                trial = fit + [t]
                M_ = [[psi_at(proj[Qn](u), x, y) for Qn in Qs] for u in trial]
                if rank(M_) == len(trial):
                    fit = trial
                if len(fit) == 4:
                    break
            test = [t for t in Ts if t not in fit]
            Mat = [[psi_at(proj[Qn](t), x, y) for Qn in Qs] for t in fit]
            rhs = [S(group, t, x, y, weighted) for t in fit]
            Rq = solve(Mat, rhs)
            for t in test:
                pred = sum(psi_at(proj[Qn](t), x, y) * Rq[i] for i, Qn in enumerate(Qs))
                assert pred == S(group, t, x, y, weighted), (group, weighted, t)
            # R_G vs the full dominant-cone sum (partial sums converge geometrically)
            roots, _, _ = setup(group)
            full = 0.0
            for a in range(0, 400):
                for b in range(0, 400):
                    r1, r2 = roots(a, b)
                    if r1 >= 0 and r2 >= 0:
                        full += float(weight(r1, r2, weighted)) * float(x) ** a * float(y) ** b
            assert abs(full - float(Rq[3])) < 1e-9, (group, weighted, full, float(Rq[3]))
            # half-open faces matter: non-strict truncation is NOT given by the same R_Q
            t = test[0]
            pred = sum(psi_at(proj[Qn](t), x, y) * Rq[i] for i, Qn in enumerate(Qs))
            assert pred != S(group, t, x, y, weighted, strict=False)
            print("%-5s weights=%-5s: vertex decomposition exact on %d further T; R_G = dominant-cone sum (%.12f)"
                  % (group, "Q_lam" if weighted else "1", len(test), full))
    # Degenerate character psi = 1 (Lemma 3.5B(ii)): S(T) is a polynomial of degree <= 2 on L_0.
    for group in ["SL3", "PGL3"]:
        Ts = [t for t in itertools.product(range(2, 21, 2), repeat=2) if regular_T(group, t)]
        mono = lambda t: [Fr(1), Fr(t[0]), Fr(t[1]), Fr(t[0] ** 2), Fr(t[0] * t[1]), Fr(t[1] ** 2)]
        for weighted in (False, True):
            fit = []
            for t in Ts:
                if rank([mono(u) for u in fit + [t]]) == len(fit) + 1:
                    fit.append(t)
                if len(fit) == 6:
                    break
            coef = solve([mono(t) for t in fit], [S(group, t, Fr(1), Fr(1), weighted) for t in fit])
            for t in Ts:
                assert sum(c * m for c, m in zip(coef, mono(t))) == S(group, t, Fr(1), Fr(1), weighted)
            print("%-5s weights=%-5s, psi = 1: S(T) is a quadratic polynomial on L_0 (checked on %d T)"
                  % (group, "Q_lam" if weighted else "1", len(Ts)))
    print("\nALL CHECKS PASSED")

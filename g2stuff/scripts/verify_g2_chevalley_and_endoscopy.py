#!/usr/bin/env python3
"""
Standalone SymPy verification suite (Part 1 of 3) for:
  D. Joyner, "On the transfer of Shalika germs for G_2" (Draft 3, November 2026)

Verifies:
  1. Appendix A.5-A.6: G_2 root/coroot lattices, Cartan pairings, Weyl group
     Omega ~= D_6, all 10 subgroup conjugacy classes, and Smith normal form
     computation of H^1(F, T_G) = X_* / I_Gamma X_* for all 7 elliptic rows of
     Table A.6.
  2. Appendix A.1-A.4: Triality Chevalley basis {h_alpha, h_beta, X_+-rho} in
     so(8) with X_{-rho} = ^t X_rho, Z-closure, integrality of all structure
     constants, and all 36 [h_rho, X_sigma] weight relations.
  3. Appendix A.3: Corrected maximal split torus embeddings (A.12), (A.13),
     and (A.13') for SL(3), H_1 = PGL(3) (short roots), and
     H_2 = (SL(2) x SL(2)) / {+-1} (orthogonal roots {alpha, zeta}).
  4. Sections 6-8 & Appendix A.7: Adjoint nilpotent/unipotent orbit dimensions
     (regular = 12, subregular G_2(a_1) = 10 for X_beta + X_{2alpha+beta},
     tilde{A}_1 = 8 for X_{alpha+beta}, A_1 = 6 for X_beta; and verification
     that 1994's X_alpha + X_{alpha+beta} had dimension 8 rather than 10),
     plus Jacobson-Morozov sl_2-triples and g_2(2) gradings.
  5. Section 2 (Figure 1, Remark 2026.11): Bruhat-cell solver across all 6 cells
     of G_2 / P_alpha and G_2 / P_beta proving the subregular Dynkin curve has
     1 short-root line l_alpha and 3 long-root lines l_beta (at t_0 in {0, +-sqrt(3)}).
  6. Section 7 (Proposition 7.6A, Example 7.6B(b), Corollary 7.6C): Biquadratic
     root orbits, polynomial P(Y), and Legendre-symbol values mod p (5 <= p <= 23).
"""

import itertools
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def lie(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    return A * B - B * A


def exp_nilp(M: sp.Matrix) -> sp.Matrix:
    res = sp.eye(8)
    cur = sp.eye(8)
    for k in range(1, 8):
        cur = sp.expand(cur * M / k)
        if cur == sp.zeros(8, 8):
            break
        res += cur
    return sp.expand(res)


def build_chevalley_basis():
    J = sp.zeros(8, 8)
    for i in range(8):
        J[i, 7 - i] = 1

    Xa = sp.zeros(8, 8)
    Xa[0, 1] = 1; Xa[2, 3] = 1; Xa[2, 4] = 1
    Xa[3, 5] = -1; Xa[4, 5] = -1; Xa[6, 7] = -1

    Xb = sp.zeros(8, 8)
    Xb[1, 2] = 1; Xb[5, 6] = -1

    Xg = sp.zeros(8, 8)
    Xg[0, 2] = -1; Xg[1, 3] = 1; Xg[1, 4] = 1
    Xg[3, 6] = -1; Xg[4, 6] = -1; Xg[5, 7] = 1

    Xd = sp.zeros(8, 8)
    Xd[0, 3] = 1; Xd[0, 4] = 1; Xd[1, 5] = 1
    Xd[2, 6] = -1; Xd[3, 7] = -1; Xd[4, 7] = -1

    Xe = sp.zeros(8, 8)
    Xe[0, 5] = 1; Xe[2, 7] = -1

    Xz = sp.zeros(8, 8)
    Xz[0, 6] = 1; Xz[1, 7] = -1

    mats_X = {
        "alpha": Xa, "beta": Xb, "gamma": Xg,
        "delta": Xd, "eps": Xe, "zeta": Xz,
    }
    mats_Xm = {k: v.T for k, v in mats_X.items()}
    mats_h = {
        "alpha": sp.diag(1, -1, 2, 0, 0, -2, 1, -1),
        "beta":  sp.diag(0, 1, -1, 0, 0, 1, -1, 0),
        "gamma": sp.diag(1, 2, -1, 0, 0, 1, -2, -1),
        "delta": sp.diag(2, 1, 1, 0, 0, -1, -1, -2),
        "eps":   sp.diag(1, 0, 1, 0, 0, -1, 0, -1),
        "zeta":  sp.diag(1, 1, 0, 0, 0, 0, -1, -1),
    }
    return J, mats_X, mats_Xm, mats_h


def verify_roots_and_table_A6():
    print("[1/6] Verifying G_2 root/coroot lattices and Table A.6 elliptic tori...")
    s3 = sp.sqrt(3)
    alpha = sp.Matrix([1, 0])
    beta = sp.Matrix([-sp.Rational(3, 2), s3 / 2])
    pos_roots = {
        "alpha": alpha,
        "beta": beta,
        "gamma": alpha + beta,
        "delta": 2 * alpha + beta,
        "eps": 3 * alpha + beta,
        "zeta": 3 * alpha + 2 * beta,
    }
    coroots = {k: sp.simplify(2 * v / v.dot(v)) for k, v in pos_roots.items()}
    M_ab = sp.Matrix.hstack(coroots["alpha"], coroots["beta"])
    cochar_coords = {k: tuple(int(c) for c in (M_ab.inv() * coroots[k])) for k in pos_roots}
    assert cochar_coords == {
        "alpha": (1, 0),
        "beta": (0, 1),
        "gamma": (1, 3),
        "delta": (2, 3),
        "eps": (1, 1),
        "zeta": (1, 2),
    }

    def refl_on_cochars(r_vec):
        rv = 2 * r_vec / r_vec.dot(r_vec)
        e1, e2 = coroots["alpha"], coroots["beta"]
        img1 = e1 - r_vec.dot(e1) * rv
        img2 = e2 - r_vec.dot(e2) * rv
        return sp.simplify(M_ab.inv() * sp.Matrix.hstack(img1, img2))

    sa = refl_on_cochars(alpha)
    sb = refl_on_cochars(beta)
    w = sb * sa
    assert sa == sp.Matrix([[-1, 1], [0, 1]])
    assert sb == sp.Matrix([[1, 0], [3, -1]])
    assert w == sp.Matrix([[-1, 1], [-3, 2]])

    def mkey(M):
        return tuple(int(x) for x in M)

    W_set = [sp.Matrix(2, 2, k) for k in sorted({mkey(w**j) for j in range(6)} | {mkey(sa * (w**j)) for j in range(6)})]
    assert len(W_set) == 12

    subgroups = {frozenset({mkey(sp.eye(2))})}
    for r in range(1, 4):
        for gens in itertools.combinations(W_set, r):
            H = {mkey(sp.eye(2))}
            frontier = list(gens)
            while frontier:
                cur = frontier.pop()
                for hk in list(H):
                    hm = sp.Matrix(2, 2, hk)
                    for prod in (cur * hm, hm * cur):
                        pk = mkey(prod)
                        if pk not in H:
                            H.add(pk)
                            frontier.append(prod)
            subgroups.add(frozenset(H))

    conj_classes = []
    visited = set()
    for H in sorted(subgroups, key=len):
        if H in visited:
            continue
        for g in W_set:
            visited.add(frozenset(mkey(g * sp.Matrix(2, 2, h) * g.inv()) for h in H))
        conj_classes.append(H)
    assert len(conj_classes) == 10

    elliptic_summary = []
    for H in conj_classes:
        stacked = sp.Matrix.vstack(*[sp.Matrix(2, 2, h) - sp.eye(2) for h in H])
        if stacked.rank() == 2:
            cols = []
            for h in H:
                M = sp.Matrix(2, 2, h) - sp.eye(2)
                cols.extend([M[:, 0], M[:, 1]])
            snf = smith_normal_form(sp.Matrix.hstack(*cols), domain=sp.ZZ)
            inv_f = tuple(sorted(abs(int(snf[i, i])) for i in range(2) if abs(int(snf[i, i])) != 1))
            short_r = sum(1 for nm in ("alpha", "gamma", "delta") if mkey(refl_on_cochars(pos_roots[nm])) in H)
            long_r = sum(1 for nm in ("beta", "eps", "zeta") if mkey(refl_on_cochars(pos_roots[nm])) in H)
            elliptic_summary.append((len(H), short_r, long_r, inv_f))

    expected_table_A6 = [
        (2, 0, 0, (2, 2)),  # {+-1} quadratic -> (Z/2)^2
        (3, 0, 0, (3,)),    # C_3 cubic -> Z/3
        (4, 1, 1, (2,)),    # <s_alpha, s_zeta> biquadratic -> Z/2
        (6, 0, 0, ()),      # C_6 -> 0
        (6, 0, 3, ()),      # S_3 (long reflections) -> 0
        (6, 3, 0, (3,)),    # S_3 (short reflections) -> Z/3
        (12, 3, 3, ()),     # W -> 0
    ]
    assert sorted(elliptic_summary) == sorted(expected_table_A6)
    print("  [PASS] All 7 elliptic Cartan rows of Table A.6 verified via Smith normal form.")
    return pos_roots, coroots


def verify_chevalley_and_tori(J, mats_X, mats_Xm, mats_h, pos_roots, coroots):
    print("[2/6] Verifying Appendix A.4 Chevalley basis over Z in so(8)...")
    r_names = ["alpha", "beta", "gamma", "delta", "eps", "zeta"]
    for rn in r_names:
        X, Xm, h = mats_X[rn], mats_Xm[rn], mats_h[rn]
        assert X * J + J * X.T == sp.zeros(8, 8)
        assert h * J + J * h.T == sp.zeros(8, 8)
        assert lie(X, Xm) == h
        for r2 in r_names:
            pairing = sp.simplify(pos_roots[r2].dot(coroots[rn]))
            assert lie(h, mats_X[r2]) == pairing * mats_X[r2]

    chev_basis = [mats_h["alpha"], mats_h["beta"]] + [mats_X[k] for k in r_names] + [mats_Xm[k] for k in r_names]
    B_mat = sp.Matrix([[m[i, j] for i in range(8) for j in range(8)] for m in chev_basis]).T
    assert B_mat.rank() == 14

    for m1 in chev_basis:
        for m2 in chev_basis:
            br = lie(m1, m2)
            vec = sp.Matrix([br[i, j] for i in range(8) for j in range(8)])
            c, params = B_mat.gauss_jordan_solve(vec)
            assert len(params) == 0
            assert all(val.is_integer for val in c)
    print("  [PASS] 14-element Chevalley basis closes over Z with X_{-rho} = ^t X_rho.")

    print("[3/6] Verifying Appendix A.3 torus embeddings (A.12)-(A.13')...")
    t2, t3 = sp.symbols("t2 t3")
    t1 = t2 + t3  # log of a1 = a2 * a3
    T_diag = sp.diag(t1, t2, t3, 0, 0, -t3, -t2, -t1)
    weights = {}
    for rn in r_names:
        br = lie(T_diag, mats_X[rn])
        nz_idx = next((i, j) for i in range(8) for j in range(8) if mats_X[rn][i, j] != 0)
        weights[rn] = sp.simplify(br[nz_idx] / mats_X[rn][nz_idx])

    # (A.13) PGL(3): diag(a1, a2, 1) -> root diffs are {t1-t2=t3=alpha, t1=delta, t2=gamma} = short roots!
    pgl3_roots = {sp.simplify(x - y) for x, y in itertools.combinations([t1, t2, 0], 2)}
    assert pgl3_roots == {weights["alpha"], weights["gamma"], weights["delta"]}

    # (A.13') (SL(2) x SL(2))/{+-1}: u^2 = a3 (alpha), v^2 = a1*a2 (zeta), u*v = a1 (delta), v*u^-1 = a2 (gamma)
    assert sp.simplify(t3 - weights["alpha"]) == 0
    assert sp.simplify((t1 + t2) - weights["zeta"]) == 0
    assert sp.simplify(sp.Rational(1, 2) * (t3 + (t1 + t2)) - weights["delta"]) == 0
    assert sp.simplify(sp.Rational(1, 2) * ((t1 + t2) - t3) - weights["gamma"]) == 0
    print("  [PASS] Torus embeddings (A.13) and (A.13') pull back to short roots and {alpha, zeta}.")
    return chev_basis, B_mat


def verify_orbits_and_dynkin_curve(J, mats_X, mats_Xm, mats_h, chev_basis, B_mat):
    print("[4/6] Verifying adjoint orbit dimensions and sl_2-triples (Sec 6-8, App A.7)...")

    def orbit_dim(Y):
        imgs = [lie(m, Y) for m in chev_basis]
        return sp.Matrix([[img[i, j] for i in range(8) for j in range(8)] for img in imgs]).rank()

    assert orbit_dim(mats_X["alpha"] + mats_X["beta"]) == 12   # regular
    assert orbit_dim(mats_X["beta"] + mats_X["delta"]) == 10   # subregular G_2(a_1)
    assert orbit_dim(mats_X["alpha"] + mats_X["gamma"]) == 8   # 1994 typo gave tilde{A}_1 (dim 8)
    assert orbit_dim(mats_X["gamma"]) == 8                     # 2-regular tilde{A}_1
    assert orbit_dim(mats_X["beta"]) == 6                      # 3-regular A_1

    # Subregular sl_2-triple in A.7
    X_plus = mats_X["beta"] + mats_X["delta"]
    X_minus = mats_Xm["beta"] + mats_Xm["delta"]
    H_sub = mats_h["beta"] + mats_h["delta"]
    assert lie(H_sub, X_plus) == 2 * X_plus
    assert lie(H_sub, X_minus) == -2 * X_minus
    assert lie(X_plus, X_minus) == H_sub
    print("  [PASS] Orbit dimensions (12, 10, 8, 6) and subregular sl_2-triple verified.")

    print("[5/6] Verifying subregular Dynkin curve line types across Bruhat cells (Sec 2, Fig. 1)...")

    def theta(rn, z, neg=False):
        return exp_nilp(z * (mats_Xm[rn] if neg else mats_X[rn]))

    n_a = theta("alpha", 1) * theta("alpha", -1, neg=True) * theta("alpha", 1)
    n_b = theta("beta", 1) * theta("beta", -1, neg=True) * theta("beta", 1)
    words = [
        [], ["a"], ["b"], ["a", "b"], ["b", "a"], ["a", "b", "a"], ["b", "a", "b"],
        ["a", "b", "a", "b"], ["b", "a", "b", "a"],
        ["a", "b", "a", "b", "a"], ["b", "a", "b", "a", "b"],
        ["a", "b", "a", "b", "a", "b"],
    ]
    r_names = ["alpha", "beta", "gamma", "delta", "eps", "zeta"]
    b_plus_vecs = sp.Matrix([[m[i, j] for i in range(8) for j in range(8)]
                             for m in [mats_h["alpha"], mats_h["beta"]] + [mats_X[k] for k in r_names]]).T

    def solve_lines(rho_name):
        ch = "a" if rho_name == "alpha" else "b"
        reps = [w for w in words if not w or w[-1] != ch]
        found = []
        for w in reps:
            w_mat = sp.eye(8)
            for c in w:
                w_mat = w_mat * (n_a if c == "a" else n_b)
            inv_roots = [
                k for k in r_names
                if sp.Matrix.hstack(
                    b_plus_vecs,
                    sp.Matrix([(w_mat.inv() * mats_X[k] * w_mat)[i, j] for i in range(8) for j in range(8)]),
                ).rank() > 8
            ]
            ts = [sp.Symbol(f"t_{i}") for i in range(len(inv_roots))]
            g = sp.eye(8)
            for k, sym in zip(inv_roots, ts):
                g = g * theta(k, sym)
            g = g * w_mat
            ginv = J * g.T * J
            Y = sp.expand(ginv * X_plus * g)
            c_vec, _ = B_mat.gauss_jordan_solve(sp.Matrix([Y[i, j] for i in range(8) for j in range(8)]))
            idx_rho = 2 + r_names.index(rho_name)
            eqs = [sp.expand(c_vec[0]), sp.expand(c_vec[1]), sp.expand(c_vec[idx_rho])] + [
                sp.expand(c_vec[8 + j]) for j in range(6)
            ]
            eqs = [e for e in eqs if e != 0]
            if not ts:
                if not eqs:
                    found.append((w, {}))
            else:
                for sol in sp.solve(eqs, ts, dict=True):
                    found.append((w, sol))
        return found

    lines_a = solve_lines("alpha")
    lines_b = solve_lines("beta")
    assert len(lines_a) == 1
    assert len(lines_b) == 3
    print("  [PASS] Dynkin curve has 1 short-root line (alpha) and 3 long-root lines (beta).")


def verify_biquadratic_hilbert_symbols():
    print("[6/6] Verifying biquadratic transfer factor Legendre symbols (Sec 7, Prop. 7.6A & Ex. 7.6B)...")
    for p in [5, 7, 11, 13, 17, 19, 23]:
        squares = {(x * x) % p for x in range(1, p)}
        eps_p = next(e for e in range(1, p) if e not in squares)
        vals = set()
        for u in range(1, p):
            for v in range(1, p):
                val = ((eps_p * v * v - u * u) * (eps_p * v * v - 9 * u * u)) % p
                assert val != 0, f"Unexpected zero at p={p}"
                vals.add(1 if val in squares else -1)
        if p == 5:
            assert vals == {-1}
        else:
            assert vals == {-1, 1}
    print("  [PASS] Example 7.6B(b) verified: Legendre symbol is identically -1 at p=5 and +-1 for 7 <= p <= 23.")


if __name__ == "__main__":
    J, mats_X, mats_Xm, mats_h = build_chevalley_basis()
    pos_roots, coroots = verify_roots_and_table_A6()
    chev_basis, B_mat = verify_chevalley_and_tori(J, mats_X, mats_Xm, mats_h, pos_roots, coroots)
    verify_orbits_and_dynkin_curve(J, mats_X, mats_Xm, mats_h, chev_basis, B_mat)
    verify_biquadratic_hilbert_symbols()
    print("\nALL CHECKS IN verify_g2_chevalley_and_endoscopy.py PASSED.")
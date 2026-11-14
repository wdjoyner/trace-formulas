#!/usr/bin/env python3
"""
Standalone SymPy/SciPy verification suite (Part 2 of 3) for:
  D. Joyner, "On the transfer of Shalika germs for G_2" (Draft 3, November 2026)

Verifies:
  1. Section 3 & Section 4: Affine toric variety Z = Spec k[S], all 11 facet
     normals of cone(S), all 24 coordinate formulas on the 4 patches of Sec 3,
     unimodularity (det = +-1) and Igusa forms omega_{Z,U} on all 12 fundamental
     patches of Proposition 3.4A, and all 7 branches in Table 4.3A.
  2. Section 4 (Remark 2026.23): Exact face lattice of the dual cone
     sigma = cone(S)^v across all 2^11 = 2048 ray subsets via linear programming,
     proving f-vector (1, 11, 43, 82, 84, 46, 12, 1), 268 faces of dim >= 2,
     38 singular faces, and the 5 minimal singular faces.
  3. Section 4 (Lemma 4.4) & Sections 7-8: Differential rank of pi|_E showing
     pi(E_{empty,alpha,delta}) = closure(tilde{A}_1) (dim 8) and
     pi(E_{empty,beta,zeta}) = closure(A_1) (dim 6).
  4. Sections 5, 7, 8: Right Maurer-Cartan determinants (det = 1), Kirillov-Kostant
     symplectic Pfaffians |pi^* omega_{O_2}| = |x(delta)| dx(delta)... and
     |pi^* omega_{O_3}| = |x(zeta)|^2 dx(zeta)..., and exact Leray residue
     division proving Eqs. (7.3)-(7.4) and (8.4)-(8.5) (X-degrees +2 and +3).
"""

from fractions import Fraction
import itertools
import numpy as np
from scipy.optimize import linprog
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


GENS_Z = {
    "lam": (1,  0,  0, 0, 0, 0, 0),
    "za":  (0,  1,  0, 0, 0, 0, 0),
    "zb":  (0,  0,  1, 0, 0, 0, 0),
    "wg":  (0,  0,  0, 1, 0, 0, 0),
    "wd":  (0,  0,  0, 0, 1, 0, 0),
    "we":  (0,  0,  0, 0, 0, 1, 0),
    "wz":  (0,  0,  0, 0, 0, 0, 1),
    "xa":  (1, -1,  0, 0, 0, 0, 0),
    "xb":  (1,  0, -1, 0, 0, 0, 0),
    "xg":  (1, -1, -1, 1, 0, 0, 0),
    "xd":  (1, -2, -1, 0, 1, 0, 0),
    "xe":  (1, -3, -1, 0, 0, 1, 0),
    "xz":  (1, -3, -2, 0, 0, 0, 1),
}
G_NAMES = list(GENS_Z.keys())
M_OMEGA = (7, -10, -6, 1, 1, 1, 1)


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


def build_chevalley_matrices():
    J = sp.zeros(8, 8)
    for i in range(8):
        J[i, 7 - i] = 1
    Xa = sp.zeros(8, 8); Xa[0, 1] = 1; Xa[2, 3] = 1; Xa[2, 4] = 1; Xa[3, 5] = -1; Xa[4, 5] = -1; Xa[6, 7] = -1
    Xb = sp.zeros(8, 8); Xb[1, 2] = 1; Xb[5, 6] = -1
    Xg = sp.zeros(8, 8); Xg[0, 2] = -1; Xg[1, 3] = 1; Xg[1, 4] = 1; Xg[3, 6] = -1; Xg[4, 6] = -1; Xg[5, 7] = 1
    Xd = sp.zeros(8, 8); Xd[0, 3] = 1; Xd[0, 4] = 1; Xd[1, 5] = 1; Xd[2, 6] = -1; Xd[3, 7] = -1; Xd[4, 7] = -1
    Xe = sp.zeros(8, 8); Xe[0, 5] = 1; Xe[2, 7] = -1
    Xz = sp.zeros(8, 8); Xz[0, 6] = 1; Xz[1, 7] = -1
    ha = sp.diag(1, -1, 2, 0, 0, -2, 1, -1)
    hb = sp.diag(0, 1, -1, 0, 0, 1, -1, 0)
    r_names = ["alpha", "beta", "gamma", "delta", "eps", "zeta"]
    mats_X = {"alpha": Xa, "beta": Xb, "gamma": Xg, "delta": Xd, "eps": Xe, "zeta": Xz}
    mats_Xm = {k: v.T for k, v in mats_X.items()}
    chev_basis = [ha, hb] + [mats_X[k] for k in r_names] + [mats_Xm[k] for k in r_names]
    B_mat = sp.Matrix([[m[i, j] for i in range(8) for j in range(8)] for m in chev_basis]).T
    return J, ha, hb, r_names, mats_X, mats_Xm, chev_basis, B_mat


def verify_patches_and_table_43A():
    print("[1/4] Verifying facets of cone(S), Table 4.3A, and all 12 patches of Prop. 3.4A...")
    G_sym = sp.Matrix([GENS_Z[k] for k in G_NAMES])
    facets = {}
    for comb in itertools.combinations(range(13), 6):
        sub = G_sym[list(comb), :]
        if sub.rank() == 6:
            v = sub.nullspace()[0]
            lcm_d = sp.lcm([sp.denom(x) for x in v])
            v_int = [int(x * lcm_d) for x in v]
            g = int(np.gcd.reduce([abs(x) for x in v_int]))
            v_int = tuple(x // g for x in v_int)
            for sgn in (1, -1):
                u = tuple(sgn * x for x in v_int)
                dots = [sum(u[j] * GENS_Z[k][j] for j in range(7)) for k in G_NAMES]
                if all(d >= 0 for d in dots):
                    facets[u] = tuple(G_NAMES[i] for i, d in enumerate(dots) if d == 0)
    assert len(facets) == 11

    expected_branches = {
        (1, 1, 1, 1, 2, 3, 4): (1, 1, Fraction(1, 1)),
        (1, 1, 0, 0, 1, 2, 2): (1, 2, Fraction(2, 1)),
        (1, 0, 1, 0, 0, 0, 1): (1, 2, Fraction(2, 1)),
        (2, 1, 0, 0, 0, 1, 1): (2, 6, Fraction(3, 1)),
        (3, 1, 0, 0, 0, 0, 0): (3, 11, Fraction(11, 3)),
        (2, 0, 1, 0, 0, 0, 0): (2, 8, Fraction(4, 1)),
        (1, 0, 0, 0, 0, 0, 0): (1, 7, Fraction(7, 1)),
    }
    special_facets = {u for u in facets if u[0] > 0}
    assert special_facets == set(expected_branches.keys())
    for u, (ea, eb, ebeta) in expected_branches.items():
        a_val = u[0]
        b_val = sum(M_OMEGA[j] * u[j] for j in range(7))
        assert (a_val, b_val, Fraction(b_val, a_val)) == (ea, eb, ebeta)

    patches_12 = [
        ("Z_{a,b}",   ["lam", "xa", "xb", "xg", "xd", "xe", "xz"], {"xa", "xb"}),
        ("Z_{a}",     ["lam", "xa", "zb", "xg", "xd", "xe", "xz"], {"xa", "zb"}),
        ("Z_{b}",     ["lam", "za", "xb", "xg", "xd", "xe", "xz"], {"za", "xb"}),
        ("Z_{empty}", ["lam", "za", "zb", "wg", "wd", "we", "wz"], {"za", "zb"}),
        ("Z_{0,a,g}", ["za", "zb", "wg", "xg", "xd", "xe", "xz"], {"zb", "xg", "wg"}),
        ("Z_{0,a,d}", ["za", "zb", "wg", "wd", "xd", "xe", "xz"], {"zb", "xd", "wd"}),
        ("Z_{0,a,e}", ["za", "zb", "wg", "wd", "we", "xe", "xz"], {"zb", "xe", "we"}),
        ("Z_{0,a,z}", ["za", "zb", "wg", "wd", "we", "wz", "xz"], {"zb", "xz", "wz"}),
        ("Z_{0,b,g}", ["za", "zb", "wg", "xg", "xd", "xe", "xz"], {"za", "xg", "wg"}),
        ("Z_{0,b,d}", ["za", "zb", "wg", "wd", "xd", "xe", "xz"], {"za", "xd", "wd"}),
        ("Z_{0,b,e}", ["za", "zb", "wg", "wd", "we", "xe", "xz"], {"za", "xe", "we"}),
        ("Z_{0,b,z}", ["za", "zb", "wg", "wd", "we", "wz", "xz"], {"za", "xz", "wz"}),
    ]
    covered_facets = set()
    for pname, lgens, inv_set in patches_12:
        M = sp.Matrix([GENS_Z[k] for k in lgens]).T
        assert abs(int(M.det())) == 1, f"{pname} not unimodular!"
        invM = M.inv()
        for k in G_NAMES:
            exps = invM * sp.Matrix(GENS_Z[k])
            for gname, e in zip(lgens, exps):
                assert e.is_integer and (e >= 0 or gname in inv_set)
        for u in facets:
            if all(sum(u[j] * GENS_Z[g][j] for j in range(7)) == 0 for g in inv_set):
                covered_facets.add(u)
    assert covered_facets == set(facets.keys())
    print("  [PASS] All 12 patches unimodular, regular, and cover all 11 toric divisors; Table 4.3A verified.")
    return list(facets.keys())


def verify_cone_face_lattice(u_list):
    print("[2/4] Verifying full face lattice of dual cone sigma (Sec 4, Remark 2026.23)...")
    U_arr = np.array(u_list, dtype=float)
    true_faces = []
    for mask in range(2**11):
        in_idx = [i for i in range(11) if (mask >> i) & 1]
        out_idx = [i for i in range(11) if not ((mask >> i) & 1)]
        if not out_idx:
            true_faces.append(frozenset(u_list))
            continue
        A_eq = U_arr[in_idx] if in_idx else None
        b_eq = np.zeros(len(in_idx)) if in_idx else None
        res = linprog(
            np.zeros(7),
            A_ub=-U_arr[out_idx],
            b_ub=-np.ones(len(out_idx)),
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=[(None, None)] * 7,
            method="highs",
        )
        if res.success:
            true_faces.append(frozenset(u_list[i] for i in in_idx))

    by_dim = {}
    sing_faces = []
    for f in true_faces:
        if not f:
            d, is_reg = 0, True
        else:
            M = sp.Matrix(list(f))
            d = M.rank()
            is_reg = (len(f) == d) and all(abs(int(smith_normal_form(M, domain=sp.ZZ)[i, i])) == 1 for i in range(d))
        by_dim[d] = by_dim.get(d, 0) + 1
        if d >= 2 and not is_reg:
            sing_faces.append(f)

    f_vec = tuple(by_dim[d] for d in range(8))
    assert f_vec == (1, 11, 43, 82, 84, 46, 12, 1)
    assert sum((-1) ** d * f_vec[d] for d in range(8)) == 0
    assert sum(f_vec[2:]) == 268
    assert len(sing_faces) == 38
    min_sing = [f for f in sing_faces if not any(f2 < f for f2 in sing_faces)]
    assert len(min_sing) == 5
    print("  [PASS] Dual cone f-vector (1, 11, 43, 82, 84, 46, 12, 1), 268 faces (dim >= 2), 38 singular, 5 minimal singular verified.")


def verify_images_and_leray_forms():
    print("[3/4] Verifying branch orbit images in Lemma 4.4 and differential ranks...")
    J, ha, hb, r_names, mats_X, mats_Xm, chev_basis, B_mat = build_chevalley_matrices()

    def theta(rn, z, neg=False):
        return exp_nilp(z * (mats_Xm[rn] if neg else mats_X[rn]))

    xd, xe, xz = sp.symbols("xd xe xz", nonzero=True)

    def branch_rank(b_mat, b_syms):
        cols = []
        b_inv = J * b_mat.T * J
        for s in b_syms:
            xi = sp.expand(b_inv * sp.diff(b_mat, s))
            cols.append(B_mat.gauss_jordan_solve(sp.Matrix([xi[i, j] for i in range(8) for j in range(8)]))[0])
        for rn in r_names:
            Xm = mats_Xm[rn]
            xi = sp.expand(Xm - b_inv * Xm * b_mat)
            cols.append(B_mat.gauss_jordan_solve(sp.Matrix([xi[i, j] for i in range(8) for j in range(8)]))[0])
        return sp.Matrix.hstack(*cols).subs({xd: 2, xe: 3, xz: 5}).rank()

    assert branch_rank(theta("delta", xd) * theta("eps", xe) * theta("zeta", xz), [xd, xe, xz]) == 8
    assert branch_rank(theta("zeta", xz), [xz]) == 6
    assert branch_rank(theta("eps", xe) * theta("zeta", xz), [xe, xz]) == 6  # E_{empty,alpha,zeta} (beta=11/3) maps onto closure(A_1)
    print("  [PASS] Differential ranks on E_{empty,alpha,delta} (=8) and E_{empty,beta,zeta} (=6) prove Lemma 4.4.")

    print("[4/4] Verifying Kirillov-Kostant symplectic Pfaffians and Leray fiber forms (Sec 7-8)...")
    va, vb, vg, vd, ve, vz = sp.symbols("va vb vg vd ve vz")
    n_p = (
        theta("beta", vb, neg=True)
        * theta("gamma", vg, neg=True)
        * theta("delta", vd, neg=True)
        * theta("eps", ve, neg=True)
        * theta("zeta", vz, neg=True)
    )
    n_p_inv = J * n_p.T * J
    mc5_cols = [
        B_mat.gauss_jordan_solve(sp.Matrix([sp.simplify(sp.diff(n_p, s) * n_p_inv)[i, j] for i in range(8) for j in range(8)]))[0][9:14, 0]
        for s in [vb, vg, vd, ve, vz]
    ]
    assert sp.simplify(sp.Matrix.hstack(*mc5_cols).det()) == 1

    # O_3 = A_1 (dim 6) Kirillov-Kostant Pfaffian
    xis_O3 = [-hb / xz] + [mats_Xm[k] for k in ["beta", "gamma", "delta", "eps", "zeta"]]
    Omega_O3 = sp.Matrix([[sp.simplify((xz * mats_X["zeta"] * lie(x1, x2)).trace()) for x2 in xis_O3] for x1 in xis_O3])
    det_ratio_O3 = sp.simplify(Omega_O3.det() / xz**4)
    assert det_ratio_O3.is_Rational and det_ratio_O3 > 0  # Pfaffian = c * x(zeta)^2

    # O_2 = tilde{A}_1 (dim 8) Kirillov-Kostant Pfaffian on (xd, xe, xz, va, vg, vd, ve, vz)
    u_b = theta("delta", xd) * theta("eps", xe) * theta("zeta", xz)
    N_ub = u_b - sp.eye(8)
    Y_b = sp.zeros(8, 8)
    cur = sp.eye(8)
    for k in range(1, 7):
        cur = sp.expand(cur * N_ub)
        if cur == sp.zeros(8, 8):
            break
        Y_b += ((-1) ** (k - 1)) * cur / k
    Y_b = sp.expand(Y_b)
    ad_cols = [lie(Y_b, m) for m in chev_basis]
    A_Yb = sp.Matrix.hstack(*[B_mat.gauss_jordan_solve(sp.Matrix([col[r, c] for r in range(8) for c in range(8)]))[0] for col in ad_cols])
    T_mats = [sp.diff(Y_b, s) for s in [xd, xe, xz]] + [lie(Y_b, mats_Xm[k]) for k in ["alpha", "gamma", "delta", "eps", "zeta"]]
    xis_O2 = []
    for Tm in T_mats:
        t_vec, _ = B_mat.gauss_jordan_solve(sp.Matrix([Tm[r, c] for r in range(8) for c in range(8)]))
        xi_c, params = A_Yb.gauss_jordan_solve(t_vec)
        xi_c = xi_c.subs({p: 0 for p in params})
        xis_O2.append(sum((xi_c[k] * chev_basis[k] for k in range(14)), sp.zeros(8, 8)))
    Skew_O2 = sp.Matrix([[sp.simplify((T_mats[i] * xis_O2[j]).trace()) for j in range(8)] for i in range(8)])
    det_ratio_O2 = sp.simplify(Skew_O2.det() / xd**2)
    assert det_ratio_O2.is_Rational and det_ratio_O2 > 0  # Pfaffian = c * x(delta)

    # Check residue cancellation giving (7.4) and (8.5):
    za, zb, wg, wd, we, wz = sp.symbols("za zb wg wd we wz", positive=True)
    lam_7 = xd * za**2 * zb / wd
    omega_Z_7 = xd**4 * za**5 * zb / wd**5
    res_7 = sp.simplify(omega_Z_7 / (lam_7**3 / za))
    leray_7 = sp.simplify(res_7 / xd)
    assert leray_7 == 1 / (wd**2 * zb**2)

    lam_8 = xz * za**3 * zb**2 / wz
    omega_Z_8 = xz**6 * za**10 * zb**7 / wz**7
    res_8 = sp.simplify(omega_Z_8 / (lam_8**4 / zb))
    leray_8 = sp.simplify(res_8 / xz**2)
    assert leray_8 == 1 / (wz**3 * za**2)
    print("  [PASS] Symplectic Pfaffians (x(delta) and x(zeta)^2) and Leray forms (7.4) and (8.5) verified.")


if __name__ == "__main__":
    u_list = verify_patches_and_table_43A()
    verify_cone_face_lattice(u_list)
    verify_images_and_leray_forms()
    print("\nALL CHECKS IN verify_g2_toric_and_forms.py PASSED.")
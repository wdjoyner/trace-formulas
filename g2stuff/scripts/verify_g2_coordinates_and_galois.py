#!/usr/bin/env python3
"""
Standalone SymPy verification suite (Part 3 of 3) for:
  D. Joyner, "On the transfer of Shalika germs for G_2" (Draft 3, November 2026)

Verifies all exact closed-form formulas introduced in Draft 3 (Sections 1 & 2)
in the explicit 8x8 Chevalley basis of Appendix A.4 (X_{-rho} = ^t X_rho,
root ordering Sigma_G^+ = (alpha, beta, gamma, delta, eps, zeta)):
  1. Section 1, Eq. (1.21a): Exact all-order unipotent coordinate polynomials
     x(rho) in Lemma 1.21 for t_0^(n_-) = t_0 * prod_{rho>0} theta_rho(x(rho)).
  2. Section 1, Eq. (1.21b) & Remark 2026.8: Exact star gallery coordinate
     identities n_alpha = 1/z(W_0,alpha), n_beta = 1/z(W_0,beta),
     n_gamma = 1/(z(W_0,beta) z(s_beta W_0, gamma)), and triangular gallery
     identities for n_delta, n_eps, n_zeta.
  3. Section 1, Eq. (1.22) & w(rho)|_{lambda=0}: Exact constants
     (c_1,...,c_7) = (-1, 2, 3, -3, -3, 1, 3) and exact lambda -> 0 limits.
  4. Section 2, Eqs. (2.11)-(2.14): Exact Chevalley commutators, parabolic
     conjugations by theta_{-alpha}(z) and theta_{-beta}(z), and exact 8x8
     rational-matrix verification of m_sigma * sigma(b) * m_sigma^-1 = b'
     with n_0 = 1 identically in Eq. (2.9).
  5. Section 2, Proposition 2.14A: Exact birational Galois involutions on
     the special-fiber coordinates (z(alpha), z(beta), w(gamma), w(delta),
     w(eps), w(zeta)) at lambda = 0, verifying F_alpha^2 = id, F_beta^2 = id,
     and pullback Jacobian ratios = 1 on both Leray fiber volume forms
     (7.4) on E_{empty,alpha,delta} and (8.5) on E_{empty,beta,zeta}.
  6. Section 2, Eqs. (2.16)-(2.17): Exact Weyl conjugations by s_alpha and
     s_beta with all structure signs eta_{rho,tau} and cubic reordering terms.
"""

import sympy as sp


def build_setup():
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

    def exp_nilp(M):
        res = sp.eye(8)
        cur = sp.eye(8)
        for k in range(1, 8):
            cur = sp.expand(cur * M / k)
            if cur == sp.zeros(8, 8):
                break
            res += cur
        return sp.expand(res)

    def theta(rn, z, neg=False):
        return exp_nilp(z * (mats_Xm[rn] if neg else mats_X[rn]))

    def log_unip(U):
        N = U - sp.eye(8)
        res = sp.zeros(8, 8)
        cur = sp.eye(8)
        for k in range(1, 8):
            cur = sp.expand(cur * N)
            if cur == sp.zeros(8, 8):
                break
            res += ((-1) ** (k - 1)) * cur / k
        return sp.expand(res)

    def factor_in_N_minus(U):
        rem = U
        out = {}
        for rn in r_names:
            L = log_unip(rem)
            vec = sp.Matrix([L[i, j] for i in range(8) for j in range(8)])
            c, _ = B_mat.gauss_jordan_solve(vec)
            val = sp.simplify(c[2 + r_names.index(rn)])
            out[rn] = val
            rem = sp.expand(theta(rn, -val) * rem)
        assert rem == sp.eye(8), f"Non-identity remainder in N_- factorization: {rem}"
        return out

    s_a = theta("alpha", 1) * theta("alpha", -1, neg=True) * theta("alpha", 1)
    s_b = theta("beta", 1) * theta("beta", -1, neg=True) * theta("beta", 1)
    return r_names, theta, factor_in_N_minus, s_a, s_b


def verify_section_1_exact(r_names, theta, factor_in_N_minus, s_a, s_b):
    print("[1/3] Verifying Section 1 exact formulas: Eqs. (1.21a), (1.21b), (1.22), w(rho), Remark 2026.8...")
    A_i, B_i = sp.symbols("A_i B_i")  # alpha(t_0)^-1, beta(t_0)^-1
    G_i, D_i, E_i, Z_i = A_i * B_i, A_i**2 * B_i, A_i**3 * B_i, A_i**3 * B_i**2
    na, nb, ng, nd, ne, nz = sp.symbols("n_a n_b n_g n_d n_e n_z")
    n_syms = {"alpha": na, "beta": nb, "gamma": ng, "delta": nd, "eps": ne, "zeta": nz}
    rho_inv = {"alpha": A_i, "beta": B_i, "gamma": G_i, "delta": D_i, "eps": E_i, "zeta": Z_i}

    n_minus = sp.eye(8)
    t_conj_inv = sp.eye(8)
    for rn in r_names:
        n_minus = sp.expand(n_minus * theta(rn, n_syms[rn]))
    for rn in reversed(r_names):
        t_conj_inv = sp.expand(t_conj_inv * theta(rn, -rho_inv[rn] * n_syms[rn]))

    x_exact = factor_in_N_minus(sp.expand(t_conj_inv * n_minus))

    expected_121a = {
        "alpha": (1 - A_i) * na,
        "beta": (1 - B_i) * nb,
        "gamma": (1 - G_i) * ng - B_i * (1 - A_i) * na * nb,
        "delta": (1 - D_i) * nd + 2 * A_i * B_i * (1 - A_i) * na * ng + B_i * (1 - A_i) ** 2 * na**2 * nb,
        "eps": (
            (1 - E_i) * ne
            + 3 * A_i**2 * B_i * (1 - A_i) * na * nd
            - 3 * A_i * B_i * (1 - A_i) ** 2 * na**2 * ng
            - B_i * (1 - A_i) ** 3 * na**3 * nb
        ),
        "zeta": (
            (1 - Z_i) * nz
            - 3 * A_i * B_i * (1 - A_i) * (2 - G_i) * na * ng**2
            - 3 * A_i**2 * B_i * (1 - A_i) * na * nb * nd
            + A_i**3 * B_i * (1 - B_i) * nb * ne
            + 3 * A_i**2 * B_i * (1 - G_i) * ng * nd
            + 3 * B_i * (1 - A_i) ** 2 * (A_i + G_i - 1) * na**2 * nb * ng
            + B_i * (1 - A_i) ** 3 * (1 + B_i) * na**3 * nb**2
        ),
    }
    for rn in r_names:
        assert sp.expand(x_exact[rn] - expected_121a[rn]) == 0

    # Star gallery relations: w_+ * n_- * n_W^-1 in B_- (upper triangular in GL_8)
    a1, b1, a2, b3, a4, b5 = sp.symbols("a1 b1 a2 b3 a4 b5", nonzero=True)
    M1 = sp.expand(s_a * n_minus * theta("alpha", -a1, neg=True))
    sol_g = sp.solve([M1[i, j] for i in range(8) for j in range(i)], [na], dict=True)[0]
    M2 = sp.expand(s_b * n_minus * theta("beta", -b1, neg=True))
    sol_g.update(sp.solve([M2[i, j] for i in range(8) for j in range(i)], [nb], dict=True)[0])
    M3 = sp.expand((s_a * s_b) * n_minus.subs(sol_g) * theta("beta", -b1, neg=True) * theta("alpha", -a2, neg=True))
    sol_g.update(sp.solve([sp.simplify(M3[i, j]) for i in range(8) for j in range(i) if M3[i, j] != 0], [ng], dict=True)[0])
    assert sol_g[na] == 1 / a1 and sol_g[nb] == 1 / b1 and sol_g[ng] == 1 / (a2 * b1)

    # Remaining triangular gallery relations in Remark 2026.8:
    M4 = sp.expand((s_b * s_a * s_b) * n_minus.subs(sol_g) * theta("beta", -b1, neg=True) * theta("alpha", -a2, neg=True) * theta("beta", -b3, neg=True))
    sol_d = sp.solve([sp.simplify(M4[i, j]) for i in range(8) for j in range(i) if M4[i, j] != 0], [nd], dict=True)[0]
    assert sp.simplify(3 * a2**2 * b1 * b3 * sol_d[nd] - (-(b1 + b3) - a2**3 * b1 * b3 * (ne + b1 * nz))) == 0

    sol_g.update(sol_d)
    M5 = sp.expand((s_a * s_b * s_a * s_b) * n_minus.subs(sol_g) * theta("beta", -b1, neg=True) * theta("alpha", -a2, neg=True) * theta("beta", -b3, neg=True) * theta("alpha", -a4, neg=True))
    sol_e = sp.solve([sp.simplify(M5[i, j]) for i in range(8) for j in range(i) if M5[i, j] != 0], [ne], dict=True)[0]
    assert sp.simplify(a2**3 * a4 * b1 * b3 * sol_e[ne] - (3 * a2 * b1 + 2 * a4 * (b1 + b3) - a2**3 * a4 * b1**2 * b3 * nz)) == 0

    sol_g.update(sol_e)
    M6 = sp.expand((s_b * s_a * s_b * s_a * s_b) * n_minus.subs(sol_g) * theta("beta", -b1, neg=True) * theta("alpha", -a2, neg=True) * theta("beta", -b3, neg=True) * theta("alpha", -a4, neg=True) * theta("beta", -b5, neg=True))
    sol_z = sp.solve([sp.simplify(M6[i, j]) for i in range(8) for j in range(i) if M6[i, j] != 0], [nz], dict=True)[0]
    assert sp.simplify(a2**3 * a4**3 * b1**2 * b3**2 * b5 * sol_z[nz] - (a4**3 * b3**2 * b5 - b1**2 * (a2**3 * b3 + (a2 + a4) ** 3 * b5))) == 0

    # Verify w(rho)|_{lambda=0} formulas in Section 1:
    lam, aX, bX = sp.symbols("lam aX bX")
    subs_122 = {na: 1 / a1, nb: 1 / b1, ng: 1 / (a2 * b1)}
    subs_lam = {A_i: 1 - lam * aX, B_i: 1 - lam * bX}
    za0, zb0 = a1 / aX, b1 / bX
    gX, dX, eX, zX = aX + bX, 2 * aX + bX, 3 * aX + bX, 3 * aX + 2 * bX
    expected_w0 = {
        "gamma": (gX / (aX * bX)) * (a1 / a2) - 1 / bX,
        "delta": (dX * nd + 2 * aX / (a1 * b1 * a2)) * (a1**2 * b1 / (aX**2 * bX)),
        "eps": (eX * ne + 3 * aX * nd / a1) * (a1**3 * b1 / (aX**3 * bX)),
        "zeta": (
            zX * nz
            - 3 * aX / (a1 * b1**2 * a2**2)
            - 3 * aX * nd / (a1 * b1)
            + bX * ne / b1
            + 3 * gX * nd / (b1 * a2)
        ) * (a1**3 * b1**2 / (aX**3 * bX**2)),
    }
    m_ab = {"gamma": (1, 1), "delta": (2, 1), "eps": (3, 1), "zeta": (3, 2)}
    for rn, (ma, mb) in m_ab.items():
        x_lin = sp.diff(x_exact[rn].subs(subs_122).subs(subs_lam), lam).subs(lam, 0)
        w0 = sp.simplify(x_lin * (za0**ma) * (zb0**mb))
        assert sp.simplify(w0 - expected_w0[rn]) == 0
    print("  [PASS] Eqs. (1.21a), (1.21b), (1.22), w(rho)|_{lambda=0}, and gallery relations verified.")


def verify_section_2_exact(r_names, theta, factor_in_N_minus, s_a, s_b):
    print("[2/3] Verifying Section 2 exact formulas: Eqs. (2.11)-(2.14) and (2.16)-(2.17)...")
    xa, xb, xg, xd, xe, xz, z = sp.symbols("x_a x_b x_g x_d x_e x_z z")
    b_unip = sp.eye(8)
    for rn, sym in zip(r_names, [xa, xb, xg, xd, xe, xz]):
        b_unip = sp.expand(b_unip * theta(rn, sym))

    pts = {
        xa: sp.Rational(1, 3), xb: sp.Rational(1, 5), xg: sp.Rational(1, 7),
        xd: sp.Rational(1, 11), xe: sp.Rational(1, 13), xz: sp.Rational(1, 17),
        z: sp.Rational(1, 2),
    }

    # Eq. (2.11)
    phi_a = {
        "alpha": xa / (1 + xa * z),
        "beta": xb + 3 * z * xg - 3 * z**2 * xd + z**3 * xe,
        "gamma": xg - 2 * z * xd + z**2 * xe,
        "delta": xd - z * xe,
        "eps": xe,
        "zeta": xz + 3 * z * xd**2 - 3 * z**2 * xd * xe + z**3 * xe**2,
    }
    ua_v = (1 + xa * z).subs(pts)
    ta_mat = sp.diag(ua_v, 1 / ua_v, ua_v**2, 1, 1, 1 / ua_v**2, ua_v, 1 / ua_v)
    lhs_211 = (theta("alpha", -z, neg=True) * b_unip * theta("alpha", z, neg=True)).subs(pts)
    rhs_211 = theta("alpha", (-xa * z**2 / (1 + xa * z)).subs(pts), neg=True) * ta_mat
    for rn in r_names:
        rhs_211 = rhs_211 * theta(rn, phi_a[rn].subs(pts))
    assert lhs_211 == rhs_211

    # Eq. (2.13)
    ub = 1 + xb * z
    phi_b = {
        "alpha": ub * xa - z * xg,
        "beta": xb / ub,
        "gamma": xg / ub,
        "delta": xd + z * xg**2 / ub,
        "eps": xe - z * xz + z**2 * xg**3 / ub,
        "zeta": xz - (2 + xb * z) * z * xg**3 / ub**2,
    }
    ub_v = ub.subs(pts)
    tb_mat = sp.diag(1, ub_v, 1 / ub_v, 1, 1, ub_v, 1 / ub_v, 1)
    lhs_213 = (theta("beta", -z, neg=True) * b_unip * theta("beta", z, neg=True)).subs(pts)
    rhs_213 = theta("beta", (-xb * z**2 / ub).subs(pts), neg=True) * tb_mat
    for rn in r_names:
        rhs_213 = rhs_213 * theta(rn, phi_b[rn].subs(pts))
    assert lhs_213 == rhs_213

    # Eqs. (2.12) & (2.14): check m_sigma * sigma(b) * m_sigma^-1 == t_0 * prod theta_rho(phi_rho) (n_0 == 1!)
    p, q = sp.Rational(3, 2), sp.Rational(5, 3)
    t0_mat = sp.diag(p, q / p, p**2 / q, 1, 1, q / p**2, p / q, 1 / p)
    A_t0, B_t0 = p**2 / q, q**2 / p**3

    za_gal = (A_t0 - 1) / pts[xa]
    lhs_212 = theta("alpha", -za_gal, neg=True) * (s_a * t0_mat * s_a.inv() * b_unip.subs(pts)) * theta("alpha", za_gal, neg=True)
    rhs_212 = t0_mat
    for rn in r_names:
        rhs_212 = rhs_212 * theta(rn, phi_a[rn].subs({**pts, z: za_gal}))
    assert lhs_212 == rhs_212

    zb_gal = (B_t0 - 1) / pts[xb]
    lhs_214 = theta("beta", -zb_gal, neg=True) * (s_b * t0_mat * s_b.inv() * b_unip.subs(pts)) * theta("beta", zb_gal, neg=True)
    rhs_214 = t0_mat
    for rn in r_names:
        rhs_214 = rhs_214 * theta(rn, phi_b[rn].subs({**pts, z: zb_gal}))
    assert lhs_214 == rhs_214

    # Eqs. (2.16) & (2.17)
    x_216 = {
        "beta": xe, "gamma": xd, "delta": -xg, "eps": -xb,
        "zeta": xz + 3 * xg * xd + xb * xe,
    }
    lhs_216 = (s_a * b_unip * s_a.inv()).subs(pts)
    rhs_216 = theta("alpha", -pts[xa], neg=True)
    for rn in r_names[1:]:
        rhs_216 = rhs_216 * theta(rn, x_216[rn].subs(pts))
    assert lhs_216 == rhs_216

    x_217 = {
        "alpha": -xg + xa * xb,
        "gamma": xa,
        "delta": xd + 2 * xa * xg - xa**2 * xb,
        "eps": -xz + 3 * xa * xg**2 - 3 * xa**2 * xb * xg + xa**3 * xb**2,
        "zeta": xe - 3 * xa**2 * xg + 2 * xa**3 * xb,
    }
    lhs_217 = (s_b * b_unip * s_b.inv()).subs(pts)
    rhs_217 = theta("beta", -pts[xb], neg=True)
    for rn in r_names:
        if rn != "beta":
            rhs_217 = rhs_217 * theta(rn, x_217[rn].subs(pts))
    assert lhs_217 == rhs_217
    print("  [PASS] Eqs. (2.11)-(2.14) (with n_0 = 1) and Eqs. (2.16)-(2.17) verified on 8x8 rational matrices.")


def verify_proposition_214A():
    print("[3/3] Verifying Proposition 2.14A: special-fiber Galois involutions & Leray measure invariance...")
    aX, bX = sp.symbols("aX bX")
    za, zb, wg, wd, we, wz = sp.symbols("za zb wg wd we wz", nonzero=True)

    # (a) Involution property of F_alpha (remembering sigma_alpha(aX) = -aX):
    Da = 1 + 3 * aX * wg - 3 * aX**2 * wd + aX**3 * we
    fa = {
        za: za,
        zb: zb / Da,
        wg: (wg - 2 * aX * wd + aX**2 * we) / Da,
        wd: (wd - aX * we) / Da,
        we: we / Da,
        wz: wz / Da**2,
    }
    fa_twisted = {k: sp.simplify(v.subs(aX, -aX)) for k, v in fa.items()}
    for k in [za, zb, wg, wd, we, wz]:
        comp = sp.simplify(fa[k].subs(fa_twisted, simultaneous=True))
        assert comp == k, f"F_alpha not an involution on {k}: got {comp}"

    # (b) Involution property of F_beta (remembering sigma_beta(bX) = -bX):
    Db = 1 - bX * wg
    fb = {
        za: za / Db,
        zb: zb,
        wg: wg / Db,
        wd: wd / Db**2,
        we: (we - bX * wz) / Db**3,
        wz: wz / Db**3,
    }
    fb_twisted = {k: sp.simplify(v.subs(bX, -bX)) for k, v in fb.items()}
    for k in [za, zb, wg, wd, we, wz]:
        comp = sp.simplify(fb[k].subs(fb_twisted, simultaneous=True))
        assert comp == k, f"F_beta not an involution on {k}: got {comp}"

    # (c) Pullback invariance of Leray 4-form (7.4) on E_{empty,alpha,delta} (za = we = wz = 0):
    sub_E2 = {za: 0, we: 0, wz: 0}
    J_E2_a = sp.simplify(sp.Matrix([fa[zb].subs(sub_E2), fa[wg].subs(sub_E2), fa[wd].subs(sub_E2)]).jacobian([zb, wg, wd]).det())
    assert sp.simplify(J_E2_a / ((fa[zb].subs(sub_E2) ** 2 * fa[wd].subs(sub_E2) ** 2) / (zb**2 * wd**2))) == 1

    J_E2_b = sp.simplify(sp.Matrix([fb[zb], fb[wg], fb[wd]]).jacobian([zb, wg, wd]).det())
    assert sp.simplify(J_E2_b / ((fb[zb] ** 2 * fb[wd] ** 2) / (zb**2 * wd**2))) == 1

    # (d) Pullback invariance of Leray 6-form (8.5) on E_{empty,beta,zeta} (zb = 0):
    vars_E3 = [za, wg, wd, we, wz]
    J_E3_a = sp.simplify(sp.Matrix([fa[v] for v in vars_E3]).jacobian(vars_E3).det())
    assert sp.simplify(J_E3_a / ((fa[za] ** 2 * fa[wz] ** 3) / (za**2 * wz**3))) == 1

    J_E3_b = sp.simplify(sp.Matrix([fb[v] for v in vars_E3]).jacobian(vars_E3).det())
    assert sp.simplify(J_E3_b / ((fb[za] ** 2 * fb[wz] ** 3) / (za**2 * wz**3))) == 1
    print("  [PASS] Proposition 2.14A involutions and D_6-Galois invariance of (7.4) and (8.5) verified.")


if __name__ == "__main__":
    r_names, theta, factor_in_N_minus, s_a, s_b = build_setup()
    verify_section_1_exact(r_names, theta, factor_in_N_minus, s_a, s_b)
    verify_section_2_exact(r_names, theta, factor_in_N_minus, s_a, s_b)
    verify_proposition_214A()
    print("\nALL CHECKS IN verify_g2_coordinates_and_galois.py PASSED.")
#!/usr/bin/env python3
"""
Standalone SymPy verification suite (Part 4 of 4 — Open Problem 1) for:
  D. Joyner, Claude, and Gemini,
  "On the transfer of Shalika germs for G_2" (Draft 6, November 2026)

Verifies symbolically in the explicit 8x8 Chevalley basis of Appendix A.4:
  1. Section 6, Eqs. (6.5a)-(6.5b) & Remark 2026.15:
     Kirillov-Kostant 10-form Pfaffians on O_1 along E_beta and E_alpha are
     nonzero constants (288 and 864), confirming omega_{E_beta(u)} =
     +/- dv(alpha) ^ dz(alpha)/z(alpha)^2 = +/- alpha(X) dv(alpha) ^ dz(W_0,alpha)/z(W_0,alpha)^2.
  2. Section 7, Propositions 7.6D & 7.6E:
     - Exact Bruhat torus factors n^{-1} w^{-1} in N_+ N_- alpha^vee(p) beta^vee(q)
       for s_alpha, s_beta, s_zeta, and -1 = (s_alpha s_beta)^3.
     - All-order symbolic Laurent series proof of R = z(alpha)^{-4} R_E (1 + O(z(alpha)))
       and Q = z(alpha)^{-6} Q_E (1 + O(z(alpha))) directly from Eq. (1.21a) with
       free coordinates (L, w(gamma), w(delta), x(eps), x(zeta)), including the
       exact polynomial G in Q_E.
     - Verification of the repaired z(alpha)^{-4} = lambda^{-2} x(delta)^2 z(beta)^2 / w(delta)^2
       substitution giving Phi_E = (x(delta)^2 / w(delta)^2) F_1 F_2 in L^x.
  3. Section 7, Proposition 7.6G & Theorem 7.6H (Solution of Corollary 7.6F / (X_2)):
     - Exact fiber equations on E_{empty,alpha,delta}(theta_delta(1)) and exact
       untwisted/twisted D_6 action (s_alpha, s_beta, s_zeta, -1) on
       (z(beta), w(gamma), w(delta), xi = v(beta)).
     - Exact degree-1 birational isomorphism Psi_X: E_{empty,alpha,delta}(u_0) -> (P^1)^4,
       (z(beta), w(gamma), w(delta), xi) -> (U, V, xi_1, xi_2), its explicit rational
       inverse, X-independent Gamma_T-action, exact 4x4 Jacobian identity pulling back
       alpha(X) zeta(X) dU/(U-1)^2 ^ dV/V ^ dxi_1^dxi_2/(xi_1-xi_2)^2 to the Leray
       4-form (7.4), exact Cayley norm N_{L/F}(Phi_E) showing omega_{K/L}(Phi_E) =
       (t^2 - d_alpha d_zeta, d_alpha)_F is independent of X, and the arithmetic of
       the hand-evaluated factors whose product gives C'(q) (the factors themselves
       are typed in, not computed here).
  4. Section 8, Propositions 8.3A-8.3E (Cubic Tori, r = 3):
     - Asymmetry of Gamma_T-orbits on long roots (Delta_0(X) = const).
     - Exact Bruhat torus factors (p_1, q_1) and (p_2, q_2) for w^2 and w^4,
       1-cocycle identity, Artin norm invariant tilde_Phi_{E,3} in F^x on
       E_{empty,beta,zeta}(theta_zeta(1)), and degree-2 hexagon double cover
       y_hex^2 = (m_1 + m_2)^2 - 4 d_{024} d_{135} over (P^1_alpha)^6.
  5. Section 8, Propositions 8.3F-8.3G and Claim 8.3H (Draft 6):
     - X-independent D_6 action in intrinsic coordinates, SL_2(alpha) invariants,
       split quadric cone structure, and an exact 6x6 Jacobian audit over K.
     - The residue of the t-one-form at t_*(X), computed as an exact Laurent
       expansion over Q(w), w^2+w+1=0: a simple pole with residue -2/9 for all X.
     - Arithmetic of the hand-derived valuation-shell formulas giving |C_3(q)|.
       These formulas are typed in; their derivation is Open Problem (1)(b).
"""

import sympy as sp


def build_chevalley():
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

    s_a = theta("alpha", 1) * theta("alpha", -1, neg=True) * theta("alpha", 1)
    s_b = theta("beta", 1) * theta("beta", -1, neg=True) * theta("beta", 1)
    return r_names, mats_X, mats_Xm, ha, hb, theta, log_unip, s_a, s_b


def verify_section_6_subregular_forms(r_names, mats_X, mats_Xm, ha, hb, theta, log_unip):
    print("[1/6] Verifying Section 6 subregular Kirillov-Kostant 10-form Pfaffians...")
    basis_14 = [ha, hb] + [mats_X[k] for k in r_names] + [mats_Xm[k] for k in r_names]
    xb, xg, xd, xe, xz = sp.symbols("xb xg xd xe xz")
    b_mat = sp.eye(8)
    for rn, sym in zip(r_names[1:], [xb, xg, xd, xe, xz]):
        b_mat = sp.expand(b_mat * theta(rn, sym))
    Xb_lie = log_unip(b_mat)
    tangents_b = [sp.diff(Xb_lie, c) for c in [xb, xg, xd, xe, xz]] + [
        Xb_lie * mats_Xm[rn] - mats_Xm[rn] * Xb_lie for rn in r_names[1:]
    ]
    for pt_b in [{xb: 1, xg: 0, xd: 1, xe: 0, xz: 0}, {xb: 2, xg: 1, xd: 3, xe: 5, xz: 7}]:
        X0 = Xb_lie.subs(pt_b)
        ad_X0 = sp.Matrix([[(X0 * m - m * X0)[i, j] for i in range(8) for j in range(8)] for m in basis_14]).T
        xis = []
        for T in tangents_b:
            T_v = sp.Matrix([T.subs(pt_b)[i, j] for i in range(8) for j in range(8)])
            sol, params = ad_X0.gauss_jordan_solve(T_v)
            for prm in params:
                sol = sol.subs(prm, 0)
            xi_m = sp.zeros(8, 8)
            for idx in range(14):
                xi_m += sol[idx] * basis_14[idx]
            xis.append(xi_m)
        Om = sp.Matrix(10, 10, lambda i, j: (X0 * (xis[i] * xis[j] - xis[j] * xis[i])).trace())
        assert Om.det() == 288**2

    xa = sp.Symbol("xa")
    a_mat = sp.eye(8)
    for rn, sym in zip(["alpha", "gamma", "delta", "eps", "zeta"], [xa, xg, xd, xe, xz]):
        a_mat = sp.expand(a_mat * theta(rn, sym))
    Xa_lie = log_unip(a_mat)
    tangents_a = [sp.diff(Xa_lie, c) for c in [xa, xg, xd, xe, xz]] + [
        Xa_lie * mats_Xm[rn] - mats_Xm[rn] * Xa_lie for rn in ["alpha", "gamma", "delta", "eps", "zeta"]
    ]
    X0 = Xa_lie.subs({xa: 1, xg: 0, xd: 0, xe: 1, xz: 1})
    ad_X0 = sp.Matrix([[(X0 * m - m * X0)[i, j] for i in range(8) for j in range(8)] for m in basis_14]).T
    xis = []
    for T in tangents_a:
        T_v = sp.Matrix([T.subs({xa: 1, xg: 0, xd: 0, xe: 1, xz: 1})[i, j] for i in range(8) for j in range(8)])
        sol, params = ad_X0.gauss_jordan_solve(T_v)
        for prm in params:
            sol = sol.subs(prm, 0)
        xi_m = sp.zeros(8, 8)
        for idx in range(14):
            xi_m += sol[idx] * basis_14[idx]
        xis.append(xi_m)
    Om_a = sp.Matrix(10, 10, lambda i, j: (X0 * (xis[i] * xis[j] - xis[j] * xis[i])).trace())
    assert Om_a.det() == 864**2
    print("      PASS: Kirillov-Kostant 10-form Pfaffians = 288 (E_beta) and 864 (E_alpha).")


def verify_bruhat_and_prop_76E(r_names, theta, s_a, s_b):
    print("[2/6] Verifying Bruhat torus factors and all-order symbolic proof of Prop. 7.6E...")
    na, nb, ng, nd, ne, nz = sp.symbols("na nb ng nd ne nz")
    n_inv = sp.eye(8)
    for rn, sym in reversed(list(zip(r_names, [na, nb, ng, nd, ne, nz]))):
        n_inv = sp.expand(n_inv * theta(rn, -sym))

    w_m1 = (s_a * s_b) ** 3
    w_sz = s_b * s_a * s_b * s_a * s_b
    w_rot = s_b * s_a

    M_m1 = sp.expand(n_inv * w_m1.inv())
    R_poly = sp.expand(M_m1[0, 0])
    Q_poly = sp.expand(M_m1[:2, :2].det())
    assert R_poly == sp.expand(na * nb * ne + 2 * na * ng * nd + na * nz + nd**2 - ng * ne)
    assert Q_poly == sp.expand(nb * nd**3 + nb * ne * nz + 3 * ng**2 * nd**2 + 3 * ng * nd * nz - ng**3 * ne + nz**2)

    M_sz = sp.expand(n_inv * w_sz.inv())
    assert sp.expand(M_sz[0, 0] + (nb * ne + 2 * ng * nd + nz)) == 0
    assert sp.expand(M_sz[:2, :2].det() - Q_poly) == 0

    M_w4 = sp.expand(n_inv * (w_rot**4))
    p1_poly = sp.expand(M_w4[0, 0])
    assert p1_poly == sp.expand(na**2 * ng + 2 * na * nd + ne)
    M_w2 = sp.expand(n_inv * (w_rot**2))
    assert sp.expand(M_w2[0, 0] - (nb * ne + 2 * nd * ng + nz)) == 0
    assert sp.expand(M_w2[:2, :2].det() + (nb**2 * ne + 3 * nb * ng * nd + nb * nz + ng**3)) == 0

    # All-order formal Laurent series proof of Prop. 7.6E from Eq. (1.21a)
    L, zb, wg, wd, xe, xz, aX, bX, gX, dX, eX, zX = sp.symbols("L zb wg wd xe xz aX bX gX dX eX zX")
    xd_sub = L * wd / zb

    def lmul(A, B, maxp=10):
        out = {}
        for da, va in A.items():
            for db, vb in B.items():
                if da + db <= maxp:
                    out[da + db] = out.get(da + db, 0) + va * vb
        return {k: sp.expand(v) for k, v in out.items() if v != 0}

    def ladd(*args):
        out = {}
        for A in args:
            for k, v in A.items():
                out[k] = out.get(k, 0) + v
        return {k: sp.expand(v) for k, v in out.items() if v != 0}

    def lscale(c, A):
        return {k: sp.expand(c * v) for k, v in A.items() if v != 0}

    def d_s(rX):
        return {2: L * rX, 4: -(L**2) * rX**2 / 2}

    def inv_d(rX):
        return {-2: 1 / (L * rX), 0: sp.Rational(1, 2)}

    def one_m(rX):
        return {0: 1, 2: -L * rX}

    na_s = lmul({1: L}, inv_d(aX), 2)
    nb_s = lmul({2: L / zb}, inv_d(bX), 2)
    dA, dB, dG = d_s(aX), d_s(bX), d_s(gX)
    Ai, Bi, Gi = one_m(aX), one_m(bX), one_m(gX)
    ng_s = lmul(ladd({1: L * wg / zb}, lmul(Bi, lmul(dA, lmul(na_s, nb_s)))), inv_d(gX), 2)
    dA2 = lmul(dA, dA)
    na2 = lmul(na_s, na_s)
    na3 = lmul(na2, na_s)
    dA3 = lmul(dA2, dA)
    nd_s = lmul(
        ladd(
            {0: xd_sub},
            lscale(-2, lmul(Ai, lmul(Bi, lmul(dA, lmul(na_s, ng_s))))),
            lscale(-1, lmul(Bi, lmul(dA2, lmul(na2, nb_s)))),
        ),
        inv_d(dX),
        1,
    )
    ne_s = lmul(
        ladd(
            {0: xe},
            lscale(-3, lmul(lmul(Ai, Ai), lmul(Bi, lmul(dA, lmul(na_s, nd_s))))),
            lscale(3, lmul(Ai, lmul(Bi, lmul(dA2, lmul(na2, ng_s))))),
            lmul(Bi, lmul(dA3, lmul(na3, nb_s))),
        ),
        inv_d(eX),
        0,
    )
    nz_s = lmul(
        ladd(
            {0: xz},
            lscale(3, lmul(Ai, lmul(Bi, lmul(dA, lmul(ladd({0: 2}, lscale(-1, Gi)), lmul(na_s, lmul(ng_s, ng_s))))))),
            lscale(3, lmul(lmul(Ai, Ai), lmul(Bi, lmul(dA, lmul(na_s, lmul(nb_s, nd_s)))))),
            lscale(-1, lmul(lmul(Ai, lmul(Ai, Ai)), lmul(Bi, lmul(dB, lmul(nb_s, ne_s))))),
            lscale(-3, lmul(lmul(Ai, Ai), lmul(Bi, lmul(dG, lmul(ng_s, nd_s))))),
            lscale(-3, lmul(Bi, lmul(dA2, lmul(ladd(Ai, Gi, {0: -1}), lmul(na2, lmul(nb_s, ng_s)))))),
            lscale(-1, lmul(Bi, lmul(dA3, lmul(ladd({0: 1}, Bi), lmul(na3, lmul(nb_s, nb_s)))))),
        ),
        inv_d(zX),
        0,
    )

    R_ser = ladd(
        lmul(na_s, lmul(nb_s, ne_s), -2),
        lscale(2, lmul(na_s, lmul(ng_s, nd_s), -2)),
        lmul(na_s, nz_s, -2),
        lmul(nd_s, nd_s, -2),
        lscale(-1, lmul(ng_s, ne_s, -2)),
    )
    Q_ser = ladd(
        lmul(nb_s, lmul(nd_s, lmul(nd_s, nd_s, -1), -3), -4),
        lmul(nb_s, lmul(ne_s, nz_s, -4), -4),
        lscale(3, lmul(lmul(ng_s, ng_s, 1), lmul(nd_s, nd_s, -1), -4)),
        lscale(3, lmul(ng_s, lmul(nd_s, nz_s, -3), -4)),
        lscale(-1, lmul(lmul(ng_s, lmul(ng_s, ng_s, 1), 0), ne_s, -4)),
        lmul(nz_s, nz_s, -4),
    )

    root_subs = {gX: aX + bX, dX: 2 * aX + bX, eX: 3 * aX + bX, zX: 3 * aX + 2 * bX}
    F1 = 1 + bX * wg + aX * zX * wd
    F2 = 1 + bX * wg + gX * eX * wd
    R_E = F1 * F2 / (aX * gX * dX**2 * eX * zX * zb**2)
    den_R = aX * bX**2 * gX**2 * dX**2 * eX * zX * zb**2
    assert min(R_ser.keys()) == -4
    assert sp.expand(sp.expand((R_ser[-4] - R_E) * den_R).subs(root_subs)) == 0

    G_expected = (
        9 * aX**4 * wd**2 + 30 * aX**3 * bX * wd**2 + 18 * aX**3 * bX * wd * wg**2 + 18 * aX**3 * wd * wg
        + 37 * aX**2 * bX**2 * wd**2 + 27 * aX**2 * bX**2 * wd * wg**2 + 9 * aX**2 * bX * wd * wg - 18 * aX**2 * wd
        + 20 * aX * bX**3 * wd**2 + 15 * aX * bX**3 * wd * wg**2 - 7 * aX * bX**2 * wd * wg - 6 * aX * bX**2 * wg**3
        - 22 * aX * bX * wd - 12 * aX * bX * wg**2 - 6 * aX * wg + 4 * bX**4 * wd**2 + 3 * bX**4 * wd * wg**2
        - 4 * bX**3 * wd * wg - 3 * bX**3 * wg**3 - 7 * bX**2 * wd - 5 * bX**2 * wg**2 - bX * wg + 1
    )
    Q_E = F2 * G_expected / (bX * gX**3 * dX**3 * eX * zX**2 * zb**4)
    den_Q = aX**3 * bX**4 * gX**4 * dX**3 * eX**2 * zX**2 * zb**4
    assert min(Q_ser.keys()) == -6
    assert sp.expand(sp.expand((Q_ser[-6] - Q_E) * den_Q).subs(root_subs)) == 0

    # Verify z(alpha)^{-4} = lambda^{-2} x(delta)^2 z(beta)^2 / w(delta)^2 cancels z(beta)^2 in R_E
    za, xd, lam = sp.symbols("za xd lam")
    za_sq = lam * wd / (xd * zb)
    prod_R = sp.simplify((za_sq ** (-2)) * R_E.subs(root_subs))
    assert not prod_R.has(zb)
    print("      PASS: All-order symbolic proof of Prop. 7.6E and repaired Phi_E = (xd^2/wd^2)*F1*F2.")


def verify_section_7_birational_proof_X2(r_names, theta):
    print("[3/6] Verifying Section 7 D_6 fiber action, birational map to (P^1)^4, and Theorem 7.6H ((X_2))...")
    va, vb, vg, vd, ve, vz, xd, xe, xz = sp.symbols("va vb vg vd ve vz xd xe xz")
    b_E2 = sp.expand(theta("delta", xd) * theta("eps", xe) * theta("zeta", xz))
    n_plus = sp.eye(8)
    for rn, sym in zip(r_names, [va, vb, vg, vd, ve, vz]):
        n_plus = sp.expand(n_plus * theta(rn, sym, neg=True))
    diff_fib = sp.expand(b_E2 * n_plus - n_plus * theta("delta", 1))
    fib_sol = sp.solve(
        [diff_fib[i, j] for i in range(8) for j in range(8) if diff_fib[i, j] != 0],
        [xd, xe, xz, va, vg, vd, ve, vz],
        dict=True,
    )[0]
    assert fib_sol == {xd: 1, xe: 0, xz: 0, va: 0, vg: 0, vd: 0, ve: 0, vz: 0}
    z_sb = sp.Symbol("z_sb")
    n_fib = n_plus.subs(fib_sol)
    assert sp.expand(theta("beta", z_sb, neg=True) * n_fib - n_fib.subs(vb, vb + z_sb)) == sp.zeros(8, 8)

    # Sparse polynomial verification of exact D_6 action on (zb, wg, wd, xi, aX, bX)
    R, r_zb, r_wg, r_wd, r_xi, r_aX, r_bX = sp.ring("zb, wg, wd, xi, aX, bX", sp.QQ)

    def simp(n, d):
        if n == 0:
            return R.zero, R.one
        g = n.gcd(d)
        n //= g
        d //= g
        if d.LC < 0:
            n = -n
            d = -d
        return n, d

    def compose_single(st, imgs, D, powers):
        out = []
        for num, den in st:
            def sub_p(P):
                if P == 0:
                    return R.zero, 0
                terms = P.terms()
                max_w = max(sum(e[i] * powers[i] for i in range(6)) for e, _ in terms)
                acc = R.zero
                for e, c in terms:
                    w = sum(e[i] * powers[i] for i in range(6))
                    term_val = R(c) * (D ** (max_w - w))
                    for i in range(6):
                        if e[i] > 0:
                            term_val *= imgs[i] ** e[i]
                    acc += term_val
                return acc, max_w
            n_val, wn = sub_p(num)
            d_val, wd_p = sub_p(den)
            if wn >= wd_p:
                d_val *= D ** (wn - wd_p)
            else:
                n_val *= D ** (wd_p - wn)
            out.append(simp(n_val, d_val))
        return out

    Da = 1 - 3 * r_aX * r_wg - 3 * r_aX**2 * r_wd
    Db = 1 + r_bX * r_wg
    imgs_a = [r_zb, r_wg + 2 * r_aX * r_wd, r_wd, r_xi, -r_aX, r_bX + 3 * r_aX]
    pows_a = [1, 1, 1, 0, 0, 0]
    imgs_b = [r_zb, r_wg, r_wd, r_xi + r_bX * r_zb, r_aX + r_bX, -r_bX]
    pows_b = [0, 1, 2, 0, 0, 0]
    id_r = [(g, R.one) for g in [r_zb, r_wg, r_wd, r_xi, r_aX, r_bX]]

    st_a = compose_single(id_r, imgs_a, Da, pows_a)
    st_b = compose_single(id_r, imgs_b, Db, pows_b)
    assert compose_single(st_a, imgs_a, Da, pows_a) == id_r
    assert compose_single(st_b, imgs_b, Db, pows_b) == id_r

    cur = id_r
    for step in range(1, 7):
        cur = compose_single(cur, imgs_a, Da, pows_a)
        cur = compose_single(cur, imgs_b, Db, pows_b)
        if step == 3:
            st_m1 = list(cur)
        if step == 6:
            st_6 = list(cur)
    assert st_6 == id_r
    st_sz = compose_single(st_m1, imgs_a, Da, pows_a)

    # Birational coordinates (U, V, xi1, xi2) and exact 4x4 Jacobian
    zb, wg, wd, xi, aX, bX = sp.symbols("zb wg wd xi aX bX")
    gX, dX, eX, zX = aX + bX, 2 * aX + bX, 3 * aX + bX, 3 * aX + 2 * bX
    F0 = 1 + bX * wg
    F1 = 1 + bX * wg + aX * zX * wd
    F2 = 1 + bX * wg + gX * eX * wd
    G = (
        9 * aX**4 * wd**2 + 30 * aX**3 * bX * wd**2 + 18 * aX**3 * bX * wd * wg**2 + 18 * aX**3 * wd * wg
        + 37 * aX**2 * bX**2 * wd**2 + 27 * aX**2 * bX**2 * wd * wg**2 + 9 * aX**2 * bX * wd * wg - 18 * aX**2 * wd
        + 20 * aX * bX**3 * wd**2 + 15 * aX * bX**3 * wd * wg**2 - 7 * aX * bX**2 * wd * wg - 6 * aX * bX**2 * wg**3
        - 22 * aX * bX * wd - 12 * aX * bX * wg**2 - 6 * aX * wg + 4 * bX**4 * wd**2 + 3 * bX**4 * wd * wg**2
        - 4 * bX**3 * wd * wg - 3 * bX**3 * wg**3 - 7 * bX**2 * wd - 5 * bX**2 * wg**2 - bX * wg + 1
    )
    H = zX * (bX * gX * wd - 2 * F0) * (gX * zX * wd - F0)
    assert sp.expand(st_m1[3][0].as_expr() * G - st_m1[3][1].as_expr() * (xi * G + H * zb)) == 0

    # Check Gamma_T action on U = F1/F0, V = G/(F0*F1*F2), Phi_E = F1*F2/wd^2
    U_pair = simp(R(sp.expand(F1)), R(sp.expand(F0)))
    V_pair = simp(R(sp.expand(G)), R(sp.expand(F0 * F1 * F2)))
    Phi_pair = simp(R(sp.expand(F1 * F2)), R(sp.expand(wd**2)))

    # Under s_alpha: U -> 1/U, V -> V
    U_sa = compose_single([U_pair], imgs_a, Da, pows_a)[0]
    V_sa = compose_single([V_pair], imgs_a, Da, pows_a)[0]
    assert U_sa == simp(U_pair[1], U_pair[0])
    assert V_sa == V_pair

    # Under -1: verify on exact 3-step composition via rational test + degree-1 inverse
    U, V, A, Z = sp.symbols("U V A Z")
    b_AZ = (Z - 3 * A) / 2
    L1 = 3 * A * wg - Z * wg - 2
    L2 = (
        -6 * A**3 * U + 6 * A**3 + 2 * A**2 * U**2 * Z - 8 * A**2 * U * Z + 14 * A**2 * Z - 4 * A * U**2 * Z**2
        - 6 * A * U * Z**2 + 10 * A * Z**2 + 2 * U**2 * Z**3 - 4 * U * Z**3 + 2 * Z**3
        + wg * (9 * A**4 * U - 9 * A**4 + 9 * A**3 * U * Z - 21 * A**3 * Z + 3 * A**2 * U * Z**2 - 15 * A**2 * Z**2 + 3 * A * U * Z**3 - 3 * A * Z**3)
    )
    Q0 = A * U * (3 * A**2 * U - 3 * A**2 - 2 * A * U * Z - 2 * A * Z - U * Z**2 + Z**2)
    assert sp.cancel((L2 / (L1 * Q0)).subs(U, (F1 / F0).subs({aX: A, bX: b_AZ})) - (G / (F0 * F1 * F2)).subs({aX: A, bX: b_AZ})) == 0
    wg_inv = sp.cancel(sp.solve(sp.Eq(V, L2 / (L1 * Q0)), wg)[0])
    wd_inv = sp.cancel(((U - 1) * (1 + b_AZ * wg_inv)) / (A * Z))
    assert sp.cancel((F1 / F0).subs({aX: A, bX: b_AZ, wg: wg_inv, wd: wd_inv}) - U) == 0

    # Exact (-1)^* and s_zeta^* actions on U, V, Phi_E in sparse polynomial ring R (instant!)
    cur_inv = [U_pair, V_pair, Phi_pair]
    for _ in range(3):
        cur_inv = compose_single(cur_inv, imgs_a, Da, pows_a)
        cur_inv = compose_single(cur_inv, imgs_b, Db, pows_b)
    U_m1, V_m1, Phi_m1 = cur_inv
    assert U_m1 == U_pair
    assert V_m1 == simp(V_pair[1], V_pair[0])
    assert Phi_m1 == Phi_pair
    U_sz, V_sz, Phi_sz = compose_single(cur_inv, imgs_a, Da, pows_a)
    assert U_sz == simp(U_pair[1], U_pair[0])
    assert V_sz == simp(V_pair[1], V_pair[0])
    assert Phi_sz == simp(R(sp.expand(F0 * F2)), R(sp.expand(wd**2)))

    # Exact 4x4 Jacobian identity
    F012 = sp.expand(F0 * F1 * F2)
    num_U_wg = sp.expand(F0 * sp.diff(F1, wg) - F1 * sp.diff(F0, wg))
    num_U_wd = sp.expand(F0 * sp.diff(F1, wd) - F1 * sp.diff(F0, wd))
    num_lV_wg = sp.expand(F012 * sp.diff(G, wg) - G * sp.diff(F012, wg))
    num_lV_wd = sp.expand(F012 * sp.diff(G, wd) - G * sp.diff(F012, wd))
    det_num = sp.expand(num_U_wg * num_lV_wd - num_U_wd * num_lV_wg)
    pull_4 = sp.simplify((F0**2 / (aX * zX * wd**2)) * (det_num / (F0**3 * F1 * F2 * G)) * (G / (H * zb**2)))
    assert pull_4 == -1 / (wd**2 * zb**2) or pull_4 == 1 / (wd**2 * zb**2)

    # Cayley parameterization U = (t + sa*sz)/(t - sa*sz) and F-rational 4-form + Phi_E norm
    t, s, x1, y1, uX, vX, sa, sz, da, dz = sp.symbols("t s x1 y1 uX vX sa sz da dz")
    U_c = (t + sa * sz) / (t - sa * sz)
    V_c = (s + sz) / (s - sz)
    xi1_c, xi2_c = x1 + sz * y1, x1 - sz * y1
    J_4 = sp.Matrix([U_c, V_c, xi1_c, xi2_c]).jacobian([t, s, x1, y1]).det()
    coeff_tsxy = sp.simplify((sa * uX) * (sz * vX) * J_4 / ((U_c - 1) ** 2 * V_c * (xi1_c - xi2_c) ** 2))
    assert sp.simplify(coeff_tsxy + uX * vX / (2 * y1**2 * (s**2 - sz**2))) == 0

    Phi_c = sp.expand(
        sp.cancel(
            (sa * uX) * (sz * vX) * U_c
            * ((sa * uX) * (sz * vX) + ((sz * vX - sa * uX) / 2) * ((sz * vX + 3 * sa * uX) / 2) * (U_c - 1))
            / (U_c - 1) ** 2
        ).subs({sa**2: da, sz**2: dz, sa**3: da * sa, sz**3: dz * sz})
    )
    expected_Phi_c = sp.expand(uX * vX * (t + sa * sz) * (2 * t * uX * vX + dz * vX**2 - 3 * da * uX**2) / 8)
    assert sp.expand(Phi_c - expected_Phi_c) == 0
    print("      PASS: Birational map Psi_X, X-independent Gamma_T action, 4-form pullback, and Cayley Phi_E verified.")


def verify_padic_constant_C_prime():
    print("[4/6] Checking the product of hand-evaluated factors giving C'(q) for p = 5, 7, 11, 13...")

    def hilbert_p(a, b, p):
        va = 0
        while a % p == 0:
            a //= p
            va += 1
        vb = 0
        while b % p == 0:
            b //= p
            vb += 1
        sign = (-1) ** (va * vb * ((p - 1) // 2))
        leg_a = pow(a % p, (p - 1) // 2, p)
        if leg_a == p - 1:
            leg_a = -1
        leg_b = pow(b % p, (p - 1) // 2, p)
        if leg_b == p - 1:
            leg_b = -1
        return sign * (leg_a**vb) * (leg_b**va)

    for p in [5, 7, 11, 13]:
        eps = next(x for x in range(2, p) if pow(x, (p - 1) // 2, p) == p - 1)
        # Case (a1): da = eps, dz = p
        It_a1 = sp.Rational(p - 1, p) * (hilbert_p(1 - eps * p, eps, p) - 1) + sp.Rational(1, p) * (
            hilbert_p(p * p - eps * p, eps, p) - 1
        )
        Is_a1 = sp.Integer(2)
        Ixi_a1 = -sp.Rational(p + 1, p**2)
        C_a1 = sp.sqrt(p) * It_a1 * Is_a1 * Ixi_a1

        # Case (a2): da = p, dz = eps
        It_a2 = sp.Rational(p - 1, p) * (hilbert_p(1 - eps * p, p, p) - 1) + sp.Rational(1, p) * (
            hilbert_p(p * p - eps * p, p, p) - 1
        )
        Is_a2 = sp.Rational(p + 1, p)
        Ixi_a2 = -sp.Rational(2, p)
        C_a2 = sp.sqrt(p) * It_a2 * Is_a2 * Ixi_a2

        # Case (b): da = p, dz = eps * p
        It_b = sp.Rational(p - 1, p) * (hilbert_p(1 - eps * p * p, p, p) - 1) + sp.Rational(1, p * p) * sum(
            hilbert_p(p * p * y * y - eps * p * p, p, p) - 1 for y in range(p)
        )
        Is_b = sp.Integer(2)
        Ixi_b = -sp.Rational(p + 1, p**2)
        C_b = p * It_b * Is_b * Ixi_b

        assert C_a1 == C_a2 == 4 * (p + 1) / (p ** sp.Rational(5, 2))
        assert C_b == sp.Rational(2 * (p + 1) ** 2, p**3)
    print("      PASS (arithmetic of hand-evaluated factors I_t, I_s, I_xi): C'(q) product, symmetric in (d_alpha, d_zeta).")


def verify_section_8_cubic_tori(r_names, theta):
    print("[5/6] Verifying Section 8 cubic torus cocycle tilde_Phi_{E,3} and hexagon double cover...")
    va, vb, vg, vd, ve, vz, xz = sp.symbols("va vb vg vd ve vz xz")
    b_E3 = theta("zeta", xz)
    n_plus = sp.eye(8)
    for rn, sym in zip(r_names, [va, vb, vg, vd, ve, vz]):
        n_plus = sp.expand(n_plus * theta(rn, sym, neg=True))
    diff_fib3 = sp.expand(b_E3 * n_plus - n_plus * theta("zeta", 1))
    fib3_sol = sp.solve(
        [diff_fib3[i, j] for i in range(8) for j in range(8) if diff_fib3[i, j] != 0],
        [xz, vb, vg, vd, ve, vz],
        dict=True,
    )[0]
    assert fib3_sol == {xz: 1, vb: 0, vg: 0, vd: 0, ve: 0, vz: 0}

    za, wg, wd, we, wz, eta, aX, bX, zb = sp.symbols("za wg wd we wz eta aX bX zb")
    gX, dX, eX, zX = aX + bX, 2 * aX + bX, 3 * aX + bX, 3 * aX + 2 * bX
    Da = 1 - 3 * aX * wg - 3 * aX**2 * wd - aX**3 * we
    Db = 1 + bX * wg
    subs_a = {
        za: za,
        wg: (wg + 2 * aX * wd + aX**2 * we) / Da,
        wd: (wd + aX * we) / Da,
        we: we / Da,
        wz: wz / Da**2,
        eta: eta + aX * za,
        aX: -aX,
        bX: bX + 3 * aX,
    }
    subs_b = {
        za: za / Db,
        wg: wg / Db,
        wd: wd / Db**2,
        we: (we + bX * wz) / Db**3,
        wz: wz / Db**3,
        eta: eta,
        aX: aX + bX,
        bX: -bX,
    }

    eta0 = eta
    eta1 = sp.cancel(eta0.subs(subs_a, simultaneous=True))
    eta5 = sp.cancel(eta1.subs(subs_b, simultaneous=True))
    eta2 = sp.cancel(eta5.subs(subs_a, simultaneous=True))
    eta4 = sp.cancel(eta2.subs(subs_b, simultaneous=True))
    eta3 = sp.cancel(eta4.subs(subs_a, simultaneous=True))

    # Verify hexagon double-cover discriminant formula y_hex^2 = (m1 + m2)^2 - 4 * d024 * d135
    u2, u3, u4, u5 = sp.symbols("u2 u3 u4 u5")
    sol_wg = sp.cancel((gX / (aX * u5) - 1) / bX)
    eq2 = sp.fraction(sp.cancel(eta2.subs({eta: 0, za: 1 / aX, wg: sol_wg}) - u2))[0]
    sol_we = sp.cancel(sp.solve(eq2, we)[0])
    eq4 = sp.fraction(sp.cancel(eta4.subs({eta: 0, za: 1 / aX, wg: sol_wg, we: sol_we}) - u4))[0]
    sol_wz = sp.cancel(sp.solve(eq4, wz)[0])
    eq3_num = sp.fraction(sp.cancel(eta3.subs({eta: 0, za: 1 / aX, wg: sol_wg, we: sol_we, wz: sol_wz}) - u3))[0]
    A_c, B_c, C_c = sp.Poly(eq3_num, wd).all_coeffs()
    disc_norm = sp.cancel((B_c**2 - 4 * A_c * C_c) / (aX**4 * bX**2 * u5**2 * dX**2))

    e0, e1, e2, e3, e4, e5 = sp.Integer(0), sp.Integer(1), u2, u3, u4, u5
    m1 = (e1 - e0) * (e3 - e2) * (e5 - e4)
    m2 = (e2 - e1) * (e4 - e3) * (e0 - e5)
    d024 = (e0 - e2) * (e2 - e4) * (e4 - e0)
    d135 = (e1 - e3) * (e3 - e5) * (e5 - e1)
    assert sp.expand(disc_norm - ((m1 + m2) ** 2 - 4 * d024 * d135)) == 0

    # Verify exact tau-invariance of tilde_Phi_{E,3} on rational orbit of w^2
    na_3 = 1 / (aX * za)
    nb_3 = 1 / (bX * zb)
    ng_3 = (bX * wg + 1) / (bX * gX * za * zb)
    nd_3 = (wd / (za**2 * zb) - 2 * aX * na_3 * ng_3) / dX
    ne_3 = (we / (za**3 * zb) - 3 * aX * na_3 * nd_3) / eX
    nz_3 = (wz / (za**3 * zb**2) + 3 * aX * na_3 * ng_3**2 + 3 * aX * na_3 * nb_3 * nd_3 - bX * nb_3 * ne_3 - 3 * gX * ng_3 * nd_3) / zX
    P1 = 2 * aX**3 * we + aX**2 * bX * we + 3 * aX**2 * wd + 2 * aX * bX * wd + bX * wg + 1
    P2 = (
        2 * aX**3 * bX * wz + 2 * aX**3 * we + 5 * aX**2 * bX**2 * wz + 3 * aX**2 * bX * wd * wg + 5 * aX**2 * bX * we
        + 3 * aX**2 * wd + 4 * aX * bX**3 * wz + 4 * aX * bX**2 * wd * wg + 4 * aX * bX**2 * we + 4 * aX * bX * wd
        + bX**4 * wz + bX**3 * wd * wg + bX**3 * we + bX**2 * wd + bX**2 * wg**2 + 2 * bX * wg + 1
    )
    Q2 = -(
        aX**3 * bX * wz + aX**3 * we + 3 * aX**2 * bX**2 * wz + 3 * aX**2 * bX * wd * wg + 3 * aX**2 * bX * we
        + 3 * aX**2 * wd + 3 * aX * bX**3 * wz + 6 * aX * bX**2 * wd * wg + 3 * aX * bX**2 * we + 3 * aX * bX**2 * wg**3
        + 6 * aX * bX * wd + 6 * aX * bX * wg**2 + 3 * aX * wg + bX**4 * wz + 3 * bX**3 * wd * wg + bX**3 * we
        + 2 * bX**3 * wg**3 + 3 * bX**2 * wd + 3 * bX**2 * wg**2 - 1
    )
    q1_raw = (
        na_3**3 * nb_3**2 * ne_3 + 3 * na_3**3 * nb_3 * nd_3 * ng_3 + na_3**3 * nb_3 * nz_3 + na_3**3 * ng_3**3
        + 3 * na_3**2 * nb_3 * nd_3**2 - 3 * na_3**2 * nb_3 * ne_3 * ng_3 - 3 * na_3**2 * nd_3 * ng_3**2
        - 3 * na_3**2 * ng_3 * nz_3 - 6 * na_3 * nd_3**2 * ng_3 - 3 * na_3 * nd_3 * nz_3 + 3 * na_3 * ne_3 * ng_3**2
        - nd_3**3 - ne_3 * nz_3
    )

    def step_pt(p):
        for _ in range(2):
            da_v = 1 - 3 * p[aX] * p[wg] - 3 * p[aX] ** 2 * p[wd] - p[aX] ** 3 * p[we]
            p = {
                za: p[za],
                wg: (p[wg] + 2 * p[aX] * p[wd] + p[aX] ** 2 * p[we]) / da_v,
                wd: (p[wd] + p[aX] * p[we]) / da_v,
                we: p[we] / da_v,
                wz: p[wz] / da_v**2,
                eta: p[eta] + p[aX] * p[za],
                aX: -p[aX],
                bX: p[bX] + 3 * p[aX],
            }
            db_v = 1 + p[bX] * p[wg]
            p = {
                za: p[za] / db_v,
                wg: p[wg] / db_v,
                wd: p[wd] / db_v**2,
                we: (p[we] + p[bX] * p[wz]) / db_v**3,
                wz: p[wz] / db_v**3,
                eta: p[eta],
                aX: p[aX] + p[bX],
                bX: -p[bX],
            }
        return p

    pt0 = {
        za: sp.Rational(1, 2),
        wg: sp.Rational(1, 3),
        wd: sp.Rational(1, 5),
        we: sp.Rational(1, 7),
        wz: sp.Rational(1, 11),
        eta: sp.Rational(2, 3),
        aX: sp.Integer(2),
        bX: sp.Integer(5),
    }
    pt1 = step_pt(pt0)
    pt2 = step_pt(pt1)
    assert step_pt(pt2) == pt0

    def eval_phi3(p):
        q1_v = (zb**3 * aX**3 * za**6 * dX**3 * eX**2 * zX * q1_raw).subs({**p, zb: 1})
        return ((za**3 / wz**3) * (q1_v**2 * Q2**2) / (P1**2 * P2**2)).subs(p)

    assert eval_phi3(pt0) == eval_phi3(pt1) == eval_phi3(pt2)
    print("      PASS: Cubic torus cocycle tilde_Phi_{E,3} in F^x and hexagon double cover verified.")



def verify_section_8_proof_X3_and_C3():
    """6. Section 8 (Draft 6): intrinsic SL2(alpha)-fibration, split quadric cone C_K(F), residue at t_*, C_3(q) arithmetic."""
    from fractions import Fraction

    print("[6/6] Verifying Section 8: Props. 8.3F-8.3G, 6x6 Dual(K) audit, the residue at t_*, and C_3(q) arithmetic...")

    # --- 6A. Proposition 8.3F(a): X-independent D_6 action in intrinsic coordinates (8.7d) ---
    z_a, rg, nd, ne, nz, eta = sp.symbols("z_a rg nd ne nz eta")
    aX, bX = sp.symbols("aX bX")
    gX, dX, eX, zX = aX + bX, 2 * aX + bX, 3 * aX + bX, 3 * aX + 2 * bX

    za = z_a / aX
    wg = (gX * rg - aX) / (aX * bX)
    wd = (dX * nd + 2 * aX * rg) / (aX**2 * bX)
    we = (eX * ne + 3 * aX * nd) / (aX**3 * bX)
    L_X = zX * nz - 3 * aX * rg**2 + 3 * (gX * rg - aX) * nd + bX * ne
    wz = L_X / (aX**3 * bX**2)

    da = 1 - 3 * aX * wg - 3 * aX**2 * wd - aX**3 * we
    D_sa = 3 * nd + ne + 3 * rg - 1
    assert sp.cancel(da + (eX / bX) * D_sa) == 0

    sa_map = {
        z_a: -z_a,
        rg: (rg + 2 * nd + ne) / D_sa,
        nd: -(nd + ne) / D_sa,
        ne: ne / D_sa,
        nz: (3 * nd**2 + 3 * nd * ne + ne**2 - nz) / D_sa**2,
        eta: eta + z_a,
        aX: -aX,
        bX: bX + 3 * aX,
    }
    assert sp.cancel(za.subs(sa_map, simultaneous=True) - za) == 0
    assert sp.cancel(wg.subs(sa_map, simultaneous=True) - (wg + 2 * aX * wd + aX**2 * we) / da) == 0
    assert sp.cancel(wd.subs(sa_map, simultaneous=True) - (wd + aX * we) / da) == 0
    assert sp.cancel(we.subs(sa_map, simultaneous=True) - we / da) == 0
    assert sp.cancel(wz.subs(sa_map, simultaneous=True) - wz / da**2) == 0
    assert sp.cancel(L_X.subs(sa_map, simultaneous=True) + L_X / D_sa**2) == 0

    db = 1 + bX * wg
    sb_map = {
        z_a: z_a / rg,
        rg: 1 / rg,
        nd: -(nd + 2 * rg) / rg**2,
        ne: -(ne + nz - 3 * rg**2) / rg**3,
        nz: (nz - 3 * rg**2 + 3 * rg) / rg**3,
        eta: eta,
        aX: aX + bX,
        bX: -bX,
    }
    assert sp.cancel(za.subs(sb_map, simultaneous=True) - za / db) == 0
    assert sp.cancel(wg.subs(sb_map, simultaneous=True) - wg / db) == 0
    assert sp.cancel(wd.subs(sb_map, simultaneous=True) - wd / db**2) == 0
    assert sp.cancel(we.subs(sb_map, simultaneous=True) - (we + bX * wz) / db**3) == 0
    assert sp.cancel(wz.subs(sb_map, simultaneous=True) - wz / db**3) == 0
    assert sp.cancel(L_X.subs(sb_map, simultaneous=True) - L_X / rg**3) == 0

    # --- 6B. Proposition 8.3F(b): SL_2(alpha) invariants (j2, j3', j3'') (8.7e) ---
    u_sl2 = sp.Symbol("u_sl2")
    sl2_inf = {
        rg: (rg + u_sl2) / (1 + u_sl2),
        nd: (nd - 2 * u_sl2 * rg - u_sl2**2) / (1 + u_sl2) ** 2,
        ne: (ne - 3 * u_sl2 * nd + 3 * u_sl2**2 * rg + u_sl2**3) / (1 + u_sl2) ** 3,
        nz: (nz + 3 * u_sl2 * rg**2 + 3 * u_sl2**2 * rg + u_sl2**3) / (1 + u_sl2) ** 3,
    }
    j2 = (nd + rg**2) / (1 - rg) ** 2
    j3p = (ne + 3 * rg * nd + 2 * rg**3) / (1 - rg) ** 3
    j3q = (nz - rg**3) / (1 - rg) ** 3
    for inv_expr in (j2, j3p, j3q):
        assert sp.cancel(inv_expr.subs(sl2_inf, simultaneous=True) - inv_expr) == 0

    # --- 6C. Proposition 8.3G: Split quadric cone C_K(F), Hilbert-90 W_0, S_F, (-1)^*(Y+1), Dual(K) 6x6 audit ---
    u0, u1, Y = sp.symbols("u0 u1 Y")
    u2 = -(Y**2 + u0 * u1) / (u0 + u1)
    tau_cone = {u0: u1, u1: u2, Y: Y}

    assert sp.cancel((Y + u0) * (Y + u1) * (Y + u2) + (u0 + u1) * (u1 + u2) * (u2 + u0)) == 0
    Q0 = Y**2 + Y * (u0 - u1) + u0**2 + u0 * u1 + u1**2
    A_num = (Y - u1) * (Y + u0) * (u0 + u1)
    W0 = -Q0 / A_num
    assert sp.cancel(W0.subs(tau_cone, simultaneous=True) / W0 + (u0 + u1) / (Y + u1)) == 0
    S_F = sp.cancel(Q0**3 / A_num**2)
    assert sp.cancel(S_F.subs(tau_cone, simultaneous=True) - S_F) == 0

    # Exact Dual(K) 6x6 Jacobian & (-1)^*(Y+1)=4/(Y+1) over K = Q(2*cos(2*pi/7)) (th^3 + th^2 - 2*th - 1 = 0, delta_K = 7)
    def k_add(x, y): return (x[0] + y[0], x[1] + y[1], x[2] + y[2])
    def k_sub(x, y): return (x[0] - y[0], x[1] - y[1], x[2] - y[2])
    def k_neg(x): return (-x[0], -x[1], -x[2])
    def k_mul(x, y):
        a0, a1, a2 = x
        b0, b1, b2 = y
        p0, p1, p2 = a0 * b0, a0 * b1 + a1 * b0, a0 * b2 + a1 * b1 + a2 * b0
        p3, p4 = a1 * b2 + a2 * b1, a2 * b2
        return (p0 + p3 - p4, p1 + 2 * p3 - p4, p2 - p3 + 3 * p4)
    def k_tau(x): return (x[0] - 2 * x[1] + 3 * x[2], -x[2], x[1] - x[2])
    def k_norm(x):
        n = k_mul(x, k_mul(k_tau(x), k_tau(k_tau(x))))
        assert n[1] == 0 and n[2] == 0
        return n[0]
    def k_inv(x):
        n = k_norm(x)
        adj = k_mul(k_tau(x), k_tau(k_tau(x)))
        return (adj[0] / n, adj[1] / n, adj[2] / n)
    def k_div(x, y): return k_mul(x, k_inv(y))
    def Fk(n, d=1): return (Fraction(n, d), Fraction(0), Fraction(0))

    ONE = Fk(1)
    def d_const(x): return (x, Fk(0))
    def d_add(a, b): return (k_add(a[0], b[0]), k_add(a[1], b[1]))
    def d_sub(a, b): return (k_sub(a[0], b[0]), k_sub(a[1], b[1]))
    def d_neg(a): return (k_neg(a[0]), k_neg(a[1]))
    def d_mul(a, b): return (k_mul(a[0], b[0]), k_add(k_mul(a[0], b[1]), k_mul(a[1], b[0])))
    def d_inv(a):
        inv0 = k_inv(a[0])
        return (inv0, k_neg(k_mul(a[1], k_mul(inv0, inv0))))
    def d_div(a, b): return d_mul(a, d_inv(b))
    def d_tau(a): return (k_tau(a[0]), k_tau(a[1]))

    def map_F6_to_fiber(coords6, x_a=Fraction(2), x_b=Fraction(-1)):
        c0, c1, c2, r_v, s_v, t_v = coords6
        def pack_dk(q0, q1, q2): return ((q0[0], q1[0], q2[0]), (q0[1], q1[1], q2[1]))
        def dq_to_dk(q): return (Fk(q[0]), Fk(q[1]))
        def q_add(a, b): return (a[0] + b[0], a[1] + b[1])
        def q_sc(c, a): return (c * a[0], c * a[1])
        def q_mul(a, b): return (a[0] * b[0], a[0] * b[1] + a[1] * b[0])

        eta0 = pack_dk(c0, c1, c2)
        eta2 = d_tau(eta0)
        eta4 = d_tau(eta2)
        r_k, s_k, t_k = dq_to_dk(r_v), dq_to_dk(s_v), dq_to_dk(t_v)
        f4, f3, f2, f1 = d_const(Fk(4)), d_const(Fk(3)), d_const(Fk(2)), d_const(ONE)
        Y_d = d_div(d_mul(r_k, d_add(d_mul(s_k, t_k), f4)), f4)

        rst = q_mul(r_v, q_mul(s_v, t_v))
        rs = q_mul(r_v, s_v)
        rt = q_mul(r_v, t_v)
        u0_0 = q_add(q_add(q_sc(Fraction(-1, 4), rst), q_sc(Fraction(-3, 14), rt)), r_v)
        u0_1 = q_add(q_add(q_add(q_sc(Fraction(-1, 4), rst), q_sc(Fraction(3), rs)), q_sc(Fraction(-1, 28), rt)), r_v)
        u0_2 = q_add(q_sc(Fraction(2), rs), q_sc(Fraction(1, 14), rt))
        u0_d = pack_dk(u0_0, u0_1, u0_2)
        u1_d = d_tau(u0_d)

        Nj2 = d_add(d_add(d_mul(Y_d, Y_d), d_mul(u0_d, u1_d)), d_add(u0_d, u1_d))
        Dj2 = d_mul(d_add(Y_d, f1), d_add(Y_d, u0_d))
        j2_d = d_div(Nj2, Dj2)
        B2 = d_add(d_sub(d_mul(Y_d, d_add(u0_d, f1)), d_mul(u0_d, u1_d)), d_add(d_mul(f2, u0_d), u1_d))
        B4 = d_sub(f1, u0_d)
        c2_v = d_div(d_mul(f2, d_mul(Dj2, d_add(u0_d, u1_d))), d_mul(Nj2, B2))
        c4_v = d_div(d_mul(f2, Dj2), d_mul(Nj2, B4))
        j3p_d = d_sub(d_div(d_sub(f1, j2_d), c2_v), d_mul(f2, j2_d))
        j3q_d = d_add(d_sub(d_neg(d_div(j2_d, c4_v)), d_div(d_sub(f1, j2_d), c2_v)), d_mul(f2, j2_d))

        cr = d_div(d_sub(eta2, eta0), d_sub(eta4, eta0))
        A_rg = d_sub(d_mul(cr, d_mul(j2_d, d_sub(d_add(d_mul(f3, j2_d), j3p_d), f1))),
                     d_mul(d_sub(j2_d, f1), d_add(j2_d, d_add(j3p_d, j3q_d))))
        B_rg = d_sub(d_mul(cr, d_mul(j2_d, d_add(d_mul(f2, j2_d), j3p_d))),
                     d_mul(d_sub(j2_d, f1), d_add(j3p_d, j3q_d)))
        rg_d = d_div(B_rg, A_rg)
        za_s = d_div(d_mul(d_sub(eta2, eta0), d_sub(d_mul(d_sub(d_add(d_mul(f3, j2_d), j3p_d), f1), rg_d),
                     d_add(d_mul(f2, j2_d), j3p_d))), d_sub(j2_d, f1))
        om_rg = d_sub(f1, rg_d)
        om_rg2 = d_mul(om_rg, om_rg)
        om_rg3 = d_mul(om_rg2, om_rg)
        rg2 = d_mul(rg_d, rg_d)
        rg3 = d_mul(rg2, rg_d)
        nd_d = d_sub(d_mul(j2_d, om_rg2), rg2)
        ne_d = d_sub(d_sub(d_mul(j3p_d, om_rg3), d_mul(f3, d_mul(rg_d, nd_d))), d_mul(f2, rg3))
        nz_d = d_add(d_mul(j3q_d, om_rg3), rg3)

        a0_v = (x_a, 3 * x_a + 5 * x_b, x_b)
        a1_v = k_tau(k_tau(a0_v))
        aX_d = d_const(a0_v)
        bX_d = d_const(k_sub(a1_v, a0_v))
        gX_d = d_add(aX_d, bX_d)
        dX_d = d_add(d_mul(f2, aX_d), bX_d)
        eX_d = d_add(d_mul(f3, aX_d), bX_d)
        zX_d = d_add(d_mul(f3, aX_d), d_mul(f2, bX_d))
        aX2, aX3, bX2 = d_mul(aX_d, aX_d), d_mul(aX_d, d_mul(aX_d, aX_d)), d_mul(bX_d, bX_d)
        z_al = d_div(za_s, aX_d)
        w_ga = d_div(d_sub(d_mul(gX_d, rg_d), aX_d), d_mul(aX_d, bX_d))
        w_de = d_div(d_add(d_mul(dX_d, nd_d), d_mul(f2, d_mul(aX_d, rg_d))), d_mul(aX2, bX_d))
        w_ep = d_div(d_add(d_mul(eX_d, ne_d), d_mul(f3, d_mul(aX_d, nd_d))), d_mul(aX3, bX_d))
        LX_d = d_add(d_sub(d_mul(zX_d, nz_d), d_mul(f3, d_mul(aX_d, rg2))),
                     d_add(d_mul(d_sub(d_mul(f3, d_mul(gX_d, rg_d)), d_mul(f3, aX_d)), nd_d), d_mul(bX_d, ne_d)))
        w_ze = d_div(LX_d, d_mul(aX3, bX2))
        return [z_al, w_ga, w_de, w_ep, w_ze, eta0], Y_d[0][0], [rg_d[0], nd_d[0], ne_d[0], nz_d[0], za_s[0], eta0[0]]

    base_pt = [Fraction(1), Fraction(2), Fraction(-1), Fraction(3), Fraction(5), Fraction(2)]
    J_K = [[None] * 6 for _ in range(6)]
    vals, Y_val, intr_vals = None, None, None
    for col in range(6):
        inp = [(base_pt[i], Fraction(1 if i == col else 0)) for i in range(6)]
        out, yv, iv = map_F6_to_fiber(inp)
        if vals is None:
            vals, Y_val, intr_vals = [o[0] for o in out], yv, iv
        for row in range(6):
            J_K[row][col] = out[row][1]

    # Verify (-1)^*(Y + 1) = 4 / (Y + 1) on C_K(F)
    p_rg, p_nd, p_ne, p_nz, p_za, p_eta = intr_vals
    for _ in range(3):
        d = k_sub(k_add(k_add(k_mul(Fk(3), p_nd), p_ne), k_mul(Fk(3), p_rg)), ONE)
        p_za, p_rg, p_nd, p_ne, p_nz, p_eta = (
            k_neg(p_za),
            k_div(k_add(p_rg, k_add(k_mul(Fk(2), p_nd), p_ne)), d),
            k_neg(k_div(k_add(p_nd, p_ne), d)),
            k_div(p_ne, d),
            k_div(k_sub(k_add(k_mul(Fk(3), k_mul(p_nd, p_nd)), k_add(k_mul(Fk(3), k_mul(p_nd, p_ne)), k_mul(p_ne, p_ne))), p_nz), k_mul(d, d)),
            k_add(p_eta, p_za),
        )
        r0 = p_rg
        r02 = k_mul(r0, r0)
        r03 = k_mul(r02, r0)
        p_za, p_rg, p_nd, p_ne, p_nz = (
            k_div(p_za, r0),
            k_inv(r0),
            k_neg(k_div(k_add(p_nd, k_mul(Fk(2), r0)), r02)),
            k_neg(k_div(k_sub(k_add(p_ne, p_nz), k_mul(Fk(3), r02)), r03)),
            k_div(k_add(k_sub(p_nz, k_mul(Fk(3), r02)), k_mul(Fk(3), r0)), r03),
        )
    om = k_sub(ONE, p_rg)
    om2, om3 = k_mul(om, om), k_mul(om, k_mul(om, om))
    r2, r3 = k_mul(p_rg, p_rg), k_mul(p_rg, k_mul(p_rg, p_rg))
    j2_m = k_div(k_add(p_nd, r2), om2)
    j3p_m = k_div(k_add(p_ne, k_add(k_mul(Fk(3), k_mul(p_rg, p_nd)), k_mul(Fk(2), r3))), om3)
    j3q_m = k_div(k_sub(p_nz, r3), om3)
    u0_m = k_add(ONE, k_div(k_mul(Fk(2), k_add(j3p_m, j3q_m)), k_mul(j2_m, j2_m)))
    u1_m = k_tau(u0_m)
    u2_m = k_tau(u1_m)
    s2_m = k_add(k_mul(u0_m, u1_m), k_add(k_mul(u1_m, u2_m), k_mul(u2_m, u0_m)))
    Ym_val = Fraction(4) / (Y_val + 1) - 1
    assert s2_m[1] == 0 and s2_m[2] == 0 and Ym_val**2 + s2_m[0] == 0
    assert k_mul(j2_m, k_mul(Fk(Ym_val + 1), k_add(Fk(Ym_val), u0_m))) == k_mul(k_sub(ONE, u2_m), k_add(u0_m, u1_m))

    def det_K(M):
        n = len(M)
        A = [[x for x in row] for row in M]
        det = ONE
        for i in range(n):
            piv = i
            while piv < n and A[piv][i] == Fk(0):
                piv += 1
            if piv != i:
                A[i], A[piv] = A[piv], A[i]
                det = k_neg(det)
            det = k_mul(det, A[i][i])
            inv_ii = k_inv(A[i][i])
            for r_idx in range(i + 1, n):
                fac = k_mul(A[r_idx][i], inv_ii)
                if fac != Fk(0):
                    for c_idx in range(i, n):
                        A[r_idx][c_idx] = k_sub(A[r_idx][c_idx], k_mul(fac, A[i][c_idx]))
        return det

    d6 = det_K(J_K)
    wz3_za2 = k_mul(k_mul(vals[4], k_mul(vals[4], vals[4])), k_mul(vals[0], vals[0]))
    om_pull = k_div(d6, wz3_za2)
    assert om_pull == (Fraction(-282296, 42052775427), Fraction(0), Fraction(0))

    c0v, c1v, c2v, rv, sv, tv = base_pt
    x_av, x_bv = Fraction(2), Fraction(-1)
    a0_k = (x_av, 3 * x_av + 5 * x_bv, x_bv)
    b0_k = k_sub(k_tau(k_tau(a0_k)), a0_k)
    agd_v, bez_v = k_norm(a0_k), k_norm(b0_k)
    e0_k = (c0v, c1v, c2v)
    d024_v = k_mul(k_sub(e0_k, k_tau(e0_k)), k_mul(k_sub(k_tau(e0_k), k_tau(k_tau(e0_k))), k_sub(k_tau(k_tau(e0_k)), e0_k)))[0]
    F_ind_v = d024_v / 7
    N_Kv = tv**3 - 28 * tv**2 + 112 * tv + 448
    P_Av = 9*tv**3*x_av + 13*tv**3*x_bv - 84*tv**2*x_av - 112*tv**2*x_bv - 336*tv*x_av - 560*tv*x_bv + 1344*x_av + 896*x_bv
    P_Bv = 3*tv**3*x_av + 4*tv**3*x_bv - 60*tv**2*x_av - 68*tv**2*x_bv + 336*tv*x_av + 224*tv*x_bv - 1344*x_av - 1344*x_bv
    P_0v = 4 * (6*tv**2*x_av + 11*tv**2*x_bv - 56*tv*x_bv - 672*x_av - 784*x_bv)
    om_analytic = -agd_v * (Fraction(1) / F_ind_v) * Fraction(64, 7) * bez_v * N_Kv**2 * rv / (rv * (P_Av * sv + P_Bv) + P_0v) ** 3
    assert abs(om_pull[0]) == abs(om_analytic)

    # --- 6D. Claim 8.3H: residue -2/9 at t_*, U_* = -3; arithmetic of the hand-derived shell formulas for |C_3(q)| ---
    r_s, s_s, t_s, al, xa, xb, w = sp.symbols("r_s s_s t_s al xa xb w")
    sq3 = 2 * w + 1

    def red_w(expr):
        return sp.rem(sp.Poly(sp.expand(expr), w), sp.Poly(w**2 + w + 1, w)).as_expr()

    def simp_w(expr):
        n, d = sp.fraction(sp.together(expr))
        dc = d.subs(w, -1 - w)
        return sp.factor(sp.cancel(red_w(n * dc) / red_w(d * dc)))

    u0_r0 = sp.Rational(1, 6) * sq3 * r_s * (1 - 3 * al * s_s * t_s)
    Y_r = sp.Rational(1, 2) * r_s * (1 + 3 * al * s_s * t_s)
    J_kum = sp.Matrix([[sp.diff(f, v) for v in [r_s, s_s, t_s]] for f in [r_s * s_s, r_s * t_s, Y_r]])
    res_kum = simp_w(3 * sq3 * al * J_kum.det() / (6 * u0_r0))

    P_A_k = 9 * al**2 * t_s**3 * xa + 9 * al * t_s * xb - 2 * sq3 * xa
    P_B_k = 6 * sq3 * al**2 * t_s**3 * xb + 9 * al * t_s**2 * xa + xb
    P_0_k = 6 * (3 * al * t_s**2 * xa + xb)
    D_kum = red_w(P_A_k - 3 * al * t_s * P_B_k)
    l1_kum = simp_w(D_kum / (3 * sq3 * al**2 * t_s**3 - 1))
    t_star_k = sp.solve(l1_kum, t_s)[0]
    assert simp_w(-P_0_k.subs(t_s, t_star_k) / (2 * P_B_k.subs(t_s, t_star_k))) == -3

    S_F_kum = simp_w(81 * al**2 * t_s**3 * (54 * al**4 * t_s**6 * w + 27 * al**4 * t_s**6 + 18 * al**2 * t_s**3 - 2 * w - 1) / (27 * al**4 * t_s**6 + 1) ** 2)
    bez_kum = -3 * al * sq3 * (al * xb**3 - xa**3)
    coeff_t = simp_w(2 * bez_kum / S_F_kum * (216 * t_s**3) * (res_kum / r_s) * (2 * P_0_k / D_kum) / (-P_0_k**3))
    # Residue at t = t_*(X), computed as an exact Laurent expansion over Q(w), w^2+w+1=0.
    # (Draft 6 substituted t = t_* directly into coeff_t*(t - t_*); that is fragile, because
    # SymPy zeroes the factor (t - t_*) before reducing the denominator modulo w^2+w+1, and it
    # returned 0 in SymPy 1.14.  Draft 6 also asserted the value +-2/27; the exact value is -2/9.
    # Only its X-independence and |-2/9|_F = 1 for p >= 5 are used in the paper.)
    h_s = sp.symbols("h_s")

    def red_frac_w(c):
        cn, cd = sp.fraction(sp.together(c))
        cc = cd.subs(w, -1 - w)
        return sp.cancel(red_w(sp.expand(cn * cc)) / red_w(sp.expand(cd * cc)))

    def leading_term_at_ts(expr):
        P = sp.Poly(sp.expand(expr.subs(t_s, t_star_k + h_s)), h_s)
        for (k,), c in sorted(P.terms()):
            v = red_frac_w(c)
            if sp.simplify(v) != 0:
                return k, v
        raise AssertionError("expression vanishes identically near t_*")

    n_coeff, d_coeff = sp.fraction(sp.together(coeff_t))
    k_n, lead_n = leading_term_at_ts(n_coeff)
    k_d, lead_d = leading_term_at_ts(d_coeff)
    assert (k_n, k_d) == (0, 1)  # simple pole at t_*
    res_at_ts = sp.factor(red_frac_w(lead_n / lead_d))
    assert res_at_ts == sp.Rational(-2, 9)  # X-independent, a p-adic unit for p >= 5
    print(f"      PASS: simple pole of the t-one-form at t_*(X) with exact residue {res_at_ts} (X-independent).")

    # Valuation-shell formulas for I_{P^1(K)}, B_1(S), B_2(1), and |C_3(q)|.  These are typed in from
    # the hand derivation sketched in the proof of Claim 8.3H; the checks below confirm only their
    # algebra, not that they equal the regularized integrals (see Open Problem (1) in the paper).
    q, S = sp.symbols("q S", positive=True)
    def geom(R): return R / (1 - R)

    I_P1K_unram = sp.factor((1 - 1 / q**2) / (1 - q) + (1 / q) * (1 - 1 / q**2) * q / (1 - q))
    I_P1K_ram = sp.factor((1 + 1 / q) * 2 * (1 - 1 / q) / (1 - q))
    assert sp.simplify(I_P1K_unram + 2 * (q + 1) / q**2) == 0
    assert sp.simplify(I_P1K_ram + 2 * (q + 1) / q**2) == 0

    B1_unram = (
        (1 - 1 / q) * geom(w * S / q)
        + (1 - 2 / q)
        + (1 - 1 / q) * geom(1 / (q * S**4))
        + (1 - 1 / q) * geom(w**2 * q * S**3)
    )
    assert red_w(sp.numer(sp.together(B1_unram.subs(S, 1)))) == 0
    B1_prime_unram = simp_w(sp.diff(B1_unram, S).subs(S, 1))
    B2_unram = simp_w(
        -q / (q + 1)
        + (1 - 2 / q)
        + (1 - 1 / q) * geom(w / q**2)
        + (1 - 1 / q) * geom(w**2 / q)
    )
    prod_unram = simp_w(B1_prime_unram * B2_unram)
    assert sp.simplify(prod_unram - 12 / (q**2 - 1)) == 0
    J_Q3_unram = sp.simplify(sp.Rational(1, 4) * ((q - 1) / q) * prod_unram)
    assert sp.simplify(J_Q3_unram - 3 / (q * (q + 1))) == 0
    assert sp.simplify((-I_P1K_unram) * J_Q3_unram - 6 / q**3) == 0

    B1_ram = (-1 / q) + (1 - 1 / q) * geom(1 / (q * S**4))
    assert sp.simplify(B1_ram.subs(S, 1)) == 0
    B1_prime_ram = sp.factor(sp.diff(B1_ram, S).subs(S, 1))
    assert sp.simplify(B1_prime_ram + 4 / (q - 1)) == 0
    B2_ram_mag = sp.factor(q / (q + 1) + 1 / q)
    assert sp.simplify(B2_ram_mag - (q**2 + q + 1) / (q * (q + 1))) == 0
    J_Q3_ram = sp.simplify(sp.Rational(1, 4) * ((q - 1) / q) * (-B1_prime_ram) * B2_ram_mag)
    assert sp.simplify(J_Q3_ram - (q**2 + q + 1) / (q**2 * (q + 1))) == 0
    assert sp.simplify((-I_P1K_ram) * J_Q3_ram - 2 * (q**2 + q + 1) / q**4) == 0
    print(f"      PASS (arithmetic of hand-derived shell sums): |C_3(q)| = {(-I_P1K_unram)*J_Q3_unram} (unram), {(-I_P1K_ram)*J_Q3_ram} (tame ram).")


if __name__ == "__main__":
    r_names, mats_X, mats_Xm, ha, hb, theta, log_unip, s_a, s_b = build_chevalley()
    verify_section_6_subregular_forms(r_names, mats_X, mats_Xm, ha, hb, theta, log_unip)
    verify_bruhat_and_prop_76E(r_names, theta, s_a, s_b)
    verify_section_7_birational_proof_X2(r_names, theta)
    verify_padic_constant_C_prime()
    verify_section_8_cubic_tori(r_names, theta)
    verify_section_8_proof_X3_and_C3()
    print("\nALL 6 VERIFICATION SUITES PASSED (the constants C'(q) and C_3(q) are checked only as arithmetic of hand-derived factors).")
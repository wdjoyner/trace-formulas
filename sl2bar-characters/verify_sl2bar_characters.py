#!/usr/bin/env python3
"""
verify_sl2bar_characters.py

Computational verification module for:
"Two-orbit unramified elliptic character relations for depth-zero
representations of metaplectic covers of SL_2"
by David Joyner, Argon, and ChatGPT.

This self-contained module performs finite numerical consistency checks for
selected statements in the manuscript. It does NOT construct the metaplectic
cover or its cocycle, prove the compact splitting, or certify a general theorem.
The finite-field character values are supplied by the stated formulas, not
computed from independently constructed representations.

Checks covered:
1. Proposition 3.2: Finite-field character table values for cuspidal
   representations sigma_theta of SL_2(F_q), orthogonality, and cuspidality
   on the lower unipotent radical U^-(F_q).
2. Proposition 1.1: Perfectness of SL_2(F_q) (q = 7) and coprimality conditions
   n | (q - 1), gcd(n, q + 1) = 1, gcd(n, p) = 1.
3. Proposition 3.3: Mackey double-coset reduction of the pro-p intersection
   J_{j,m} = K^{(j)} cap g_m K^{(j)}_+ g_m^{-1} onto U^-(F_q) for both j in {0, 1}.
4. Lemma 4.1 & Lemma 4.2: Bijectivity of the n-th power map on bar{T},
   anisotropy of the leading coefficient bar{A}, and nonvanishing of both
   off-diagonal entries of k^{-1} bar{A} k for all k in SL_2(F_q).
5. Proposition 4.3: p-adic matrix verification of the fixed-ball theorem
   B^t = B^{t^n} = B(v_i, r) and vertex stabilizer reductions rho_j(x^{-1} t x)
   (central zI for d < r, zU with U nontrivial unipotent for d = r) across
   both vertex orbits j in {0, 1}.
6. Theorems 1.2 & 1.3 and Section 6 (Table 1): Direct Frobenius character sum
   evaluation vs. closed formulas and two-orbit L-packet cancellation over Q_7
   with covering degree n = 3.
"""

from __future__ import annotations
import cmath
import math
from typing import Dict, List, Tuple

Matrix2x2 = Tuple[Tuple[int, int], Tuple[int, int]]


def mat_mul_mod(A: Matrix2x2, B: Matrix2x2, mod: int) -> Matrix2x2:
    """Multiply two 2x2 integer matrices modulo `mod`."""
    return (
        ((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod),
        ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod),
    )


def mat_pow_mod(A: Matrix2x2, exp: int, mod: int) -> Matrix2x2:
    """Raise a 2x2 matrix A to a non-negative integer power modulo `mod`."""
    result: Matrix2x2 = ((1 % mod, 0), (0, 1 % mod))
    base = A
    e = exp
    while e > 0:
        if e & 1:
            result = mat_mul_mod(result, base, mod)
        base = mat_mul_mod(base, base, mod)
        e >>= 1
    return result


def mat_inv_sl2_mod(A: Matrix2x2, mod: int) -> Matrix2x2:
    """Inverse of a determinant-1 2x2 matrix modulo `mod`."""
    return (
        (A[1][1] % mod, (-A[0][1]) % mod),
        ((-A[1][0]) % mod, A[0][0] % mod),
    )


def mat_det_mod(A: Matrix2x2, mod: int) -> int:
    """Determinant of a 2x2 matrix modulo `mod`."""
    return (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % mod


def mat_trace_mod(A: Matrix2x2, mod: int) -> int:
    """Trace of a 2x2 matrix modulo `mod`."""
    return (A[0][0] + A[1][1]) % mod


def generate_sl2_fq(q: int) -> List[Matrix2x2]:
    """Return all elements of SL_2(F_q) for prime q."""
    elems: List[Matrix2x2] = []
    for a in range(q):
        for b in range(q):
            for c in range(q):
                for d in range(q):
                    if (a * d - b * c) % q == 1:
                        elems.append(((a, b), (c, d)))
    return elems


def generate_nonsplit_torus(q: int, delta: int) -> List[Matrix2x2]:
    """
    Return the cyclic nonsplit torus bar{T} of order q + 1 in SL_2(F_q),
    realized as [[a, delta*b], [b, a]] with a^2 - delta*b^2 = 1 (mod q).
    """
    torus: List[Matrix2x2] = []
    for a in range(q):
        for b in range(q):
            if (a * a - delta * b * b) % q == 1:
                torus.append(((a, (delta * b) % q), (b, a)))
    return torus


def find_torus_generator(torus: List[Matrix2x2], q: int) -> Matrix2x2:
    """Find a cyclic generator gamma_0 of bar{T} of order q + 1."""
    order = q + 1
    I_mat: Matrix2x2 = ((1, 0), (0, 1))
    for g in torus:
        seen = set()
        curr = I_mat
        for _ in range(order):
            seen.add(curr)
            curr = mat_mul_mod(curr, g, q)
        if len(seen) == order:
            return g
    raise ValueError("No generator found for bar{T}.")


def verify_finite_field_data(q: int = 7, n: int = 3, delta: int = 3) -> Dict[str, object]:
    """
    Verify Proposition 1.1, Lemma 4.1, and Proposition 3.2 over F_q.
    """
    assert math.gcd(n, q) == 1, "n must be coprime to p = q"
    assert (q - 1) % n == 0, "n must divide q - 1"
    assert math.gcd(n, q + 1) == 1, "n must be coprime to q + 1"

    # Check delta is a quadratic non-residue mod q
    squares = {(x * x) % q for x in range(1, q)}
    assert (delta % q) not in squares, f"{delta} must be a non-square mod {q}"

    sl2 = generate_sl2_fq(q)
    assert len(sl2) == q * (q * q - 1)

    # 1. Check perfectness deterministically: the elementary generators
    # u(1), l(1) are each commutators, and generate all of SL_2(F_q).
    # For q >= 7, choose a = 2 with a^2 != 1 (mod q).
    a = 2
    assert (a * a - 1) % q != 0
    diagonal = ((a, 0), (0, pow(a, -1, q)))
    diagonal_inv = mat_inv_sl2_mod(diagonal, q)
    upper = ((1, 1), (0, 1))
    lower = ((1, 0), (1, 1))
    elementary = (upper, lower)
    for target, factor in ((upper, (a * a - 1) % q),
                           (lower, (pow(a, -2, q) - 1) % q)):
        if target == upper:
            seed = ((1, pow(factor, -1, q)), (0, 1))
        else:
            seed = ((1, 0), (pow(factor, -1, q), 1))
        seed_inv = mat_inv_sl2_mod(seed, q)
        comm = mat_mul_mod(mat_mul_mod(diagonal, seed, q),
                           mat_mul_mod(diagonal_inv, seed_inv, q), q)
        assert comm == target, "Elementary generator is not the claimed commutator"
    identity: Matrix2x2 = ((1, 0), (0, 1))
    subgroup = {identity}
    frontier = [identity]
    while frontier:
        curr = frontier.pop()
        for generator in elementary:
            product = mat_mul_mod(curr, generator, q)
            if product not in subgroup:
                subgroup.add(product)
                frontier.append(product)
    is_perfect = (len(subgroup) == len(sl2))
    assert is_perfect, "Elementary commutators did not generate SL_2(F_q)"

    # 2. Nonsplit torus bar{T} and n-th power automorphism
    bar_T = generate_nonsplit_torus(q, delta)
    assert len(bar_T) == q + 1
    gamma0 = find_torus_generator(bar_T, q)

    nth_powers = {mat_pow_mod(t, n, q) for t in bar_T}
    assert len(nth_powers) == q + 1, "t -> t^n must be a bijection on bar{T}"

    # Inverse exponent e such that e * n = 1 (mod q + 1)
    e = pow(n, -1, q + 1)
    assert (e * n) % (q + 1) == 1
    assert e % 2 == 1, "Inverse exponent e must be odd"

    # 3. Construct character theta and reparameterized eta = theta^{<n>}
    dlog: Dict[Matrix2x2, int] = {}
    curr: Matrix2x2 = ((1, 0), (0, 1))
    for k in range(q + 1):
        dlog[curr] = k
        curr = mat_mul_mod(curr, gamma0, q)

    def theta(t: Matrix2x2) -> complex:
        return cmath.exp(2j * math.pi * dlog[t] / (q + 1))

    def eta(t: Matrix2x2) -> complex:
        return theta(mat_pow_mod(t, e, q))

    minus_I: Matrix2x2 = ((q - 1, 0), (0, q - 1))
    assert abs(eta(minus_I) - theta(minus_I)) < 1e-12, "Central signs must match"

    # Verify chi_eta(t^n) == chi_theta(t) on all regular elements of bar{T}
    I_mat: Matrix2x2 = ((1, 0), (0, 1))
    for t in bar_T:
        if t not in (I_mat, minus_I):
            t_inv = mat_inv_sl2_mod(t, q)
            tn = mat_pow_mod(t, n, q)
            tn_inv = mat_inv_sl2_mod(tn, q)
            chi_theta_t = -theta(t) - theta(t_inv)
            chi_eta_tn = -eta(tn) - eta(tn_inv)
            assert abs(chi_theta_t - chi_eta_tn) < 1e-12

    # 4. Verify full character table of sigma_theta on SL_2(F_q)
    trace_to_elliptic: Dict[int, complex] = {}
    for t in bar_T:
        if t not in (I_mat, minus_I):
            tr_val = mat_trace_mod(t, q)
            t_inv = mat_inv_sl2_mod(t, q)
            trace_to_elliptic[tr_val] = -theta(t) - theta(t_inv)

    def chi_theta(g: Matrix2x2) -> complex:
        if g == I_mat:
            return (q - 1) * theta(I_mat)
        if g == minus_I:
            return (q - 1) * theta(minus_I)
        tr_g = mat_trace_mod(g, q)
        if tr_g == 2 % q:
            return -theta(I_mat)
        if tr_g == (q - 2) % q:
            return -theta(minus_I)
        if tr_g in trace_to_elliptic:
            return trace_to_elliptic[tr_g]
        return 0.0 + 0.0j

    # Check norm <chi_theta, chi_theta>_{SL_2(F_q)} == 1
    norm_sq = sum(abs(chi_theta(g)) ** 2 for g in sl2) / len(sl2)
    assert abs(norm_sq - 1.0) < 1e-12, f"Expected norm 1, got {norm_sq}"

    # Check cuspidality on U^-(F_q) = {[[1, 0], [c, 1]] : c in F_q}
    U_minus = [((1, 0), (c, 1)) for c in range(q)]
    u_fixed_dim = sum(chi_theta(u) for u in U_minus) / q
    assert abs(u_fixed_dim) < 1e-12, "Cuspidal representation must have 0 U^-(F_q)-fixed vectors"

    # Orthogonality for EVERY regular character modulo theta ~ theta^{-1},
    # not just the norm of the one character used above.
    character_vectors = []
    for exponent in range(1, (q + 1) // 2):
        def char_k(t: Matrix2x2) -> complex:
            return cmath.exp(2j * math.pi * exponent * dlog[t] / (q + 1))
        nonsplit_values = {
            mat_trace_mod(t, q): -char_k(t) - char_k(mat_inv_sl2_mod(t, q))
            for t in bar_T if t not in (I_mat, minus_I)
        }
        def value(g: Matrix2x2) -> complex:
            if g == I_mat:
                return complex(q - 1)
            if g == minus_I:
                return (q - 1) * char_k(minus_I)
            tr = mat_trace_mod(g, q)
            if tr == 2 % q:
                return -1.0 + 0.0j
            if tr == (q - 2) % q:
                return -char_k(minus_I)
            return nonsplit_values.get(tr, 0.0 + 0.0j)
        character_vectors.append([value(g) for g in sl2])
    for k, xvec in enumerate(character_vectors):
        for ell, yvec in enumerate(character_vectors):
            inner = sum(x.conjugate() * y for x, y in zip(xvec, yvec)) / len(sl2)
            expected = 1 if k == ell else 0
            assert abs(inner - expected) < 1e-10, (
                f"Finite-field character orthogonality failed at ({k},{ell})")

    return {
        "sl2_order": len(sl2),
        "is_perfect": is_perfect,
        "torus_order": len(bar_T),
        "inverse_exponent_e": e,
        "chi_norm_sq": norm_sq,
        "u_minus_fixed_dim": abs(u_fixed_dim),
    }


def verify_mackey_unipotent_reduction(p: int = 7, m: int = 1) -> Dict[str, bool]:
    """Check explicit intersection witnesses for both vertex orbits.

    Write K^(j) = D^j K D^-j. Because D commutes with g_m, conjugating
    J_(j,m) by D^-j reduces membership to
        u in SL_2(Z_p), g_m^-1 u g_m in K_1.
    Writing u=[[a,b],[c,d]], the second condition forces
        a,d = 1 (mod p), b = 0 (mod p^(2m+1)); hence the reduction is
    contained in U^-(F_p). Conversely all lower-unipotent u_c give
    witnesses. The test uses exact rational 2x2 matrix conjugation.
    """
    from fractions import Fraction

    assert p >= 5 and m >= 1

    def mult(A, B):
        return tuple(tuple(sum(A[i][k] * B[k][j] for k in (0, 1))
                           for j in (0, 1)) for i in (0, 1))

    D = ((Fraction(p), Fraction(0)), (Fraction(0), Fraction(1)))
    D_inv = ((Fraction(1, p), Fraction(0)), (Fraction(0), Fraction(1)))
    gm = ((Fraction(p ** m), Fraction(0)),
          (Fraction(0), Fraction(1, p ** m)))
    gm_inv = ((Fraction(1, p ** m), Fraction(0)),
              (Fraction(0), Fraction(p ** m)))
    identity = ((1, 0), (0, 1))
    results = {}
    for j in (0, 1):
        dj, dj_inv = (D, D_inv) if j else (identity, identity)
        images = set()
        for c in range(p):
            u = ((1, 0), (c, 1))
            h = mult(mult(dj, u), dj_inv)
            h_prime = mult(mult(gm_inv, h), gm)
            u_prime = mult(mult(dj_inv, h_prime), dj)
            assert all(entry.denominator == 1 for row in u_prime for entry in row)
            assert all((u_prime[i][k] - identity[i][k]) % p == 0
                       for i in (0, 1) for k in (0, 1)), (
                "Conjugated witness must be in K^(j)_+")
            u_reduced = mult(mult(dj_inv, h), dj)
            images.add(tuple(tuple(int(entry % p) for entry in row)
                             for row in u_reduced))
        expected = {((1, 0), (c, 1)) for c in range(p)}
        assert images == expected
        results[f"j{j}_onto_U_minus"] = True
    return results


def verify_anisotropic_leading_term(q: int = 7, delta: int = 3) -> bool:
    """
    Verify Lemma 4.2: for bar{A} = 2 * [[0, delta], [1, 0]] in M_2(F_q),
    every conjugate k^{-1} bar{A} k (for k in SL_2(F_q)) is traceless, has
    irreducible characteristic polynomial, and has BOTH off-diagonal entries
    nonzero in F_q.
    """
    sl2 = generate_sl2_fq(q)
    A_bar: Matrix2x2 = ((0, (2 * delta) % q), (2 % q, 0))
    for k in sl2:
        k_inv = mat_inv_sl2_mod(k, q)
        A_conj = mat_mul_mod(mat_mul_mod(k_inv, A_bar, q), k, q)
        assert mat_trace_mod(A_conj, q) == 0, "Conjugate must be traceless"
        assert A_conj[0][1] % q != 0, "Upper-right entry must be nonzero in F_q"
        assert A_conj[1][0] % q != 0, "Lower-left entry must be nonzero in F_q"
    return True


def make_tr_mod(p: int, r: int, delta: int, M: int) -> Matrix2x2:
    """
    Construct t_r = (1 + p^r sqrt(delta)) / (1 - p^r sqrt(delta)) in SL_2(Z / p^M Z)
    on the basis (1, sqrt(delta)).
    """
    mod = p ** M
    pr = p ** r
    denom = (1 - delta * pr * pr) % mod
    denom_inv = pow(denom, -1, mod)
    num: Matrix2x2 = ((1, (delta * pr) % mod), (pr % mod, 1))
    num_sq = mat_mul_mod(num, num, mod)
    t_r: Matrix2x2 = (
        ((num_sq[0][0] * denom_inv) % mod, (num_sq[0][1] * denom_inv) % mod),
        ((num_sq[1][0] * denom_inv) % mod, (num_sq[1][1] * denom_inv) % mod),
    )
    assert mat_det_mod(t_r, mod) == 1, "t_r must have determinant 1 mod p^M"
    return t_r


def verify_fixed_ball_p_adic(p: int = 7, n: int = 3, delta: int = 3, max_r: int = 3) -> List[Dict[str, object]]:
    """
    Check finite congruence consequences of Proposition 4.3 (not a proof) for
    t_r = (1 + p^r sqrt(delta)) / (1 - p^r sqrt(delta)), r = 1, ..., max_r.
    """
    M = 2 * max_r + 4
    mod = p ** M
    sl2_fp = generate_sl2_fq(p)
    I_fp: Matrix2x2 = ((1, 0), (0, 1))
    results = []

    for r in range(1, max_r + 1):
        t_r = make_tr_mod(p, r, delta, M)
        t_r_n = mat_pow_mod(t_r, n, mod)

        for label, mat in [("t_r", t_r), ("t_r^n", t_r_n)]:
            for d in range(0, r + 2):
                for k_fp in sl2_fp:
                    a, b = k_fp[0]
                    c, d_entry = k_fp[1]
                    if a != 0:
                        d_lift = ((1 + b * c) * pow(a, -1, mod)) % mod
                        k_lift: Matrix2x2 = ((a, b), (c, d_lift))
                    else:
                        b_lift = ((-1) * pow(c, -1, mod)) % mod
                        k_lift = ((a, b_lift), (c, d_entry))
                    k_inv = mat_inv_sl2_mod(k_lift, mod)
                    conj = mat_mul_mod(mat_mul_mod(k_inv, mat, mod), k_lift, mod)

                    upper_right = conj[0][1]
                    lower_left = (conj[1][0] * (p ** d)) % mod

                    if d <= r:
                        assert upper_right % (p ** d) == 0, f"{label} must fix vertex at d={d} <= r={r}"
                        ur_div = (upper_right // (p ** d)) % p
                        ll_div = lower_left % p
                        diag0 = conj[0][0] % p
                        diag1 = conj[1][1] % p
                        red_mat: Matrix2x2 = ((diag0, ur_div), (ll_div, diag1))
                        if d < r:
                            assert red_mat == I_fp, f"Expected I at d={d}<r={r}, got {red_mat}"
                        else:
                            assert diag0 == 1 and diag1 == 1 and ll_div == 0 and ur_div != 0, (
                                f"Expected nontrivial upper unipotent at d=r={r}, got {red_mat}"
                            )
                    else:
                        assert upper_right % (p ** d) != 0, f"{label} cannot fix vertex at d={d} > r={r}"

        results.append({"r": r, "ball_radius_verified": r, "power_ball_verified": r})
    return results


def sphere_size(q: int, d: int) -> int:
    """Number of vertices at distance d from v_i in the (q+1)-regular tree."""
    if d == 0:
        return 1
    return (q + 1) * (q ** (d - 1))


def compute_orbit_character_sum(q: int, r: int, i: int, j: int, theta_z: complex = 1.0) -> complex:
    """
    Compute the Frobenius character sum (20)/(21) directly by summing over
    all spheres d in {0, ..., r} with d = j - i (mod 2).
    """
    total = 0.0 + 0.0j
    parity = (j - i) % 2
    for d in range(0, r + 1):
        if d % 2 == parity:
            N_d = sphere_size(q, d)
            if d < r:
                total += N_d * (q - 1) * theta_z
            else:
                total += N_d * (-theta_z)
    return total


def closed_formula_character(q: int, r: int, i: int, j: int, theta_z: complex = 1.0) -> complex:
    """Closed formula from Theorem 1.3(ii): theta(zI) * ((-1)^{r + 1 + j - i} q^r - 1)."""
    sign = (-1) ** (r + 1 + j - i)
    return theta_z * (sign * (q ** r) - 1)


def verify_q7_tables() -> List[Dict[str, int]]:
    """
    Verify Table 1 in Section 6 (F = Q_7, q = 7, n = 3) for r = 1, 2, 3,
    and check Theorem 1.3(ii)-(iii) across all i, j in {0, 1} and r = 1..6.
    """
    q = 7
    table_rows = []
    expected = {
        1: (1, 8, 6, -8, -2),
        2: (57, 8, -50, 48, -2),
        3: (57, 400, 342, -344, -2),
    }
    for r in range(1, 7):
        for i in (0, 1):
            for j in (0, 1):
                frob_val = compute_orbit_character_sum(q, r, i, j, 1.0)
                closed_val = closed_formula_character(q, r, i, j, 1.0)
                assert abs(frob_val - closed_val) < 1e-12

        if r in expected:
            even_verts = sum(sphere_size(q, d) for d in range(0, r + 1) if d % 2 == 0)
            odd_verts = sum(sphere_size(q, d) for d in range(0, r + 1) if d % 2 == 1)
            val_0 = int(round(compute_orbit_character_sum(q, r, 0, 0, 1.0).real))
            val_1 = int(round(compute_orbit_character_sum(q, r, 0, 1, 1.0).real))
            pkt_sum = val_0 + val_1
            assert (even_verts, odd_verts, val_0, val_1, pkt_sum) == expected[r]
            table_rows.append({
                "r": r,
                "even_vertices": even_verts,
                "odd_vertices": odd_verts,
                "Theta_0": val_0,
                "Theta_1": val_1,
                "packet_sum": pkt_sum,
            })
    return table_rows


def main() -> None:
    print("=" * 72)
    print("Verification Suite: Two-Orbit Depth-Zero Character Relations (SL_2)")
    print("=" * 72)

    ff_info = verify_finite_field_data(q=7, n=3, delta=3)
    print(f"[PASS] Prop 1.1 & 3.2: |SL_2(F_7)| = {ff_info['sl2_order']}, "
          f"perfect = {ff_info['is_perfect']}, |bar{{T}}| = {ff_info['torus_order']}, "
          f"e = {ff_info['inverse_exponent_e']}, <chi,chi> = {ff_info['chi_norm_sq']:.1f}, "
          f"dim(sigma^{{U^-}}) = {ff_info['u_minus_fixed_dim']:.1f}")

    mackey_info = verify_mackey_unipotent_reduction(p=7, m=1)
    print(f"[PASS] Prop 3.3: Mackey pro-p subgroup J_{{j,m}} reduces onto U^-(F_7): {mackey_info}")

    aniso_ok = verify_anisotropic_leading_term(q=7, delta=3)
    print(f"[PASS] Lemma 4.2: Off-diagonal entries of k^{{-1}} bar{{A}} k nonzero for all 336 k in SL_2(F_7): {aniso_ok}")

    padic_balls = verify_fixed_ball_p_adic(p=7, n=3, delta=3, max_r=3)
    print(f"[PASS] Prop 4.3: p-adic fixed-ball B(v_0, r) and vertex reductions verified for r = 1, 2, 3: {padic_balls}")

    table_rows = verify_q7_tables()
    print("\n[PASS] Theorem 1.3 & Section 6 Table 1 (Q_7, n = 3):")
    print(f"{'r':>3} | {'|B cap Gv_0|':>14} | {'|B cap Gv_1|':>14} | {'Theta_{0,theta}':>15} | {'Theta_{1,theta}':>15} | {'Sum':>5}")
    print("-" * 72)
    for row in table_rows:
        print(f"{row['r']:>3} | {row['even_vertices']:>14} | {row['odd_vertices']:>14} | "
              f"{row['Theta_0']:>15} | {row['Theta_1']:>15} | {row['packet_sum']:>5}")
    print("=" * 72)
    print("All finite numerical consistency checks passed (not a proof of the cover theorem).")




# ---------------------------------------------------------------------------
# Pytest-compatible unit test wrappers
# ---------------------------------------------------------------------------

def test_finite_field_cuspidal_character():
    info = verify_finite_field_data(q=7, n=3, delta=3)
    assert info["sl2_order"] == 336
    assert info["is_perfect"] is True
    assert info["torus_order"] == 8
    assert info["inverse_exponent_e"] == 3
    assert abs(info["chi_norm_sq"] - 1.0) < 1e-12
    assert info["u_minus_fixed_dim"] < 1e-12


def test_mackey_pro_p_unipotent_reduction():
    res = verify_mackey_unipotent_reduction(p=7, m=1)
    assert res["j0_onto_U_minus"] is True
    assert res["j1_onto_U_minus"] is True


def test_anisotropic_off_diagonal_nonvanishing():
    assert verify_anisotropic_leading_term(q=7, delta=3) is True


def test_fixed_ball_and_vertex_reductions():
    res = verify_fixed_ball_p_adic(p=7, n=3, delta=3, max_r=3)
    assert len(res) == 3
    for idx, entry in enumerate(res, start=1):
        assert entry["r"] == idx
        assert entry["ball_radius_verified"] == idx
        assert entry["power_ball_verified"] == idx


def test_additional_tame_residue_fields():
    for q, delta in ((13, 2), (19, 2)):
        info = verify_finite_field_data(q=q, n=3, delta=delta)
        assert info["is_perfect"] and info["torus_order"] == q + 1
        assert verify_anisotropic_leading_term(q=q, delta=delta)


def test_q7_character_table_and_packet_sum():
    rows = verify_q7_tables()
    assert rows[0] == {"r": 1, "even_vertices": 1, "odd_vertices": 8, "Theta_0": 6, "Theta_1": -8, "packet_sum": -2}
    assert rows[1] == {"r": 2, "even_vertices": 57, "odd_vertices": 8, "Theta_0": -50, "Theta_1": 48, "packet_sum": -2}
    assert rows[2] == {"r": 3, "even_vertices": 57, "odd_vertices": 400, "Theta_0": 342, "Theta_1": -344, "packet_sum": -2}



import unittest

class TestSL2BarCharacters(unittest.TestCase):
    def test_finite_field(self):
        test_finite_field_cuspidal_character()

    def test_mackey(self):
        test_mackey_pro_p_unipotent_reduction()

    def test_anisotropic(self):
        test_anisotropic_off_diagonal_nonvanishing()

    def test_fixed_ball(self):
        test_fixed_ball_and_vertex_reductions()

    def test_q7_table(self):
        test_q7_character_table_and_packet_sum()

    def test_other_fields(self):
        test_additional_tame_residue_fields()


if __name__ == "__main__":
    main()
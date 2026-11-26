#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""
twofold_cover_check.py

Exact checks for "Notes on characters of supercuspidal representations of the
twofold metaplectic cover of SL_2(F), F p-adic" (character_relations_twofold.tex,
Draft 2).  Everything is computed over F = Q_p with rational matrix entries and
exact arithmetic (fractions.Fraction).  The quadratic Hilbert symbol of Q_p is
evaluated by the tame formula, which is exact for rational arguments.

The script checks the following statements of the paper on random samples.
These are consistency checks.  The proofs in the paper do not depend on them.

 1. The Kubota function beta is a 2-cocycle on SL_2(Q_p)           (eq. (3.2))
 2. beta is trivial on upper and on lower unipotent pairs           (Lemma 3.5)
 3. r_0 splits beta over K_0 = SL_2(Z_p)                            (eq. (3.3))
 4. The lifted Weyl and torus elements                              (Lemma 3.6)
 5. The extended function beta' is a 2-cocycle on GL_2(Q_p)         (eq. (3.4))
 6. Edge discrepancy s_1(k) = ell(a) s_0(k) on the Iwahori subgroup,
    with s_1 computed in two independent ways: from unipotent
    generators (Lemma 3.5) and from conjugation by the lift of
    D = diag(p,1) in the cover of GL_2 (eq. (3.5))                  (Prop. 3.8)
 7. s_1 is multiplicative on K_1                                    (Lemma 3.3)
 8. Conjugation by (h(u),1) preserves the Kubota coordinate, and
    conjugation by (diag(r1,r2),1) in the cover of GL_2 multiplies
    it by v(r1 r2, g).  Formula r_1(k) = r_0(k0) v(p,k0)             (Prop. 7.1,
    Example 7.2)
 9. Sphere sums, closed formulas and the tables                     (Thm. 5.4,
    Cor. 5.6, Section 6)
10. Fixed balls of t_r in the tree over Q_p, by listing lattices    (Prop. 5.1)

Statement numbers refer to Draft 2 (November 26, 2026).
"""
import random
import sys
from fractions import Fraction as Fr

random.seed(20261126)


# ---------------------------------------------------------------- p-adic tools
def val(x, p):
    x = Fr(x)
    assert x != 0
    n, d, v = x.numerator, x.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def unit_res(x, p):
    """Residue mod p of the unit part of x."""
    x = Fr(x)
    v = val(x, p)
    u = x / Fr(p) ** v
    return (u.numerator * pow(u.denominator, -1, p)) % p


def ell(a, p):
    """Quadratic residue character of a nonzero residue a mod p."""
    a %= p
    assert a != 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def hilbert(a, b, p):
    """Quadratic Hilbert symbol (a,b)_2 of Q_p, p odd (eq. (3.1))."""
    m, n = val(a, p), val(b, p)
    s = ell(-1, p) ** ((m * n) % 2)
    s *= ell(unit_res(a, p), p) ** (n % 2)
    s *= ell(unit_res(b, p), p) ** (m % 2)
    return s


# ---------------------------------------------------------------- matrices
def mul(g, h):
    (a, b), (c, d) = g
    (e, f), (i, j) = h
    return ((a * e + b * i, a * f + b * j), (c * e + d * i, c * f + d * j))


def det(g):
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


def inv(g):
    (a, b), (c, d) = g
    D = det(g)
    return ((d / D, -b / D), (-c / D, a / D))


def diag(a, d):
    return ((Fr(a), Fr(0)), (Fr(0), Fr(d)))


def n_up(t):
    return ((Fr(1), Fr(t)), (Fr(0), Fr(1)))


def n_lo(c):
    return ((Fr(1), Fr(0)), (Fr(c), Fr(1)))


def h(u):
    return diag(u, 1 / Fr(u))


def w(t):
    t = Fr(t)
    return ((Fr(0), t), (-1 / t, Fr(0)))


def x_of(g):
    return g[1][0] if g[1][0] != 0 else g[1][1]


def beta(g, k, p):
    """Kubota cocycle on SL_2(Q_p) (eq. (3.2))."""
    gk = mul(g, k)
    return hilbert(x_of(gk) / x_of(g), x_of(gk) / x_of(k), p)


def cmul(G, K, p):
    """Multiplication in the cover: G = (g, zeta)."""
    return (mul(G[0], K[0]), G[1] * K[1] * beta(G[0], K[0], p))


def cinv(G, p):
    gi = inv(G[0])
    return (gi, G[1] * beta(G[0], gi, p))


# -- extension to GL_2 (eq. (3.4))
def a_of(g):
    return diag(1, 1 / det(g))


def v_fn(u, k, p):
    return 1 if k[1][0] != 0 else hilbert(u, k[1][1], p)


def beta_ext(g, k, p):
    pg, pk = mul(a_of(g), g), mul(a_of(k), k)
    ak = a_of(k)
    conj = mul(mul(ak, pg), inv(ak))          # (a(g)g)^{a(k)^{-1}}
    return beta(conj, pk, p) * v_fn(det(k), pg, p)


def emul(G, K, p):
    return (mul(G[0], K[0]), G[1] * K[1] * beta_ext(G[0], K[0], p))


def einv(G, p):
    gi = inv(G[0])
    return (gi, G[1] * beta_ext(G[0], gi, p))


# ---------------------------------------------------------------- sampling
def rand_unit(p):
    while True:
        x = Fr(random.randint(1, 3 * p * p), random.randint(1, 3 * p * p))
        if val(x, p) == 0:
            return x


def rand_int(p):
    """Random element of Z_p intersected with Q (possibly zero)."""
    while True:
        x = Fr(random.randint(-2 * p * p, 2 * p * p), random.randint(1, 2 * p))
        if x == 0 or val(x, p) >= 0:
            return x


def rand_F(p):
    return Fr(random.randint(-40, 40), random.randint(1, 40)) * Fr(p) ** random.randint(-2, 2)


def rand_sl2(p):
    g = diag(1, 1)
    for _ in range(4):
        g = mul(g, n_up(rand_F(p)))
        g = mul(g, n_lo(rand_F(p)))
    return g


def rand_K0(p):
    g = diag(1, 1)
    for _ in range(3):
        g = mul(g, n_up(rand_int(p)))
        g = mul(g, n_lo(rand_int(p)))
    if random.random() < 0.5:
        g = mul(g, h(rand_unit(p)))
    return g


def rand_iwahori(p):
    """k in I = K_0 cap K_1: integral, det 1, upper right entry in pZ_p."""
    k = mul(n_lo(rand_int(p)), mul(h(rand_unit(p)), n_up(p * rand_int(p))))
    k = mul(k, n_lo(rand_int(p)))
    k = mul(k, n_up(p * rand_int(p)))
    assert val(k[0][0], p) == 0 and (k[0][1] == 0 or val(k[0][1], p) >= 1)
    return k


def r0(k, p):
    """Kubota splitting over K_0 (eq. (3.3))."""
    c, d = k[1]
    if c != 0 and d != 0 and val(c, p) >= 1:
        return hilbert(c, d, p)
    return 1


def s0(k, p):
    return (k, r0(k, p))


def unipotent_word_K0(k, p):
    """Write k in K_0 as a word in elementary unipotents with entries in Z_p."""
    (a, b), (c, d) = k
    if c != 0 and val(c, p) == 0:
        # k = n_up(x) n_lo(c) n_up(y)
        return [("u", (a - 1) / c), ("l", c), ("u", (d - 1) / c)]
    # c is not a unit, so a is a unit: k = n_lo(c/a) h(a) n_up(b/a)
    word = [("l", c / a)]
    # h(a) = w(a) w(-1),  w(t) = n_up(t) n_lo(-1/t) n_up(t)
    for t in (a, Fr(-1)):
        word += [("u", t), ("l", -1 / t), ("u", t)]
    word.append(("u", b / a))
    return word


def s1_by_unipotents(k, p):
    """s_1(k) for k in K_1 = D K_0 D^{-1}: conjugate a unipotent word by D and
    multiply the lifts (n,1) (Lemma 3.5)."""
    D = diag(p, 1)
    k0 = mul(mul(inv(D), k), D)
    out = (diag(1, 1), 1)
    for kind, t in unipotent_word_K0(k0, p):
        # D n_up(t) D^{-1} = n_up(p t),  D n_lo(c) D^{-1} = n_lo(c/p)
        m = n_up(p * t) if kind == "u" else n_lo(t / p)
        out = cmul(out, (m, 1), p)
    assert out[0] == k
    return out


def s1_by_conjugation(k, p):
    """s_1(k) = D~ s_0(D^{-1} k D) D~^{-1} in the cover of GL_2 (eq. (3.5))."""
    D = diag(p, 1)
    Dt = (D, 1)
    k0 = mul(mul(inv(D), k), D)
    out = emul(emul(Dt, s0(k0, p), p), einv(Dt, p), p)
    assert out[0] == k
    return out


# ---------------------------------------------------------------- the checks
def check_cover(p, N=300):
    for _ in range(N):
        g1, g2, g3 = rand_sl2(p), rand_sl2(p), rand_sl2(p)
        assert beta(g1, g2, p) * beta(mul(g1, g2), g3, p) == \
            beta(g1, mul(g2, g3), p) * beta(g2, g3, p), "cocycle"
    for _ in range(N):
        s, t = rand_F(p), rand_F(p)
        assert beta(n_up(s), n_up(t), p) == 1
        if s != 0 and t != 0 and s + t != 0:
            assert beta(n_lo(s), n_lo(t), p) == 1
    for _ in range(N):
        k1, k2 = rand_K0(p), rand_K0(p)
        assert r0(k1, p) * r0(k2, p) * beta(k1, k2, p) == r0(mul(k1, k2), p), "r0"
    for _ in range(N):
        t, t2 = rand_F(p), rand_F(p)
        if t == 0 or t2 == 0:
            continue
        wt = cmul(cmul((n_up(t), 1), (n_lo(-1 / t), 1), p), (n_up(t), 1), p)
        assert wt == (w(t), 1)
        wt2 = (w(t2), 1)
        prod = cmul(wt, cinv(wt2, p), p)
        assert prod == (h(t / t2), hilbert(-t2, t, p)), "Lemma 3.6"
    print("  p=%d: cocycle, unipotent triviality, r_0, Weyl/torus lifts  OK" % p)


def rand_gl2(p):
    g = rand_sl2(p)
    return mul(diag(rand_F(p) or 1, rand_F(p) or 1), g)


def check_extension(p, N=300):
    for _ in range(N):
        g1, g2, g3 = rand_gl2(p), rand_gl2(p), rand_gl2(p)
        assert beta_ext(g1, g2, p) * beta_ext(mul(g1, g2), g3, p) == \
            beta_ext(g1, mul(g2, g3), p) * beta_ext(g2, g3, p), "ext cocycle"
        s1_, s2_ = rand_sl2(p), rand_sl2(p)
        assert beta_ext(s1_, s2_, p) == beta(s1_, s2_, p)
    print("  p=%d: extended cocycle on GL_2, restriction to SL_2          OK" % p)


def check_edge(p, N=300):
    D = diag(p, 1)
    signs = set()
    for _ in range(N):
        k = rand_iwahori(p)
        A = s1_by_unipotents(k, p)
        B = s1_by_conjugation(k, p)
        assert A == B, "two computations of s_1 disagree"
        ratio = A[1] * r0(k, p)
        assert ratio == ell(unit_res(k[0][0], p), p), "edge discrepancy"
        signs.add(ratio)
    assert signs == {1, -1}
    # multiplicativity of s_1 on K_1
    for _ in range(N):
        k1 = mul(mul(D, rand_K0(p)), inv(D))
        k2 = mul(mul(D, rand_K0(p)), inv(D))
        A1, A2 = s1_by_unipotents(k1, p), s1_by_unipotents(k2, p)
        assert cmul(A1, A2, p) == s1_by_unipotents(mul(k1, k2), p)
        assert A1 == s1_by_conjugation(k1, p)
    # -I
    mI = diag(-1, -1)
    assert s1_by_unipotents(mI, p)[1] * r0(mI, p) == ell(-1, p)
    print("  p=%d: edge discrepancy ell(a) on I, s_1 homomorphic, -I       OK" % p)


def check_diag_conj(p, N=300):
    for _ in range(N):
        u = rand_F(p)
        if u == 0:
            continue
        g = rand_sl2(p)
        H = (h(u), 1)
        out = cmul(cmul(H, (g, 1), p), cinv(H, p), p)
        assert out[1] == 1, "diagonal conjugation"
    for _ in range(N):
        r1, r2 = rand_F(p), rand_F(p)
        if r1 == 0 or r2 == 0:
            continue
        g = rand_sl2(p)
        if random.random() < 0.3:
            g = mul(h(rand_F(p) or 1), n_up(rand_F(p)))
        R = (diag(r1, r2), 1)
        out = emul(emul(R, (g, 1), p), einv(R, p), p)
        assert out[1] == v_fn(r1 * r2, g, p), "Prop. 7.1(b)"
    D = diag(p, 1)
    for _ in range(N):
        k0 = rand_K0(p)
        k = mul(mul(D, k0), inv(D))
        assert s1_by_unipotents(k, p)[1] == r0(k0, p) * v_fn(Fr(p), k0, p), "r_1"
    print("  p=%d: diagonal conjugation in SL_2 and GL_2, formula for r_1  OK" % p)


def sphere(q, d):
    return 1 if d == 0 else (q + 1) * q ** (d - 1)


def ordinary(q, r, parity):
    """Ordinary character divided by theta(z); parity = (j - i) mod 2."""
    total = 0
    for d in range(r + 1):
        if d % 2 == parity:
            total += sphere(q, d) * ((q - 1) if d < r else -1)
    return total


def check_formulas():
    for q in (3, 5, 7, 9, 11, 13, 25, 27):
        for r in range(1, 9):
            for parity in (0, 1):
                assert ordinary(q, r, parity) == (-1) ** (r + 1 + parity) * q ** r - 1
            assert ordinary(q, r, 0) + ordinary(q, r, 1) == -2
    # Tables of Section 6: q = 7, theta(-1) = -1, ell(-1) = -1
    q, th, l = 7, -1, -1
    rows = {1: ((6, -8), (-6, 8), (-6, -8), -14),
            2: ((-50, 48), (50, -48), (50, 48), 98),
            3: ((342, -344), (-342, 344), (-342, -344), -686)}
    for r, (near1, ordm, genm, tot) in rows.items():
        o = (ordinary(q, r, 0), ordinary(q, r, 1))
        assert o == near1
        assert (th * o[0], th * o[1]) == ordm
        g = (th * o[0], l * th * o[1])
        assert g == genm and sum(g) == tot == 2 * (-1) ** (r + 1) * th * q ** r
        assert g[0] + l * g[1] == -2 * th
    q, th = 5, -1
    assert (th * ordinary(q, 1, 0), th * ordinary(q, 1, 1)) == (-4, 6)
    assert (th * ordinary(q, 2, 0), th * ordinary(q, 2, 1)) == (26, -24)
    print("  closed formulas, packet sums and the Q_7, Q_5 tables            OK")


# -- fixed balls by lattice computation over Z/p^N
def check_fixed_ball(p, eps, rmax=3):
    """t_r = (1 + p^r sqrt(eps))/(1 - p^r sqrt(eps)) acting on Z_p + Z_p sqrt(eps).
    A vertex at distance d from v_0 is the lattice Z_p e + p^d Z_p^2 for a
    primitive vector e modulo p^d.  It is fixed iff t e is in the lattice."""
    assert ell(eps, p) == -1
    for r in range(1, rmax + 1):
        P = Fr(p) ** r
        nrm = 1 - P * P * eps
        a, b = (1 + P * P * eps) / nrm, 2 * P / nrm          # t = a + b sqrt(eps)
        assert a * a - eps * b * b == 1
        t = ((a, b * eps), (b, a))                            # columns: t*1, t*sqrt(eps)
        for d in range(0, r + 3):
            M = p ** d
            fixed = moved = 0
            reps = [(1, y) for y in range(M)] + [(x * p, 1) for x in range(M // p)] if d > 0 else [(1, 0)]
            for e in reps:
                te = (t[0][0] * e[0] + t[0][1] * e[1], t[1][0] * e[0] + t[1][1] * e[1])
                # te in Z_p e + p^d Z_p^2  iff  det(e, te) = 0 mod p^d
                dt = e[0] * te[1] - e[1] * te[0]
                ok = (dt == 0) or val(dt, p) >= d
                fixed += ok
                moved += (not ok)
            assert len(reps) == sphere(p, d)
            if d <= r:
                assert moved == 0, (p, r, d)
            else:
                assert fixed == 0, (p, r, d)
    print("  p=%d: fixed set of t_r is the ball of radius r (r <= %d)        OK" % (p, rmax))


def main():
    print("Twofold metaplectic cover of SL_2(Q_p): exact checks")
    for p in (3, 5, 7, 11):
        check_cover(p)
        check_extension(p)
        check_edge(p)
        check_diag_conj(p)
    check_formulas()
    check_fixed_ball(7, 3)
    check_fixed_ball(5, 2)
    check_fixed_ball(3, 2, rmax=3)
    print("All checks passed.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print("CHECK FAILED:", exc)
        sys.exit(1)

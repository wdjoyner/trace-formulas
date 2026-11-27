#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""
tame_cover_check.py

Exact checks for "Characters of supercuspidal representations of tame
metaplectic covers of SL_2(F): a Bruhat-Tits tree approach"
(character_relations_tame_covers.tex, Draft 1).

Everything is computed over F = Q_p with rational matrix entries and exact
arithmetic (fractions.Fraction).  The degree n of the cover divides p - 1.
The group mu_n is written additively as Z/n: the class e stands for the
root of unity zeta^e, where zeta = g^((p-1)/n) for a fixed primitive root g
modulo p.  The n-th Hilbert symbol of Q_p is evaluated by the tame formula,
which is exact for rational arguments because p does not divide n.

The script checks the following statements of the paper.  These are
consistency checks on random samples.  The proofs in the paper do not
depend on them.

 1. Symbol identities (H1)-(H4) for the n-th Hilbert symbol        (Section 6)
 2. The Kubota function beta is a 2-cocycle on SL_2(Q_p)           (eq. (6.3))
 3. beta is trivial on upper and on lower unipotent pairs          (Lemma 6.2)
 4. The lifted Weyl and torus elements                             (Lemma 6.3)
 5. The formula r_0 for the splitting over K_0 = SL_2(Z_p)         (Prop. 6.4)
 6. Edge character s_1(k) = omega(a) s_0(k) on the Iwahori subgroup,
    with s_1 computed from unipotent generators; s_1 is
    multiplicative on K_1                                          (Prop. 6.6)
 7. The central sign: s_1(-I) = s_0(-I) iff (p-1)/n is even        (Cor. 6.7)
 8. Commutators of lifted diagonal elements and the lifts of h(u)
    along the standard apartment                                   (Prop. 6.10)
 9. Sphere sums, closed formulas and the tables                    (Thm. 5.6,
    Cor. 5.9, Section 8)
10. Fixed balls of t_r in the tree over Q_p, by listing lattices   (Prop. 5.1)
11. The power map on the finite nonsplit torus                     (Section 7)

Statement numbers refer to Draft 1 (November 27, 2026).
"""
import random
import sys
from fractions import Fraction as Fr
from math import gcd

random.seed(20261127)

PAIRS = [(3, 2), (5, 2), (5, 4), (7, 2), (7, 3), (7, 6), (11, 2), (11, 5),
         (11, 10), (13, 2), (13, 3), (13, 4), (13, 6), (13, 12)]


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
    u = x / Fr(p) ** val(x, p)
    return (u.numerator * pow(u.denominator, -1, p)) % p


def primitive_root(p):
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in range(2, p) if (p - 1) % r == 0):
            return g
    raise ValueError(p)


class Cover:
    """The Kubota n-fold cover of SL_2(Q_p), n | p - 1, mu_n = Z/n."""

    def __init__(self, p, n):
        assert (p - 1) % n == 0
        self.p, self.n = p, n
        g = primitive_root(p)
        self.dlog = {pow(g, e, p): e for e in range(p - 1)}

    def omega(self, a):
        """n-th power residue character of a nonzero residue, in Z/n."""
        return self.dlog[a % self.p] % self.n

    def hilbert(self, a, b):
        """(a,b)_n = omega((-1)^{alpha beta} a^beta / b^alpha), eq. (6.2)."""
        p = self.p
        al, be = val(a, p), val(b, p)
        c = pow(-1, al * be) * pow(unit_res(a, p), be, p) * pow(unit_res(b, p), -al, p)
        return self.omega(c % p)

    def beta(self, g, k):
        """Kubota cocycle (eq. (6.3))."""
        gk = mul(g, k)
        return self.hilbert(x_of(gk) / x_of(g), x_of(gk) / x_of(k))

    def cmul(self, G, K):
        return (mul(G[0], K[0]), (G[1] + K[1] + self.beta(G[0], K[0])) % self.n)

    def cinv(self, G):
        gi = inv(G[0])
        return (gi, (-G[1] - self.beta(G[0], gi)) % self.n)

    def r0(self, k):
        """Splitting over K_0 (Prop. 6.4)."""
        c, d = k[1]
        if c != 0 and val(c, self.p) >= 1:
            return self.hilbert(c, d)
        return 0

    def s_by_unipotents(self, k, m):
        """The splitting of K_m = D^m K_0 D^{-m} at k, from a unipotent word."""
        p = self.p
        Dm = diag(Fr(p) ** m, 1)
        k0 = mul(mul(inv(Dm), k), Dm)
        out = (diag(1, 1), 0)
        for kind, t in unipotent_word_K0(k0, p):
            mat = n_up(Fr(p) ** m * t) if kind == "u" else n_lo(t / Fr(p) ** m)
            out = self.cmul(out, (mat, 0))
        assert out[0] == k
        return out


# ---------------------------------------------------------------- matrices
def mul(g, h):
    (a, b), (c, d) = g
    (e, f), (i, j) = h
    return ((a * e + b * i, a * f + b * j), (c * e + d * i, c * f + d * j))


def inv(g):
    (a, b), (c, d) = g
    D = a * d - b * c
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


def unipotent_word_K0(k, p):
    """Write k in K_0 as a word in elementary unipotents with entries in Z_p."""
    (a, b), (c, d) = k
    if c != 0 and val(c, p) == 0:
        return [("u", (a - 1) / c), ("l", c), ("u", (d - 1) / c)]
    word = [("l", c / a)]
    for t in (a, Fr(-1)):                 # h(a) = w(a) w(-1) = w(a) w(1)^{-1}
        word += [("u", t), ("l", -1 / t), ("u", t)]
    word.append(("u", b / a))
    return word


# ---------------------------------------------------------------- sampling
def rand_unit(p):
    while True:
        x = Fr(random.randint(1, 3 * p * p), random.randint(1, 3 * p * p))
        if val(x, p) == 0:
            return x


def rand_int(p):
    while True:
        x = Fr(random.randint(-2 * p * p, 2 * p * p), random.randint(1, 2 * p))
        if x == 0 or val(x, p) >= 0:
            return x


def rand_F(p):
    return Fr(random.randint(-40, 40), random.randint(1, 40)) * Fr(p) ** random.randint(-2, 2)


def rand_Fx(p):
    while True:
        x = rand_F(p)
        if x != 0:
            return x


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


# ---------------------------------------------------------------- the checks
def check_symbol(C, N=300):
    p, n = C.p, C.n
    H = C.hilbert
    for _ in range(N):
        a, b, c = rand_Fx(p), rand_Fx(p), rand_Fx(p)
        assert H(a * b, c) == (H(a, c) + H(b, c)) % n                 # (H1)
        assert H(a, b * c) == (H(a, b) + H(a, c)) % n
        assert H(a, -a) == 0                                          # (H2)
        if a != 1:
            assert H(a, 1 - a) == 0
        assert (H(a, b) + H(b, a)) % n == 0                           # (H3)
        u, v = rand_unit(p), rand_unit(p)
        assert H(u, v) == 0                                           # (H4)
        assert H(u, p) == C.omega(unit_res(u, p)) == H(u, p * v)
    assert {C.omega(a) for a in range(1, p)} == set(range(n))
    for a in range(1, p):                  # omega(a) = 0 iff a is an n-th power
        assert (C.omega(a) == 0) == any(pow(b, n, p) == a for b in range(1, p))


def check_cover(C, N=250):
    p, n = C.p, C.n
    for _ in range(N):
        g1, g2, g3 = rand_sl2(p), rand_sl2(p), rand_sl2(p)
        assert (C.beta(g1, g2) + C.beta(mul(g1, g2), g3)) % n == \
            (C.beta(g1, mul(g2, g3)) + C.beta(g2, g3)) % n, "cocycle"
    for _ in range(N):
        s, t = rand_F(p), rand_F(p)
        assert C.beta(n_up(s), n_up(t)) == 0
        if s != 0 and t != 0 and s + t != 0:
            assert C.beta(n_lo(s), n_lo(t)) == 0
    for _ in range(N):
        t, t2 = rand_Fx(p), rand_Fx(p)
        wt = C.cmul(C.cmul((n_up(t), 0), (n_lo(-1 / t), 0)), (n_up(t), 0))
        assert wt == (w(t), 0)
        assert C.cinv((w(t2), 0)) == (w(-t2), 0)
        prod = C.cmul(wt, C.cinv((w(t2), 0)))
        assert prod == (h(t / t2), C.hilbert(t, -t2)), "Lemma 6.3"
    for _ in range(N):
        k1, k2 = rand_K0(p), rand_K0(p)
        assert (C.r0(k1) + C.r0(k2) + C.beta(k1, k2)) % n == C.r0(mul(k1, k2)), "r0"
        assert C.s_by_unipotents(k1, 0) == (k1, C.r0(k1)), "r0 from unipotents"


def check_edge(C, N=250):
    p, n = C.p, C.n
    D = diag(p, 1)
    seen = set()
    for _ in range(N):
        k = rand_iwahori(p)
        ratio = (C.s_by_unipotents(k, 1)[1] - C.r0(k)) % n
        assert ratio == C.omega(unit_res(k[0][0], p)), "edge character"
        seen.add(ratio)
    assert seen == set(range(n)), "edge character has order n"
    for _ in range(N):
        k1 = mul(mul(D, rand_K0(p)), inv(D))
        k2 = mul(mul(D, rand_K0(p)), inv(D))
        A1, A2 = C.s_by_unipotents(k1, 1), C.s_by_unipotents(k2, 1)
        assert C.cmul(A1, A2) == C.s_by_unipotents(mul(k1, k2), 1)
    # the central sign
    mI = diag(-1, -1)
    eps = (C.s_by_unipotents(mI, 1)[1] - C.r0(mI)) % n
    assert eps == C.omega(-1)
    assert (2 * eps) % n == 0
    odd = ((p - 1) // n) % 2 == 1
    assert (eps != 0) == odd
    if odd:
        assert n % 2 == 0 and eps == n // 2
    return eps


def check_apartment(C, N=120):
    p, n = C.p, C.n
    for _ in range(N):
        a, b = rand_Fx(p), rand_Fx(p)
        A, B = (h(a), 0), (h(b), 0)
        comm = C.cmul(C.cmul(A, B), C.cinv(C.cmul(B, A)))
        assert comm == (diag(1, 1), (2 * C.hilbert(b, a)) % n), "commutator"
    for _ in range(N):
        u = rand_unit(p)
        om = C.omega(unit_res(u, p))
        base = C.s_by_unipotents(h(u), 0)
        assert base == (h(u), 0)
        for m in range(-3, 4):
            lift = C.s_by_unipotents(h(u), m)
            assert lift == (h(u), (m * om) % n), "apartment lifts"


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
            # recursion used in the proof of Theorem 5.6
            A = ordinary(q, r, r % 2)
            B = ordinary(q, r, (r + 1) % 2)
            assert ordinary(q, r + 1, r % 2) == A + q * sphere(q, r)
            assert ordinary(q, r + 1, (r + 1) % 2) == B - sphere(q, r + 1)
    # Table of Section 8: q = 7, theta of order eight, theta(-1) = -1
    q, th = 7, -1
    table = {1: (6, -8), 2: (-50, 48), 3: (342, -344)}
    for r, pair in table.items():
        o = (ordinary(q, r, 0), ordinary(q, r, 1))
        assert o == pair
        for eps in (1, -1):                     # eps = 1: n = 3;  eps = -1: n = 2, 6
            gen_plus = o                          # near +I the sign is trivial
            gen_minus = (th * o[0], eps * th * o[1])
            assert sum(gen_plus) == -2
            assert gen_minus[0] + eps * gen_minus[1] == -2 * th
            if eps == -1:
                assert sum(gen_minus) == 2 * (-1) ** (r + 1) * th * q ** r
        assert (th * o[0], -th * o[1]) == {1: (-6, -8), 2: (50, 48), 3: (-342, -344)}[r]
        assert sum((th * o[0], -th * o[1])) == {1: -14, 2: 98, 3: -686}[r]
    q, th = 5, -1
    assert (th * ordinary(q, 1, 0), th * ordinary(q, 1, 1)) == (-4, 6)
    assert (th * ordinary(q, 2, 0), th * ordinary(q, 2, 1)) == (26, -24)
    # fourfold cover over Q_5: eps = -1
    assert (th * ordinary(q, 1, 0), -th * ordinary(q, 1, 1)) == (-4, -6)
    assert (th * ordinary(q, 2, 0), -th * ordinary(q, 2, 1)) == (26, 24)


def check_fixed_ball(p, eps, rmax=3):
    """t_r = (1 + p^r sqrt(eps))/(1 - p^r sqrt(eps)) acting on Z_p + Z_p sqrt(eps).
    A vertex at distance d from v_0 is the lattice Z_p e + p^d Z_p^2 for a
    primitive vector e modulo p^d.  It is fixed iff t e is in the lattice."""
    assert pow(eps, (p - 1) // 2, p) == p - 1
    for r in range(1, rmax + 1):
        P = Fr(p) ** r
        nrm = 1 - P * P * eps
        a, b = (1 + P * P * eps) / nrm, 2 * P / nrm
        assert a * a - eps * b * b == 1
        t = ((a, b * eps), (b, a))
        for d in range(0, r + 3):
            M = p ** d
            reps = [(1, y) for y in range(M)] + [(x * p, 1) for x in range(M // p)] if d > 0 else [(1, 0)]
            assert len(reps) == sphere(p, d)
            fixed = 0
            for e in reps:
                te = (t[0][0] * e[0] + t[0][1] * e[1], t[1][0] * e[0] + t[1][1] * e[1])
                dt = e[0] * te[1] - e[1] * te[0]
                fixed += (dt == 0) or val(dt, p) >= d
            assert fixed == (len(reps) if d <= r else 0), (p, r, d)


def check_power_map():
    for q in (3, 5, 7, 9, 11, 13, 25, 27):
        for n in range(2, q):
            if (q - 1) % n:
                continue
            kernel = gcd(n, q + 1)              # kernel of x -> x^n on Z/(q+1)
            assert kernel == (1 if n % 2 else 2)
            if n % 2:
                e = pow(n, -1, q + 1)
                assert e % 2 == 1 and (e * n) % (q + 1) == 1
    assert pow(3, -1, 8) == 3                   # Q_7, n = 3: theta^<3> = theta^3


def main():
    print("Tame n-fold covers of SL_2(Q_p): exact checks")
    print("  %3s %3s  %-22s %s" % ("p", "n", "s_1(-I) / s_0(-I)", "sign"))
    for p, n in PAIRS:
        C = Cover(p, n)
        check_symbol(C)
        check_cover(C)
        eps = check_edge(C)
        check_apartment(C)
        print("  %3d %3d  zeta^%-17d %+d" % (p, n, eps, 1 if eps == 0 else -1))
    print("  symbol identities, cocycle, unipotent and Weyl lifts, r_0,")
    print("  edge character, central sign, apartment lifts               OK")
    check_formulas()
    print("  closed formulas, recursion, packet sums and the tables       OK")
    check_fixed_ball(7, 3)
    check_fixed_ball(5, 2)
    check_fixed_ball(3, 2)
    print("  fixed set of t_r is the ball of radius r (p = 3, 5, 7)       OK")
    check_power_map()
    print("  power map on the finite nonsplit torus                       OK")
    print("All checks passed.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as exc:
        print("CHECK FAILED:", exc)
        sys.exit(1)

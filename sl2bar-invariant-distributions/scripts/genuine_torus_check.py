# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact checks for "A hitch-hiker's guide to genuine invariant
distributions on metaplectic covers of SL(2) over a p-adic field" (Draft 3).

Run: python3 genuine_torus_check.py   (a few seconds)

Model: F = Q_p with n | p - 1 (so mu_n lies in F and p does not divide 2n).
Elements of F^x are nonzero rationals.  The tame n-th power Hilbert symbol
is returned as an exponent k in Z/n (meaning zeta^k for a fixed primitive
n-th root of unity).  All checks are exact.  The identities checked below do
not depend on the sign convention chosen for the tame symbol.

Checks:
  1. The two expressions for the Kubota cocycle beta in Section 3.1 agree.
  2. beta is a 2-cocycle (associativity of the group law (3.2)).
  3. On the diagonal torus, beta(h(a), h(b)) = (b, a)_n, so the commutator
     of the lifts of h(a) and h(b) is (a, b)_n^(-2)   (Lemma 5.2(a)).
  4. h(a) is central in the covering torus iff a is a nu-th power, where
     nu = n (n odd) or n/2 (n even)   (Lemma 5.2(b)).
  5. The preimage of h(C), C = p^Z (O^x)^nu, is abelian, and C has index
     nu in F^x   (Lemma 5.1, Lemma 5.2(c)).
  6. u -> (u, 1) is a homomorphism on the upper and lower unipotent
     subgroups and on conjugates of them (Steinberg relation), Section 3.2.
  7. Bruhat identities  w0 u_x = h(1/x) u(-x) u^-(1/x)  and
     w0^(-1) u_x = h(-1/x) u(-x) u^-(1/x)   (Section 6.2).
  8. w0 has order 4 in SL(2)   (Section 3.2).
"""
from fractions import Fraction as Fr
import random
import sys


def val(x, p):
    x = Fr(x)
    num, den, v = x.numerator, x.denominator, 0
    while num % p == 0:
        num //= p
        v += 1
    while den % p == 0:
        den //= p
        v -= 1
    return v


def unit_residue(x, p):
    x = Fr(x)
    y = x / Fr(p) ** val(x, p)
    return (y.numerator * pow(y.denominator, -1, p)) % p


def primroot(p):
    primes = [q for q in range(2, p) if (p - 1) % q == 0
              and all(q % r for r in range(2, q))]
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in primes):
            return g


def make_dlog(p, g):
    table, x = {}, 1
    for k in range(p - 1):
        table[x] = k
        x = x * g % p
    return table


class Field:
    def __init__(self, p, n):
        assert (p - 1) % n == 0 and p % 2 == 1 and n % p != 0
        self.p, self.n = p, n
        self.nu = n if n % 2 else n // 2
        self.g = primroot(p)
        self.dlog = make_dlog(p, self.g)

    def hilb(self, a, b):
        """Tame symbol (a, b)_n as an exponent mod n."""
        p = self.p
        al, be = val(a, p), val(b, p)
        c = Fr(-1) ** (al * be) * Fr(a) ** be / Fr(b) ** al
        return self.dlog[unit_residue(c, p)] % self.n

    def is_power(self, a, m):
        """Is a an m-th power in F^x?  (p does not divide m.)"""
        return val(a, self.p) % m == 0 and \
            self.dlog[unit_residue(a, self.p)] % m == 0


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def xfun(A):
    return A[1][0] if A[1][0] != 0 else A[1][1]


def beta(F, A, B):
    """beta(g1,g2) = (x(g1g2)/x(g1), x(g1g2)/x(g2))_n."""
    C = mul(A, B)
    return F.hilb(Fr(xfun(C)) / xfun(A), Fr(xfun(C)) / xfun(B))


def beta_first_form(F, A, B):
    """beta(g1,g2) = (x1, x2)_n (-x1^{-1} x2, x(g1 g2))_n."""
    x1, x2, x3 = Fr(xfun(A)), Fr(xfun(B)), Fr(xfun(mul(A, B)))
    return (F.hilb(x1, x2) + F.hilb(-x2 / x1, x3)) % F.n


def gmul(F, X, Y):
    return (mul(X[0], Y[0]), (X[1] + Y[1] + beta(F, X[0], Y[0])) % F.n)


def h(t):
    t = Fr(t)
    return ((t, Fr(0)), (Fr(0), 1 / t))


def u(x):
    return ((Fr(1), Fr(x)), (Fr(0), Fr(1)))


def ul(y):
    return ((Fr(1), Fr(0)), (Fr(y), Fr(1)))


W0 = ((Fr(0), Fr(-1)), (Fr(1), Fr(0)))
W0INV = ((Fr(0), Fr(1)), (Fr(-1), Fr(0)))
I2 = ((Fr(1), Fr(0)), (Fr(0), Fr(1)))


def rand_unit(p, rng):
    while True:
        a, b = rng.randint(1, 40 * p), rng.randint(1, 40 * p)
        if a % p and b % p:
            return Fr(rng.choice([1, -1]) * a, b)


def rand_elt(p, rng):
    return rand_unit(p, rng) * Fr(p) ** rng.randint(-3, 3)


def rand_sl2(p, rng):
    while True:
        a, b, c = rand_elt(p, rng), rand_elt(p, rng), rand_elt(p, rng)
        if rng.random() < 0.25:
            c = Fr(0)
            return ((a, b), (Fr(0), 1 / a))
        if a != 0:
            return ((a, b), (c, (1 + b * c) / a))


FAILED = []


def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        FAILED.append(name)


def run(p, n, trials=300, seed=1):
    F = Field(p, n)
    rng = random.Random(seed + 1000 * p + n)
    tag = "(p=%d, n=%d, nu=%d)" % (p, n, F.nu)

    # 1. two forms of beta
    ok = True
    for _ in range(trials):
        A, B = rand_sl2(p, rng), rand_sl2(p, rng)
        if beta(F, A, B) != beta_first_form(F, A, B):
            ok = False
            break
    check("1. two expressions for beta agree " + tag, ok)

    # 2. cocycle identity
    ok = True
    for _ in range(trials):
        A, B, C = (rand_sl2(p, rng) for _ in range(3))
        lhs = (beta(F, A, B) + beta(F, mul(A, B), C)) % n
        rhs = (beta(F, B, C) + beta(F, A, mul(B, C))) % n
        if lhs != rhs:
            ok = False
            break
    check("2. beta is a 2-cocycle " + tag, ok)

    # 3. torus product and commutator
    ok3a, ok3b = True, True
    for _ in range(trials):
        a, b = rand_elt(p, rng), rand_elt(p, rng)
        if beta(F, h(a), h(b)) != F.hilb(b, a):
            ok3a = False
        X, Y = (h(a), 0), (h(b), 0)
        XY, YX = gmul(F, X, Y), gmul(F, Y, X)
        # XY = (1, c) YX with c = XY[1] - YX[1]
        if XY[0] != YX[0] or (XY[1] - YX[1]) % n != (-2 * F.hilb(a, b)) % n:
            ok3b = False
    check("3a. beta(h(a),h(b)) = (b,a)_n " + tag, ok3a)
    check("3b. commutator of lifts = (a,b)_n^(-2) " + tag, ok3b)

    # 4. center of the covering torus is the preimage of A^nu
    gens = [Fr(p), Fr(F.g)]  # p and a unit generating residues
    ok = True
    for k in range(-2 * F.nu, 2 * F.nu + 1):
        for r in range(1, p):
            a = Fr(p) ** k * r
            central = all((2 * F.hilb(a, b)) % n == 0 for b in gens)
            if central != F.is_power(a, F.nu):
                ok = False
    check("4. h(a) central iff a in F^(x nu) " + tag, ok)

    # 5. C = p^Z (O^x)^nu : index nu, abelian preimage
    def in_C(a):
        return F.dlog[unit_residue(a, p)] % F.nu == 0
    ok = True
    for _ in range(trials):
        a = Fr(p) ** rng.randint(-3, 3) * rand_unit(p, rng) ** F.nu
        b = Fr(p) ** rng.randint(-3, 3) * rand_unit(p, rng) ** F.nu
        if not (in_C(a) and in_C(b)) or (2 * F.hilb(a, b)) % n != 0:
            ok = False
    classes = {F.dlog[r] % F.nu for r in range(1, p)}
    check("5. preimage of h(C) abelian, [F^x : C] = nu " + tag,
          ok and len(classes) == F.nu)

    # 6. unipotent sections: beta vanishes on N x N for the upper and
    #    lower unipotent subgroups and for random conjugates of N0
    def inv(A):
        return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
    ok = True
    for _ in range(trials):
        a, b = rand_elt(p, rng), rand_elt(p, rng)
        G = rand_sl2(p, rng)
        A = mul(mul(G, u(a)), inv(G))
        B = mul(mul(G, u(b)), inv(G))
        if beta(F, u(a), u(b)) or beta(F, ul(a), ul(b)) or beta(F, A, B):
            ok = False
            break
    check("6. beta trivial on unipotent radicals (N0, lower, conjugates) "
          + tag, ok)


def run_matrix_checks():
    rng = random.Random(7)
    ok = True
    for _ in range(200):
        x = Fr(rng.randint(1, 999), rng.randint(1, 999)) * rng.choice([1, -1])
        if mul(W0, u(x)) != mul(mul(h(1 / x), u(-x)), ul(1 / x)):
            ok = False
        if mul(W0INV, u(x)) != mul(mul(h(-1 / x), u(-x)), ul(1 / x)):
            ok = False
    check("7. Bruhat identities for w0 u_x and w0^-1 u_x", ok)
    w2 = mul(W0, W0)
    check("8. w0 has order 4", w2 != I2 and mul(w2, w2) == I2)


if __name__ == "__main__":
    for (p, n) in [(7, 3), (13, 3), (13, 4), (13, 6), (17, 4), (19, 9)]:
        run(p, n)
    run_matrix_checks()
    print()
    print("%d check(s) failed" % len(FAILED))
    sys.exit(1 if FAILED else 0)

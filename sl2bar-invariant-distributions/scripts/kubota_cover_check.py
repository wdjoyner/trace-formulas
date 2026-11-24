# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact checks for Draft 2 of the preservation-first revision of
"A hitch-hiker's guide to genuine invariant distributions on metaplectic
covers of SL(2) over a p-adic field" (tame case).

Run:  python3 kubota_cover_check.py        (about ten seconds)

Model.  F = Q_p with n | p-1, so mu_n lies in F and p does not divide n.
Elements of F^x are nonzero rationals.  The tame n-th power Hilbert symbol
(a,b)_n is stored as an exponent in Z/n (it means zeta^k for a fixed
primitive n-th root of unity zeta).  Elements of the cover are pairs
(g, k) with g in SL(2,Q) and k in Z/n, multiplied by Kubota's cocycle.
All arithmetic is exact.

Each check is tied to a numbered statement of the paper:
  C1  Lemma 2.1      beta is a 2-cocycle (random triples).
  C2  Lemma 2.2/2.3  beta(h(a),h(b)) = (b,a)_n; inverse formula;
                     commutator of lifts = (a,b)_n^(-2)  [up to the sign
                     convention of the symbol the radical is the same].
  C3  Prop. 2.7      h(a) lifts to the center of the covering torus iff
                     a is a nu-th power; index nu^2.
  C4  Lemma 2.8/2.10  C = p^Z (O^x)^nu is isotropic of index nu
                     (hence Lagrangian, since nu^2 = nu * nu).
  C5  Lemma 2.12      w~ (h(b),1) w~^{-1} = (h(1/b),1) for w~ = (w0,1).
  C6  Lemma 2.12      kappa(z) = w~ z w~^{-1} z equals (1,(-1,a)_n) for
                     z = (h(a),1).
  C7  Lemma 2.13      a -> (h(a^n),1) is a homomorphism;
                     (h(a),1)^n = (h(a^n), (-1,a)_2^[n even]).
  C8  Prop. 3.3      number of Weyl-fixed genuine central characters is 4,
                     and chi_sigma is quadratic (n odd, all four quadratic
                     characters occur) or trivial (n even).
  C9  Lemma 2.3(b)   Kubota's section k -> (k, kappa_K(k)) splits the cover
                     over SL(2,Z_p); kappa_K = 1 on upper triangular k.
  C10 Thm 3.12        ingredients of the Gindikin-Karpelevich computation:
                     (w0^-1,1)(u(x),1) = (u(y),1)(h(-1/x),1)(k,1) with
                     kappa_K(k) = 1, for |x| > 1; and the average of
                     (u,p)_n^(-m) over residues u vanishes unless n | m.
"""
from fractions import Fraction as Fr
from itertools import product
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


class Field:
    def __init__(self, p, n):
        assert (p - 1) % n == 0 and n % p != 0
        self.p, self.n = p, n
        self.nu = n if n % 2 else n // 2
        self.g = primroot(p)
        self.dlog, x = {}, 1
        for k in range(p - 1):
            self.dlog[x] = k
            x = x * self.g % p

    def hilb(self, a, b, m=None):
        """Tame symbol (a,b)_m as an exponent mod m (default m = n)."""
        m = m or self.n
        p = self.p
        al, be = val(a, p), val(b, p)
        c = Fr(-1) ** (al * be) * Fr(a) ** be / Fr(b) ** al
        return (self.dlog[unit_residue(c, p)] * ((p - 1) // m)) % (p - 1) // ((p - 1) // m) % m

    def is_power(self, a, m):
        return val(a, self.p) % m == 0 and self.dlog[unit_residue(a, self.p)] % m == 0


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def xfun(A):
    return A[1][0] if A[1][0] != 0 else A[1][1]


def beta(F, A, B):
    C = mul(A, B)
    return F.hilb(Fr(xfun(C)) / xfun(A), Fr(xfun(C)) / xfun(B))


def gmul(F, X, Y):
    return (mul(X[0], Y[0]), (X[1] + Y[1] + beta(F, X[0], Y[0])) % F.n)


def ginv(F, X):
    A = X[0]
    Ai = ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))
    return (Ai, (-X[1] - beta(F, A, Ai)) % F.n)


def h(t):
    t = Fr(t)
    return ((t, Fr(0)), (Fr(0), 1 / t))


def u(x):
    return ((Fr(1), Fr(x)), (Fr(0), Fr(1)))


W0 = ((Fr(0), Fr(-1)), (Fr(1), Fr(0)))
W0INV = ((Fr(0), Fr(1)), (Fr(-1), Fr(0)))
I2 = ((Fr(1), Fr(0)), (Fr(0), Fr(1)))


def rand_elt(p, rng):
    a = Fr(rng.choice([1, -1]) * rng.randint(1, 30 * p), rng.randint(1, 30 * p))
    return a * Fr(p) ** rng.randint(-3, 3)


def rand_sl2(p, rng):
    while True:
        a, b, c = rand_elt(p, rng), rand_elt(p, rng), rng.choice([Fr(0), rand_elt(p, rng)])
        if a != 0:
            return ((a, b), (c, (1 + b * c) / a))


def kappaK(F, k):
    c, d = k[1][0], k[1][1]
    if c != 0 and val(c, F.p) > 0:
        return F.hilb(c, d)
    return 0


def rand_K(p, rng):
    def zp():
        return Fr(rng.randint(-20 * p, 20 * p), rng.choice([1, 2, 3, 4, 6]) if p > 6 else 1)
    while True:
        a, b, c = zp(), zp(), zp() * rng.choice([1, p, p * p, 0])
        if a != 0 and val(a, p) == 0 and val(b, p) >= 0 if b != 0 else a != 0 and val(a, p) == 0:
            d = (1 + b * c) / a
            if c == 0 or val(c, p) >= 0:
                return ((a, b), (c, d))


def reps(F):
    """Representatives of F^x / F^{x n}: p^i g^j, 0 <= i,j < n."""
    return [Fr(F.p) ** i * Fr(F.g) ** j for i in range(F.n) for j in range(F.n)]


def check(p, n, rng):
    F = Field(p, n)
    nu = F.nu
    out = {}
    # C1
    ok = True
    for _ in range(300):
        A, B, C = rand_sl2(p, rng), rand_sl2(p, rng), rand_sl2(p, rng)
        ok &= (beta(F, A, B) + beta(F, mul(A, B), C)) % n == (beta(F, B, C) + beta(F, A, mul(B, C))) % n
    out["C1 cocycle"] = ok
    # C2
    ok = True
    for _ in range(300):
        a, b = rand_elt(p, rng), rand_elt(p, rng)
        ok &= beta(F, h(a), h(b)) == F.hilb(b, a)
        X, Y = (h(a), 0), (h(b), 0)
        comm = gmul(F, gmul(F, X, Y), gmul(F, ginv(F, X), ginv(F, Y)))
        ok &= comm == (I2, (-2 * F.hilb(a, b)) % n)
        ok &= ginv(F, (h(a), 0)) == (h(1 / a), F.hilb(a, a))
    out["C2 torus cocycle, inverse, commutator"] = ok
    # C3
    R = reps(F)
    central = [a for a in R if all((2 * F.hilb(a, b)) % n == 0 for b in R)]
    out["C3 center = nu-th powers, index nu^2"] = (
        all(F.is_power(a, nu) for a in central)
        and all((a in central) == F.is_power(a, nu) for a in R)
        and len(R) // len(central) == nu * nu)
    # C4
    Cset = [a for a in R if F.dlog[unit_residue(a, p)] % nu == 0]
    out["C4 C isotropic of index nu"] = (
        all((2 * F.hilb(a, b)) % n == 0 for a in Cset for b in Cset)
        and len(R) // len(Cset) == nu)
    # C5, C6
    ok5 = ok6 = True
    wt, wti = (W0, 0), ginv(F, (W0, 0))
    for _ in range(300):
        b = rand_elt(p, rng)
        c = gmul(F, gmul(F, wt, (h(b), 0)), wti)
        ok5 &= c == (h(1 / b), 0)
        ok6 &= gmul(F, c, (h(b), 0)) == (I2, F.hilb(-1, b))
    out["C5 Weyl conjugation of trivial lifts"] = ok5
    out["C6 kappa(h(a),1) = (-1,a)_n"] = ok6
    # C7
    ok = True
    for _ in range(100):
        a, b = rand_elt(p, rng), rand_elt(p, rng)
        ok &= gmul(F, (h(a ** n), 0), (h(b ** n), 0)) == (h((a * b) ** n), 0)
        X = (I2, 0)
        for _k in range(n):
            X = gmul(F, X, (h(a), 0))
        sign = 0
        if n % 2 == 0:
            sign = (F.hilb(-1, a, 2) * (n // 2)) % n
        ok &= X == (h(a ** n), sign)
    out["C7 n-th power map"] = ok
    # C8: Weyl-fixed genuine characters of the center, modulo principal units.
    # Center modulo U_1 is generated by mu_n, t = (h(p^nu),1), r = (h(g^nu),1).
    # A genuine character omega (trivial on lifts of U_1) is given by
    # x = omega(t) (any nonzero complex number) and y = omega(r).
    # Weyl-fixed  <=>  omega^2 = kappa on the center.  Values are roots of
    # unity; store exponents modulo L.
    m = (p - 1) // nu                      # order of g^nu modulo U_1
    L = 2 * n * (p - 1)
    e = lambda k: (k * (L // n)) % L       # zeta^k as exponent mod L
    # relation: r^m = (h(g^(p-1)), c_r) with g^(p-1) in U_1
    X = (I2, 0)
    for _k in range(m):
        X = gmul(F, X, (h(Fr(F.g) ** nu), 0))
    assert unit_residue(X[0][0][0], p) == 1 and val(X[0][0][0], p) == 0
    c_r = X[1]
    kap_t = F.hilb(-1, Fr(p) ** nu)
    kap_r = F.hilb(-1, Fr(F.g) ** nu)
    ys = [y for y in range(L) if (2 * y) % L == e(kap_r) and (m * y) % L == e(c_r)]
    xs = [x for x in range(L) if (2 * x) % L == e(kap_t)]
    fixed = [(x, y) for x in xs for y in ys]
    # chi_sigma(a) = omega(h(a^n),1) on generators a = p and a = g
    def omega_of_power(a, x, y):
        # (h(a^n),1) = t^i r^j * zeta^c  with a^n = p^(nu i) g^(nu j) * unit in U_1
        aa = Fr(a) ** n
        i = val(aa, p) // nu
        j = F.dlog[unit_residue(aa, p)] // nu
        Y = (I2, 0)
        for _k in range(i):
            Y = gmul(F, Y, (h(Fr(p) ** nu), 0))
        for _k in range(j):
            Y = gmul(F, Y, (h(Fr(F.g) ** nu), 0))
        return (i * x + j * y - e(Y[1])) % L      # omega(h(a^n),1), up to U_1
    chis = sorted({(omega_of_power(p, x, y), omega_of_power(F.g, x, y)) for x, y in fixed})
    if n % 2:
        good = chis == sorted(product([0, L // 2], repeat=2))
    else:
        good = chis == [(0, 0)]
    out["C8 four Weyl-fixed classes; chi_sigma quadratic (n odd) / trivial (n even)"] = (
        len(fixed) == 4 and good)
    # C9
    ok = True
    for _ in range(300):
        A, B = rand_K(p, rng), rand_K(p, rng)
        ok &= kappaK(F, mul(A, B)) == (kappaK(F, A) + kappaK(F, B) + beta(F, A, B)) % n
    out["C9 Kubota splitting over SL(2,Z_p)"] = ok
    # C10
    ok = True
    for _ in range(200):
        x = rand_elt(p, rng)
        if val(x, p) >= 0:
            x = x / Fr(p) ** (val(x, p) + rng.randint(1, 3))
        t = -1 / x
        k = ((Fr(1), Fr(0)), (1 / x, Fr(1)))
        # w0^{-1} u(x) = u(y) h(t) k'  with k' = k * (upper unipotent in K);
        # compare in the cover using k'' = h(t)^{-1} u(y)^{-1} w0^{-1} u(x)
        lhs = gmul(F, (W0INV, 0), (u(x), 0))
        kk = mul(h(1 / t), lhs[0])
        # kk is lower row (1/x, 1) up to left upper-unipotent factor
        # solve u(y): top row of h(1/t)*lhs = (a,b); need u(-y) to make it in K
        a, b = kk[0]
        c, d = kk[1]
        assert c == 1 / x and d == 1
        # k' = u(-y') kk with entries integral: choose y' = b (then k' = [[a - b c, 0],[c,1]])
        kprime = mul(u(-b), kk)
        assert val(kprime[0][0], p) == 0 and kprime[0][1] == 0
        # y in F for the left factor: u(Y) h(t) k' = lhs  with Y = t^2 * b
        Yv = t * t * b
        rhs = gmul(F, gmul(F, (u(Yv), 0), (h(t), 0)), (kprime, kappaK(F, kprime)))
        ok &= rhs == lhs and kappaK(F, kprime) == 0
    for m_ in range(1, 3 * n + 1):
        tot = [0] * n
        for uu in range(1, p):
            tot[(-m_ * F.hilb(uu, p)) % n] += 1
        # u -> (u,p)_n^(-m) is a character of the residue units; its sum
        # vanishes exactly when it is nontrivial
        vanishes = any(tot[k] for k in range(1, n))
        ok &= vanishes == (m_ % n != 0)
        if m_ % n == 0:
            ok &= tot[0] == p - 1
    out["C10 Gindikin-Karpelevich ingredients"] = ok
    return out


def main():
    rng = random.Random(20261124)
    cases = [(7, 3), (13, 3), (11, 5), (5, 2), (7, 2), (5, 4), (13, 4), (13, 6), (7, 6), (17, 8), (29, 7)]
    bad = 0
    for p, n in cases:
        res = check(p, n, rng)
        for name, ok in res.items():
            print("p=%2d n=%d  %-78s %s" % (p, n, name, "ok" if ok else "FAIL"))
            bad += not ok
    print("\n%d failure(s)" % bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

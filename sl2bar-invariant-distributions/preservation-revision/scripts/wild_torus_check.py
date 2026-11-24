# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact checks of the wild examples in Draft 2 (Section 8).

Run:  python3 wild_torus_check.py

W1  F = Q_2, n = 2.  With the quadratic Hilbert symbol of Q_2, Kubota's
    beta is a 2-cocycle on SL(2,Q) (random triples); the covering torus is
    abelian; (-I,1)^2 = (I,-1), so the center of the double cover of
    SL(2,Q_2) is cyclic of order 4 (Lemma 2.3(e)).
W2  F = Q_3(omega), omega^2+omega+1 = 0, n = 3 (so nu = 3).  Counting cubes
    in (O/9)^x gives [O^x : O^{x3}] = 27, hence [F^x : F^{x3}] = 81, the
    genuine irreducible representations of the covering torus have
    dimension 9, and C_0 = pi^Z O^{x3} has index 27 (not Lagrangian).
W3  F = Q_2(i), n = 4 (so nu = 2).  Counting squares in (O/8)^x gives
    [O^x : O^{x2}] = 8, hence [F^x : F^{x2}] = 16, dimension 4, and
    C_0 = pi^Z O^{x2} has index 8 (not Lagrangian).
The index formula checked is [O^x : O^{xm}] = |mu_m(F)| * |m|_F^{-1}.
"""
from fractions import Fraction as Fr
import random
import sys


def v2(x):
    x = Fr(x); a, b, v = x.numerator, x.denominator, 0
    while a % 2 == 0: a //= 2; v += 1
    while b % 2 == 0: b //= 2; v -= 1
    return v


def hilb2(a, b):
    """Quadratic Hilbert symbol of Q_2 as an exponent mod 2."""
    al, be = v2(a), v2(b)
    u = Fr(a) / Fr(2) ** al
    w = Fr(b) / Fr(2) ** be
    u = (u.numerator * pow(u.denominator, -1, 8)) % 8
    w = (w.numerator * pow(w.denominator, -1, 8)) % 8
    eps = lambda t: ((t - 1) // 2) % 2
    om = lambda t: ((t * t - 1) // 8) % 2
    return (eps(u) * eps(w) + al * om(w) + be * om(u)) % 2


def mul(A, B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))


def xfun(A):
    return A[1][0] if A[1][0] != 0 else A[1][1]


def beta(A, B):
    C = mul(A, B)
    return hilb2(Fr(xfun(C)) / xfun(A), Fr(xfun(C)) / xfun(B))


def rand_elt(rng):
    return Fr(rng.choice([1, -1]) * rng.randint(1, 60), rng.randint(1, 60)) * Fr(2) ** rng.randint(-3, 3)


def rand_sl2(rng):
    while True:
        a, b, c = rand_elt(rng), rand_elt(rng), rng.choice([Fr(0), rand_elt(rng)])
        return ((a, b), (c, (1 + b * c) / a))


def w1():
    rng = random.Random(7)
    ok = True
    for _ in range(2000):
        A, B, C = rand_sl2(rng), rand_sl2(rng), rand_sl2(rng)
        ok &= (beta(A, B) + beta(mul(A, B), C)) % 2 == (beta(B, C) + beta(A, mul(B, C))) % 2
    mI = ((Fr(-1), Fr(0)), (Fr(0), Fr(-1)))
    ok &= beta(mI, mI) == 1 == hilb2(-1, -1)          # (-I,1)^2 = (I,-1)
    return ok


def count_powers(units, mulmod, m):
    def power(x):
        y = x
        for _ in range(m - 1):
            y = mulmod(y, x)
        return y
    return len({power(x) for x in units})


def w2():
    M = 9                                             # 9 = unit * pi^4, pi = 1 - omega
    def mm(x, y):                                     # (a + b w)(c + d w), w^2 = -1 - w
        a, b = x; c, d = y
        return ((a*c - b*d) % M, (a*d + b*c - b*d) % M)
    def is_unit(x):                                   # norm a^2 - ab + b^2 prime to 3
        a, b = x
        return (a*a - a*b + b*b) % 3 != 0
    units = [(a, b) for a in range(M) for b in range(M) if is_unit((a, b))]
    idx = len(units) // count_powers(units, mm, 3)
    return len(units) == 54 and idx == 27 and idx == 3 * 9   # |mu_3| * |3|^{-1}, q^e = 3^2


def w3():
    M = 8                                             # 8 = unit * pi^6, pi = 1 + i
    def mm(x, y):
        a, b = x; c, d = y
        return ((a*c - b*d) % M, (a*d + b*c) % M)
    units = [(a, b) for a in range(M) for b in range(M) if (a*a + b*b) % 2 == 1]
    idx = len(units) // count_powers(units, mm, 2)
    return len(units) == 32 and idx == 8 and idx == 2 * 4    # |mu_2| * |2|^{-1}, q^e = 2^2


def main():
    res = {"W1 Q_2, n=2: cocycle; center cyclic of order 4": w1(),
           "W2 Q_3(omega), n=3: [O^x:O^x3]=27, dim 9, C_0 of index 27": w2(),
           "W3 Q_2(i), n=4: [O^x:O^x2]=8, dim 4, C_0 of index 8": w3()}
    bad = 0
    for k, ok in res.items():
        print("%-62s %s" % (k, "ok" if ok else "FAIL")); bad += not ok
    print("\n%d failure(s)" % bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()

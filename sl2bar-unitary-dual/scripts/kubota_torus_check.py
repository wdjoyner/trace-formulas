# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact checks of the covering-torus computations in
"On the unitary dual of SL(2,F)-bar, F p-adic" (Draft 2, 2026).
Run: python3 kubota_torus_check.py (about one second).

Model: F = Q_p with n | p-1 (so mu_n is in F and gcd(p, n) = 1).
Elements of F^x are represented by nonzero rationals.  The tame n-th
Hilbert symbol is returned as an exponent k in Z/n, meaning zeta^k
for the fixed primitive n-th root of unity zeta = g^((p-1)/n), where
g is the least primitive root mod p.  All checks are exact.
"""
from fractions import Fraction as Fr
from itertools import product
import random

def val(x, p):
    x = Fr(x); v = 0
    if x == 0:
        return 10 ** 9  # valuation of 0 (only compared with >= 0 or > 0)
    num, den = x.numerator, x.denominator
    while num % p == 0: num //= p; v += 1
    while den % p == 0: den //= p; v -= 1
    return v

def unit_residue(x, p):
    x = Fr(x); v = val(x, p); y = x / Fr(p) ** v
    return (y.numerator * pow(y.denominator, -1, p)) % p

def primroot(p):
    for g in range(2, p):
        primes = [q for q in range(2, p) if (p - 1) % q == 0 and all(q % r for r in range(2, q))]
        if all(pow(g, (p - 1) // q, p) != 1 for q in primes):
            return g

def dlog(r, p, g):
    x = 1
    for k in range(p - 1):
        if x == r % p: return k
        x = x * g % p
    raise ValueError

def hilb(a, b, p, n, g):
    """Tame symbol (a,b)_n as an exponent mod n."""
    al, be = val(a, p), val(b, p)
    c = Fr(-1) ** (al * be) * Fr(a) ** be / Fr(b) ** al
    # r^((p-1)/n) = (g^k)^((p-1)/n) = zeta^k with k = dlog(r)
    return dlog(unit_residue(c, p), p, g) % n

def mul(A, B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))

def xfun(A):
    return A[1][0] if A[1][0] != 0 else A[1][1]

def beta(A, B, p, n, g):
    C = mul(A, B)
    return hilb(Fr(xfun(C)) / xfun(A), Fr(xfun(C)) / xfun(B), p, n, g)

def h(t): t = Fr(t); return ((t, Fr(0)), (Fr(0), 1 / t))
def u(x): return ((Fr(1), Fr(x)), (Fr(0), Fr(1)))
W = ((Fr(0), Fr(1)), (Fr(-1), Fr(0)))
Winv = ((Fr(0), Fr(-1)), (Fr(1), Fr(0)))

def gmul(X, Y, p, n, g):
    """Multiply (A, z)(B, w) = (AB, z + w + beta(A,B)) in exponent notation."""
    return (mul(X[0], Y[0]), (X[1] + Y[1] + beta(X[0], Y[0], p, n, g)) % n)

def rand_unit_rational(p, rng):
    while True:
        a = rng.randint(1, 50 * p); b = rng.randint(1, 50 * p)
        if a % p and b % p: return Fr(rng.choice([1, -1]) * a, b)

def rand_elt(p, rng):
    return rand_unit_rational(p, rng) * Fr(p) ** rng.randint(-3, 3)

def rand_sl2(p, rng):
    while True:
        a, b, c = rand_elt(p, rng), rand_elt(p, rng), rand_elt(p, rng)
        if rng.random() < 0.2: c = Fr(0)
        if a != 0:
            d = (1 + b * c) / a
            if d != 0: return ((a, b), (c, d))

def check(p, n, trials=300, seed=1):
    assert (p - 1) % n == 0
    g = primroot(p); rng = random.Random(seed)
    d = n // (2 if n % 2 == 0 else 1)
    out = {}
    # 0. cocycle identity (validates the implementation)
    ok = True
    for _ in range(trials):
        A, B, C = rand_sl2(p, rng), rand_sl2(p, rng), rand_sl2(p, rng)
        lhs = (beta(A, B, p, n, g) + beta(mul(A, B), C, p, n, g)) % n
        rhs = (beta(A, mul(B, C), p, n, g) + beta(B, C, p, n, g)) % n
        ok &= lhs == rhs
    out["cocycle identity"] = ok
    # 1. beta(h(a),h(b)) = (b,a)_n
    ok = all(beta(h(a), h(b), p, n, g) == hilb(b, a, p, n, g)
             for a, b in ((rand_elt(p, rng), rand_elt(p, rng)) for _ in range(trials)))
    out["beta(h(a),h(b)) = (b,a)"] = ok
    # 2. commutator h~(a) h~(b) h~(a)^-1 h~(b)^-1 = (a,b)^(-2)
    ok = True
    for _ in range(trials):
        a, b = rand_elt(p, rng), rand_elt(p, rng)
        lhs = (beta(h(a), h(b), p, n, g) - beta(h(b), h(a), p, n, g)) % n  # h~(a)h~(b) vs h~(b)h~(a)
        ok &= lhs == (-2 * hilb(a, b, p, n, g)) % n
    out["[h~(a),h~(b)] = (a,b)^(-2)"] = ok
    # 3. w~^{-1} = (w^{-1}, 1) and w~^{-1} h~(t) w~ = h~(t^{-1}) for all t
    out["beta(w, w^-1) = 1"] = beta(W, Winv, p, n, g) == 0
    ok = True
    for _ in range(trials):
        t = rand_elt(p, rng)
        X = gmul(gmul((Winv, 0), (h(t), 0), p, n, g), (W, 0), p, n, g)
        ok &= X[0] == h(1 / t) and X[1] == 0
    out["w~^-1 h~(t) w~ = h~(t^-1)"] = ok
    # 4. h~(t)^{-1} = (h(t^{-1}), (t,-1))
    ok = True
    for _ in range(trials):
        t = rand_elt(p, rng)
        # inverse of (h(t),0) is (h(t^-1), -beta(h(t),h(t^-1)))
        ok &= (-beta(h(t), h(1 / t), p, n, g)) % n == hilb(t, -1, p, n, g)
    out["h~(t)^-1 = (t,-1) h~(t^-1)"] = ok
    # 5. center: a central iff (a,b)^2 = 1 for all b; index of center = d^2
    reps = [Fr(p) ** i * Fr(g) ** j for i in range(n) for j in range(n)]  # F^x / F^x^n
    central = [a for a in reps if all((2 * hilb(a, b, p, n, g)) % n == 0 for b in reps)]
    out["[F^x : center-set] = d^2"] = (len(reps) // len(central) == d * d)
    dth = {(val(a, p) % n, dlog(unit_residue(a, p), p, g) % n) for a in reps
           if val(a, p) % d == 0 and dlog(unit_residue(a, p), p, g) % d == 0}
    out["center-set = (F^x)^d"] = {(val(a, p) % n, dlog(unit_residue(a, p), p, g) % n) for a in central} == dth
    # 6. nu(t) = (h(t^d),1) multiplicative iff n | d^2
    mult = all(beta(h(s ** d), h(t ** d), p, n, g) == 0
               for s, t in ((rand_elt(p, rng), rand_elt(p, rng)) for _ in range(trials)))
    out[f"nu multiplicative (expected {d*d % n == 0})"] = (mult == (d * d % n == 0))
    # 7. u -> (p,u)^2 on units has order exactly d
    vals = {(2 * hilb(p, Fr(g) ** j, p, n, g)) % n for j in range(p - 1)}
    out["u -> (pi,u)^2 has order d on units"] = (len(vals) == d)
    return out


def kappa(k, p, n, g):
    """Candidate Kubota splitting on K = SL(2, O): (c, d)_n if 0 < |c| < 1, else 1."""
    c, dd = k[1][0], k[1][1]
    if c != 0 and val(c, p) > 0:
        return hilb(c, dd, p, n, g)
    return 0

def rand_K(p, rng):
    while True:
        a, b, c = [Fr(rng.randint(-60, 60), rng.choice([1, 2, 4, 8, 3]) if p != 3 else rng.choice([1, 2, 4])) for _ in range(3)]
        if rng.random() < 0.4: c = c * p
        if rng.random() < 0.15: c = Fr(0)
        if a != 0 and val(a, p) >= 0 and val(b, p) >= 0 and val(c, p) >= 0:
            d = (1 + b * c) / a
            if d != 0 and val(d, p) >= 0: return ((a, b), (c, d))

def check_splitting(p, n, trials=400, seed=2):
    """Check kappa(k1 k2) = kappa(k1) + kappa(k2) + beta(k1, k2), so k -> (k, kappa(k))
    is a homomorphism K -> G~, and kappa = 0 on upper triangular elements of K."""
    g = primroot(p); rng = random.Random(seed); ok = True
    for _ in range(trials):
        A, B = rand_K(p, rng), rand_K(p, rng)
        ok &= kappa(mul(A, B), p, n, g) == (kappa(A, p, n, g) + kappa(B, p, n, g) + beta(A, B, p, n, g)) % n
    return ok


if __name__ == "__main__":
    import sys
    PAIRS = [(7, 3), (13, 3), (5, 4), (13, 4), (7, 6), (13, 6), (3, 2), (7, 2)]
    all_ok = True
    for p, n in PAIRS:
        res = check(p, n)
        res["splitting k -> (k, kappa(k)) on SL(2,O)"] = check_splitting(p, n)
        ok = all(res.values())
        all_ok &= ok
        print(f"p={p:2d} n={n}:", "all checks pass" if ok else res)
    ex = hilb(5, -1, 5, 4, primroot(5))
    print("Example 3.1: (5,-1)_4 has exponent", ex, "(2 means -1)")
    all_ok &= (ex == 2)
    print("ALL PASS" if all_ok else "SOME CHECK FAILED")
    sys.exit(0 if all_ok else 1)

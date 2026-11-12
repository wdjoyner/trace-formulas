# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Checks of the five examples added in the style-guide pass (November 2026):
Example 4.A (ex:trunc-Q: heights and truncation on the upper half plane),
Examples 4.C and 4.D (ex:JA-hyp-p, ex:JA-central-p: J_G and J_A at a
hyperbolic element and J_A at a central element, for the unit e_p), and
Example 7.F (ex:uprime-gl2: the weight u'_B for delta_p). Example 7.D
(ex:kappa-unram) is derived from Lemma 7.6(d) (lem:kappa-orbital) and has no numerical check.

Exact rational arithmetic where possible. Floats only for the real place."""
import math
import random
import sys
from fractions import Fraction as Fr

from padic_lib import vp
from cover_lib import M2, mul, inv, a_, n_, W, cmul, cinv, in_K, sigma

random.seed(20261112)
FAIL = []


def check(name, ok):
    print(("ok   " if ok else "FAIL ") + name)
    if not ok:
        FAIL.append(name)


# ------------------------------------------------------------------ 4.A
def H_real(g):
    """H(g) = -log ||e_2 g|| at the real place (Lemma 4.3(a))."""
    c, d = g[1]
    return -0.5 * math.log(c * c + d * d)


def g_of_z(u, y):
    s = math.sqrt(y)
    return ((s, u / s), (0.0, 1 / s))  # n(u) a(sqrt y)


def mulf(g, h):
    return ((g[0][0] * h[0][0] + g[0][1] * h[1][0], g[0][0] * h[0][1] + g[0][1] * h[1][1]),
            (g[1][0] * h[0][0] + g[1][1] * h[1][0], g[1][0] * h[0][1] + g[1][1] * h[1][1]))


def rand_sl2z():
    while True:
        c, d = random.randint(-30, 30), random.randint(-30, 30)
        if c != 0 and math.gcd(c, d) == 1:
            break
    # solve a d - b c = 1
    for a in range(-200, 201):
        if (a * d - 1) % c == 0:
            b = (a * d - 1) // c
            return ((a, b), (c, d))


ok1 = ok2 = ok3 = True
for _ in range(2000):
    u, y = random.uniform(-3, 3), math.exp(random.uniform(-3, 3))
    z = complex(u, y)
    x = g_of_z(u, y)
    ok1 &= abs(H_real(x) - 0.5 * math.log(y)) < 1e-12
    gam = rand_sl2z()
    gz = (gam[0][0] * z + gam[0][1]) / (gam[1][0] * z + gam[1][1])
    Hg = H_real(mulf(gam, x))
    ok2 &= abs(Hg - 0.5 * math.log(gz.imag)) < 1e-9
    ok3 &= H_real(x) + Hg <= 1e-12
check("4.A: H(n(u)a(y^1/2)) = (1/2) log y", ok1)
check("4.A: H(gamma x) = (1/2) log Im(gamma z) for gamma in SL(2,Z)", ok2)
check("4.A: H(x) + H(gamma x) <= 0 for c != 0", ok3)

ok = True
for _ in range(300):
    z = complex(random.uniform(-1, 1), math.exp(random.uniform(-2, 2)))
    for T in (0.0, 0.3, 1.0):
        cnt = 0
        # cosets B(Q)\G(Q) meeting SL(2,Z): coprime (c, d) up to sign
        for c in range(0, 40):
            for d in range(-40, 41):
                if math.gcd(c, d) != 1 or (c == 0 and d != 1):
                    continue
                if c == 0 or True:
                    im = z.imag / abs(c * z + d) ** 2
                    if im > math.exp(2 * T):
                        cnt += 1
        ok &= cnt <= 1
check("4.A: for T >= 0 at most one coset with Im(delta z) > e^{2T}", ok)


# ------------------------------------------------------------------ 4.C
def JA_closed(p, m):
    return math.log(p) * (m - (1 - p ** (-m)) / (p - 1))


def JA_cosets(p, m):
    # p^{-m} * sum over cosets r p^{-m} + Z_p of log max(1, |r p^{-m}|_p)
    tot = 0.0
    for r in range(p ** m):
        if r == 0:
            continue
        val = m - vp(Fr(r), p)  # |r p^-m|_p = p^(m - v_p(r))
        tot += max(0, val) * math.log(p)
    return tot * p ** (-m)


ok_conj = ok_JA = ok_JG = True
for p in (3, 5, 7):
    for _ in range(40):
        while True:
            t = Fr(random.randint(1, 400), random.randint(1, 400))
            if t * t != 1 and vp(t, p) == 0:
                break
        m = vp(1 - 1 / (t * t), p)
        # conjugation in the cover (sigma-model at an odd prime)
        for _ in range(5):
            y = Fr(random.randint(-500, 500), p ** random.randint(0, 4))
            ny = (n_(y), 1)
            prod = cmul(cmul(cinv(ny, p), (a_(t), 1), p), ny, p)
            target = mul(a_(t), n_((1 - 1 / (t * t)) * y))
            ok_conj &= prod[0] == target and prod[1] == 1
            # in K* (= {(k,1)} in the sigma-model) iff |(1-t^-2) y|_p <= 1
            u = (1 - 1 / (t * t)) * y
            ok_conj &= in_K(prod[0], p) == (u == 0 or vp(u, p) >= 0)
        # J_G = |D|^{1/2} * vol{|y| <= p^m} = p^-m * p^m
        absD = Fr(1, p ** vp(t - 1 / t, p))
        ok_JG &= absD * p ** m == 1
        ok_JA &= abs(JA_closed(p, m) - JA_cosets(p, m)) < 1e-12
check("4.C: n(-y)(a(t),1)n(y) = (a(t)n((1-t^-2)y),1), in K* iff |(1-t^-2)y| <= 1", ok_conj)
check("4.C: J_G(a(t), e_p) = 1", ok_JG)
check("4.C: J_A(a(t), e_p) = log p (m - (1-p^-m)/(p-1))", ok_JA)
check("4.C: p = 3, t = 2: m = 1 and J_A = (2/3) log 3",
      vp(1 - Fr(1, 4), 3) == 1 and abs(JA_closed(3, 1) - 2 * math.log(3) / 3) < 1e-14)

# ------------------------------------------------------------------ 4.D
ok = True
for p in (3, 5, 7, 11):
    s = sum(-j * math.log(p) * (p ** (-j) - p ** (-j - 1)) for j in range(1, 200))
    ok &= abs(s + math.log(p) / (p - 1)) < 1e-12
check("4.D: int_{Z_p} log|2y|_p dy = -log p/(p-1) (p odd)", ok)
ok = True
for p in (3, 5, 7):
    for _ in range(50):
        y = Fr(random.randint(-300, 300), p ** random.randint(0, 3))
        for z in (1, -1):
            g = (M2(z, 0, 0, z), 1)
            x = cmul(g, (n_(y), 1), p)
            ok &= x[1] == 1 and in_K(x[0], p) == (y == 0 or vp(y, p) >= 0)
check("4.D: z(n(y),1) lies in K* iff y in Z_p, so Phi_p = 1_{Z_p}", ok)


# ------------------------------------------------------------------ 7.F
def H1_p(g, p):
    """H_1(g) = -log||e_2 g||_p + (1/2) log|det g|_p, in units of log p."""
    (a, b), (c, d) = g
    nrm = max(-vp(e, p) for e in (c, d) if e != 0)  # log_p ||e_2 g||
    det = a * d - b * c
    return Fr(-nrm) + Fr(-vp(det, p), 2)


ok = True
for p in (3, 5, 7):
    dp = M2(p, 0, 0, 1)
    for _ in range(200):
        # random k in SL(2, Z_(p)) with integer entries
        while True:
            c, d = random.randint(-50, 50), random.randint(-50, 50)
            if math.gcd(c, d) == 1 and (c, d) != (0, 0):
                break
        for a in range(-300, 301):
            if c != 0 and (a * d - 1) % c == 0:
                k = M2(a, (a * d - 1) // c, c, d)
                break
        else:
            if c == 0:
                k = M2(d, 0, 0, d)
            else:
                continue
        val = H1_p(mul(k, dp), p)
        expect = Fr(-1, 2) if vp(Fr(d), p) == 0 else Fr(1, 2)
        ok &= val == expect
    # consistency of Lemma 7.8(a) at x = 1: v_A(1) - H1(delta) - H1(w delta) = 0
    ok &= -H1_p(dp, p) - H1_p(mul(W, dp), p) == 0
check("7.F: -H_1(k delta_p) = (1/2) log p if d is a unit, -(1/2) log p if p | d", ok)
check("7.F: v_A(1) - H_1(delta_p) - H_1(w delta_p) = 0", ok)

ok = True
for p in (3, 5, 7):
    cnt = tot = 0
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a * d - b * c) % p == 1:
                        tot += 1
                        cnt += d == 0
    ok &= Fr(cnt, tot) == Fr(1, p + 1)
check("7.F: {k in K_p : p | d} has measure 1/(p+1)", ok)

print()
print("%d failed" % len(FAIL))
sys.exit(1 if FAIL else 0)

# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact checks of the n = 2 foundations in Section 2 of the revised
"hitch-hiker's guide to the metaplectic trace formula for SL(2)".

Everything is computed with exact rationals: an element of SL(2, Q) is
viewed in SL(2, Q_v) for v = p or v = infinity, and the quadratic Hilbert
symbol (a, b)_v of rationals is evaluated by the standard formulas.
Random elements are generated with a fixed seed, so the run is reproducible.

Each check prints PASS/FAIL; the script exits nonzero on any failure.
Statement numbers refer to sec2-foundations.tex.
"""
import random
import sys
from fractions import Fraction as Fr
from sympy import primefactors

random.seed(20261110)
FAILS = []
from padic_lib import INF, vp, hilbert


def report(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILS.append(name)


def absv(x, v):
    x = Fr(x)
    if x == 0:
        return Fr(0)
    if v == INF:
        return abs(x)
    return Fr(v) ** (-vp(x, v))


# ---------------------------------------------------------------- matrices
def mul(g, h):
    (a, b), (c, d) = g
    (e, f), (gg, hh) = h
    return ((a * e + b * gg, a * f + b * hh), (c * e + d * gg, c * f + d * hh))


def det(g):
    return g[0][0] * g[1][1] - g[0][1] * g[1][0]


def inv(g):
    (a, b), (c, d) = g
    D = det(g)
    return ((d / D, -b / D), (-c / D, a / D))


def M(a, b, c, d):
    return ((Fr(a), Fr(b)), (Fr(c), Fr(d)))


I2 = M(1, 0, 0, 1)
MINUS1 = M(-1, 0, 0, -1)
W = M(0, 1, -1, 0)


def xg(g):
    c, d = g[1]
    return c if c != 0 else d


# ---------------------------------------------------------------- cocycles
def beta(g1, g2, v):
    """Kubota's cocycle, second form: (x3/x1, x3/x2)_v."""
    x1, x2, x3 = xg(g1), xg(g2), xg(mul(g1, g2))
    return hilbert(x3 / x1, x3 / x2, v)


def beta_first_form(g1, g2, v):
    """First form: (x1, x2)_v (-x1^{-1} x2, x3)_v."""
    x1, x2, x3 = xg(g1), xg(g2), xg(mul(g1, g2))
    return hilbert(x1, x2, v) * hilbert(-x2 / x1, x3, v)


def sigma_gl2(g1, g2, v):
    """2-fold cocycle on GL(2): (x3/x1, x3/(x2 det g1))_v."""
    x1, x2, x3 = xg(g1), xg(g2), xg(mul(g1, g2))
    return hilbert(x3 / x1, x3 / (x2 * det(g1)), v)


def in_K(g, p):
    return all(e == 0 or vp(e, p) >= 0 for row in g for e in row) and vp(det(g), p) == 0


def kappa(g, p):
    """Kubota's correction at an odd prime p: (c, d)_p if g in K and 0<|c|_p<1."""
    if p == INF or p == 2 or not in_K(g, p):
        return 1
    c, d = g[1]
    if c != 0 and vp(c, p) > 0:
        return hilbert(c, d, p)
    return 1


def cocycle_ok(cyc, g1, g2, g3, v):
    return cyc(g1, g2, v) * cyc(mul(g1, g2), g3, v) == cyc(g1, mul(g2, g3), v) * cyc(g2, g3, v)


# ---------------------------------------------------------------- samplers
def rand_rat(p=None, minval=0, big=40):
    """Random nonzero rational; if p is given, of p-adic valuation >= minval."""
    while True:
        num = random.randint(-big, big)
        den = random.randint(1, big)
        if num == 0:
            continue
        x = Fr(num, den)
        if p is None or p == INF:
            return x
        if x.denominator % p == 0:
            continue
        if vp(x, p) < minval:
            x *= Fr(p) ** (minval - vp(x, p))
        return x


def upper(u):
    return M(1, u, 0, 1)


def lower(u):
    return M(1, 0, u, 1)


def diag(t):
    return M(t, 0, 0, 1 / Fr(t))


def rand_sl2Q(length=4):
    g = I2
    for _ in range(length):
        r = random.random()
        if r < 0.35:
            g = mul(g, upper(rand_rat()))
        elif r < 0.7:
            g = mul(g, lower(rand_rat()))
        elif r < 0.9:
            g = mul(g, diag(rand_rat()))
        else:
            g = mul(g, W)
    return g


def rand_unit(p, m=0):
    """Random p-adic unit congruent to 1 mod p^m (m=0: any unit)."""
    while True:
        x = rand_rat(p, 0)
        if vp(x, p) != 0:
            continue
        if m == 0:
            return x
        return 1 + Fr(p) ** m * rand_rat(p, 0)


def rand_K(p, m=0, length=5):
    """Random element of K_m (m >= 1) or of K_0 = SL(2, Z_(p))."""
    g = I2
    for _ in range(length):
        r = random.random()
        if r < 0.35:
            g = mul(g, upper(Fr(p) ** m * rand_rat(p, 0) if random.random() < .8 else Fr(0)))
        elif r < 0.7:
            # include lower unipotents with c of positive valuation
            g = mul(g, lower(rand_rat(p, max(m, random.choice([0, 1, 2])))))
        elif r < 0.9:
            g = mul(g, diag(rand_unit(p, m)))
        elif m == 0:
            g = mul(g, W)
    assert in_K(g, p)
    return g


def rand_torus(theta):
    s = rand_rat()
    D = 1 - theta * s * s
    if D == 0:
        return rand_torus(theta)
    a, b = (1 + theta * s * s) / D, 2 * s / D
    return M(a, b * theta, b, a)


def rand_E_times(theta):
    a, b = rand_rat(), rand_rat()
    if random.random() < 0.2:
        b = Fr(0)
    if a * a - theta * b * b == 0:
        return rand_E_times(theta)
    return M(a, b * theta, b, a)


PLACES = [INF, 2, 3, 5, 7]
NS = 100  # samples per test

# ===================================================================
print("Section 2.1: the local cover (n = 2)")
# Lemma 2.1: cocycle; the two printed forms agree
for v in PLACES:
    ok1 = all(cocycle_ok(beta, rand_sl2Q(), rand_sl2Q(), rand_sl2Q(), v) for _ in range(NS))
    ok2 = all(beta(g, h, v) == beta_first_form(g, h, v)
              for g, h in ((rand_sl2Q(), rand_sl2Q()) for _ in range(NS)))
    report("Lemma 2.1: beta_v is a 2-cocycle, v=%s" % v, ok1)
    report("(2.0) the two formulas for beta_v agree, v=%s" % v, ok2)

# Lemma 2.2(b) / item I.1: beta is NOT trivial on K x K, but beta = d(kappa) there
for p in [3, 5, 7]:
    pairs = [(rand_K(p), rand_K(p)) for _ in range(NS)]
    nontriv = any(beta(a, b, p) == -1 for a, b in pairs)
    report("I.1: beta_p is nontrivial on K x K, p=%d" % p, nontriv)
    ok = all(beta(a, b, p) == kappa(a, p) * kappa(b, p) * kappa(mul(a, b), p) for a, b in pairs)
    report("Lemma 2.2(b): k -> (k, kappa(k)) is a homomorphism on K, p=%d" % p, ok)
    # and k -> (k,1) is not: the image of K under k -> (k,1) is not a subgroup
    report("I.1: k -> (k,1) is not a homomorphism on K, p=%d" % p,
           any(beta(a, b, p) != 1 for a, b in pairs))

# Lemma 2.2(c) / item I.2: beta = 1 on K_m x K_m once 1 + p^m O consists of squares
# (m >= 1 for odd p; m >= 3 = 2e+1 for F = Q_2)
for p, m in [(3, 1), (5, 1), (7, 1), (2, 3)]:
    pairs = [(rand_K(p, m), rand_K(p, m)) for _ in range(3 * NS)]
    report("Lemma 2.2(c): beta_p = 1 on K_m x K_m, p=%d, m=%d" % (p, m),
           all(beta(a, b, p) == 1 for a, b in pairs))
pairs = [(rand_K(2, 2), rand_K(2, 2)) for _ in range(3 * NS)]
report("Lemma 2.2(c): beta_2 is not identically 1 on K_2 x K_2 for F = Q_2",
       any(beta(a, b, 2) == -1 for a, b in pairs))


def kappa2(g):
    c, d = g[1]
    return hilbert(c, d, 2) if c != 0 else 1


report("Remark 2026.1: k -> (k, (c,d)_2) splits K_2 for F = Q_2",
       all(beta(a, b, 2) == kappa2(a) * kappa2(b) * kappa2(mul(a, b)) for a, b in pairs))
pairs = [(rand_K(2, 1), rand_K(2, 1)) for _ in range(3 * NS)]
report("Remark 2026.1: that section does not split K_1 for F = Q_2",
       not all(beta(a, b, 2) == kappa2(a) * kappa2(b) * kappa2(mul(a, b)) for a, b in pairs))

# Lemma 2.2(e) / item I.6: the center
for v in PLACES:
    sq = beta(MINUS1, MINUS1, v)
    report("Lemma 2.2(e): (-1,1)^2 = (1,(-1,-1)_v), v=%s" % v, sq == hilbert(-1, -1, v),
           "(-1,-1)_v = %d" % sq)
    report("Lemma 2.2(e): p^{-1}(+-1) is central, v=%s" % v,
           all(beta(MINUS1, g, v) == beta(g, MINUS1, v) for g in (rand_sl2Q() for _ in range(NS))))
report("I.6: center cyclic of order 4 exactly for v = inf, 2 (of the places tested)",
       [hilbert(-1, -1, v) for v in PLACES] == [-1, -1, 1, 1, 1])

# Lemma 2.2(f): on A, beta(a1,a2) = (t1,t2) and A-bar is abelian
for v in PLACES:
    ok = True
    for _ in range(NS):
        t1, t2 = rand_rat(), rand_rat()
        a1, a2 = diag(t1), diag(t2)
        ok &= beta(a1, a2, v) == hilbert(t1, t2, v) == beta(a2, a1, v)
    report("Lemma 2.2(f): beta(a1,a2) = (t1,t2)_v symmetric, v=%s" % v, ok)

# Lemma 2.2(g) / I.8: preimages of commuting pairs commute; tori T_theta
# theta: a nonsquare unit (unramified E = F(sqrt theta)) and a ramified choice
THETA = {INF: Fr(-1), 2: Fr(5), 3: Fr(2), 5: Fr(2), 7: Fr(3)}
THETA_RAM = {INF: Fr(-1), 2: Fr(2), 3: Fr(3), 5: Fr(5), 7: Fr(7)}
for _v in PLACES:
    for _th in (THETA[_v], THETA_RAM[_v]):
        # theta is not a square in Q_v: some Hilbert symbol (theta, y)_v is -1
        assert any(hilbert(_th, y, _v) == -1 for y in [-1, 2, 3, 5, 7, 10, 15, 6])
for v in PLACES:
    for th in (THETA[v], THETA_RAM[v]):
        ok = True
        for _ in range(NS):
            g, h = rand_torus(th), rand_torus(th)
            assert det(g) == 1 and mul(g, h) == mul(h, g)
            ok &= beta(g, h, v) == beta(h, g, v)
        report("Lemma 2.2(g): preimage of T_theta abelian, v=%s, theta=%s" % (v, th), ok)

# Lemma 2.2(h): unipotent lifts.  For n = 2 the section u -> (u,1) is a
# homomorphism on EVERY unipotent subgroup g N g^{-1} (Steinberg relation),
# and conjugation by any lift of g carries (n,1) to (g n g^{-1}, 1).
def conj_factor(g, u, v):
    # (g,1)(u,1)(g,1)^{-1} = (g u g^{-1}, c); for n = 2, (g,1)^{-1} = (g^{-1}, beta(g,g^{-1}))
    return beta(g, u, v) * beta(mul(g, u), inv(g), v) * beta(g, inv(g), v)


for v in PLACES:
    okN = all(beta(upper(rand_rat()), upper(rand_rat()), v) == 1 for _ in range(NS))
    report("Lemma 2.2(a): n -> (n,1) is a homomorphism on N, v=%s" % v, okN)
    okL = all(beta(lower(rand_rat()), lower(rand_rat()), v) == 1 for _ in range(NS))
    report("Lemma 2.2(h): u -> (u,1) is a homomorphism on lower unipotents too, v=%s" % v, okL)
    ok = True
    for _ in range(NS):
        g = rand_sl2Q()
        u1, u2 = mul(mul(g, upper(rand_rat())), inv(g)), mul(mul(g, upper(rand_rat())), inv(g))
        ok &= beta(u1, u2, v) == 1
    report("Lemma 2.2(h): u -> (u,1) is a homomorphism on g N g^-1 for random g, v=%s" % v, ok)
    ok = all(conj_factor(rand_sl2Q(), upper(rand_rat()), v) == 1 for _ in range(NS))
    report("Lemma 2.2(h): (g,z)(n,1)(g,z)^-1 = (g n g^-1, 1) for random g, v=%s" % v, ok)

# ===================================================================
print("Section 2.2: the global cover (k = Q, n = 2)")


def places_for(*gs):
    S = {INF, 2}
    for g in gs:
        for row in g:
            for e in row:
                if e != 0:
                    for z in (e.numerator, e.denominator):
                        S.update(primefactors(abs(z)))
    return S


def kappa_A(g):
    out = 1
    for v in places_for(g):
        out *= kappa(g, v)
    return out


ok_rec, ok_split = True, True
for _ in range(NS):
    g, h = rand_sl2Q(), rand_sl2Q()
    S = places_for(g, h, mul(g, h))
    prod_beta = 1
    for v in S:
        prod_beta *= beta(g, h, v)
    ok_rec &= prod_beta == 1
    # modified global cocycle sigma = prod_v beta_v * d(kappa_v)
    sig = 1
    for v in S:
        sig *= beta(g, h, v) * kappa(g, v) * kappa(h, v) * kappa(mul(g, h), v)
    ok_split &= sig == kappa_A(g) * kappa_A(h) * kappa_A(mul(g, h))
report("Hilbert reciprocity: prod_v beta_v(g,h) = 1 on SL(2,Q)", ok_rec)
report("Lemma 2.6(a), (2.9): gamma -> (gamma, kappa_A(gamma)) splits sigma_A over SL(2,Q)", ok_split)
okB = all(kappa_A(mul(diag(rand_rat()), upper(rand_rat()))) == 1 for _ in range(NS))
report("Lemma 2.6(b): on B(Q) the rational splitting is b -> (b,1)", okB)

# Example 2.C: for gamma in SL(2,Z) with c != 0, kappa_A(gamma) = (d / c') (Jacobi), c' = odd part of |c|
def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


def rand_sl2Z():
    g = I2
    for _ in range(6):
        e = Fr(random.randint(-6, 6))
        g = mul(g, upper(e) if random.random() < .5 else lower(e))
    return g


ok, cnt = True, 0
for _ in range(4 * NS):
    g = rand_sl2Z()
    c, d = int(g[1][0]), int(g[1][1])
    if c == 0:
        continue
    co = abs(c)
    while co % 2 == 0:
        co //= 2
    ok &= kappa_A(g) == jacobi(d, co)
    cnt += 1
report("Example 2.C: kappa_A(gamma) = (d/c') on SL(2,Z)", ok and cnt > 100, "%d samples" % cnt)

# Lemma 2.6(d): global center; -1 at the infinite place only
eps_sq = hilbert(-1, -1, INF)
report("Lemma 2.6(d): lift of (-1 at inf, +1 elsewhere) has square (1,-1): not a direct product",
       eps_sq == -1)
glob = 1
for v in [INF, 2, 3, 5, 7, 11]:
    glob *= hilbert(-1, -1, v)
report("Lemma 2.6(d): the rational element -1 has square 1 (product formula)", glob == 1)

# ===================================================================
print("Section 2.3: the GL(2) cover (n = 2)")


def rgl():
    return mul(rand_sl2Q(), M(rand_rat(), 0, 0, 1))


for v in PLACES:
    ok = all(cocycle_ok(sigma_gl2, rgl(), rgl(), rgl(), v) for _ in range(NS))
    report("Lemma 2.10(a): sigma is a 2-cocycle on GL(2), v=%s" % v, ok)
    ok = all(sigma_gl2(g, h, v) == beta(g, h, v) for g, h in ((rand_sl2Q(), rand_sl2Q()) for _ in range(NS)))
    report("Lemma 2.10(a): sigma restricts to beta on SL(2), v=%s" % v, ok)
    # commutator formula for commuting h in GL(2), gamma in SL(2)
    ok = True
    for _ in range(NS):
        th = THETA[v]
        h, gam = rand_E_times(th), rand_torus(th)
        assert mul(h, gam) == mul(gam, h)
        lhs = sigma_gl2(h, gam, v) * sigma_gl2(gam, h, v)
        rhs = hilbert(xg(mul(h, gam)) / xg(h), det(h), v)
        ok &= lhs == rhs
        y, t = rand_rat(), rand_rat()
        hh, a = M(y, 0, 0, 1), diag(t)
        ok &= sigma_gl2(hh, a, v) * sigma_gl2(a, hh, v) == hilbert(y, t, v)
    report("Lemma 2.10(c): commutator = (x(h gamma)/x(h), det h)_v; diag(y,1) acts on A-bar by (y,t)_v, v=%s" % v, ok)
    if v != INF:
        some = any(hilbert(rand_rat(), rand_rat(), v) == -1 for _ in range(50))
        report("Lemma 2.10(c): the preimage of the diagonal torus of GL(2) is non-abelian, v=%s" % v, some)

for v in PLACES:
    tw = lambda g, h, v: sigma_gl2(g, h, v) * hilbert(det(g), det(h), v)
    report("Remark 2026.2: the twisted cocycle sigma*(det,det) is also a cocycle, v=%s" % v,
           all(cocycle_ok(tw, rgl(), rgl(), rgl(), v) for _ in range(NS // 2)))
ok = True
for _ in range(NS):
    g, h = rgl(), rgl()
    pr = 1
    for v in places_for(g, h, mul(g, h), M(det(g), 0, 0, det(h))):
        pr *= sigma_gl2(g, h, v)
    ok &= pr == 1
report("Section 2.3: Hilbert reciprocity prod_v sigma_v(g,h) = 1 on GL(2,Q)", ok)

# splitting of the GL(2) cover over GL(2, Z_p), p odd
for p in [3, 5, 7]:
    def rGLK():
        return mul(rand_K(p), M(rand_unit(p), 0, 0, 1))

    def kap_gl(g):
        c, d = g[1]
        if c != 0 and vp(c, p) > 0:
            return hilbert(c, d / det(g), p)
        return 1
    pairs = [(rGLK(), rGLK()) for _ in range(NS)]
    ok = all(sigma_gl2(a, b, p) == kap_gl(a) * kap_gl(b) * kap_gl(mul(a, b)) for a, b in pairs)
    report("Lemma 2.10(b): k -> (k, (c, d/det k)_p) splits GL(2,Z_p) when 0<|c|<1, p=%d" % p, ok)

# ===================================================================
print()
print("Lemma 2.1 and Section 2.1.4: topology of the cover (2026 referee report, 1.1 and 1.3)")
# beta is not continuous: beta(-1, lower(c)) = (c,-1)_v, while lower(c) -> 1
report("Lemma 2.1: beta_R(-1, lower(c)) = sgn(c), so beta_R is discontinuous at (-1, 1)",
       all(beta(MINUS1, lower(Fr(1, n)), INF) == 1 and beta(MINUS1, lower(Fr(-1, n)), INF) == -1
           for n in range(1, 40)) and beta(MINUS1, I2, INF) == 1)
report("Lemma 2.1: beta_3(-1, lower(3^n)) = (-1)^n, so beta_3 is discontinuous at (-1, 1)",
       all(beta(MINUS1, lower(Fr(3) ** n), 3) == (-1) ** n for n in range(1, 12)))
# in general beta(a(t), lower(c)) = (c,t)_v; for v = 5 and the non-square t = 2 this is (-1)^n at c = 5^n
report("Example 2.A: beta_5(a(2), lower(5^n)) = (-1)^n, so beta_5 is discontinuous at (a(2), 1)",
       all(beta(diag(2), lower(Fr(5) ** n), 5) == (-1) ** n for n in range(1, 12)))
ok = all(beta(diag(t), lower(c), v) == hilbert(c, t, v)
         for v in PLACES for t, c in ((rand_rat(), rand_rat()) for _ in range(NS)))
report("Example 2.A: beta_v(a(t), lower(c)) = (c,t)_v, all v", ok)
# beta = 1 on U x U, U = {a > 0, d > 0} in SL(2,R)
def rand_U():
    while True:
        g = rand_sl2Q()
        if g[0][0] > 0 and g[1][1] > 0:
            return g
pairs = [(rand_U(), rand_U()) for _ in range(20 * NS)]
# include pairs with c = 0 and with product lower-left entry 0
pairs += [(upper(rand_rat()), rand_U()) for _ in range(NS)] + [(rand_U(), upper(rand_rat())) for _ in range(NS)]
for _ in range(NS):
    g = rand_U()
    (a, b), (c, d) = g
    if c != 0:
        # h in U with (gh)_{21} = c*a2 + d*c2 = 0
        a2 = abs(rand_rat())
        c2 = -c * a2 / d
        b2 = rand_rat()
        d2 = (1 + b2 * c2) / a2
        if d2 > 0:
            pairs.append((g, M(a2, b2, c2, d2)))
report("Lemma 2.1: beta_R = 1 on U x U, U = {a > 0, d > 0} (%d pairs)" % len(pairs),
       all(beta(g, h, INF) == 1 for g, h in pairs))
# the unit e_p read through g -> (g,1): e_p(k,1) = kappa(k); k_n -> -1 but kappa(k_n) = (-1)^n
report("Section 2.1.4: kappa_3((-1,0;3^n,-1)) = (-1)^n, so g -> e_3(g,1) is not locally constant",
       all(kappa(M(-1, 0, Fr(3) ** n, -1), 3) == (-1) ** n for n in range(1, 12)))
# continuity of the sections actually used: on A the cocycle is the Hilbert symbol, which is
# locally constant: (t0, s) = 1 for s in 1 + p^m Z_p (m = 1 odd p, m = 3 for p = 2), s > 0 for v = oo
ok = True
for v in PLACES:
    for _ in range(NS):
        t0 = rand_rat()
        if v == INF:
            s = abs(rand_rat())
        else:
            s = 1 + Fr(v) ** (3 if v == 2 else 1) * rand_rat(v, 0)
        ok &= beta(diag(t0), diag(s), v) == 1 and beta(diag(s), diag(t0), v) == 1
report("Lemma 2.2(i): a -> (a,1) is continuous on A(F): beta(a(t0), a(s)) = 1 for s near 1", ok)
ok = True
for p in [3, 5, 7]:
    for _ in range(NS):
        k = rand_K(p, 1)
        ok &= kappa(k, p) == 1
report("Lemma 2.2(i): kappa = 1 on K_1 (p odd), so k -> (k, kappa(k)) is continuous on K", ok)

print()
if FAILS:
    print("%d check(s) FAILED: %s" % (len(FAILS), ", ".join(FAILS)))
    sys.exit(1)
print("All Section 2 (n = 2) checks passed.")

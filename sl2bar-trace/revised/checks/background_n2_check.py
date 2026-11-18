# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Checks of the examples added to Section 2 in the background pass of
November 18, 2026 (labels in parentheses):

  ex:hilbert        Hilbert symbols of Q and the product formula
  ex:nak-local      the NAK decomposition of the lower unipotent n-bar(c)
  ex:height-local   H and the norm on n-bar(c)
  ex:hecke-local    the index [K : K_1] = p(p^2 - 1)
  ex:measure-real   area of the modular surface and the two volumes
  ex:nak-global     H(gamma g_z) = (1/2) log Im(gamma_0 z)
  ex:norm-global    the norm of a(p) and of an element of SL(2, Z)
  ex:gl2-center     the signs (y, t)_v in Ad(diag(y, 1))
  ex:unramified-weil  the sign (-1, p)_p and the fixed vector of K_p^*
  lem:classical     Shimura's factor j(gamma, z) = theta(gamma z)/theta(z)
  ex:shimura-lift   Shimura's lift of eta(2z)^12 theta(z)^(-3), weight 9/2

Exact rational or integer arithmetic where possible. Floats only for the
real place and for the theta function."""
import cmath
import math
import random
import sys
from fractions import Fraction as Fr

from padic_lib import vp, hilbert, legendre, INF
from cover_lib import M2, mul, a_, n_, W, beta, in_K, kappa

random.seed(20261118)
FAIL = []


def check(name, ok):
    print(("ok   " if ok else "FAIL ") + name)
    if not ok:
        FAIL.append(name)


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def rand_rat(big=40):
    while True:
        x = Fr(random.randint(-big, big), random.randint(1, big))
        if x != 0:
            return x


# ------------------------------------------------------------ ex:hilbert
check("hilbert: (-1,3)_v = 1, -1, -1 at v = inf, 2, 3",
      [hilbert(-1, 3, v) for v in (INF, 2, 3)] == [1, -1, -1])
check("hilbert: (-1,3)_p = 1 for the other primes",
      all(hilbert(-1, 3, p) == 1 for p in PRIMES if p not in (2, 3)))
check("hilbert: (2,5)_v = 1, -1, -1 at v = inf, 2, 5",
      [hilbert(2, 5, v) for v in (INF, 2, 5)] == [1, -1, -1])
check("hilbert: (-1,-1)_v = -1 exactly at v = inf, 2",
      [v for v in [INF] + PRIMES if hilbert(-1, -1, v) == -1] == [INF, 2])
check("hilbert: (p,u)_p = (u/p) and (p,p)_p = (-1/p) for odd p",
      all(hilbert(p, u, p) == legendre(u, p) for p in (3, 5, 7, 11) for u in range(1, p))
      and all(hilbert(p, p, p) == legendre(-1, p) for p in (3, 5, 7, 11, 13)))


def square_classes(p):
    """Number of classes of Q_p^x / Q_p^x2 separated by Hilbert symbols."""
    reps = [1, -1, 2, -2, 3, -3, 5, -5, 6, -6, 7, -7, 10, -10, 14, -14, p, -p, 2 * p, 3 * p]
    probes = [-1, 2, 3, 5, 7, p]
    return len({tuple(hilbert(r, t, p) for t in probes) for r in reps})


check("hilbert: Q_p^x/Q_p^x2 has 4 classes for p = 3, 5, 7 and 8 for p = 2",
      [square_classes(p) for p in (3, 5, 7, 2)] == [4, 4, 4, 8])
ok = True
for _ in range(500):
    a, b = rand_rat(), rand_rat()
    prod = hilbert(a, b, INF)
    # all primes dividing numerators or denominators are at most 40
    for p in PRIMES:
        prod *= hilbert(a, b, p)
    ok &= prod == 1
check("hilbert: product formula on 500 random pairs", ok)


# ---------------------------------------------- ex:nak-local, ex:height-local
def nbar(c):
    return M2(1, 0, c, 1)


ok = okc = okh = True
for p in (2, 3, 5, 7):
    for _ in range(300):
        c = rand_rat()
        if vp(c, p) > 0:
            continue
        k = M2(0, -1, 1, Fr(1) / c)
        n, a = n_(Fr(1) / c), a_(Fr(1) / c)
        ok &= mul(n, mul(a, k)) == nbar(c) and in_K(k, p)
        # the lifts (g, 1) multiply with trivial cocycles
        okc &= beta(a, k, p) == 1 and beta(n, mul(a, k), p) == 1
        okc &= beta(a, k, INF) == 1 and beta(n, mul(a, k), INF) == 1
        # H = log|1/c|_p = v_p(c) log p <= 0, and the norm is |c|_p
        okh &= vp(Fr(1) / c, p) == -vp(c, p) and -vp(c, p) >= 0
check("nak-local: nbar(c) = n(1/c) a(1/c) k with k in K, for |c|_p >= 1", ok)
check("nak-local: (nbar(c),1) = (n,1)(a,1)(k,1) in the cover (cocycles are 1)", okc)
check("height-local: H(nbar(c)) = -log max(1,|c|_p) = -log ||nbar(c)||_p", okh)

ok = True
for _ in range(500):
    c = random.uniform(-20, 20)
    t = 1 / math.sqrt(1 + c * c)
    # n(x) a(t) k_theta with bottom row (c, 1) = t^{-1} (-sin, cos)
    s, co = -c * t, t
    ok &= abs(s * s + co * co - 1) < 1e-12
    H = math.log(t)
    ok &= abs(H + 0.5 * math.log(1 + c * c)) < 1e-12
    ok &= abs(H) <= math.log(math.sqrt(2 + c * c)) + 1e-12
check("height-local: real place, H(nbar(c)) = -(1/2) log(1+c^2), |H| <= log||.||", ok)

# ------------------------------------------------------------ ex:hecke-local
ok = True
for p in (3, 5, 7):
    cnt = sum(1 for a in range(p) for b in range(p) for c in range(p) for d in range(p)
              if (a * d - b * c) % p == 1)
    ok &= cnt == p * (p * p - 1)
check("hecke-local: [K : K_1] = |SL(2, F_p)| = p(p^2-1); 24 for p = 3", ok)

# ------------------------------------------------------------ ex:measure-real
# hyperbolic area of the standard fundamental domain, by quadrature
N = 200000
area = 0.0
for i in range(N):
    x = -0.5 + (i + 0.5) / N
    area += (1.0 / math.sqrt(1 - x * x)) / N  # int_{sqrt(1-x^2)}^inf dy/y^2
check("measure: area of SL(2,Z)\\H for dx dy/y^2 is pi/3", abs(area - math.pi / 3) < 1e-6)
zeta2 = sum(1.0 / (n * n) for n in range(1, 2000000)) + 1.0 / 2000000
check("measure: (1/2) * (pi/3) * pi = zeta(2) (Tamagawa volume of SL(2,Z)\\SL(2,R))",
      abs(0.5 * (math.pi / 3) * math.pi - zeta2) < 1e-6)
prod = 1.0
for p in range(2, 200000):
    if all(p % q for q in range(2, int(p ** 0.5) + 1)):
        prod *= 1 - 1.0 / (p * p)
check("measure: zeta(2) * prod_p (1 - p^-2) = 1", abs(zeta2 * prod - 1) < 1e-5)
check("measure: the volume for dk of mass 1 and da = dt/|t| is (pi/3)/2 = pi/6",
      abs(area / 2 - math.pi / 6) < 1e-6)


# normalization pass: tau = (6/pi) dg, and the totally real formula
check("measure: Tamagawa = pi * prod_p (1 - p^-2) * dg = (6/pi) dg, so (6/pi)(pi/6) = 1",
      abs(math.pi * prod - 6 / math.pi) < 1e-5)
# k = Q(sqrt 5): |d_k| zeta_k(2) pi^-2 = 2 pi^2 / (15 sqrt 5), with zeta_k = zeta * L(., chi_5)
chi5 = {0: 0, 1: 1, 2: -1, 3: -1, 4: 1}
L2 = sum(chi5[n % 5] / (n * n) for n in range(1, 2000001))
check("measure: L(2, chi_5) = 4 pi^2 / (25 sqrt 5)", abs(L2 - 4 * math.pi ** 2 / (25 * math.sqrt(5))) < 1e-6)
check("measure: Q(sqrt 5): 5 zeta_k(2) / pi^2 = 2 pi^2 / (15 sqrt 5)",
      abs(5 * zeta2 * L2 / math.pi ** 2 - 2 * math.pi ** 2 / (15 * math.sqrt(5))) < 1e-5)
# the same number from the hyperbolic volume 2 zeta_k(-1) (2 pi)^2 = 4 pi^2/15 of SL(2,O_k)\H^2:
# (1/2) * (4 pi^2 / 15) * |d_k|^(-1/2)   (zeta_k(-1) = 1/30)
check("measure: Q(sqrt 5): agrees with (1/2) * 2 zeta_k(-1) (2 pi)^2 / sqrt 5",
      abs(0.5 * 2 * (1 / 30) * (2 * math.pi) ** 2 / math.sqrt(5) - 2 * math.pi ** 2 / (15 * math.sqrt(5))) < 1e-12)

# ------------------------------------------------------------ ex:nak-global
def rand_sl2q():
    while True:
        a, b, c = rand_rat(12), rand_rat(12), rand_rat(12)
        if a != 0:
            return M2(a, b, c, (1 + b * c) / a)


ok = True
for _ in range(400):
    g = rand_sl2q()
    c, d = g[1]
    u, y = random.uniform(-2, 2), math.exp(random.uniform(-2, 2))
    z = complex(u, y)
    # finite places: |t|_p^{-1} = max(|c|_p, |d|_p)
    Hfin = 0.0
    for p in PRIMES:
        vals = [vp(e, p) for e in (c, d) if e != 0]
        Hfin += min(vals) * math.log(p)  # -log max(|c|_p,|d|_p)
    Hinf = 0.5 * math.log(y / abs(complex(c) * z + complex(d)) ** 2)
    # primitive integral vector proportional to (c, d)
    L = math.lcm(c.denominator, d.denominator)
    c0, d0 = int(c * L), int(d * L)
    gg = math.gcd(c0, d0)
    c0, d0 = c0 // gg, d0 // gg
    expect = 0.5 * math.log(y / abs(c0 * z + d0) ** 2)
    ok &= abs(Hfin + Hinf - expect) < 1e-9
check("nak-global: H(gamma g_z) = (1/2) log(y/|c_0 z + d_0|^2), (c_0,d_0) primitive", ok)

# ----------------------------------------------------------- ex:norm-global
ok = True
for p in (3, 5, 7):
    g = a_(p)
    norm_p = max(Fr(p) ** (-vp(e, p)) for row in g for e in row if e != 0)  # max |entry|_p
    norm_inf = math.sqrt(sum(float(e) ** 2 for row in g for e in row))
    ok &= norm_p == p and abs(norm_inf - math.sqrt(p * p + p ** -2)) < 1e-12
    # H(a(p)) = log|p|_p + log|p|_inf = 0
    ok &= abs(-math.log(p) + math.log(p)) == 0 and norm_p * norm_inf > p * p
check("norm-global: ||a(p)|| = p sqrt(p^2 + p^-2) > p^2 while H(a(p)) = 0", ok)
check("norm-global: ||(2 1; 1 1)|| = sqrt 7", abs(math.sqrt(4 + 1 + 1 + 1) - math.sqrt(7)) < 1e-15)

# ------------------------------------------------------------ ex:gl2-center
check("gl2-center: (-1,-1)_inf = -1, so Ad(diag(-1,1)) exchanges the lifts of -1",
      hilbert(-1, -1, INF) == -1)
check("gl2-center: (3,-1)_3 = -1 and (u,-1)_3 = 1 for units u",
      hilbert(3, -1, 3) == -1 and all(hilbert(u, -1, 3) == 1 for u in (1, 2, 4, 5, 7)))

# -------------------------------------------------------- ex:unramified-weil
check("unramified-weil: (-1,p)_p = (-1/p) for odd p",
      all(hilbert(-1, p, p) == legendre(-1, p) for p in (3, 5, 7, 11, 13, 17)))
check("unramified-weil: kappa(n(u)) = kappa(w) = 1 at p = 3, 5, 7",
      all(kappa(n_(u), p) == 1 and kappa(W, p) == 1 for p in (3, 5, 7) for u in (1, 2, Fr(1, 2))))


# -------------------------------------------------------------- lem:classical
def theta(z, terms=60):
    q = cmath.exp(2j * cmath.pi * z)
    return 1 + 2 * sum(q ** (n * n) for n in range(1, terms))


def jacobi(a, n):
    """Jacobi symbol (a/n) for odd n > 0."""
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def shimura_symbol(c, d):
    """Shimura's (c/d) for odd d: (c/|d|), times -1 if c < 0 and d < 0; (0/+-1) = 1."""
    if c == 0:
        return 1
    s = jacobi(c, abs(d))
    return -s if (c < 0 and d < 0) else s


ok = True
tested = 0
while tested < 300:
    c = 4 * random.randint(-12, 12)
    d = random.randint(-25, 25)
    if d % 2 == 0 or math.gcd(c, d) != 1:
        continue
    if c == 0:
        if abs(d) != 1:
            continue
        a, b = d, random.randint(-3, 3)
    else:
        a = next(x for x in range(-400, 401) if (x * d - 1) % c == 0)
        b = (a * d - 1) // c
    z = complex(random.uniform(-0.5, 0.5), random.uniform(0.6, 1.4))
    gz = (a * z + b) / (c * z + d)
    if gz.imag < 0.02:
        continue
    eps = 1 if d % 4 == 1 else 1j
    j = shimura_symbol(c, d) / eps * cmath.sqrt(c * z + d)  # principal branch
    lhs = theta(gz, terms=200)
    ok &= abs(lhs - j * theta(z)) < 1e-8 * max(1, abs(lhs))
    tested += 1
check("classical: theta(gamma z) = eps_d^-1 (c/d) (cz+d)^(1/2) theta(z) on Gamma_0(4)", ok)

# ------------------------------------------------------------- ex:shimura-lift
NQ = 150  # we need a(n^2) for n <= 12


def pmul(A, B):
    C = [0] * NQ
    for i, x in enumerate(A):
        if x:
            for j, y in enumerate(B):
                if i + j >= NQ:
                    break
                C[i + j] += x * y
    return C


def ppow(A, e):
    R = [1] + [0] * (NQ - 1)
    for _ in range(e):
        R = pmul(R, A)
    return R


def pinv(A):
    assert A[0] == 1
    R = [0] * NQ
    R[0] = 1
    for n in range(1, NQ):
        R[n] = -sum(A[k] * R[n - k] for k in range(1, n + 1))
    return R


def euler(step):
    """prod_{n>=1} (1 - q^(step n))."""
    R = [1] + [0] * (NQ - 1)
    n = step
    while n < NQ:
        S = R[:]
        for i in range(NQ - n):
            S[i + n] -= R[i]
        R = S
        n += step
    return R


th = [0] * NQ
th[0] = 1
n = 1
while n * n < NQ:
    th[n * n] = 2
    n += 1
# f = eta(2z)^12 theta(z)^-3 = q prod (1-q^2n)^12 / theta^3, weight 9/2 on Gamma_0(4)
f = [0] + pmul(ppow(euler(2), 12), pinv(ppow(th, 3)))[:NQ - 1]
# F = (eta(z) eta(2z))^8 = q prod (1-q^n)^8 (1-q^2n)^8, weight 8 on Gamma_0(2)
F = [0] + pmul(ppow(euler(1), 8), ppow(euler(2), 8))[:NQ - 1]
check("shimura-lift: F = q - 8q^2 + 12q^3 + 64q^4 - 210q^5 - 96q^6 + 1016q^7 + ...",
      F[1:8] == [1, -8, 12, 64, -210, -96, 1016])
check("shimura-lift: f = q - 6q^2 + 12q^3 - 8q^4 + ... (a(1) = 1)", f[1] == 1)
ok = True
for n in range(1, 13):
    lift = sum(d ** 3 * f[(n // d) ** 2] for d in range(1, n + 1) if n % d == 0 and d % 2 == 1)
    ok &= lift == F[n]
check("shimura-lift: A(n) = sum_{d | n, d odd} d^3 a(n^2/d^2) for n <= 12", ok)
check("shimura-lift: a(9) = A(3) - 27 = -15 and a(25) = A(5) - 125 = -335",
      f[9] == -15 and f[25] == -335 and F[3] == 12 and F[5] == -210)
print("    f =", " ".join("%+dq^%d" % (f[i], i) for i in range(1, 10) if f[i]))

print()
print("%d failed" % len(FAIL))
sys.exit(1 if FAIL else 0)

"""The transfer factor Delta_II near the identity for the biquadratic tori of split G_2.

Setting (paper, Section 7, Proposition 7.6).  T is elliptic with Galois image
Gamma_T = <s_a, s_z> = {1, s_a, s_z, -1} in W(G_2), splitting over K = F(sqrt(d_a), sqrt(d_z)),
where sqrt(d_a) generates the fixed field of s_z and sqrt(d_z) that of s_a.  For Y in t(F),
    a(Y) = sqrt(d_a) u,   z(Y) = sqrt(d_z) v,   u, v in F,
and H = H_2 has roots +-a, +-z.  The claim is that, for Y regular and small,
    Delta_II(exp Y) = c * (P(Y), d_a)_F,   P = b g d e (Y) = (d_z v^2 - d_a u^2)(d_z v^2 - 9 d_a u^2)/16,
where (,)_F is the Hilbert symbol and c is a constant.

Part 1 checks the root-theoretic input exactly (SymPy):
  * the Gamma_T-orbits on the roots outside H, and that each is symmetric with trivial stabilizer;
  * b, g, d, e in terms of a and z, and N_{L/F}(b g) = b g d e = P.
Part 2 evaluates (P(u,v), d_a)_F over Q_p for several biquadratic fields and a grid of (u, v),
and checks the consistency relation (P, d_a d_z)_F = 1 (P is a norm from L = F(sqrt(d_a d_z))).
"""
from fractions import Fraction
import itertools
import sympy as sp

# ---------------- Part 1: root data ----------------
# roots in the basis (alpha, beta)
R = {'a': (1, 0), 'b': (0, 1), 'g': (1, 1), 'd': (2, 1), 'e': (3, 1), 'z': (3, 2)}
R.update({'-' + k: (-v[0], -v[1]) for k, v in list(R.items())})
name = {v: k for k, v in R.items()}
# Euclidean model: alpha = (1,0), beta = (-3/2, sqrt3/2)
s3 = sp.sqrt(3)
vec = lambda c: sp.Matrix([c[0] * 1 + c[1] * sp.Rational(-3, 2), c[1] * s3 / 2])


def refl(r, x):
    rv, xv = vec(R[r]), vec(x)
    out = xv - 2 * (xv.dot(rv) / rv.dot(rv)) * rv
    # back to (alpha, beta) coordinates
    m = sp.Matrix([[1, sp.Rational(-3, 2)], [0, s3 / 2]]).solve(out)
    return (int(m[0]), int(m[1]))


Gamma = {
    '1': lambda x: x,
    's_a': lambda x: refl('a', x),
    's_z': lambda x: refl('z', x),
    '-1': lambda x: (-x[0], -x[1]),
}
outside_H = [k for k in R if k.lstrip('-') not in ('a', 'z')]
orbits, seen = [], set()
for r in outside_H:
    if r in seen:
        continue
    orb = {name[g(R[r])] for g in Gamma.values()}
    seen |= orb
    orbits.append(sorted(orb))
print("Gamma_T-orbits on roots outside H:", orbits)
for orb in orbits:
    r = orb[0]
    stab = [k for k, g in Gamma.items() if g(R[r]) == R[r]]
    pm = [k for k, g in Gamma.items() if g(R[r]) in (R[r], tuple(-c for c in R[r]))]
    neg = name[tuple(-c for c in R[r])]
    print(f"  orbit of {r}: stabilizer {stab}; stabilizer of the pair {{{r}, {neg}}}: {pm}")
assert len(orbits) == 2 and all(len(o) == 4 for o in orbits)

A, Z = sp.symbols('A Z')  # A = alpha(Y), Z = zeta(Y)
lin = lambda c: sp.Rational(1, 2) * ((2 * c[0] - 3 * c[1]) * A + c[1] * Z)  # root c in terms of alpha, zeta
for k in ('b', 'g', 'd', 'e'):
    print(f"  {k}(Y) =", sp.simplify(lin(R[k])))
P = sp.expand(lin(R['b']) * lin(R['g']) * lin(R['d']) * lin(R['e']))
print("  b g d e (Y) =", sp.factor(P))
# sigma restricted to L is s_a (or s_z): s_a(b) = e, s_a(g) = d, so N_{L/F}(b g) = b g d e
assert name[Gamma['s_a'](R['b'])] == 'e' and name[Gamma['s_a'](R['g'])] == 'd'
assert name[Gamma['s_z'](R['b'])] == '-e' and name[Gamma['s_z'](R['g'])] == '-d'
assert sp.expand(P - (Z**2 - A**2) * (Z**2 - 9 * A**2) / 16) == 0
print("  N_{L/F}(b(Y) g(Y)) = b g d e (Y) = (z^2 - a^2)(z^2 - 9 a^2)/16: verified")


# ---------------- Part 2: Hilbert symbols over Q_p ----------------
def val(x, p):
    x = Fraction(x)
    n, d, v = x.numerator, x.denominator, 0
    while n % p == 0:
        n //= p; v += 1
    while d % p == 0:
        d //= p; v -= 1
    return v, Fraction(n, d)


def legendre(x, p):  # x a p-adic unit given as a Fraction
    r = (x.numerator * pow(x.denominator, -1, p)) % p
    return 1 if pow(r, (p - 1) // 2, p) == 1 else -1


def hilbert(a, b, p):  # p odd
    va, ua = val(a, p)
    vb, ub = val(b, p)
    s = (-1) ** ((va * vb * ((p - 1) // 2)) % 2)
    return s * legendre(ua, p) ** (vb % 2) * legendre(ub, p) ** (va % 2)


def nonsquare_unit(p):
    return next(e for e in range(2, p) if legendre(Fraction(e), p) == -1)


for p in (5, 7, 11, 13):
    eps = nonsquare_unit(p)
    fields = {'(eps, p)': (eps, p), '(p, eps)': (p, eps), '(p, eps p)': (p, eps * p), '(eps p, p)': (eps * p, p)}
    grid = [Fraction(m) * Fraction(p) ** k for k in (-1, 0, 1) for m in range(1, p)]
    for label, (da, dz) in fields.items():
        vals = set()
        for u, v in itertools.product(grid, grid):
            Pv = (dz * v * v - da * u * u) * (dz * v * v - 9 * da * u * u) / 16
            assert Pv != 0
            assert hilbert(Pv, da * dz, p) == 1, "P should be a norm from L"
            vals.add(hilbert(Pv, da, p))
        print(f"p={p:2d}  (d_a, d_z)={label:11s}  values of (P, d_a)_F on the grid: {sorted(vals)}"
              + ("   <-- not constant" if len(vals) > 1 else ""))


# Where the sign changes, in the case that both quadratic subfields F(sqrt d_a), F(sqrt d_z) are ramified.
print("\nBoth ramified, d_a = p, d_z = eps p: (P, d_a)_F by region of (v(u), v(v))")
for p in (5, 7, 11, 13, 17, 19, 23):
    eps = nonsquare_unit(p)
    da, dz = p, eps * p
    same, diff = set(), set()
    for m1 in range(1, p):
        for m2 in range(1, p):
            for k1, k2 in itertools.product((0, 1, 2), repeat=2):
                u, v = Fraction(m1) * p**k1, Fraction(m2) * p**k2
                Pv = (dz * v * v - da * u * u) * (dz * v * v - 9 * da * u * u) / 16
                (same if k1 == k2 else diff).add(hilbert(Pv, da, p))
    print(f"  p={p:2d}: v(u) = v(v): {sorted(same)};  v(u) != v(v): {sorted(diff)}")

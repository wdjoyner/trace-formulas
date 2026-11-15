"""Exact independent check: regular cyclic-cubic X can have polar discriminant zero.

Uses SymPy, not Sage or manuscript code. Residue characteristic >=5.
Does not prove the global principal value or Hypothesis (X_3).
"""
import sympy as sp

a, b, z = sp.symbols("a b z")
A = [a, -2*a-b, a+b]  # tau conjugates: alpha, -delta, gamma
Delta = A[0] - A[1]
M = A[0]+A[1]-2*A[2]
D = sp.expand(M**2 + 3*Delta**2)
Q = 3*a**2 + 3*a*b + b**2
assert sp.expand(sum(A)) == 0
assert sp.expand(D - 12*Q) == 0
assert sp.expand(D - 6*sum(u*u for u in A)) == 0

# All six positive G2 roots in the paper's notation.
roots = {
    "alpha": a, "beta": b, "gamma": a+b, "delta": 2*a+b,
    "epsilon": 3*a+b, "zeta": 3*a+2*b,
}
assert sp.expand(roots["gamma"]-A[2]) == 0
assert sp.expand(roots["delta"]+A[1]) == 0
assert sp.expand(roots["beta"]-(A[2]-A[0])) == 0
assert sp.expand(roots["epsilon"]-(A[0]-A[1])) == 0
assert sp.expand(roots["zeta"]-(A[2]-A[1])) == 0

# The discriminant quadric has no root-hyperplane linear factor.
for name, linear in roots.items():
    if name == "alpha":
        assert sp.factor(Q.subs(a,0)) == b**2
    else:
        res = sp.factor(sp.resultant(Q, linear, b))
        assert res != 0
        assert sp.factor(res/a**2) in (1,3,-1,-3), (name,res)
print("PASS: D=12(3a^2+3ab+b^2)=6 Tr(u^2); no root divides D")

# The Kummer eigenline: tau(u)=z*u, tau^2(u)=z^2*u,
# b=(z^2-1)*a and z^2+z+1=0.
cyclotomic = sp.Poly(z*z+z+1,z)
b_eig = (z*z-1)*a
assert sp.rem(sp.Poly(D.subs(b,b_eig),z),cyclotomic).is_zero
for name, linear in roots.items():
    factor = sp.rem(sp.Poly(sp.expand(linear.subs(b,b_eig)/a),z),
                    cyclotomic)
    assert not factor.is_zero
    assert sp.gcd(factor,cyclotomic).degree() == 0
print("PASS: Kummer eigenvector is fully regular and has D=0")

# Q_7: x^3-2 remains irreducible mod 7; zeta_3 reduces to 2 or 4.
assert (2*2+2+1) % 7 == 0
assert {pow(c,3,7) for c in range(1,7)} == {1,6}
mod7 = {name: int(linear.subs({a:1,b:3})) % 7
        for name,linear in roots.items()}
assert all(v!=0 for v in mod7.values())
assert int(D.subs({a:1,b:3})) % 7 == 0
print("PASS: Q_7 example root coefficients modulo 7:",mod7)
# Exact 7-adic vanishing follows from cyclotomic identity, not mod-7 check.

d = sp.sqrt(-3)
for ratio in [(-3+d)/2,(-3-d)/2]:
    assert sp.simplify(Q.subs({a:1,b:ratio})) == 0
    assert all(sp.simplify(f.subs({a:1,b:ratio})) != 0
               for f in roots.values())
print("PASS: exactly two regular, nonzero F-lines if sqrt(-3) is in F")
print("LIMIT: symbolic root algebra only; no LS integral and no (X_3).")

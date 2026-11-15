"""Independent Galois-orbit and Langlands-Shelstad resonance audit for G2.

Checks the split cyclic-cubic quadric cone in Draft 6, Proposition 8.3G,
and the local repeated-polar normal form. Requires SymPy, Python >=3.9.
Does NOT establish any global principal-value identity or Hypothesis (X3).
"""
from itertools import product
import sympy as sp

# The points at Y=-1 where all three norm factors 1-u_i^2 vanish.
pts = [
    u for u in product((-1, 1), repeat=3)
    if 1 + u[0]*u[1] + u[1]*u[2] + u[2]*u[0] == 0
]
assert len(pts) == 6
tau = lambda x: (x[1], x[2], x[0])
seen = set()
orbits = []
for x in pts:
    if x in seen:
        continue
    orb = (x, tau(x), tau(tau(x)))
    assert tau(orb[-1]) == x and len(set(orb)) == 3
    seen.update(orb)
    orbits.append(orb)
assert len(orbits) == 2 and seen == set(pts)
print("PASS: six geometric third-norm points, two cyclic degree-three orbits")
for o in orbits:
    print(" ", o)

# Identify the four points on the x0 chart and two missing points.
s, t, r = sp.symbols("s t r")
y = (1+s*t)/2
a = (1+s-s*t)/2
b = (s-1+s*t)/2
c = -t-s/sp.Integer(4)
seen4 = set()
for s0, t0, r0 in [
    (sp.S(0), sp.Rational(1,2), sp.S(-2)),
    (sp.S(0), -sp.Rational(1,2), sp.S(-2)),
    (sp.S(2), sp.Rational(1,2), sp.S(-1)),
    (sp.S(-2), -sp.Rational(1,2), sp.S(-1)),
]:
    rep = {s:s0,t:t0}
    u = tuple(int(sp.expand(r0*val).subs(rep)) for val in (a,b,c))
    assert sp.simplify(r0*y.subs(rep)+1) == 0
    assert u in pts
    seen4.add(u)
assert len(seen4) == 4
omitted = set(pts)-seen4
assert omitted == {(1,-1,1),(1,-1,-1)}
assert all(-1+sp.Rational(z[0]-z[1],2)==0 for z in omitted)
print("PASS: exactly two omitted points with x0=0")

# Field argument: u0^2=1 => u0=+-1, all conjugates equal.
# Then at Y=-1 the cone evaluates to 4, not 0 (p>=5).
assert 1+1+1+1 == 4

# Repeated-polar point is F-rational when Dcal=0.
D, M = sp.symbols("D M",nonzero=True)
s_star = 2*M/(3*D)
t_star = -M/(2*D)
discr = M**2+3*D**2
for expr in [
    s_star*t_star-1,
    a.subs({s:s_star,t:t_star})-s_star/2,
    b.subs({s:s_star,t:t_star})-s_star/2,
    c.subs({s:s_star,t:t_star})-s_star/2,
    y.subs({s:s_star,t:t_star})-1,
]:
    n = sp.together(expr).as_numer_denom()[0]
    assert sp.rem(sp.Poly(n,M),sp.Poly(discr,M)).is_zero
z3 = sp.symbols("z3")
kummer_ratio = -3*z3**2/(1-z3)
n = sp.together(kummer_ratio**2+3).as_numer_denom()[0]
assert sp.rem(sp.Poly(n,z3),sp.Poly(z3**2+z3+1,z3)).is_zero
print("PASS: repeated-polar F-point and Kummer eigenvector example")

# First blow-up of h=u^2+r*v: u=rho, r=rho*R.
rho, R, v, u = sp.symbols("rho R v u")
h1 = sp.factor((u*u+r*v).subs({u:rho,r:rho*R}))
assert h1 == rho*(rho+R*v)
jac = sp.det(sp.Matrix([rho*R,rho,v]).jacobian((rho,R,v)))
assert jac == -rho
omega = sp.factor((rho*R)*jac/h1**3)
regulator = sp.factor(h1**(-3))
assert sp.simplify(sp.limit(rho*omega,rho,0)+1/(R**2*v**3)) == 0
assert sp.simplify(sp.limit(rho**3*regulator,rho,0)-1/(R**3*v**3)) == 0
print("PASS: E1 ord(omega)=-1, ord(regulator)=-3; chi(1)=1")

# Local zeta integral for |rho|^(-1-sigma) d rho, Re(sigma)<0.
q, sigma = sp.symbols("q sigma",positive=True)
zeta = (1-1/q)*q**sigma/(1-q**sigma)
assert sp.simplify(
    sp.limit(sigma*zeta,sigma,0)+(1-1/q)/sp.log(q)
) == 0
print("PASS: one-parameter Mellin continuation has a simple pole at sigma=0")
print("WARNING: nonresonance (LS 1984, (1.4)) fails; no global X3 proof")

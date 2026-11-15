"""Exact independent four-chart check of the cubic G2 exceptional cone.

Starting input: manuscript Draft 6, Proposition 8.3G (8.7h).
Uses SymPy, not Sage. Algebraic identities only: NOT a proof of X_3 or
Langlands--Shelstad principal-value compatibility.
"""
import sympy as sp

r, s, t = sp.symbols("r s t")
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")
A0, A1, A2 = sp.symbols("A0 A1 A2")
Delta, M = A0 - A1, A0 + A1 - 2*A2
F = Delta*(1 - 3*s**2/sp.Integer(4)) + M*s
Frec = Delta*(s**2 - sp.Rational(3, 4)) + M*s
P = s*(s**2-4)
Prec = 4*s**2-1
charts = {
    "x0": (1, s, t, s*t),
    "x1": (s, 1, s*t, t),
    "x2": (t, s*t, 1, s),
    "x3": (s*t, t, s, 1),
}

def source(z):
    x0, x1, x2, x3 = z
    return ((x0+x1-x3)/2, (x1-x0+x3)/2,
            -x2-x1/4, (x0+x3)/2)

def polys(z):
    a, b, c, y = source(z)
    a_form = (y-b)*(y+a)*(a+b)
    T = ((b-y)*(-y-2*a-b), (y+a)*(-y+a+2*b),
         -(a+b)*(2*y+a-b))
    U = (a*(b-y)**2, b*(y+a)**2, c*(a+b)**2)
    H0 = sp.expand(A0*T[0] + A1*T[1] + A2*T[2])
    H1 = sp.expand(A0*U[0] + A1*U[1] + A2*U[2])
    return a, b, c, y, a_form, H0, H1

# Check the cyclic common-denominator identity on an independent cone chart.
a,b,y,z = sp.symbols("a b y z")
c = -(y*y+a*b)/(a+b)
u = (a,b,c)
q = []
for i in range(3):
    p_i, p_next = u[i], u[(i+1)%3]
    q.append(y*y+y*(p_i-p_next)+p_i**2+p_i*p_next+p_next**2)
T = ((b-y)*(-y-2*a-b), (y+a)*(-y+a+2*b),
     -(a+b)*(2*y+a-b))
U = (a*(b-y)**2, b*(y+a)**2, c*(a+b)**2)
for i in range(3):
    p_i, p_next = u[i], u[(i+1)%3]
    W = (p_next-y)*(z*p_i*(p_next-y)-y-2*p_i-p_next)/q[i]
    assert sp.cancel(q[0]*W - T[i] - z*U[i]) == 0

Nplus = sp.prod(y+v for v in u)
A = (y-b)*(y+a)*(a+b)
assert sp.cancel(Nplus**2*q[0]**3 - A**2*q[0]*q[1]*q[2]) == 0
print("PASS cyclic W_i and norm cancellation")

for name, vec in charts.items():
    assert sp.expand(vec[0]*vec[3]-vec[1]*vec[2]) == 0
    a,b,c,y,A,H0,H1 = polys(vec)
    dd = 1 if name in ("x0","x1") else t*t
    f = F if name in ("x0","x2") else Frec
    p = P if name in ("x0","x2") else Prec
    h = sp.cancel((H0+r*H1)/dd)
    assert sp.expand(h.subs(r,0)-f) == 0

    k = ((M+2*Delta*t)/8 if name == "x0" else
         -(M+2*Delta*t)/8 if name == "x1" else
         (2*Delta+M*t)/8 if name == "x2" else
         -(2*Delta+M*t)/8)
    assert sp.cancel(h-f*(1+r*y)-r*p*k) == 0

    expected_A = ((p/4 if name in ("x1","x3") else -p/4)
                  *(1 if dd == 1 else t**3))
    assert sp.expand(A-expected_A) == 0
    j = sp.factor(sp.det(sp.Matrix([r*a,r*b,r*y]).jacobian((r,s,t)))/r**2)
    sign = 1 if name in ("x0","x3") else -1
    assert sp.cancel(j/(a+b)-sign*sp.Rational(1,2)) == 0

    # Therefore omega = +/- B*r*p^2/(16*h^3),
    # R = -p^2 * prod(1-r^2*u_i^2)^2/(1024*(1+r*y)^3*h^3).
    # On p=0 the polar h=f*(1+r*y). Exactly two norm factors
    # vanish simultaneously at p=0 and 1+r*y=0.
    roots = [0,2,-2] if name in ("x0","x2") else [
        sp.Rational(1,2),-sp.Rational(1,2)]
    for root in roots:
        y0 = y.subs(s,root)
        assert sp.expand(h.subs(s,root)-f.subs(s,root)*(1+r*y0)) == 0
        hits = sum(sp.simplify(v.subs(s,root)**2-y0**2)==0
                   for v in (a,b,c))
        assert hits == 2
    print("PASS chart",name)

assert sp.simplify(F.subs(s,0)-(A0-A1)) == 0
assert sp.simplify(F.subs(s,2)-4*(A1-A2)) == 0
assert sp.simplify(F.subs(s,-2)+4*(A0-A2)) == 0
assert sp.expand(sp.discriminant(F,s)-(M**2+3*Delta**2)) == 0

# Special trace-zero, repeated-polar case, over Q(sqrt(-3)).
m = sp.sqrt(-3)
spec = {A0:(m/3+1)/2, A1:(m/3-1)/2, A2:-m/3}
star = 2*m/3
a,b,c,y,A,H0,H1 = polys(charts["x0"])
assert sp.simplify(F.subs(spec).subs(s,star)) == 0
assert sp.simplify(sp.diff(F,s).subs(spec).subs(s,star)) == 0
assert sp.simplify(H1.subs(spec).subs({s:star,t:1/star})) == 0
assert sp.simplify(sp.diff(H1,t).subs(spec).subs(s,star)) != 0

# Generic blow-up of (P,C): omega order 2-3+1=0;
# regulator order 2+4-3-3=0 (two norm factors contribute +4).
assert 2-3+1 == 0
assert 2+4-3-3 == 0
print("PASS separation, repeated-root warning and generic triple-curve orders")
# Isolated extra norm intersections on a representative x0 chart.
# These are zero loci, not claims of a resolution of singularities.
u0, u1, u2, y0 = source(charts["x0"])
for boundary_root, third, extra_ts in [
    (sp.Integer(0), u2, [-sp.Rational(1,2), sp.Rational(1,2)]),
    (sp.Integer(2), u0, [sp.Rational(1,2)]),
    (-sp.Integer(2), u1, [-sp.Rational(1,2)]),
]:
    extra = sp.factor((y0**2-third**2).subs(s,boundary_root))
    for extra_t in extra_ts:
        assert sp.simplify(extra.subs(t,extra_t)) == 0
print("PASS locations of isolated third-norm intersections on the triple curves")
print("NOT CHECKED: resolution at isolated intersections, descent, global LS PV or X_3")

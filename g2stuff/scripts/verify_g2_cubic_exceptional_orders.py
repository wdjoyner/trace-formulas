"""Exact symbolic checks of the generic cubic exceptional divisor.
Standalone Python 3 + SymPy. No SageMath or repository imports.
Starting point: Proposition 8.3G(b), formula (8.7h), Draft 6.
Checks rational identities, NOT principal values or (X_3).
"""
import sympy as sp

r, a, b = sp.symbols("r a b")
A0, A1, A2, B = sp.symbols("A0 A1 A2 B")
c = -(1 + a*b)/(a + b)
v = [a, b, c]
u = [r*a, r*b, r*c]
Y = r
Q = lambda x,y: Y**2 + Y*(x-y) + x**2 + x*y + y**2
Anum = lambda x,y: (Y-y)*(Y+x)*(x+y)
W = lambda x,y: (y-Y)*(x*y-Y*(x+1)-2*x-y)/Q(x,y)
q = 1+a-b+a*a+a*b+b*b
A = (1-b)*(1+a)*(a+b)
T = [-(b-1)*(1+2*a+b), (1+a)*(-1+a+2*b), -(a+b)*(2+a-b)]
U = [a*(b-1)**2, b*(1+a)**2, -(1+a*b)*(a+b)]
assert sp.cancel(Q(u[0],u[1])/r**2-q) == 0
assert sp.cancel(Anum(u[0],u[1])/r**3-A) == 0
for i in range(3):
    assert sp.cancel(W(u[i],u[(i+1)%3])-(T[i]+r*U[i])/q) == 0
assert sp.expand(sum(T)) == 0
assert sp.expand(sum(U)) == 0
H0 = sp.expand(A0*T[0]+A1*T[1]+A2*T[2])
H1 = sp.expand(A0*U[0]+A1*U[1]+A2*U[2])
Lam = sp.cancel(sum([Ai*W(u[i],u[(i+1)%3])
                     for i,Ai in enumerate([A0,A1,A2])]))
assert sp.cancel(Lam-(H0+r*H1)/q) == 0
S = sp.cancel(Q(u[0],u[1])**3/Anum(u[0],u[1])**2)
assert sp.cancel(S-q**3/A**2) == 0
jac = sp.Matrix([u[0],u[1],Y]).jacobian([r,a,b]).det()
assert sp.factor(jac-r**2) == 0
omega = 2*B*r*A**2/((a+b)*(H0+r*H1)**3)

N = lambda values: sp.prod(values)
qi = [sp.factor(Q(u[i],u[(i+1)%3])/r**2) for i in range(3)]
assert sp.factor(N([1+x for x in v])**2*q**3/N(qi)-A**2) == 0
reg = -A**2*N([1-r**2*x**2 for x in v])**2 / (
    64*(1+r)**3*(H0+r*H1)**3)
assert sp.factor((omega/reg) +
    128*B*r*(1+r)**3/((a+b)*N([1-r**2*x**2 for x in v])**2)) == 0
# Independent check of multiplicative norm pullback before simplification.
reg_raw = (-N([1+x for x in v])**2
    * N([1-r**2*x**2 for x in v])**2*q**3
    / (64*(1+r)**3*N(qi)*(H0+r*H1)**3))
assert sp.factor(reg_raw/reg-1) == 0

point = {a:2,b:3,A0:1,A1:-1,A2:0,B:1}
assert q.subs(point) == 19 and A.subs(point) == -30
assert H0.subs(point) == -37
assert sp.cancel((omega/r).subs(point).subs(r,0)) != 0
assert sp.cancel(reg.subs(point).subs(r,0)) != 0
print("PASS: exact cubic form/regulator pullbacks and ratio cancellation")
print("Generic E orders: form +1, regulator 0, character 0 (tame)")
print("Not checked: global LS principal values, polar intersections, (X_3)")

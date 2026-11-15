"""Independent exact local-resolution checks for G2 cubic cone (2026-11-15).

SymPy only, ordinary Python 3; starting rational formulas in Draft 6 (8.7h).
Checks algebraic local blow-up models, not global Langlands-Shelstad PV or X_3.
"""
import sympy as sp

r,s,t,v=sp.symbols("r s t v")
A0,A1,A2=sp.symbols("A0 A1 A2")
D=A0-A1
M=A0+A1-2*A2
F=D*(1-sp.Rational(3,4)*s*s)+M*s
P=s*(s*s-4)
K=(M+2*D*t)/8
a=(1+s-s*t)/2
b=(s-1+s*t)/2
c=-t-s/4
y=(1+s*t)/2
C=1+r*y
h=F*C+r*P*K

# Repeated polar exact equation and normal-form blow-up Jacobians.
sstar=2*M/(3*D)
tstar=-M/(2*D)
assert sp.simplify(F+sp.Rational(3,4)*D*(s-sstar)**2
                   -(M*M+3*D*D)/(3*D))==0
assert sp.simplify(K-D*(t-tstar)/4)==0
u,rho,R,Z,z,w=sp.symbols("u rho R Z z w")
hm=u*u+r*w
h1=sp.factor(hm.subs({u:rho,r:rho*R}))
assert sp.expand(h1-rho*(rho+R*w))==0
h2=sp.factor(h1.subs({rho:Z*z,R:Z}))
assert sp.expand(h2-Z**2*z*(z+w))==0
jac2=sp.det(sp.Matrix([Z**2*z,Z*z,w]).jacobian((Z,z,w)))
assert sp.factor(jac2-Z**2*z)==0
assert sp.factor((Z**2*z)*jac2/h2**3
                 -1/(Z**2*z*(z+w)**3))==0
print("PASS repeated polar: 2 blow-ups, E1 orders (-1,-3), E2 (-2,-6)")

# Four isolated points and their exact factor patterns.
pts=[(sp.Integer(0),sp.Rational(1,2),sp.Integer(-2)),
     (sp.Integer(0),-sp.Rational(1,2),sp.Integer(-2)),
     (sp.Integer(2),sp.Rational(1,2),sp.Integer(-1)),
     (-sp.Integer(2),-sp.Rational(1,2),sp.Integer(-1))]
expected=[("zw","z","w"),("z","zw","w"),
          ("w","z","zw"),("z","w","zw")]
hz_expected=[2*(A0-A2),2*(A1-A2),-2*(A0-A2),-2*(A1-A2)]
diff_expected=[2*(A1-A2),2*(A0-A2),-2*(A0-A1),2*(A0-A1)]
z0,w0=sp.symbols("z0 w0")
for index,(s0,t0,r0) in enumerate(pts):
    assert sp.simplify(C.subs({r:r0,s:s0,t:t0}))==0
    rs=(v-1)/y
    types=[]
    gzs=[]
    for ai in (a,b,c):
        eps=sp.simplify((r0*ai).subs({s:s0,t:t0}))
        assert eps in (sp.Integer(1),sp.Integer(-1))
        q=1-eps*r*ai
        g=sp.factor(eps*ai+y)
        assert sp.factor((q-v).subs(r,rs)-(1-v)*g/y)==0
        g0=sp.factor(g.subs({s:s0+z0,t:t0+w0}))
        gz=sp.diff(g0,z0).subs({z0:0,w0:0})
        gw=sp.diff(g0,w0).subs({z0:0,w0:0})
        gzw=sp.diff(g0,z0,w0).subs({z0:0,w0:0})
        typ=("z" if gz!=0 and gw==0 else
             "w" if gz==0 and gw!=0 else
             "zw" if gz==gw==0 and gzw!=0 else "FAIL")
        types.append(typ)
        gzs.append(gz)
    assert tuple(types)==expected[index]
    hh=h.subs(r,rs)
    hz=sp.factor(sp.diff(hh,s).subs({s:s0,t:t0,v:0}))
    hv=sp.factor(sp.diff(hh,v).subs({s:s0,t:t0,v:0}))
    assert sp.simplify(hz-hz_expected[index])==0
    nz=types.index("z")
    q_z_slope=gzs[nz]/y.subs({s:s0,t:t0})
    assert sp.simplify(hz-hv*q_z_slope-diff_expected[index])==0
    print("PASS isolated p%d:"%(index+1), types, "noncoincident polar")

# Local incidence model: P=z, C=v, H=v+3z, Nz=v+2z, Nw=v+w, Nzw=v+zw.
nu,L,W,mu,T,ell=sp.symbols("nu L W mu T ell")
# First blow-up z=rho, v=rho*ell.
H1=rho*(ell+3)
Nz1=rho*(ell+2)
Nw1=rho*ell+w
Nzw1=rho*(ell+w)
C1=rho*ell
P1=rho
omega1=sp.factor(P1**2*rho/H1**3)
reg1=sp.factor(P1**2*(Nz1*Nw1*Nzw1)**2/(C1**3*H1**3))
assert omega1==(ell+3)**-3
assert sp.factor(reg1-(ell+2)**2*(ell+w)**2*(rho*ell+w)**2/
                 (ell**3*(ell+3)**3))==0
# Point blow-up rho=nu, ell=nu*L, w=nu*W: extra Jacobian nu**2.
omega2=sp.factor(omega1.subs({ell:nu*L,w:nu*W})*nu**2)
reg2=sp.factor(reg1.subs({rho:nu,ell:nu*L,w:nu*W}))
assert sp.limit(omega2/nu**2,nu,0)==sp.Rational(1,27)
assert sp.simplify(sp.limit(reg2/nu,nu,0)
                   -4*W**2*(L+W)**2/(27*L**3))==0
# Curve blow-up L=mu,W=mu*T: extra Jacobian mu.
omega3=sp.factor(omega2.subs({L:mu,W:mu*T})*mu)
reg3=sp.factor(reg2.subs({L:mu,W:mu*T}))
assert sp.limit(omega3/mu,mu,0)!=0
assert sp.simplify(sp.limit(reg3/mu,mu,0)
                   -4*nu*(T+1)**2*(T+nu)**2/27)==0
assert sp.factor((rho*ell).subs({rho:nu,ell:nu*L}).subs(L,mu))==nu**2*mu
# After final blow-up, strict sections T=-nu and T=-1 are distinct at nu=0.
assert sp.det(sp.Matrix([nu,mu,T+nu]).jacobian((nu,mu,T)))==1
assert sp.det(sp.Matrix([nu,mu,T+1]).jacobian((nu,mu,T)))==1
print("PASS isolated-point model: E_Z (0,0), E_p (+2,+1), E_final (+1,+1)")
print("UNPROVED: global resolution, F-descent, Langlands-Shelstad PV, (X_3)")

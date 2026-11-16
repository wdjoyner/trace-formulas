# Independent exact checks (Claude, Nov 16 2026) of Theorem 7.6H(b), (7.12), Prop. 7.6G(a)
# relations, and the Jacobian identity in the proof of Theorem 7.6H, at random rational points.
from fractions import Fraction as Q
import random, sympy as sp
random.seed(2)
def polys(a,b,wg,wd):
    al,be,ga,de,ep,ze=a,b,a+b,2*a+b,3*a+b,3*a+2*b
    F0=1+be*wg; F1=F0+al*ze*wd; F2=F0+ga*ep*wd
    G=F0*F1*F2-ze*(be*ga*wd-2*F0)*(al*ep*wg*wd-2*de*wd-wg*F0)
    H=ze*(be*ga*wd-2*F0)*(ga*ze*wd-F0)
    return F0,F1,F2,G,H
# point maps (P=(zb,wg,wd,xi,a,b))
def sa(P):
    zb,wg,wd,xi,a,b=P; D=1-3*a*wg-3*a*a*wd
    return (zb/D,(wg+2*a*wd)/D,wd/D,xi,-a,b+3*a)
def sb(P):
    zb,wg,wd,xi,a,b=P; f=1+b*wg
    return (zb,wg/f,wd/f**2,xi+b*zb,a+b,-b)
def UVX(P):
    zb,wg,wd,xi,a,b=P; F0,F1,F2,G,H=polys(a,b,wg,wd)
    return (F1/F0, G/(F0*F1*F2), xi, xi+H/G*zb)
def rnd(): return Q(random.randint(-30,30),random.randint(1,11))
pts=[tuple(rnd() for _ in range(6)) for _ in range(6)]
comp=lambda P: sa(sb(P))   # pullback of (sb* sa*) evaluated: f(sa(sb(P)))
def pw(f,n,P):
    for _ in range(n): P=f(P)
    return P
ok=lambda L: all(L)
print("sa^2=id",ok(sa(sa(P))==P for P in pts),"sb^2=id",ok(sb(sb(P))==P for P in pts),"(sb sa)^6=id",ok(pw(comp,6,P)==P for P in pts))
m1=lambda P: pw(comp,3,P)
for P in pts[:3]:
    print(" (-1) on (a,b):",m1(P)[4:]==(-P[4],-P[5]))
for name,g in (("sa",sa),("-1",m1),("sz",lambda P: m1(sa(P)))):
    res=[]
    for P in pts:
        U,V,x1,x2=UVX(P); U2,V2,y1,y2=UVX(g(P))
        res.append((U2*U==1, U2==U, V2==V, V2*V==1, (y1,y2)==(x1,x2), (y1,y2)==(x2,x1)))
    print(name,"[U->1/U, U fixed, V fixed, V->1/V, xi fixed, xi swapped]:",[all(r[i] for r in res) for i in range(6)])
# Phi_E checks
for P in pts:
    zb,wg,wd,xi,a,b=P; F0,F1,F2,G,H=polys(a,b,wg,wd)
    Q2=m1(P); F0b,F1b,F2b,Gb,Hb=polys(Q2[4],Q2[5],Q2[1],Q2[2])
    assert F1b*F2b/Q2[2]**2==F1*F2/wd**2
print("(-1)*Phi_E=Phi_E ok")
# Jacobian identities, symbolic diff evaluated at points
a,b,wg,wd,zb,xi=sp.symbols('a b wg wd zb xi')
F0,F1,F2,G,H=polys(a,b,wg,wd)
U=F1/F0; V=G/(F0*F1*F2); xi2=xi+H/G*zb; Z=3*a+2*b
M2=[[sp.diff(U,wg),sp.diff(U,wd)],[sp.diff(sp.log(V),wg),sp.diff(sp.log(V),wd)]]
M4=[[sp.diff(f,c) for c in (zb,wg,wd,xi)] for f in (U,V,xi,xi2)]
for P in pts[:4]:
    sub=dict(zip((zb,wg,wd,xi,a,b),[sp.Rational(x.numerator,x.denominator) for x in P]))
    d2=sp.Matrix([[e.subs(sub) for e in r] for r in M2]).det()
    d4=sp.Matrix([[e.subs(sub) for e in r] for r in M4]).det()
    pap=(a*Z*H/(F0**3*F1*F2)).subs(sub); need=(a*Z*H/(F0**2*G)).subs(sub)
    dens=(a*Z/(U-1)**2/V/(xi-xi2)**2).subs(sub)
    print(" det2/paper=",sp.nsimplify(d2/pap)," det2/needed=",sp.nsimplify(d2/need)," (7.12) ratio=",sp.nsimplify(dens*d4*sub[wd]**2*sub[zb]**2))

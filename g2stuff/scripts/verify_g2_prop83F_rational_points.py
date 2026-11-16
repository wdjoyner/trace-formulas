# Independent exact checks (Claude, Nov 16 2026) of Prop. 8.3F(a) (intrinsic coordinates,
# L_X laws) at random rational points, and of the Legendre-symbol values in Example 7.6B(b).
from fractions import Fraction as Q
import random
random.seed(5)
# geometric actions on E_{0,beta,zeta}: P=(za_,wg,wd,we,wz,eta,a,b), za_=z(alpha)
def sa(P):
    z,wg,wd,we,wz,eta,a,b=P; D=1-3*a*wg-3*a*a*wd-a**3*we
    return (z,(wg+2*a*wd+a*a*we)/D,(wd+a*we)/D,we/D,wz/D**2,eta+a*z,-a,b+3*a)
def sb(P):
    z,wg,wd,we,wz,eta,a,b=P; f=1+b*wg
    return (z/f,wg/f,wd/f**2,(we+b*wz)/f**3,wz/f**3,eta,a+b,-b)
def intr(P):
    z,wg,wd,we,wz,eta,a,b=P; al,be,ga,de,ep,ze=a,b,a+b,2*a+b,3*a+b,3*a+2*b
    za=al*z; r=(al*be*wg+al)/ga; nd=(al*al*be*wd-2*al*r)/de
    ne=(al**3*be*we-3*al*nd)/ep
    nz=(al**3*be**2*wz+3*al*r*r-3*(ga*r-al)*nd-be*ne)/ze
    L=ze*nz-3*al*r*r+3*(ga*r-al)*nd+be*ne
    return (za,r,nd,ne,nz,eta),L
def claim_sa(I):
    za,r,nd,ne,nz,eta=I; D=3*nd+ne+3*r-1
    return (-za,(r+2*nd+ne)/D,-(nd+ne)/D,ne/D,(3*nd*nd+3*nd*ne+ne*ne-nz)/D**2,eta+za),D
def claim_sb(I):
    za,r,nd,ne,nz,eta=I
    return (za/r,1/r,-(nd+2*r)/r**2,-(ne+nz-3*r*r)/r**3,(nz-3*r*r+3*r)/r**3,eta)
rnd=lambda: Q(random.randint(-30,30),random.randint(1,9)) or Q(1,3)
pts=[tuple(rnd() for _ in range(8)) for _ in range(8)]
okA=okB=okL1=okL2=inv=True
for P in pts:
    I,L=intr(P)
    I2,L2=intr(sa(P)); C,D=claim_sa(I); okA&=(I2==C); okL1&=(L2==-L/D**2)
    I3,L3=intr(sb(P)); okB&=(I3==claim_sb(I)); okL2&=(L3==L/I[1]**3)
    inv&= sa(sa(P))==P and sb(sb(P))==P
print("involutions",inv,"| 8.3F(a) s_alpha*",okA,"s_beta*",okB,"| L_X laws",okL1,okL2)
# Example 7.6B(b): Legendre of (eps v^2-u^2)(eps v^2-9u^2), eps nonsquare
def leg(x,p): x%=p; return 0 if x==0 else (1 if pow(x,(p-1)//2,p)==1 else -1)
for p in (5,7,11,13,17,19,23,29):
    eps=next(e for e in range(2,p) if leg(e,p)==-1)
    vals={leg((eps*v*v-u*u)*(eps*v*v-9*u*u),p) for u in range(1,p) for v in range(1,p)}
    print(p,sorted(vals),end="; ")
print()

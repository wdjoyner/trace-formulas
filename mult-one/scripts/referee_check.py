# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Exact checks for "Direct comparison of SL(2) with its metaplectic cover", Draft 5.

Checked, with Hilbert symbols over Q_p on random elements of SL(2, Z):
  * the map k -> (k, s_v(k)) of (2.9) is a homomorphism on SL(2, Z_p), p = 3, 5, 7;
  * Lemma 2.3(h): conjugating (n, 1), n upper unipotent, gives sign 1;
  * the formula (w,1)(g,1)(w,1)^{-1} = (w g w^{-1}, (a, -bc)_2) of Remark A.2;
  * the element h of Remark A.2: the conjugation sign is -1 for q = 3, 7, 11
    and +1 for q = 5, 13.
Run: python3 referee_check.py   (standard library only; exits nonzero on failure)
"""
import sys
FAIL = []
from fractions import Fraction as Fr
import random
def val(x,p):
    x=Fr(x); n=x.numerator; d=x.denominator; v=0
    while n%p==0: n//=p; v+=1
    while d%p==0: d//=p; v-=1
    return v, Fr(n,d)
def leg(u,p):
    u=Fr(u); r=(u.numerator*pow(u.denominator,-1,p))%p
    return 1 if pow(r,(p-1)//2,p)==1 else -1
def hil(a,b,p):
    al,u=val(a,p); be,v=val(b,p)
    s=(-1)**(al*be*((p-1)//2))
    if be%2: s*=leg(u,p)
    if al%2: s*=leg(v,p)
    return s
def mul(A,B): return ((A[0][0]*B[0][0]+A[0][1]*B[1][0],A[0][0]*B[0][1]+A[0][1]*B[1][1]),(A[1][0]*B[0][0]+A[1][1]*B[1][0],A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def inv(A): return ((A[1][1],-A[0][1]),(-A[1][0],A[0][0]))
def X(A): return A[1][0] if A[1][0]!=0 else A[1][1]
def beta(A,B,p):
    c=X(mul(A,B)); return hil(c/X(A),c/X(B),p)
def cmul(a,b,p): return (mul(a[0],b[0]), beta(a[0],b[0],p)*a[1]*b[1])
def cinv(a,p): return (inv(a[0]), beta(a[0],inv(a[0]),p)*a[1])
def conj(g,h,p): return cmul(cmul(g,h,p),cinv(g,p),p)
def s(A,p):
    c,d=A[1]
    if c*d!=0 and val(c,p)[0]%2: return hil(c,d,p)
    return 1
def rnd():
    A=((Fr(1),Fr(0)),(Fr(0),Fr(1)))
    for _ in range(6):
        k=Fr(random.randint(-9,9))
        A=mul(A,random.choice([((1,k),(0,1)),((1,0),(k,1))]))
    return tuple(tuple(Fr(x) for x in r) for r in A)
random.seed(1)
for p in (3,5,7):
    # kappa homomorphism on SL2(Z) inside SL2(Z_p)
    bad=0
    for _ in range(3000):
        A,B=rnd(),rnd()
        if beta(A,B,p)*s(A,p)*s(B,p)*s(mul(A,B),p)!=1: bad+=1
    # facts (h)
    n=((Fr(1),Fr(1)),(Fr(0),Fr(1))); badh=0
    for _ in range(2000):
        g=rnd(); g=mul(g,((Fr(p),Fr(0)),(Fr(0),Fr(1,p)))) if random.random()<.5 else g
        if conj((g,1),(n,1),p)[1]!=1: badh+=1
    print(p,"kappa failures",bad,"facts(h) failures",badh)
    if bad or badh: FAIL.append(("kappa/facts(h)",p))
# counterexample to (sc-relation), q=3 mod 4
for p in (3,7,11,5,13):
    e=Fr(1); h=((Fr(-1)+p*e,-e),(Fr(p),Fr(-1))); w=((Fr(0),Fr(-1)),(Fr(1),Fr(0)))
    assert h[0][0]*h[1][1]-h[0][1]*h[1][0]==1
    tr=h[0][0]+h[1][1]; disc=tr*tr-4
    r=conj((w,1),(h,1),p)
    print(p,"disc val",val(disc,p)[0],"s(h)",s(h,p),"s(whw^-1)",s(r[0],p),"conj sign",r[1])
    if val(disc,p)[0]!=1 or r[1]!=(-1 if p%4==3 else 1): FAIL.append(("Remark A.2 element",p))
# general formula (w,1)(g,1)(w,1)^-1 = (w g w^-1, (a,-bc)) for abc != 0
random.seed(2)
w=((Fr(0),Fr(-1)),(Fr(1),Fr(0)))
for p in (3,5,7):
    bad=0;n=0
    for _ in range(3000):
        g=rnd()
        if random.random()<.5: g=mul(g,((Fr(p),Fr(0)),(Fr(0),Fr(1,p))))
        a,b=g[0];c,d=g[1]
        if a*b*c==0: continue
        n+=1
        if conj((w,1),(g,1),p)[1]!=hil(a,-b*c,p): bad+=1
    print(p,"conjugation-by-w formula: tested",n,"failures",bad)
    if bad: FAIL.append(("conjugation formula",p))

print("FAILED:" if FAIL else "all checks passed", FAIL if FAIL else "")
sys.exit(1 if FAIL else 0)

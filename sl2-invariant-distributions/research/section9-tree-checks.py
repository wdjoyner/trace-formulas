from fractions import Fraction as Fr
# Truncated fixed-point (Korman / Schneider-Stuhler) sums on the tree of SL2, split element a(t), t in 1+p^n exactly.
# Fixed tree: apartment positions i in Z; vertices at distance j<=n from apartment hanging at i: N_j=(q-1)q^(j-1) (j>=1), N_0=1.
# type(x) = (i+j) mod 2 ; ball B(o,R): |i|+j<=R.
def N(q,j): return 1 if j==0 else (q-1)*q**(j-1)
def sums(q,n,R):
    St=0; sc=0; pip=0; pim=0; triv=0
    V=0;E=0
    for i in range(-R,R+1):
        for j in range(0,n+1):
            if abs(i)+j>R: continue
            cnt=N(q,j)
            degfix = (q+1) if j<n else 1   # degree in full fixed tree (n>=1)
            typ=(i+j)%2
            V+=cnt
            # edges inside ball: count edge to parent (j>=1) ; apartment edges separately
            if j>=1: E+=cnt
            St += cnt*(degfix-1)
            triv += cnt
            # depth-zero supercuspidal c-Ind_{K_0} sigma, dim sigma=q-1: char q-1 at identity (j<n), -1 at unipotent (j==n)
            if typ==0: sc += cnt*((q-1) if j<n else -1)
            # pi_+ : type0 -> trivial (1), type1 -> St_q ; pi_- opposite
            stq=degfix-1
            pip += cnt*(1 if typ==0 else stq)
            pim += cnt*(stq if typ==0 else 1)
    E += 2*R  # apartment edges inside ball
    return dict(St=St-E, triv=triv-E, sc=sc, pip=pip-E, pim=pim-E)
for q in (3,5,7):
    for n in (1,2,3,4):
        for R in (10,12,20):
            s=sums(q,n,R)
            assert s['St']==2*q**n-1, (q,n,R,s)
            assert s['triv']==1
            assert s['sc']==q**n-1, (q,n,R,s)
            assert s['pip']==q**n and s['pim']==q**n, (q,n,R,s)
print("split checks OK: St=2q^n-1, triv=1, sc=q^n-1, pi_+=pi_-=q^n (R even)")
for q in (3,5):
  for n in (1,2):
    print(q,n,[sums(q,n,R) for R in (11,13)])
# elliptic unramified: fixed set = ball radius n about type-0 vertex
def ell(q,n):
    V0=V1=E=0; St=0;pip=pim=0
    for j in range(n+1):
        cnt=1 if j==0 else (q+1)*q**(j-1)
        deg=(q+1) if j<n else (1 if n>0 else 0)
        if j%2==0: V0+=cnt
        else: V1+=cnt
        if j>=1:E+=cnt
        St+=cnt*(deg-1)
        pip+=cnt*(1 if j%2==0 else deg-1); pim+=cnt*(deg-1 if j%2==0 else 1)
    return St-E, pip-E, pim-E, V0-V1
for q in (3,5):
    for n in range(4):
        St,pp,pm,d=ell(q,n); assert St==-1 and pp+pm==0 and pp-pm==2*d==2*(-q)**n
print("elliptic checks OK: St=-1, pi_+ + pi_- =0, D=2(V0-V1)=2(-q)^n")
# elliptic measure identity  sum_T |W_T|^-1 int_T |D| = 1
for q in (3,5,7,9):
    unr=Fr(q*q-q+1,q*q+q+1); ram=Fr(q,q*q+q+1)
    assert unr+2*ram==1
    print(q,unr,ram)

# Resolution of the repeated-polar and isolated third-norm configurations

**November 15, 2026. Independent auxiliary research note.** Starting rational formulas are Proposition 8.3G, (8.7h), of the corrected G2 Shalika-germ manuscript (Draft 6). All geometric assertions are local, after extension to the splitting field. This does **not** establish (X_3) or the global Langlands–Shelstad principal value.

## Chart data

In the x0=r chart write
\[
y=(1+st)/2,\quad a=(1+s-st)/2,\quad b=(s-1+st)/2,\quad c=-t-s/4,
\quad Y=ry,\quad (u_0,u_1,u_2)=r(a,b,c).
\]
For \(A_i=\tau^i(\alpha(X))\), \(\Delta=A_0-A_1\), \(M=A_0+A_1-2A_2\) and \(B=\beta(X)\epsilon(X)\zeta(X)\), set
\[
F=\Delta(1-3s^2/4)+Ms,\quad P=s(s^2-4),\quad K=(M+2\Delta t)/8,
\quad C=1+ry,\quad h=FC+rPK,\quad N=\prod_{i=0}^2(1-r^2a_i^2).
\]
Then, up to a nonzero constant and orientation,
\[
\omega_{\mathcal Q_3}=\frac{BrP^2}{16h^3}\,dr\wedge ds\wedge dt,\qquad
R_{\mathrm{cone}}=-\frac{P^2N^2}{1024C^3h^3},\qquad
\kappa=c'''\chi(C).
\]

## The repeated-polar case

If \(\mathscr D=M^2+3\Delta^2=0\), take
\(s_*=2M/(3\Delta)\), \(t_*=-M/(2\Delta)\), \(u=s-s_*\) and \(v=t-t_*\).
For regular X the quantity \(P(s_*)\) is nonzero. The **exact** equation is
\[
h=-\frac{3\Delta}{4}u^2(1+ry)+\frac{\Delta}{4}rP(s)v.
\]
A local unit change gives \(h\sim u^2+rv\). Moreover \(C,P,N\) are units, so \(\omega\sim rh^{-3}\,dr\,du\,dv\) and \(R\sim h^{-3}\).

Blow up the smooth curve \((r,u)\), taking \(u=\rho,\ r=\rho R_1\). Then \(h=\rho(\rho+R_1v)\). Blow up the intersection \((\rho,R_1)\), taking \(R_1=\lambda,\ \rho=\lambda z\). Then
\[
r=\lambda^2z,\qquad u=\lambda z,\qquad
h=\lambda^2z(z+v),\qquad
dr\wedge du\wedge dv=\pm\lambda^2z\,d\lambda\wedge dz\wedge dv.
\]
The reduced divisors \(\lambda=0,z=0,z+v=0\) have simple normal crossings. The other blow-up charts have transverse strict transforms. The new exceptional orders are:

| New divisor | order of 3-form | order of regulator | character exponent mod 3 |
|---|---:|---:|---:|
| E1 | −1 | −3 | 0 |
| E2 | −2 | −6 | 0 |

Since \((M/\Delta)^2=-3\), and the cyclic cubic K/F has no quadratic subextension, the repeated-polar parameter \(M/\Delta\) lies in F when this configuration exists; its local centers are F-defined.

## Four third-norm points

The four distinct points in the x0 chart where the third norm factor also vanishes are:

| Point | s | t | r | z-type norm index | w-type | zw-type |
|---|---:|---:|---:|---:|---:|---:|
| p1 | 0 | 1/2 | −2 | 1 | 2 | 0 |
| p2 | 0 | −1/2 | −2 | 0 | 2 | 1 |
| p3 | 2 | 1/2 | −1 | 1 | 0 | 2 |
| p4 | −2 | −1/2 | −1 | 0 | 1 | 2 |

At each, set \(z=s-s_0,\ w=t-t_0,\ v=C=1+Y\). If \(\varepsilon_i=u_i(p)=\pm1\), the vanishing norm factor is \(Q_i=1-\varepsilon_i u_i\), and **exactly**
\[
Q_i-v=\frac{1-v}{y}(\varepsilon_i a_i+y).
\]
The three expressions in parentheses have factors \(z\), \(w\), and \(zw\), respectively, times nonzero units. For regular X the polar is \(h=F(s_0)v+z U_h\), with nonzero \(U_h\) at the point, and its slope differs from the z-type norm slope. This gives the local incidence model (up to units/higher terms)
\[
P=z,\quad C=v,\quad h=v+\alpha z,\quad
Q_z=v+\beta z,\quad Q_w=v+\gamma w,\quad Q_{zw}=v+\delta zw,
\quad \alpha\beta\gamma\delta(\alpha-\beta)\ne0.
\]

Three explicit blow-ups yield a local simple-normal-crossings model:

1. Blow up the smooth curve \(Z=(z,v)\). On \(z=\rho,v=\rho\ell\), the strict character, w-type norm and zw-type norm divisors near the special point are \(\ell=0\), \(\gamma w+\rho\ell=0\), and \(\ell+\delta w=0\). The polar and z-type norm strict transforms meet this exceptional divisor at the *distinct nonzero* sections \(\ell=-\alpha,-\beta\). The generic exceptional orders are \((\operatorname{ord}\omega,\operatorname{ord}R)=(0,0)\), and \(\chi(C)=\chi(\rho)\chi(\ell)\).
2. Blow up the point \((\rho,\ell,w)=(0,0,0)\). On its rho-chart, \(\rho=\nu,\ell=\nu L,w=\nu W\), the three strict sections are \(L=0,\ \gamma W+\nu L=0,\ L+\delta W=0\), meeting along the smooth curve \(L=W=0\). The other two charts are already normal crossings. The new point exceptional has orders \((+2,+1)\), with \(C=\nu^2L\).
3. Blow up \(L=W=0\). On \(L=\mu,W=\mu T\), the two norm sections are \(\gamma T+\nu=0\) and \(1+\delta T=0\), disjoint at \(\nu=0\). On the complementary chart \(W=\mu,L=\mu T\), the character and zw-norm sections are \(T=0\) and \(T+\delta=0\), also disjoint. Remaining sections are transverse to the exceptional components. The final exceptional orders are \((+1,+1)\) and \(C=\nu^2\mu\).

| New exceptional | form order | regulator order | character exponent mod 3 |
|---|---:|---:|---:|
| E_Z | 0 | 0 | 1 |
| E_p | +2 | +1 | 2 |
| E_final | +1 | +1 | 1 |

All differential-form orders include the blow-up Jacobians. The third-norm calculation thus **does not leave a new polar order** on these exceptional components, but the cubic character remains nontrivial.

## Scope and verification

An independent Python 3/SymPy checker verifies the discriminant factorization, repeated-polar blow-up substitutions and Jacobians, exact norm-factor patterns and polar slopes at the four points, and the normal-form blow-up formulas and orders. The complete five-page 12pt Times LaTeX/PDF note is available separately in the accompanying conversation.

**Remaining:** Galois descent of the four local models; global normal-crossings data of the original Igusa compactification; the principal-value compatibility of the actual regulator and character with Langlands–Shelstad; Lemmas 0.8 and 5.14; and (X_3). No changes are made to the Draft 6 main manuscript. AI verification is not human refereeing.

Sources: Joyner, Claude, Gemini, *On the transfer of Shalika germs for G₂*, Draft 6 (2026), §8; Langlands–Shelstad, *On principal values on p-adic manifolds*, LNM 1041 (1984), 250–279.


**Subsequent descent and principal-value audit (2026-11-15).** The four points on this affine chart represent only four of six split-field points, forming two Galois orbits of degree three. The orbitwise resolution descends, but its exceptional fibers have no F-rational points, so no local F-principal-value integral is supported there. In the repeated-polar case the first new exceptional divisor is F-rational and has trivial-character logarithmic pole: Langlands--Shelstad condition (1.4) fails there and the single Mellin regulator has a localized pole. See [cubic-galois-descent-ls-resonance-2026-11-15.md](cubic-galois-descent-ls-resonance-2026-11-15.md). These discoveries do not settle the global integral.

# Cubic \(G_2\) cone: four-chart polar and boundary audit

**November 15, 2026 — independent mathematical note; Draft 6 unchanged.**

**Scope.** Start from the rational identities in Proposition 8.3G, equation (8.7h), of \`revised/g2-shalika-germs-2026.tex\`. Everything below is a rational-function calculation on the split cone. It does not prove the global Langlands–Shelstad principal-value equality or \((X_3)\).

## Coordinates

Over a splitting field write \(u_i=\tau^i(u_0)\) and \(Y^2+u_0u_1+u_1u_2+u_2u_0=0\). Put

\[
x_0=Y+(u_0-u_1)/2,\quad x_1=u_0+u_1,\quad
x_2=-u_2-(u_0+u_1)/4,\quad x_3=Y-(u_0-u_1)/2.
\]

Then \(x_0x_3-x_1x_2=0\). Blow up the vertex. On chart \(x_j=r\), write \((x_0,x_1,x_2,x_3)=r v_j(s,t)\), where

| Chart | \(v_j(s,t)\) | \(y_j=Y/r\) |
|---|---|---|
| \(x_0\) | \((1,s,t,st)\) | \((1+st)/2\) |
| \(x_1\) | \((s,1,st,t)\) | \((s+t)/2\) |
| \(x_2\) | \((t,st,1,s)\) | \((s+t)/2\) |
| \(x_3\) | \((st,t,s,1)\) | \((1+st)/2\) |

Let \(a,b,c\) be \(u_0/r,u_1/r,u_2/r\), respectively. Let \(A_i=\tau^i(\alpha(X))\), \(B=\beta(X)\epsilon(X)\zeta(X)\), \(\Delta=A_0-A_1\), and \(M=A_0+A_1-2A_2\). Define
\[
F(s)=\Delta(1-3s^2/4)+Ms,\qquad F^\vee(s)=\Delta(s^2-3/4)+Ms,
\]
\[
P(s)=s(s^2-4),\qquad P^\vee(s)=4s^2-1,
\quad C_j=1+r y_j,\quad N_j=\prod_{i=0}^2(1-r^2u_{ij}^2).
\]

The exact adapted common-denominator identity for the cyclic conjugates of \(W_\alpha\) is
\[
W_i=(T_i+rU_i)/q_0,\quad
q_0=y^2+y(a-b)+a^2+ab+b^2,
\]
where
\[
\begin{array}{ll}
T_0=(b-y)(-y-2a-b),&U_0=a(b-y)^2,\\
T_1=(y+a)(-y+a+2b),&U_1=b(y+a)^2,\\
T_2=-(a+b)(2y+a-b),&U_2=c(a+b)^2.
\end{array}
\]
The cone identity \(N(y+a)^2q_0^3=[(y-b)(y+a)(a+b)]^2N(q_0)\) cancels the apparent \(q_0\)-poles. In particular the seeming pole along \(x_0=x_1=0\) is removable.

## Exact four-chart formula

Write \(h_j=F_j(s)C_j+rP_j(s)K_j(t)\), with

| Chart | \(F_j\) | \(P_j\) | \(8K_j(t)\) |
|---|---|---|---|
| \(x_0\) | \(F\) | \(P\) | \(M+2\Delta t\) |
| \(x_1\) | \(F^\vee\) | \(P^\vee\) | \(-M-2\Delta t\) |
| \(x_2\) | \(F\) | \(P\) | \(2\Delta+Mt\) |
| \(x_3\) | \(F^\vee\) | \(P^\vee\) | \(-2\Delta-Mt\) |

Direct substitution and Jacobian calculation yield, up to the orientation sign,
\[
\boxed{\pi^*\omega_{\mathcal Q_3}
=\pm\frac{BrP_j(s)^2}{16h_j^3}\,dr\wedge ds\wedge dt,}
\]
\[
\boxed{\pi^*R_{\rm cone}
=-\frac{P_j(s)^2N_j^2}{1024\,C_j^3h_j^3},\qquad
\pi^*\kappa_1(t_*)=c'''\chi(C_j).}
\]
These are **rational identities**, not assertions about principal values. On \(x_2,x_3\), the numerator and the cubic polar denominator both contain a factor \(t^6\), which cancels exactly. The coefficients and Jacobians have been checked symbolically in all four charts.

## Divisors on the vertex exceptional surface \(E:r=0\)

The boundary is the union of three ruling lines \(P_j=0\), and the polar is \(F_j=0\). For pairwise distinct \(A_i\),
\[
F(0)=A_0-A_1,\quad F(2)=4(A_1-A_2),\quad
F(-2)=-4(A_0-A_2).
\]
Consequently **the boundary and polar divisors are disjoint on \(E\)**. At a generic point of \(E\), orders of the actual form and regulator are \(+1,0\); along a generic boundary line their additional orders are \(+2,+2\); along a simple polar line they are \(-3,-3\).

The polar quadratic has discriminant
\[
\mathscr D=M^2+3\Delta^2.
\]
If \(\mathscr D\ne0\), its two ruling components are simple and meet \(E\) transversely. **Special regular \(X\) can have \(\mathscr D=0\)** when \(\sqrt{-3}\) lies in the coefficient field. Then the polar meets \(E\) in a *double* ruling line \(s_*=2M/(3\Delta)\). Under \(A_0+A_1+A_2=0\), its radial derivative on chart \(x_0\) is
\[
(\partial_r h_0)_{r=0,s=s_*}=4\Delta/3-8Mt/9.
\]
It vanishes at \(t_*=3\Delta/(2M)\); the polar has an ordinary quadratic singularity there. This requires further embedded resolution, even if \(X\) is regular.

## Triple intersection curves away from \(E\)

Let \(B=\{P_j=0\}\), \(D=\{h_j=0\}\), \(C=\{1+r y_j=0\}\). On each boundary line \(s=s_b\),
\[
h_j(s_b,t,r)=F_j(s_b)\big(1+r y_j(s_b,t)\big),
\quad F_j(s_b)\ne0.
\]
Therefore \(B\cap D=B\cap C\) set-theoretically, away from \(E\). **These are boundary–polar–character triple intersections.** Along their generic points *two* norm factors \(1-r^2u_{ij}^2\) also vanish simply. On chart \(x_0\):

| \(s_b\) | Pair of vanishing norm factors | Extra zero of third norm factor |
|---|---|---|
| \(0\) | \(i=0,1\) | \(t=\pm1/2\) |
| \(2\) | \(i=1,2\) | \(t=1/2\) |
| \(-2\) | \(i=0,2\) | \(t=-1/2\) |

The other charts give equivalent reciprocal coordinates.

Blow up a generic triple curve \(Z=(P_j,C_j)\). With transverse coordinates \(z=P_j\), \(v=C_j\), the polar \(h_j\) has order \(1\) in the ideal \((z,v)\), and the two norm factors each have order \(1\). The resulting exceptional \(E_Z\) has
\[
\operatorname{ord}_{E_Z}\omega=(2-3)+1=0,\qquad
\operatorname{ord}_{E_Z}R=2+4-3-3=0.
\]
The \(+1\) in the first calculation is the codimension-two blow-up Jacobian. Nevertheless \(\chi(C_j)=\chi(\rho)\chi(v/\rho)\), so the character retains its nontrivial factor along the newly introduced exceptional coordinate \(\rho\).

## Generic divisor table

| Divisor | Fiber-form order | Regulator order | Character |
|---|---:|---:|---|
| Original vertex \(E\) | \(+1\) | \(0\) | trivial near \(E\) |
| Boundary \(P=0\) | \(+2\) | \(+2\) | unit away from \(C\) |
| Polar \(h=0\) | \(-3\) | \(-3\) | unit away from \(C\) |
| Character \(C=0\) | \(0\) | \(-3\) | \(\chi(C)\) |
| Norm \(1\pm ru_i=0\) | \(0\) | \(+2\) | unit away from \(C\) |
| Generic new exceptional \(E_Z\) | \(0\) | \(0\) | \(\chi(\rho)\) |

**Open:** the isolated third-norm-factor points, the repeated-polar case, descent to all \(F\)-rational strata, the remaining original Igusa boundary/spurious divisors, and the global Langlands–Shelstad normal-crossings/principal-value comparison. This work neither establishes Claim 8.3H nor upgrades \((X_3)\).

**References:** D. Joyner–Claude–Gemini, *On the transfer of Shalika germs for \(G_2\)*, Draft 6, §8 (2026); R. Langlands and D. Shelstad, *On principal values on \(p\)-adic manifolds*, Lecture Notes in Math. 1041 (1984), 250–279. **AI review is not independent mathematical certification.**

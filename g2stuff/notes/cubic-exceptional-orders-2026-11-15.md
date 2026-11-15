# Orders of the actual cubic fiber form, character, and regulator at the exceptional divisor

*Independent computation, 2026-11-15. Companion to Draft 6; not a revision of the principal paper.*

## Scope

Use the **actual** formulas in Proposition 8.3G(b), (8.7h), of
[\`g2-shalika-germs-2026.tex\`](../revised/g2-shalika-germs-2026.tex).
Assume those starting formulas. We calculate along the blow-up of the singular vertex of
\[
\mathcal C_K:\ Y^2+u_0u_1+u_1u_2+u_2u_0=0,\quad
u_i=\tau^i(u_0).
\]
The generic exceptional divisor is \(E\simeq\mathbb P^1\times\mathbb P^1\).
Orders are invariant under a separable splitting-field extension, so work on
the chart \(Y=r,\ (u_0,u_1,u_2)=r(a,b,c)\), where
\(c=-(1+ab)/(a+b)\). The exceptional divisor is \(r=0\).

## Exact pullback formulas

Set
\[
q=1+a-b+a^2+ab+b^2,\quad
A=(1-b)(1+a)(a+b),\quad B=\beta(X)\epsilon(X)\zeta(X).
\]
Let \(A_0,A_1,A_2\) be the three conjugates of \(\alpha(X)\). Define
\[
\begin{aligned}
(T_0,T_1,T_2)&=(-(b-1)(1+2a+b),\ (1+a)(-1+a+2b),\
 -(a+b)(2+a-b)),\\
(U_0,U_1,U_2)&=(a(b-1)^2,\ b(1+a)^2,\ -(1+ab)(a+b)),\\
H_0&=\sum_i A_iT_i,\qquad H_1=\sum_i A_iU_i .
\end{aligned}
\]
Direct substitution into (8.7h) gives
\[
Q_0=r^2q,\qquad A_{\mathrm{num}}=r^3A,\qquad
S_F=q^3/A^2,\qquad
W_i=(T_i+rU_i)/q,\qquad
\Lambda_F=(H_0+rH_1)/q.
\]
Since
\[
du_0\wedge du_1\wedge dY
 =r^2\,dr\wedge da\wedge db,\qquad
u_0+u_1=r(a+b),
\]
the **actual cubic fiber 3-form** is, up to its orientation sign,
\[
\boxed{\displaystyle
\pi^*\omega_{\mathcal Q_3} =
\pm\frac{2B\,r A^2}{(a+b)(H_0+rH_1)^3}
\,dr\wedge da\wedge db .}
\]

For the norm regulator, put
\(\mathcal N(1-r^2a^2)=\prod_{v\in\{a,b,c\}}(1-r^2v^2)\).
Writing \(q_0=q\), its conjugates satisfy
\[
q_1=\frac{(1+b)^2q}{(a+b)^2},\qquad
q_2=\frac{(a-1)^2q}{(a+b)^2},
\]
and
\[
\mathcal N(1+a)=-\frac{(a^2-1)(b^2-1)}{a+b},\qquad
\boxed{\ \mathcal N(1+a)^2\frac{q^3}{q_0q_1q_2}=A^2\ }.
\]
The \(r^6\) terms in \(\mathcal N(Y+u_0)^2\) and
\(\mathcal N(Q_0)\) cancel. The norm identity then reduces the
**actual Igusa regulator** exactly to
\[
\boxed{\displaystyle
\pi^*R_{\mathrm{cone}}
=-\frac{A^2\mathcal N(1-r^2a^2)^2}
{64(1+r)^3(H_0+rH_1)^3}.}
\]
Finally the **actual cubic character** in (8.7h) is
\(\pi^*\kappa_1(t_*)=c'''\omega_{K/F}(1+r)\).
For an unramified or tamely ramified cyclic cubic extension,
\(\omega_{K/F}(1+r)=1\) for sufficiently small \(r\).

Dividing the two exact rational expressions exhibits a stronger cancellation:
\[
\boxed{\displaystyle
\frac{\pi^*\omega_{\mathcal Q_3}}
{\pi^*R_{\mathrm{cone}}}
=\mp\frac{128B\,r(1+r)^3}
{(a+b)\mathcal N(1-r^2a^2)^2}\,dr\wedge da\wedge db.}
\]
Thus their *shared* cubic denominator \((H_0+rH_1)^3\),
which contains the \(\Lambda_F\)-dependence, cancels.

## Generic exceptional orders

On the dense open set of \(E\) where \(A\ne0\), \(H_0\ne0\),
and \(a+b\ne0\), the leading regulator coefficient is
\[
R_E=-\frac{A^2}{64H_0^3}\ne0.
\]
Therefore the generic divisorial orders are

| Pullback | \(\operatorname{ord}_E\) |
|---|---:|
| Fiber form \(\pi^*\omega_{\mathcal Q_3}\) | **+1** |
| Regulator \(\pi^*R_{\mathrm{cone}}\) | **0** |
| Cubic character \(\pi^*\kappa_1(t_*)\) | **0**, locally constant |
| Regulated density \(\lvert R_{\mathrm{cone}}\rvert^{\sigma/3}\lvert\omega_{\mathcal Q_3}\rvert\) | **+1** |

For an algebraic nonvanishing witness over the split coefficient field,
\(a=2,b=3,c=-7/5,(A_0,A_1,A_2)=(1,-1,0)\) gives
\(q=19,A=-30,H_0=-37\).

## Crucial remaining polar intersection

Let \(D\) be \(H_0+rH_1=0\). At a smooth point of \(E\cap D\)
where \(D\) is transverse to \(E\), and all remaining rational factors
are units, **both** the form and regulator have order **−3** along \(D\).
With \(h=H_0+rH_1\) as a second coordinate the regularized density
has local form
\[
|r|\,|h|^{-3-\sigma}|dr\,dh\,dt|
\quad\times\quad\text{a nonvanishing analytic factor}.
\]
The generic *radial* integral \(\int |r|\,dr\) converges. The \(h\)-integral
still requires the Langlands–Shelstad principal-value prescription.

This computation does **not** prove \((X_3)\) or Claim 8.3H.
It does **not** check the global fiberwise factorization or the boundary
strata on other blow-up charts, nor Lemmas 0.8 and 5.14. In particular,
one must still test the zeros and poles of \(R_E\), the proper transforms
of the polar and Igusa boundary divisors, and the order of integration/
meromorphic continuation.

**Reproduction:** \`python3 scripts/verify_g2_cubic_exceptional_orders.py\`
from \`g2stuff/\`. The script independently verifies the rational identities,
not the Langlands–Shelstad analytic construction.

Prepared by ChatGPT (OpenAI) from Draft 6. AI review is not independent
mathematical certification. See the project revision log.
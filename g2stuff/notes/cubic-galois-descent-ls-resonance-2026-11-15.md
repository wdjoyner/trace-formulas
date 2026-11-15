# Cubic Galois descent and Langlands–Shelstad resonance audit

**November 15, 2026. Independent auxiliary note. The principal paper remains Draft 6.**

This note follows the four-chart and special-local-resolution calculations in Proposition 8.3G (8.7g–h) of the corrected G2 Shalika-germ manuscript. It gives two distinct results: the geometric third-norm points do not lie on the F-rational locus, whereas the repeated-polar case can produce an F-rational **resonant** exceptional divisor. The latter is an obstruction to applying the proposed one-parameter principal value, not a disproof of Hypothesis (X3).

## 1. Six geometric points in two degree-three orbits

Let K/F be a cyclic cubic field extension, τ its Galois generator, u_i=τ^i(u_0), and Y in F. The cone is

\[
 Y^2+u_0u_1+u_1u_2+u_2u_0=0.
\]

The third-norm points satisfy Y=-1 and 1-u_0²=1-u_1²=1-u_2²=0. Over K they are the six sign triples with not all signs equal. They form exactly two cyclic orbits:

\[
 \mathcal O_+=\{(-1,1,1),(1,1,-1),(1,-1,1)\},
\]
\[
 \mathcal O_-=\{(1,-1,-1),(-1,-1,1),(-1,1,-1)\}.
\]

The earlier x0-chart lists only four: the omitted points (1,-1,-1) and (1,-1,1) have x0=Y+(u0-u1)/2=0. Each Galois orbit descends to a reduced closed point of degree 3, with residue field K.

**There are no F-rational points on either orbit.** If u0²=1 in the *field* K, then u0=±1 and all three conjugates coincide. With Y=-1 the cone would give 1+3=4=0, impossible for residue characteristic at least 5. In fact the three geometric boundary components Y-u1=0, Y+u0=0, and u0+u1=0 contain no F-points off the vertex: the first two force u0 in F and 4Y²=0, while the last implies τ(u0)=-u0 and hence u0=0.

**Descent.** The union of the two orbits and the unions of the corresponding Galois-conjugate blow-up centers are Galois-invariant. The special-point blow-ups and their intrinsic non-normal-crossings centers can be performed equivariantly (locally wherever those centers are disjoint). Blow-ups commute with flat base change (Stacks Project, Lemma 31.33.3, Tag 0805). Since an F-point of a blow-up maps to an F-point downstairs, none of the exceptional fibers over these degree-three closed points has an F-rational point. Consequently there is no local *F-analytic principal-value integral* supported near those exceptional fibers. Formal character exponents computed on K-split charts must not be treated as separate cubic characters on K-points.

## 2. Repeated-polar case is F-rational

Set A_i=τ^i(α(X)), Δ=A0-A1 and M=A0+A1-2A2. Suppose X is regular and

\[
 \mathscr D=M^2+3\Delta^2=0.
\]

Then (M/Δ)²=-3. A cubic field extension cannot contain a new quadratic subfield, so M/Δ already belongs to F. The repeated-polar singular point has s*=2M/(3Δ), t*=-M/(2Δ), and s*t*=1. On the vertex exceptional quadric, at this point,

\[
 Y/r=1,\qquad u_0/r=u_1/r=u_2/r=s_*/2.
\]

Thus it is F-rational. The condition is algebraically attainable for cyclic trace-zero triples: if μ3 is in F, take a Kummer cubic K=F(θ) with τθ=ζ3θ and α(X)=θ, for which (M/Δ)²=-3. Whether every manuscript regularity hypothesis permits such an X still merits explicit verification.

## 3. Exact Langlands–Shelstad obstruction

Use the local model from the previous note, h=u²+rv, with the other factors units. The actual form, regulator and character are

\[
 \omega\sim r h^{-3}\,dr\wedge du\wedge dv,\qquad
 R_{\rm cone}\sim h^{-3},\qquad \chi(Y+1)=1.
\]

On the first blow-up u=ρ and r=ρR1,

\[
 h=\rho(\rho+R_1v),\qquad
 dr\wedge du\wedge dv=\pm\rho\,d\rho\wedge dR_1\wedge dv.
\]

At generic F-points of the new exceptional divisor E1 (R1 and v units),

\[
 \operatorname{ord}_{E_1}\omega=-1,\qquad
 \operatorname{ord}_{E_1}R_{\rm cone}=-3,\qquad \chi(Y+1)=1.
\]

Langlands–Shelstad's condition (1.4), in their article *On principal values on p-adic manifolds* (1984), explicitly excludes a **trivial** multiplicative character with exponent c=0 in dρ/ρ. Here c=ord(ω)+1=0. Therefore their local principal value is *not defined by the cited construction* on this exceptional divisor. Their blow-up invariance Lemma 1.D does not apply either.

Inserting the manuscript's proposed single Mellin factor |R_cone|^(σ/3) yields the radial factor

\[
 \int_{|\rho|\le q^{-m}}|\rho|^{-1-\sigma}\,d\rho
 =(1-q^{-1})\frac{q^{m\sigma}}{1-q^\sigma}\quad(\Re\sigma<0).
\]

The right-hand side has a simple pole at σ=0 with residue -(1-q^-1)/log q; the local coefficient is nonzero because the cubic character equals 1 and the absolute measure is positive on a small enough chart. The second blow-up does **not** eliminate the exceptional valuation responsible for this pole.

One could introduce an independent regulator |ρ|^z and take a Laurent finite part, but that finite part depends on the scaling of ρ unless one specifies invariant subtraction data. Consequently merely saying “take the finite part” is not a replacement for Langlands–Shelstad's coordinate-independent principal-value construction.


## 3a. Where the usual local principal value *does* apply

At generic smooth F-rational points of the polar divisor, with character locally constant and ord(ω)=-3, ord(R)=-3, choose a transverse F-coordinate x=h. The shell computation is

\[
 \int_{|x|\le q^{-m}} |x|^{-3-\sigma}\,dx
 =(1-q^{-1})\frac{q^{m(2+\sigma)}}{1-q^{2+\sigma}}.
\]

This is initially convergent for Re(σ)<-2 and holomorphic by continuation at σ=0. Its value is (1-q^-1)q^(2m)/(1-q²), or -q/(q+1) for m=1. The Langlands–Shelstad monomial exponent is c=-2 and the trivial character is nonresonant.

At a generic point of the character divisor C={Y+1=0} away from the polar divisor, choose x=Y+1. The normal integral of χ(x)|x|^-σ is, for an unramified cubic character,

\[
 (1-q^{-1})\frac{(\chi(\varpi)q^{\sigma-1})^m}
 {1-\chi(\varpi)q^{\sigma-1}},
\]

and it is zero shellwise for a ramified cubic character. Both are holomorphic at σ=0. This is a valid application of Langlands–Shelstad Lemma 1.A for the **isolated transverse normal integrals**, with locally constant tangential unit factors. It is **not** a statement about F-rational character–polar intersections or globally interchanging the remaining fiber integrations. The full typeset five-page note includes the detailed derivation.

## 4. Conclusions and scope

- **Positive descent result:** all six third-norm points form two degree-three closed orbits; the associated blow-ups descend, but their exceptional fibers have no F-rational points and cannot contribute local F-principal-value terms.
- **Negative principal-value finding:** repeated-polar E1 is a trivial-character logarithmic pole, failing the Langlands–Shelstad nonresonance requirement. The proposed single Mellin parameter has a genuine localized pole at zero.
- **Still unresolved:** whether the repeated-polar case is excluded by an additional condition on the *actual* regular X in the original Igusa fiber; a coordinate-independent replacement regularization if it is not excluded; possible global cancellations; remaining F-rational character/polar strata; the original Igusa compactification, Lemmas 0.8/5.14 and Hypothesis (X3).
- Langlands–Shelstad (1984) explicitly assume characteristic-zero local fields. The argument above only asserts their principal-value theorem under that hypothesis; an equal-characteristic extension requires a separate source or proof.

The companion checker verifies the six points, both cyclic orbits, the missing x0-chart points, an algebraic repeated-polar example, the blow-up valuation, the simple Mellin pole, and the list of local resonance candidates. It checks algebra, **not** any global principal-value equality.

### Sources

- D. Joyner, Claude, Gemini, *On the transfer of Shalika germs for G2*, Draft 6 (2026), Proposition 8.3G (8.7g–h), Claim 8.3H.
- Langlands–Shelstad, *On principal values on p-adic manifolds*, LNM 1041 (1984), §1, especially (1.4), Lemmas 1.A, 1.D, and Corollary 1.E. Original PDF: https://www.sunsite.ubc.ca/DigitalMathArchive/Langlands/pdf/prin2-ps.pdf
- Stacks Project, Lemma 31.33.3 (Tag 0805): https://stacks.math.columbia.edu/tag/0805

**This AI-aided note is not an independent human referee certification.** The Draft 6 main manuscript is unchanged.

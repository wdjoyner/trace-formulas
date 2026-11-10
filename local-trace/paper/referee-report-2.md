# Referee Report

Manuscript: Simple local trace formulas for unramified \\(p\\)-adic groups — Revised, corrected and updated\
Authors: David Joyner and Claude\
Version: November 10, 2026

## 1. Overall assessment

Recommendation: Major revision before circulating this as a mathematically verified correction of the original paper.

This is an ambitious and potentially valuable revision. The treatment is substantially more informative than a conventional errata document, especially in its attempt to separate established results, conditional assertions, and conjectural extensions.

I particularly welcome three features: the replacement of the original lattice-point argument by Brion's theorem, the recognition that a truncated spectral kernel need not converge to a purely absolutely continuous spectral measure, and the explicit rank-one examples involving \\(PGL(2)\\) and \\(SL(2)\\).

Nevertheless, I have found a substantive error in the general reductive-group formulation, as well as a separate problem in the periodic-family machinery. There are also proof steps that need more justification before the principal higher-rank results can be accepted.

The distinction I would emphasize is between the rank-one calculations, which provide useful concrete evidence and in places admit direct proofs, and the general higher-rank results, whose present arguments are not yet sufficiently complete.

I do not recommend abandoning the approach. I recommend repairing its mathematical foundations and narrowing the claims where necessary.

## 2. Major mathematical issues

### M1. The extension from semisimple to reductive groups is not justified

Correction required

This affects the introduction, §2, the truncation construction, and Theorem 4.5.

The 1992 paper explicitly assumes that \\(G\\) is a connected unramified semisimple group.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://msp.org\&sz=32)

MSP

&#x20;The new manuscript frequently assumes only that \\(G\\) is reductive.



The distinction matters.

In (2.9), the spherical transform is defined by

\\[ f^\vee(\chi)=\int\_{G(F)^1}f(g)\Gamma\_\chi(g^{-1})\\,dg, \\]

although \\(f\\) belongs to the spherical Hecke algebra of \\(G(F)\\), not necessarily of \\(G(F)^1\\).

For a concrete counterexample, take \\(G=GL(2,F)\\), let \\(K=GL(2,\mathcal O)\\), and put

\\[ f=\mathbf 1\_{\pi I_2K}. \\]

Since \\(G(F)^1=\\{g:|\det g|=1\\}\\), the support of \\(f\\) is disjoint from \\(G(F)^1\\). Consequently,

\\[ f^\vee(\chi)=0 \\]

for every \\(\chi\\). But \\(f(\pi I_2)=1\\).

Thus the inversion formula in Corollary 2.3, as stated for all \\(g\in G(F)\\), is false.

The quotient by central cocharacters in (3.3), the choice of double-coset representatives, and the use of \\(G(T)\\) also require more care when the split center is noncompact.

Recommended correction: For this revision, I would restore the original semisimple hypothesis throughout the main argument. A subsequent extension to reductive groups could be developed using a consistent treatment of central characters, \\(G(F)^1\\), and the quotient by the split center.

This is a relatively economical repair that preserves the central examples and much of the intended theory.

### M2. Lemma 2.8 is false as stated

Counterexample

This is a particularly concrete problem in the subsection on \\((G,M)\\)-families.

The lemma asserts the existence of a smooth compactly supported \\(u_B\\) such that

\\[ \sum\_{r\in L^\vee} \frac{u_B(\lambda+r)}{\theta_B(\lambda+r)} = \frac1{\widetilde\theta_B(\chi\_\lambda)}. \\]

Consider \\(G=PGL(2)\\). Use the manuscript's notation

\\[ X\_\*(A)=\mathbb Z\varpi^\vee,\qquad \alpha^\vee=2\varpi^\vee. \\]

Writing \\(z=\chi\_\lambda(\varpi^\vee(\pi))\\), we have

\\[ \widetilde\theta_B(\chi\_\lambda)=1-z^2. \\]

Its reciprocal has a pole at \\(z=-1\\), corresponding to

\\[ \lambda_0=\frac{\pi i}{\log q}. \\]

However, the period lattice in the chosen coordinate is

\\[ L^\vee=\frac{2\pi i}{\log q}\mathbb Z. \\]

The linear factor \\(\theta_B(\lambda+r)\\) is proportional to \\(\lambda+r\\). None of these factors vanishes at \\(\lambda_0\\) for \\(r\in L^\vee\\).

Consequently, for smooth compactly supported \\(u_B\\), the left-hand side is smooth near \\(\lambda_0\\), while the right-hand side has a pole.

The asserted identity is therefore impossible.

The obstruction comes from the fact that the coroot lattice need not be saturated in \\(X\_\*(A)\\). The periodic denominator has singular hyperplanes not obtained merely by translating the linear denominator through \\(L^\vee\\).

Recommended correction: Remove Lemma 2.8 in its present form, or reformulate it using the appropriate affine coroot hyperplane arrangement and lattice covering. Lemma 2.9 must then be reconsidered.

Although §2.5 says that these lemmas are not used in the main proof, §7.4 explicitly invokes Lemma 2.8. That reference should also be removed until the corrected construction is established.

### M3. Proposition 3.6: the higher-rank proof needs additional justification

I regard the replacement of the original Lemma 3.5 by Brion's vertex decomposition as a promising improvement.

The underlying mathematical idea is sound: a lattice-point generating function for a polytope can be expressed as a sum of rational generating functions of its tangent cones. This is precisely the setting of Brion's theorem.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



However, I am not yet prepared to accept the full proof of Proposition 3.6 in higher rank.

The issue is not that I have found a counterexample to the proposition. Rather, several steps need to be promoted from assertions into fully documented lemmas.

Step 1: The partition into regions \\(S_P\\) and finitely many cosets of \\(X\_\*(A_M)\\) appears reasonable. It would help to prove explicitly that the chosen representatives and the coefficients are independent of \\(T\\).

Step 2: The derivation from Casselman's asymptotics depends on the uniformity in the unramified parameter \\(\chi\\) and on the precise use of opposite-parabolic Jacquet modules. Remark 2026 concerning (3.1) acknowledges that the required version has not been fully checked. This is an essential input, not merely an editorial detail.

Step 3: The reduction to the polytopes \\(\Pi\_{P,e}(T)\\) uses positivity of coefficients involving projections of fundamental weights. That positivity should be stated and proved as a separate root-system lemma.

Step 4: The treatment of half-open faces and their contribution to the \\(T\\)-independent rational functions should be supplied in full. The present discussion appeals to standard inclusion–exclusion, but the higher-rank bookkeeping is part of what makes the result nontrivial.

The manuscript acknowledges that the new argument has only been checked thoroughly in rank one.

My assessment: Proposition 3.6 is plausible, but its proof is incomplete at the level expected for a general theorem. I would add a detailed rank-two example for \\(SL(3)\\), preferably with an independent lattice-point computation, before claiming that the higher-rank argument is established.

### M4. Proposition 4.2 and the passage to the spectral measure

Proposition 4.2 is another important improvement over the 1997 version.

Defining \\(I(\chi,\phi)\\) as the constant coefficient of the nonoscillating part of \\(I^T\\) is conceptually cleaner than asserting that the truncated kernel itself is independent of \\(T\\).

However, the proof of part (b) contains a nontrivial confluence argument.

The statement that analyticity of the total sum, together with uniqueness of exponential-polynomial expansions, yields polynomial coefficients with the asserted rational dependence requires a more explicit proof.

A natural method would be to use a finite-dimensional exponential-polynomial space and confluent Vandermonde matrices, carefully controlling collisions among the frequencies

\\[ \chi(\mu(T)). \\]

That would make the definition of \\(P_0(0;\chi,\phi)\\) much more secure.

There is also an inconsistency in the introduction. It states that Proposition 4.2 establishes \\(G\\)-admissibility of \\(\phi\mapsto I(\chi,\phi)\\). But Proposition 4.2 only establishes \\(K\\)-conjugation invariance, and Remark 2026 explicitly acknowledges that full \\(G\\)-admissibility has not been proved.

The introduction should be corrected accordingly.

## 3. Theorem 4.5 and Conjecture 4.6

I find the corrected formulation of Theorem 4.5 more satisfactory than the unconditional assertion attributed to the 1997 version.

In particular, the proof of part (b), conditional on Hypothesis (R), is convincing in its essential analytic mechanism.

If the oscillatory coefficients multiplied by the Plancherel density are smooth, their Fourier coefficients decay faster than any power. This controls the polynomial dependence on the truncation parameter and allows the nonzero frequencies to disappear in the limit.

That is an effective argument.

There are two matters I would clarify.

First, (R) is a strong assumption involving smoothness of individual coefficients. It should not be presented as a routine technical regularity condition. The \\(SL(2)\\) example demonstrates that it contains real representation-theoretic information.

Second, the manuscript should distinguish more consistently between a functional on Satake transforms, a distribution on the unitary character torus, and a finite complex measure.

A spectral functional need not automatically be representable by a measure. Conjecture 4.6(a) asserts such a representation, so its general existence cannot also be treated as proved elsewhere in the manuscript.

The comments in §7.4 claiming that Arthur's formula already provides an unconditional proof of this conjecture go further than the argument in §7.3 establishes.

I would retain Conjecture 4.6, but rewrite §7.4 as a proposed route to proving it.

## 4. The worked examples in §6

Strongest part of the revision

I independently checked several of the key rank-one identities algebraically. I did not have the separate Python scripts referenced by the manuscript, so this is not an independent certification of their implementations.

### The \\(PGL(2)\\) example

The spherical-function normalization, including

\\[ Q_G=1+q^{-1}, \\]

is consistent with the rank-one Plancherel formula.

The proposed formulas for the three classes of regular elliptic elements are also algebraically consistent with the stated tree counts.

In particular, the rational kernel for type \\((R')\\), despite its somewhat unusual appearance, agrees with the result obtained by summing the corresponding spherical-function series.

I found no arithmetic error in these formulas.

The assertion that Hypothesis (R) holds for \\(PGL(2)\\) is supported by the cancellation of the poles against the Plancherel density. To establish (R) exactly as formulated, the proof should explicitly pass from the orbital kernels \\(I^T(\chi,\gamma)\\) to arbitrary admissible test functions \\(\phi\\).

### The \\(SL(2)\\) example

This is arguably the most interesting new mathematical contribution.

I checked symbolically the identity

\\[ I(\chi,\gamma)=\frac12 I\_{\mathrm{st}}(\chi) \\]

using the two rational expressions in (6.6) and Proposition 6.4.

The decomposition

\\[ O\_\gamma(f) = \int f^\vee(\chi)I(\chi,\gamma)\\,d\mu(\chi) +\frac12 f^\vee(\chi_0) \\]

is also consistent with the stated spherical transforms and orbital-integral counts.

For example, in the \\(q=3\\) case and \\(f_1=\mathbf1\_{Ka_1K}\\),

\\[ f_1^\vee(\chi_0)=-4. \\]

The continuous contribution is \\(2\\), and the atomic contribution is \\(-2\\), giving

\\[ O\_\gamma(f_1)=0, \\]

as required.

This is a useful and illuminating example of why the \\(T\\)-independent rational kernel may fail to describe the full spectral measure.

One correction is necessary: The element

\\[ \gamma= \begin{pmatrix} 0&-1\\\ 1&0 \end{pmatrix} \\]

is not unramified elliptic over every \\(p\\)-adic field. For odd residue characteristic, the asserted type \\(U_0\\) requires \\(-1\\) to be nonsquare in the residue field, as it is for \\(q=3\\).

For example, over \\(\mathbb Q_5\\), the element is split rather than elliptic.

The example should explicitly impose the relevant assumption or replace \\(\gamma\\) by an element with irreducible unramified characteristic polynomial.

Subject to that correction, I would retain Proposition 6.4 as a central result of the revision.

## 5. The endoscopic section (§5)

The modernization of §5 is welcome, particularly the replacement of the conjectural status of the fundamental lemma by its established status. The reduction from matching unit elements to the spherical Hecke algebra is supported by Hales's work.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.cambridge.org\&sz=32)

Cambridge University Press



Nevertheless, I recommend more care with the formulation of the transfer identity.

Equation (5.11) should explicitly specify the normalization of orbital integrals, the transfer factor, and the matching conditions. In general, endoscopic transfer is formulated using sums over matching conjugacy classes; the displayed single-class identity needs justification in the precise \\(SL(n)\\) setting under consideration.

In (5.2), the quotient

\\[ G'(F)/G(F)S'(F) \\]

should technically use the image of \\(SL(n,F)\\) in \\(PGL(n,F)\\), since the map is not injective. Quotient measures and finite central kernels must then be handled consistently.

Proposition 5.1, in the maximal-order case where the endoscopic group is an elliptic torus, is a reasonable and valuable consequence of the stated transfer identity.

Proposition 5.2 is conditional on the availability of an appropriate stable spectral measure for \\(H_m\\). That conditional status is correctly recorded in the proposition, but the subsequent prose should not describe it as an unconditional conclusion.

I would also add a short argument explaining why ramified characters of the finite classifying group do not contribute in the spherical setting before restricting the singular part in Conjecture 4.6(c) to unramified \\(\kappa\\).

## 6. Readability and exposition

The exposition is generally clear for a reader already familiar with \\(p\\)-adic harmonic analysis. The historical commentary and glossary are useful, although the manuscript sometimes becomes difficult to follow because the current theorem, its 1997 predecessor, and the justification for the correction are interwoven.

I recommend keeping the mathematical development in the main text and moving most of the detailed historical errata into an appendix.

One possible organizational improvement would be to put the literature review immediately after the introduction, followed by notation, representation-theoretic preliminaries, the main argument, the spectral theorem, endoscopy, and worked examples.

The worked examples could also profitably appear before the main higher-rank proof. The \\(PGL(2)\\) and \\(SL(2)\\) comparison gives readers a concrete reason to care about the distinction between smooth coefficients and residual spectral atoms.

The introduction should contain a compact summary of exactly what is proved, what depends on (R), and what remains conjectural. The existing status table is a good foundation for that purpose, but should distinguish Proposition 5.1 from the conditional Proposition 5.2.

I would move the 1997 acknowledgements from the introduction to an acknowledgements section near the end, preserving the historical attribution.

Finally, I recommend using the genuine LaTeX subsection commands for §7.1–7.4 rather than manually numbered paragraphs, so the derivation from Arthur's formula is properly represented in the table of contents.

## 7. Bibliography and LaTeX

I checked several external bibliographic items. The original 1992 publication is correctly identified, and the 2026 edition of Macdonald's Spherical Functions on a Group of \\(p\\)-adic Type, with Anne-Marie Aubert, is real and correctly identified as Lecture Notes in Mathematics 2392.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://portal.mardi4nfdi.de\&sz=32)

MaRDI portal+1



Arthur's 1987 paper on supercuspidal characters as weighted orbital integrals also has the bibliographic details given in the manuscript; its “not verified” note can be deleted.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://personal.math.ubc.ca\&sz=32)

Personal Math UBC



The bibliography is extensive and valuable, but I have not independently verified every entry. I would remove the remaining editorial verification annotations from a publication version once those entries have been checked.

LaTeX compilation: I compiled the supplied source twice using `pdflatex`. It successfully produces a 39-page PDF. Cross-references resolve, and there are no compilation errors. I found only two extremely small overfull boxes, each less than one point, along with a few underfull-box warnings.

The TeX itself is in good condition.

## 8. Recommended priorities for the next revision

I would address the revisions in this order:

1. Restore the semisimple hypothesis or fully repair the treatment of the center and \\(G(F)^1\\). This resolves the most immediate scope error.
2. Correct or remove Lemma 2.8, and delete its unsupported use in §7.4.
3. Expand the proofs of Proposition 3.6 and Proposition 4.2, including the higher-rank polyhedral bookkeeping and the confluence argument.
4. Correct the scope of the \\(SL(2)\\) example, and preserve Proposition 6.4 with a self-contained proof.
5. Clarify §5 and §7, particularly the distinction between proved spectral measures and anticipated consequences of Arthur's local trace formula.
6. Polish the exposition, with the status of each theorem made explicit and the detailed revision commentary moved out of the main argument.

## 9. Final judgment

My assessment is favorable toward the mathematical direction of the revision, but not yet toward its status as a fully verified theorem package.

The strongest result is the explicit \\(SL(2)\\) example demonstrating the appearance of a spectral atom at a reducibility point of the unramified principal series. The calculation is coherent, and its interpretation is illuminating.

The Brion-based reconstruction of the general argument is promising but needs a more complete higher-rank proof. The principal new counterexamples I found concern the extension to reductive groups and Lemma 2.8; neither requires abandoning the rank-one results.

The manuscript could therefore become a worthwhile corrected and expanded version of the original paper, particularly if it is presented with a clear separation between:

- fully proved results;
- conditional results under Hypothesis (R);
- higher-rank arguments awaiting completion;
- conjectural spectral and endoscopic extensions.

My recommendation is major revision, with the \\(SL(2)\\) spectral-atom result retained and emphasized. That example is substantial enough to motivate the revision independently of whether the more general conjectures are eventually established.
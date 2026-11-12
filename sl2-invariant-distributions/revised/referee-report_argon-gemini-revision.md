# Referee Report

Manuscript: A hitch-hiker's guide to invariant distributions on \\(SL(2)\\) over a \\(p\\)-adic field\
Author: David Joyner\
Draft reviewed: Argon–Gemini revision of the November 2, 1994 manuscript

## 1. Overall assessment

Major revision required

The manuscript has a worthwhile mathematical and pedagogical objective: to explain invariant distributions on \\(SL(2,F)\\) by starting with the explicit classification of irreducible representations, developing their character theory and Paley–Wiener transforms, and ending with supertempered distributions.

This approach has several strengths. Rank one makes much of the harmonic analysis explicit, the Gelfand–Graev and Sally–Shalika character formulas provide concrete examples, and the progression from representation theory to invariant distributions is natural.

However, I found several substantial mathematical problems, including incorrect assertions, incomplete proofs, and some conclusions that do not follow from the preceding material.

The most serious problems concern:

1. The definitions and classification of representations.
2. The image of the normalized orbital-integral transform.
3. The passage from Fourier transforms of functions to Fourier transforms of distributions.
4. The admissible and tempered Paley–Wiener theorems.
5. The treatment of analytic distributions.
6. The characterization of supertempered distributions.

Some of these are repairable with relatively modest changes. Others require restructuring the arguments, particularly in Sections 5–8.

My recommendation is major revision, followed by another mathematical refereeing pass. I would not yet regard the manuscript as suitable for publication or circulation as a corrected mathematical reference.

I distinguish below between findings established by direct mathematical arguments, external sources, and matters that remain unverified.

## 2. Major mathematical findings

### A. The Fourier transform is incorrectly described as a bijection

Section 7.1, around lines 1313–1323 · Independently verified

The manuscript states that there is a bijection

\\[ f\longmapsto \widehat f,\qquad C_c^\infty(G)\longrightarrow PW(G), \\]

where

\\[ \widehat f(\pi)=\Theta\_\pi(f). \\]

This is false. The character Fourier transform is not injective on the full Hecke algebra.

Here is an explicit counterexample.

Take \\(f\in C_c^\infty(G)\\), choose \\(g\in G\\), and define

\\[ f^g(x)=f(g^{-1}xg). \\]

Every irreducible admissible character is conjugation-invariant. Consequently,

\\[ \Theta\_\pi(f^g)=\Theta\_\pi(f) \\]

for every irreducible admissible \\(\pi\\).

Choose \\(f\\) and \\(g\\) so that \\(f^g\ne f\\). Then

\\[ h=f-f^g\ne0, \\]

but

\\[ \widehat h(\pi)=0 \\]

for every \\(\pi\\).

Thus the trace Fourier transform has a nontrivial kernel.

The correct construction is a map from an appropriate quotient:

\\[ C_c^\infty(G)/\ker(\mathcal F\_{\mathrm{tr}}) \longrightarrow PW(G). \\]

For invariant distributions, one can define a Fourier-side functional on the image because invariant distributions annihilate the kernel, provided the trace Paley–Wiener separation theorem is used to establish the required identification.

Required correction: Replace the asserted bijection by a quotient construction, state the precise separation result, and distinguish the trace transform from the operator-valued Fourier transform.

This issue affects Sections 6, 7, and 8.

### B. The theorem on Fourier transforms of tempered distributions is false as stated

Section 6.2, around lines 1243–1261 · Independently verified

The theorem begins with an arbitrary tempered distribution \\(T\\) on \\(G\\) and asserts the existence of a spectral functional satisfying

\\[ T(f)=\widehat T(\widehat f). \\]

The theorem must require \\(T\\) to be conjugation-invariant.

Indeed, point evaluation at \\(x_0\in G\\),

\\[ T(f)=f(x_0), \\]

defines a continuous functional on the Harish-Chandra Schwartz space, hence a tempered distribution.

But, choosing \\(f\\) and \\(g\\) appropriately,

\\[ T(f-f^g)\ne0, \qquad \widehat{f-f^g}=0. \\]

No functional depending only on the character Fourier transform can distinguish \\(f\\) from \\(f^g\\).

Therefore, the claimed spectral representation cannot hold for arbitrary tempered distributions.

Required correction: Restrict the statement to invariant tempered distributions and reformulate the resulting theorem using the invariant Schwartz quotient.

The same objection applies to the corresponding assertions later in Section 8, including the proposed theorem for \\(GL(2,F)\\).

### C. The normalized orbital integral does not generally vanish at the singular points

Section 4.2.1, around lines 795–850 · Independently verified

The manuscript claims that

\\[ f\longmapsto F_f^A \\]

takes values in Weyl-invariant, compactly supported, locally constant functions on \\(A\\) that vanish at \\(a=\pm1\\).

It attributes the vanishing to the factor

\\[ |D(a)|^{1/2}=|a-a^{-1}|. \\]

This reasoning ignores the singular behavior of the unnormalized orbital integral.

For a particularly simple counterexample, take

\\[ f=\mathbf1\_{SL(2,O_F)} \\]

and normalize the Haar measures compatibly with the stated constant-term formula.

For \\(a\in O_F^\times\\), \\(a\ne\pm1\\), that formula gives

\\[ F_f^A(a)= |a|\int_F \mathbf1\_{SL(2,O_F)} \begin{pmatrix}a&ax\\\0&a^{-1}\end{pmatrix} \\,dx. \\]

Because \\(a\\) is a unit, the integrand is \\(1\\) precisely when \\(x\in O_F\\). With \\(\operatorname{vol}(O_F)=1\\),

\\[ \boxed{F_f^A(a)=1.} \\]

In particular,

\\[ \lim\_{\substack{a\to1\\\a\ne1}}F_f^A(a)=1, \\]

not zero.

The Shalika-germ behavior of the unnormalized orbital integral compensates for the vanishing discriminant factor.

Required correction: Remove the vanishing assertion and reformulate the image theorem using the correct germ and boundary behavior.

This is particularly important because the claimed surjectivity is subsequently used to derive several Paley–Wiener image descriptions.

### D. The principal-series reducibility criterion is incomplete

Section 3.1, around lines 372–393 · Checked against an external source

The Gelfand–Graev lemma states that \\(T\_\chi\\) is irreducible precisely when \\(\chi\\) is not one of the three nontrivial quadratic characters.

But the normalized principal series is also reducible at

\\[ \chi=|\cdot|,\qquad \chi=|\cdot|^{-1}. \\]

Indeed, the manuscript itself subsequently discusses the reducibility at \\(|\cdot|^{-1}\\), so there is an internal contradiction.

A corrected statement is:

\\[ \boxed{ I_B^G(\chi)\text{ is reducible} \iff \chi=|\cdot|^{\pm1} \quad\text{or}\quad \chi^2=1,\ \chi\ne1. } \\]

The two exceptional nonunitary parameters have nonsplit length-two principal series, whereas nontrivial quadratic characters give a direct sum of two irreducibles. This agrees with the modern treatment of principal-series reducibility.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://academic.oup.com\&sz=32)

OUP Academic



I recommend giving the exact sequences at both \\(|\cdot|^{\pm1}\\) and clearly distinguishing irreducibility, semisimplicity, and unitarizability.

### E. Two foundational definitions need correction

Section 2.1 · Independently verified

First, the manuscript defines a representation of \\(G\\) as continuous into \\(\operatorname{Aut}(V)\\) endowed with the discrete topology.

Continuity into a discrete group requires the representation to have an open kernel. This is much stronger than smoothness and excludes ordinary infinite-dimensional irreducible admissible representations.

The intended notion is that every vector has an open stabilizer.

Second, the theorem attributed to Harish-Chandra, Bernstein, and Clozel says that every unitary representation has an admissible dense smooth subspace.

The assertion needs an irreducibility hypothesis.

For example, consider the trivial representation on the infinite-dimensional Hilbert space

\\[ H=\ell^2(\mathbb N). \\]

Every vector is smooth, so \\(H^\infty=H\\), but

\\[ \dim H^K=\infty \\]

for every compact open \\(K\\). Thus \\(H^\infty\\) is not admissible.

The appropriate theorem concerns irreducible unitary representations, not arbitrary unitary representations.

Both corrections should be made before proceeding to the classification of the dual.

### F. The Paley–Wiener image descriptions omit necessary compatibility relations

Sections 5.1–5.3, around lines 1130–1206 · Direct derivation and external comparison

At a nontrivial quadratic character \\(\eta\\),

\\[ I_B^G(\eta)=\pi\_\eta^+\oplus\pi\_\eta^-. \\]

Consequently, for every test function \\(f\\),

\\[ \boxed{ \Theta\_{I_B^G(\eta)}(f) = \Theta\_{\pi\_\eta^+}(f)+ \Theta\_{\pi\_\eta^-}(f). } \\]

The trace of the induced family varies algebraically with its unramified parameter. Hence the sum of the two constituent character values must agree with the value obtained by evaluating that algebraic family at the reducibility point.

The manuscript recognizes compatibility conditions in its statement of the admissible Paley–Wiener theorem but does not state them precisely. It subsequently argues that values can be arbitrary on the discrete part of the unitary or tempered dual.

That conclusion is not justified and, without the compatibility relations, is false.

The original Bernstein–Deligne–Kazhdan theorem makes the correct formulation particularly clear: spectral data are linear forms on the Grothendieck group, regular under unramified twisting, and subject to a uniform compact-open level condition.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.math.tau.ac.il\&sz=32)

School of Mathematical Sciences



Required correction: Formulate the trace Paley–Wiener theorem first in terms of the Grothendieck group. Then specialize it to \\(SL(2,F)\\), including explicit relations at every reducibility point.

This would be one of the manuscript's most valuable improvements.

### G. The admissible-distribution descent theorem has a counterexample

Section 8.2, around lines 1522–1583 · Independently derived

The manuscript asserts that if \\(D\\) is a \\(G\\)-admissible invariant distribution, then its descended distribution \\(D_A\\) on the diagonal torus \\(A\\) is \\(A\\)-admissible.

Under the definition of \\(D_A\\) given in the manuscript, this is false without additional hypotheses or a different normalization.

Take the character of the trivial representation:

\\[ D=\Theta\_{\mathbf1},\qquad F_D(g)=1. \\]

This is an admissible invariant distribution.

The manuscript's descent formula gives

\\[ D_A(h)=\frac12\int_A |D_G(a)|^{1/2}h(a)\\,da, \\]

where I have written \\(D_G(a)\\) for the Weyl discriminant to avoid confusing it with the distribution.

Thus the density of \\(D_A\\) is proportional to

\\[ |a-a^{-1}|. \\]

But this function is not locally constant at \\(a=1\\). On an abelian group, the admissibility condition stated in Section 8 requires precisely the relevant local smoothness under sufficiently small compact-open subgroups.

The proof's appeal to the Shalika-germ expansion does not fix this. Local constancy on the punctured neighborhood does not imply uniform local constancy across the puncture.

Required correction: Rework the descent result with the intended constant-term or Jacquet-module normalization. The present \\(D_A\\) should not be asserted to preserve admissibility in general.

### H. The supertempered section contains a false conclusion about elliptic support

Section 9.2, around lines 1880–1888 · Independently verified and checked against Herb

The remark claims that a supertempered distribution must be supported on the elliptic set \\(G_e\\).

This is false.

Consider the Steinberg representation \\(\mathrm{St}\\), which is square-integrable. Its character is supertempered under the weak-constant-term criterion.

Nevertheless, the formula already given in Section 4.2.5 implies, on a regular split diagonal element with \\(|a|>1\\),

\\[ \begin{aligned} \Theta\_{\mathrm{St}} \begin{pmatrix}a&0\\\0&a^{-1}\end{pmatrix} &= \frac{|a|+|a|^{-1}}{|a-a^{-1}|}-1\\\ &=|a|^{-2}\ne0. \end{aligned} \\]

Thus its character is not supported on elliptic elements.

The underlying conceptual problem is a conflation of the ordinary constant term with the weak constant term.

Rebecca Herb's paper explicitly relates the weak constant term of a tempered character to the maximal tempered quotient of its normalized Jacquet module. That is not, in general, the entire Jacquet-module character. Herb also establishes the characterization of supertempered virtual characters using weak constant terms.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.numdam.org\&sz=32)

Numdam



The appropriate distinction is:

- Vanishing of a weak constant term expresses a spectral decay or cancellation condition.
- Support on elliptic elements is a stronger, different property.

The manuscript's construction

\\[ \Theta\_{\pi\_\eta^+}-\Theta\_{\pi\_\eta^-} \\]

is an important example of a supertempered virtual character whose split regular character values cancel. It should be retained, but it does not justify imposing elliptic support on every supertempered distribution.

Required correction: Remove the elliptic-support conclusion, distinguish ordinary from weak constant terms throughout Section 9, and formulate the classification using Herb's theorem.

The manuscript also cites Herb's article as an unpublished preprint. It was published as:

Rebecca A. Herb, Supertempered virtual characters, Compositio Mathematica 93 (1994), no. 2, 139–154.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.numdam.org\&sz=32)

Numdam



## 3. Additional corrections

The following issues also merit attention.

| Location | Finding                                                                                                                                                   | Recommendation                                                                                                                      |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| §2.2     | The expression \\(\chi_0(a/\|a\|)\\) is not a valid general way to extract the unit part of \\(a\in F^\times\\).                                          | Write \\(a=\varpi^{v(a)}u\\), \\(u\in O_F^\times\\), and define the character using \\(\chi_0(u)\\).                                |
| §3.1     | The definition of \\(\operatorname{sign}\_\tau\\) by \\(\operatorname{sign}\_\tau(\tau)=1\\) is incorrect in general.                                     | Use the quadratic norm character \\(\operatorname{sign}\_\tau(x)=(x,\tau)\_F\\), the Hilbert symbol.                                |
| §4.1     | The definition of \\(\Xi(g)\\) uses a discriminant obtained from algebraic eigenvalues, rather than the modulus associated with an Iwasawa decomposition. | Define the Iwasawa projection explicitly and use it in the Harish-Chandra spherical function.                                       |
| §4.2     | Some Weyl integration calculations use \\(1/2\\) for every nonsplit torus.                                                                                | Retain \\(1/\|W_T\|\\) until the rational Weyl group is determined.                                                                 |
| §7       | Reducibility points are treated as though the relevant spectral parameter spaces were ordinary complex manifolds.                                         | Work with Bernstein components, their coordinate rings, and the correct spectral compatibility conditions.                          |
| §9.3     | The second proof of the supertempered example omits orbital integration when applying the Weyl integration formula.                                       | Replace the displayed identity with one involving the orbital integrals of the translated test function, or omit this second proof. |

Two points deserve further explanation.

Quadratic characters. For \\(F=\mathbb Q_3\\) and \\(\tau=3\\), the norm character of \\(\mathbb Q_3(\sqrt3)/\mathbb Q_3\\) satisfies

\\[ \operatorname{sign}\_3(3)=-1. \\]

This follows directly from the quadratic norm form and reduction modulo \\(3\\). Thus the manuscript's proposed characterization fails in an elementary example.

Rational Weyl groups. For \\(SL(2,F)\\), nonsplit torus Weyl groups do not always have order two. When \\(-1\\) is not a square, the rational Weyl group of a ramified elliptic torus can be trivial. Moy and Tadić give the relevant distinctions explicitly.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://scispace.com\&sz=32)

SciSpace



The character-integration calculations should be checked against these cases.

### The analytic-distribution section requires a more careful proof

Section 7, especially lines 1324–1465 · Assessment of the displayed arguments

The density of Laurent polynomials in the holomorphic functions on \\(\mathbb C^\times\\), for the compact-open topology, is a reasonable starting point. The argument can be justified using Laurent expansions.

However, the manuscript's converse theorem concerning exponential bounds on the functionals \\(E\_{M,a}\\) is not established by the proof supplied.

It needs a precise statement showing how growth bounds for the Laurent coefficients imply continuity in the holomorphic compact-open topology.

For the rank-one torus, I suggest an explicit lemma of the following form.

Let \\(\lambda\\) be a linear functional on \\(\mathbb C[z,z^{-1}]\\), and set

\\[ c_n=\lambda(z^n). \\]

If there exist \\(C,R>0\\) such that

\\[ |c_n|\le C R^{|n|} \qquad(n\in\mathbb Z), \\]

then \\(\lambda\\) extends continuously to \\(\mathcal O(\mathbb C^\times)\\).

The proof uses the Laurent expansion of a holomorphic function and Cauchy estimates on a sufficiently large closed annulus. The converse follows by applying a continuity estimate to \\(z^n\\) and \\(z^{-n}\\).

This would provide a rigorous replacement for an important portion of the current argument.

It would not, by itself, resolve the spectral compatibility issues identified earlier.

## 4. Readability and organization

I recommend restructuring the manuscript into four parts while retaining its present progression.

Part I — Representations and characters

Introduce the field, compact subgroups, smooth and admissible representations, induction, reducibility, unitary and tempered duals, and character formulas. Include a classification table.

Part II — Fourier transforms and Paley–Wiener theory

Carefully distinguish operator-valued transforms, trace transforms, and normalized orbital integrals. State the Bernstein–Deligne–Kazhdan theorem before calculating its rank-one consequences.

Part III — Invariant distributions

Introduce the invariant quotient of the Hecke algebra, spectral distributions, Schwartz duality, analytic functionals, and admissibility. Clearly distinguish proved results from conjectural extensions.

Part IV — Supertempered distributions

Explain ordinary and weak constant terms, give the explicit reducible-principal-series examples, and conclude with Herb's classification and a summary of the mathematical results.

### Additional expository improvements

I recommend adding a short historical and literature-review section near the beginning. It should explain the contributions of Gelfand–Graev, Sally–Shalika, Harish-Chandra, Bernstein–Deligne–Kazhdan, Casselman, Kazhdan, Tadić, and Herb, rather than simply naming them at individual theorems.

A glossary and notation table would help considerably. In particular, the manuscript repeatedly uses \\(D\\) for both a distribution and the Weyl discriminant. I suggest writing \\(\Delta_G(\gamma)\\) for the latter.

The manuscript would also benefit from concrete computations over \\(F=\mathbb Q_3\\) and \\(F=\mathbb Q_5\\). These examples would expose the differing rational Weyl groups, exhibit all three quadratic characters, and illustrate the reducibility points.

Finally, I would replace informal headings such as “Nice admissible distributions are analytic” with headings describing the mathematical hypotheses, and distinguish theorems proved in this manuscript from theorems merely quoted.

## 5. Compilation and technical checks

I independently attempted to compile the uploaded LaTeX source.

| Check                                  | Result                                                         |
| -------------------------------------- | -------------------------------------------------------------- |
| XeLaTeX                                | Failed because `babel`'s `bidi=basic` option requires LuaLaTeX |
| LuaLaTeX                               | Successfully compiled                                          |
| Output                                 | 26 pages after two passes                                      |
| Overfull boxes                         | 4                                                              |
| Hyperref PDF-string warnings           | 60                                                             |
| Unresolved citations after second pass | None observed                                                  |

These technical findings are from an actual local compilation, not an inference from the source.

For the next revision, I recommend `amsart`, with consistent theorem environments, properly numbered results, and cross-references using `\label` and `\ref`. The current use of unnumbered boldface theorem headings makes mathematical cross-checking unnecessarily difficult.

The calculations and counterexamples identified earlier were checked directly where indicated. I did not independently certify all Sally–Shalika supercuspidal character formulas or run a separate computer implementation of them; those remain items for a subsequent verification pass.

## 6. Recommended revision priorities

I would approach the revision in the following order.

1\. Repair the representation-theoretic foundations. Correct smoothness, irreducibility, principal-series reducibility, quadratic-character conventions, and the dual-space parameterization.

2\. Rebuild Sections 4–6 around the correct trace Paley–Wiener theorem. This includes correcting the orbital-integral claims and explicitly describing the spectral matching conditions. This is the largest mathematical task.

3\. Rebuild Sections 7–8 using the invariant quotient. Reprove the analytic-functional statements and reconsider the descent theorem rather than retaining an incorrect lemma.

4\. Correct the weak-constant-term treatment in Section 9. The existing explicit supertempered example is valuable and should remain. Herb's 1994 published theorem provides a sound endpoint.

5\. Complete the editorial revision. Add the literature review, notation, glossary, examples, numbered theorems, revision history, and a summary of results.

## 7. Final recommendation

I believe the manuscript is worth revising. Its most valuable feature is the attempt to connect several aspects of \\(p\\)-adic harmonic analysis in one accessible account of \\(SL(2,F)\\).

The classification of the principal series, the explicit characters, the Fourier transforms, and the reducible-principal-series supertempered examples offer a natural educational progression.

But I would distinguish two goals:

- An expository survey of established theory: achievable with a careful correction of the existing manuscript.
- A paper establishing new general results on invariant distributions: this requires substantial new proof work, particularly in Sections 7 and 8.

For the immediate next draft, I recommend pursuing the first goal while retaining any new results that can be proved rigorously.

The most important change is to put the trace Paley–Wiener theorem and the invariant quotient at the center of the manuscript. Once that framework is corrected, the remainder can be organized much more cleanly.

Referee verdict: major revision. The central expository project is viable, but the present arguments do not establish several of the manuscript's principal assertions.
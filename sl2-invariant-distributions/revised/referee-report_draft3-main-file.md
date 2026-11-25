# **Referee report**

**Manuscript:** *A hitch-hiker's guide to invariant distributions on&#x20;*\\(\mathrm{SL}\_2\\)*&#x20;over a&#x20;*\\(p\\)*-adic field*

**Version:** Draft 3, November 24, 2026

**Recommendation:** Further revision, with particular attention to the mathematical foundations of the spectral duality and admissibility results, rather than a substantial restructuring of the paper.

## **1. General assessment**

The manuscript has the potential to become a useful expository and research-oriented account of invariant distributions on \\(\mathrm{SL}\_2(F)\\). Its principal strength is that it uses the relative simplicity of the rank-one representation theory to explain distinctions that are considerably harder to appreciate for general reductive \\(p\\)-adic groups.

In particular, the following themes deserve to be retained:

- The distinction between operator-valued Fourier transforms and trace transforms.
- The role of the cocenter in invariant harmonic analysis.
- The geometry of reducible principal series and exceptional Bernstein fibers.
- The relationship between admissible, unitary and tempered spectral data.
- The interpretation of invariant distributions as spectral functionals.
- The distinction between supertemperedness, ellipticity and cuspidality.
- The use of concrete examples and elementary proofs to illuminate general theorems.

The introductory material is generally readable and mathematically sound. The manuscript also does a commendable job of distinguishing established results, conditional conclusions and open research problems.

There is, however, an important limitation to this referee report. **The uploaded LaTeX file is the master document and not the complete manuscript.** It references five separate source files:

| Missing source file               | Subject                                     |
| --------------------------------- | ------------------------------------------- |
| `spectral-geometry.tex`           | Spectral and Bernstein geometry             |
| `trace-pw-comparison.tex`         | Comparison of trace transforms              |
| `spectral-duality.tex`            | Continuous spectral duals                   |
| `admissible-distributions.tex`    | Admissibility, descent and quasi-finiteness |
| `supertempered-distributions.tex` | Supertempered distributions                 |

Consequently, I can referee the mathematical arguments contained in the master document directly, but I cannot certify the proofs in these five sections from the uploaded file alone. They contain much of the new mathematical material advertised in the abstract.

## **2. Mathematical correctness**

### **M1. Establish the equivalence of the cocenter and the conjugation-invariant quotient**

**Priority: Medium. Section 5.**

The use of Kazhdan's density theorem is appropriate. However, the paper would benefit from an elementary lemma separating two logically distinct results.

Put

\\[ \mathcal H\_{\mathrm{conj}}(G)= \operatorname{span}\_{\mathbb C} \\{f-f^g:f\in\mathcal H(G),\\,g\in G\\}. \\]

The paper should establish

\\[ [\mathcal H(G),\mathcal H(G)] =\mathcal H\_{\mathrm{conj}}(G) \\]

before invoking the density theorem to establish

\\[ \ker\mathcal F\_{\mathrm{tr}} =[\mathcal H(G),\mathcal H(G)]. \\]

The first equality is essentially algebraic, whereas the second is a substantial representation-theoretic theorem.

**Suggested improvement:** Supply a short proof of the first equality using compact-open local units and translations. This would make the subsequent identification of invariant distributions with functionals on the trace image substantially more transparent.

### **M2. Strengthen the result concerning continuity of invariant distributions**

**Priority: High. Subsection on invariant distributions and their spectral functionals.**

The manuscript states that an algebraic functional on the trace image defines an invariant functional on the Hecke algebra, but that continuity must subsequently be checked.

This is unnecessarily cautious for the usual locally convex topology on the \\(p\\)-adic Hecke algebra.

Indeed, one can choose an exhaustion by finite-dimensional spaces

\\[ \mathcal H(G)=\varinjlim_n H_n, \\]

where \\(H_n\\) consists of functions supported in a prescribed compact set and bi-invariant under a prescribed compact open subgroup.

Every linear functional on each \\(H_n\\) is continuous. Consequently, every algebraic linear functional on \\(\mathcal H(G)\\) is continuous for its standard locally convex inductive-limit topology.

This gives the useful identification

\\[ \boxed{ \mathcal H(G)'^{\\,G} \simeq \PW\_{\mathrm{tr}}(G)^\* } \\]

where the right-hand side is the algebraic dual of the trace image.

The situation for Schwartz spaces and holomorphic function spaces is quite different: there continuity becomes a substantive condition.

**Suggested improvement:** Make this distinction into a proposition. It provides an excellent motivation for the later section on continuous spectral duality.

### **M3. Specify the topology of the Harish-Chandra Schwartz space**

**Priority: High. Sections 2 and 5.**

The manuscript gives the appropriate schematic seminorms

\\[ p_N(f)= \sup\_{g\in G} \frac{|f(g)|(1+\sigma(g))^N}{\Xi(g)}. \\]

However, referring to the Schwartz space simply as a locally convex completion does not adequately specify its topology.

I recommend defining the fixed-level spaces

\\[ \mathcal C(G//J) = \\{f\in\mathcal C(G):f\text{ is }J\text{-bi-invariant}\\}, \\]

equipping each with its Fréchet topology, and then writing

\\[ \mathcal C(G)=\varinjlim_J\mathcal C(G//J). \\]

A tempered distribution is then continuous precisely when its restriction to every fixed-level Schwartz space is continuous.

This distinction is particularly important because the paper compares three different types of coefficient growth.

| Spectral test-function space                                     | Growth condition on dual coefficients |
| ---------------------------------------------------------------- | ------------------------------------- |
| Laurent polynomials with their standard inductive-limit topology | Arbitrary growth                      |
| Smooth functions on the unit circle                              | At most polynomial growth             |
| Holomorphic functions on \\(\mathbb C^\times\\)                  | At most exponential growth            |

These are different duality theories. The manuscript should make their relationship one of its central expository points.

### **M4. Develop the complementary-series example**

**Priority: Medium. Section 2.**

The discussion of principal-series reducibility is correct under the stated normalization. In particular, the manuscript correctly distinguishes

\\[ \chi=|\cdot|^{\pm1} \\]

from the three nontrivial quadratic characters.

The discussion of complementary series, however, is less precise than it needs to be. The normalization has already been fixed, so the paper can give the explicit spherical complementary-series interval

\\[ I(|\cdot|^s),\qquad 0\<s<1. \\]

The negative interval is obtained through the Weyl-group symmetry.

In terms of the spectral parameter

\\[ z=\chi(\varpi)=q^{-s}, \\]

the spherical complementary series corresponds to

\\[ q^{-1}\<z<1 \\]

and its inverse interval.

Reducibility parameters (schematic, not to scale)

This would be particularly helpful when explaining why tempered data can algebraically determine admissible trace data without determining them continuously.

The diagram concerns the unramified principal-series parameter space, not the entire unitary dual.

### **M5. Improve the treatment of normalized orbital integrals**

**Priority: Medium. Section 4.**

The example using \\(f=\mathbf1_K\\) is one of the strongest elementary calculations in the manuscript.

The conclusion

\\[ F_f^A(a(t))=1 \\]

for regular \\(t\in\mathcal O^\times\\), with the indicated measure normalizations, is correct.

It demonstrates clearly why the vanishing of the Weyl discriminant does not imply vanishing of the normalized orbital integral near a singular element.

Nevertheless, the displayed identity would benefit from a derivation of the change of variables. In particular, use

\\[ n(y)^{-1}a(t)n(y) = a(t)n((1-t^{-2})y). \\]

The relevant Jacobian is

\\[ |1-t^{-2}|^{-1}. \\]

Combined with the discriminant factor, this gives

\\[ \frac{|t-t^{-1}|}{|1-t^{-2}|}=|t|. \\]

This makes the cancellation mechanism completely explicit.

It would also be worthwhile to extend the example to nonunit \\(t\\). For \\(f=\mathbf1_K\\), the orbital integral vanishes there because an element of \\(K\\) has unit eigenvalues.

Thus the complete normalized split orbital integral in this example is

\\[ F\_{\mathbf1_K}^A(a(t))= \begin{cases} 1,& |t|=1,\quad t\ne\pm1,\\\ 0,& |t|\ne1. \end{cases} \\]

The reader then has an explicit example connecting orbital integration, descent and the spherical trace transform.

### **M6. Distinguish fixed-level Paley–Wiener theorems from the global theorem**

**Priority: High. Section 5 and subsequent sections.**

The statement of the Bernstein–Deligne–Kazhdan trace Paley–Wiener theorem appears mathematically sound.

There is, however, a potential difficulty in its subsequent application.

The theorem gives a characterization of the global trace image using a uniform compact-open support condition. One must be careful about strengthening this to a statement at a *prescribed* compact-open level.

For example, the implication

\\[ L([\pi])=0 \quad\text{whenever }\pi^J=0 \\]

does not follow from the stated global theorem as sufficient to conclude, without an additional argument, that

\\[ L=\mathcal F\_{\mathrm{tr}}(f) \quad\text{for some }f\in\mathcal H(G//J). \\]

One needs a fixed-level realization theorem or an appropriate type-theoretic argument.

This issue is especially relevant to the finite-character interpolation results advertised in Section 8.

**Suggested improvement:** Separate the following three assertions explicitly:

1. Global algebraic trace realization.
2. Realization at a specified compact-open level.
3. Continuous realization in the corresponding Schwartz trace space.

They should not be used interchangeably.

### **M7. The bilateral Laurent-coefficient criterion is correct**

**Priority: Low. Retain and expand.**

I checked both directions of the proof of the Laurent-coefficient theorem.

The equivalence between continuous extension to

\\[ \mathcal O(\mathbb C^\times) \\]

and the bound

\\[ |c_n|\le CR^{|n|} \\]

is correct. The proof using Cauchy's estimates on two circles is efficient and readable.

The Weyl-invariant corollary is also correct.

I suggest adding two further examples.

**Example 1: Derivative evaluation.**

For

\\[ \lambda(h)=z_0h'(z_0), \\]

one obtains

\\[ c_n=nz_0^n. \\]

This satisfies the exponential-growth condition and illustrates that analytic functionals need not be simple point evaluations.

**Example 2: An analytic functional that is not tempered.**

Take

\\[ \lambda(h)=h(2). \\]

Then

\\[ c_n=2^n. \\]

This defines a continuous functional on the holomorphic function space but does not define a continuous functional on the smooth unit-circle space.

Indeed, the Laurent polynomials

\\[ h_m(z)=2^{-m}z^m \\]

converge to zero in \\(C^\infty(S^1)\\), while

\\[ h_m(2)=1 \\]

for every \\(m\\).

This is a particularly simple illustration of the instability of recovering non-tempered evaluations from tempered trace data.

### **M8. Introduce the topology comparison as a unified theorem**

**Priority: Medium to high.**

The preceding observations suggest a theorem that would give the paper a stronger conceptual structure.

Let

\\[ P=\mathbb C[z,z^{-1}]. \\]

Consider the natural maps

The elementary rank-one model. Passing to continuous duals reverses the arrows.

All the displayed maps are injective and have dense image. Passing to the appropriate duals gives inclusions

\\[ C^\infty(S^1)' \hookrightarrow \mathcal O(\mathbb C^\times)' \hookrightarrow P^\*. \\]

Both inclusions are strict.

The three spaces correspond to polynomial, exponential and unrestricted moment growth, respectively.

This theorem can be proved entirely by elementary Fourier and Laurent analysis. The Weyl-invariant version follows by averaging.

Its incorporation into the paper would give readers a unified model for much of the subsequent theory, without claiming an unproved global group-theoretic analogue.

## **3. Mathematical issues requiring particular attention in Sections 3 and 6–9**

The following are verification tasks rather than confirmed errors, because the relevant source files were not included in the attachment.

### **M9. Spectral geometry and exceptional Bernstein fibers**

The manuscript should carefully distinguish:

- The ordinary algebraic quotient of the unramified character torus.
- The extended quotient.
- The primitive spectrum of the Bernstein block.
- The tempered dual of that block.
- The Grothendieck-group relations at reducibility points.

In particular, at \\(z=-1\\) the two quadratic constituents belong to the same inducing fiber, while the Steinberg and trivial representations arise at the exceptional parameters \\(q^{\pm1}\\).

The role of correcting cocharacters in an extended-quotient description deserves explicit treatment. A naive extended quotient can obscure the distinction between these two kinds of exceptional fibers.

### **M10. Algebraic determination by tempered traces**

The abstract advertises the result that admissible traces are algebraically determined by tempered traces.

This is plausible and has a particularly attractive rank-one proof strategy:

- Unitary principal-series traces determine their Laurent polynomials by uniqueness.
- Tempered quadratic constituents supply the exceptional constituent values.
- The Steinberg trace, together with the induced trace at a reducibility parameter, determines the trivial-representation trace.
- Supercuspidal representations of \\(\mathrm{SL}\_2(F)\\) are tempered.

The key identity is

\\[ \Theta\_{\mathbf1}(f) = \Theta\_{I(|\cdot|)}(f) -\Theta\_{\mathrm{St}}(f). \\]

This is a useful algebraic phenomenon. It should not be confused with a continuous extension principle.

I recommend presenting the resulting relationship in a commutative diagram, with the domain, range and topology of every arrow specified.

### **M11. Admissible distributions and finite Bernstein support**

This is potentially one of the most substantive additions to Draft 3.

The first issue requiring verification is the exact definition of an admissible distribution being used.

There are several related but distinct conditions:

| Condition                            | Meaning                                                                                           |
| ------------------------------------ | ------------------------------------------------------------------------------------------------- |
| Finite Bernstein support             | Spectral support lies in finitely many Bernstein components                                       |
| Central finiteness                   | The Bernstein-center orbit spans a finite-dimensional space                                       |
| Local finite-character interpolation | Restriction to a specified test-function subspace agrees with a finite character combination      |
| Character regularity                 | Representability by a locally integrable function, locally constant on the regular semisimple set |

These notions should not be treated as equivalent without proof.

For instance, consider the family of traces \\(P_f(z)\\) in a single Bernstein component. An arbitrary functional

\\[ D(f)=\lambda(P_f) \\]

has support in one component. Nevertheless, the central orbit of \\(\lambda\\) under Laurent-polynomial multiplication can be infinite-dimensional.

This example illustrates why finite Bernstein support alone does not immediately give central finiteness.

A particularly important verification is whether local finite-character interpolation takes place on sufficiently large test-function spaces to transfer Harish-Chandra's regularity conclusions.

Agreement on an arbitrary finite-dimensional collection of test functions is not enough.

### **M12. Central eigenfunctionals and generalized eigenfunctionals**

I recommend developing an elementary model using

\\[ u=z+z^{-1}. \\]

Suppose that \\(\lambda\\) is an eigenfunctional for multiplication by \\(u\\), with eigenvalue \\(a\\). Writing

\\[ c_n=\lambda(z^n), \\]

one obtains the recurrence

\\[ c\_{n+1}+c\_{n-1}=ac_n. \\]

For \\(a^2\ne4\\), its solutions have the form

\\[ c_n=A r^n+B r^{-n}, \qquad r+r^{-1}=a. \\]

At the exceptional values \\(a=\pm2\\), the repeated-root solutions have the form

\\[ c_n=(A+Bn)(\pm1)^n. \\]

However, the Weyl-invariance condition \\(c_n=c\_{-n}\\) forces \\(B=0\\) for these eigenfunctionals.

Generalized eigenfunctionals require separate treatment and introduce higher-order derivative evaluations.

This is a promising connection between Bernstein-center actions, analytic functionals, exceptional spectral parameters and quasi-finiteness.

### **M13. Supertempered virtual characters**

The summary's asserted rank-one classification is consistent with the expected representation-theoretic picture:

\\[ \mathcal{ST}(G) = \operatorname{span}\_{\mathbb C} \left\\{ \Theta\_\pi:\pi\text{ discrete series} \right\\} + \operatorname{span}\_{\mathbb C} \left\\{ \Theta\_{\pi\_\eta^+} -\Theta\_{\pi\_\eta^-}: \eta\ne1,\ \eta^2=1 \right\\}. \\]

For odd residue characteristic, the second span has the three expected generators.

There are several important distinctions that Section 9 should maintain.

Schematic decomposition of spans of finite virtual characters in rank one.

In particular:

- Supertemperedness does not imply supercuspidality.
- Vanishing weak constant terms does not imply vanishing ordinary constant terms.
- Supertemperedness does not imply literal support on the elliptic regular set.
- A splitting of the elliptic Grothendieck quotient does not automatically give a topological splitting of a completed space of distributions.

The Steinberg representation is an excellent test case for these distinctions.

I also recommend verifying the assertion about the trivial-orbit coefficient in the local character expansion at \\(\pm I\\). Any such criterion should specify whether it concerns boundedness, vanishing, extension, normalized character values or another singular-limit property.

## **4. Readability and organization**

Introductory exposition

9/10

Notation and conventions

9/10

Elementary mathematical examples

9/10

Precision of visible theorem statements

8/10

Integration of research themes

7/10

Bibliographical completeness

7/10

Qualitative referee assessment of the supplied master document, not of the five missing sections.

### **R1. Retain the orienting paragraphs**

The short paragraphs at the beginning of sections and subsections are very effective.

For example, the paragraph explaining that the principal-series reducibility criterion depends upon the normalization prepares the reader for precisely the issue that follows.

This aspect of Draft 3 should be preserved.

### **R2. Add a roadmap to the introduction**

The paper now contains several substantial mathematical themes. The introduction would benefit from subsections such as:

- Historical background and objectives.
- Structure of the paper.
- Principal mathematical results.
- Classical inputs and remaining questions.
- Notation and conventions.

At present, the introduction does not fully reflect the breadth of the expanded manuscript.

### **R3. Reduce the length of the abstract**

The abstract attempts to summarize nearly every major development in the manuscript.

I recommend reducing its mathematical content to approximately 180–220 words, retaining the AI-aided statement required by the house style guide.

The more detailed inventory of contributions belongs in the introduction.&#x20;

### **R4. Number the literature review and glossary**

The literature review is substantial enough to constitute a numbered section or a subsection of the introduction.

The glossary should also appear in the table of contents. It could be a numbered final section or an appendix.

This would improve navigation and consistency.

### **R5. Expand the glossary**

Most of the existing glossary entries are accurate but relatively terse.

The following terms should be added or expanded:

| Term                         | Suggested emphasis                                        |
| ---------------------------- | --------------------------------------------------------- |
| Admissible distribution      | Definition and distinction from admissible representation |
| Bernstein center             | Its action on representations and distributions           |
| Central-finite distribution  | Finite-dimensional central orbit                          |
| Extended quotient            | Exceptional stabilizers and representation labels         |
| Quasi-finite distribution    | Exact definition adopted in the manuscript                |
| Analytic spectral functional | Holomorphic topology and moment growth                    |
| Complementary series         | Unitary but non-tempered representations                  |
| Local character expansion    | Nilpotent orbits and singular asymptotics                 |
| Spectral moment              | Evaluation on Laurent monomials                           |
| Fixed-level trace image      | The role of compact-open subgroups                        |

Each glossary entry should ideally have two or three explanatory sentences and a reference to the section where the concept is developed.

### **R6. Improve the diagrams**

The manuscript is particularly well suited to TikZ diagrams. I would recommend diagrams illustrating:

- The exceptional fibers of the Bernstein quotient.
- The admissible, unitary and tempered spectra of the unramified block.
- The inclusions between the three continuous spectral duals.
- The factorization of invariant distributions through the cocenter.
- The relationship between weak and ordinary constant terms.
- The splitting of the elliptic quotient.
- The relationship between central finiteness and spectral support.

These diagrams would serve a mathematical purpose rather than merely a decorative one.

### **R7. Add a running example over&#x20;**\\(\mathbb Q_3\\)

The existing examples over \\(\mathbb Q_3\\) are excellent.

I recommend using \\(F=\mathbb Q_3\\) throughout the manuscript as a running example.

The same field can illustrate:

\\[ F^\times/(F^\times)^2=\\{1,2,3,6\\}, \\]

the five reducible inducing characters, the exceptional unramified parameters

\\[ z\in\left\\{\frac13,-1,3\right\\}, \\]

the three quadratic character differences, orbital integrals, spectral moments and central eigenfunctional recurrences.

This would tie the individual sections together and make the manuscript more accessible to a graduate student encountering the theory for the first time.

## **5. Bibliographical issues**

The literature review is already considerably better than a conventional list of references. It explains why the references matter.

Nevertheless, before circulating the next draft, the bibliography requires a verification pass.

Several entries explicitly contain qualifications such as “pages not verified,” “journal data not verified,” “full text not verified” and “applicability to be reconciled.”

These qualifications are appropriate in a working draft, but they should ultimately be resolved or moved into the revision log.

I would give particular attention to the references concerning:

- Arthur's Schwartz trace Paley–Wiener theorem.
- Herb's characterization of supertempered virtual characters.
- Bernstein-center finite distributions.
- Roche's theory of principal-series types.
- Aubert–Baum–Plymen–Solleveld extended quotients.
- Fixed-level and elliptic cocenter theory.

The Arthur reference is especially important because a precise application of the existing Schwartz trace Paley–Wiener theorem could resolve or considerably narrow some of the paper's stated open topological questions.

I have not independently verified the bibliographic metadata or the exact theorem numbers in these references for this report.

## **6. Recommended action plan for Draft 4**

### **Draft 4 revision checklist**

0 of 15

High priority

Obtain and referee all five included LaTeX source files.

Establish the algebraic cocenter and conjugation-quotient identification.

Correct the discussion of continuity for the Hecke algebra.

Specify the fixed-level and global Schwartz topologies.

Separate global trace realization from prescribed-level realization.

Verify the finite-block admissibility and interpolation arguments.

Verify the supertempered splitting and singular-limit criteria.

Medium priority

Develop the unified polynomial, smooth and holomorphic spectral duality theorem.

Expand the central eigenfunctional and recurrence examples.

Give a complete complementary-series example.

Expand the orbital-integral Jacobian calculation.

Add a running example over the field of 3-adic numbers.

Expand the introduction, glossary and mathematical diagrams.

Verify all bibliographic references.

Low priority

Shorten the abstract and consolidate the revision history.

&#x20;Copy revision checklist

## **7. Final recommendation**

I would not recommend shortening the paper substantially or abandoning any of its major mathematical directions.

The most promising feature of the manuscript is its emerging synthesis of three perspectives:

- **Algebraic:** Bernstein components, Grothendieck groups, cocenters and central actions.
- **Analytic:** Schwartz spaces, holomorphic function spaces and continuous spectral duals.
- **Geometric:** Orbital integrals, descent, exceptional spectral fibers and elliptic representations.

The elementary rank-one calculations provide a natural bridge between all three.

My recommendation is to make Draft 4 primarily a **mathematical consolidation and verification draft**, rather than adding another major research section. The existing program is already sufficiently rich.

I found no fundamental obstruction in the mathematical material I could inspect directly. The visible proofs, particularly the bilateral Laurent criterion and the elementary Mellin-transform calculation, are sound. Most of my corrections concern precision, topology, logical dependencies and the justification of stronger conclusions.

A definitive correctness assessment of Draft 3, however, requires the five supplementary LaTeX files. Those sections contain the results most in need of independent mathematical scrutiny.
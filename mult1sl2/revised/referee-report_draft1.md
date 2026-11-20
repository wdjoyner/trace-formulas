> Referee report on Draft 1, supplied by the author (Nov. 20, 2026). Draft 2 responds to it;
> see `../revision_log.md`, section 1. Line numbers refer to Draft 1 (`git show 045016f`).
> Formatting was cleaned for GitHub (math delimiters, stray web-citation artifacts); the text is unchanged.

# Referee report: *Multiplicity one for SL(2)*, Draft 1

**Manuscript:** David Joyner, Draft 1 (2026), revised from the 1995 manuscript\
**Scope:** Mathematical correctness, completeness of proofs, logical organization, notation, and readability.

## **Overall assessment**

Major revision recommended

The manuscript has considerable mathematical and historical interest. Its central objective—to derive multiplicity one for cuspidal automorphic representations of $SL(2,\mathbb A)$ from a trace-formula comparison with the twofold metaplectic cover—is worth developing.

The most important improvement in the 2026 revision is its explicit separation of established results from conditional assertions. In particular, the Introduction correctly acknowledges that the original 1995 proof did not establish all the required local and global matching identities.

**However, I have found a significant additional gap in the new proof of the conditional main theorem.** It concerns the finiteness of the cuspidal spectrum when only the level and $K_\infty$-types are fixed.

This matters because the manuscript's main result is conditional on two hypotheses, GH and LH, but the proof should still be rigorous *assuming those hypotheses*. As written, that has not yet been established.

My recommendation is to retain the conditional approach, repair the global spectral argument, and distinguish the historical local calculations from those that are currently proved and verified.

## **1. Major mathematical issues**

### **1.1. The finiteness lemma is false**

Lines 3361–3372; used in lines 3398–3418

The manuscript asserts:

> Only finitely many cuspidal automorphic representations, counted with multiplicity, have a nonzero vector fixed by a prescribed finite-level subgroup and with $K_\infty$-types in a prescribed finite set.

This is false.

For $k=\mathbb Q$, take full level $SL(2,\widehat{\mathbb Z})$ and the trivial $SO(2)$-type at infinity. There are infinitely many spherical Hecke–Maass cusp forms of level one, with Laplace eigenvalues tending to infinity. This follows, for example, from the cuspidal Weyl law.

The distinction is between:

- **Finite multiplicity:** each irreducible cuspidal representation occurs with finite multiplicity.
- **Finite spectral counting:** only finitely many representations occur below a prescribed spectral bound, at fixed level and $K_\infty$-types.

The first assertion does not imply finiteness of the set of representations.

Consequently, the finite sets $\mathcal A$ and $\overline{\mathcal A}$ introduced in Step 1 of the proof have not been justified.

This invalidates the subsequent application of Artin's independence theorem to a supposedly finite collection of Hecke characters.

**Suggested repair:** Introduce an archimedean spectral cutoff, such as a bound on the Casimir eigenvalues, and establish a legitimate method of passing from the trace identity to the resulting finite spectral comparisons. One possible approach uses spectral multipliers and trace-class convergence, but this will require additional arguments, and potentially a strengthening of GH to cover an appropriate test-function space.

Merely adding a Casimir bound to the lemma will not suffice: the proof must explain how that bound is imposed while preserving the corresponding-function identity.

This is the highest-priority correction.

### **1.2. An inconsistency in the nonarchimedean character correspondence**

Lines 1234–1274, especially Definition at line 1266

The proposed extension of a genuine torus character involves a parameter $\epsilon$ satisfying

$$ \epsilon^2=(\varpi,\varpi)_2^{-1}\chi_1(\varpi^2), $$

where I write $\varpi$ for the uniformizer.

The corresponding ordinary character involves $\theta$, satisfying

$$ \theta^2=\chi_1(\varpi^2). $$

But the definition then declares that the characters correspond when

$$ \epsilon=\theta. $$

These conditions are incompatible whenever $(\varpi,\varpi)_2=-1$.

For a concrete example, take $F=\mathbb Q_3$, $\varpi=3$, and $\chi_1=1$. Then

$$ (3,3)_3=-1,\qquad \epsilon^2=-1,\qquad \theta^2=1. $$

Thus $\epsilon=\pm i$ while $\theta=\pm1$, and the prescribed correspondence cannot exist.

This is a genuine algebraic inconsistency, not merely a missing proof.

**Suggested repair:** Choose a square root $\eta_\varpi$ of $(\varpi,\varpi)_2^{-1}$ and define the correspondence by

$$ \epsilon=\eta_\varpi\theta. $$

The character and function-matching formulas must then be adjusted consistently. In particular, the Fourier-transform calculation in lines 1289–1344 should be redone with every Hilbert-symbol factor displayed.

### **1.3. Errors in the real torus character formulas**

Lines 1461–1512

There are two issues.

First, the formula for the real Hilbert symbol at lines 1463–1471 depends only on the sign of $x$. The actual formula is

$$ (x,y)_{2,\mathbb R}= \begin{cases} -1,&x<0\text{ and }y<0,\\ 1,&\text{otherwise}. \end{cases} $$

Second, the proposed matching of functions is inconsistent with the preceding character correspondence.

The manuscript declares $\eta=\epsilon i$, but then prescribes

$$ \overline f(a(x),1)=\epsilon f(a(x)), \qquad x<0. $$

For equality of the Fourier transforms for the corresponding characters as defined, the factor on the negative component should instead be

$$ \boxed{\overline f(a(x),1)=-i f(a(x)),\qquad x<0.} $$

This follows by substituting $\eta=\epsilon i$ into the two character integrals. The definition should be corrected before its consequences for principal-series character transfer are used.

### **1.4. The elliptic character argument omits anisotropic Cartans**

Lines 1518–1584

The proof at lines 1581–1584 says that the Weyl integration formula contains only two Cartan contributions: an elliptic Cartan and the split Cartan.

That description applies to $SL(2,\mathbb R)$, but not generally to $SL(2,F)$ for a nonarchimedean local field.

Over a $p$-adic field, there may be several inequivalent anisotropic Cartans associated with distinct quadratic extensions of $F$.

Therefore, matching orbital integrals on a single elliptic Cartan does not automatically imply equality of the corresponding characters.

**Suggested repair:** State the matching over every relevant stable or rational conjugacy class of anisotropic Cartan, then apply the Weyl integration formula with all its terms. The character-relation caveat already acknowledged in Remark 3.4 should be integrated into this correction.

### **1.5. Scope of Waldspurger's multiplicity-one theorem**

Lines 3470–3477

The last step uses the assertion

$$ m(\overline\pi)\leq 1 $$

for every genuine cuspidal automorphic representation of the metaplectic cover.

This deserves a more precise reference.

Some expositions of Waldspurger's theory formulate multiplicity one on the subspace $\mathcal A_{00}$, orthogonal to the elementary theta series arising from one-dimensional quadratic forms. For example, Ikeda explicitly distinguishes $\mathcal A_0$ from $\mathcal A_{00}$ when quoting Waldspurger's theorem.

I am not asserting that the manuscript's multiplicity-one input is false. Rather, **the exact scope of the cited theorem needs verification**.

If the cited result covers only $\mathcal A_{00}$, the proof must either show that its representations lie in that subspace or separately handle the elementary theta representations.

This is particularly important because the proposed theorem concerns the entire genuine cuspidal spectrum.

### **1.6. Undefined matching conditions at certain regular elliptic elements**

Lines 1956–1982

The definitions of the three real elliptic correspondences contain the denominator

$$ e^{i\theta}+e^{-i\theta}=2\cos\theta. $$

This vanishes at $\theta=\pi/2$ and $3\pi/2$.

Those values are not excluded in the manuscript, and the corresponding elements of $SL(2,\mathbb R)$ are regular elliptic elements.

The definitions must therefore be reformulated. One solution would be to express the identities without division, together with an appropriate condition at the zeros. The subsequent character identities should then be rechecked.

### **1.7. The Satake isomorphism does not, by itself, establish orbital-integral matching**

Lines 1586–1661

The discussion constructs an isomorphism between spherical Hecke algebras and concludes:

> This implies the matching of orbital integrals for spherical functions.

This implication requires justification.

An algebra isomorphism identifies spherical Hecke eigencharacters, but an equality of geometric orbital integrals is an additional statement. It does not follow formally from the existence of the algebra isomorphism alone.

The manuscript should distinguish the spectral matching supplied by Satake theory from the geometric matching needed for the global trace formula.

The existing acknowledgment that weighted orbital integrals have been matched only in special cases is appropriate and should be retained.

### **1.8. Definitions of the Hecke algebras**

Lines 390–419

The spherical Hecke algebra is defined using $C^\infty(G(F)//K)$, without explicitly requiring compact support.

The usual spherical Hecke algebra consists of **compactly supported, locally constant, bi-**$K$**-invariant functions**.

Without the compact-support restriction, convolution need not be defined within the proposed space.

This should be corrected in the preliminary definitions and checked for consistency throughout the manuscript.

### **1.9. Other assertions requiring qualification**

The description of the adelic metaplectic cover in lines 466–495 should be revised. In the standard construction, the global cover is obtained from the restricted product of local covers by quotienting by the subgroup of central sign tuples whose product is $1$. The statement that the global cover can simply be identified with a subgroup of the restricted product is not justified as written.

The Iwahori–Hecke isomorphism presented as a theorem in lines 2099–2103 is subsequently questioned by the manuscript itself. The appropriate linear group in the established metaplectic correspondence is generally $PGL(2)$, rather than $SL(2)$, as discussed in the cited Takeda–Wood work. Since the assertion is explicitly unverified, it should be presented as a historical claim rather than a theorem.

Finally, the local measure normalization on anisotropic tori in lines 431–436 needs a more precise definition. Conjugacy over an algebraic closure does not itself identify the groups of $F$-rational points or transport Haar measures between them.

## **2. Assessment of the conditional main theorem**

The underlying idea of Chapter 6 is attractive.

Once an appropriate finite spectral identity has been obtained, the intended argument is logically clear: isolate a fixed unramified Hecke eigensystem, use local character separation to distinguish the remaining constituents, and apply injectivity of local transfer together with multiplicity one on the metaplectic side.

In particular, I found no error in the elementary tensor-product independence lemma at lines 3374–3384.

The major obstruction is the transition from a global trace identity involving an infinite cuspidal spectrum to a finite comparison of coefficients.

I would therefore describe the current status of Theorem 6.1 as:

**A conditional multiplicity-one argument with an unresolved spectral-isolation step and an additional reference verification concerning metaplectic multiplicity one.**

This is a more accurate status than either calling the proof complete or rejecting the strategy altogether.

I also recommend emphasizing that GH is a particularly strong hypothesis. It asserts equality of the complete cuspidal trace distributions for a substantial class of matching functions. That assumption encompasses much of the difficult global comparison the original project hoped to establish.

## **3. Readability and exposition**

The manuscript is generally understandable to a reader familiar with automorphic representations, reductive groups over local fields, and Arthur's trace formula. Nevertheless, it still reads in places as a collection of independently written research notes rather than a unified monograph.

### **Organization**

I recommend reorganizing the opening chapters to make a sharper distinction between the mathematical framework and the historical development.

The Introduction should state the conditional theorem, define GH and LH informally, and explain their mathematical purpose. The local chapters should then distinguish verified results, partial calculations, and unproved historical claims.

Chapter 6 is currently the clearest part of the manuscript. Its separation into hypotheses, theorem, proof, and limitations works well and is a good model for the other chapters.

### **Proof presentation**

Several proofs are too abbreviated for statements that carry substantial mathematical content.

Examples include the small-support weighted orbital-integral lemma (lines 1367–1376), where the proof is described only as a direct calculation, and the real discrete-series matching lemma (lines 1986–2023), where the proof appeals to the Weyl integration formula without displaying the actual character substitutions.

For these results, I would include at least one complete calculation with explicit normalizations. This would allow readers to identify exactly where the cocycle factors enter.

The supercuspidal correspondence in Chapter 3 is particularly important. Its 2026 caveat is welcome, but a proposition known to require correction should not appear as an established result without a qualification attached directly to its statement.

### **Notation**

Several symbols are overloaded. In particular, $\pi$ denotes both a uniformizer and a representation; $S$ denotes several different sets; and $\chi$ serves as both an inducing character and a spectral parameter.

I recommend using $\varpi$ exclusively for a local uniformizer, $\pi$ for representations, and $S$ consistently for sets of places. The distinction between $G(F)$, $\overline{G(F)}$, and their sections should also be maintained more carefully.

A notation table near the beginning would substantially improve readability.

### **Bibliography and historical commentary**

The historical material is interesting, but several entries still describe preprints from the 1990s without giving final publication data. These should be updated where possible.

The literature discussion should distinguish multiplicity one, strong multiplicity one, local theta correspondence, and global Waldspurger packets. These are closely related topics, but they are not interchangeable.

The paper Modularity of the Rankin–Selberg L-series, and multiplicity one for SL(2) supplies a useful historical point of comparison, while the later work of Chai and Zhang on a qualified strong multiplicity-one theorem for $SL(2)$ would be worth mentioning in the Introduction.

## **4. LaTeX and technical presentation**

I also tested the source using `pdflatex`.

**The manuscript compiles successfully.**

The compiled document is 56 pages. After three compilation passes, there were no unresolved citation or cross-reference warnings.

There are three overfull boxes, including ones in the Iwahori correspondence discussion, the Weil representation section, and the trace-formula chapter. These are relatively minor formatting defects.

A few straightforward editorial corrections would also help: replace informal proof markers such as `proof:` with the `amsthm` proof environment, use `\operatorname{tr}` consistently, replace older `eqnarray` environments with `align`, and standardize notation for the metaplectic cover.

The source is technically serviceable; the substantive mathematical revisions are more urgent than the typesetting.

## **5. Recommended revision program**

I would prioritize the next draft as follows.

| Priority | Task                                                                          | Importance |
| -------- | ----------------------------------------------------------------------------- | ---------- |
| 1        | Repair the false spectral finiteness lemma and global isolation argument      | Critical   |
| 2        | Correct the $p$-adic torus character correspondence                       | Critical   |
| 3        | Correct the real torus character and elliptic matching formulas               | High       |
| 4        | Verify the precise multiplicity-one theorem used for the metaplectic spectrum | High       |
| 5        | Repair the treatment of anisotropic Cartans in the Weyl integration formula   | High       |
| 6        | Separate established local theorems from historical, unverified claims        | High       |
| 7        | Clarify spherical orbital-integral transfer and Hecke algebra definitions     | High       |
| 8        | Improve notation, expand selected proofs, and modernize references            | Moderate   |

## **Final recommendation**

The manuscript has a worthwhile organizing idea, and the 2026 revision is a substantial improvement in mathematical transparency over the unconditional claims attributed to the 1995 version.

I would not recommend presenting Draft 1 as a completed proof of its conditional main theorem. The incorrect finiteness lemma is a real gap, while the local character formulas contain several concrete inconsistencies that can be corrected independently.

**I recommend a Draft 2 focused on repairing Chapter 6 first**, followed by a careful local-character audit of Chapter 4. There is no need to abandon the project or substantially rewrite all six chapters.

The most promising contribution may ultimately be a rigorous, carefully qualified exposition of the trace-formula approach to multiplicity one for $SL(2)$, identifying precisely which local and global transfer statements would make the method work. That would have value even if some of the original conjectural comparisons remain unproved.
# Referee report: A hitch-hiker’s guide to the metaplectic trace formula for \\(SL(2)\\)

Manuscript reviewed: `preview.tex` and Sections 2–6, including the foundations, rank-zero trace formula, geometric expansion, spectral expansion, and invariant trace formula.

Recommendation: Major revision.

The manuscript is a substantial and worthwhile reconstruction of the trace formula for the metaplectic double cover of \\(SL(2)\\). Its overall organization is sensible, the specialization to \\(n=2\\) clarifies several difficult points, and the worked calculations are particularly valuable.

However, I found two definite mathematical errors in the foundational and local analytic arguments. Both should be corrected before the manuscript is circulated as a fully verified treatment. I also found several places where the proof or the claimed level of explicitness needs qualification.

## 1. Major correctness issues

### 1.1. Kubota’s cocycle is not continuous

Location: `sec2-foundations.tex`, lines 76–105, particularly Lemma 2.1; also lines 427–428 and 499–505.

Lemma 2.1 calls the explicitly defined Kubota cocycle \\(\beta\\) a continuous Borel 2-cocycle. This is false at a real place.

For a concrete counterexample, take \\(F=\mathbb R\\), \\(g_1=-I\\), and

\\[ g_2(c)= \begin{pmatrix} 1&0\\\c&1 \end{pmatrix}. \\]

For \\(c\ne0\\), the manuscript’s formula gives

\\[ \beta(-I,g_2(c))=(c,-1)\_{\mathbb R} = \begin{cases} -1,&c<0,\\\ 1,&c>0. \end{cases} \\]

Yet \\(g_2(c)\to I\\) as \\(c\to0\\), and \\(\beta(-I,I)=1\\). Thus \\(\beta\\) is discontinuous.

This is more than a terminology issue. The model \\((g,\zeta)\\) is a legitimate Borel model, but its usual product topology is not the topology of the metaplectic covering group. In particular, the real metaplectic group cannot be obtained by placing the ordinary product topology on \\(SL(2,\mathbb R)\times\mu_2\\).

The definition on lines 427–428,

\\[ f\in C_c^\infty(\overline{G(\mathbb Q_p)})\_- \quad\Longleftrightarrow\quad g\longmapsto f(g,1)\in C_c^\infty(G(\mathbb Q_p)), \\]

therefore also needs correction. A smooth function on the covering group need not have a globally smooth expression through this discontinuous section. The analogous definition in Section 3, lines 73–75, has the same problem.

Required repair: Define the metaplectic cover with its covering-group topology, define smooth test functions intrinsically on that group, and use the Kubota coordinates only as Borel coordinates. Replace the continuity assertion for the adelic cocycle on lines 502–503 accordingly.

The algebraic cocycle formulas may remain valid, but the analytic framework must be formulated using the correct topology.

### 1.2. A central element is incorrectly said to act trivially

Location: `sec6-invariant.tex`, lines 451–463, especially line 461.

The proof of Lemma 6's local normalization calculation states:

> “Here \\((w,1)\_v^2=(-1,1)\\) acts trivially.”

This is false for genuine representations at a real place.

Indeed, Section 2 itself establishes that

\\[ (-I,1)^2=(I,-1) \\]

over \\(\mathbb R\\). In any genuine representation \\(\pi\\),

\\[ \pi(-I,1)^2=\pi(I,-1)=-\operatorname{Id}. \\]

Consequently, \\(\pi(-I,1)\\) cannot be the identity; its eigenvalue is necessarily \\(i\\) or \\(-i\\) on an irreducible genuine representation.

The assertion is used in the proof of the adjoint relation for the unnormalized intertwining operator. That relation requires a central-character phase, or a carefully adjusted convention for the Weyl intertwiner.

Required repair: Re-derive the adjoint and functional equations with the action of \\(w^2=-I\\) retained explicitly, and then verify that the chosen scalar factors \\(r_v(\pi_v,\lambda)\\) cancel the phases needed for the normalized identities.

I emphasize the distinction: this demonstrates an error in the proof, not necessarily a false normalization theorem. The explicit real normalized eigenvalues displayed later may still be correct. But their proof must not use the stated triviality assertion.

Correction to point 1.2: On checking the scope of that proof more closely, the disputed statement occurs specifically in part (a) of Lemma `explicit-r`, where \\(v\\) is finite, non-dyadic, and the inducing character is unramified. In that setting \\((-I,1)\\) lies in the chosen splitting \\(K_v^\*\\) and does act trivially. I withdraw objection 1.2 as a mathematical error. The central element would not act trivially for an arbitrary genuine representation, but the manuscript does not make that assertion here.

The principal definite defect remains the topology and smooth-function definitions in Section 2. The following observations concern proof completeness, precision, and readability rather than additional established counterexamples.

### 1.3. The test-function problem can also be seen at a finite place

There is an especially useful example showing why the issue in §1.1 is consequential.

Take \\(F=\mathbb Q_3\\) and

\\[ k_n=\begin{pmatrix}-1&0\\\3^n&-1\end{pmatrix} \in SL(2,\mathbb Z_3). \\]

Then \\(k_n\to-I\\), while the splitting function of `sec2-foundations.tex`, lines 133–137, satisfies

\\[ \kappa_3(k_n)=(3^n,-1)\_3=(-1)^n. \\]

The spherical Hecke identity \\(e_3\\), defined on lines 433–436, consequently has

\\[ e_3(k_n,1)=(-1)^n. \\]

Thus \\(g\mapsto e_3(g,1)\\) is not locally constant, although \\(e_3\\) is supposed to belong to the manuscript’s space of smooth compactly supported test functions.

This produces an internal contradiction between the definition of the test-function space and the claimed Hecke-algebra identity.

The repair is straightforward conceptually: adopt the intrinsic smooth-function space on the topological cover, rather than using the globally discontinuous Kubota section as a smooth chart.

## 2. Additional points requiring attention

| Location                          | Finding                                                                                                                                                                                                                                                           | Assessment                      |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| Section 3, lines 116–119          | The proof asserts that a continuous character has an open kernel. This is false in general, although the required assertion for the compact open subgroup at almost all finite places is valid.                                                                   | Minor proof correction          |
| Section 4, lines 710–742, 779–793 | The fine geometric expansion introduces coefficients \\(a^G(S,u\_\xi)\\) without computing them. The manuscript acknowledges this, but the distinction between a defined coefficient and an evaluated one should be maintained consistently.                      | Completeness and exposition     |
| Section 5, lines 939–959          | The residual spectrum is identified with even Weil representations, but the precise relationship between the square-class parameters \\(b\\) and \\(b'\\) remains unsettled.                                                                                      | Normalization/labeling gap      |
| Section 6, lines 419–449, 513–537 | The explicit real normalizing factor is presented for \\(\chi_v=\operatorname{sgn}^{\epsilon}\\). The subsequent global discussion should also specify the formula for general unitary inducing characters with a nonzero \\(\lvert\cdot\rvert^{it}\\) component. | Clarification needed            |
| Section 6, lines 582–594          | The normalizing factors at dyadic and other bad places are imported from the literature rather than evaluated explicitly.                                                                                                                                         | Qualified reliance on citations |
| Section 6, lines 900–901          | The invariant trace formula is described as having “every term explicit.” That overstates what is achieved, given the unevaluated coefficients and bad-place factors.                                                                                             | Editorial correction            |

### The global normalizing factors deserve a more careful presentation

This is the most important item after the topology issue.

A general real unitary character has the form

\\[ \chi_v(t)=\operatorname{sgn}(t)^\epsilon |t|^{i\tau}. \\]

The formula for the real intertwining eigenvalues should either accommodate \\(\tau\\) explicitly, by shifting the spectral parameter, or explain the normalization that removes it.

I would also recommend distinguishing three notions that presently occur close together:

1. Existence of a normalizing factor satisfying the required analytic axioms.
2. An explicit formula for that factor at a particular place.
3. Compatibility of all local choices with the global normalizing function.

These are different assertions. The manuscript is appropriately cautious about the bad places in Remark 2026, but that caution should carry through to the theorem summaries.

### The treatment of \\(M(w,0)=-1\\)

Location: `sec6-invariant.tex`, Proposition `Mw0`, lines 990–1023.

This is among the more interesting results of the manuscript.

The argument uses the vanishing of the nonconstant Whittaker coefficients at \\(\lambda=0\\), reducing the Eisenstein series to its constant term. It then exploits automorphy and the two opposite unipotent subgroups to force the remaining function to vanish.

The structure of this proof is convincing, conditional on the stated analytic continuation and Whittaker-factorization results.

I recommend retaining the result prominently, but adding a short explanation of why the pole of the zeta function at \\(s=1\\) produces the required zero in the Whittaker coefficients, and why the two unipotent subgroups generate enough of the covering group to conclude the argument.

This will help readers see why the proof establishes a genuine representation-theoretic fact, not just an identity of \\(L\\)-functions.

## 3. Readability assessment

Section 2 — Foundations

Major correction required

The presentation of the cocycle, compact splitting, and adelic quotient is useful. However, the distinction between Borel coordinates and the topology of the covering group must be made explicit. This is the first change I would make.

Section 3 — Rank zero

Generally clear

The reduction of the rank-zero trace formula to Fourier analysis and Poisson summation is particularly effective. The proof of the character-factorization lemma needs the small correction mentioned above.

Section 4 — Geometric expansion

Technically dense

The argument benefits from the specialization to rank one, but the succession of truncation functions, weighted orbital integrals, and Laurent coefficients is difficult to follow without a roadmap.

Section 5 — Spectral expansion

Good structure

The separation of the cuspidal, residual, and continuous spectra is helpful. A diagram showing how the Eisenstein series, constant-term operator, intertwiner, and residual representations relate would substantially improve accessibility.

Section 6 — Invariant formula

Needs exposition

The normalization calculations and Fourier construction of the correction term are valuable. The reader needs a clearer explanation of why subtracting \\(\Phi_A\\) makes the weighted orbital integral invariant, before encountering the full formal machinery.

### Suggested editorial changes

I would make the following revisions, in this order:

1\. Add a one-page overview before Section 2. Explain the progression from the covering group, through geometric and spectral expansions, to invariant distributions. State precisely which results are proved and which are invoked from Arthur, Langlands, and Li.

2\. Introduce a notation table. Include \\(G\\), \\(\overline G\\), \\(A\\), \\(B\\), \\(N\\), \\(K_v^\*\\), \\(\beta_v\\), \\(\sigma_v\\), \\(\kappa_v\\), \\(J_A\\), \\(I_A\\), \\(\varphi_A\\), and \\(\Phi_A\\). In particular, distinguish the two functions \\(\varphi_A\\) and \\(\Phi_A\\), since they live on different sides of Fourier inversion.

3\. Use \\(k=\mathbb Q\\), \\(S=\\{\infty,2\\}\\) as a running example. The manuscript already has good pieces of this example. Bringing them together would make the roles of the real and dyadic places, the four ramified square classes, and the local normalizing factors much easier to understand.

4\. Separate historical corrections from the main exposition. The repeated comparisons with the 1995 notes are valuable documentation, but they interrupt the mathematical development. A consolidated appendix listing corrections and revised theorem numbers would make the main text more readable.

5\. Move the “what rests on citation” discussions into a uniform end-of-section subsection. These discussions are unusually helpful and should be preserved. A common format would make the manuscript's claims easier to audit.

6\. Expand the explanatory paragraph preceding the invariant trace formula. Emphasize the conceptual identity\
\\[\
I_A(\gamma,f)=J_A(\gamma,f)-\Phi_A(\gamma,f)\
\\]\
and explain geometrically why \\(J_A\\) fails to be invariant and spectrally why the correction term has exactly the required variation.

## 4. LaTeX and presentation

I compiled `preview.tex` successfully using three passes of `pdflatex`.

Compiled length

# 54 pages

Unresolved references

# 0

There is one significant overfull line, approximately 26.9 pt, in the proof of the local Iwasawa decomposition (`sec2-foundations.tex`, around lines 322–326). Several much smaller spacing warnings are not serious.

The six uploaded files did not include the referenced `checks/` scripts or `revision_log.md`, so I have not independently certified the manuscript's numerical verification claims.

## 5. Overall judgment

The manuscript has several strengths:

- The restriction to the double cover makes the rank-one theory appreciably clearer.
- The rank-zero Poisson summation argument is well motivated.
- The explicit real intertwining calculations are a valuable teaching contribution.
- The inclusion of residual representations and ramified spectral classes substantially improves the spectral treatment.
- The authors generally distinguish new proofs from results imported from the literature, which is good mathematical practice.

The main revision priority is to correct the topology of the metaplectic cover and the associated definition of test functions throughout Sections 2–6. Because the Hecke algebra and test-function spaces are used everywhere, this should be addressed before treating the later formal identities as fully established.

After that, I would concentrate on the local normalization conventions, the remaining unevaluated coefficients, and improving the transitions between the geometric, spectral, and invariant sides.

My recommendation remains major revision, but not rejection. The overall strategy appears promising, and I did not identify a counterexample to the final invariant trace formula itself. The review does not amount to an independent verification of every convergence theorem or cited analytic input; those remain the principal items requiring a more exhaustive audit after the foundational repair.
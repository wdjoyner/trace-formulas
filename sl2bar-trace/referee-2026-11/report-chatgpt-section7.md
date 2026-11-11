# Independent referee report on Section 7

## I. Proposition 7.5: the character of \(r_\psi^+-r_\psi^-\)

### 1. The formula itself

**Assessment: Correct on the regular semisimple set, subject to the analytic qualifications below.**  
**Evidence: A; B (Thomas 2008).**

The asserted formula is

\[
\Theta_\psi^+(x)-\Theta_\psi^-(x)
=\frac{\Delta_\psi(x)}{|\det(1+p(x))|_v^{1/2}}.
\]

I independently repeated the kernel calculation. Writing \(P\phi(\xi)=\phi(-\xi)\), the desired distribution is \(\operatorname{tr}(\omega_\psi(f)P)\).

For \(g=\begin{pmatrix}\alpha&b\\c&d\end{pmatrix}\), \(c\ne0\), the kernel of the Weil representation is

\[
k_g(\xi,\eta)=\gamma_v(c)^{-1}|c|_v^{-1/2}
\psi\left(\frac{\alpha\xi^2-2\xi\eta+d\eta^2}{c}\right).
\]

Consequently,

\[
k_g(\xi,-\xi)
=\gamma_v(c)^{-1}|c|_v^{-1/2}
\psi\left(\frac{D^+(g)}c\,\xi^2\right),
\]

where \(D^+(g)=2+\operatorname{tr}g\). Evaluating this quadratic Gaussian integral gives

\[
|D^+(g)|_v^{-1/2}
(c,D^+(g))_v
\frac{\gamma_v(D^+(g))}{\gamma_v(1)},
\]

which is precisely the manuscript's \(\Delta_\psi/|D^+|^{1/2}\).

The algebraic constant and its Hilbert-symbol sign agree with my derivation. Thomas's character formula supplies a separate check of the magnitude and Weil-index structure, but not of this particular Kubota-coordinate sign without translating conventions.

### 2. Finite-place proof: finite rank and the diagonal trace

**Assessment: Substantially correct, but one justification should be made explicit.**  
**Evidence: A.**

For sufficiently small compact open \(K_m\), the \(K_m\)-fixed vectors in the Schrödinger model form a finite-dimensional space. Invariance under the upper unipotents bounds the support in a lattice; invariance under conjugate lower unipotents bounds the support of the Fourier transform. Thus these vectors are supported on a bounded lattice and constant on cosets of another lattice. Their space is finite-dimensional.

This proves finite rank for \(\omega_\psi(f)\) when \(f\) is suitably bi-\(K_m\)-invariant, as in the manuscript.

I recommend inserting this two-lattice argument explicitly. It explains both finite-dimensionality and why the resulting kernel is Bruhat–Schwartz. The diagonal trace formula then follows from a finite-rank kernel decomposition.

### 3. Uniform stabilization of truncated Gauss integrals

**Assessment: The claim is correct, but the proof is compressed.**  
**Evidence: A, including independent code.**

I ran a checker written independently of the repository's script. For the standard \(p\)-adic additive characters, I evaluated

\[
\int_{p^{-M}\mathbb Z_p}\psi_p(a\xi^2)\,d\xi
\]

for several \(a\) at \(p=2,3,5\). The values stabilize exactly as expected: for example, at \(p=2\), \(a=1\) stabilizes at \(1+i\) from \(M=1\), while \(a=2\) stabilizes at \(\sqrt2(1+i)\) from \(M=2\). These tests do not use the authors' program.

For a proof, it is enough to state and establish a uniform shell-vanishing lemma: when \(a\) ranges over a compact subset of \(F^\times\), the integral of \(\psi(a\xi^2)\) over sufficiently distant valuation shells vanishes, with a common threshold. In the dyadic case the threshold must explicitly account for \(v(2)\).

This would close the only abbreviated step in the finite-place argument. The computations are supporting evidence, not a substitute for that lemma.

### 4. Archimedean proof and reduction to \(c\ne0\)

**Assessment: Acceptable with a more precise analytic citation and an expanded reduction argument.**  
**Evidence: A; B (Thomas 2008).**

For compactly supported smooth \(f\), the relevant integrated Weil operator is smoothing and trace class. The manuscript correctly uses the Gaussian regularization

\[
e^{-\epsilon|\xi|^2}
\]

and obtains a bound controlled by \(|D^+(g)|^{-1/2}\) on support bounded away from \(D^+=0\).

However, the sentence that smooth vectors are Schwartz functions does not by itself prove that the *two-variable integral kernel* \(K_f(\xi,\eta)\) is Schwartz. The authors should either show smoothing on both sides (including the adjoint) or cite a precise kernel-and-trace result. Thomas's 2008 paper discusses the integrated-operator trace through its kernel in §12.2; that is a better citation than the generic references currently given. Maktouf's work should not be presented as the direct archimedean justification.

The reduction to test functions supported where \(c\ne0\) is legitimate on the regular semisimple set: every regular conjugacy class meets that open set, conjugation preserves the distribution, and one can use local conjugation neighborhoods together with a finite partition of unity on the compact support. This argument should be spelled out in two sentences.

The extension from the regular set to all test functions relies on the local integrability theorem for the Weil character, not on the kernel computation alone. The manuscript mostly distinguishes these correctly.

### 5. Equation (7.7), Thomas Theorem 1C, and the second comparison

**Assessment: Equation (7.7) is correct; the first comparison is accurate only up to sign; the second is a comparison of forms, not a checked normalization identity.**  
**Evidence: A; B (Thomas 2008, Theorem 1C; Thomas 2013, Theorem D).**

Without the parity operator \(P\), the diagonal kernel produces

\[
\Theta_{\omega_\psi}(g,\zeta)=
\zeta(c,D^-)_v
\frac{\gamma_v(D^-)}{\gamma_v(1)}
|D^-|_v^{-1/2},
\qquad D^-=\operatorname{tr}g-2.
\]

I verified this independently. Since \(\det(g-1)=-D^-\), its magnitude and Weil-index factor agree with Thomas's Theorem 1C. Importantly, **Thomas states Theorem 1C only up to sign**. Thus Thomas does not independently certify the specific sign \((-c,D^-)_v\) claimed in the manuscript; that sign is supported by the manuscript's separate Schrödinger-model computation.

The second comparison uses

\[
\omega_\psi((-1,1))=\gamma_v(1)^2P,
\]

hence

\[
\Theta_\psi^+-\Theta_\psi^-
=\gamma_v(1)^{-2}\Theta_{\omega_\psi}((-1,1)\,\cdot).
\]

This follows directly from the chosen representation conventions. Thomas's Theorem D, however, is expressed in his own metaplectic coordinates and includes a quadratic-form Weil-index factor \(\gamma_\psi(Q_g)\). The manuscript acknowledges that it has not matched those normalizations. I agree with retaining the comparison, but it should say explicitly: *the formulas have the same representation-theoretic relationship; an equality between their coordinate factors has not been verified.*

The remark suggesting that changing a Weil-index normalization merely changes \(\psi\) by a square class is too imprecise to justify an exact comparison. Remove that justification or provide the actual change-of-conventions formula.

## II. Condition (N5), Lemma 7.8, and Remark 2026.18

### 6. Lemma 7.8(c): the intertwining-operator relation

**Assessment: Correct.**  
**Evidence: A.**

Set \(\alpha=\operatorname{Ad}(\delta_a)\), \(\pi'=\pi\circ\alpha^{-1}=\pi\kappa_a\), and let \(A_\lambda\) be the corresponding change-of-model operator.

Conjugating \(w^{-1}n(u)\) by \(\delta_a^{-1}\), moving the resulting diagonal factor through the inducing character, and changing variables \(u\mapsto u/a\), yields

\[
M(\pi',\lambda)A_\lambda
=c(\lambda)A_{-\lambda}M(\pi,\lambda),
\qquad
c(\lambda)=\pi^w(\tilde b)|a|_S^{-\lambda}.
\]

The factor \(|a|_S^{-\lambda}\) is important: the Jacobian contributes \(|a|_S\), canceling the extra \(|a|_S^{-1}\) from normalized induction. I obtain the same relation as the manuscript.

### 7. Lemma 7.8(c): differentiation and cancellation of \(\log|a|\)

**Assessment: Correct, including the signs.**  
**Evidence: A.**

Writing \(R=r^{-1}M\) and

\[
\rho(\lambda)=\frac{r(\pi',\lambda)}
{c(\lambda)r(\pi,\lambda)},
\]

one gets \(A_{-\lambda}R(\pi,\lambda)=\rho(\lambda)R(\pi',\lambda)A_\lambda\) and

\[
\frac{\rho'}{\rho}
=\frac{r'}r(\pi',\lambda)
-\frac{r'}r(\pi,\lambda)+\log|a|_S.
\]

In the compact picture,

\[
A'_\lambda=\widetilde H A_\lambda,\qquad
\widetilde H=-\frac12\log|a|_S+H_1(k\delta_a).
\]

The derivative identity contains **two** occurrences of \(-\widetilde H\): one directly and one conjugated by the normalized intertwiner. Their scalar parts contribute \(+\log|a|_S\), canceling the \(-\log|a|_S\) from \(-\rho'/\rho\).

What remains is exactly

\[
d_a(\pi,\lambda)=
\sum_{v\in S_k}
\left(
\frac{r_v'}{r_v}(\pi_v\kappa_a,\lambda)
-\frac{r_v'}{r_v}(\pi_v,\lambda)
\right).
\]

The manuscript's derivative calculation is sound. Because it is central to the conditional theorem, I recommend isolating the scalar cancellation in one displayed equation rather than leaving it inside a long paragraph.

### 8. Lemma 7.8(d): compatibility with (N2)

**Assessment: Correct as a necessary compatibility statement; insufficient as an existence argument.**  
**Evidence: A.**

Applying the relation in point 6 to \((\pi,\lambda)\) and \((\pi^w,-\lambda)\) shows that the respective compositions of unnormalized intertwining operators differ by

\[
\pi(\tilde b)\pi^w(\tilde b)\in\{\pm1\}.
\]

This scalar is independent of \(\lambda\). Therefore the corresponding products of normalizing factors can differ by a constant sign, exactly as part (d) states.

This eliminates one possible conflict with (N2). It does **not** prove that normalizing factors can be chosen globally on quadratic-twist orbits to satisfy all of (N1)–(N5). The manuscript should retain that distinction.

### 9. Existence and reasonableness of (N5)

**Assessment: Reasonable as a hypothesis; not established at all required places. Neither proved nor refuted by this review.**  
**Evidence: A for the reduction of the problem; B (Goldberg–Szpruch and Szpruch's published scope).**

A sufficient form of (N5) would be

\[
r_v(\chi_{\psi,v}\chi,\lambda)
=C_v(\chi)\,F_v(\chi^2,\lambda),
\]

where \(C_v(\chi)\) is independent of \(\lambda\), **and** the resulting \(R_v\) satisfies (N1)–(N4). Because quadratic twisting leaves \(\chi^2\) unchanged, such a construction is plausible.

The obstacle is not the parameter heuristic; it is simultaneous compatibility with involutivity, unitarity, analytic continuation, and the chosen normalization on each orbit. The self-associate cases noted in Remark 2026.18 make naïve transport along twist orbits invalid.

A concrete limitation of the literature is important: **Goldberg–Szpruch's Plancherel-measure paper assumes the residue characteristic is prime to the covering degree \(n\)**. For the double cover \(n=2\), that excludes dyadic fields. It therefore cannot establish (N5) over \(\mathbb Q_2\). Szpruch's earlier local-coefficient work does encompass even residue characteristic, but I did not locate a theorem there asserting the required \(\lambda\)-independence together with (N1)–(N4). Nor did I verify that W.-W. Li's factors in *La formule des traces pour les revêtements de groupes réductifs connexes, II* satisfy (N5).

**Required disposition:** Keep (N5) explicitly conditional. To remove it, the authors need a normalization theorem with precisely this quadratic-twist equivariance, including ramified and dyadic data. The cited literature, as actually checked here, does not yet supply that theorem.

## III. The Waldspurger packet paragraph after Proposition 7.12

### 10. Theta packets versus packets from cuspidal \(PGL(2)\)

**Assessment: The stated distinction is consistent with the verified examples, but its universal formulation needs a more precise source and conventions.**  
**Evidence: A for the theta-character difference; B (Gan–Savin and Adams); not independently established for every cuspidal packet.**

For the theta representations \(r_\psi^\pm\), the stable combination is indeed

\[
\Theta_\psi^+-\Theta_\psi^-,
\]

by Proposition 7.5 and the independently checked \(\Delta_\psi\)-covariance.

For packets associated with cuspidal \(\sigma\) on \(PGL(2)\), the paragraph identifies \(\Theta_{\pi^+}+\Theta_{\pi^-}\) as stable. This is compatible with the Steinberg example and with Adams's real character formulas. But the paragraph should specify its packet-labeling convention, additive character, and source for the general stable-character identity. Gan–Savin supplies the local correspondence and explicit examples; the passage consulted does not by itself state the blanket stable-sum assertion in the manuscript's precise \(\star\)-conjugacy normalization.

I would not delete the claim; I would distinguish a sourced general theorem from the two direct checks that follow it.

### 11. The Steinberg packet \(\{\mathrm{sp},r_\psi^-\}\)

**Assessment: Correct, with the usual local-correspondence conventions.**  
**Evidence: B (Gan–Savin, §5, Steinberg example); A for the virtual-character calculation.**

Gan–Savin explicitly gives the theta correspondences

\[
\Theta_\psi(\mathrm{St}_{SO(3)})=\omega_\psi^{\mathrm{odd}},
\qquad
\Theta_\psi(1_{SO(3)_{\mathrm{anis}}})=\mathrm{St}_\psi,
\]

and the exact sequence

\[
0\longrightarrow\mathrm{St}_\psi
\longrightarrow I_{B,\psi}(|\cdot|^{1/2})
\longrightarrow\omega_\psi^{\mathrm{even}}
\longrightarrow0.
\]

Thus the Steinberg packet has exactly the stated two members. Moreover,

\[
\Theta_{\mathrm{St}_\psi}+\Theta_{\omega_\psi^{\mathrm{odd}}}
=
\Theta_{I_{B,\psi}(|\cdot|^{1/2})}
-(\Theta_{\omega_\psi^{\mathrm{even}}}
-\Theta_{\omega_\psi^{\mathrm{odd}}}).
\]

Both terms on the right are stable under the manuscript's earlier identities. This confirms the asserted stable sum without appealing to a general packet theorem.

### 12. Real discrete-series packets

**Assessment: Correct; add a precise citation to Adams.**  
**Evidence: A; B (Adams, §15, equations (15.7)–(15.8)).**

For weights \(m,m+2,\ldots\) and \(-m,-m-2,\ldots\), with \(m>1\) a half-integer, Abel summation gives the manuscript's two virtual characters:

\[
\Theta_m^++\Theta_m^-=
-\frac{\sin((m-1)\theta)}{\sin\theta},
\qquad
\Theta_m^+-\Theta_m^-=
\frac{i\cos((m-1)\theta)}{\sin\theta}.
\]

The first is even in \(\theta\); the second is odd. This matches stability under the involution \(\theta\mapsto-\theta\).

Adams explicitly constructs the averaged stable genuine discrete-series character and discusses the distinct genuine central characters of the two members. The paragraph should cite his displayed formulas rather than his paper generally.

I did not independently consult Waldspurger's original 1980 and 1991 articles, so the general multiplicity statements attributed specifically to those papers remain source-unverified in this report. Gan–Savin does explicitly recount Waldspurger's correspondence and its epsilon dichotomy.

## IV. Lemmas 7.1–7.3: local cocycles and stable conjugacy

### 13. \(GL(2)\)-conjugation, centralizer sign, and \(\Delta_\psi\)

**Assessment: Correct in the independently checked formulas and examples; no counterexample found.**  
**Evidence: A, including independent exact computations.**

Using Kubota's cocycle, I independently checked the formula

\[
\operatorname{Ad}(\delta_a)(g,\zeta)
=
(\delta_ag\delta_a^{-1},v_a(g)\zeta),
\quad
v_a(g)=
\begin{cases}
1&c\ne0,\\
(a,d)_v&c=0.
\end{cases}
\]

The algebraic identity

\[
(1+\gamma)^2=\gamma\det(1+\gamma)
\]

in \(F[\gamma]\) supplies a short independent derivation of the centralizer sign \((\det h,\det(1+\gamma))_v\).

I also checked the covariance

\[
\Delta_\psi(\operatorname{Ad}(h)x)
=\eta_x(\det h)\Delta_\psi(x)
\]

and hence invariance under the twisted action.

The independent script performed **1,536 Hilbert-symbol consistency checks** and **453 cocycle, conjugation, and covariance checks**, using real, dyadic, and triadic Hilbert symbols. These are tests on selected rational matrices, not a machine proof for every local field.

A particularly useful dyadic example is

\[
\gamma=
\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix},
\qquad
h=\begin{pmatrix}1&-1\\1&1\end{pmatrix}.
\]

Here \(h\gamma=\gamma h\), \(\det h=2\), and \(D^+(\gamma)=16/5\). Over \(\mathbb Q_2\),

\[
(2,16/5)_2=-1,
\]

so \(h\) exchanges the two lifts under ordinary \(GL(2)\)-conjugation, whereas the twisted action fixes the chosen lift. Over \(\mathbb R\), the corresponding sign is \(+1\).

For the manuscript's \(\mathbb Q_3\) example, I independently verified

\[
(-3,-1)_3=(-3,-3)_3=-1.
\]

These examples strongly support the sign convention in Lemmas 7.1–7.3. For readability, one explicit worked dyadic example would be more informative than referring only to random tests.

## V. Lemma 7.6(c) and Theorem 7.7

### 14. The \(\kappa\)-orbital integral and translation by \(-1\)

**Assessment: Correct.**  
**Evidence: A.**

If \(E=F(\sqrt\theta)\) and \(\gamma\) is regular elliptic, then

\[
D^+(\gamma)D^+(-\gamma)
=4-(\operatorname{tr}\gamma)^2
\in-\theta F^{\times2}.
\]

It follows that

\[
\eta_\gamma(a)\eta_{-\gamma}(a)
=\kappa_E(a)(a,-1)_v.
\]

The ordinary action on a lift \(\tilde z\) of \(-I\) introduces precisely the additional factor \((a,-1)_v\). The two factors cancel, leaving \(\kappa_E(a)\). Summing the resulting orbital-integral identity gives

\[
J_G^\kappa(x,f_{\tilde z})
=J_G^{\mathrm{st}}(\tilde z x,f).
\]

I find no missing sign here. This is one of the clearest new identities in Section 7 and merits emphasis.

### 15. The Hasse norm theorem, index two, and stability of \(S_{\mathrm{ell}}\)

**Assessment: Correct, provided the stated global-measure conventions are retained.**  
**Evidence: A (group-theoretic derivation).**

For the cyclic quadratic extension \(E/k\), the Hasse norm theorem identifies \(k^\times/N E^\times\) with its image in \(\mathbb A_k^\times/N\mathbb A_E^\times\). Global reciprocity identifies that image with the kernel of the nontrivial quadratic idele-class character \(\kappa_E\). The index is therefore two.

Thus the indicator of the rational norm classes is \(\frac12(1+\kappa_E)\), yielding

\[
\sum_{\mathcal O\subset GL(2,k)\cdot\gamma}J_{\mathcal O}(f)
=\frac12\,\mathrm{vol}(T_\gamma(k)\backslash T_\gamma(\mathbb A))
\left(J_G^{\mathrm{st}}(\gamma,f)
+J_G^\kappa(\gamma,f)\right).
\]

Combining this with point 14 proves the asserted decomposition of the regular elliptic terms into \(S_{\mathrm{ell}}(f)+S_{\mathrm{ell}}(f_-)\).

The stability assertion for \(S_{\mathrm{ell}}\) follows because each local stable orbital integral is invariant under the twisted \(GL(2)\)-action. This is a **pre-stabilization of the regular elliptic contribution**, not yet an endoscopic transfer identity. The authors correctly make that distinction elsewhere.

### 16. Comparison with Li, Théorème 5.2.6

**Assessment: The coefficients \(1/2,1/2\) are correctly reported; equality with Li's transferred terms is not established here.**  
**Evidence: B (Li, Théorème 5.2.6 and the coefficient formula immediately preceding it).**

Li gives \(\iota(\tilde G,H)=1/2\) when one of \(n'\) or \(n''\) is zero, and \(1/4\) when both are positive. For \(n=1\), the two ordered elliptic endoscopic data are \((1,0)\) and \((0,1)\), so each coefficient is exactly \(1/2\).

However, Li's stable terms are distributions on transferred functions for the endoscopic groups \(SO(3)\), with transfer factors and the appropriate singular contributions. The manuscript's two terms are still distributions on the original cover. The comparison is therefore correct **as a comparison of decomposition and coefficients**, not as a proved identification of distributions.

Suggested correction: replace any wording suggesting direct identification by “the same two-term coefficient pattern as Li's formula; matching the transferred distributions requires the transfer normalization not carried out here.”

## VI. Proposition 7.10 and Example 7.E

### 17. Quadratic-character expansion of the zeta integral

**Assessment: Correct under the stated PID hypothesis on \(\mathcal O_S\).**  
**Evidence: A.**

I independently checked the local square-class Fourier inversion that drives the proof:

\[
\int_{F^\times}h(\xi t^2)\,d^\times t
=
\frac12\sum_{\kappa\in(F^\times/F^{\times2})^\vee}
\kappa(\xi)
\int_{F^\times}h(y)\kappa(y)\,d^\times y.
\]

The constants agree after accounting for the square-map Jacobian and \([F^\times:F^{\times2}]=4|2|_v^{-1}\).

The global decomposition of elements of \(\mathcal O_S\) modulo \(S\)-units then produces

\[
Z(f_z,s)=\frac12
\sum_{\kappa\in\mathfrak X_S}
L^S(s,\kappa)\,Z_S(\Phi_S,\kappa_S,s).
\]

Taking the finite part at \(s=1\) gives the coefficient

\[
a^G(S,u_\xi)=
\frac12\left(c_S+
\sum_{\substack{\kappa\in\mathfrak X_S\\\kappa\ne1}}
\kappa_S(\xi)L^S(1,\kappa)\right).
\]

I find no missing factor of two. The PID assumption should be restated in the proposition's headline, rather than requiring readers to retrieve it from the introductory paragraph.

### 18. Example 7.E: \(k=\mathbb Q\), \(S=\{\infty,2\}\)

**Assessment: Numerical claims verified.**  
**Evidence: A, independent numerical calculation.**

Using

\[
c_S=\frac{\gamma_{\!E}+\log2}{2},\quad
L^S(1,\kappa_{-1})=\frac\pi4,\quad
L^S(1,\kappa_2)=\frac{\log(1+\sqrt2)}{\sqrt2},\quad
L^S(1,\kappa_{-2})=\frac{\pi}{2\sqrt2},
\]

I obtain

\[
a^G(S,u_1)=1.5772627804040047
\]

and, for the class with negative real component and trivial \(2\)-adic square class,

\[
a^G(S,u_\xi)=-0.3188561175330352.
\]

Both agree with the manuscript's rounded figures.

The 16 local square classes reduce to four coefficient values because the coefficient is unchanged by multiplication by a diagonal \(S\)-unit. This is also correct. A short table of the four values would be a useful improvement.

## VII. Theorem 7.13 and the limits of the result

### 19. Dependence on (N5)

**Assessment: The theorem is appropriately conditional, but the scope of the condition can be stated more precisely.**  
**Evidence: A, tracing the arguments.**

Theorem 7.13 assumes (N5) at the outset, which protects the conditional statements. Nevertheless, it is worth distinguishing:

- The regular elliptic decomposition, the unipotent coefficient formula, and the theta-character identity are not derived using (N5).
- Equivariance of the normalized weighted distributions \(I_A\), and the subsequent applications of that equivariance, do use (N5).
- Stable principal-series characters do not require (N5), as Proposition 7.9(c) already notes.

I recommend stating this dependency map immediately before Theorem 7.13, perhaps as a three-sentence paragraph. It will prevent readers from interpreting the entire section as conditional.

### 20. Theorem 7.13(c): “Every term ... is an eigendistribution”

**Assessment: This statement needs correction.**  
**Evidence: A.**

The theorem lists the eigencharacters of *individually indexed* distributions such as \(J_G^{\mathrm{st}}(\gamma,\cdot)\), \(I_A(a(t),\cdot)\), and \(J_{\mathrm{unip}}^\kappa(z,\cdot)\).

But a sum of eigendistributions with **different** eigencharacters is generally not itself an eigendistribution. In particular, the grouped expressions \(S_{\mathrm{ell}}\) and the sums over \(t\) or \(\kappa\) need not have one ordinary \(GL(2,k_S)\)-eigencharacter.

**Corrected wording:**

> The individually indexed distributions occurring in (a) transform by the indicated characters. Their displayed sums need not be eigendistributions under the untwisted action. In particular, \(S_{\mathrm{ell}}\) is stable for the twisted action, not generally an eigendistribution for the ordinary action.

I regard this as a genuine statement-level error, although it does not invalidate the underlying calculations.

### 21. “What the theorem does not say”

**Assessment: Accurate and important.**  
**Evidence: A; B (Li's stabilization framework).**

The manuscript properly separates its pre-stabilization from a full identity \(I(f)=S(f)+S(f_-)\) with an endoscopic transfer to \(SO(3)\). It acknowledges the missing singular elliptic limits, stabilization of weighted terms, transfer and fundamental lemma, and packet treatment of the remaining cuspidal spectrum.

I found no additional passage that unequivocally claims the *full* stabilized trace formula has been proved. Some introductory language (“this is the shape of Li's stable trace formula”) should be tied explicitly to the comparison of shape, as in point 16.

## VIII. Consolidated classification

### Errors requiring corrected statements

**E1.** Theorem 7.13(c), “Every term ... is an eigendistribution,” is too strong for the grouped sums. Correct as in point 20.

### Gaps or incomplete justifications

**G1.** Proposition 7.5: supply the compact-open fixed-vector argument and a uniform Gauss-shell lemma (points 2–3).

**G2.** Proposition 7.5: specify an archimedean kernel-and-trace theorem and expand the conjugation/partition-of-unity reduction (point 4).

**G3.** Existence of normalizing factors with (N1)–(N5) at ramified and dyadic places remains unproved (point 9).

**G4.** The general stable-sum statement for all cuspidal \(PGL(2)\) packets needs a precise theorem and compatible packet labels (point 10).

### Statements that are correct or plausible but have an insufficient stated justification

**J1.** Thomas's Theorem 1C cannot determine the exact Kubota-coordinate sign because it is explicitly stated up to sign (point 5).

**J2.** Lemma 7.8(d) establishes compatibility with one involutivity constraint, not existence of factors satisfying (N5) (point 8).

**J3.** Li's \(1/2+1/2\) coefficient pattern is confirmed, but equality with transferred \(SO(3)\)-distributions is not obtained by that numerical comparison (point 16).

### Citations inaccurate in scope or not independently confirmed

**C1.** Maktouf is not an adequate direct reference for the archimedean Schwartz-kernel claim; cite a precise archimedean result, preferably in Thomas (point 4).

**C2.** Goldberg–Szpruch excludes dyadic residue characteristic under its standing assumptions, and therefore cannot establish the dyadic case of (N5) (point 9).

**C3.** I did not confirm a theorem in Szpruch 2009 or Li II that gives exactly (N5), nor did I match Thomas 2013's metaplectic-coordinate factor to the manuscript's Kubota normalization (points 5 and 9).

**C4.** I verified the local Steinberg packet from Gan–Savin and the real stable discrete-series formula from Adams, but not the original Waldspurger multiplicity assertions directly from Waldspurger 1980/1991 (points 10–12).

### Notation and exposition

**R1.** In Lemma 7.8, put \(\pi'\), \(A_\lambda\), \(c(\lambda)\), \(\rho(\lambda)\), and \(d_a(\pi,\lambda)\) in a short preliminary notation paragraph.

**R2.** Distinguish ordinary \(GL(2)\)-equivariance, twisted stability, and endoscopic transfer at the beginning of §7; these are three different assertions.

**R3.** Keep the distinction between the regular-set character identity and its distributional extension visible throughout Proposition 7.5.

**R4.** Add one worked dyadic cocycle calculation and a four-value table for Example 7.E.

## IX. Three most important changes

**First:** Complete Proposition 7.5's analytic presentation, especially the uniform nonarchimedean Gauss-integral argument and the precise archimedean smoothing citation. The character formula is foundational for the section's notion of stability.

**Second:** Preserve (N5) as an explicit unproved hypothesis, but formulate the exact local normalization theorem needed to remove it. Do not imply that Goldberg–Szpruch handles the dyadic case. The derivative calculation in Lemma 7.8 is correct; the existence of the required factors is the real outstanding issue.

**Third:** Correct Theorem 7.13(c)'s eigendistribution wording and distinguish rigorously between the paper's regular elliptic pre-stabilization and Li's fully transferred stabilized formula. This will make the scope of the paper's contribution unmistakable.

**Overall recommendation:** Major revision, not rejection. The new Section 7 contains valuable, apparently sound local calculations and a useful explicit reorganization of the regular elliptic terms. The priority should be to strengthen the analytic justifications and accurately delimit the normalization and transfer claims, rather than to recast the section's mathematical program.

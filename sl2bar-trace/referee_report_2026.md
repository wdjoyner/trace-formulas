# Referee report: A hitch-hiker's guide to the metaplectic trace formula for SL(2)

November 10, 2026 · Referee: Claude (Anthropic), for David Joyner

Copy of the referee report kept in [Claude Docs](https://claude.ai/artifact/7MmqhX7GnoJNup9xbb9RNG). Item numbers match `revision_log.md`. Section numbers refer to `original-1995/cctrace_new.tex` as compiled.

## Summary and overall assessment

Recommendation: major revision. The manuscript is a useful expository roadmap, but in its present form several foundational statements are wrong, the spectral side is incomplete, and the invariant and stable sections rest on conjectures and unpublished preprints.

The paper (dated 1-27-95, revised 6-2002) aims to adapt Arthur's trace formula, first non-invariant and then invariant, to the n-fold Kubota cover of G = Res_{k/Q} SL(2), where k contains the n-th roots of unity. It then sketches a partial stabilization along the lines of Labesse–Langlands [LL], using GL(2)-conjugation as stable conjugacy. Files reviewed: cctrace_new.tex (the LaTeX2e master), cctrace1.tex (the older Scientific Word master), cctrace2–7.tex and cctracer.tex. The master also inputs cctrac3b.tex, which was not supplied with the article. It is book7d.tex from the 1997 book manuscript, which holds Sections 4.3–4.5 (basic properties, the equivalence relation, weighted unipotent orbital integrals). The appendix at the end reviews it.

Strengths:

- It is a clear, concrete specialization of Arthur's machinery to the simplest rank-one case, with the SL(2) values of τ, τ̂ and σ written out explicitly. These checks are correct: σ_B^B = 0, σ_B^G = τ_B, and k^T(x) = F^G K_G + Σ τ_B F^B (K_G − K_B).
- The rank-0 section (the Heisenberg-type cover of the torus) is a good warm-up.
- The splitting of the cover over B(Q) by b ↦ (b,1) is correct. On B the cocycle is (d_2, d_1)_n, and its global product is trivial by the product formula. The paper should say this explicitly, because Eisenstein series and the truncation operator depend on it.

Main problems, detailed below:

1. Foundations of the cover (local splittings, the global cocycle, and the global cover as a quotient, not a subgroup, of the restricted product) are misstated.
2. The genuine-function and genuine-representation conventions make R(f) vanish on the space they are meant to act on.
3. The unipotent and residual contributions are missing or mishandled. This includes the claim that the residual spectrum contributes nothing.
4. Several explicit SL(2) computations have errors: the weight function v_O, u'_B, M_B^T, and the archimedean and p-adic weight v_A.
5. The invariant and stable sections depend on conjectures that are now theorems (Wen-Wei Li), and on unpublished preprints [J1], [J3].

## Major issues I: the cover, conventions, global construction

1. **The local splitting over K is not k ↦ (k,1).** Kubota's cocycle β is not trivial on SL_2(O) × SL_2(O) when |n|_v = 1. It is a coboundary there: the splitting is k ↦ (k, κ(k)), where κ(k) = (c,d)_n if 0 < |c| < 1 and κ(k) = 1 otherwise. Lemma 2.2(b) holds abstractly, but the text before Lemma 2.4 identifies K with the image of k ↦ (k,1). It then says this image is a subgroup "if p|n", which is backwards; the image is not a subgroup in either case. The same identification is used in Lemma 2.8, in Section 2.1.4 (bi-K-invariance), in the global NAK lemma, and again in 7.4 ("identify K with a subset (K,1)"). Every K-invariance statement should use the correct section. This also corrects the stated reason why the global product converges (item 3).
2. **Lemma 2.2(c): "split over K_m for m ≥ n" is not the right condition.** Splitting over K_m holds once 1 + π^m O lies in F^{×n}, together with a compatibility on the off-diagonal entries. The threshold depends on the ramification (roughly m > v(n) + v(π)·e/(p−1)), not on n. Please either state "for m sufficiently large" with a reference such as [KP] or Moore [M], or give the precise bound.
3. **The global cocycle ∏_v β_v does not converge as written.** For g_1, g_2 in K_v, the value β_v(g_1, g_2) can be nontrivial when x(g_1 g_2) has positive valuation, so "by Lemma 2(b)" does not apply. The standard construction (Kubota [K2], Gelbart [Ge2], [KP]) uses the modified local cocycles β_v·∂κ_v, which are trivial on K_v × K_v at almost all v. Equivalently, one takes the restricted product of the local covers relative to the subgroups (K_v, κ_v(K_v)) and divides by {(ζ_v) : ∏ ζ_v = 1}. This choice also determines the G(Q)-splitting (2.9): s_A(γ) = ∏ s_v(γ) is exactly the finite product of the κ-corrections. As written, (2.9) and the definition of β_A belong to different normalizations.
4. **The global cover is a quotient, not a subgroup, of ∏' of the local covers.** Section 2.2 ("we may identify G(A)-bar with a subgroup of the restricted direct product") and Section 3.1 ("there is an embedding A(A)-bar ↪ ∏' of the local covers of k_v^×") should both say quotient by the kernel of the product map ⊕μ_n → μ_n. This matters later: factorizability of genuine representations (Lemma 3.1, Example 5.3, Lemma 7.19) is a statement about this quotient.
5. **The genuine conventions are inconsistent, so R(f) vanishes on L²_gen.** Section 2.1.4 calls f genuine if f(g,ζ) = ζ f(g,1). Section 3.1 calls a representation genuine if π(g,ζ) = ζ^{-1} π(g,1), and functions with that property "anti-genuine". On the space L²(G(Q)\G(A)-bar)_gen of genuine functions, the right regular representation satisfies R(ζ) = ζ. So for genuine f, R(f)φ(x) = ∫ f(y) φ(xy) dy picks up ∫_{μ_n} ζ² dζ, which is 0 unless n | 2. The fix is the one Li adopts: genuine representations with π(ζ) = ζ, and anti-genuine test functions with f(g,ζ) = ζ^{-1} f(g,1). The convention should be stated once and used everywhere, including Sections 3.3, 4.1, 5.3 and the kernels.
6. **The center is not a direct product in general.** In Lemma 2.2(e), (−1,ζ)² = (1, (−1,−1)_n ζ²). Here (−1,−1)_n can be nontrivial, for example when n = 2 at a real place. So p^{-1}({±1}) is an extension of {±1} by μ_n, possibly cyclic of order 2n. The same correction applies to Lemmas 2.3(e) and 2.6(d).
7. **NAK uniqueness (Lemmas 2.4 and 2.9).** In g = nak, the factor a is determined modulo A ∩ K, not modulo the center. What is well defined is H(g). Please restate these lemmas accordingly.
8. **Lemma 2.2(g)** (preimages of anisotropic tori are abelian) is attributed to "[Fl, p. 128]", but that reference has no volume, and the claim carries much weight in Section 7. For general n, the commutator pairing on the preimage of T = E^1 needs an argument or a precise citation. Lemma 2.2(h) uses n both for the degree of the cover and for a unipotent matrix. It should be stated for the canonical lift of gNg^{-1}, because u ↦ (u,1) is not a homomorphism on lower-triangular unipotents for Kubota's cocycle.
9. **Index of the split component.** A_G should be the trivial group, not {±1}: A_P means the split component of the center. Also, for G = Res_{k/Q} SL(2), A_B is the Q-split part of Res_{k/Q} G_m, which is 1-dimensional. That is why 𝔞 = R. But H(g) = log|t|_{Q_p} must then mean the norm ∏_{v|p} |t_v|_v, not the max used in 2.1.2. Please distinguish the two.
10. **Iwasawa measure.** "dg = δ_B(a)^{1/2} dk da dn, g = kan" is incorrect. For g = kan the measure is dg = δ_B(a) dk da dn; for g = nak it is δ_B(a)^{-1} dn da dk. Section 4.1.1 also uses δ(a) dn da dk for the Siegel domain, which should be δ(a)^{-1}.

## Major issues II: the trace formula itself

### Rank 0 (Section 3)

1. **Stabilizer condition.** Q^×_{p,δ} is defined as {x : (x,δ)_n = 1}, but conjugation acts through (x,δ)_n² (Lemma 2.2(f) and Remark 3.7). The stabilizer is {x : (x,δ)_n² = 1}; the two differ when n is even.
2. **Theorem 3.2 is misstated.** Genuine irreducible representations of a Heisenberg-type cover are parametrized by genuine characters of its center, which is the preimage of A^N with N = n/gcd(n,2). They are not parametrized by "characters of the form χ^N of A(A)^1". Matching them with characters of A^N needs a chosen splitting over A^N, which the text does not specify. The theorem is also stated for all genuine irreducible representations, while the proof (Poisson summation and Claims 1–2) only treats automorphic ones (m > 0), matched with characters of A(Q)^N \ A(A)^{1,N}. Please restate it as a correspondence of automorphic spectra.
3. **A Hasse principle is used without comment.** Equation (3.18) passes from δ ∈ A(Q) ∩ A(A)^N to δ ∈ A(Q)^N. This holds because μ_N ⊂ k: by Kummer theory and Chebotarev, a local N-th power at almost all places is a global N-th power, so Grunwald–Wang exceptions cannot occur. Please state this; it is the only place where the hypothesis μ_n ⊂ k enters the rank-0 argument.
4. **Mackey/Clifford.** "Not self-conjugate" is vacuous as defined, since h ∈ C always fixes χ. The irreducibility statement needs C to be a maximal abelian subgroup and χ^h ≠ χ for h ∉ C. Lemma 3.4 is ordinary Clifford theory; [GeKn, Lemma 2.1] concerns restriction from GL(2) to SL(2) and does not seem to be the right citation. In (3.20), the induction is from A^N, which is not maximal abelian, so that induced representation is a multiple of an irreducible one, which conflicts with the earlier use of C_p. The cocycle (3.2) simplifies to (t_2, t_1)_n, so the cocycle identity is immediate and does not need the long verification mentioned.

### Geometric side (Section 4)

5. **The weight function v_O(x,T) = 2(T − H(x)) is wrong.** It is not left A(A)-invariant, yet it is integrated over G_μ(A)\G(A). For a regular split class, unfolding gives both parabolics containing A, so the weight is 2T − H(x) − H(wx) up to Arthur's normalization. That expression is invariant under x ↦ ax because H(wax) = −H(a) + H(wx). The step from Σ_{δ∈P(Q)\G(Q)} τ̂_P(H(δηx) − T) to τ̂_P(H(ηx) − T) in (4.3)–(4.4) is where the w-term was lost. The statement that G_μ is G or a Cartan should also read: G_μ is a Cartan subgroup, since the classes O are unramified, and the case G_μ = G only occurs for ±1. book7d.tex (the missing cctrac3b.tex) already has the corrected weight v(x,T) = 2T − log δ(x) − log δ(wx). cctrace3.tex should be brought into line with it, after checking the factor: log δ = 2H.
6. **Central classes.** The formula (4.5) for μ = ±1 keeps only the f(μ)-term. The class O of ±1 also contains ±(unipotent) elements, whose weighted unipotent integrals are the hard part of the analysis. cctrac3b.tex (book7d.tex) handles these through J_unip and the coefficients a^G(S,u), and the book's version of 5.4(a) (book7f.tex) sums over γ ∈ O. But Section 5.4(a) of cctrace5.tex lists only a^G f(z) + ½ a^A J_A(z,f). The unipotent orbital integrals a^G(S,zu) J_G(zu,f) over the (G,S)-classes are missing; they do appear in 6.4(a).
7. **Proof of Lemma 4.4.** The argument reduces to the unipotent sum over Γ_0 ⊂ N and Poisson summation at the archimedean place. Two points are not addressed: (i) why the terms γ ∉ B(Q) vanish on the Siegel set for large T (compact support of f), and (ii) the sum over μ ∈ A(Q) in K_B. Poisson summation over the compact quotient N(Q)\N(A) is cleaner adelically, and it is legitimate because the cover splits canonically over N. In the integrand, μ is undefined. Corollaries 4.5–4.7 claim per-class T^{-C} bounds that the given proof does not establish; Arthur proves the needed per-class estimate in [A2, §7] and polynomiality in [A12].
8. **Proposition 4.8 (K_O^T polynomial for each O)** is stronger than what Arthur proves, and its proof is announced but not given, in cctrac3b.tex (book7d.tex) either. Please state which of k_O^T and j_O^T defines J_O^T, and cite the precise result.

### Spectral side (Section 5)

9. **The residual spectrum is not empty.** The Introduction says there is no analog of the residual term [LL, (5.5)]. For n-fold covers, the residues of Eisenstein series give the theta representations: the Weil representation for n = 2 (Gelbart [Ge2] is about exactly this) and Kubota–Kazhdan–Patterson theta functions in general. These are part of the discrete spectrum and must appear on the spectral side, alongside the cuspidal terms.
10. **Ramified classes χ are omitted.** Theorem 5.31 assumes χ is unramified, which by Example 5.32 means μ^w ≠ μ. The classes with μ^w = μ, which give the analog of the −¼ tr(M(w,0) I_B(μ,f)) term of Jacquet–Langlands and Gelbart–Jacquet, never appear. Section 5.4(b) also needs the factor and sign checked. Arthur [A14, Thm 8.2], or Li III, covers the general case.
11. **Example 5.32: the sign is right; a factor of 2 is wrong.** The author worries that the minus sign is a mistake. It is not: the continuous term is −(1/4π)∫ tr(M(−it)M'(it) π_it(f)) dt, in agreement with [LL]. However, with the stated identification ς(T) = 2ςT and ς(α^∨) = 2ς, the limit is (1/2)(4T·I − M^{-1}M') = 2T·I − ½M^{-1}M', not 4T·I − M^{-1}M'. The final step forgot to divide by ς(α^∨).
12. **Lemma 5.28 is not proved.** The proof establishes at most absolute convergence, not K_χ^T = J_χ^T. The claim that Λ_2^T K_χ(x,x) is compactly supported is false: it is rapidly decreasing. The proof of Lemma 5.29 ("K_P is continuous, hence integrable") is not a proof. The metaplectic Maass–Selberg relations behind Theorem 5.31 should be cited, for example Mœglin–Waldspurger [MW2], which allows finite central covers.
13. **Example 5.24 confuses E_G and E_B.** For χ = (G,ρ) cuspidal there is no Eisenstein series: K_{G,χ}(x,y) = Σ (π(f)φ)(x) times the conjugate of φ(y). For χ = (A,μ), K_{G,χ} = ½∫ Σ E(x, I_B(π,f)φ) times the conjugate of E(y,φ), plus the residual part. The "I_B(π,f)φ(x)δ_B(x)" term belongs to K_{B,χ}. Example 5.25 inherits the error. Example 5.5 should read ρ = ρ' or ρ = ρ'^w, and B is associate to itself, not only to its opposite.

### Invariant form (Section 6)

14. **Conditional status.** Conjectures 6.2–6.5 and 6.6 (normalized intertwining operators) are hypotheses of the main theorem of Section 6, so the invariant trace formula is conditional as written. The abstract should say so, or better, cite Li II (2012), which proves the local trace formula, the tempered invariant Paley–Wiener theorem, and the normalization of intertwining operators for covers, and Li IV (2014). The cover here has only complex archimedean places when n > 2, and Mp(2) at real places when n = 2.
15. **Example 6.1 sign.** u'_B(k,y) = −H_B(ky), not |H_B(ky)|. Computing ∫(1_{X>0} − 1_{X>−H}) dX gives −H in both cases H > 0 and H < 0.
16. **6.4(b) is incomplete and inconsistent with 7.8(g).** With the remark "I_A(π,f) = 0 for π tempered", 6.4(b) is identically zero. But the global normalizing factor term −(1/4π)∫ (m'/m)(μ_it) tr(I_B(μ_it,f)) dt is invariant and survives. It reappears in 7.8(g), so 6.4 should contain it. The global m(σ) is never identified; for these covers it is a ratio of Hecke L-functions of μ^N, given by the metaplectic Gindikin–Karpelevich formula (Kubota, [KP]). It should be written down, since it is what makes the formula usable. The book version (item (e) of book7g.tex and book7gnw.tex) does include this term, as a^G(I_A(σ)) = −m'(σ)/m(σ); cctrace6.tex dropped it.
17. **Condition (b) in I_N(G)_Γ (equation 6.7) is circular.** It defines φ(σ,X) in terms of itself. The intended definition is φ(σ,X) = ∫_{i𝔞*} φ(σ_Λ) e^{−Λ(X)} dΛ.

### Stable form (Section 7)

18. **The action of GL(2) on the cover needs a definition.** β is only defined on SL(2), so "the n-fold cover of G_1 defined using β in §2.1" does not determine a cover of GL(2). There are several, for example the Kazhdan–Patterson twists. Please fix one and check that it restricts to Kubota's cover. More importantly, the preimage of T_1 = E^× in the GL(2)-cover is in general not abelian. Conjugation by t ∈ T_1 then multiplies γ ∈ T-bar by a root of unity ε(t,γ), so δ ↦ I_O(f^δ) is a function on D(T/F) only up to a character. This needs to be resolved before (7.5)–(7.7) make sense.
19. **Global D(T).** T(Q) is not discrete in T(A_S) for finite S, so Proposition 7.1 should be over T(A) with the unit functions outside S. By the Hasse norm theorem, D(T/Q) = Q^×/NE^× injects into D(T/A) with index 2, so κ runs over two characters. The index [D(T/Q):D(T/A_S)] should be inverted. Lemma 7.3(a) as stated is about I^{st}_O, not SI_O.
20. **A-elliptic terms (7.4).** With T_1 = Cent(A, G_1), the diagonal torus of GL(2), one gets D(A/F) = 1. The paper instead uses A·Z, giving F^×/F^{×2}. That may be deliberate: on the cover, diag(a,1) acts on A-bar through Hilbert symbols. If so, the relevant quotient is governed by (·,·)_n, so F^×/F^{×2} must be justified. Globally, Q^×/Q^{×2} does not embed in the finite group D(A/A_S), so the index in (7.9) is undefined.
21. **Equation (7.17) diverges.** The sum over rational unipotent classes a ∈ Q^×/Q^{×2} has infinite fibers over Q_S^×/Q_S^{×2}. This is why Arthur uses the coefficients a^G(S,u) and [LL] use zeta-function regularization (the S_3 term). The middle equality is also wrong: Σ_κ Σ_a κ(a)X(a) = [group]·X(1), not Σ_a X(a).
22. **Weight v_A in (7.13).** √|1+n_v²| is the real-place formula. At complex places it is √(1+|n_v|²) (up to normalization), and at p-adic places it is max(1,|n_v|_v).
23. **Statements deferred to [J3].** Lemmas 7.6, 7.9, 7.11, 7.12, 7.18 and 7.20, the stability of I_G(γ,f), and the local conjectures in [J1] are all deferred to preprints. Lemma 7.18 states no assertion. Lemma 7.13's statement has a missing "=" and a γ-dependent constant c inside a limit. Remark 7.17 (#L(π) = ∏ #(k_v^×/k_v^{×2}) for every genuine π when n > 1) is unproved and needs at least an argument that each non-square class acts nontrivially. Conjecture 7.21 (stability of S) is the crux of stabilization. If [J1] and [J3] have since appeared, for instance as the invariant-distributions paper, please cite the published versions; otherwise mark these results as conditional in the abstract.

## Minor issues and typos, by section

| Place | Issue | Suggested fix |
| --- | --- | --- |
| Intro, line 79 of cctrace_new | The line "%\overline{G(\aaa)}$ on the space of square-integrable" is commented out, so the sentence reads "…representation of genuine cups forms" | Remove the %, and change "cups" to "cusp" |
| §2 Notation | "ν(π) = q^{-1}" | ν(π) = 1 and \|π\| = q^{-1} |
| Lemma 2.2(d), 2.3(d) | The archimedean splitting is relevant only for n = 2 | Say so; for n > 2 every archimedean place is complex and the cover is trivial there |
| Remark after Lemma 2.2 | "maximal comapct"; the remark about the n-fold covers of SU(2,C) is trivially true because the cocycle is trivial over C | Typo fix; shorten |
| §2.1 | β_p(g_{1,v}, g_{2,v}) under ∏_{p≤∞} | Index p, not v |
| Lemma 2.4 | "({\rm mod}\;Z(G(\qqq_p))" has an unbalanced parenthesis; K_p is undefined (K_0 is meant) | Fix |
| §2.1.3 | ϖ is called "the dual root"; it is the fundamental coweight. The coroot is α^∨ = X_α. "X_alpha" is missing a backslash | Fix terminology and typo |
| §2.1.4 | Spherical Hecke algebra stated for (p,2n) = 1, but Lemma 2.2(b) has (p,n) = 1 | Make consistent |
| Lemma 2.5 | Stated over G(A) before the global H is defined | Move it to §2.2 |
| Lemma 2.7 | K_∞ is not open; for simply connected G, strong approximation gives a single Γ | Use K_f compact open; note the coproduct has one term |
| Lemma 2.8(d) | For SL(2), ‖x^{-1}‖ = ‖x‖ | N = 1 |
| §2.2.4 | "Spherical in the sense of 2.1.4" | Must be the unit element of the Hecke algebra (with the κ-splitting) for almost all p |
| §3.1 | "Let μ_n act on G(A) = A_k^×"; A(A)^1 "as in the previous section" is never defined; (3.3) uses β(g_1,g_2) for β(g,g') | Fix |
| §3.2 | "C_p = A(R)^N" for p < ∞; (3.9) has a subscript A_p where C_p is meant | A(Q_p)^N; C_p |
| (3.12), (3.14) | f̄(x) should be f̄(y); the centralizer is written "{A ∈ … \| ghg^{-1} = h}" | Fix variables |
| (3.15), Thm 3.6 | The last line is Σ_x; it should be an integral, since A_δ\A is compact but not finite globally | ∫ |
| (3.16) | s_A(δ) appears inside a local factor | s_p(δ) |
| Lemma 3.8(c) | "Unit maps to unit" requires normalized counting measure on Q_{p,y}^×\Q_p^× | State the normalization |
| Claims 1–2 | lim_{n→∞} should be lim_{m→∞}; f_n should be f_m. Exchanging the limit with the infinite spectral sum needs justification | Fix and justify |
| (3.21)–(3.22) | Refers to "§4.3.1 below", which does not exist | Fix the reference |
| Lemma 4.1 | K_P = Σ K_O should be Σ K_{P,O}. The kernel f(xγy^{-1}) conflicts with f(x^{-1}γy) used later. The proof line φ(n^{-1}γ^{-1}g) is garbled | Use Arthur's convention throughout |
| §4.1.1 | The constants u ≥ 1/2 and T_0 > √3/2 are for SL_2(Z) over Q; ω is used both for a set and for ϖ; "T_0 > T_1" reverses Arthur's roles; N in Lemma 4.2 is unused | Fix |
| Cor. 4.6–4.7 | The absolute value is misplaced: \|k^T_O dx − …\|dx | Fix |
| §4.2 | ς is used for unipotent elements and also for elements of μ_n | Rename |
| §5 intro | "Lemma 1.7", "(4.5)", "Proposition 4.14", "Theorem 6.15", "4.1.1" are stale | See the cross-reference section |
| Lemma 5.1 | "Each occurring with finite multiplicity" is false for arbitrary discrete Γ | Add cofinite volume and type I, and say "direct integral" |
| §5.3 | k^T_χ uses K_{P,χ}(x,x) instead of K_{P,χ}(δx,δx); (5.9) has "since the volume of N(Q)\N(A)" with the sentence unfinished | Fix |
| §5.4 | S and A_S are used before §6 defines them; "given in section 5" should point to §4 or cctrac3b | Fix |
| §6 intro | "(3.1)" should be (6.1); "One of the objects to this subsection"; f_S should be f^S | Fix |
| Conj. 6.6(1) | R I_P = I_P R should be R_{P'\|P} I_P(χ,x) = I_{P'}(χ,x) R_{P'\|P} | Fix |
| After Conj. 6.6 | "follow either from [Sa]": Sally treats the universal cover of SL_2(R); here n = 2 gives Mp_2(R), and n > 2 gives only SL_2(C) | Cite appropriately |
| Thm 6.23 | v_π should be ν_π | Fix |
| §7.5 Def. 7.11 | T_1(F) = E^{×1} and T_1(F) = E^× both appear | Fix |
| (7.25) vs (7.1)–(7.2) | Signs and the factor ¼ do not match; E_H^G is undefined | Reconcile |

## Cross-references, bibliography, LaTeX

With an empty stub for the missing cctrac3b.tex, cctrace_new.tex compiles with pdflatex. The only warning is the duplicate label Sh. cctrace1.tex needs Scientific Word's tcilatex and cannot be built with a standard TeX installation. cctrace5.tex and cctrace7.tex use the macros `\aaa` and `\qqq`, which only cctrace_new.tex defines.

**Cross-references.** Almost every reference is hard-coded, and equations are numbered globally as (1), (2), …, not (2.1). As a result, most references point to the wrong place or to nothing. Examples: "Lemma 2(b)", "(2.1–2.3)", "(1.10)", "(1.12)", "Lemma 1.7", "Lemma 6.9 above", "Lemma 5.28", "Theorem 6.31", "Example 6.32", "Lemma 7.16", "section 2.7", "subsection 5.1.1", "(6.14)", "(7.22–24)", and "4.????". Recommendation: add `\numberwithin{equation}{section}` and replace every hard-coded reference with `\label`/`\ref`, and every [A2]-style reference with `\cite`.

**Preamble.** amsgen is an internal package and should not be loaded; amsfonts as a class option does nothing. `\def\qed` overrides amsthm's `\qed`. Proofs should use the proof environment rather than "proof:" and a hand-typed box. `\printindex` and makeidx are present but there are no `\index` entries. The obsolete `\Bbb`, `\frak` and `\cal` compile, but `\mathbb`, `\mathfrak` and `\mathcal` are the modern forms. The contact address in the Introduction is out of date.

**Bibliography corrections.**

| Entry | Problem | Correction |
| --- | --- | --- |
| [KP] | Year | Publ. Math. IHES 59 (1984), 35–142 |
| [LL] | Volume and pages | Canad. J. Math. 31 (1979), 726–785 |
| [J2] | Volume | Israel J. Math. 61 (1988), 113–154 |
| [Fl] | Incomplete | Invent. Math. 57 (1980), 119–182 |
| [GeKn] | Coauthor | A. W. Knapp |
| [PR] | Spelling | M. S. Raghunathan |
| [A13], [A14] | Listed as preprints | Amer. J. Math. 104 (1982), 1243–1288 and 1289–1336 |
| [A16] | Listed as preprint | J. reine angew. Math. 452 (1994), 163–217 |
| [L4] | No series number | Ann. of Math. Studies 96 (1980) |
| [MW1] | Listed as preprint | Ann. Sci. ÉNS 22 (1989), 605–674 |
| [Sh] | Duplicate entry | Delete one copy |
| [M], [Se], [Ko1] | Cited but missing | Add Moore (Publ. IHES 35, 1968), Serre's *Linear representations of finite groups*, and Kottwitz |
| [J1], [J3] | Preprints carrying key results | Cite published versions, or state what remains unproved |

## Literature since 1995 and recommendations

The central claims of Sections 4–6 have since been proved in general by Wen-Wei Li. Any revision should be organized around his results: the paper's value would then lie in the explicit SL(2) computations and in the stabilization attempt of Section 7, rather than in re-deriving Arthur's general machinery.

- [Li I, "Le développement géométrique fin"](https://arxiv.org/abs/1004.4011): the fine geometric expansion for covers, including Brylinski–Deligne covers. It uses anti-genuine test functions, which is the convention issue in Major issues I, item 5.
- [Li II, "Analyse harmonique locale"](https://arxiv.org/abs/1107.1865), Ann. Sci. ÉNS 45 (2012), 787–859: Plancherel, normalization of intertwining operators, local trace formula, and the tempered invariant Paley–Wiener theorem for local covers. These are the paper's Conjectures 6.2–6.6.
- Li III, "Le développement spectral fin", Math. Ann. 356 (2013), 1029–1064 ([arXiv](https://arxiv.org/abs/1107.2220)): the fine spectral expansion, covering the ramified χ and the discrete and residual parts missing from Section 5.
- [Li IV, "Distributions invariantes"](https://eudml.org/doc/275551), Ann. Inst. Fourier 64 (2014), 2379–2448: the invariant trace formula for adelic covers, assuming the invariant Paley–Wiener theorem at real places. That hypothesis holds for the covers considered here.
- Li, "Transfert d'intégrales orbitales pour le groupe métaplectique", Compos. Math. 147 (2011), 524–590: endoscopic transfer for Mp(2n). This is the relevant comparison point for the n = 2 case of Section 7.
- Also relevant: Flicker–Kazhdan, "Metaplectic correspondence" (Publ. IHES 64, 1986), and Mezo's invariant trace formula comparison for metaplectic GL(n). For the dual-group view of what "stable" should mean for n-fold covers, see Weissman and Gan–Gao on L-groups of Brylinski–Deligne covers.

Recommendations:

1. Fix the foundations in Section 2: the κ-splitting, the global cover as a quotient, and a single genuine/anti-genuine convention. Then recheck every place that uses them.
2. Supply or merge cctrac3b.tex, and make the central-class (unipotent) contributions explicit and consistent across 4.5, 5.4 and 6.4.
3. Rewrite the spectral side to include the residual (theta) spectrum and the classes with μ^w = μ, and identify the global normalizing factor m explicitly.
4. Present Sections 4–6 as "Li's theorems specialized to SL(2)", with the explicit SL(2) formulas as the contribution. Correct v_O, u'_B, the factor in M_B^T, and v_A.
5. Present Section 7 explicitly as a program. Before claiming stabilization, define the GL(2)-cover and its conjugation action, resolve the non-abelian preimage of T_1, and justify the choice of D(A/F) and the L-packet sizes.
6. Convert all cross-references to \label/\ref and \cite, and correct the bibliography as tabulated above.

In its revised form the paper would be a worthwhile worked example. As it stands, a reader could not rely on its formulas without independently checking each one.

## Appendix: cctrac3b.tex is book7d.tex

book7d.tex fits the gap exactly. Its subsections are Basic properties, An equivalence relation on G(Q), The definition of J_M(u,f), and A more explicit form of the geometric terms. These hold the Proposition 4.18 that cctrace6.tex cites (the fine expansion of J_O), Example 4.14 (J_A(z,f)), and the definitions of J_unip and a^M(S,γ). The other book files line up with the article the same way:

| Article file | Book file | Contents |
| --- | --- | --- |
| cctrace_new (intro) | book7a | Introduction |
| cctrace2 | book7b | Rank 0 case |
| cctrace3 | book7c | Kernel, reduction theory, truncation |
| cctrac3b | book7d | Basic properties, equivalence, J_M(u,f), fine expansion |
| cctrace4 | book7e | Spectral decomposition, Eisenstein series |
| cctrace5 | book7f | Integrability of k_χ^T, the trace formula |
| cctrace6 | book7g, book7gnw | Invariant form |
| cctrace7 | book7h | Stable(r) form |

book7gnw.tex is the later of the two invariant-form files: it adds Aoki's metaplectic Paley–Wiener theorem at the real place. Recommendation: copy book7d.tex to cctrac3b.tex, rename \Sb/\endSb, and renumber "Proposition 279", "Example 275" and "(9.19)" to the article's numbering.

Issues in book7d.tex:

1. **The fine expansion is cited to the wrong source for covers.** The Proposition credited to [A12, Thm 8.1] is stated for genuine f on the cover, but Arthur proves it only for connected reductive groups. For covers the result is Li I, whose abstract stresses that the cover case needs unexpected modifications. The coefficients a^M(S,γ) should be defined with the centralizer in the cover.
2. **J_A(z,f) at a central z is not the plain limit stated in the Example.** As a → 1, |D(a)|^{1/2} ∫ f(y^{-1}azy) v_A(y) dy has a log|a − a^{-1}| singularity. Arthur's definition (the paper's own display taken from [A7, (8.1)]) is the limit of r_A^A(z,a) J_A(az,f) + r_A^G(z,a) J_G(az,f). Here r_A^G is not 1, because the class induced from u = 1 in A to G is the regular unipotent class. That correction term is what cancels the singularity. Setting r_A = 1 and taking the limit is valid only for regular a.
3. **Centralizer list.** The display after "anisotropic modulo its center" lists G_γ = G for γ = ±1, which is not anisotropic. The class of ±1 is not a semisimple class in the paper's sense either: it contains ±u. So the claim "all such classes are unramified" should exclude it. The cover's centralizer also matters: for split γ ∉ A^N it is smaller than the preimage of A, and the genuine orbital integral vanishes (book3b.tex, Lemma 5.2). This should be stated here.
4. **The weight normalization is inconsistent.** v(x,T) is computed as the length of the convex hull of T − H(x) and −(T − H(wx)), which is 2T − H(x) − H(wx). It is then written as 2T − log δ(x) − log δ(wx), but δ(a) = |t|², so log δ = 2H. Pick one normalization.
5. **J_unip with T_0 = 0.** J_unip is defined by truncating at T_0 = 0. The truncated integral is only defined, and polynomial, for T sufficiently regular. The correct definition evaluates the polynomial J_unip^T at T = 0.
6. **The weight v_A is wrong at p-adic places.** The Example gives v_A = Σ log√|1+n_p²|_p, as in (7.13). At p-adic places it should be log max(1,|n_p|_p) (Major issues II, item 22).
7. **Minor slips.** f_∞ should be in C_c^∞, not C^∞. "\symbol{126}" should be ∼. Overlines are dropped in the statement of the hyperbolic-class Theorem (G_μ(A) for the cover). The sum over γ ∈ O in the last Example should run over (G,S)-classes.

The book files also confirm that several errors listed above persist in the book: u'_B = |H_B| (Example 6.1), the factor 4T in M_B^T (Example 5.32), and the global cocycle construction.

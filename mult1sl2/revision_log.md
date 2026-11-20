# Revision log: *Multiplicity one for SL(2)*

## Stages

- **1995.** The Scientific Word manuscript `aabook.tex` with its `\input` files (not in this repository).
- **Draft 1** (Claude, November 20, 2026). It was refereed by Carbon (Gemini). The files are merged into one pdflatex file, the main theorem is stated conditionally (the author's decision), and mechanical fixes are applied. In git, see commit `045016f`. The separate Draft 1 log (`revision_log.md` in the author's working copy) is not included here.
- **Draft 2** (Claude, November 20, 2026). This is the response to the referee report on Draft 1 in `revised/referee-report_draft1.md`, which was supplied by the author. The rest of this log covers Draft 1 → Draft 2.

The source compiles with `pdflatex` (three passes, 64 pages), with no warnings, no overfull boxes, and no undefined references or citations.

## 1. Response to the referee, point by point

| Referee item | Verdict | What was done |
|---|---|---|
| 1.1 False finiteness lemma | **Agree.** At fixed level and fixed K∞-types the cuspidal spectrum is infinite (Weyl law). Harish-Chandra's finiteness holds only once the infinitesimal character is also fixed. | Lemma 7.10 is restated with a fixed archimedean infinitesimal character ν. Hypothesis GH is refined to an identity for each ν (Definition 7.4, Hypothesis 7.6). A new condition (LH4) requires finitely many genuine infinitesimal characters over each linear one. The proof of Theorem 7.9 fixes ν = ν∞(π) and is otherwise unchanged. Remark 7.7 explains why the refinement is needed, shows that the refined GH implies the Draft 1 form, and sketches (without carrying it out) how Arthur's multipliers might derive the refined form from the unrefined one. This is the "strengthening of GH" that the referee anticipated. |
| 1.2 p-adic torus characters inconsistent | **Agree** (checked: (3,3)₃ = −1). | §5.3.1 is rewritten. Lemma 5.1 computes the cocycle on A and shows that conjugation by w sends (a,1) to (a⁻¹,1). Lemma 5.2 proves the genuine-character formula, which Draft 1 left to the reader. The correspondence is now ε = η_ϖ·ϑ with η_ϖ² = (ϖ,ϖ)⁻¹. The Fourier computation is redone with every Hilbert symbol shown; Draft 1 had also dropped the factor (x_a,ϖ)⁻¹ and written ε for ϑ. The matching of functions becomes φ̄ = η_ϖ⁻¹(x_a,ϖ)φ on the odd coset. The new Lemma 5.6 includes a converse and Weyl compatibility. Prop. 5.11 now has a real proof. Two worked examples over ℚ₃ are added. |
| 1.3 Real Hilbert symbol and real matching | **Agree with both parts.** The boxed −i is correct. | The symbol is corrected. Lemma 5.14 proves the matching φ̄ = −iφ for x < 0, as an "if and only if". |
| 1.4 Only one anisotropic Cartan used | **Agree.** | §5.3.3 is rewritten. The Weyl formula sums over all anisotropic Cartans (for p odd, two classes for each of the three quadratic extensions). The definitions require matching on every one of them. Lemma 5.18 states the needed character relation as a hypothesis on every elliptic Cartan. "Vanish off the elliptic set" is replaced by "vanishing hyperbolic orbital integrals". |
| 1.5 Scope of Waldspurger's theorem | **Agree.** The theorem is for 𝒜₀₀; I confirmed this from Piatetski-Shapiro's "Work of Waldspurger" (re-TeXed copy online, Theorem 1.1). | New Lemma 7.12 shows that the π̄′ arising in the proof is not isomorphic to any elementary theta constituent, so all of its copies lie in 𝒜₀₀. The argument uses Labesse–Langlands (π comes from a cuspidal Π on GL(2)), the Gelbart–Jacquet bound \|s\| < 1/4, and the Jacquet module of the even Weil representation (exponent 1/2 versus < 1/2). A remark asks that the normalizations be rechecked. |
| 1.6 Division by 2cos θ | **Agree.** | Definition 5.26 now states the three matchings in multiplied form. Remark 5.27 shows two consequences: Φ_f̄ must vanish over −I, and "even/odd" forces Φ_f to be even or odd under −I, which matches the central characters. Example 5.28 is added. Lemma 5.29 is recomputed with the explicit character substitutions and a table; I verified it symbolically with sympy. **Note:** I fixed the labels as "ε = + means holomorphic". In that convention the 1995 statements differ from mine by ε ↦ −ε together with swapping +odd and −odd, which is an orientation flip. The content is the same, but whether this agrees with Gelbart's labels has not been checked. |
| 1.7 Satake does not give orbital-integral matching | **Agree.** | Remark 5.21: Satake gives the spectral matching, and hyperbolic orbital integrals via F_f = Sf. Elliptic orbital integrals of spherical functions (a fundamental lemma) are not established and are now listed as part of what GH assumes. The Satake correspondence is defined explicitly through the torus matching (Definition 5.20). |
| 1.8 Hecke algebra lacks compact support | **Agree.** I found a second problem in the same definition. | Compact support is now required. Draft 1 imposed bi-K-invariance on f(g,1), but it should be invariance under the splitting κ(K). An example (the unit element) shows why this matters. |
| 1.9a Global cover as a subgroup | **Agree.** | §2.2 is rewritten: the global cover is the restricted product modulo Z₀ = {(ς_v) : ∏ς_v = 1}. The cocycle is written with the modified β′_v, since the product of the unmodified β_v is not finite. An example is added. |
| 1.9b Savin theorem stated as a theorem | **Agree.** | It is now Claims 5.31–5.32 (unverified; PGL(2) versus SL(2)). |
| 1.9c Measures on anisotropic tori | **Agree.** | T(F) is compact, so it is normalized to volume 1. The pull-back construction is withdrawn. |
| §2 Status of Theorem 6.1 | Agree with the referee's description. | The Introduction now says that GH is strong and that Draft 1 overlooked the infinitesimal-character issue. |
| §3 Organization and claims | Agree. | A new §1.2 "Conventions on the status of statements" introduces a **Claim** environment for unverified 1995 statements, with the qualification attached to the statement. Converted to Claims: the supercuspidal proposition and its corollary, the Savin theorem and its corollary, the p-adic non-tempered lemma, and the weighted-orbital-integral lemma. |
| §3 Proofs too short | Partly agree. | The real discrete-series lemma now has a full calculation. The weighted-orbital-integral lemma **cannot be proved as stated** (see §2 below), so it is demoted with an explanation rather than expanded. The real non-tempered lemma now has a proof derived from Lemma 5.29. |
| §3 Notation | Agree. | ϖ is the uniformizer throughout, and π is used only for representations. The set of Cartan representatives is renamed 𝒯. The real/p-adic correspondences χ_i are renamed c_i. The ordinary-character parameter is renamed ϑ. A notation table is added (§1.4). |
| §3 Bibliography and literature | Agree. | Added Chai–Zhang (PJM 285 (2016) 345–374) and Zhang (PJM 292 (2018)). Adams [Ad2] is updated to Duke Math. J. 92 (1998) 129–178. Added Gelbart–Jacquet 1978, Gelbart–Piatetski-Shapiro (Invent. 1980), Harish-Chandra LNM 62, Borel–Jacquet, and Arthur's Paley–Wiener paper. The Introduction now distinguishes multiplicity one, strong multiplicity one, the theta correspondence, and Waldspurger packets. |
| §4 LaTeX | Agree. | `proof:` is replaced by the `proof` environment (17 places). `\tr` is now `\operatorname{tr}`, and every `eqnarray` is now `align`. All 67 `\over` are converted to `\frac`. Overfull boxes: 0. |

## 2. Further corrections not raised by the referee

1. **Weighted orbital integrals (Claim 5.9 / Remark 5.10).** The 1995 lemma says that weighted orbital integrals of *any* corresponding pair correspond. That cannot hold. Adding to f̄ a function ḡ − ḡ^y that has vanishing orbital integrals keeps the pair corresponding, but it changes J_A by ∫ ḡ(x⁻¹ax)(v_A(x) − v_A(xy)) dx, because J_A is non-invariant. The same objection applies to the real remark in §5.3.2. A correct version must restrict to specially constructed pairs or use Arthur's invariant distributions I_M. Neither statement is used in Chapter 7.
2. **Haar measure.** The formula dg = δ_B(a)^{1/2} dk da dn (g = kan) is corrected to δ_B(a) dk da dn.
3. **The p-adic even Weil representation** was called supercuspidal. It is not, since it has a nonzero Jacquet module.
4. **Real non-tempered lemma.** This was stated without proof. It now has a proof from Lemma 5.29 and the Grothendieck-group identities.
5. Smaller fixes: the reference "correspond evenly in the sense of §5.3.3" in the real Weil section now points to the real definition. The garbled formula "F(χ) = (I_A(χ,f))" is cleaned up. Prop. 5.11 is stated as a trace identity.

## 3. Original versus new results

- **From the 1995 draft, corrected:** the character correspondences on A (p-adic and real), the matching definitions, the elliptic and real discrete-series correspondences, the Satake correspondence, and the structure of the conditional argument in Chapter 7.
- **New in Draft 2:** Lemmas 5.1, 5.2, 5.6 and 5.14; the proof of Prop. 5.11; Lemma 5.18 in its corrected form; the computation in Lemma 5.29 and Remark 5.27; the proof of the real non-tempered lemma; Definition 7.4 and the refined Hypothesis 7.6; (LH4); Lemma 7.12; Remarks 5.10, 5.21 and 7.7.

## 4. Sources not consulted directly in this revision

These were cited from memory or from secondary listings and have not been checked against the originals:

- Harish-Chandra LNM 62 and Borel–Jacquet (for the finiteness theorem). It is also unchecked whether Moeglin–Waldspurger covers finite central covers.
- Arthur, Acta Math. 150 (1983), cited for multipliers.
- Gelbart–Jacquet 1978 (the bound |s| < 1/4).
- Gelbart–Piatetski-Shapiro, Invent. Math. 59 (1980) (structure of the elementary theta space).
- Labesse–Langlands (cuspidal π of SL(2) comes from a cuspidal Π of GL(2)).
- Waldspurger [Wa1], whose 𝒜₀₀ scope was confirmed only through Piatetski-Shapiro's exposition.
- Cartier (F_f = Sf for spherical f).
- Gelbart's labels in [Ge2] and Adams' labels in [Ad2].
- Adams [Ad1]. I found no confirmed publication data, so it remains a "preprint".
- Manderscheid [M1]–[M3] and Moen [Mo1]. Their publication data were not updated.
- The page range of Zhang's 2018 PJM paper. I confirmed only the starting page, 283.

## 5. Open items for Draft 3

1. Check the normalizations in Lemma 7.12(ii) against [Ge2] and [GePS].
2. Either carry out the multiplier argument of Remark 7.7(2), or keep the refined GH as an assumption.
3. Correct the supercuspidal character relation (Remark 4.3), on every anisotropic Cartan.
4. Reconcile the discrete-series labels with [Ge2] and [Ad2].
5. Write out the cocycle bookkeeping for F_f̄ = Sf̄ on the cover (Remark 5.21).
6. House style: the per-section examples are now present in Chapters 2, 5 and 7, but not yet in Chapters 3, 4 and 6.

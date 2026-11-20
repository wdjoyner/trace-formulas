# Revision log: *Multiplicity one for SL(2)*

## Stages

- **1995.** The Scientific Word manuscript `aabook.tex` with its `\input` files (not in this repository).
- **Draft 1** (Claude, November 20, 2026). It was refereed by Carbon (Gemini). The files are merged into one pdflatex file, the main theorem is stated conditionally (the author's decision), and mechanical fixes are applied. In git, see commit `045016f`. Its log is the last section of this file.
- **Draft 2** (Claude, November 20, 2026). This is the response to the referee report on Draft 1 in `revised/referee-report_draft1.md`, which was supplied by the author. Sections 1–5 below cover Draft 1 → Draft 2.

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

## Draft 1: from the 1995 manuscript to Draft 1

> This is the Draft 1 log as written on November 20, 2026, supplied by the author. Its theorem, section, and line numbers refer to Draft 1 (commit `045016f`), not to Draft 2. Several items it lists as "flagged but not changed" or "not yet done" are addressed in Draft 2 (sections 1 and 2 above). For example, the claim in Chapter 5 that "this defines a character" is now Lemma 5.2, and the 1995 proof sketches are now Claims or have full proofs.

Source: the 1995 Scientific Word manuscript `aabook.tex` with its input files
`aabook1.tex`, `aabook3.tex`, `aabook4.tex`, `aabook2a.tex`–`aabook2e.tex`,
`aabook5.tex`, `aabook6.tex`, `aabookrf.tex` (title-page date 4-9-95).
Output: the single file `multiplicity-one-SL2.tex` (pdflatex, 12pt Times, letter, American English).

### AI usage

- **Carbon (Google Gemini)** refereed the merged 1995 draft (three reports, Nov 20, 2026).
- **Claude (Anthropic)**:
  - merged the source files into one pdflatex file and replaced the Scientific Word macros;
  - assessed Carbon's reports, separating the points that hold from those that don't;
  - made the corrections listed below and rewrote the Introduction, Section 5.4 and Chapter 7 so that the main result is stated conditionally.
- **The author** decided to state the main result conditionally (Nov 20, 2026).

### Decision: conditional main result

The 1995 draft claimed an unconditional proof of multiplicity one for SL(2).
That theorem is true. Labesse and Langlands conjectured it, and Ramakrishnan
proved it (Ann. of Math. 152 (2000)). The 1995 argument, however, has gaps:

- dyadic places (Section 5.4);
- archimedean places;
- several local character relations at odd places;
- the global step in Chapter 7.

Draft 1 replaces it by:

- **Hypothesis 7.3 (GH):** a global trace identity tr R_cusp(f) = tr R̄_cusp(f̄) for corresponding pairs.
- **Hypothesis 7.4 (LH):** local spectral transfer (separation, transfer with injectivity, detection) at each place of S(π).
- **Theorem 7.6:** under GH and LH at the places of S(π), m(π) = 1, and π corresponds to a unique genuine cuspidal π̄.
- **Proposition 7.10:** LH holds at odd places where π_v is K_0- or K_1-spherical.
- **Corollary 7.11:** consequences for π that are hyperspecial-spherical at every odd place.
- **Section 7.4:** what Chapters 3–5 provide toward LH, and what is missing.
- **Section 7.5:** the two gaps in the final step of the 1995 argument.

#### New in Draft 1 versus original

- **New:** the formulation of GH and LH, the proof of Theorem 7.6 (finiteness → Artin's lemma at unramified places → transfer → tensor linear independence → Waldspurger's multiplicity one), Proposition 7.10, Corollary 7.11, and Sections 7.4–7.5. Theorem 7.6 does not use Waldspurger's near-equivalence count.
- **Original (1995), corrected:** Chapters 2–6, apart from Section 5.4 and Section 5.6.

### Changes, by chapter

#### Front matter and Introduction
- Title-page subtitle "Draft 1 / Corrected and expanded version", with the date line "Original draft: 1995. Corrected and expanded draft: 2026".
- The abstract was rewritten. It opens with an AI-disclosure sentence and states the conditional result.
- The Introduction was rewritten and now contains:
  - a new §1.1 on the status of the result (Labesse–Langlands, Ramakrishnan, Blasius, and what is incomplete in 1995);
  - an outline updated to the current chapter numbers;
  - Acknowledgments, now including the AI roles.

#### Chapter 2
- ν(π) = q^{-1} → ν(π) = 1, with |π|_F = q^{-1}.
- In β_1: v(deg g_2, ·) → v(det g_2, ·). Also "cocyle" → "cocycle".
- Non-split torus: a² + b²θ = 1, a,b ∈ F^× → a² − b²θ = 1, a,b ∈ F (the determinant of [[a, bθ],[b, a]]).
- Lemma 2.3(d): a leftover "n = 2" was removed.
- Global cocycle:
  - β_p → β_v.
  - "converges by Lemma 3(b)" was replaced by a remark: one should use the cohomologous cocycle β_v·s_v(g_1)s_v(g_2)s_v(g_1g_2)^{-1}, which is trivial on K_{0,v} × K_{0,v} for almost all v [K2].
  - "an 2-fold" → "a 2-fold".
- Cross-references now use \label/\ref: "equations (2.1-2.3)", "(2.9)", "2.1.4", "Lemma 3(...)", and "part (a) of the above lemma" (the lemma has no parts).
- Typo: "measue" → "measure".

#### Chapter 3
- Typos: "representations theory", "chracter".
- Cross-references now point to the correct chapter.

#### Chapter 4
- σ̄ := σ ⊗ 1 is not genuine. It was replaced by σ ⊗ ε (ε = identity character of μ_2), and μ_n → μ_2.
- Hilbert symbols (·,·)_n → (·,·)_2.
- References to "(2.3)" now point to §2.1 and the multiplication formula.
- Small typos fixed.
- **New Remark 4.3 (caveat):**
  - The splitting K̄_i ≅ K_i × μ_2 is k ↦ (k, s_i(k)), not k ↦ (k, 1).
  - So σ̄((k,ζ)) = ζ s_i(k) σ(k), but the proof treats s_i as trivial.
  - The function (x,ζ) ↦ ζχ_π(x) is not obviously a class function.
  - The proposition is not used in Chapter 7.

#### Chapter 5
- Introduction: the real case now points to §5.3.2 and §5.5, and the p = 2 case to the new §5.4.
- §5.2: "Orbital integrals - vanishing theorems" (there are no vanishing theorems) → "Orbital integrals: definitions".
- The weight v_A was stated for F = Q_p or R as log √|1+n²|_F. That fails p-adically (it is log 0 if n² = −1). It is now:
  - log (1+|n|²)^{1/2} for archimedean F;
  - log max(1, |n|_F) for non-archimedean F.
  - Normalization constants were not rechecked against Arthur.
- The centralizer references were corrected: Lemma 3(h)/(g) → Lemma 2.3(g)/(f) (T̄, Ā abelian).
- "(2.6)" → the conjugation formula plus Lemma 2.3(h).
- "J_M(γ,f)= =lim" → "J_A(γ,f) = lim".
- §5.3.1:
  - "The p=2 case is similar" was removed. It is false as stated: over Q_2, (−I,1)² = (I,−1), so Ā_2(F) is not a direct product.
  - "for n = 2" headings and hypotheses were removed.
  - The definition of corresponding functions on A used f where φ was meant.
- §5.3.2: in the boxed equation, f(a,1) → f̄(a,1).
- §5.3.3: "chapter 4 below" → Chapter 4 above, with a pointer to Remark 4.3.
- **§5.4 (aabook2b.tex) is withdrawn.** It was replaced by a short section listing the reasons:
  - the braid relation is false (s_1s_2 has infinite order);
  - X is not closed under inversion when −1 is a non-square, and the wrong β was computed;
  - N is undefined when c = 0 or d = 0, does not preserve the Iwahori subgroup, and is not multiplicative;
  - restrictions to G_s do not form a convolution algebra, cocycle factors were dropped, and the splitting of B̄_k was ignored;
  - an algebra injection does not induce the claimed map on irreducible modules;
  - the global orbital-integral argument is circular.
  - The section closes with a remark on Takeda–Wood (p = 2, partner SO(3) ≅ PGL(2)).
- **§5.6 (aabook2d.tex):**
  - Savin's theorem and its corollary are kept "as stated in the 1995 draft".
  - New Remark 5.23: in later work the metaplectic cover of SL(2) = Sp(2) is paired with SO(3) ≅ PGL(2), not SL(2), so the statement should be checked against [Sav]. It is not used in Chapter 7.
  - The reference to the withdrawn orbital-integral identity ("§4.4.2") was removed.
  - A missing ^∧ in the corollary was added.
- **§5.7 (aabook2e.tex):**
  - Lemma references were fixed ("Lemma 3" → the Gaussian integral lemma).
  - "in the sense of then" was filled in with §5.3.1 and §5.3.3.
  - "§5.3" → §5.5; "chapter 7 below" → Chapter 4.
  - "Lebesque" → "Lebesgue"; "has be choosen" → "has been chosen".

#### Chapter 6
- Base field: Q was replaced by the number field k throughout, for example M(Q), M_1(Q), A_1(Q), P_1(Q).
- Example 6.1: the weight Σ log √|1+t_v²|_v used the torus parameter t_v. It is now the local weights v_{A,v} of §5.2.1, which are in n_v.
- A doubled comma was removed, and "given by the previous example" was corrected.

#### Chapter 7
- **Rewritten entirely.** The 1995 text is preserved in the original `aabook6.tex`.
- Sign correction: the decomposition-of-measures identity is now (7.1):

  tr R̄(f̄) − tr R(f) = Σ J_χ(f) − Σ J_χ(f̄)

  (the 1995 draft had + in front of the f̄-sum).
- Base field: G(Q)\G(A) → G(k)\G(A).

#### Bibliography
- Added: [Ra] Ramakrishnan 2000; [TW] Takeda–Wood 2018; [J3] Joyner, NYJM 4 (1998), the generalized Hecke algebra paper.
- Restored (cited but commented out in 1995): [Ad1], [H], [Rao], [Shal].
- Typos fixed: "froms", "Irreducibiliy", "Pac. J. Mth.", "Correspondence de Shimura" → "Correspondance", "invarinat", a mismatched quote.

#### Throughout
- archimedian → archimedean; choosen → chosen; Iwawori → Iwahori; arbitary → arbitrary; "the the" → "the"; 1980's → 1980s.

### Flagged but not changed

- **Ch 6, Definition of M_P^T:** the case "χ = (G,ρ), M_B^T = 1" is listed twice. The second case was probably meant for P = B and a different χ.
- **Ch 6:** the factor vol(R/Z) and the J2 date (1996, cited from a 1995 manuscript) are unchanged.
- **Ch 5, §5.3.1:**
  - the claim that the formula defines a character is "left to the reader";
  - "corresponds evenly on the hyperbolic set" is defined via a map t that is introduced only later (§5.3.3).
- **Ch 3:** "the argument of [Ar] sketched above" refers to nothing sketched in the text.
- **Several 1995 proofs** remain "proof: … □" sketches ("a direct calculation", "left to the reader"). These include Lemma 5.6 (weighted orbital integrals for small support) and the claim that every unitary genuine unramified representation is a principal series.
- **Three overfull boxes** (Corollary 5.22, Conjecture 5.25, one display in §6.1) are present in the 1995 layout.

### Sources not consulted directly during this revision

The following were used only as cited in the 1995 text or through their abstracts, not read:

- [Sav] Savin, Local Shimura correspondence;
- [Wa1], [Wa2] Waldspurger;
- [Fl] Flicker;
- [HM] Howe–Moy;
- [M1]–[M3] Manderscheid;
- [GS] Gelbart–Sally;
- [Mo1], [Mo2] Moen;
- [Kut] Kutzko.

In particular:

- The statement of Waldspurger's multiplicity one theorem for the cover, which Theorem 7.6 relies on, was taken from the 1995 text.
- The remark that Savin's partner group is SO(3) ≅ PGL(2) rests on the Takeda–Wood abstract and on the Gan–Savin results it describes.
- Ramakrishnan's theorem was checked against the published abstract (Ann. of Math. 152 (2000) 45–111) and arXiv:math/0007203.

### Style-guide conformance (joyner-math-paper-style-guide.md)

**Done:**
- AI-disclosure opening of the abstract;
- Acknowledgments with AI roles and a pointer to this log;
- Draft/date lines;
- the restriction (conditional result) stated in the abstract and Introduction;
- 12pt Times, letter size, American English, compiles with pdflatex.

**Not yet done:**
- glossary;
- background section more detailed than the glossary;
- at least one example per section;
- a separate literature review section (§1.1 partly serves).

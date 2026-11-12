# Revision log: the spectral measure of an elliptic orbital integral, via Arthur's local trace formula

This log accompanies `route-b-draft.tex` (the "Route B" companion paper). It records the drafts, the AI usage, which results are original and which are new, the sources that could not be consulted, and every change of the Draft 2 style-guide pass. It follows `../../joyner-math-paper-style-guide.md` (Draft 2, November 11, 2026), Sections 6, 8 and 9.

Files in the git history track the drafts. File names carry no draft number (style guide, Section 9). The log of the Route A paper is `../revision_log.md`.

## Drafts and stages

| Draft | Date | What | Record |
|---|---|---|---|
| 0 | 2026-11-10 | Outline of the companion paper | `OUTLINE.md` |
| 1 | 2026-11-10 | First draft: background, Arthur's formula, the two specializations, main theorem in outline, comparison with Route A, examples, literature review, status list, glossary | git history of `route-b-draft.tex` |
| 2 | 2026-11-12 | Style-guide pass: preamble, title page, AI disclosure, acknowledgments, citation keys, the [Ar91] citations, section order, orienting paragraphs, rank-one examples, notation table, summary of results | *Draft 2: style-guide pass* (below) |
| 3 | 2026-11-12 | Mathematical revision: Section 4 restated to match [Ar91], with a remark on normalized and unnormalized weighted characters; "Why it should hold" in §8 replaced by a lemma, a proposition and a corollary; §9 expanded with the R-groups, elliptic data and κ-supports of SL(n) | *Draft 3: mathematical revision* (below) |

## AI usage

- **Claude (Anthropic)**, co-author.
  - It suggested the approach: to reprove the results of the 1997 paper from Arthur's later work on the local trace formula. The suggestion was made during the 2026 revision of that paper (the Route A paper).
  - It wrote the outline and Draft 1 (text, examples, literature review, glossary).
  - It made the Draft 2 style-guide pass recorded here, including all the new text listed below.
  - It made the Draft 3 mathematical revision recorded here, at DJ's request. All the new statements and proofs of Draft 3 are Claude's and are unrefereed.
- **No other AI system** has contributed. The paper has not been refereed, by a person or by an AI system.
- **D. Joyner** decided to pursue the suggestion, directed the work, made the rulings recorded below, and reviews the drafts.

Review by AI systems is not an independent certification of the results.

## Original and new results (style guide, rule 6.5)

This is a new paper of 2026. Every statement in it is new in 2026 or is quoted with a reference. Nothing is carried over from the 1992 or 1997 texts. The results of the Route A paper are cited as [JC26] and are not reproved.

## Sources that could not be consulted, or were not checked (style guide, rule 4.3)

- **[Ar91]** was consulted (the Numdam scan supplied by DJ). Draft 2: Propositions 6.1 and 11.3, Section 12 and its Remarks. Draft 3: also the Introduction, §2 with the Weyl integration formula (2.2), Proposition 4.5, and Lemma 12.1. The scan was read through OCR text, with the key pages (46, 88, 91, 92) checked as images.
- **[Ar81]** was not consulted. "Lemma 6.3" (the product formula for (G,M)-families) is cited in Draft 3 on the authority of [Ar91, p. 92], which calls it "the product formula [4, Lemma 6.3]".
- **[Ar93] and [Ar96]** were not consulted. Everything in the paper that rests on the elliptic form of the spectral side, and the term-by-term form of Theorem D, is therefore unverified.
- **[Ar88]** was not consulted. "Cor. 7.4" is cited on the authority of [Ar91], which calls the splitting formula "[10, Corollary 7.4]" (p. 77) and takes the constants d(L₁,L₂) from "[10, p. 356]".
- **[Ar81], [Ar89a], [Ar89b], [Ar93], [Ar94], [Ar96], [Ar98], [Ar99]** and every other entry of the bibliography were not consulted in this pass. Section and lemma numbers quoted from them ([Ar81, §§6–7, Lemma 6.2], [Ca80, Thm. 3.1], [Ka86, §4]) are unverified.
- The bibliographic data were not checked against publisher records. Status 2.1 of the paper says the same. One entry to look at first: [Ar98] is given as pp. 35–52, and this was not confirmed.
- The citations of [JC26] were checked against the source of its Draft 2 (see step 4 below).

## Draft 3: mathematical revision (2026-11-12)

DJ asked for mathematical revisions: more specifics in "Why it should hold" (§8) and more detailed reasoning in §9. Claude also restated Section 4 to match [Ar91], because the argument of §8 depends on it. **Unlike Draft 2, this draft changes mathematical statements.** Every change is listed here. Nothing in Draft 3 has been refereed.

**Compiling.** 34 pages (Draft 2 had 24), no errors, no warnings, no undefined references, no overfull or underfull boxes.

**Title page.** Subtitle "Draft 3". Date line "First draft: November 10, 2026. Draft 3: November 12, 2026".

### The most important finding: normalized versus unnormalized weighted characters

Arthur's spectral side (12.10) uses weighted characters built from **unnormalized** intertwining operators. Lemma 3.4 of the paper, on which the removal of the spherical factor rests, holds only for **normalized** ones. Draft 3 states this in the new **Remark 4.1** and draws the following consequences. They are Claude's derivation from the product formula for (G,M)-families and have not been compared with the literature.

- The unnormalized weighted character is a sum over Levi subgroups L ⊇ M of a scalar r_M^L (logarithmic derivatives of normalizing factors) times a normalized weighted character for L.
- **Rank one is not affected.** The only extra term is a multiple of the ordinary character of f ⊗ φ, which vanishes because φ is cuspidal. So the PGL(2) and SL(2) statements stand as they were.
- **Rank ≥ 2 is affected.** Terms from Levi subgroups strictly between M₀ and G need not vanish. The formula I_B ρ = c_G J_{M₀}(χ⁻¹, φ) of Theorem B, the first term of Theorem 7.1, and the displayed form of Conjecture 8.1 may be missing these terms. This includes the PGL(3) and SL(3) discussions of §10.
- Not affected: the existence of the measure (Theorem A), the smoothness of the density ([Ar91, Lemma 12.1]), and the supports in Theorem C.

**Status changes (rule 4.2).** No status was upgraded. Three were qualified downward:
- Theorem B and Theorem 7.1: "proved modulo normalizations" now also carries "in rank ≥ 2 the formula for the density may need further terms" (Introduction, new Status 7.2, Summary, item (N1)).
- Conjecture 8.1: its displayed form is "subject to Remark 4.1" in rank ≥ 2. The conjecture is then the statement I = I_B.
- The statements of Theorems A–D themselves were **not** edited. DJ should decide whether Theorem B is to be restated.

### Changes to existing mathematical text

1. **§4.1 (truncation).** "J^T(f) = ∫ K_f(x,x) u(x,T) dx is asymptotic to a polynomial in T. Its constant term J(f)…" became: the truncated integral is K^T(f); it differs from a function J^T(f) by an exponentially small amount [Ar91, Prop. 4.5]; for p-adic F, J^T(f) is a finite sum of polynomials times roots of unity [Ar91, Prop. 6.1]; J(f) = p₀(0, f).
2. **§4.2 (the formula).**
   - "Arthur proves two expansions of J(f)", with both (4.1) and (4.2) written as "J(f) = …", became: the local trace formula is the identity J_geom(f) = J_spec(f) [Ar91, Thm. 12.2], with (4.1) = J_geom and (4.2) = J_spec. A sentence says that neither is J(f) itself ([Ar91, (12.13)]).
   - (4.2): the integral over Π_temp(M) became an integral over Π_disc(M) with the coefficient a^M_disc(π), as in [Ar91, (12.10)].
   - Weighted orbital integral: the domain M_γ∖G became A_M(F)∖G(F), and the (G,M)-family e^{−Λ(H_P(x₁) − H_P̄(x₂))} became e^{−Λ(H_P(x₂) − H_P̄(x₁))}, as in [Ar91, (12.1), (12.2)].
   - Γ_ell(M) is now described as in [Ar91, §2], with its measure.
   - Removed: "In (4.2), J_M(π,f) is a weighted character of G(F)×G(F) attached to π⊗π^∨. The measure dπ and the precise domain of integration are as in [Ar91]." Replaced by a description of Π_disc(M), a^M_disc and the unnormalized weighted character, from [Ar91, (12.4)–(12.8)].
   - New Remark 4.1 (above).
   - Example 4.2 (was 4.1): "J(f) =" became "J_geom(f) =", and "expansion" became "side".
3. **§4.4 (splitting).** A paragraph was added on where (4.3) comes from, saying that it is used for the normalized operators and that the signs from the twist by −Λ are unchecked.
4. **Status 4.3 (was 4.2).** Rewritten: (4.1) and (4.2) were compared with [Ar91, Thm. 12.2]; the elliptic form, (4.3) and the passage to normalized operators are unchecked.
5. **Proposition 5.1.** Part (a): "J^T(𝐟) is constant for T large, and J(𝐟) = … = I(f,φ)" became "the truncated integral K^T(𝐟) is constant for T large, and K^T(𝐟) = … = I(f,φ)". Part (b) gained the conclusion "So J_geom(𝐟) = I(f,φ)". The proof of (b) now derives this from Arthur's Weyl integration formula [Ar91, (2.2)]. With Arthur's measures the identity is exact, and the Summary no longer says that the constants of (4.1) are being checked.
6. **§6.3 and Example 6.5.** "the spectral side of J(f⊗φ)" became "the spectral side J_spec(f⊗φ)", and §6.3 now says "passing to normalized operators as in Remark 4.1".
7. **§7.** New Status 7.2 after the proof outline (the rank ≥ 2 caveat).
8. **§8, "Why it should hold".** The Draft 2 paragraph was replaced. It read:
   > Both sides are linear in φ and determined by their pairings with all f^∨, and Theorem 4.5(a) of [JC26] gives I(f,φ) as ∫ f^∨ I^T dμ for T large. If the oscillatory part of I^T pairs to zero in the limit, which happens for PGL(2) and, numerically, for PGL(3) ([JC26, App. A]), then ∫ f^∨ I dμ = I(f,φ). Comparing with Theorem 7.1 for all f then gives Conjecture 8.1 when there is no singular part, because the f^∨ are dense in C(Θ̂ᵘ/W). So the conjecture is already a consequence of the PGL(2) results of [JC26] and Theorem 7.1, and of the PGL(3) computation, once the normalizations are fixed. The real content is a direct proof that identifies the two constructions.

   The new text keeps this argument and makes each step a statement (next subsection).
9. **§9.** The opening paragraph and the Draft 2 Status 9.1 ("This section is an outline…") were replaced. The overview paragraph ("For G = SL(n) and κ…") is unchanged.
10. **§10.4.** The predicted weight was "⅓(Δ_κ⁻¹ + Δ_{κ²}⁻¹) c_S … which is ⅔ if all transfer factors and c_S equal 1". The factor c_S was an error: by [JC26, (5.4A) and Prop. 5.1] it cancels. Now "⅓(Δ_κ⁻¹ + Δ_{κ²}⁻¹) … which is ⅔ if both transfer factors equal 1".
11. **Items (N1), (N2), (N8)** of §12, the Summary table, the abstract, the Introduction, the notation table and the glossary entry *Local trace formula* were updated to match.

### New mathematical text, for refereeing

**Section 8.**
1. **Lemma 8.2** (`l:dense`): Satake transforms are dense in the continuous W-invariant functions on Θ̂ᵘ, so a finite W-invariant measure is determined by its integrals against them. Proof by Stone–Weierstrass and Riesz. Uses that G is split.
2. **Proposition 8.3** (`p:AB`): if Route A and Route B each write the functional f^∨ ↦ I(f,φ) as an L¹ density times ρ dχ plus a singular measure, then the densities agree almost everywhere and the singular measures agree. Proof: Lemma 8.2 and uniqueness of the Lebesgue decomposition.
3. **"When the hypotheses hold"**: (B) is Theorem 7.1. (A) is [JC26, Thm. 4.5(b)] under (C) and (R) or (R′), unconditional for PGL(2) ([JC26, Lemma 6.1A]), and [JC26, Prop. 6.4] for SL(2). The W-invariance of Route A's I(χ,φ) is argued in one sentence and should be checked.
4. **Corollary 8.4** (`c:pgl2`): for PGL(2), Theorem 7.1 implies I(χ,φ)ρ(χ) = −¼(J_A(χ⁻¹,φ) + J_A(χ,φ)) almost everywhere. This is Conjecture 8.1 up to an average over W. The W-invariance of the weighted character, which would remove the average, is expected and unchecked.
5. **"What the argument does not show"** and **"A reformulation"**: Route A's I(χ,φ) is written as tr(𝒥(χ) π_χ(φ)), with 𝒥(χ) the matrix of constant terms of truncated inner products from [JC26, Props. 3.6 and 4.2]. The conjecture then compares two operators on the level-n vectors. This paragraph is heuristic.

**Section 9.** Coordinates: χ has parameter z = (z₁, …, z_n) up to a scalar, and μ(χ) is the set of ζ with ζz a permutation of z.
6. **Lemma 9.1** (`l:slnR`): R_χ ≅ μ(χ), a subgroup of μ_n, and R_χ ⊇ μ_m exactly when the multiset {z_i} is a union of cosets of μ_m. This gives a direct proof, for SL(n), of the statements quoted from [Ke82] in §3.4.
7. **The sets T_m** and the point χ_n = T_n.
8. **A convention** (§9.2): an element of an R-group is represented by the element of its coset that preserves the positive roots α with χ_α = 1, following [Ar91, §12, Remark 3]. **The definition of "elliptic" in §3.4 does not say which representative is meant, and the choice matters** (example: SL(4), z = (1,1,−1,−1)). §3.4 itself was not edited.
9. **Proposition 9.2** (`p:slnell`): if r ∈ R^M_χ is elliptic in a Levi subgroup M ⊋ M₀ of SL(n), then M = M_m (n/m blocks of size m), χ ∈ T_m, and r is the class of a product of m-cycles with c(w) = ζ primitive of order m. Conversely all such triples are elliptic, and dim T_m = n/m − 1 = dim a_{M_m}^G. The key step is that a sum of positive roots is not zero.
10. **Corollary 9.3** (`c:slnindex`): the singular terms of Theorem 7.1 for SL(n) are indexed by ζ ≠ 1 in μ_n, and the terms with M = G are φ(n) virtual characters at the one point χ_n.
11. **Example 9.4** (`ex:sl4`): SL(4).
12. **Equation (9.1)** (`e:kappadecomp`): O_γ(f) as the stable term plus κ-terms, from [JC26, (5.4A), (5.11), Lemma 5.0]. The constant c_S cancels in the κ-terms.
13. **Lemma 9.5** (`l:iota`), proof sketched: for the standard L-embedding, the image of the unramified unitary characters of H_m is T_m. [JC26] does not specify its L-embedding, and the paper now assumes it is this one.
14. **Proposition 9.6** (`p:dictionary`): the κ-terms of Route A and the singular terms of Route B have the same index set (ζ ≠ 1 in μ_n) and the same supports (T_m, which is where R_χ ⊇ μ_m).
15. **Proposition 9.7** (`p:Dreduction`): if Theorem 7.1 holds, the stable term of Route A is absolutely continuous, and each κ-term is a measure on T_m, then the singular part of Theorem 7.1 is the sum of the κ-measures. This is a summed form of Theorem D. Two of the three assumptions are not known.
16. **"Prime n"** and **equation (9.2)** (`e:Dprime`): for prime n and a torus S stably conjugate to the unramified norm-one torus, 𝔇(S) ≅ F^×/N E^× has order n, the κ-terms give a point mass at χ_n of weight (1/n) Σ_{κ≠1} Δ_κ⁻¹ (so (n−1)/n if all transfer factors are 1), and Theorem D becomes the character identity (9.2). Not proved. The constants use the normalizations of [JC26, §5], which were checked only for SL(2).
17. **Status 9.8** and the list "What remains".

**Other.**
18. **Remark 4.1** (above) and the paragraph added to §4.4.
19. **Proof of Proposition 5.1(b)**: the sentences deriving J_geom(𝐟) = I(f,φ) from [Ar91, (2.2)].
20. **Abstract**: one sentence on SL(n), and the status sentences now mention the rank ≥ 2 correction.

### Semicolons

The new text has none. Draft 2 had 21 and Draft 3 has 20. The one that went was in Status 4.3, which was rewritten.

### What was left alone, and why

- **The statements of Theorems A–D, Lemma 3.4, Propositions 6.1, Lemmas 6.2 and 6.3, Theorem 7.1 and Conjecture 8.1.** They are qualified by Remark 4.1 and Status 7.2, not rewritten.
- **§3.4**, including the definition of an elliptic element, although §9.2 shows that it is ambiguous.
- **§4.3 (the elliptic form)** and **(4.3)**. [Ar93] and [Ar88] were not available.
- **§10.1–10.3.** For PGL(3), Remark 4.1 may change what "Theorem B predicts" means. The text was not edited.
- **"The two truncations" and "What (R) means here"** in §8.
- **`OUTLINE.md`.**
- No script was added. The new arguments are by hand.

### Numbering concordance: Draft 2 → Draft 3

Every `\label` of Draft 2 is kept (checked by comparing the `.aux` files). Section numbers, equation numbers (1.1)–(4.3) and Theorems A–D are unchanged.

| Object | Draft 2 | Draft 3 |
|---|---|---|
| Remark (normalized and unnormalized weighted characters) | — | Remark 4.1 |
| Example `ex:ltf` | Example 4.1 | Example 4.2 |
| Status (Arthur's formula) | Status 4.2 | Status 4.3 |
| Status (rank ≥ 2 caveat) | — | Status 7.2 |
| Remark (smoothness) | Remark 7.2 | Remark 7.3 |
| Example `ex:main` | Example 7.3 | Example 7.4 |
| Lemma `l:dense`, Proposition `p:AB`, Corollary `c:pgl2` | — | Lemma 8.2, Proposition 8.3, Corollary 8.4 |
| Example `ex:compare` | Example 8.2 | Example 8.5 |
| §§9.1–9.4 | — | new subsections of §9 |
| Lemma `l:slnR`, Proposition `p:slnell`, Corollary `c:slnindex`, Example `ex:sl4`, Lemma `l:iota`, Proposition `p:dictionary`, Proposition `p:Dreduction` | — | 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7 |
| Status (SL(n)) | Status 9.1 | Status 9.8 (rewritten) |
| Example `ex:endo` | Example 9.2 | Example 9.9 |
| Equations `e:kappadecomp`, `e:Dprime` | — | (9.1), (9.2) |

### Checks of this draft, and what was not verified

- **Source diff.** Every line of Draft 2 that does not appear verbatim in Draft 3 was listed by script and compared with this section.
- **Hand checks.** The SL(4) examples (the two representatives of the class with c = −1 at z = (1,1,−1,−1), and the point χ₄), the average over W in Corollary 8.4, and the weights ½ and ⅔ for n = 2, 3 were worked by hand.
- **Not verified:** everything in *New mathematical text*. In particular Remark 4.1 (no source consulted beyond [Ar91]), Lemma 9.5 (sketch), the claim 𝔇(S) ≅ F^×/N E^×, the constants of (9.2), and the W-invariance statements in §8.
- **Suggested for the referee (Argon):** Remark 4.1 first, since it decides whether Theorem B must be restated in rank ≥ 2. Then Proposition 9.2 and Proposition 8.3.

## Draft 2: style-guide pass (2026-11-12)

The paper was brought into line with the style guide, following the audit of November 11 and DJ's instructions of November 12. **No statement, proof, hypothesis or status label was changed**, with the two exceptions DJ approved: a status sentence added to the abstract, and one sentence removed from Status 4.2 (below).

**Compiling.**
- Before the pass: 17 pages, no errors, no undefined references, no overfull or underfull boxes. 15 hyperref "token not allowed in a PDF string" warnings, from math in section titles.
- After the pass: 24 pages, **no errors, no warnings, no undefined references, no overfull or underfull boxes**.

### Rulings (DJ, 2026-11-12) and defaults used

- **Subtitle and date line.** Subtitle "Draft 2". Date line "First draft: November 10, 2026. Draft 2: November 12, 2026". The wording of rule 6.2 ("Corrected and expanded version", "Original draft: …") is not used, because this is a new paper.
- **Numbering.** Ordinary numbering in the order of Section 2 of the guide, with the concordance below.
- **Abstract.** A sentence on the status of the results is added (below).
- **[Ar91] placeholders.** Filled from the source, which DJ supplied.
- **Log.** This file, separate from the log of the Route A paper.
- **[DECIDE] defaults.**
  - Document class `article`: kept.
  - Fonts: newtx is preferred, but it is not installed in the build environment and CTAN could not be reached. The fallback `mathptmx` is used, and the newtx line is in the preamble as a comment.
  - Glossary placement: at the end, before the Acknowledgments. It stays Appendix A.
  - Author line: "David Joyner and Claude", kept. A version for arXiv or a journal would need Claude moved to the acknowledgments.

### Changes, by step

1. **Preamble.**
   - Was `11pt`, 1.1in margins, Computer Modern. Now `12pt,letterpaper`, `fontenc` T1, `mathptmx`, `geometry` with one-inch margins.
   - `\numberwithin{equation}{section}` added. Equations were numbered (1)–(8) through the paper.
   - `\DeclareMathOperator` for vol and tr (previously `\operatorname` macros), diag (was `\mathrm{diag}`, one occurrence) and Ad (new text only).
   - `longtable` and `array` loaded for the notation table.
   - Section titles with math use `\texorpdfstring`.
   - Theorems A–D are one environment with a lettered counter, so that they can carry `\label`s (`t:A`–`t:D`). The printed form is unchanged. All hand-typed references to them are now `\ref`s.
   - The hand-typed "(N1)" and "(N2)" are `\ref`s to new labels `n:1`–`n:8` on the items of the status list.
   - Spelling: "cancelled" became "canceled" (Remark 7.2), and "Acknowledgements" became "Acknowledgments".
2. **Title page, abstract, acknowledgments.**
   - Subtitle "Draft 2" (was "Draft"). Date line as ruled.
   - `wdjoyner@gmail.com` on the author line (rule 5.1).
   - The footnote on the date was split. "This is a working draft. Statements are labeled … to be checked." is a `\thanks` on the title, verbatim. "Claude is an AI model made by Anthropic." is a `\thanks` on Claude's name, with a pointer to the Acknowledgments.
   - The abstract opens with an AI-disclosure sentence that points to the Acknowledgments (rule 5.2). "This AI-aided paper revises…" became "The paper revises…".
   - **Abstract, status (ruling 3).** Added at the end: "This is a working draft. The results are proved modulo normalizations in Arthur's formula that have not yet been checked. The main theorem is proved in outline, and the statement for SL(n) is given in outline only. The section 'Status and what remains' lists what is missing."
   - The Acknowledgments were rewritten (rules 5.3–5.5). They say that the paper began with Claude's suggestion to reprove the 1997 results from Arthur's later work, give Claude's role as co-author, say that no other AI system contributed and that the paper has not been refereed, state that AI review is not an independent certification, and point to this log. The Draft 1 text was: "This draft was prepared with the help of Claude (Anthropic); its plan follows the outline `OUTLINE.md` in the same directory."
3. **Citation keys** (rule 1.7).
   - `ArSTF` was one entry for three papers. It is now `Ar01` (II, Invent. Math. 143), `Ar02` (I, J. Inst. Math. Jussieu 1) and `Ar03` (III, Ann. of Math. 158). The two `\cite`s became `\cite{Ar02,Ar01,Ar03}` (text of §2.2) and `\cite{Ar01,Ar02,Ar03}` (Status 2.1).
   - `Cas80` became `Ca80` and `Cas95` became `Ca95`, in the bibliography and in the 4 `\cite`s. This matches the Route A paper. There is no clash with Cartier's `Ca79`.
   - `Ar13` was out of order in the bibliography and now follows `Ar03`.
   - All other keys already conformed.
4. **Citations of the Route A paper [JC26]** (rule 8.3: cite the current draft).
   - "App. B" became "App. A" (5 places), and "(B.4)" became "(A.4)" (2 places), after the renaming of the PGL(3) appendix in Draft 2 of that paper.
   - `\cite[\S8]{JC26}` (earlier reductions of the fundamental lemma) became `\cite[Literature review]{JC26}`. Section 8 of that paper is now its summary.
   - The bibliography entry now gives the Draft 2 title, "Draft 2. Corrected and expanded version".
   - Every other number cited from [JC26] was checked to exist, with the cited content, in its Draft 2 source: §2, §4.3, §5, (1.1), (4.8), (4.10), (5.4A), (6.5), Lemma 3.5A, Lemma 4.4, Prop. 4.2, Thm. 4.5, Conj. 4.6, Props. 5.1 and 5.2, Thm. 6.1, Rem. 6.2, Prop. 6.4, Rem. 2026.20.
5. **The [Ar91] citations** (ruling 4). See the next subsection.
6. **Structure** (Section 2 of the guide).
   - The literature review moved from §10 to §2, verbatim apart from the citation keys.
   - New §11, *Summary of results*.
   - Order: 1 Introduction, 2 Literature review, 3 Unramified background (with 3.1 Notation), 4 Arthur's local trace formula, 5 The geometric side, 6 The spectral side, 7 The main theorem, 8 Comparison with Route A, 9 SL(n) and endoscopy, 10 Examples, 11 Summary of results, 12 Status and what remains, Appendix A Glossary, Acknowledgments, References.
   - The *Plan* paragraph of the Introduction was put in the new order, with a sentence for §11.
   - There was no revision history in the body to move.
7. **Additions.** See *New text* below.

### The [Ar91] citations

Two placeholders were filled, and one sentence was removed.

| Place | Draft 1 | Draft 2 |
|---|---|---|
| §4.2, before (4.1) | `\cite[Theorems on pp.~?]{Ar91}` | `\cite[Props.~6.1 and~11.3, Thm.~12.2]{Ar91}` |
| §4.4, before (4.3) | `\cite{Ar88}, \cite[\S?]{Ar91}` | `\cite[Cor.~7.4]{Ar88}, \cite[\S10]{Ar91}` |
| Status 4.2, last sentence | "The theorem numbers in [Ar91] are to be supplied." | removed |

In [Ar91], Proposition 6.1 (p. 46) is the geometric expansion of the constant term, Proposition 11.3 (p. 88) is its spectral expansion, and Theorem 12.2 (p. 91) is the local trace formula. The splitting formula is used in §10 (pp. 77–78) and in the proof of Corollary 11.2 (pp. 82–83).

**Differences between the paper and [Ar91], found while filling the citations.** Nothing was changed in the paper. These are for the next draft, and they bear on items (N1) and (N2).

1. **What equals what.** Theorem 12.2 says that the expressions (12.9) and (12.10) are equal. It does not say that either equals the constant term J(f). Proposition 6.1 expands the constant term (written J̃(f) there) with a different weight, ṽ_M of (6.6), and without the sign. By (12.13), J̃(f) is a sum over parabolic subgroups Q of terms J_geom^{M_Q}(f_Q) c′_Q, of which (12.9) is the term Q = G. The paper's §4.2 says "Arthur proves two expansions of J(f)" and writes both (4.1) and (4.2) as formulas for J(f). Proposition 5.1(a) then identifies J(f ⊗ φ) with I(f, φ). This chain needs to be restated from (12.9) = (12.10).
2. **Geometric side.** (4.1) agrees with (12.9), coefficient and sign included.
3. **Spectral side.** (12.10) is an integral over Π_disc(M), with a coefficient a^M_disc(π) defined by (12.4)–(12.6). The paper's (4.2) is an integral over Π_temp(M) with no such coefficient. The paper says that the domain and the measure are "as in [Ar91]".
4. **Normalization.** The weighted characters J_M(π, f) of [Ar91] are defined with the **unnormalized** operators J_{Q|P} ((12.7), (12.8), and Remark 1 on p. 95). The paper's weighted characters use the normalized operators, and Lemma 3.4 depends on this (Remark 3.5 of the paper says so). The passage from Arthur's unnormalized form to a normalized one is not in [Ar91].
5. **Truncation.** For p-adic F, J^T(f) is a finite sum of polynomials times exponentials in T, and J(f) is the constant term p₀(0, f) (Proposition 6.1). The paper's §4.1 says "asymptotic to a polynomial in T".
6. **Weight.** Arthur's (G,M)-family is e^{−Λ(H_P(x₂) − H_P̄(x₁))} (12.1). The paper has x₁ and x₂ the other way round. Arthur's weighted orbital integral is over A_M(F)∖G(F) in each variable. The paper writes M_γ∖G.
7. **Splitting.** [Ar91] does not state the splitting formula (4.3) for weighted characters of f₁ ⊗ f₂. It applies the splitting formula for products of (G,M)-families, [Ar88, Cor. 7.4], inside the proof of the spectral expansion. Status 4.2 already says that the form of (4.3) in the local setting is being checked.

### New text, for refereeing (ground rule 2)

**New mathematical text.** Each item needs an independent check. All of it is in rank one, for SL(2) and PGL(2).

1. **Example 3.1** (`ex:notation`, §3.1): the notation in rank one. Unramified characters are χ(diag(t, t⁻¹)) = μ(t) for SL(2) and χ(diag(a, b)) = μ(a/b) for PGL(2), with z = μ(π). Then χ_α(π) = z for SL(2) and z² for PGL(2). The unitary characters form the unit circle, and w acts by z ↦ z⁻¹. These are the coordinates of [JC26, §6.0].
2. **Table 1** (`tab:notation`, §3.1): notation. It restates definitions from the paper or cites [JC26]. Four entries define symbols that Draft 1 used without a definition, and need a look:
   - a_M, a_M^L and H_M, H_P (taken from the glossary of [JC26]);
   - θ_Q (described in words, with pointers to [Ar81, §6] and [JC26, (2.16)]);
   - D(γ) (the Weyl discriminant, the standard definition);
   - L_M^∨ (described only as a lattice modulo which the twist τ_Λ is defined; Draft 1 does not say which lattice).
   The table also records that π is both a uniformizer and a representation.
3. **Example 3.3** (`ex:norm`, §3.2): (3.1)–(3.3) in rank one. c_α = (1 − q⁻¹y)/(1 − y) with y = χ_α(π). On the unit circle it has no zero and one pole, at y = 1 (z = 1 for SL(2), z = ±1 for PGL(2)).
4. **Example 3.6** (`ex:wchar`, §3.3): the (G,A)-family of normalized operators in rank one, with θ_B = v⁻¹ξ and θ_B̄ = −v⁻¹ξ as in [JC26, Example 2.5]. The result is R_A(χ,B) = −v R_{B̄|B}(χ)⁻¹ (d/dξ) R_{B̄|B}(χ_Λ) at ξ = 0, and R_A(χ,B)Φ_K = 0. The sign and the factor v depend on the convention for θ.
5. **Example 3.7** (`ex:R`, §3.4): R-groups in rank one. For SL(2), R_χ is trivial except at z = −1, where it is W and its non-trivial element is elliptic. For PGL(2) all R-groups are trivial.
6. **Example 4.1** (`ex:ltf`, §4.2): in rank one the coefficients of (4.1) and (4.2) are 1 for M = G and −1/2 for M = A. The example says that −1/2 is the constant c_G of Theorem B.
7. **Example 5.2** (`ex:geom`, §5): the term M = A of the geometric side vanishes, because a regular element of the split torus is not elliptic. It restates the proof of Proposition 5.1(b) in rank one.
8. **Example 6.5** (`ex:spec`, §6.3): the surviving spectral terms. For PGL(2), −(1/2)∫ f^∨(χ) J_A(χ⁻¹, φ) dχ. For SL(2), the same and a point mass at χ₀. It restates the list of §6.3 and §10.2.
9. **Example 7.3** (`ex:main`, §7): Theorem 7.1 for PGL(2) and SL(2), "with the same normalizations assumed". It restates §10.1 and §10.2.
10. **Example 8.2** (`ex:compare`, §8): Conjecture 8.1 for PGL(2). It restates §10.1 and item (N5).
11. **Example 9.2** (`ex:endo`, §9): n = 2. One non-trivial unramified κ, of order 2, and the endoscopic group is a torus. It restates Status 9.1 and §10.2.
12. **Section 11**, *Summary of results*: a table of nine results with the status of each, and two closing sentences. The referee should check that no status is stated more strongly than in the body.
13. **Abstract:** the status sentences quoted in step 2.

**New text without mathematical content.**
- Orienting paragraphs (rule 3.2) at the start of §1, §2.1, §2.2, §3.1–3.4, §4.1–4.4, §5, §6, §6.1, §6.2, §7, §8, §9, §10, §10.1–10.4 and §12. §2, §3, §4, §6.3 and the glossary already had one.
- The *Plan* paragraph of §1 (reordered, one sentence added).
- The Acknowledgments.

### Semicolons

Rule 3.8 was applied to new text only, and the new text has none. Draft 1 had 24 semicolons and Draft 2 has 21. The three that went were not removed from kept text: one was in the Draft 1 acknowledgment sentence, which was replaced, and two separated the three papers of the `ArSTF` entry, which was split.

### What was left alone, and why

- **The mathematics.** The seven differences from [Ar91] listed above are not corrected. They need a ruling and a new draft.
- **Rule 6.6** ("Remark 2026.n" for unverified items): not applied. The paper uses numbered "Status" paragraphs, and converting them would alter status labels.
- **Rules 6.1, 6.3, 6.7, 6.8:** not applicable to a new paper. The concordance below is given under ground rule 5.
- **Rule 3.3** for §2 (literature review), §11, §12 and the glossary: they explain no concepts, so they have no example. The Route A pass ruled the same way.
- **Rule 3.4:** the paper has no `definition` environments. The definitions made in the text (normalized operators, weighted characters, R-groups, elliptic elements) each have a rank-one example now. The definitions of §4 that are quoted from Arthur (truncated kernel, weighted orbital integral, T_disc and T_ell) have only Example 4.1 and the SL(2) case of §10.2. A worked weighted orbital integral would be new mathematics, and item 6 above shows that the conventions are not yet fixed.
- **Rules 3.5–3.7 and Section 4 of the guide** were not checked line by line. The notation table covers the undefined symbols that were noticed. π is still used for both a uniformizer and a representation.
- **The Status paragraphs, the "Proof outline" and "Sketch" labels, and Theorems A–D** are unchanged.
- **Hand-typed names:** "(R)", "(R′)", "(U_r)", "Route A" and "Route B" are names, not numbers, and stay as typed. "Theorem 4.5(a) of [JC26]" is a citation of another paper.
- **Rule 8.2** (a LaTeX log): Section 9 of the guide asks for `revision_log.md` in this repository.
- **Rule 8.4** (scripts by commit hash): the paper cites `examples/pgl3/` by path.
- **`OUTLINE.md`** is a record of Draft 0 and was not changed. Its section numbers are those of the outline, not of either draft.
- **hyperref** keeps colored links, as in the Route A paper.

### Numbering concordance (ground rule 5): Draft 1 → Draft 2

Every `\label` of Draft 1 is kept. This was checked by comparing the `.aux` files.

| Object | Draft 1 | Draft 2 |
|---|---|---|
| Introduction | §1 | §1 |
| Literature review; Before 1997; After 1997 | §10; §10.1; §10.2 | §2; §2.1; §2.2 |
| Status (bibliography not checked) | Status 10.1 | Status 2.1 |
| Unramified background; Notation; Normalized intertwining operators; Weighted characters; R-groups | §2; §2.1; §2.2; §2.3; §2.4 | §3; §3.1; §3.2; §3.3; §3.4 |
| Status (normalization) | Status 2.1 | Status 3.2 |
| Lemma `l:sphvanish` | Lemma 2.2 | Lemma 3.4 |
| Remark (dependence on normalization) | Remark 2.3 | Remark 3.5 |
| Arthur's local trace formula, and its four subsections | §3, §§3.1–3.4 | §4, §§4.1–4.4 |
| Status (constants, domain, splitting) | Status 3.1 | Status 4.2 |
| The geometric side | §4 | §5 |
| Proposition `p:geom` | Proposition 4.1 | Proposition 5.1 |
| The spectral side, and its three subsections | §5, §§5.1–5.3 | §6, §§6.1–6.3 |
| Proposition `p:split` | Proposition 5.1 | Proposition 6.1 |
| Lemma `l:cusp` | Lemma 5.2 | Lemma 6.2 |
| Lemma `l:noDS` | Lemma 5.3 | Lemma 6.3 |
| Status (Lemma `l:noDS`) | Status 5.4 | Status 6.4 |
| The main theorem | §6 | §7 |
| Theorem `t:main` | Theorem 6.1 | Theorem 7.1 |
| Remark (smoothness) | Remark 6.2 | Remark 7.2 |
| Comparison with Route A | §7 | §8 |
| Conjecture `c:AB` | Conjecture 7.1 | Conjecture 8.1 |
| SL(n) and endoscopy | §8 | §9 |
| Status (outline) | Status 8.1 | Status 9.1 |
| Examples, and its four subsections | §9, §§9.1–9.4 | §10, §§10.1–10.4 |
| Status (PGL(2)); Status (SL(3)) | Status 9.1; Status 9.2 | Status 10.1; Status 10.2 |
| Summary of results | — | §11 |
| Status and what remains | §11 | §12 |
| Glossary | Appendix A | Appendix A |
| Equation `e:main` | (1) | (1.1) |
| Equations `e:GK`, `e:rnorm`, `e:fix` | (2), (3), (4) | (3.1), (3.2), (3.3) |
| Equations `e:geo`, `e:spec`, `e:split` | (5), (6), (7) | (4.1), (4.2), (4.3) |
| Theorems A–D; items (N1)–(N8) | unchanged | unchanged |
| New examples | — | Examples 3.1, 3.3, 3.6, 3.7, 4.1, 5.2, 6.5, 7.3, 8.2, 9.2 |
| New table | — | Table 1 |

### Checks of this pass

- **Source diff.** Every line of Draft 1 that does not appear verbatim in Draft 2 was listed by script and compared with the changes recorded here. There are no others.
- **Labels.** All 31 labels of Draft 1 are present in Draft 2.
- **Arithmetic of the new examples.** The coefficient −1/2 and the R-groups in rank one were worked by hand. No script was needed, and none was added.
- **Not verified.** The new examples have not been refereed. The convention for θ_B in Example 3.6 is taken from [JC26, Example 2.5] and was not compared with [Ar81].

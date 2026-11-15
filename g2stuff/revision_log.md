# Revision log: on the transfer of Shalika germs for G₂

This log accompanies `revised/g2-shalika-germs-2026.tex`. It records the drafts of the 2026 revision, the AI usage, which results are original and which are new, the verification levels, and the sources that could not be consulted. It follows `../joyner-math-paper-style-guide.md`, Sections 6, 8 and 9.

Files in the git history track the drafts. File names carry no draft number (style guide, Section 9).

## Drafts and stages

| Draft | Date | What | Record |
|---|---|---|---|
| 0 | 2026-11-13 | Literal amsart transcription of the summer 1994 manuscript, referee report (Claude), and verification scripts | `original-1994/`, `transcription/`, `referee/`, `scripts/` (PR #15) |
| 1 | 2026-11-13 | Corrected and expanded edition (with a same-day addendum before refereeing: the transfer factor for the biquadratic tori, Proposition 7.6–Corollary 7.8): every item of the referee report addressed or flagged; Theorems 6.1, 7.2, 8.3 restated as conditional germ identities; new Propositions 3.4A, 3.7, Table 4.3A, Table A.6; literature review, summary, glossary | `revised/g2-shalika-germs-2026.tex`, `revised/CHANGES.md` (PRs #16, #17) |
| 2 | 2026-11-14 | Second referee pass and revision by Gemini ("Carbon"): Kirillov–Kostant orbit forms and rational Leray fiber forms replace (7.3)–(7.4), (8.4)–(8.5); subregular representative in §6 corrected to exp(X_β + X_{2α+β}); torus embeddings (A.13)–(A.13′) corrected; Lemma 4.4 orbit images, Dynkin-curve lines, face counts 268/38 and the H¹(F,S₃) count proved; Hales 1989 consulted directly | `revised/CHANGES.md`, `scripts/verify_g2_*.py` |
| 3 | 2026-11-14 | Third pass by Carbon: exact Lemma 1.21 polynomials (1.21a), star gallery relations (1.21b), constants (c₁,…,c₇) = (−1,2,3,−3,−3,1,3) in (1.22), exact (2.11)–(2.17), Proposition 2.14A; Propositions 7.6–7.8 renumbered 7.6A–C. Referee report by Carbon. Checked and committed by Claude, with small edits (see below) | `revised/`, `referee/g2_shalika_germs_draft3_referee_report.tex`, this PR |
| 4 | 2026-11-14 | Fourth pass by Claude, after D. Joyner found the TeX version (2016) of Hales' memoir [Ha92a]: Lemma 5.17 proof corrected; Propositions 7.6D–7.6E and Corollary 7.6F (explicit κ(t_*) for the biquadratic tori; the predicted Hilbert symbol appears as a factor); new script `g2_cocycle_biquadratic.py` | `revised/`, this PR |
| 5 | 2026-11-14 | Fifth pass by Gemini ("Carbon"): the inversion correction in (7.10), direct construction of the biquadratic fiber birational map and proof of (X₂) modulo Lemmas 5.14 and 0.8, explicit C′(q), and cubic cocycle / hexagon-cover computation. The companion code passed five SymPy suites when executed during repository update. | `revised/`, `referee/g2_shalika_germs_draft5_referee_report.tex`, `scripts/verify_g2_open_problem_1.py`, `revised/CHANGES.md` |
| 6 | 2026-11-14 | Sixth pass by Gemini ("Carbon"): §8 intrinsic coordinates, SL₂(α)-fibration and split quadric cone (Propositions 8.3F–8.3G), and an evaluation of J₃(X) presented as a proof of (X₃). Refereed by Claude. When committing, Claude fixed the residue check in the script (the residue is −2/9, not ±2/27), made 8.3H a claim with a sketched proof, kept Theorem 8.3 conditional on (X₃), and added Open Problem (1)(a)–(c) | `revised/`, `referee/g2_shalika_germs_draft6_referee_report.tex`, `referee/g2_draft6_referee_report_claude.tex`, `scripts/verify_g2_open_problem_1.py`, `revised/CHANGES.md` |

**Source variants.** The body follows `g2new5.tex` and `g2new9.tex`. The variants `g2new5d.tex` (one parenthetical sentence in the proof of Lemma 5.14 and one word in §5) and `g2new9d.tex` (hypotheses (4) and (6) of Conjecture 9.1, and a closing sentence) are described in Remark 2026.42 and in the transcription. It is not known which version is later.

**Draft 5 upload check (2026-11-14).** The supplied `g2_shalika_germs_2026.tex` compiled with `pdflatex` in this environment; the supplied `verify_g2_open_problem_1.py` completed all five assertions suites under SymPy 1.14.0. Execution of another AI's assertions is not an independent proof of every claim. The Carbon Draft 5 referee report is included as an AI-authored report, not an independent certification. The uploaded PDF differs in pagination from our local build; source is authoritative.

**Draft 6 check by Claude (2026-11-14).**
- Draft 6 compiled with pdflatex (72 pages, clean).
- Five of the six scripts passed. `verify_g2_open_problem_1.py` failed in Suite 6, at the assertion that the residue at t_*(X) is ±2/27.
- A 50-digit numerical evaluation and an exact Laurent expansion over ℚ(√−3) both give a simple pole with residue −2/9, independent of X.
- The proof of 8.3H uses nine undefined objects, and it rests on a regularization not shown to agree with the principal value of [LS83].
- The full report is `referee/g2_draft6_referee_report_claude.tex`. The edits made on commit are listed in `revised/CHANGES.md`.

## AI usage

- **Claude (Anthropic, Opus 5.5)**, co-author.
  - As referee, it wrote the referee report on the 1994 manuscript (`referee/g2_referee_report.tex`).
  - As co-author and reviser, it made the transcription and drafted Draft 1: the corrections, the new statements and proofs, Remarks 2026.1–2026.45, the literature review, summary, glossary and acknowledgments, and `revised/CHANGES.md`.
  - It wrote and ran the verification scripts in `scripts/`.
  - It checked some bibliographic entries against publisher and arXiv records (see below).
- **Gemini ("Carbon", Google)** refereed Draft 1 and produced Drafts 2 and 3, the three `scripts/verify_g2_*.py` modules, and the Draft 3 referee report. Its report recommends acceptance as a preprint and states that every formula was confirmed; that report is by the author of Drafts 2–3, so it is not an independent referee.
- **Gemini ("Carbon")** also prepared Drafts 5 and 6, their verification program, changelog entries and referee / verification reports. These assess its own revisions and should not be treated as independent referees.
- **Claude** refereed Draft 6 and, when committing it, made the edits listed in `revised/CHANGES.md` (the residue check, Claim 8.3H, Theorem 8.3, Open Problem (1)).
- **D. Joyner** wrote the 1994 manuscript, directed the revision, and is responsible for the final text.

AI review is not an independent certification of the results. No human referee has read any draft.

### Claude's check of Draft 3 (2026-11-14)

- All three `verify_g2_*.py` scripts were rerun from a clean directory and pass (about 20 s in total). Their asserts were read: they test the stated identities in the 8×8 model of §A.4, not merely print values.
- Draft 3 compiles with pdflatex (62 pages) with no errors, undefined references or overfull boxes. Remark numbers 2026.1–45 are unchanged from Draft 1.
- **Draft 2's new fiber forms (7.3)–(7.4) are a genuine correction of Draft 1.** On E_{∅,α,δ} the map π is n⁻¹bn with b = θ_δθ_εθ_ζ, independent of z(β), w(γ), w(δ), so those are fiber directions. Draft 1's limit construction treated w(γ), w(δ) as orbit coordinates. The new fiber form scales as |c|² under X ↦ cX, as Corollary 7.6C requires.
- **Draft 2's face counts (268, 38) are right and Draft 1's (262, 32) were wrong**: `g2_exceptional_divisors.py` only enumerated faces with at most 7 rays and omitted σ itself. Fixed; the 5 minimal singular faces are unchanged.
- Hales 1989 (numdam) was checked through a machine reading of the PDF (L2). It confirms the §6 fiber coordinates z(β), v(β), w(ι), w(δ) and the birational map to (P¹)⁴, and Lemma 4.2 for Sp(2n) (on pp. 216–217). It also shows that Prop. 2.11 is a quasi-split reduction, not the reduction lemma, and that Prop. 2.14 treats H = H₁×H₂ up to finite center, a possible route for H₂ that no draft has explored.
- Documentation slips in Carbon's files: CHANGES.md and the scripts cited Remarks 2026.5, .8, .18, .23 where 2026.8, .11, .23, .36 were meant, and Propositions 7.6–7.8 by their Draft 1 numbers. Corrected in CHANGES.md and in the script docstrings; the Draft 3 referee report is committed unchanged.
- Edits to the paper: the Prop. 2.11 attribution (§5), a new open problem on Hales' product case, and the restored sentence "AI review is not an independent certification…" in the Acknowledgments (style guide).
- Not checked by Claude: the derivations behind (1.21b) and Proposition 2.14A beyond the scripts; the claim that Galois invariance under the two simple-reflection involutions settles input (iii) for the biquadratic torus, whose Galois image contains s_ζ and −1.
- **Author line.** Carbon's Draft 3 listed David Joyner alone. At David Joyner's direction the authors are now David Joyner, Claude and Gemini, since Carbon's contributions (the corrected fiber forms of §§7–8, the exact formulas of §§1–2, Proposition 2.14A, and the corrections in §A.3 and to the face counts) are substantial. The \thanks notes, the first sentence of the abstract and the Acknowledgments say so.

## Verification levels

As in the referee report:
- **L1**: checked here, by hand or by an exact computation whose script is in `scripts/`.
- **L2**: checked against a secondary account (for example a machine summary of a source), not the source itself.
- **L3**: taken on trust from a source that was not consulted.

| Item | Level | How |
|---|---|---|
| Patch formulas of §3, Igusa forms of §4, residue forms (8.1) and on E_{∅,α,δ} | L1 | `g2_patch_jacobians.py` (SymPy) |
| Kirillov–Kostant forms and Leray fiber forms (7.3)–(7.4), (8.4)–(8.5) (Draft 2) | L1 | `verify_g2_toric_and_forms.py` |
| Exact (1.21a), (1.21b), (1.22), (2.11)–(2.17), Proposition 2.14A (Draft 3) | L1 | `verify_g2_coordinates_and_galois.py` (identities in the 8×8 model) |
| Chevalley basis, torus embeddings (A.13)–(A.13′), orbit dimensions, Dynkin-curve lines, Table A.6 | L1 | `verify_g2_chevalley_and_endoscopy.py` |
| Regularity of the twelve patches (Proposition 3.4A) | L1 | `g2_patch_regularity.py` |
| Covering up to codimension 2; branches and Igusa constants (Table 4.3A) | L1 | `g2_toric_divisors.py` |
| Normality of Z (Proposition 3.7): 658,651 lattice points | L1 | `g2_saturation_full.py` |
| Singular faces of the fan; candidate exceptional divisors (Remark 2026.23) | L1 | `g2_exceptional_divisors.py` |
| H¹(F,T) and endoscopic roots for all elliptic tori (Table A.6) | L1 | `g2_tori_endoscopy.py` |
| Lemma 3.5 (new proof), Lemma 3.6, Lemma 5.6, Lemma 4.4 for G₂, A.5 | L1 | by hand |
| Lie(Z(H)) = 0 and centralizers are Levi subgroups (Remark 2026.29) | L1 | by hand |
| Count of étale cubic algebras (Remark 2026.46) | L1 | by hand |
| Δ₀ for the biquadratic tori (Proposition 7.6A), Corollary 7.6C | L1 | by hand; root data by `g2_transfer_factor_biquadratic.py` |
| Example 7.6B (Hilbert symbols over Q_p, p = 5,…,23) | L1 | `g2_transfer_factor_biquadratic.py` |
| Projection formula (x, a)_L = (N x, a)_F; definitions of Δ_I–Δ_IV | L3 | standard, from [Ser79], [LS87] |
| Hales' descent in [Ha89] and the explicit SO(4) computation | L2 | Carbon read [Ha89] directly; Claude checked through a machine reading of the numdam PDF |
| [Ha92a] Ch. I §5 (Eq. 5.3, Cor. 5.4, 5.7, Rem. 5.6), Ch. II §7 (Prop. 7.3), Prop. II.9.1 | S | read in the TeX version (2016) by Claude (Draft 4) |
| [Ha92a] Ch. V, VI (θ = 1, Dynkin lines, κ(E_α)) | L3 | quoted from 1994; now available to check |
| Draft 5: (7.10) inversion, (X₂) fiber map, C′(q), cubic cocycle, hexagon cover | L1 for executable identities only | `verify_g2_open_problem_1.py` (all five suites executed on 2026-11-14); geometric and analytic completeness not independently certified |
| Draft 6: Propositions 8.3F–8.3G, 6×6 Jacobian audit; residue −2/9 at t_*(X) | L1 | `verify_g2_open_problem_1.py`, Suite 6 (residue by exact Laurent expansion over ℚ(w)) |
| Claim 8.3H: Mellin regularization, B₁(1) = 0, shell sums giving C₃(q) | L3 | sketch only; the script checks the algebra of the typed-in formulas (Open Problem (1)(b)) |
| Theorem 7.6H(d): regularized factors I_t, I_s, I_ξ of C′(q) | by hand, unchecked | the script checks only their product (Open Problem (1)(c)) |
| Propositions 7.6D–7.6E: cocycle by principal minors, R, Q, leading terms on E_{∅,α,δ} | L1 | `g2_cocycle_biquadratic.py` (symbolic; leading terms checked numerically against exact (1.21a) to 10⁻¹²) |
| Tate–Nakayama restriction to L in Proposition 7.6D; projection formula in 7.6E | L1/L3 | by hand; standard facts from [Ser79] |
| [Ha92b] Lemma 6.1 (Lemma 5.19) | L3 | not consulted |
| [La83] Lemma 2.12 and the principal value formulas | L3 | not consulted |
| Corollary 8.8 (normalizations in (0.1), Formula 0.6 and [GH16]) | L3 | not checked in detail |

## Original and new results (style guide, rule 6.5)

**Original (1994), kept with corrections:** §0: Conjecture 0.0A (Matching of germs, from [LS89]), Lemma 0.4, Formula 0.6, Lemma 0.8 (now with a proviso). §1: Lemmas 1.5, 1.12, 1.21, Corollary 1.6, Definition 1.16 (corrected), (1.8)–(1.22). §2: Lemmas 2.10, 2.15, (2.1)–(2.17). §3: the patch construction, Conjecture 3.4, Lemmas 3.5 and 3.6 (corrected), Notation 3.3d. §4: the patch list, the Igusa forms (corrected), Table 4.3 (corrected), Lemma 4.4 (corrected). §5: Lemmas 5.6, 5.7, 5.10, 5.14 (now a hypothesis), 5.17, 5.19 (as quoted). §§6–8: Lemma 6.4, the computations (6.2)–(6.5), (7.1)–(7.5), (8.1)–(8.7). §9: Conjecture 9.1 (restated). Appendix A.1–A.7.

**Restated:** Theorems 6.1, 7.2 and 8.3 are now conditional germ identities (Remarks 2026.29, 2026.31, 2026.34, 2026.36). Lemma 3.7 is now Proposition 3.7 (for G₂) and Conjecture 3.7A.

**Removed:** the decomposition f = f₁ + f₂ before Lemma 5.19; the sentence "spurious divisors do not contribute" in Lemma 5.14; the complete-intersection claim of Lemma 3.7; the untypeset material after `\enddocument` in four source files.

**New in 2026:**
- Statements: Conjecture 0.0 as stated, Definition 1.3, Proposition 3.4A, Proposition 3.7, Conjecture 3.7A, Hypotheses (X_r) (Remark 2026.29), Proposition 7.6A, Example 7.6B, Corollary 7.6C, Proposition 2.14A and the exact formulas (1.21a), (1.21b) (Draft 3), Corollary 8.8.
- Tables and figures: Table 4.3A, Table A.6, the Dynkin curve figure.
- Proofs: Lemma 3.5, Lemma 5.6, Proposition 3.4A, Proposition 3.7, Corollary 8.8, A.5, A.6.
- Sections: the literature review, the notation table, the summary of results and open problems, the glossary.
- Statements added in Drafts 4–6: Propositions 7.6D–7.6G, Corollary 7.6F, Theorem 7.6H, Propositions 8.3A–8.3G, Corollary 8.3B, Claim 8.3H (sketch).
- Remarks 2026.1–2026.46.

**Numbering.** The 1994 numbering is kept. New items carry letters or follow the last 1994 number of their section, so no concordance is needed.

## Sources that could not be consulted, or were not checked (style guide, rule 4.3)

- [Ha92b] (Hales, U(3)): Lemma 6.1, the source of Lemma 5.19, was not consulted.
- [Ha89] (Hales, GSp(4)): consulted directly by Carbon in Draft 2; checked by Claude through a machine reading (L2).
- [Ha92a] (Hales, subregular germ): consulted in Draft 4 (TeX version of 2016). Ch. I §5 and Ch. II §§7, 9 were read. Hales' Prop. II.7.3 agrees with (1.21b) for n_α, n_β, n_γ; the other three were not compared, because the sign conventions differ. Results quoted from Ch. V and VI have not yet been rechecked.
- [La83], [LS83]: the principal value formalism and [La83, Lemma 2.12] are quoted, not checked (Remark 2026.33).
- [As98]: the count of F-classes in the subregular class could not be compared with Assem's (Remark 2026.46).
- [SV00]: cited for the triality theorem without checking the exact formulation (Remark 2026.43).
- [Ha92a], [Ha89]: the 1994 claims that Conjecture 3.4 is known for A_n and C_n, and false for D_n, were not checked (Remark 2026.15).
- The two works cited only in `g2new9d.tex` as [A] and [H4] are not identified.
- **Bibliography.** Checked in the referee report against publisher or library records: [Ra72], [Ro80], [She89], [Ha89], [Ha92b], [La83], [LS83]. Checked in this draft against publisher or arXiv records: [As00], [Ts15]. The data for [As98], [GH16], [Wa97], [Ng10], [Wa01], [De02], [Ha94] are as recorded during the referee report. The remaining entries carry over the 1994 data with page ranges and publication details added from standard references; they have not been individually checked.

## Next steps (after Draft 6)

1. Complete Claim 8.3H: define the objects in its proof, show that the Mellin regularization computes the Langlands–Shelstad principal value, and derive the shell sums (Open Problem (1)(b), Remark 2026.40).
2. Check the regularized factors of C′(q) in Theorem 7.6H(d) independently (Open Problem (1)(c)).
3. Settle (X₁) for the 1-regular germ (Open Problem (1)(a)).
4. Resolve the exceptional and spurious divisor proviso (Lemma 0.8) and the contribution of the β = 11/3 branch.
5. Revisit the outstanding cases of elliptic tori and the product-group comparison from Hales, with checked citations.
6. Seek an independent mathematical review of §§7–8, including the assumptions of Lemmas 5.14 and 0.8, and request a human specialist referee. Passing symbolic assertions is not a substitute for such a review.


## Post-Draft-6 auxiliary calculations (2026-11-15)

- Added `notes/shell-sums-2026-11-15.tex`: an independent research note deriving valuation-shell expressions for the quadratic factors `I_t`, `I_s`, `I_xi` and for the **proposed** cubic factors `I_{P^1(K)}`, `B_1'(1)`, and `B_2(1)` under the explicitly chosen Mellin continuations.
- Added `scripts/verify_g2_shell_sums_independent.py`, a standalone Python 3 / SymPy checker that passed before commit. It confirms arithmetic identities but cannot test the analytic definitions of regularized integrals.
- Status: Open Problem (1)(c) is reduced to reconciling the chosen meromorphic continuations with the Langlands–Shelstad principal-value construction. The analogous compatibility, the cone factorization and the geometry of exceptional divisors remain open for Open Problem (1)(b); Hypothesis (X_3) is **not** proved by this note. Draft number remains 6.
- The companion PDF was generated locally but is not included in this source-only commit.

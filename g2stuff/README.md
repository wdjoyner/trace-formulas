# On the transfer of Shalika germs for G₂

An unpublished manuscript by David Joyner, dated summer 1994, and its corrected and expanded 2026 revision with AI assistance.

The manuscript uses Langlands' Igusa-theoretic method to match the 1-, 2- and
3-regular κ-Shalika germs of the split exceptional group G₂ with germs on its
cuspidal endoscopic groups PGL(3) and (SL(2)×SL(2))/{±1}. It then argues
that this, together with Shelstad's result for the regular germ, gives local
transfer for G₂.

## Layout

```
g2stuff/
├── original-1994/   the 1994 AMS-TeX source files, unchanged
├── transcription/   literal single-file amsart transcription (no corrections)
├── referee/         referee reports on the 1994 manuscript and later drafts
├── notes/           independent analytical notes (not part of the main draft)
├── scripts/         computational checks accompanying the revised drafts
├── revised/         corrected edition (currently Draft 9) and CHANGES.md
├── revision_log.md  drafts, AI usage, verification levels, sources not consulted
└── README.md
```

## Contents

| File | What it is |
| --- | --- |
| `original-1994/g2new0.tex` … `g2new9.tex`, `g2newapp.tex`, `g2newref.tex` | The manuscript as written, one AMS-TeX file per section (§0–§9, appendix, references). |
| `original-1994/g2new5d.tex`, `g2new9d.tex` | Variant versions of §5 and §9. It is not known which version is later. |
| `transcription/g2_shalika_germs_transcription.tex`, `.pdf` | All sections in one amsart file, 12pt Times, letter paper, 49 pages. It is literal, as in §6.7 of the style guide: errors are kept, and Claude's notes appear only as `% Claude:` comments. The variant passages and the text that follows `\enddocument` in four source files are kept in `\iffalse` blocks, all of which compile when switched on. |
| `referee/g2_referee_report.tex`, `.pdf` | Referee report by Claude (15 pages): eleven major issues, a table of minor issues and misprints, the results verified as correct, readability, a bibliography check, compliance with the style guide, and notes on the transcription. Every point has a verdict and a verification level (L1–L3). It also serves as the errata log for the transcription. |
| `revised/g2-shalika-germs-2026.tex`, `.pdf` | **Draft 9** corrected and expanded edition (82 pages), a readability revision of Draft 8 (the final mathematical form), by David Joyner, Claude, and Gemini (Carbon). It proves (X₂) for the biquadratic tori, subject to the manuscript's remaining hypotheses, and states the expected value of the cubic fiber integral as Conjecture 8.3H; (X₁) and (X₃) are open problems. The PDF is built from the committed source. |
| `referee/g2_shalika_germs_draft3_referee_report.tex`, `.pdf` | Report on Draft 3 by Carbon (5 pages), the author of Drafts 2–3, so not independent. Recommends release as a preprint. Claude's check of Draft 3 is in `revision_log.md`. |
| `revised/CHANGES.md` | Consolidated history of Drafts 1–9 and the 1994 errata, including Claude's edits when committing Draft 6 and the Draft 7 editorial pass (with the renumbering of the Remarks 2026.n). |
| `referee/g2_shalika_germs_draft5_referee_report.tex` | Carbon's 3-page Draft 5 referee / verification report (author of this revision; not an independent referee). |
| `referee/g2_shalika_germs_draft6_referee_report.tex`, `.pdf` | Carbon's 3-page Draft 6 report (by the author of the revision; not an independent referee). Committed unchanged; it predates the corrections below. |
| `referee/g2_draft6_referee_report_claude.tex`, `.pdf` | Claude's 4-page referee report on Draft 6: the failed residue check (the residue is −2/9, not ±2/27), the incomplete proof of 8.3H, the overstated abstract, and how each point was handled on commit. |
| `referee/g2_draft6_referee_report_claude_2.tex`, `.pdf` | Claude's second report (5 pages) on the post-Draft-6 source, including the November 15 remark: the compile error, independent checks, the scope of the repeated-polar issue for Claim 8.3H, a wrong Jacobian in the proof of Theorem 7.6H, and readability. Its points were addressed in Draft 7. |
| `referee/g2_draft8_readability_plan_carbon.md` | Carbon's editorial plan for Draft 8: inline formulas to display, dense paragraphs to split, and extra vertical spacing. Carried out in Draft 9; it changes no mathematics. |
| `scripts/verify_g2_open_problem_1.py` | SymPy suite for Drafts 5–6, six suites: §6 Pfaffians; §7 identities, birational map and the product giving C′(q); §8 cocycle and cover; Propositions 8.3F–8.3G, the residue at t_* (exact), and the arithmetic of the C₃(q) shell formulas. About 20 s. |
| `revision_log.md` | Drafts, AI usage, verification levels (L1–L3), original vs. new results, sources not consulted, next steps. |
| `scripts/g2_toric_divisors.py` | Toric structure of the monomial variety Z of §3: every branch of λ = 0 with its Igusa constants a, b, β, and which patches meet which divisors (about 75 s). |
| `scripts/g2_saturation_full.py` | A complete proof that the semigroup of Z is saturated, so Z is normal for G₂. |
| `scripts/g2_patch_jacobians.py`, `g2_patch_regularity.py` | The patch formulas of §3, the Igusa forms of §4, the residue forms on the β = 3, 4 branches, and the regularity of the twelve patches. (Its versions of (7.3)–(7.4), (8.4)–(8.5) are the superseded 1994-style ones.) |
| `scripts/verify_g2_chevalley_and_endoscopy.py` | Carbon (Drafts 2–3): the Chevalley basis of §A.4, torus embeddings (A.13)–(A.13′), orbit dimensions, the Dynkin-curve lines of Figure 1, Table A.6, Example 7.6B. |
| `scripts/verify_g2_toric_and_forms.py` | Carbon: cone facets and patches, the face lattice of σ (268 faces of dim ≥ 2, 38 singular), Lemma 4.4 orbit images, Kirillov–Kostant and Leray forms (7.3)–(7.4), (8.4)–(8.5). |
| `scripts/verify_g2_coordinates_and_galois.py` | Carbon: exact (1.21a), (1.21b), (1.22), (2.11)–(2.17) and Proposition 2.14A in the 8×8 model. |
| `scripts/g2_exceptional_divisors.py` | The singular torus orbits of Z and candidate exceptional divisors of a toric resolution (face count corrected in Draft 3). |
| `scripts/g2_cocycle_biquadratic.py` | Draft 4: Hales' cocycle t_* by principal minors, the polynomials R and Q of (7.8), their leading terms on the 2-regular divisor (checked against exact formulas), and the norm identities behind Proposition 7.6E. |
| `scripts/g2_transfer_factor_biquadratic.py` | The root data behind Proposition 7.6A and the Hilbert symbols of Example 7.6B over Q_p. |
| `scripts/g2_tori_endoscopy.py` | H¹(F,T) for every elliptic torus of split G₂, and the root system of the endoscopic group for each κ. |
| `scripts/verify_g2_thm76H_rational_points.py`, `verify_g2_prop83F_rational_points.py` | Claude (Draft 7): independent exact checks at random rational points of Theorem 7.6H(b), (7.12), the Jacobian in the proof of Theorem 7.6H, Proposition 7.6G(a), Proposition 8.3F(a), and Example 7.6B(b). The first takes a few minutes. |

The scripts need Python 3 with NumPy, SymPy and SciPy. They are named so that
`../run_checks.py` does not run them, because they take longer and need SciPy.
Run them one at a time, for example `python3 g2_tori_endoscopy.py`.

## Independent follow-up note (November 15, 2026)

- [`notes/conjecture-8.3H-heuristic-2026-11-16.tex`](notes/conjecture-8.3H-heuristic-2026-11-16.tex) preserves the Draft 7 sketch of the evaluation of `J₃(X)` (now Conjecture 8.3H), including the auxiliary functions defined only in explicit models of K.
- [`notes/shell-sums-2026-11-15.tex`](notes/shell-sums-2026-11-15.tex) derives the valuation-shell continuations behind the quadratic constant \(C'(q)\) and the proposed cyclic-cubic constant \(C_3(q)\). This is an auxiliary research note, **not a new draft of the main manuscript**. For the **isolated one-dimensional cubic factors**, §1 of Langlands–Shelstad's paper now supplies a direct principal-value justification, as proved in the expanded note. However, the **global cubic-cone regulator and fiberwise factorization** have not been justified; \((X_3)\) remains open by direct computation. The note also verifies that the affine cubic quadric cone has a singular vertex, whose blow-up creates an exceptional \(\mathbb P^1\times\mathbb P^1\) requiring analysis.
- [`scripts/verify_g2_shell_sums_independent.py`](scripts/verify_g2_shell_sums_independent.py) is a pure-Python/SymPy checker, independent of the earlier suites. Run `python3 scripts/verify_g2_shell_sums_independent.py` from `g2stuff/`.


## Cubic exceptional-divisor audit (November 15, 2026)

- [`notes/cubic-exceptional-orders-2026-11-15.md`](notes/cubic-exceptional-orders-2026-11-15.md) computes the **actual** 3-form, cubic character, and Igusa regulator from Proposition 8.3G(b) on the blow-up of the singular vertex of the cyclic-cubic quadric cone. The generic exceptional orders are **(+1, 0, 0)**. An exact norm identity cancels the common `Lambda_F^{-3}` factor in the ratio of form and regulator.
- [`scripts/verify_g2_cubic_exceptional_orders.py`](scripts/verify_g2_cubic_exceptional_orders.py) independently verifies the rational coordinate, norm, Jacobian and ratio identities using Python 3 + SymPy. Run `python3 scripts/verify_g2_cubic_exceptional_orders.py`.
- **Remaining analytic issue:** along the transverse intersection with `H0 + r*H1 = 0`, both form and regulator have order **−3**; the corresponding principal value is not justified by this generic calculation. Other blow-up charts, Igusa boundary divisors, Lemmas 0.8/5.14, and direct `(X_3)` remain open. The principal manuscript is still **Draft 6**.


### Four-chart cubic intersection audit (November 15, 2026)

- [`notes/cubic-four-chart-intersections-2026-11-15.md`](notes/cubic-four-chart-intersections-2026-11-15.md) ([printable LaTeX source](notes/cubic-four-chart-intersections-2026-11-15.tex)) computes the actual cubic fiber form, regulator, and character on all four vertex blow-up charts. For regular `X`, polar and boundary curves are disjoint on the exceptional surface; they have explicit triple intersections away from it. The note also identifies a repeated-polar exceptional case and the generic orders (0, 0) after blowing up a triple-intersection curve.
- [`scripts/verify_g2_four_blowup_charts.py`](scripts/verify_g2_four_blowup_charts.py) is a standalone exact SymPy checker for the four charts, cyclic common denominator, regulator norm cancellation, boundary/polar equations and repeated-polar case. Run `python3 scripts/verify_g2_four_blowup_charts.py` from `g2stuff/`. The checker also verifies the coordinates of the isolated third-norm zeros; it does not resolve them. The LaTeX source builds with two runs of `pdflatex` (12pt Times, US Letter). The compiled PDF is distributed separately and has not been committed.
- **Scope limitation:** this is an auxiliary analysis, not a proof of global Langlands–Shelstad principal-value compatibility or `(X_3)`. The isolated third-norm points and further global boundary/resolution checks remain open. Draft 6 of the main paper is unchanged.


### Special cubic local resolutions (November 15, 2026)

- [Repeated-polar and third-norm local resolution note](notes/cubic-special-local-resolutions-2026-11-15.md): explicit two-curve-blow-up SNC resolution of the repeated polar \(\mathscr D=0\), and three-stage (curve, point, curve) local resolution at all four isolated third-norm intersections. Exceptional orders are computed for the actual cubic fiber 3-form, regulator and cubic-character argument. The repeated-polar new divisors have orders \((-1,-3)\) and \((-2,-6)\) for (form, regulator); the third-norm new divisors have \((0,0),(+2,+1),(+1,+1)\), with nontrivial character exponents \(1,2,1\bmod3\).
- [Standalone Python/SymPy checker](scripts/verify_g2_special_resolution.py): algebraic factorization and blow-up/Jacobian regression checks; run from the g2stuff directory with **python3 scripts/verify_g2_special_resolution.py**. The longer printed 12-point Times LaTeX/PDF exposition is available as a conversation attachment; only the Markdown note and code are committed.
- **Limits:** the blow-up models are local over a splitting field, not a proof of Galois descent, global Langlands–Shelstad principal-value compatibility, Lemmas 0.8/5.14, or \((X_3)\). Main manuscript **still Draft 6**.


## Cubic Galois descent and Langlands--Shelstad resonance (November 15, 2026)

- [Descent and resonance research note](notes/cubic-galois-descent-ls-resonance-2026-11-15.md): the *six* geometric third-norm points (only four lie on the earlier x0 chart) form **two degree-three Galois orbits**, whose equivariant blow-ups have no F-rational exceptional points. In fact the split cubic boundary components have no F-points off the vertex. Their local split-field character exponents are not separate F-principal-value contributions.
- [Independent SymPy checker](scripts/verify_g2_descent_ls.py): verifies the two Galois orbits, omitted x0-chart points, the repeated-polar F-point, the first exceptional valuation and the localized Mellin pole. Run with Python 3 and SymPy.
- **New obstruction:** when the repeated-polar discriminant \(\mathscr D=M^2+3\Delta^2\) vanishes, the first new exceptional divisor has actual fiber-form order \(-1\), regulator order \(-3\), and **trivial** cubic character. Langlands--Shelstad's nonresonance condition (1.4) therefore fails. The proposed single Mellin factor \(|R_{\rm cone}|^{\sigma/3}\) produces a localized simple pole at \(\sigma=0\). The cited LS theorem assumes characteristic-zero local fields.
- **Main paper unchanged:** these results do **not** prove Claim 8.3H or \((X_3)\). A globally invariant regularization or a proof that the exceptional special \(X\) is excluded is still required. A printable five-page LaTeX/PDF appendix was prepared separately; the repository files here are the Markdown note and Python checker.


### Regularity and repeated-polar discriminant (November 15, 2026)

- [Full regularity/discriminant proof](notes/cubic-regularity-discriminant-2026-11-15.md) shows **every nonzero \(X\in\mathfrak t(F)\) is regular** for the cyclic-cubic torus, but \(\mathscr D=M^2+3\Delta^2=6\operatorname{Tr}_{K/F}(\alpha(X)^2)\) can vanish on **two regular \(F\)-lines** precisely when \(\mu_3\subset F\), or equivalently \(q\equiv1\bmod3\) in residue characteristic at least \(5\). This includes all tame ramified cyclic cubic cases and some unramified cases; an explicit unramified example uses \(F=\mathbb Q_7\), \(K=F(\sqrt[3]{2})\). Scaling \(X\) toward zero does not remove the repeated-polar condition.
- [Independent SymPy verification](scripts/verify_g2_polar_regular.py): run \`python3 scripts/verify_g2_polar_regular.py\` from \`g2stuff/\`. It checks the root formulas and discriminant algebra, not principal values.
- **Implication:** the repeated-polar Langlands--Shelstad resonance reported in the descent note cannot be excluded by the manuscript's regularity or smallness assumptions. The result is now also included **in the main TeX manuscript** as Remark \`rem:8.polar-regular\`, immediately following Proposition 8.3G, with a cross-reference from the status of Claim 8.3H. No result here proves or disproves \((X_3)\); the draft number remains 6.

## Status

**Draft 9 of the corrected edition (November 27, 2026).** Draft 9 is a readability revision of Draft 8, made from Carbon's editorial plan (`referee/g2_draft8_readability_plan_carbon.md`): the inline formulas it lists are now displayed, nine dense paragraphs are split, and multi-line displays have more vertical space. No statement, label or equation number changed. Draft 8 (November 16, 2026) is the final mathematical form. It completes the write-up of Draft 7: the evaluation of the cubic fiber integral is stated as Conjecture 8.3H with a heuristic derivation, intermediate formulas are printed, and (X₁) and (X₃) are stated as open problems. The editable source is `revised/g2-shalika-germs-2026.tex`; the committed PDF is built from it.

- **Established in the revision, subject to the paper's stated assumptions (Lemma 5.14 and the proviso of Lemma 0.8):**
  - the normal, Cohen–Macaulay toric model, its codimension-one patches, and the special-fiber constants;
  - for the biquadratic tori, a birational map of the 4-dimensional fiber to `(P¹)^4` and a direct proof of `(X₂)` (Theorem 7.6H);
  - for the cyclic cubic tori, the fibration of the 6-dimensional fiber onto a split quadric cone (Propositions 8.3F–8.3G).
- **Conjectural:** the value of the cubic fiber integral `J₃(X)` that would prove `(X₃)`, with constants `C₃(q)` (Conjecture 8.3H, with a heuristic derivation; the earlier detailed sketch is in `notes/conjecture-8.3H-heuristic-2026-11-16.tex`). Open Problem (1)(b) and Remark 2026.23 list what is missing to prove Conjecture 8.3H, including the repeated-polar directions of Remark 2026.22 (numbering of Drafts 7–8). The main gap is that the Mellin regularization used has not been shown to compute the Langlands–Shelstad principal value.
- **Still conditional or open:**
  - the direct `(X₁)` and `(X₃)` calculations;
  - an independent check of the hand-evaluated factors of `C′(q)`;
  - the exceptional and spurious divisors, and the β = 11/3 contribution;
  - the remaining torus cases.
- **Computational check:** `verify_g2_open_problem_1.py` passes all six suites under SymPy 1.14.0. Draft 6 as delivered failed Suite 6 (its residue check); Claude replaced that check with an exact Laurent expansion, which gives −2/9. The suites check identities, not the analytic steps.

The original 1994 manuscript and earlier drafts remain in Git history and in their existing directories. No human referee is represented here.

AI review is not an independent certification of the results.

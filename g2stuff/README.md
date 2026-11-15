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
├── revised/         corrected edition (currently Draft 6) and CHANGES.md
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
| `revised/g2-shalika-germs-2026.tex`, `.pdf` | **Draft 6** corrected and expanded edition (73 pages), by David Joyner, Claude, and Gemini (Carbon). It proves (X₂) for the biquadratic tori, subject to the manuscript's remaining hypotheses, and sketches (X₃) for the cyclic cubic tori. The PDF is built from the committed source. |
| `referee/g2_shalika_germs_draft3_referee_report.tex`, `.pdf` | Report on Draft 3 by Carbon (5 pages), the author of Drafts 2–3, so not independent. Recommends release as a preprint. Claude's check of Draft 3 is in `revision_log.md`. |
| `revised/CHANGES.md` | Consolidated history of Drafts 1–6 and the 1994 errata, including Claude's edits when committing Draft 6. |
| `referee/g2_shalika_germs_draft5_referee_report.tex` | Carbon's 3-page Draft 5 referee / verification report (author of this revision; not an independent referee). |
| `referee/g2_shalika_germs_draft6_referee_report.tex`, `.pdf` | Carbon's 3-page Draft 6 report (by the author of the revision; not an independent referee). Committed unchanged; it predates the corrections below. |
| `referee/g2_draft6_referee_report_claude.tex`, `.pdf` | Claude's 4-page referee report on Draft 6: the failed residue check (the residue is −2/9, not ±2/27), the incomplete proof of 8.3H, the overstated abstract, and how each point was handled on commit. |
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

The scripts need Python 3 with NumPy, SymPy and SciPy. They are named so that
`../run_checks.py` does not run them, because they take longer and need SciPy.
Run them one at a time, for example `python3 g2_tori_endoscopy.py`.

## Status

**Draft 6 of the corrected edition (November 14, 2026).** The editable source and the PDF built from it are in `revised/g2-shalika-germs-2026.tex` and `revised/g2-shalika-germs-2026.pdf`.

- **Established in the revision, subject to the paper's stated assumptions (Lemma 5.14 and the proviso of Lemma 0.8):**
  - the normal, Cohen–Macaulay toric model, its codimension-one patches, and the special-fiber constants;
  - for the biquadratic tori, a birational map of the 4-dimensional fiber to `(P¹)^4` and a direct proof of `(X₂)` (Theorem 7.6H);
  - for the cyclic cubic tori, the fibration of the 6-dimensional fiber onto a split quadric cone (Propositions 8.3F–8.3G).
- **Sketched only:** the evaluation of the cubic fiber integral `J₃(X)` that would prove `(X₃)`, with constants `C₃(q)` (Claim 8.3H). Open Problem (1)(b) and Remark 2026.40 list what is missing. The main gap is that the Mellin regularization used has not been shown to compute the Langlands–Shelstad principal value.
- **Still conditional or open:**
  - the direct `(X₁)` and `(X₃)` calculations;
  - an independent check of the hand-evaluated factors of `C′(q)`;
  - the exceptional and spurious divisors, and the β = 11/3 contribution;
  - the remaining torus cases.
- **Computational check:** `verify_g2_open_problem_1.py` passes all six suites under SymPy 1.14.0. Draft 6 as delivered failed Suite 6 (its residue check); Claude replaced that check with an exact Laurent expansion, which gives −2/9. The suites check identities, not the analytic steps.

The original 1994 manuscript and earlier drafts remain in Git history and in their existing directories. No human referee is represented here.

AI review is not an independent certification of the results.

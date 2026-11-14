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
├── scripts/         computational checks accompanying the revised drafts
├── revised/         corrected edition (currently Draft 5) and CHANGES.md
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
| `revised/g2-shalika-germs-2026.tex`, `.pdf` | **Draft 5** corrected and expanded edition, by David Joyner, Claude, and Gemini (Carbon), with explicit biquadratic 2-regular computations subject to the manuscript's remaining hypotheses. The source and supplied 69-page PDF are both included. |
| `referee/g2_shalika_germs_draft3_referee_report.tex`, `.pdf` | Report on Draft 3 by Carbon (5 pages), the author of Drafts 2–3, so not independent. Recommends release as a preprint. Claude's check of Draft 3 is in `revision_log.md`. |
| `revised/CHANGES.md` | Consolidated history of Drafts 1–5 and the 1994 errata; preexisting detailed entries preserved. |
| `referee/g2_shalika_germs_draft5_referee_report.tex` | Carbon's 3-page Draft 5 referee / verification report (author of this revision; not an independent referee). |
| `scripts/verify_g2_open_problem_1.py` | Draft 5 SymPy suite: five checks for §6 Pfaffians, §7 identities and birational map, p-adic constants and §8 cocycle / cover. |
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

**Draft 5 of the corrected edition (November 14, 2026).** The editable source and its supplied PDF are in `revised/g2-shalika-germs-2026.tex` and `revised/g2-shalika-germs-2026.pdf`.

- **Established in the revision, subject to the paper's stated assumptions:** the normal and Cohen–Macaulay toric model, codimension-one patches, special-fiber constants, and the explicit 2-regular biquadratic calculation. Draft 5 constructs a birational map of the 4-dimensional fiber to `(P¹)^4`, evaluates `C'(q)`, and gives a direct argument for `(X₂)` for the biquadratic tori under the remaining hypotheses involving Lemmas 5.14 and 0.8.
- **Still conditional or open:** the direct `(X₁)` and `(X₃)` calculations, exceptional and spurious divisors, the β = 11/3 contribution, and remaining torus cases. The §8 cubic cocycle and hexagon double cover do not themselves prove `(X₃)`.
- **Computational check:** the added `verify_g2_open_problem_1.py` passed all five symbolic suites when run on November 14, 2026. This checks the supplied identities but is not an independent mathematical certification.

The original 1994 manuscript and earlier drafts remain in Git history and their existing directories. Draft 5's referee / verification report was written by Carbon, which also revised the manuscript. No human referee is represented here.

AI review is not an independent certification of the results.

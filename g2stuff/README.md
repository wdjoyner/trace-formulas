# On the transfer of Shalika germs for G₂

An unpublished manuscript by David Joyner, dated summer 1994, and the first
steps of its 2026 revision with AI assistance.

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
├── referee/         referee report on the 1994 manuscript
├── scripts/         exact computations used in the referee report and Draft 1
├── revised/         the corrected edition (Draft 1) and CHANGES.md
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
| `revised/g2-shalika-germs-2026.tex`, `.pdf` | **Draft 3. Corrected and expanded version** (62 pages), by David Joyner with Claude (Draft 1) and Gemini/"Carbon" (Drafts 2–3). Original numbering kept; new items lettered; every change or gap flagged in a Remark 2026.n (45 of them). |
| `referee/g2_shalika_germs_draft3_referee_report.tex`, `.pdf` | Report on Draft 3 by Carbon (5 pages), the author of Drafts 2–3, so not independent. Recommends release as a preprint. Claude's check of Draft 3 is in `revision_log.md`. |
| `revised/CHANGES.md` | Changelog for Drafts 2–3 (Carbon), then what Draft 1 did with each item of the 1994 referee report, with a table of the Remarks 2026.n. |
| `revision_log.md` | Drafts, AI usage, verification levels (L1–L3), original vs. new results, sources not consulted, next steps. |
| `scripts/g2_toric_divisors.py` | Toric structure of the monomial variety Z of §3: every branch of λ = 0 with its Igusa constants a, b, β, and which patches meet which divisors (about 75 s). |
| `scripts/g2_saturation_full.py` | A complete proof that the semigroup of Z is saturated, so Z is normal for G₂. |
| `scripts/g2_patch_jacobians.py`, `g2_patch_regularity.py` | The patch formulas of §3, the Igusa forms of §4, the residue forms on the β = 3, 4 branches, and the regularity of the twelve patches. (Its versions of (7.3)–(7.4), (8.4)–(8.5) are the superseded 1994-style ones.) |
| `scripts/verify_g2_chevalley_and_endoscopy.py` | Carbon (Drafts 2–3): the Chevalley basis of §A.4, torus embeddings (A.13)–(A.13′), orbit dimensions, the Dynkin-curve lines of Figure 1, Table A.6, Example 7.6B. |
| `scripts/verify_g2_toric_and_forms.py` | Carbon: cone facets and patches, the face lattice of σ (268 faces of dim ≥ 2, 38 singular), Lemma 4.4 orbit images, Kirillov–Kostant and Leray forms (7.3)–(7.4), (8.4)–(8.5). |
| `scripts/verify_g2_coordinates_and_galois.py` | Carbon: exact (1.21a), (1.21b), (1.22), (2.11)–(2.17) and Proposition 2.14A in the 8×8 model. |
| `scripts/g2_exceptional_divisors.py` | The singular torus orbits of Z and candidate exceptional divisors of a toric resolution (face count corrected in Draft 3). |
| `scripts/g2_transfer_factor_biquadratic.py` | The root data behind Proposition 7.6A and the Hilbert symbols of Example 7.6B over Q_p. |
| `scripts/g2_tori_endoscopy.py` | H¹(F,T) for every elliptic torus of split G₂, and the root system of the endoscopic group for each κ. |

The scripts need Python 3 with NumPy, SymPy and SciPy. They are named so that
`../run_checks.py` does not run them, because they take longer and need SciPy.
Run them one at a time, for example `python3 g2_tori_endoscopy.py`.

## Status

**Draft 3 of the corrected edition (November 14, 2026).** Refereed by AI
systems only (Claude on Draft 1's source, Carbon on Drafts 1 and 3); no human
referee yet.

- **Proved for G₂ (with exact computations in `scripts/`).** Z is a normal,
  Cohen–Macaulay toric variety (Proposition 3.7), covered up to codimension
  two by twelve regular patches (Proposition 3.4A). λ = 0 has exactly seven
  branches, with the Igusa constants of Table 4.3A. Table A.6 lists all
  elliptic endoscopic data; the roots of PGL(3) are the short roots.
- **Conditional.** Theorems 6.1, 7.2 and 8.3 are now germ identities, proved
  on Hypotheses (X_r) (Remark 2026.29) about how explicit fiber integrals
  depend on the tangent direction X, plus Lemma 5.14 and the proviso of
  Lemma 0.8 (exceptional and spurious divisors). Corollary 8.8 notes that
  (X_r) hold a posteriori, given Gordon–Hales.
- **The 2-regular case.** For the biquadratic tori the transfer-factor term
  Δ₀(X) is computed (Proposition 7.6A). It is a Hilbert symbol in the roots
  outside H, and it is not constant when both quadratic subfields of the
  splitting field are ramified (Example 7.6B). (X₂) is reduced to one explicit
  identity, (7.7), for a κ-weighted fiber integral (Corollary 7.6C). Draft 2
  corrected the fiber form (7.4), and Draft 3 computed the coordinate
  relations (1.22) and the Galois action of §2 exactly; what remains is
  Hales' cocycle t_* [Ha92a, Ch. I] and the integral itself.
- **Open.** A direct proof of (X_r) (for r = 2: the identity (7.7)); the exceptional divisors of a toric
  resolution (one candidate has β = 2); the vanishing of the β = 11/3 term;
  the quadratic and short-reflection S₃ tori; the count of F-classes in the
  subregular class (6 or 8, not 7); whether Hales' product case [Ha89,
  Prop. 2.14] helps for (SL(2)×SL(2))/{±1}. See "Summary of results and open
  problems" in the paper and "Next steps" in `revision_log.md`.

**The original 1994 manuscript** was refereed once (Claude, November 2026),
with the verdict major revision; see `referee/`.

AI review is not an independent certification of the results.

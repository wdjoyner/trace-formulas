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
├── scripts/         exact computations used in the referee report
└── README.md
```

## Contents

| File | What it is |
| --- | --- |
| `original-1994/g2new0.tex` … `g2new9.tex`, `g2newapp.tex`, `g2newref.tex` | The manuscript as written, one AMS-TeX file per section (§0–§9, appendix, references). |
| `original-1994/g2new5d.tex`, `g2new9d.tex` | Variant versions of §5 and §9. It is not known which version is later. |
| `transcription/g2_shalika_germs_transcription.tex`, `.pdf` | All sections in one amsart file, 12pt Times, letter paper, 49 pages. It is literal, as in §6.7 of the style guide: errors are kept, and Claude's notes appear only as `% Claude:` comments. The variant passages and the text that follows `\enddocument` in four source files are kept in `\iffalse` blocks, all of which compile when switched on. |
| `referee/g2_referee_report.tex`, `.pdf` | Referee report by Claude (15 pages): eleven major issues, a table of minor issues and misprints, the results verified as correct, readability, a bibliography check, compliance with the style guide, and notes on the transcription. Every point has a verdict and a verification level (L1–L3). It also serves as the errata log for the transcription. |
| `scripts/g2_toric_divisors.py` | Toric structure of the monomial variety Z of §3: every branch of λ = 0 with its Igusa constants a, b, β, and which patches meet which divisors (about 75 s). |
| `scripts/g2_saturation_full.py` | A complete proof that the semigroup of Z is saturated, so Z is normal for G₂. |
| `scripts/g2_patch_jacobians.py`, `g2_patch_regularity.py` | The patch formulas of §3, the Igusa forms of §4, and the forms (8.1) and (8.4). |
| `scripts/g2_exceptional_divisors.py` | The singular torus orbits of Z and candidate exceptional divisors of a toric resolution. |
| `scripts/g2_tori_endoscopy.py` | H¹(F,T) for every elliptic torus of split G₂, and the root system of the endoscopic group for each κ. |

The scripts need Python 3 with NumPy, SymPy and SciPy. They are named so that
`../run_checks.py` does not run them, because they take longer and need SciPy.
Run them one at a time, for example `python3 g2_tori_endoscopy.py`.

## Status

**The original 1994 manuscript: refereed once (Claude, November 2026).** The
verdict is major revision.

- **Confirmed.** The geometric core is largely right. Z is normal for G₂, the
  essential patches are regular and cover Z up to codimension two (so
  Conjecture 3.4 holds for G₂), and the 1-, 2- and 3-regular base divisors
  have Igusa constants 2, 3 and 4.
- **Not established.** Theorems 6.1, 7.2 and 8.3 are not proved as written.
  - Hales' reduction lemma (5.19) cannot be applied, because the cuspidal
    endoscopic groups of G₂ have trivial connected center.
  - The hypotheses on the support of f can never be satisfied.
  - The roots of the endoscopic PGL(3) are the *short* roots of G₂, not the
    long ones used in §8.
  - The quadratic tori and one class of S₃ tori are missing, although both
    carry nontrivial κ.
  - E_{∅,α,ε} has β = 11/3, not 10/3, and is the same divisor as E_{∅,α,ζ}.
    Exceptional divisors are dismissed without an argument.

## Can it be repaired?

The matchings asserted in Theorems 6.1, 7.2 and 8.3 are true. Local transfer
for p-adic groups is now a theorem: Waldspurger showed that the fundamental
lemma implies transfer, and Ngô proved the fundamental lemma. Gordon and Hales
(Amer. J. Math. 138 (2016)) derive the matching of κ-Shalika germs from
Waldspurger's transfer. What fails is the 1994 proof.

- **Straightforward.**
  - Restate the theorems as germ identities.
  - Correct the PGL(3) roots and the §1–§4 slips (S″, Lemmas 3.5 and 4.4, the
    "regular branch", the patch misprints).
  - Correct the divisor table.
  - State Lemma 3.7 for G₂ (normal by the saturation script, Cohen–Macaulay by
    Hochster's theorem) and leave the general case as a conjecture.
  - Add the quadratic and S₃ tori, which use the same divisors.
- **Mechanical but real work.** Compute an explicit toric resolution of Z (for
  example with Sage's `ToricVariety.resolve()`), then the β and image orbit of
  each exceptional divisor. Show that the β = 11/3 divisor contributes nothing.
- **Hard.** Replace Lemma 5.19 by an explicit computation of how
  κ(t_*)·|ω_{E(u)}| depends on the tangent direction X, as Hales did for SO(4)
  in GSp(4).
  - 2-regular case: looks feasible, since the Galois image lies in W(H₂) and
    the fiber is 4-dimensional.
  - 3-regular case: closer in difficulty to Langlands–Shelstad's A₂.
  - 1-regular case: needs redoing, since the untypeset notes after §6 record an
    unresolved discrepancy.

**Planned route (§6.1 of the style guide).** A corrected edition that keeps
the Igusa approach and fixes everything in the first two groups. It would label
Theorems 6.1, 7.2 and 8.3 conditional on the X-dependence computation, state
the gap precisely in a Remark 2026.n, and note that the matching itself now
follows from Waldspurger and Gordon–Hales. The explicit computation, which
would determine the actual matching constants, can be a separate project.

AI review is not an independent certification of the results.

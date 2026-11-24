# Preservation-first revision — Draft 2

**David Joyner**, *A hitch-hiker's guide to genuine invariant distributions on metaplectic covers of SL(2) over a p-adic field* (manuscript of January 4, 1994).

This directory holds Draft 2 of the preservation-first revision. It starts from the 1994 manuscript and keeps all six of its sections and every one of its statements, in the original order. Statements are numbered consecutively within each section, and `revision_log.md` gives the concordance with the 1994 numbers. It is a separate revision path from the Draft 3 synthesis in the parent directory. Draft 2 has not been refereed. Draft 1 is in the git history.

## Contents

| File | What it is |
|---|---|
| `sl2bar-invariant-distributions-2026.tex` | The manuscript (pdflatex, 12pt Times, US Letter). |
| `sl2bar-invariant-distributions-2026.pdf` | Compiled Draft 2, 60 pages. Built with the mathptmx fallback; see below. |
| `original-1994/` | The 1994 source, unchanged. |
| `revision_log.md` | Changes from Draft 1, corrections to the 1994 text, verification level of every statement, citation checks, concordance, agenda for Draft 3. |
| `conjecture_status.md` | Conjecture-status table, comparison of the three Paley–Wiener theorems, theorem-dependency inventory. |
| `scripts/kubota_cover_check.py` | Exact checks for tame covers over Q_p, eleven pairs (p, n): cocycle, covering torus, Weyl action, n-th power section, Weyl-fixed data, Kubota's splitting, ingredients of the Gindikin–Karpelevich formula. |
| `scripts/wild_torus_check.py` | Wild examples: Q_2 with n = 2, Q_3(ω) with n = 3, Q_2(i) with n = 4. |
| `scripts/spherical_trace_check.py` | Zeros and poles of c(X)c(1/X), Macdonald's formula, the separating functions of Example 5.12. |

## What Draft 2 does

- Determines the center of the covering torus and the dimension of its genuine representations in every residue characteristic, and corrects the wild-case index formula.
- Proves a Gindikin–Karpelevich formula for Kubota's cover directly from the cocycle (tame case). This fixes the endpoint of the complementary series at s = 1/n.
- Turns the five conjectures of Section 3 into theorems for p ∤ n, using Goldberg–Szpruch (Plancherel measures) and Heiermann (rank-one theory for covers). Two of them needed corrected statements. One case stays open: unitary principal series for 4 | n and p = 2.
- Restates the three Paley–Wiener theorems on the irreducible duals, with the compatibility relations at reducible points. Necessity is proved. Surjectivity is proved up to the reducible points for p ∤ 2n, and otherwise rests on Bernstein–Deligne–Kazhdan for covers (as asserted by W.-W. Li) and on Li's tempered Paley–Wiener theorem.
- Adds a status section with a dependency diagram, worked examples (n = 1, 2, 3, 4 and three wild covers), connections to the companion manuscripts, and nine open problems.

## Review status

An AI-assisted working draft. AI use is disclosed in the first sentence of the abstract and in the Acknowledgments. The new proofs are listed in `revision_log.md`, Section 5, and none has been refereed. The literature was consulted through automated extracts of the arXiv versions, so theorem numbers should be rechecked against the published papers, and page numbers are not given. Ten statements carry a "Remark 2026.k" note saying what was not verified.

## Building

```
pdflatex sl2bar-invariant-distributions-2026.tex   # three passes
python3 ../../run_checks.py                        # runs every *_check.py in the repository
```

The preamble uses `newtxtext`/`newtxmath` when installed and falls back to `mathptmx` otherwise. The PDF here was built with the fallback. A rebuild with newtx changes the fonts and may move line breaks.

## License

Text and LaTeX: CC BY 4.0. Scripts: MIT.

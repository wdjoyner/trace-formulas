# Revised paper (2026)

- `local-trace-formula-2026.tex` / `.pdf`: the revised, corrected and expanded version of *Simple local trace formulas for unramified p-adic groups*, Draft 2 (November 12, 2026).
- `../revision_log.md`: the revision log (drafts, AI usage, original vs. new results, sources not consulted, the Draft 2 style-guide pass, numbering concordance, and the former Appendix C).
- `CHANGES.md`: what happened to every item of the errata log in Draft 1, plus a list of the "Remark 2026.n" in the text.
- `referee-report-2.md`, `RESPONSE-TO-REFEREE-2.md`: the second referee report (on the first 2026 draft) and a point-by-point response.

Built from `../original-1997/local-trace-formula-transcription.tex` and the errata log `../original-1997/transcription_log.md`, with the referee report and `../examples/` for context. Numbering follows the 1997 version (see the note on numbering in §1 of the paper).

## Contents

| § | Contents |
|---|---|
| 1 | Introduction, with a road map and a note on numbering |
| — | Literature review: work up to 1997, work since 1997 |
| 2 | Notation and background. §2.0 Conventions; corrected Macdonald formula; Example 2.5 ((G,A)-families in rank one) |
| 3 | Matrix coefficients; Casselman input (C); Brion's theorem for half-open polytopes (3.5B), positivity (3.5C), vertex decomposition (3.5A); Proposition 3.6 |
| 4 | Truncated kernel (Prop. 4.2); Theorem 4.5 (a) unconditional, (b) under (C) and (R); Conjecture 4.6 |
| 5 | κ-orbital integrals on SL(n) and the fundamental lemma (Props. 5.1–5.2) |
| 6 | Worked examples: PGL(2) (Theorem 6.1, Lemma 6.1A: (R) holds) and SL(2) (Prop. 6.4, an atom) |
| 7 | Route B: the identity from Arthur's local trace formula (sketch) |
| 8 | Summary of results (status table) and open questions |
| A | PGL(3): a rank-two test of Hypothesis (R) |
| — | Glossary, Acknowledgments, References |

## Main correction to the 1997 claim

For SL(2), the spectral measure of an unramified elliptic orbital integral has a **point mass** at the unramified quadratic character χ₀. There the Plancherel density does not vanish, and the R-group has order 2:

    O_γ(f) = ∫ f^∨ I(χ,γ) dμ + ½ f^∨(χ₀).

So "I(χ,γ) is a rational function" holds for PGL(2) but not in general. See §6.2, Conjecture 4.6 and `../examples/sl2/`.

Build with `pdflatex local-trace-formula-2026.tex` (run it twice for the table of contents).

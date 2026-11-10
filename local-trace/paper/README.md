# Revised paper (2026)

- `local-trace-formula-2026.tex` / `.pdf`: the revised, corrected and updated version of *Simple local trace formulas for unramified p-adic groups*.
- `CHANGES.md`: what happened to every item of the errata log, plus a list of the dated "Remark 2026.n" in the text.

Built from `../original-1997/local-trace-formula-transcription.tex` and the errata log `../original-1997/transcription_log.md`, with the referee report and `../examples/` for context. Numbering follows the 1997 version.

## Contents

| § | Contents |
|---|---|
| — | About this revision: history, what changed, status table |
| 1 | Introduction, with a road map |
| 2 | Notation and background. New §2.0 Conventions; corrected Macdonald formula |
| 3 | Matrix coefficients; Brion vertex decomposition (Lemma 3.5A); Proposition 3.6 (new proof) |
| 4 | Truncated kernel (Prop. 4.2); Theorem 4.5 (a) unconditional, (b) under Hypothesis (R); Conjecture 4.6 |
| 5 | κ-orbital integrals on SL(n) and the fundamental lemma (Props. 5.1–5.2) |
| 6 | Worked examples: PGL(2) (Theorem 6.1) and SL(2) (Prop. 6.4, an atom) |
| 7 | Route B: the identity from Arthur's local trace formula (sketch) |
| 8 | Literature review, before and after 1997 |
| A, B | Glossary; concordance with the 1997 numbering |

## Main correction to the 1997 claim

For SL(2), the spectral measure of an unramified elliptic orbital integral has a **point mass** at the unramified quadratic character χ₀. There the Plancherel density does not vanish, and the R-group has order 2:

    O_γ(f) = ∫ f^∨ I(χ,γ) dμ + ½ f^∨(χ₀).

So "I(χ,γ) is a rational function" holds for PGL(2) but not in general. See §6.2, Conjecture 4.6 and `../examples/sl2/`.

Build with `pdflatex local-trace-formula-2026.tex` (run it twice for the table of contents).

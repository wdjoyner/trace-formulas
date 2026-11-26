# finite-trace

Trace formulas for finite groups: the "global" (Selberg-type) and "local" (Arthur-type) identities in the setting where everything is an exact finite sum. This is meant as an entry point to the p-adic case in [`../local-trace/`](../local-trace/).

## Summary

For a finite group G and a subgroup Γ, the trace of a convolution operator on the permutation representation ℂ[Γ\G] can be computed in two ways: geometrically, as a sum over conjugacy classes of orbital sums, and spectrally, as a sum over irreducible representations of their multiplicities times their characters. This elementary identity is a model of the Selberg trace formula for a compact quotient. The analogous bilinear identity on ℂ[G] is a finite model of the compact case of Arthur's local trace formula, and it follows from the first identity applied to the pair (G×G, ΔG), with ΔG the diagonal subgroup.

The 2026 version fixes the counting-measure conventions, gives proofs and worked examples for S₃ and A₅, and explains how far the finite analogy goes. A new section computes an explicit divergence for GL(2) over a p-adic field, to show why the noncompact local formula needs truncation, Levi subgroups and weighted distributions. It also relates the finite formulas to Arthur's finite example, Vignéras's regular-bimodule method, Yang's coset-space formulas and Terras's finite spectral analogues.

## Files

| File | What it is | Status |
|---|---|---|
| `finitegp-tr-formula_2003.tex` / `.pdf` | D. Joyner, *Notes on trace formulas for finite groups*. Written in summer 1996 while visiting Stanford, with details added in 1997, 2000 and 2003. Unpublished. Dated 3-3-2003. | Original, as written |
| `finite-group-trace-formulas_2026.tex` / `.pdf` | D. Joyner, *Finite-Group Trace Formulas: Compact Global and Local Analogies, and a p-Adic Bridge*. Corrected and expanded version of the 1996–2003 notes, revised in November 2026 with mathematical and editorial help from ChatGPT (OpenAI). Adds a p-adic bridge section, a literature review, a glossary, exercises, and a summary of corrections. | Refereeing of the 2026 corrections pending |

Both files compile with `pdflatex` (or `latexmk -pdf`); the compiled PDFs are committed alongside the sources.

Planned: explicit examples (e.g. GL(2, F_q)) with verification scripts, in the same style as [`../local-trace/examples/pgl2/`](../local-trace/examples/pgl2/).

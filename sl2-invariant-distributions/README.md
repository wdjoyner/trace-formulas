# A hitch-hiker's guide to invariant distributions on SL(2) over a p-adic field

Expository notes by David Joyner on invariant distributions on
G = SL(2, F), F a non-archimedean local field of odd residue
characteristic. Original notes dated November 2, 1994; revised and
corrected with AI assistance in November 2026.

This is the ordinary-group companion to the metaplectic material in
`../sl2bar-characters/` and `../sl2bar-trace/`.

## Layout

```
sl2-invariant-distributions/
├── original-1994/   the 1994 notes and their Argon–Gemini revision, as received
├── revised/         2026 revised drafts and referee reports
├── research/        research reports written before material is integrated
├── revision_log.md   every change, stage by stage, and the AI usage
└── README.md
```

## Contents

| File | What it is |
| --- | --- |
| `revised/sl2-invariant-distributions-2026.tex`, `.pdf` | The main file of Draft 4 (November 24, 2026). It inputs six module files (see below). See the latest PDF build status in GitHub Actions. |
| `revised/referee-report_draft3-main-file.md` | Referee report by ChatGPT on the main file of Draft 3. The five module files were not part of that review. Recommendation: further revision. Draft 4 is the response. |
| `revised/referee-report_argon-gemini-revision.md` | Referee report by ChatGPT on the Argon–Gemini revision of the 1994 notes. Verdict: major revision. Draft 1 is the response to it. |
| `research/section9-supertempered-research-report.tex`, `.pdf` | Research report by Claude (November 24, 2026) on which Section 9 is based. Its statement numbers differ from the paper's. `research/section9-tree-checks.py` reruns the exact checks of the tree computations. |
| `revision_log.md` | Stages, AI usage, original and new results, every change by draft, the item-by-item response to the Draft 3 referee report, the new text that still needs refereeing, citation checks, and the concordances. |
| `original-1994/hitchhiker-sl2-repns.tex` | The 1994 notes as written (LaTeX 2.09), unchanged. |
| `original-1994/hitchhikers-guide-to-invariant-distributions-on-sl2-over-p-adic-field2.tex` | The Argon–Gemini LaTeX revision of the 1994 notes: the version the referee reviewed and Draft 1 was rewritten from. |

## Status

- **Draft 1** (ChatGPT, November 2026) is an expository rewrite responding to the referee report. It restricts itself to a survey of established theory. Its main changes: the trace map on the cocenter replaces the asserted bijection onto a Paley–Wiener space; the reducibility criterion includes `|.|^{±1}`; a counterexample shows normalized orbital integrals need not vanish at singular elements; the trace Paley–Wiener theorem is stated in Grothendieck-group form; a Laurent-coefficient criterion for analytic functionals is proved; weak constant terms are distinguished from elliptic support.
- **Draft 2** (Claude, November 12, 2026) is a style-guide pass with no mathematical changes: title page, AI disclosure, a literature review split at 1994, orienting paragraphs, six unnumbered examples, the glossary moved before the new Acknowledgments, and the revision record moved to `revision_log.md`. No theorem or equation number changed.
- Three topics from the 1994 notes are not claimed and remain open: an explicit Schwartz-space trace Paley–Wiener theorem, an admissibility-preserving descent theorem, and a global analyticity criterion for invariant distributions.
- **Not yet done:** an independent referee report on Draft 1 (the referee and the reviser were the same system), and refereeing of the text added in Draft 2, which is listed in `revision_log.md`.

## Draft 4

**Draft 4** (Claude, November 24, 2026) responds to ChatGPT's referee report on the main file of Draft 3. It is a consolidation draft with no new research section. Main changes: a proof that the commutator subspace equals the span of conjugation differences; a proposition that every linear functional on the Hecke algebra is continuous, so that invariant distributions are the full algebraic dual of the trace image; the topologies of the Hecke algebra and the Schwartz space made explicit; a theorem comparing the three spectral duals (polynomial, holomorphic, smooth); the Jacobian computation for the orbital integral of 1_K; a remark separating global, fixed-level and Schwartz realization of trace forms; an introduction with a roadmap and a list of principal results; a running example over Q_3; an expanded glossary; a sorted and partly verified bibliography. The bilateral Laurent criterion moved from the end of Section 7 to its beginning (new module `laurent-criterion.tex`). Claude also read the four modules written by ChatGPT for correctness and found no error. The item-by-item response, the concordance of numbers, and what remains unverified are in `revision_log.md`.

## Draft 3 development

The main source inputs these modules. The sixth, [laurent-criterion.tex](revised/laurent-criterion.tex), was split off in Draft 4 and is input by `spectral-duality.tex`:

- [spectral-geometry.tex](revised/spectral-geometry.tex): Section 3, including all four original TikZ figures.
- [trace-pw-comparison.tex](revised/trace-pw-comparison.tex): Section 5, including six TikZ diagrams.
- [spectral-duality.tex](revised/spectral-duality.tex): Sections 6–7, including five TikZ diagrams, continuous duals, Laurent growth, reducibility, central recurrences and corrected central-finiteness criterion.

- [admissible-distributions.tex](revised/admissible-distributions.tex): Section 8, including five TikZ diagrams, local finite-character interpolation, conditional finite-block admissibility and exact unramified split-descent criterion, corrected quasi-finite spectral definitions, and the original GL(2) question.
- [supertempered-distributions.tex](revised/supertempered-distributions.tex): Section 9 (Claude), including six TikZ figures: the six notions around supertemperedness, constant terms, a rank-one proof of Herb's classification, the quadratic constituents and a tree formula, the elliptic quotient and its two splittings, weak constant terms of distributions, behavior at ±I and a general split descent criterion, the Bernstein center and Hecke-finiteness, Euler–Poincaré pairings, examples over Q_3 and Q_5, and a global characterization. It assumes characteristic zero. Its classical inputs are listed in its last subsection and in `revision_log.md`, and most still need a source audit.

Draft 3 was an integrated working draft using the corrected Draft 2 text as an interim editorial scaffold. The original 1994 manuscript remains unchanged and authoritative for the outstanding restoration and theorem concordance. The full recovery of its mathematical content is not yet completed. The combined source has not been independently refereed. A scoped GitHub Actions workflow builds the combined PDF on changes to the revised LaTeX sources, using the same pattern as the adjoint-lift project. The PDF should be checked against the latest successful build. Global Schwartz topology, closed commutator identification, descent and group-side analyticity remain verification tasks.

## Building

`pdflatex sl2-invariant-distributions-2026.tex` (three passes) in `revised/`. The bibliography is inline, so no BibTeX run is needed. The paper uses the `newtx` fonts (`newtxtext`, `newtxmath`). The PDF is built by the scoped GitHub Actions workflow; a local build requires all six input files.

## License

Text and LaTeX sources: CC BY 4.0 (see the top-level [LICENSE](../LICENSE)).

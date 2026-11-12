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
├── revision_log.md   every change, stage by stage, and the AI usage
└── README.md
```

## Contents

| File | What it is |
| --- | --- |
| `revised/sl2-invariant-distributions-2026.tex`, `.pdf` | The revised paper, currently Draft 2 (November 12, 2026). File names carry no draft number, and git history tracks the drafts. `amsart`, 14 pages. |
| `revised/referee-report_argon-gemini-revision.md` | Referee report by ChatGPT on the Argon–Gemini revision of the 1994 notes. Verdict: major revision. Draft 1 is the response to it. |
| `revision_log.md` | Stages, AI usage, original and new results, every Draft 2 change, the new text that still needs refereeing, citation checks, and the concordance. |
| `original-1994/hitchhiker-sl2-repns.tex` | The 1994 notes as written (LaTeX 2.09), unchanged. |
| `original-1994/hitchhikers-guide-to-invariant-distributions-on-sl2-over-p-adic-field2.tex` | The Argon–Gemini LaTeX revision of the 1994 notes: the version the referee reviewed and Draft 1 was rewritten from. |

## Status

- **Draft 1** (ChatGPT, November 2026) is an expository rewrite responding to the referee report. It restricts itself to a survey of established theory. Its main changes: the trace map on the cocenter replaces the asserted bijection onto a Paley–Wiener space; the reducibility criterion includes `|.|^{±1}`; a counterexample shows normalized orbital integrals need not vanish at singular elements; the trace Paley–Wiener theorem is stated in Grothendieck-group form; a Laurent-coefficient criterion for analytic functionals is proved; weak constant terms are distinguished from elliptic support.
- **Draft 2** (Claude, November 12, 2026) is a style-guide pass with no mathematical changes: title page, AI disclosure, a literature review split at 1994, orienting paragraphs, six unnumbered examples, the glossary moved before the new Acknowledgments, and the revision record moved to `revision_log.md`. No theorem or equation number changed.
- Three topics from the 1994 notes are not claimed and remain open: an explicit Schwartz-space trace Paley–Wiener theorem, an admissibility-preserving descent theorem, and a global analyticity criterion for invariant distributions.
- **Not yet done:** an independent referee report on Draft 1 (the referee and the reviser were the same system), and refereeing of the text added in Draft 2, which is listed in `revision_log.md`.

## Building

`pdflatex sl2-invariant-distributions-2026.tex` (three passes) in `revised/`. The bibliography is inline, so no BibTeX run is needed. The paper uses the `newtx` fonts (`newtxtext`, `newtxmath`). The compiled PDF is committed beside the source.

## License

Text and LaTeX sources: CC BY 4.0 (see the top-level [LICENSE](../LICENSE)).

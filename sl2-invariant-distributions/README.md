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
└── README.md
```

## Contents

| File | What it is |
| --- | --- |
| `revised/sl2-invariant-distributions-revised-draft1.tex` | Draft 1 (November 2026): AI-assisted expository rewrite prepared with ChatGPT, responding to the referee report below. `amsart`, about 12 pages. |
| `revised/referee-report_argon-gemini-revision.md` | Referee report on the earlier Argon–Gemini LaTeX revision of the 1994 notes. Verdict: major revision. Draft 1 is the response to it. |
| `original-1994/hitchhiker-sl2-repns.tex` | The 1994 notes as written (LaTeX 2.09), unchanged. |
| `original-1994/hitchhikers-guide-to-invariant-distributions-on-sl2-over-p-adic-field2.tex` | The Argon–Gemini LaTeX revision of the 1994 notes: the version the referee reviewed and Draft 1 was rewritten from. |

## Status

Draft 1 restricts itself to an expository survey of established theory.
Its main changes relative to the refereed version:

- the asserted bijection from the Hecke algebra to a Paley–Wiener space is
  replaced by the trace map on the invariant quotient (cocenter);
- the principal-series reducibility criterion includes the points
  `|.|^{±1}` as well as the nontrivial quadratic characters;
- a counterexample shows normalized orbital integrals need not vanish at
  singular elements;
- the trace Paley–Wiener theorem is stated in its Grothendieck-group
  (Bernstein–Deligne–Kazhdan) form;
- a Laurent-coefficient criterion for analytic functionals is proved;
- weak constant terms are distinguished from elliptic support in the
  section on supertempered virtual characters.

Three topics from the 1994 notes are explicitly not claimed in Draft 1
and remain open for a later draft:

1. an explicit Schwartz-space trace Paley–Wiener theorem;
2. an admissibility-preserving descent theorem;
3. a global analyticity criterion for invariant distributions.

Draft 1 has not yet been independently refereed.

## Building

`pdflatex sl2-invariant-distributions-revised-draft1.tex` (twice) in
`revised/`. The bibliography is inline, so no BibTeX run is needed. The
draft uses the `newtx` fonts (`newtxtext`, `newtxmath`). The compiled PDF
has not been committed yet.

## License

Text and LaTeX sources: CC BY 4.0 (see the top-level [LICENSE](../LICENSE)).

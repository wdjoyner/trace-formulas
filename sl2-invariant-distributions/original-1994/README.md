# original-1994

The pre-revision sources of *A hitch-hiker's guide to invariant
distributions on SL(2) over a p-adic field* (D. Joyner), kept as received.

| File | What it is |
|---|---|
| `hitchhiker-sl2-repns.tex` | The 1994 notes, dated 11-2-94. LaTeX 2.09 (`\documentstyle`, Scientific Word header); nine sections and a bibliography. No changes. |
| `hitchhikers-guide-to-invariant-distributions-on-sl2-over-p-adic-field2.tex` | The Argon–Gemini LaTeX revision of the 1994 notes ("November 2, 1994 (Revised)"). Same nine sections, with typographical cleanup, `\cite` citations, and some mathematical edits. This is the version the referee report in `../revised/` reviewed, and the one Draft 1 was rewritten from. |

## Building

- `hitchhiker-sl2-repns.tex` uses `\documentstyle[amsfonts,12pt]{article}`
  and needs LaTeX 2.09 compatibility mode.
- The Argon–Gemini revision loads `fontspec` and `babel` with `bidi=basic`,
  so it needs LuaLaTeX (XeLaTeX fails), and the Noto Sans font.

Neither file has been test-compiled in this repository, and no PDFs are
committed.

## Caution

Both files contain the statements that the referee report identifies as
incorrect (the bijection onto the Paley–Wiener space, the reducibility
criterion, the image of the orbital-integral map, the descent lemma, the
elliptic-support claim for supertempered distributions, among others).
They are here as a record. For mathematics, use `../revised/`.

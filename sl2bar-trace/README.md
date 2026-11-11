# sl2bar-trace

*A hitch-hiker's guide to the metaplectic trace formula for SL(2): basic theory*, by David Joyner (1-27-95, slightly revised 6-2002), and its 2026 revision.

The paper works out Arthur's trace formula, in non-invariant and then invariant form, for the metaplectic cover of G = Res_{k/Q} SL(2). It then sketches a partial stabilization along the lines of Labesse–Langlands, using GL(2)-conjugation as stable conjugacy. The 1995 notes treat the n-fold Kubota cover. **The 2026 revision restricts to the 2-fold cover (n = 2).**

## Layout

| Path | Contents |
|---|---|
| `original-1995/` | The notes as received: `cctrace_new.tex` (LaTeX2e master), `cctrace1.tex` (older Scientific Word master), `cctrace2.tex`–`cctrace7.tex`, `cctracer.tex` (bibliography). The file `cctrac3b.tex` that the master inputs was not among these files; it is `book-1997/book7d.tex`, and its content is now part of `revised/sec4-geometric.tex`. |
| `book-1997/` | Chapters of the 1997 book manuscript *An application of Arthur's invariant trace formula for SL(2)* (Scientific Word; needs `tcilatex`). Chapter 9 (`book7a`–`book7h`) is the source of the notes. |
| `revision_log.md` | Every referee item, with its location, the planned fix, the revision stage, and its status |
| `revised/` | The 2026 revision (n = 2), section by section: `sec2-foundations.tex` (stage 1), `sec3-rank0.tex` (stage 2), `sec4-geometric.tex` (stage 3), `sec5-spectral.tex` (stage 4), the standalone build `preview.tex`/`.pdf`, and `checks/` (verification scripts) |

The notes correspond to Chapter 9 of the book file by file:

| Notes | Book | Contents |
|---|---|---|
| `cctrace_new.tex` (intro) | `book7a.tex` | Introduction |
| `cctrace2.tex` | `book7b.tex` | Rank 0 case |
| `cctrace3.tex` | `book7c.tex` | Kernel, reduction theory, truncation |
| `cctrac3b.tex` (missing) | `book7d.tex` | Basic properties, equivalence relation, J_M(u,f), fine geometric expansion |
| `cctrace4.tex` | `book7e.tex` | Spectral decomposition, Eisenstein series |
| `cctrace5.tex` | `book7f.tex` | Integrability of k_χ^T, the trace formula |
| `cctrace6.tex` | `book7g.tex`, `book7gnw.tex` (later) | Invariant form |
| `cctrace7.tex` | `book7h.tex` | Stable(r) form |

## Status (November 2026)

- Referee report (2026): [Claude Docs](https://claude.ai/artifact/7MmqhX7GnoJNup9xbb9RNG). Its items are tracked in `revision_log.md`.
- Revision: in stages (see `revision_log.md`). Stages 1–4 (Section 2, foundations of the double cover; Section 3, the rank-0 case; Section 4, the geometric side, which also replaces the missing `cctrac3b.tex`; Section 5, the spectral side, now with the residual Weil representations and the ramified classes) are drafted in `revised/` and checked by the scripts in `revised/checks/`. Stage 0 (a clean, compiling source tree with no mathematical changes) is still to do; it will `\input` the revised sections.

## Building

`original-1995/cctrace_new.tex` builds with `pdflatex` once a `cctrac3b.tex` is supplied. With an empty stub, it compiles. The book files need Scientific Word's `tcilatex` and do not build with a standard TeX installation.

## License

Text and LaTeX sources: CC BY 4.0 (see the top-level [LICENSE](../LICENSE)).

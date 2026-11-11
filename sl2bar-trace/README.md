# sl2bar-trace

*A hitch-hiker's guide to the metaplectic trace formula for SL(2): basic theory*, by David Joyner (1-27-95, slightly revised 6-2002), and its 2026 revision.

The paper works out Arthur's trace formula, in non-invariant and then invariant form, for the metaplectic cover of G = Res_{k/Q} SL(2). It then sketches a partial stabilization along the lines of Labesse–Langlands, using GL(2)-conjugation as stable conjugacy. The 1995 notes treat the n-fold Kubota cover. **The 2026 revision restricts to the 2-fold cover (n = 2).**

## Layout

| Path | Contents |
|---|---|
| `original-1995/` | The notes as received: `cctrace_new.tex` (LaTeX2e master), `cctrace1.tex` (older Scientific Word master), `cctrace2.tex`–`cctrace7.tex`, `cctracer.tex` (bibliography). The file `cctrac3b.tex` that the master inputs was not among these files; it is `book-1997/book7d.tex`, and its content is now part of `revised/sec4-geometric.tex`. |
| `book-1997/` | Chapters of the 1997 book manuscript *An application of Arthur's invariant trace formula for SL(2)* (Scientific Word; needs `tcilatex`). Chapter 9 (`book7a`–`book7h`) is the source of the notes. |
| `revision_log.md` | Every referee item, with its location, the planned fix, the revision stage, and its status |
| `referee-2026-11/` | The second referee report (ChatGPT) and the authors' response |
| `revised/` | The 2026 revision (n = 2), section by section: `sec1-introduction.tex` (overview, literature review), `appA-comparison.tex`, `glossary.tex`, `sec2-foundations.tex` (stage 1), `sec3-rank0.tex` (stage 2), `sec4-geometric.tex` (stage 3), `sec5-spectral.tex` (stage 4), `sec6-invariant.tex` (stage 5), `sec7-stable.tex` (stage 6), the standalone build `preview.tex`/`.pdf`, and `checks/` (verification scripts) |

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
- Second referee report (ChatGPT, 2026-11-11) and the response: [`referee-2026-11/`](referee-2026-11/). The revised draft has authors D. Joyner and Claude, a new Section 1 (overview and literature review), a glossary, and an appendix collecting the comparisons with the 1995 notes.
- Revision: in stages (see `revision_log.md`). Stages 1–6 (Section 2, foundations of the double cover; Section 3, the rank-0 case; Section 4, the geometric side, which also replaces the missing `cctrac3b.tex`; Section 5, the spectral side, now with the residual Weil representations and the ramified classes; Section 6, the invariant form, proved directly for this group; Section 7, the stable(r) form) are drafted in `revised/` and checked by the scripts in `revised/checks/`. Stage 7 (a consistency pass, and a second reading of Section 7) is done; its notes in `revision_log.md` list the corrections it made to Section 7 and what is still open. Section 7 has not had an independent referee report. Stage 0 (a clean, compiling 1995 source tree with no mathematical changes) was never done and is largely superseded: `revised/preview.tex` builds the whole revised paper.
- Section 7 (stage 6) does not follow the 1995 section. Conjugation by GL(2) can exchange the two lifts of an element of the cover, so it is not stable conjugacy; stable conjugacy (Adams, Li) is conjugation by GL(2) twisted by the sign (det h, det(1+γ)). With it the regular elliptic terms are S_ell(f) + S_ell(f₋), where f₋ is f translated by the central element −1. The unipotent coefficients a^G(S,u_ξ), left open in Section 4, are computed. The hyperbolic and unipotent terms and the cuspidal spectrum are not stabilized (that is Li's theorem), and the section says what is missing. The statements about the weighted terms assume a condition (N5) on the local normalizing factors, which holds for the explicit factors and is a hypothesis at the dyadic and ramified places.

## Building

`original-1995/cctrace_new.tex` builds with `pdflatex` once a `cctrac3b.tex` is supplied. With an empty stub, it compiles. The book files need Scientific Word's `tcilatex` and do not build with a standard TeX installation.

## License

Text and LaTeX sources: CC BY 4.0 (see the top-level [LICENSE](../LICENSE)).

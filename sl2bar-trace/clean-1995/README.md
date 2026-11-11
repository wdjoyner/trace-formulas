# sl2bar-trace/clean-1995

Stage 0 of [`../revision_log.md`](../revision_log.md): the 1995 notes as a tree that compiles with a standard TeX installation. **No mathematical changes.** It is the reference for the "1995 (compiled)" statement numbers used in the revision log and in Appendix A of the revised paper. The revised paper itself is in [`../revised/`](../revised/).

Build: `pdflatex cctrace_new.tex` (three runs). 81 pages, no errors, no undefined citations.

## What differs from `../original-1995/`

| File | Change |
|---|---|
| `cctrac3b.tex` | New here: a copy of `../book-1997/book7d.tex`. The master inputs this file, and it was missing from the notes as received. One Scientific Word artifact, `\symbol{126}`, is replaced by `\sim` |
| all files | `\Bbb` → `\mathbb` (845 times), `\frak` → `\mathfrak` (108 times); the obsolete forms gave warnings |
| `cctrace_new.tex` | The unused class option `amsfonts` is removed. Equations are numbered by section, (2.1), (2.2), …, as in the Scientific Word original; as received, they compile as (1)–(127) while the text refers to them as (4.5), (7.14), … |
| `cctracer.tex` | The duplicate entry `[Sh]` is removed |
| `cctrace1.tex` | Not copied: it is the older Scientific Word master and needs `tcilatex` |

## What stage 0 does not do

- **Cross-references are still typed by hand.** The 1995 text has no `\label` or `\ref`. Its references ("Proposition 4.18", "(7.14)", "section 2.7") are the numbers of the Scientific Word version and do not all agree with the compiled numbers; for example Section 7 compiles with equations (7.1)–(7.30). Converting them was part of the original plan for stage 0. It was dropped: every section has since been rewritten in `../revised/`, which uses `\label` and `\ref` throughout, and the stage notes in the revision log map the 1995 statements to the new ones.
- **The bibliography is not corrected** beyond the duplicate. The corrected entries are in the bibliography of the revised paper.
- With `cctrac3b.tex` present, Section 4 has seven more numbered statements at its end (4.10–4.16) than in a build with an empty stub. Sections 5–7 are numbered the same either way.

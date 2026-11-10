# Changes in the 2026 revision

The working sources are `sl2bar-trace.tex` (master) and the section files it inputs. `../original-1995/` keeps the notes as received.

| Notes file | Revision file | Section |
|---|---|---|
| `cctrace_new.tex` | `sl2bar-trace.tex` | 1–2 (introduction, background on the cover) |
| `cctrace2.tex` | `sec2.tex` | 3 (rank 0) |
| `cctrace3.tex` | `sec3.tex` | 4.1–4.2 (kernel, truncation) |
| `cctrac3b.tex` (missing; from `book7d.tex`) | `sec3b.tex` | 4.3–4.6 (basic properties, equivalence relation, J_M(u,f), fine expansion) |
| `cctrace4.tex` | `sec4.tex` | 5.1–5.2 (spectral decomposition, Eisenstein series) |
| `cctrace5.tex` | `sec5.tex` | 5.3–5.4 (integrability of k_χ^T, the trace formula) |
| `cctrace6.tex` | `sec6.tex` | 6 (invariant form) |
| `cctrace7.tex` | `sec7.tex` | 7–8 (stable(r) form, food for thought) |
| `cctracer.tex` | `refs.tex` | References |

Section, theorem and equation numbers below are those of the compiled revision.

## Stage 0 (2026-11-10): clean source tree, no mathematical changes

- **Missing file.** `sec3b.tex` is `book7d.tex` from the 1997 book. Its references to the book ("chapter 2", "chapter 6", "section 9.4", "Example 275", "(9.19)") were redirected to the article. The book's citation of its Chapter 6 (local Schwartz space) now cites [J1], with a comment.
- **Preamble.** Dropped `amsgen`, `makeidx`/`\printindex` (no index entries), the class option `amsfonts` and the `\def\qed` override. Added `amsmath`, `hyperref` and `\numberwithin{equation}{section}`.
- **Scientific Word macros.** `\Bbb`, `\frak`, `\cal` became `\mathbb`, `\mathfrak`, `\mathcal`. Fixed `\frak{)}` (§2.1.3), `{\cal \chi}` (§6.2) and `\symbol{126}` (§4.6).
- **Labels and cross-references.** Every theorem-like environment and numbered equation now has a label named after its stage-0 number (`lem:2.3`, `eq:6.12`, …), and the sections cited in the text have labels (`sec:invariant`, `sssec:normint`, …). All hard-coded internal references (about 140) were replaced by `\ref`/`\eqref`. Most of them were stale, left over from the numbering of the book or of earlier drafts. Each target was chosen by reading the context; the less obvious choices:
  - §4.1, proof of Lemma 4.4: "the upper bound (1.10)" → (4.5); "This verifies (1.12)" → (4.7).
  - §5 intro: "(4.5), Proposition 4.14 … Theorem 6.15 … 4.1.1" → (5.4), Proposition 5.7, Theorem 5.8, §5.1.1 (matches the book's wording).
  - §5.3: "(see (7.21) below)" → Theorem 5.27 (the book has "Theorem 302").
  - §5.3: "a corollary of the proof of lemma 6.9" → Langlands' combinatorial lemma [A3]; "by lemma 4.7" → (2.5). Both marked with comments.
  - §6.1: "(6.1)–(6.6)" and "(6.1)–(6.4)" are Arthur's [A6, (7.1)–(7.6)] and [A6, (7.1)–(7.4)] (as in the book).
  - §6.1: "Recall (4.14), (5.16)" → (2.4), (2.5); "subsection 5.1.1" and "subsection 4.????" → §4.3.1.
  - §6.1.1: "the terms (6.17), (5.27) (… Example 5.23)" → the term (5.28) and Example 5.28 (matches the book).
  - §6.3: "The analog of Proposition 4.16 is" → "We have", with a comment: the target is unclear (the book has "Proposition 320").
  - §7.5, proof of Lemma 7.11: "Proposition 6.20" → Proposition 6.17 ([A10, Thm 3.3]); "Proposition 4.19, Example 4.14" → Proposition 4.15, Example 4.16.
  - §7.5: "By Proposition 6.19" → Proposition 4.15 (the book has "Proposition 279", the fine expansion).
  - §7.7: "Lemma 7.7 and 7.17" → Lemmas 7.9 and 7.23.
  - §8: "(7.12,17)" → (6.19), (6.23) (the inductive definitions of I_M(γ) and I_M(π)).
- **Citations.** Every `[A2]`-style citation is now `\cite` (`[A2, p. 949]` → `\cite[p. 949]{A2}`, `[L1-2]` → `\cite{L1,L2}`, `[A2]-[A15]` → `\cite{A2}--\cite{A15}`).
- **Bibliography.** Corrected [KP] (1984), [LL] (31 (1979) 726–785), [J2] (title, 61 (1988)), [Fl] (57 (1980) 119–182), [GeKn] (A. W. Knapp), [PR] (Raghunathan), [L4] (Ann. Math. Studies 96), [MW] (Ann. Sci. ÉNS 22 (1989)). [A13], [A14], [A16] now cite their published versions. Removed the duplicate [Sh]. Added the cited but missing [M] (Moore), [Se] (Serre), [Ko1] (Kottwitz). Li I–IV are added in a later stage.
- **One typo fixed in the introduction.** The commented-out line "%\overline{G(\aaa)}$ on the space …" is restored and "cups forms" is now "cusp forms".

The revision compiles with `pdflatex` (two passes) with no errors and no undefined references.

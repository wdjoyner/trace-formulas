# trace-formulas

Trace formulas — local (p-adic), finite-group, and related — written up in LaTeX, with every explicit formula backed by a short script that checks it.

Maintained by David Joyner. Parts of this repository were prepared with the help of Claude (Anthropic); this is noted in each document where it applies.

## Contents

| Directory | What it is | Status |
|---|---|---|
| [`local-trace/`](local-trace/) | *Simple local trace formulas for unramified p-adic groups* (D. Joyner; Pacific J. Math. 154 (1992) 103–129; corrected version 1997) and its 2026 revision | Revision in progress |
| [`local-trace/original-1997/`](local-trace/original-1997/) | The 1997 version: scan, literal LaTeX transcription, errata log, referee report | Complete |
| [`local-trace/examples/pgl2/`](local-trace/examples/pgl2/) | Worked example for PGL(2): closed forms for the spectral distribution I(χ,γ) for every elliptic type, verified on the Bruhat–Tits tree | Complete, verified (q = 3) |
| [`local-trace/examples/sl2/`](local-trace/examples/sl2/) | SL(2) check: the spectral measure has an atom at the quadratic unramified character | Complete, verified (q = 3) |
| [`local-trace/examples/rank2/`](local-trace/examples/rank2/) | Exact check of the Brion vertex decomposition (Lemma 3.5A) for SL(3) and PGL(3) | Complete |
| [`local-trace/examples/pgl3/`](local-trace/examples/pgl3/) | PGL(3) on the Bruhat–Tits building: closed form for I(χ,γ) (γ of depth 0), the spectral identity with no singular part, and Hypothesis (R) failing | Complete, verified (q = 2, 3) |
| [`local-trace/paper/`](local-trace/paper/) | The revised, corrected and updated paper (PGL(2)/SL(2) examples, PGL(3) appendix, Route B sketch, glossary, literature review before/after 1997) | First complete draft (Nov. 2026) |
| [`local-trace/arthur/`](local-trace/arthur/) | Short guide: deriving the main identity from Arthur's local trace formula ("Route B") | Companion paper, Draft 5 (Nov. 2026): a working draft, normalizations not yet checked |
| [`sl2bar-trace/`](sl2bar-trace/) | *A hitch-hiker's guide to the metaplectic trace formula for SL(2)* (D. Joyner, 1995/2002) with chapters of the 1997 book manuscript, and its 2026 revision for the 2-fold cover | Revision in progress: Sections 1–7 (introduction, foundations, rank 0, geometric side, spectral side, invariant form, stable(r) form) drafted and checked |
| [`sl2bar-characters/`](sl2bar-characters/) | *Two-orbit unramified elliptic character relations for depth-zero representations of metaplectic covers of SL(2)*: odd-degree tame covers (not the 2-fold cover of `sl2bar-trace/`), reconstructed in 2026 from unfinished notes of about 2000 | Working draft 5 (Nov. 2026); refereed once, pinpoint citations still to be checked |
| [`sl2-invariant-distributions/`](sl2-invariant-distributions/) | *A hitch-hiker's guide to invariant distributions on SL(2) over a p-adic field* (D. Joyner, notes of 1994): the ordinary-group companion to the two metaplectic directories, with the 1994 source, its Argon–Gemini revision, the referee report on that revision, and the 2026 expository rewrite | Draft 2 (Nov. 2026): ChatGPT's rewrite with a style-guide pass by Claude; not independently refereed (see its `revision_log.md`) |
| [`finite-trace/`](finite-trace/) | Trace formulas for finite groups: the 1996–2003 notes and their 2026 corrected and expanded version | Notes posted; refereeing of the 2026 corrections pending |
| [`common/`](common/) | Shared notation, glossary and bibliography | Started |

## What is proved, what is checked, what is open

The 1997 paper contains errors and two genuine gaps; see the [referee report](local-trace/original-1997/referee_report_ltf.pdf) and the [errata log](local-trace/original-1997/transcription_log.md). Current state:

- **Proved and numerically verified:** the main identity for G = PGL(2), with explicit I(χ,γ) for all elliptic γ ([worked example](local-trace/examples/pgl2/pgl2_worked_example.pdf); §6.1 of the [revised paper](local-trace/paper/)).
- **Proved for semisimple G** (more generally, anisotropic center): the truncated identity (Theorem 4.5(a)) and the Brion combinatorics (Lemmas 3.5A–C). The vertex decomposition of the truncated kernel (Props. 3.6, 4.2) and the spectral identity under Hypothesis (R) (Theorem 4.5(b)) are proved in rank one, and in rank ≥ 2 they are conditional on a uniform form (C) of Casselman's asymptotics.
- **Corrected:** the 1997 claim that I(χ,γ) is always a rational function. For SL(2) the spectral measure has an atom at the quadratic unramified character, given by the κ-orbital integral (§6.2, [`examples/sl2/`](local-trace/examples/sl2/)). All normalization errors in the errata log are corrected in the revision; see [`CHANGES.md`](local-trace/paper/CHANGES.md).
- **Rank two (PGL(3), numerical):** for an unramified elliptic γ of depth 0, the spectral identity holds with no singular part, but Hypothesis (R) *fails*. So (R) is not necessary, and the paper proposes a weaker hypothesis (R′) (Appendix A, [`examples/pgl3/`](local-trace/examples/pgl3/)).
- **Open (rank ≥ 2):** a proof of (R′) or of Conjecture 4.6 (the shape of the singular part); a proof of the PGL(3) displacement table (Observation A.2); other conjugacy classes.

## Reproducing the checks

Requires Python 3 with NumPy and SymPy (also runs under SageMath's Python).

```
python3 run_checks.py
```

This runs every verification script in the repository (currently PGL(2), SL(2), a rank-two lattice-point check for SL(3)/PGL(3), the PGL(3) building computation, and the checks of Sections 2–7 of the metaplectic double cover of SL(2) in `sl2bar-trace/revised/checks/`; under a minute; the PGL(3) and `sl2bar-trace` checks also need SymPy and mpmath).

## Building the documents

Each `.tex` file is self-contained and builds with `pdflatex` (or `latexmk -pdf`). Compiled PDFs are committed alongside the sources.

## License

- **Code** (`*.py`, `*.sage`): [MIT](LICENSES/MIT.txt)
- **Text and LaTeX sources and their PDFs** (`*.tex`, `*.md`, `*.pdf`): [CC BY 4.0](LICENSES/CC-BY-4.0.txt)

See [LICENSE](LICENSE) for details. The 1992 published version in Pacific J. Math. is not included; the 1997 scan is the author's own preprint.

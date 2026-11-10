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
| [`local-trace/paper/`](local-trace/paper/) | The revised, corrected and updated paper (PGL(2)/SL(2) examples, Route B sketch, glossary, literature review before/after 1997) | First complete draft (Nov. 2026) |
| [`local-trace/arthur/`](local-trace/arthur/) | Short guide: deriving the main identity from Arthur's local trace formula ("Route B") | Sketch in §7 of the paper; standalone guide planned |
| [`finite-trace/`](finite-trace/) | Trace formulas for finite groups: the 1996–2003 notes and their 2026 corrected and expanded version | Notes posted; refereeing of the 2026 corrections pending |
| [`common/`](common/) | Shared notation, glossary and bibliography | Started |

## What is proved, what is checked, what is open

The 1997 paper contains errors and two genuine gaps; see the [referee report](local-trace/original-1997/referee_report_ltf.pdf) and the [errata log](local-trace/original-1997/transcription_log.md). Current state:

- **Proved and numerically verified:** the main identity for G = PGL(2), with explicit I(χ,γ) for all elliptic γ ([worked example](local-trace/examples/pgl2/pgl2_worked_example.pdf); §6.1 of the [revised paper](local-trace/paper/)).
- **Proved in general:** the truncated identity (Theorem 4.5(a)), the vertex decomposition of the truncated kernel (Props. 3.6, 4.2), and the spectral identity under a regularity Hypothesis (R) (Theorem 4.5(b)).
- **Corrected:** the 1997 claim that I(χ,γ) is always a rational function. For SL(2) the spectral measure has an atom at the quadratic unramified character, given by the κ-orbital integral (§6.2, [`examples/sl2/`](local-trace/examples/sl2/)). All normalization errors in the errata log are corrected in the revision; see [`CHANGES.md`](local-trace/paper/CHANGES.md).
- **Open (rank ≥ 2):** Hypothesis (R), expected when Z(G) is connected, and the description of the singular part (Conjecture 4.6). A numerical rank-2 check (PGL(3)) is the next step.

## Reproducing the checks

Requires Python 3 with NumPy (also runs under SageMath's Python).

```
python3 run_checks.py
```

This runs every verification script in the repository (currently PGL(2) and SL(2), about 6 seconds).

## Building the documents

Each `.tex` file is self-contained and builds with `pdflatex` (or `latexmk -pdf`). Compiled PDFs are committed alongside the sources.

## License

- **Code** (`*.py`, `*.sage`): [MIT](LICENSES/MIT.txt)
- **Text and LaTeX sources and their PDFs** (`*.tex`, `*.md`, `*.pdf`): [CC BY 4.0](LICENSES/CC-BY-4.0.txt)

See [LICENSE](LICENSE) for details. The 1992 published version in Pacific J. Math. is not included; the 1997 scan is the author's own preprint.

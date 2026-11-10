# trace-formulas

Trace formulas — local (p-adic), finite-group, and related — written up in LaTeX, with every explicit formula backed by a short script that checks it.

Maintained by David Joyner. Parts of this repository were prepared with the help of Claude (Anthropic); this is noted in each document where it applies.

## Contents

| Directory | What it is | Status |
|---|---|---|
| [`local-trace/`](local-trace/) | *Simple local trace formulas for unramified p-adic groups* (D. Joyner; Pacific J. Math. 154 (1992) 103–129; corrected version 1997) and its 2026 revision | Revision in progress |
| [`local-trace/original-1997/`](local-trace/original-1997/) | The 1997 version: scan, literal LaTeX transcription, errata log, referee report | Complete |
| [`local-trace/examples/pgl2/`](local-trace/examples/pgl2/) | Worked example for PGL(2): closed forms for the spectral distribution I(χ,γ) for every elliptic type, verified on the Bruhat–Tits tree | Complete, verified (q = 3) |
| [`local-trace/paper/`](local-trace/paper/) | The revised, corrected and updated paper (glossary, literature review before/after 1997) | Not started |
| [`local-trace/arthur/`](local-trace/arthur/) | Short guide: deriving the main identity from Arthur's local trace formula ("Route B") | Planned |
| [`finite-trace/`](finite-trace/) | Trace formulas for finite groups: the 1996–2003 notes and their 2026 corrected and expanded version | Notes posted; refereeing of the 2026 corrections pending |
| [`common/`](common/) | Shared notation, glossary and bibliography | Started |

## What is proved, what is checked, what is open

The 1997 paper contains errors and two genuine gaps; see the [referee report](local-trace/original-1997/referee_report_ltf.pdf) and the [errata log](local-trace/original-1997/transcription_log.md). Current state:

- **Proved and numerically verified:** the main identity for G = PGL(2), with explicit I(χ,γ) for all elliptic γ ([worked example](local-trace/examples/pgl2/pgl2_worked_example.pdf)).
- **Corrected (normalizations, statements):** Macdonald's constant and chamber convention, the geometric lemma, Casselman's pairing, the δ-factors, §5 signs and endoscopic groups — recorded in the errata log, to be incorporated into the revision.
- **Open (rank ≥ 2):** the regularity of I(χ,φ)·dμ on the unitary torus, i.e. the cancellation of poles off the walls via (G,A)~-families. A numerical rank-2 check (PGL(3)) is planned before the general write-up.

## Reproducing the checks

Requires Python 3 with NumPy (also runs under SageMath's Python).

```
python3 run_checks.py
```

This runs every verification script in the repository (currently: PGL(2), about 3 seconds).

## Building the documents

Each `.tex` file is self-contained and builds with `pdflatex` (or `latexmk -pdf`). Compiled PDFs are committed alongside the sources.

## License

- **Code** (`*.py`, `*.sage`): [MIT](LICENSES/MIT.txt)
- **Text and LaTeX sources and their PDFs** (`*.tex`, `*.md`, `*.pdf`): [CC BY 4.0](LICENSES/CC-BY-4.0.txt)

See [LICENSE](LICENSE) for details. The 1992 published version in Pacific J. Math. is not included; the 1997 scan is the author's own preprint.

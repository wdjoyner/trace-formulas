# Genuine invariant distributions on metaplectic covers of SL(2)

**David Joyner**, *A hitch-hiker's guide to genuine invariant distributions on metaplectic covers of SL(2) over a p-adic field*.

**Current manuscript:** Draft 3 (November 21, 2026), a corrected and expanded synthesis of the January 4, 1994 manuscript and the SL(2) material relevant to the author's 2001 *Journal of Fourier Analysis and Applications* article. The current paper excludes the GL(r) theory.

## Contents

- [`sl2bar-invariant-distributions.tex`](sl2bar-invariant-distributions.tex): editable manuscript (pdflatex, 12pt Times, US Letter).
- [`revision_log.tex`](revision_log.tex): editorial revision log and mathematical verification status.
- [`sl2bar-invariant-distributions.pdf`](sl2bar-invariant-distributions.pdf): compiled Draft 3 paper (22 pages).
- [`revision_log.pdf`](revision_log.pdf): compiled revision log (6 pages), including the Draft 3 changes, verification levels and a Draft 2 to Draft 3 concordance.
- [`referee-2026-11/`](referee-2026-11/): the two referee reports on Draft 2, by Gemini ("Carbon") and by Claude.
- [`scripts/genuine_torus_check.py`](scripts/genuine_torus_check.py): exact checks of the cocycle, the commutators in the covering torus (Lemma 5.2), the unipotent sections and the Bruhat identities. Run by `run_checks.py` at the top of the repository.
- [`original-1994/hitchhiker-sl2bar-repns.tex`](original-1994/hitchhiker-sl2bar-repns.tex): original 1994 manuscript, retained separately as a historical source.

The compiled files are [the Draft 3 paper PDF](sl2bar-invariant-distributions.pdf) (22 pages) and [the revision log PDF](revision_log.pdf) (6 pages). To rebuild them locally, run `pdflatex sl2bar-invariant-distributions.tex` twice and `pdflatex revision_log.tex` twice. The preamble uses newtx when it is installed and falls back to mathptmx otherwise. The committed PDFs of Draft 3 were built with the mathptmx fallback, so rebuilding with newtx changes the fonts and may move line breaks.

## Review status

This is an **expository working draft**, not an independently refereed article. Draft 2 was refereed by two AI referees (Gemini and Claude), and Draft 3 responds to both reports; Draft 3 itself has not been refereed. The topological Paley--Wiener step is explicitly conditional. Draft 3 proves the commutator structure of the covering torus and identifies the kernel and image of the endpoint intertwining operator (Proposition 6.8). The normalization of the endpoint s = 1/n, Moen's exceptional datum and the proposed principal-series images remain unverified against the sources. The published 2001 article is cited, not reproduced.

AI assistance by ChatGPT (OpenAI), Claude (Anthropic) and Gemini (Google) is identified in the first sentence of the abstract and explained in the Acknowledgments and the revision log.

Following the `trace-formulas` convention, file names do not carry draft numbers; Git history tracks successive drafts.

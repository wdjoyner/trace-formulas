# On the unitary dual of SL(2,F)-bar, F p-adic

An unpublished manuscript by David Joyner, dated July 21, 1999 (cited as a
preprint in J. Fourier Anal. Appl. 7 (2001) 343–358), and its corrected and
expanded 2026 revision with AI assistance.

The revision studies Kubota's n-fold cover of SL(2,F): the genuine
representations of the covering torus, split orbital integrals and their image,
the trace and character of genuine principal series, and a split-torus character
identity with SL(2,F) when gcd(p,2n) = 1 and n is odd or divisible by 4. The case
n ≡ 2 (mod 4), including the double cover, is excluded. Despite the title, the
paper does not classify the full unitary dual; it surveys the literature on that.

This sits next to the other metaplectic SL(2) material in `../sl2bar-trace/` and
`../sl2bar-characters/`, and the ordinary-group notes in
`../sl2-invariant-distributions/`.

## Layout

```
sl2bar-unitary-dual/
├── original-1999/   the 1999 manuscript, unchanged
├── revised/         the 2026 revision and its revision log
├── scripts/         exact-arithmetic checks
└── README.md
```

## Contents

| File | What it is |
| --- | --- |
| `revised/sl2bar-unitary-dual-2026.tex`, `.pdf` | The revised paper, currently Draft 2 (November 13, 2026), 26 pages. File names carry no draft number, and git history tracks the drafts (Draft 1, by Sol-ChatGPT, is the previous commit). |
| `revised/revision-log.tex`, `.pdf` | AI usage, original versus new results, every change from Draft 1, sources consulted and not consulted, verification levels, and the numbering concordance. |
| `scripts/kubota_torus_check.py` | Exact checks of the Kubota-cocycle computations (commutators, center, Weyl conjugation, the power map, the splitting of SL(2,O)). Run by `../run_checks.py`. |
| `original-1999/sph_corr5b.tex` | The 1999 manuscript as written. |

## Status

Draft 2 has not been independently refereed. Statements cited but not checked are
labeled "Remark 2026.n" in the paper; the revision log lists the points a human
referee should check first. AI review is not an independent certification of the
results.

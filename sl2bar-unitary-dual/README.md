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
| `revised/sl2bar-unitary-dual-2026.tex`, `.pdf` | The revised paper, currently Draft 3 (November 13, 2026), 31 pages. File names carry no draft number, and git history tracks the drafts (Draft 1 by Sol-ChatGPT, Drafts 2 and 3 by Claude). |
| `revised/referee-report_draft2_sol-chatgpt.tex` | Sol-ChatGPT's referee report on Draft 2 ("major revision, with a sound core"). Draft 3 answers it point by point; see the revision log. |
| `revised/revision-log.tex`, `.pdf` | Response to the Draft 2 referee report, AI usage, original versus new results, every change from Draft 1, sources consulted and not consulted, verification levels, and the numbering concordance. |
| `scripts/kubota_torus_check.py` | Exact checks of the Kubota-cocycle computations (commutators, center, Weyl conjugation, the power map, the splitting of SL(2,O)). Run by `../run_checks.py`. |
| `original-1999/sph_corr5b.tex` | The 1999 manuscript as written. |

## Status

Draft 2 was refereed by Sol-ChatGPT; Draft 3 answers that report and adds proofs of
Kubota's splitting of SL(2,O) and of the rank-one Jacquet-module lemma. Draft 3 has not
yet been refereed. Statements proved elsewhere are labeled "Remark 2026.n" with a status
(source checked or cited only); the revision log lists the new arguments a referee should
check first. Table 1 of the paper gives the status of each unitary-dual claim of the
1999 manuscript and the 2001 paper. AI review is not an independent certification of the
results.

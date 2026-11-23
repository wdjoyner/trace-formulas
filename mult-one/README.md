# Direct comparison of SL(2) with its metaplectic cover

A manuscript by David Joyner, revised with AI assistance in November 2026 from the 1995 book manuscript *Multiplicity one for SL(2)*.

**The question.** By the work of Weil, Shimura and Waldspurger, genuine cuspidal automorphic representations of the 2-fold metaplectic cover of SL(2, 𝔸) correspond to cuspidal automorphic representations of PGL(2, 𝔸). The cover lies over SL(2), so its orbital integrals can be compared with those of SL(2) directly. Does that give a correspondence with SL(2) itself? If not, why not, and how far off is it?

**The answer in this draft.**

- Locally, on the split torus, the direct comparison works: characters, Fourier transforms, traces of principal series, and the spherical Hecke algebras match (odd residual characteristic and the real field).
- Globally it is wrong: no genuine cuspidal representation corresponds to a given cuspidal representation of SL(2, 𝔸) under this matching at almost all places (Theorem 5.16).
- It is off by a square. The direct comparison matches unramified parameters up to sign; the Shimura–Waldspurger correspondence followed by restriction from PGL(2) squares them. Section 5.4 traces this through the trace formula: the torus terms match, and the intertwining operators, the residual spectrum and the cuspidal spectrum do not.
- The 1995 strategy of deducing multiplicity one for SL(2) from Waldspurger's theorem by this comparison therefore cannot work (Proposition 5.10, Corollary 5.17). Multiplicity one for SL(2) is a theorem of Ramakrishnan (Ann. of Math. 152, 2000).

**Status.** Theorem 5.16 and Section 5.4 were written by Claude and rest on results quoted from memory of the literature. They have not been checked by a specialist. Unverified statements are marked "Remark 2026.n" in the text.

## Layout

```
mult-one/
├── revised/
│   ├── direct-comparison-SL2.tex, .pdf    the manuscript (Draft 5)
│   ├── referee-report_draft3.tex, .pdf    Claude's referee report on Draft 3
│   └── referee-report_draft1.md           referee report on Draft 1
├── scripts/
│   ├── local_formulas_check.py            exact checks of local formulas
│   └── referee_check.py                   cocycle checks, and the counterexample of Remark A.2
├── revision_log.md                        stages, AI usage, every change, open items
└── README.md
```

Earlier drafts are not kept in this directory. The revision log describes them.

## Building

In `revised/`, run `pdflatex direct-comparison-SL2.tex` three times. The bibliography is inline, so there is no BibTeX run. The document uses 12pt Times (`mathptmx`), letter paper, and has 87 pages. The compiled PDF is committed beside the source.

The checks: `python3 scripts/local_formulas_check.py` (needs SymPy) and `python3 scripts/referee_check.py`, or `python3 run_checks.py` from the repository root.

## Open items

- Have a specialist check Theorem 5.16 and Section 5.4 against Waldspurger, Gelbart–Jacquet and Jacquet–Shalika.
- Is there a comparison of trace formulas built on the squaring correspondence, and what does it say about SL(2)?
- Do the direct matchings have a representation-theoretic meaning beyond the local identities?
- Bibliography: the volume of [J1], and several entries corrected from memory (see `revision_log.md`).

## License

Text and LaTeX sources are CC BY 4.0, and the scripts are MIT (see the top-level [LICENSE](../LICENSE)).

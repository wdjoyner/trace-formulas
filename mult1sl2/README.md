# Multiplicity one for SL(2)

A book-length manuscript by David Joyner (1995) comparing the trace formulas of SL(2) and of its 2-fold metaplectic cover. The aim is to derive multiplicity one for the cuspidal spectrum of SL(2, 𝔸) from Waldspurger's multiplicity one theorem for the cover. It was revised with AI assistance in November 2026.

**The main result is conditional.** The 1995 draft claimed an unconditional proof. The 2026 revision states the theorem under two explicit hypotheses:

- GH, a global trace identity, refined by archimedean infinitesimal character;
- LH, a local spectral transfer hypothesis at the exceptional places.

It records which steps of the 1995 argument are incomplete. Multiplicity one for SL(2) is known unconditionally from Ramakrishnan (Ann. of Math. 152, 2000). The interest here is the method.

## Layout

```
mult1sl2/
├── revised/
│   ├── multiplicity-one-SL2.tex, .pdf   the manuscript (currently Draft 3)
│   └── referee-report_draft1.md         referee report on Draft 1
├── scripts/
│   └── local_formulas_check.py          exact checks of local formulas (run by ../run_checks.py)
├── revision_log.md                      stages, AI usage, every change (Drafts 1 and 2), open items
└── README.md
```

File names carry no draft number; git history tracks the drafts. Draft 1 is commit `045016f`.

## Status

- **Draft 1** (Claude, November 20, 2026). The 1995 source files are merged into one pdflatex file, and the main theorem is stated conditionally.
- **Draft 2** (Claude, November 20, 2026). This responds to the referee report on Draft 1, which the author believes was written by ChatGPT:
  - The false finiteness lemma is replaced by Harish-Chandra finiteness at a fixed infinitesimal character, with GH refined to match and a new condition (LH4).
  - Waldspurger's theorem is applied only on 𝒜₀₀, via a new lemma excluding the elementary theta series.
  - The torus character correspondences are corrected: p-adic (ε = η_ϖ·ϑ) and real (−i).
  - All anisotropic Cartan subgroups are now included in the elliptic matching.
  - The real discrete-series matchings no longer divide by 2cos θ, and the lemma is recomputed explicitly.
  - The relationship between Satake and orbital integrals is clarified, and the Hecke algebra and global-cover definitions are corrected.
  - The unverified 1995 statements are now labelled **Claim**.
  - A weighted-orbital-integral lemma that cannot hold as stated is identified and demoted.
- **Draft 3** (Claude, November 20, 2026). A style-guide pass with no mathematical changes. It adds a literature review (before and after 1995), a summary of results and open questions, a glossary, orienting paragraphs, and examples in every section, with the cusp form Δ as a running example. It moves the acknowledgments to the end and adds the AI-certification disclaimer, the author line, and the title-page footnote. Draft comparisons move from the body to the log, unverified statements become "Remark 2026.n", and the log gets a Draft 1 → 2 → 3 concordance and an exact-check script.
- **Not yet done:**
  - An independent referee report on Draft 2.
  - A check of the normalizations in Lemma 7.12.
  - The multiplier argument of Remark 7.7.
  - A correction of the supercuspidal character relation.
  - Reconciling the discrete-series labels with Gelbart's.

  See `revision_log.md`, section 5.

## Building

In `revised/`, run `pdflatex multiplicity-one-SL2.tex` three times. The bibliography is inline, so there is no BibTeX run. The document uses 12pt Times (`mathptmx`), letter paper, and has 72 pages. The compiled PDF is committed beside the source.

The checks: `python3 scripts/local_formulas_check.py` (needs SymPy), or `python3 run_checks.py` from the repository root.

## License

Text and LaTeX sources are CC BY 4.0, and the script is MIT (see the top-level [LICENSE](../LICENSE)).

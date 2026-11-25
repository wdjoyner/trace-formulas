# Revision log: invariant distributions on SL(2) over a p-adic field

Paper: `revised/sl2-invariant-distributions-2026.tex` (*A hitch-hiker's guide to invariant distributions on SL_2 over a p-adic field*, D. Joyner).

File names carry no draft number. Git history tracks the drafts. Draft 1 is the file `revised/sl2-invariant-distributions-revised-draft1.tex` at commit `148ba6e`.

## Stages

| Stage | Scope | Status |
|---|---|---|
| 0 | The 1994 notes (`original-1994/hitchhiker-sl2-repns.tex`) | Unpublished manuscript, dated 11-2-94 |
| 1 | First, minor revision of the 1994 source by Argon (Gemini, Google): `original-1994/hitchhikers-guide-to-invariant-distributions-on-sl2-over-p-adic-field2.tex` | Done 2026 |
| 2 | Referee report on stage 1 by ChatGPT (Sol, OpenAI): `revised/referee-report_argon-gemini-revision.md`. Verdict: major revision | Done 2026 |
| 3 | Draft 1: expository rewrite by ChatGPT, responding to its own report | Done November 2026 |
| 4 | Draft 2: style-guide pass by Claude (Fable, Anthropic). No mathematical changes | Done 2026-11-12 (this entry) |

## AI usage

- **Argon (Gemini).** Stage 1. Typographical cleanup of the 1994 source, `\cite` citations, and some mathematical edits.
- **ChatGPT (Sol).** Stage 2 (referee) and stage 3 (author of Draft 1). The same system wrote the report and the revision that answers it. Draft 1 has had no independent referee.
- **Claude (Fable).** Stage 4. Set up this directory, applied `../joyner-math-paper-style-guide.md` (Draft 2 of the guide, November 11, 2026), wrote the new text listed below, and wrote this log. Claude did not referee the mathematics of Draft 1.

AI review is not an independent certification of the results.

## Original results and results new in the revision (guide 6.5)

Read off by comparing the 1994 source with Draft 1. This is a classification by origin, not a verification.

**Carried over from the 1994 notes:** the definitions of smooth and admissible representations; the principal series and the list of families; the Weyl integration formula; the discriminant (3.2) and the principal-series character (3.3); the statement of the trace Paley–Wiener theorem (now in Grothendieck-group form); the Mellin image on F^× (stated in 1994 with the proof omitted); the supertempered virtual character Θ⁺ − Θ⁻ of Example 7.2; the citation of Herb's theorem.

**New in Draft 1 (2026), most of them taken from the referee report:**

| Item in the paper | Origin |
|---|---|
| Theorem 2.2 with the points \|·\|^{±1} | Referee item D |
| Example 2.3 (η₃(3) = −1 for Q₃) | Referee, additional corrections |
| Example 3.1 (normalized orbital integral of 1_K is 1) | Referee item C |
| Proposition 4.1 (trace transform not injective) | Referee item A |
| Example 4.4 (relation at quadratic reducibility) | Referee item F |
| Proposition 4.5 with proof (Mellin image) | Draft 1 |
| Example 4.6 (point evaluation is not invariant) | Referee item B |
| Theorem 5.1 and Corollary 5.2 (Laurent-coefficient criterion) | Referee, section on analytic distributions |
| Example 6.1 (descent of the trivial character) | Referee item G |
| Remark 7.3 (supertempered does not imply elliptic support) | Referee item H |

**Statements of the 1994 notes that Draft 1 withdrew and does not claim** (Section 8 of the paper): the explicit Schwartz-space Paley–Wiener theorem and the resulting description of tempered distributions; the descent lemma for admissible distributions; the converse analyticity theorem and the theorem that "nice" admissible distributions are analytic. The Borel-structure and Tadić-decomposition sections of 1994, and the GL(2) sketch, are not in Draft 1 either.

## Stage 4: Draft 2 (style-guide pass, 2026-11-12)

### Baseline before edits

Draft 1 as received compiled with pdflatex and `newtxtext`/`newtxmath` to 11 pages: no errors, no undefined references, no overfull boxes. (With `mathptmx` substituted there was one overfull box, 25pt, in the literature paragraph.)

### Ground rules for this stage

No mathematical changes. New mathematical text only where the guide requires it. Existing semicolons left alone. Every existing `\label` kept, with one exception noted below.

### Changes

| # | Where | Change | Guide rule |
|---|---|---|---|
| 1 | File | Renamed `sl2-invariant-distributions-revised-draft1.tex` to `sl2-invariant-distributions-2026.tex` | 9 |
| 2 | Title | Added "Draft 2. Corrected and expanded version" | 6.2 |
| 3 | Date line | "Original draft: 1994. Corrected and expanded draft: 2026" (was "Original notes: November 2, 1994; revised and corrected version, November 2026 --- Draft 1") | 6.2 |
| 4 | Title page | `\thanks` note identifying the unpublished 1994 manuscript and the date of this version | 6.3 |
| 5 | Author line | `\email{wdjoyner@gmail.com}` (amsart prints it after the references) | 5.1 |
| 6 | Abstract | New opening: AI-disclosure sentences pointing to the Acknowledgments and this log. "This AI-assisted revision of notes written in 1994 is an expository introduction" became "The paper is an expository introduction". Rest unchanged | 5.2 |
| 7 | Preamble | Added `\newtheorem*{example*}{Example}` for unnumbered examples | 1.9 |
| 8 | Subsection 1.1 | "A brief guide to the literature" removed from Section 1 and replaced by an unnumbered section "Literature review" after Section 1, split at 1994. Label `sec:lit` kept | 2.3 |
| 9 | Subsection 1.2 | "Notation and conventions" is now Subsection 1.1 | consequence of 8 |
| 10 | Section 2.3 | Added label `sec:schwartzbackground` | 1.5 |
| 11 | Theorem 4.2, Remark 4.3 | Items (i), (ii) given labels; "Property (i)", "Property (ii)" now use `\ref` | 1.5 |
| 12 | Appendix A | Glossary is now an unnumbered section before the Acknowledgments. Label `app:glossary` kept. `\appendix` removed | 2.8 |
| 13 | Appendix B | "Revision record and provenance" removed from the paper. Its text is quoted below. Label `app:revision` removed with it (nothing referred to it) | 6.4 |
| 14 | End | New section "Acknowledgments" | 2.9, 5.3–5.5 |
| 15 | Bibliography | Key `CaNotes` → `Ca93` (two `\cite`s updated). Four entries added (ADSS11, Da00, SZ07, Wa03). SS68 title corrected, SS84 pages added, Cl91 volume number added. Widest label `ADSS11` | 1.7, 4.3 |
| 16 | Orienting paragraphs | Added at the start of Subsections 1.1, 2.1, 2.2, 2.3, 2.4, 4.2, 4.3 and Sections 2, 3, 4 | 3.2 |
| 17 | Examples | Six unnumbered examples added (list below) | 3.3, 3.4, 2.4 |

### Comparison-with-1994 wording removed from the body (guide 6.4)

Approved by David before the edit. Each original sentence is quoted.

| Where | Draft 1 | Draft 2 |
|---|---|---|
| Section 1, third paragraph | "The present version separates three sorts of statements" | "This paper separates three sorts of statements" |
| Remark 5.3 | "In particular the stronger global converses asserted in the 1994 notes have been withdrawn from this draft pending proof." | "In particular no stronger global converse is claimed here (see Section 8)." |
| Example 6.1 | "It therefore does not satisfy the naive smooth-density conclusion on all of A that had been inferred from geometric descent in the original notes." | "It therefore does not satisfy the naive smooth-density conclusion on all of A." |
| Remark 7.3 | "This corrects a false implication in the original notes." | (deleted) |
| Section 8 | "Three issues from the historical paper remain outside the scope of this corrected draft:" | "Three issues remain outside the scope of this paper:" |

Left in place: the last sentence of the abstract ("This version deliberately does not claim ... proposed in the original notes ...") and the first sentence of Section 1 ("The original notes were written to ..."). The first is a statement of what is claimed, and the abstract's mathematical sentences were not to be changed. The second is motivation.

### New mathematical text, for refereeing (ground rule 2)

None of this has been refereed. All examples are unnumbered.

| # | Where | Content | What it relies on |
|---|---|---|---|
| N1 | After Definition 2.1 | Example: the trivial representation is smooth, admissible, irreducible. I(χ) is admissible because B\G/J is finite (Iwasawa decomposition G = BK, and K/(K∩J) finite), so dim I(χ)^J ≤ \|B\G/J\|. Right translation on C_c^∞(G) is smooth and not admissible because G/J is infinite | Direct argument |
| N2 | End of Subsection 2.1 | Example: for F = Q₃ exactly five χ give reducible I(χ): \|·\|^{±1} (values 1/3 and 3 at the uniformizer) and η₂, η₃, η₆. η₂ is unramified because Q₃(√2) is the unramified quadratic extension | Theorem 2.2, (2.2), Subsection 2.2 |
| N3 | Subsection 2.3 | Example: matrix coefficients of the trivial representation are constants, so not compactly supported and not square-integrable (G has infinite Haar measure). So the trivial representation is neither supercuspidal nor square-integrable | Direct argument |
| N4 | End of Subsection 2.4 | Example: in the unramified family χ(x) = z^{v(x)}, \|·\|^s has z = q^{−s}. Reducibility at z = q^{−1}, q, −1. Inversion exchanges q^{−1} and q, fixes −1 and 1. I(χ) is irreducible at z = 1 | Theorem 2.2 |
| N5 | Start of Section 3 | Explanation: for regular semisimple γ the centralizer is a maximal torus, the class is closed and identified with G_γ\G, so the integrand has compact support for f in the Hecke algebra | Standard facts, stated without citation |
| N6 | Subsection 4.2 | Example: Θ_π, the orbital integral O_γ (change of variable x ↦ xg^{−1}) and f ↦ f(1) are invariant distributions | Direct argument |
| N7 | After the proof of Theorem 5.1 | Example: evaluation at z₀ has c_n = z₀^n, bound (5.1) with C = 1, R = max{\|z₀\|, \|z₀\|^{−1}}. Non-example: λ(z^n) = n! for n ≥ 0 and 0 for n < 0 violates (5.1), so has no continuous extension | Theorem 5.1 |
| N8 | Literature review | Summaries of GG63, SS68, SS84, Si79, Ca93, BDK86, Ka86, Cl91, Ar93, He94 (before 1994) and Wa03, SZ07, Da00, ADSS11 (after 1994). See the next table for how each summary was checked | See below |
| N9 | Orienting paragraphs (change 16) | Descriptive only. The paragraph for Section 2 says "Nothing in it is new" | — |

### Citations: what was checked and what was not (guide 4.3)

No source was read in full for this stage. "Search" means the bibliographic data, and where stated the content, were confirmed from publisher, Numdam, EuDML, arXiv or MathSciNet-derived listings found by web search on 2026-11-12.

| Key | Bibliographic data | Content claim in the literature review |
|---|---|---|
| ADSS11 | Search: title, authors, arXiv:1012.5548, volume Contemp. Math. 543 (2011). **Page numbers not confirmed, so none are given** | Search: later authors state that this paper supplies proofs of the Sally–Shalika formulas. Note: A.-M. Aubert and R. Plymen, arXiv:2410.20183, comment on the status of Theorem 15.2 of this paper. That note is not cited in the paper |
| Ar93 | Search: Acta Math. 171 (1993), 73–138 | Search: the introduction says the elliptic virtual characters "presumably" span the supertempered ones |
| BDK86 | Search: J. Analyse Math. 47 (1986), 180–192 | Not consulted. The summary repeats Theorem 4.2 of the paper |
| Ca93 | Search: the draft on Casselman's UBC page is headed "written 1974–1993", dated 7 May 1993. Key changed from `CaNotes` to `Ca93` on that basis | Search: the introduction of the notes covers admissible representations, induction, Jacquet modules |
| Cl91 | Search: pages 101–122 (as cited by Herb). Progr. Math. volume 101 from memory, **not confirmed** | Not consulted |
| Da00 | Search: Invent. Math. 140 (2000), no. 1, 171–226 | Search: later papers describe its use of the Hattori–Stallings rank. The sentence "a later development of the ideas around the cocenter" is from memory |
| GG63 | **Not checked** | Not consulted |
| He94 | Search: Compositio Math. 93 (1994), no. 2, 139–154 | Search (Numdam first page): proves Arthur's conjecture, and supertempered iff all weak constant terms vanish |
| Ka86 | Search: J. Analyse Math. 47 (1986), 1–36 | Not consulted. The summary repeats what Section 4 of the paper says |
| Si79 | Publisher data via search | Search (publisher's description): Schwartz space, constant term, Eisenstein integral |
| SS68 | Search (AMS reference lists): the title ends "over a local field", not "over a p-adic field". **Title corrected** | Not consulted |
| SS84 | Search: pages 303–340 added | Not consulted |
| SZ07 | Search: J. Inst. Math. Jussieu 6 (2007), no. 4, 639–688 | Search (abstract): modules over the Schwartz algebra, parabolic induction and restriction, exact and adjoint both ways |
| Wa03 | Search: J. Inst. Math. Jussieu 2 (2003), no. 2, 235–333 | Search (abstract): a write-up of Harish-Chandra's unpublished manuscript |

The paper cites whole works, without theorem or page numbers. Pinpoint citations were not added, because the sources were not consulted.

### Not verified in this stage

- The mathematics of Draft 1. This stage changed no statement or proof and did not referee them.
- Theorem 7.1 is Herb's theorem "in the form needed here". Its first sentence matches the Numdam first page. The second sentence (the rank-one specialization) was not checked against the source.
- Guide rule 6.6 asks for unverified items to be marked "Remark 2026.n". No such remarks were added, because that would change status labels. The unverified items are listed here instead.

### [DECIDE] defaults used

- Document class: kept `amsart`.
- Times package: `newtxtext`, `newtxmath`.
- Glossary: at the end, just before the Acknowledgments. Notation near the beginning (Subsection 1.1).
- Author line: the prompt gave none, so David Joyner alone. AI credit is in the Acknowledgments.

### Guide rules not applied, with reasons

- 3.3 (an example in every section) for the Introduction (exempted by David), the Literature review, Section 8, the Glossary and the Acknowledgments.
- 3.8 (no semicolons) for existing text, by instruction. New text has none.
- 4.3 pinpoint citations and 6.6 remarks: see above.
- 8.2 says the log is a LaTeX file. Section 9 (trace formula repository) says `revision_log.md`, and that rule was followed.

### Final compilation

pdflatex, three passes, TeX Live 2023 with newtx: 14 pages, no errors, no undefined references or citations, no overfull or underfull boxes.

### Concordance, Draft 1 to Draft 2

No theorem, proposition, lemma, example, remark or equation number changed. Sections 2 to 8 keep their numbers.

| Draft 1 | Draft 2 |
|---|---|
| Subsection 1.1, A brief guide to the literature | Unnumbered section "Literature review" (label `sec:lit`) |
| Subsection 1.2, Notation and conventions | Subsection 1.1 |
| Appendix A, Glossary | Unnumbered section "Glossary" (label `app:glossary`) |
| Appendix B, Revision record and provenance | Removed. Text below. Label `app:revision` removed |
| Citation key `CaNotes` | `Ca93` |
| File `sl2-invariant-distributions-revised-draft1.tex` | `sl2-invariant-distributions-2026.tex` |

### Text removed from the paper

**Appendix B of Draft 1, "Revision record and provenance"** (LaTeX source, verbatim):

> The supplied Argon--Gemini LaTeX revision of notes originally dated November 1994 is preserved verbatim as a 2026 source snapshot (not as a verified facsimile of the actual 1994 manuscript). Draft 1 (November 2026) is a substantial, AI-assisted expository rewrite prepared with ChatGPT (OpenAI) following independent mathematical refereeing of an Argon--Gemini revision. It is \emph{not} a claim that every formula of the historical manuscript has been certified. The most consequential revisions are: (a) replacement of the asserted bijection $C_c^\infty(G)\to\PW(G)$ by the invariant cocenter and trace map; (b) the correct reducibility exceptions; (c) a counterexample to singular orbital-integral vanishing; (d) the correct BDK good-form theorem; (e) a proved rank-one Laurent growth lemma; and (f) correction of the weak-constant-term/elliptic-support confusion. Unproved historical descent and distribution theorems have been omitted, with their status documented in Section \ref{sec:summary}.

**Subsection 1.1 of Draft 1, "A brief guide to the literature"** (LaTeX source, verbatim):

> Gelfand and Graev established fundamental rank-one representation-theoretic descriptions \cite{GG63}.  Sally and Shalika calculated the discrete-series characters and studied orbital-integral transforms \cite{SS68,SS84}.  Harish-Chandra's character theory and Schwartz-space theory are developed in accessible form by Silberger \cite{Si79}; Casselman's introduction explains admissible representations and Jacquet modules \cite{CaNotes}.  The trace Paley--Wiener theorem of Bernstein, Deligne and Kazhdan \cite{BDK86}, together with Kazhdan's density theorem \cite{Ka86}, supplies the invariant spectral description.  Clozel's work \cite{Cl91} concerns invariant harmonic analysis on the Schwartz space.  Arthur's treatment of elliptic tempered characters \cite{Ar93} and Herb's classification of supertempered virtual characters \cite{He94} clarify the final section.  We distinguish results actually obtained here from results only cited from these works.


## Draft 3 working assembly — November 24, 2026 (ChatGPT)

- Restored the full previously compiled spectral geometry supplement as an input module (four TikZ figures).
- Integrated the trace comparison module (six TikZ diagrams) and the new spectral duality module (five TikZ diagrams). Preserved earlier theorem labels and the bilateral Laurent criterion.
- Added the split exact sequence for reducibility constraints, moment growth classifications, central eigenfunctional and jet formulas, and global direct-sum duality. These are elementary derivations at the spectral-model level; group-side conclusions use the stated classical trace and topology inputs.
- Corrected the proposed rational Laurent-moment converse: the finite sequence with only moment 1 nonzero has rational generating series but is not center-finite. Rationality of the monomial moment series is the correct equivalent criterion.
- The unramified algebraic difference coordinate in Section 3 is converted in Sections 5–7 to the independent Steinberg trace, which survives restriction to the tempered spectrum. The non-tempered evaluation constraint is not imposed on smooth circle data.
- Combined bibliography from the geometry supplement with the existing bibliography, retaining existing keys. No new comprehensive source audit was performed; the earlier geometry verification note records consulted and unverified sources. Solleveld survey references still need full bibliographic/version checking.
- The assembled source uses Draft 2 as an interim editorial scaffold, not as a replacement for the authoritative 1994 baseline. The original files are unchanged. Full original theorem inventory and restoration remain outstanding.
- No combined pdflatex build was performed: the compilation environment could not resolve GitHub, while the connector allowed text-source commits. The existing PDF is Draft 2. The new assembly is not yet independently refereed.


## Section 8 expansion — November 24, 2026 (ChatGPT)

- Replaced the abbreviated descent section by the insertable admissible-distributions.tex module; retained the section and counterexample labels. Restored the five topics of the original Section 8, including the exploratory GL(2) argument as a research question.
- Level 1 (independent derivation, conditional on classical character inputs): bounded eigenvalue valuations on compact sets; finite-dimensional Laurent interpolation by generic unitary parameters; local finite-character decomposition; locality and stability under shrinking the admissibility subgroup; conditional finite-block admissibility. The exact Harish-Chandra definition and regularity hypotheses still require source verification.
- Level 1: split normalization counterexample at both singular points; normalized descent of the induced family; quadratic constituent difference vanishes on the regular split torus by restriction of the irreducible GL(2) principal series and transitive conjugation of its two SL(2) constituents. The last uses the classical GL(2) irreducibility and SL(2) quadratic decomposition criteria (level 3 until exact references are audited). This proves the unramified split descent obstruction criterion under those inputs.
- Recovered the character-measure construction and extended it to higher spectral derivatives in a finite block; corrected the original quasi-finite type terminology, retaining the constant Fourier mode, exceptional coordinates and the distinction between uniform and blockwise order. The Dirac distribution at identity is a counterexample to unrestricted admissibility of invariant tempered distributions. Its nonrepresentability and the central finiteness counterexamples have elementary proofs.
- Five native TikZ figures added; existing 15 figures retained. Harish-Chandra, DeBacker, Aizenbud–Gourevitch–Sayag and Chen–Tsai references added as literature leads. Full source-level verification is outstanding; Chen–Tsai full text was not retrieved and no result of that paper is used as a proof input.
- Direct GitHub checkout from the local compilation environment failed (DNS). Added a path-scoped GitHub Actions PDF build, based on the repository's existing adjoint-lift workflow. This builds and commits only the SL2 manuscript PDF on revised LaTeX changes. No independent referee review has been performed. Original 1994 mathematical inventory and full restoration remain outstanding.


## Section 9 expansion: supertempered distributions — November 24, 2026 (Claude)

Author of this stage: Claude (Fable, Anthropic). The mathematics was first delivered to the author as a research report (`research/section9-supertempered-research-report.tex`, `.pdf`) and integrated at his request. The report's statement numbers differ from the paper's, because the paper adds Herb's theorem as a numbered statement and one remark.

### Changes

- Replaced the abbreviated Section 9 by the module `revised/supertempered-distributions.tex` (twelve subsections, six TikZ figures, four tables). The labels `sec:supertemp`, `thm:herb`, `ex:supertemp`, `rem:support` and `eq:alt` are retained. `thm:herb` now states Herb's Theorems 2.5, 3.1 and 3.2. The rank-one theorem is `thm:herb-rank-one`.
- Main file: six macros (`\triv`, `\EP`, `\ST`, `\Ann`, `\Ext`, `\ev`); abstract, Introduction (one sentence on the characteristic-zero hypothesis), literature review (one paragraph before 1994, one after), summary (one sentence), glossary (two entries reworded, two added), Acknowledgments (one sentence), and fourteen bibliography entries.
- `admissible-distributions.tex`: two sentences now point forward to Corollary `cor:descent` and Proposition `prop:hecke` (see "Errors and inconsistencies" below).
- `spectral-duality.tex`: the closing paragraph on exceptional modes now says that the zero-moment subspace depends on the splitting and points to Theorems `thm:twosplit` and `thm:exact`.
- Added `research/` with the report and `section9-tree-checks.py`, the script behind the exact checks.
- The paper remains Draft 3. The original 1994 files are unchanged.

### New mathematical text, for refereeing

Everything in Section 9 is new text and has not been refereed. Levels: 1 = derived in this stage from the stated inputs; 2 = cited, statement read in the source during this stage; 3 = cited from memory, source not consulted.

| Statement (label) | Content | Level and dependence |
|---|---|---|
| `tab:four`, `prop:cass` | Jacquet character, weak constant term, normalized split restriction, compact defect | Table: level 1 from the geometric lemma. Casselman's theorem: level 3, checked against the explicit characters of I(χ), St, 1, π_η^± |
| `prop:bohr` | Weak constant term as the almost periodic part at infinity | Level 1 |
| `thm:herb` | Herb's Theorems 2.5, 3.1, 3.2 | Level 2. The displayed inequalities of the strong estimate did not extract from the PDF and were written from memory in `def:six` |
| `thm:herb-rank-one`, `cor:irr`, `cor:three-questions` | Rank-one proof of Herb's classification; kernel of the Jacquet functor; elliptic support implies cuspidal | Level 1, given the classification, `prop:cass` and Harish-Chandra's local boundedness (level 3) |
| `thm:Deta` | Four descriptions of D_η; support on tori splitting over E_η | Level 1, given the GL(2) restriction argument of Section 8 and Keys (level 3) |
| `thm:tree` | Θ_{π±}(γ) = ±(V_0 − V_1) on elliptic elements | Level 1, given the Schneider–Stuhler fixed-point formula at level zero. That formula was read only in the introduction of Korman's paper (level 2 for the statement; the level-zero hypothesis is not checked in [SS97]) |
| `prop:pseudo` | Explicit pseudo-coefficients e_{K_0} − e_{K_1} and e_I − e_{K_0} − e_{K_1} | Level 1 |
| `thm:twosplit`, `thm:exact` | Two complements of the induced part; exact sequences; annihilators; dimension table | Level 1. Attribution of the operator 1 − ½ i_B r_B to Bernstein–Deligne–Kazhdan and Dat is level 3 |
| `def:wct`, `thm:decomp` | Weak constant term of a finite-block distribution; canonical decomposition | Level 1, given Theorems `thm:local-interpolation`, `thm:induced-descent`. Part (e) conditional on the Schwartz trace identification |
| `thm:germ`, `cor:descent` | h_Θ = ½w + c_0 |t − t^{-1}| near I; split descent criterion | Level 1 from the local character expansion (level 3). c_0 = −d(π)/d(St) and Rodier's theorem are level 3 |
| `prop:sc` | Depth-zero supercuspidal character on the split torus | Level 1, given Korman's truncated formula (level 2, introduction only). Sums checked exactly by the script. Not compared with [SS68], [ADSS11] |
| `ex:cancel`, `ex:poisson` | Steinberg obstruction cancelled by supercuspidals; an elliptically supported distribution that is not supertempered | Level 1, given `prop:sc` |
| `prop:center` | Center-finite, virtual character, and supertempered | Level 1, given `thm:duality-eigen`, `thm:duality-jets` |
| `prop:hecke` | Hecke-finite equals blockwise center-finite | Level 1 in outline only. Needs a full write-up before it is relied on |
| `rem:infinite` | δ_cusp probably not admissible | Heuristic |
| `prop:EP`, `ex:norm` | Euler–Poincaré form from the infinite dihedral Hecke algebra; elliptic norm of Steinberg by integration | Level 1, given Borel and Roche (level 3). The integral identity was checked exactly for q = 3, 5, 7, 9 |
| `thm:global` | Global characterization for finite Bernstein support | Level 1 from the above; (b) conditional |

No novelty is claimed. No source was found, in a limited search, for `cor:descent`, `thm:twosplit` in this form, or the counterexamples of Subsection 9.10.

### Errors and inconsistencies found in earlier material

1. **1994 notes, Section 4.2.6.** Supercuspidal characters are stated to vanish off the elliptic set. False: by `prop:sc` a depth-zero supercuspidal character equals |t − t^{-1}|^{-1} − 1 on split elements near I, and in general c_0(π) = −d(π)/d(St) ≠ 0. Draft 3 does not repeat the claim. Nothing relying on it should be restored.
2. **1994 notes, Section 9.1.** "A Hecke-finite distribution is a virtual character, hence automatically admissible" is false as stated: parameter derivatives of characters and locally finite infinite sums are Hecke-finite (`prop:hecke`). The definition of supertempered there does not say which constant term D_P is meant. With the ordinary one, Steinberg is not supertempered, contradicting the next sentence of the notes. The 1994 corollary "supertempered implies virtual character" holds for finite Bernstein support (`prop:center`(d)). The two 1994 questions are answered in `cor:three-questions`. The 1994 lemma on elliptic support is proved there as part (c).
3. **Draft 3, old Theorem 9.1.** "Spanned by the virtual characters arising from the elliptic constituents of tempered parabolic induction" was imprecise: π_η^± are elliptic representations whose characters are not supertempered. Replaced by Herb's statement in terms of Arthur's Θ(M, σ, r) with r regular.
4. **Draft 3, old Section 9 and Glossary.** "Tempered exponents" corrected to "unitary exponents".
5. **Draft 3, Theorem `thm:unramified-descent`.** Correct for one block. The following sentence said no criterion was asserted with supercuspidal blocks. The criterion is `cor:descent`, and β = 0 is not the right condition across blocks (`ex:cancel`). Sentence amended.
6. **Draft 3, end of Section 7.** The zero-moment subspace depends on the splitting. Section 3 uses tr St − tr 1 and Sections 5–7 use tr St. Sentence amended.
7. **Draft 3, Section 8, implication diagram text.** "Not a synonym for center-finiteness" amended to point to `prop:hecke`.
8. **Hypotheses on F.** Section 1 allows any non-archimedean local field of odd residue characteristic; Sections 3, 8 and 9 need characteristic zero. One sentence added to the Introduction.
9. **Not fixed: structure of the assembled file.** `trace-pw-comparison.tex` begins with `\subsection`, so its parts are subsections of Section 5 although its text says "this section". The subsection "The bilateral Laurent criterion" lands at the end of Section 7 and duplicates Theorem `thm:duality-holomorphic`. Left for a decision by the author, because a fix renumbers Sections 5–7.

### Sources not consulted in this stage

Casselman [Ca77]; Harish-Chandra [HC99], [HC83]; Rodier [Ro75]; Keys [Ke82]; Labesse–Langlands [LL79]; Borel [Bo76]; Roche [Ro98]; Kottwitz [Ko88]; Schneider–Stuhler [SS97] (read only through Korman's introduction); Sally–Shalika [SS68] and Adler–DeBacker–Sally–Spice [ADSS11] (abstract only). Reeder [Re01], Opdam–Solleveld [OS13], Ciubotaru–He [CH17], [CH21] and Aubert–Plymen [AP24] were seen as titles, abstracts or search snippets only. Page ranges marked "not verified" in the bibliography are from memory.

### Recommended audits

1. Read [Ca77], [SS97, Section III.4] and [HC99] for the exact statements used in `prop:cass`, `thm:tree`, `prop:sc` and `thm:germ`.
2. Compare `prop:sc` and `thm:tree` with the tables of [SS68] and [ADSS11].
3. Write out `prop:hecke` in full and have it refereed.

### Compilation

The combined source was compiled with pdflatex (three passes) in a scratch copy with `mathptmx` substituted for `newtx`, which was not installed in the build environment: 56 pages, no undefined references or citations, no multiply defined labels. The committed PDF is produced by the GitHub Actions workflow after merge to main.

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

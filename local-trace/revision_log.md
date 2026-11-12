# Revision log: simple local trace formulas for unramified p-adic groups

This log accompanies `paper/local-trace-formula-2026.tex`. It records the drafts of the 2026 revision, the AI usage, the responses to referees, which results are original and which are new, and the sources that could not be consulted. It follows `../joyner-math-paper-style-guide.md` (Draft 2, November 11, 2026), Sections 6, 8 and 9.

Files in the git history track the drafts. File names carry no draft number (style guide, Section 9).

## Drafts and stages

| Draft | Date | What | Record |
|---|---|---|---|
| 0 | 2026-11-10 | Literal LaTeX transcription of the October 1997 version, with errata log and first referee report (Claude) | `original-1997/transcription.tex`, `original-1997/transcription_log.md`, `original-1997/referee_report_ltf.tex` |
| 1 | 2026-11-10 | First revised draft: corrections, Route A repairs, PGL(2) and SL(2) examples, Route B sketch, glossary, literature review. Revised after the second referee report (ChatGPT): standing hypothesis (H), Lemma 2.8, input (C), Lemmas 3.5B–C, Lemma 6.1A, PGL(3) appendix | `paper/CHANGES.md`, `paper/referee-report-2.md`, `paper/RESPONSE-TO-REFEREE-2.md`, and the former Appendix C (below) |
| 2 | 2026-11-12 | Style-guide pass: preamble, numbering by `\label`/`\ref`, title page, AI disclosure, acknowledgments, citation keys, literature review moved and split at 1997, new Section 8, PGL(3) appendix renamed A, glossary moved to the end, Appendix C moved here, Example 2.5 | *Draft 2: style-guide pass* (below) |

## AI usage

- **Claude (Anthropic)**, co-author.
  - As referee, it wrote the first referee report on the 1997 version (`original-1997/referee_report_ltf.tex`).
  - As co-author and reviser, it made the literal transcription and the errata log, drafted Drafts 1 and 2 (text, examples, literature review, summary, glossary), and wrote the response to the second referee report.
  - It wrote the verification scripts in `examples/`.
  - It checked the bibliography against publisher, Numdam/EuDML or library records (Remark 2026.18).
- **ChatGPT (OpenAI)**, independent referee. At D. Joyner's request it wrote the second referee report (`paper/referee-report-2.md`), on Draft 1 as of the morning of 2026-11-10. The changes it led to are listed in `paper/RESPONSE-TO-REFEREE-2.md`, and in *Moved from the Acknowledgments* below.
- **D. Joyner** directed the work, made the decisions recorded in this log, and reviewed the drafts.

Review by AI systems is not an independent certification of the results.

## Original and new results (style guide, rule 6.5)

**Original (1992, or added in the 1997 version), kept with corrections:**
- §2: Lemmas 2.1–2.9, Corollaries 2.3 and 2.5, Remarks 1–2. Lemma 2.1 has a corrected constant and chamber. Lemma 2.8 now needs saturation of the coroot lattice. §2.5 was added in 1997.
- §3: Lemmas 3.1–3.4, Remarks 3–5, and (3.1)–(3.4) and (3.7)–(3.9). Lemma 3.2 has a new proof. Lemma 3.3 now uses the opposite parabolic and includes δ_P^{1/2}. Proposition 3.6 has a new statement and a new proof. Proposition 3.7 was added in 1997.
- §4: Propositions 4.2 and 4.3 (4.3 was added in 1997), Lemma 4.4, Theorem 4.5, and (4.2)–(4.11). Proposition 4.2 has a new form. Theorem 4.5 is split into (a), which is unconditional, and (b), which holds under (C) and (R).
- §5 (added in 1997): rewritten. Proposition 5.2 answers, conditionally, the question with which the 1997 version closed.

**Removed:** the 1997 Lemma 3.5 (false), (3.5)–(3.6) and Remark 6. Also §4.1 with Lemma 4.1 (unverified and unused) and Remarks 7–8.

**New in 2026:**
- Statements:
  - Lemma 3.5A (Brion's vertex decomposition, replacing Lemma 3.5), Lemma 3.5B, Lemma 3.5C
  - Corollary 4.5A, Hypothesis (R), Conjecture 4.6
  - Lemma 5.0, Propositions 5.1–5.2
  - Theorem 6.1, Lemma 6.1A, Proposition 6.4
  - Conjecture 7.3
  - Appendix A (PGL(3): (A.1)–(A.4), Observation A.2) and Hypothesis (R′) (Remark 2026.20)
- Sections: §§2.0, 2.1A, 2.3A, 6, 7 and 8, the literature review and the glossary.
- Examples: all of them.
- Remarks: Remarks 2026.1–2026.20 and Remarks 6.2–6.3.

## Sources that could not be consulted, or were not checked (style guide, rule 4.3)

- [Wa89a], §7: the precise form of Lemmas 2.7 and 2.9 has not been checked against the source (Remark 2026.5). These lemmas are not used in any proof.
- [Wa89a]: the GL(N) analogue of Theorem 4.5(b) has not been checked against the formulation used here (Remark 2026.13).
- [Ca95], [Ca80]: the form (C) of Casselman's asymptotics for intermediate parabolics was not found in the literature (Remark 2026.6).
- [Ar91], [Ar93]: the normalizations of Section 7 have not been checked (Remark 2026.17).
- [Ca79], §3: the non-split form of c_α was not re-derived (Remark 2026.2).
- [LS87]: the κ-dependence of transfer factors is quoted, not checked, and sign conventions vary (Remark 2026.15).
- The bibliographic entries were checked against publisher or library records (Remark 2026.18). The literature review does not survey the later explicit computations of spherical orbital integrals on the building.

## Draft 2: style-guide pass (2026-11-12)

The paper was brought into line with the style guide (Draft 2, November 11, 2026), following the audit of November 11 and DJ's instructions of November 12. **No statement, proof, hypothesis or status label was changed.**

**Compiling.**
- Before the pass: 63 pages, no errors, no undefined references, 2 overfull and 9 underfull boxes. There were also about 170 hyperref "duplicate destination" warnings, caused by the `\tag` numbering, and 25 "token not allowed in PDF string" warnings.
- After the pass: 62 pages, **no errors, no warnings, no undefined references and no overfull boxes**. There are 18 underfull boxes, badness only.
- All 11 scripts of `run_checks.py` pass.

### Decisions (DJ, 2026-11-12) and defaults used

- **Numbering, option A1.** Every displayed number of Draft 1 is kept, so that the revision can be compared with the 1997 version. A note in the Introduction (*A note on numbering*) apologizes for the unusual numbering and explains it.
  - Results are real `\newtheorem` environments with one counter, numbered within sections. Where a counter cannot produce the 1997 number, a `\setcounter` sets it: §4 starts at 4.2, Proposition 3.6 follows the lettered lemmas, Conjecture 7.3 has no 7.1 or 7.2.
  - Lettered items (Lemmas 3.5A–C, 5.0, 6.1A, Corollary 4.5A) and all Examples use "fixed" environments. Each prints the given number and passes it to `\label`.
  - Equations use `\numberwithin`, with `\setcounter` before (3.7), (4.2), (4.7), (5.4) and (5.7), and `\tag` for (2.13A), (3.5A), (4.7A) and (5.4A).
  - Every cross-reference is `\ref` or `\eqref`: 422 `\ref` and 123 `\eqref` were converted by script, and the rest by hand.
- **Glossary.** It moves to the end, as an unnumbered section just before the Acknowledgments. The PGL(3) appendix becomes **Appendix A**, so B.n becomes A.n (concordance below).
- **Dangling references.** "Example 2.0B" (Remark 2026.12) now points to (2.13A) in §2.3A. "(5.6)" in §1 (a 1997 equation number) is now (5.11), the fundamental-lemma form of the geometric side that plays the role of the 1997 (5.6).
- **Literature review split at 1997** (was 1992). Work of 1997 counts as "up to 1997" (see the list below).
- **[DECIDE] defaults.**
  - Document class `article`: kept.
  - Fonts: newtx is preferred, but it is not installed in the build environment and CTAN could not be reached. The fallback `mathptmx` is used, and the newtx line is in the preamble as a comment.
  - Glossary placement: at the end, before the Acknowledgments.
  - Author line: the prompt said nothing, so "David Joyner and Claude" is kept. A version for arXiv or a journal would need Claude moved to the acknowledgments.
- **Date line.** "Original draft: 1997", as instructed. The `\thanks` note names both the 1992 publication and the 1997 version.

### Changes, by step

1. **Preamble.**
   - Was `11pt`, 1.1in margins, Computer Modern. Now `12pt,letterpaper`, `fontenc` T1, `mathptmx`, and `geometry` with one-inch margins.
   - `\DeclareMathOperator` for vol, tr, Hom (previously `\operatorname` macros), diag, supp, meas, Lie, Alg, Res, End, Ad, inv, Gal and tcone, replacing 49 occurrences of `\mathrm{…}`. `\mathrm{Re}` became `\operatorname{Re}`.
   - "centred" is now "centered" (§6.1), and "Acknowledgements" is now "Acknowledgments".
   - Section titles with math use `\texorpdfstring`.
2. **Numbering.** As above. Display changes: "Lemmas 3.5A–C" is now printed "Lemmas 3.5A–3.5C". The four starred hand-numbered subsections (2.0, 2.1A, 2.3A, 6.0) use `\fixedsubsection`. The subsections of Appendix A are ordinary numbered subsections.
3. **Title page, abstract, acknowledgments.**
   - Subtitle "Draft 2. Corrected and expanded version". Date line "Original draft: 1997. Corrected and expanded draft: 2026".
   - The note about the original moved from a `\footnote` on the date to a `\thanks` on the title (rule 6.3). It now names Pacific J. Math. 154 (1992) and the October 1997 version.
   - `wdjoyner@gmail.com` on the author line (rule 5.1).
   - The abstract opens with an AI-disclosure sentence that points to the Acknowledgments (rule 5.2). "This AI-aided paper revises…" became "The paper revises…".
   - The Acknowledgments were rewritten (rules 5.3–5.5). They give Claude's roles (referee of the 1997 version, co-author and reviser, transcription, scripts) and ChatGPT's role (independent referee of Draft 1). They state that AI review is not an independent certification, and they point to this log. The 1997 acknowledgment is kept. The item-by-item account of the ChatGPT report moved here (*Moved from the Acknowledgments*).
4. **Citation keys** (rule 1.7). Cas80 became Ca80 and Cas95 became Ca95, in the bibliography and in all 10 `\cite`s. There is no clash with Cartier's Ca79. All other keys already conformed. Keys in `paper/CHANGES.md`, `paper/RESPONSE-TO-REFEREE-2.md` and `original-1997/` are records and were left unchanged.
5. **Structure** (Section 2 of the guide, rule 6.4).
   - The literature review (formerly §8) is now the unnumbered *Literature review* after Section 1, in two parts: *Work up to 1997* and *Work since 1997*. The opening paragraph and the two part openings were rewritten for the new split. Everything else is moved verbatim:
     - Moved into the first part: the paragraph on [Ar93], [Wa95a] and [Wa95b] (*Elliptic harmonic analysis*); the first two sentences of *Transfer and the fundamental lemma* ([Ha95], [Wa97], [Co97]); and the first sentence of *Elliptic theory via the building* ([SS97]).
     - The rest stays in the second part.
     - All 53 citations and every sentence were checked to be present after the move.
     - Remark 2026.18 (literature) keeps its number, which is fixed because it now comes first. The counter is stepped where the remark used to be, so Remarks 2026.19–20 keep theirs.
   - New Section 8, *Summary of results and open questions*.
   - Order at the end: Section 8, Appendix A (PGL(3)), Glossary, Acknowledgments, References.
   - Appendix C was removed from the paper. It is reproduced below (*Former Appendix C*), and its label `app:revision` is the one label that could not be kept.
   - Revision history removed from the body:
     - §4 opening: "see Appendix C" became "see the revision log".
     - Glossary, *Langlands' combinatorial lemma*: "; used in the 1997 proof of Proposition 3.6" was removed.
6. **Layout.** Two overfull boxes appeared in the 12pt build. Both were removed without manual line breaks and without changing wording: in the proof of Lemma 6.1A the formula for I^T(χ,h) is now a display, and in §A.4 the formula for f_ν^∨ is now a display. The two overfull boxes of Draft 1 disappeared in the new layout.

### Checks of this pass

- **Labels.** Every `\label` of Draft 1 prints the same number in Draft 2, except `app:pgl3` (B → A) and `app:revision` (removed). This was checked by comparing the `.aux` files.
- **Source diff.** The new source, with every `\ref` and `\eqref` replaced by its printed number, was diffed word by word against Draft 1. The only differences are the ones listed in this section.
- **Example 2.5** was checked symbolically (SymPy, m = 0, …, 5).

### New mathematical text, for refereeing (ground rule 2)

These are the only additions with mathematical content. Each one needs an independent check.

1. **Example 2.5** (`ex:2.5`, §2.5): (G,A)- and (G,A)~-families in rank one.
   - θ_B = v⁻¹ξ and θ_B̄ = −v⁻¹ξ, with ξ = λ(α^∨), so c_A = v(c_B − c_B̄)/ξ.
   - Example: c_B = 1, c_B̄ = e^{−mξ}, with c_A(0) = vm.
   - Periodic version: θ̃_B = 1 − y and θ̃_B̄ = 1 − y⁻¹, with y = χ(a_α). For c̃_B = 1, c̃_B̄ = y^m this gives c̃_A = Σ_{k=0}^m y^k.
   - Status: checked symbolically.
2. **§2.3A, exponential polynomials:** two sentences of examples, pointing to Example 4.2 (three characters 1, y^t, y^{−t}, constant coefficients) and to Example 3.6 (the trivial character carries a degree-one polynomial with slope 1/ρ). Both restate those examples.
3. **§3.2:** "in rank one the only standard parabolics are B and G, so L₀ = X_*(A)".
4. **Section 8.**
   - The status table is moved from the former Appendix C.1, with "(November 2026)" removed from its heading.
   - Eight open questions, each raised in the text at the place cited. The wording of items 2 and 3 follows Remark 2026.20 and Conjecture 4.6(a).
   - The referee should check that no status is stated more strongly than in the body.
5. **Not mathematical, but new:** the numbering note in §1, the opening of the literature review and of its two parts, and the opening of Section 8.

### Semicolons

Rule 3.8 was applied to new text only. No semicolon was removed from existing text, except the one that ended the removed glossary clause. The status table, moved verbatim, keeps its semicolons.

### What was left alone, and why

- **Rule 3.2:** already met. Every section and subsection had an orienting paragraph, and the new parts have one.
- **Rule 3.3:**
  - §1 is counted as having its example in prose (PGL(2) and SL(2), and the atom).
  - The literature review, Section 8 and the glossary explain no concepts.
  - §2.0 (Conventions) is notation.
  - The opening of §2 still says "each subsection ends with an example", which is not true of §2.0.
- **Rule 3.4:** examples were added only for the (G,M)- and (G,A)~-families, exponential polynomials and L₀. Weighted orbital integrals and weighted characters (§7.1) get none, because Remark 2026.17 says that Arthur's normalizations were not checked, and an example would be new mathematics.
- **Rules 3.5–3.7 and Section 4 of the guide** (symbols at first use, hypotheses, skipped steps, citations checked against sources) were not re-checked. That needs a referee pass, and this pass makes no mathematical changes.
- **Rule 8.2** (a LaTeX log): Section 9 of the guide asks for `revision_log.md` in this repository.
- **Rule 8.4** (scripts by commit hash): not done. The paper cites the scripts by path.
- **Rule 8.6:** the repository is public. Whether the corrected version of the published paper may be posted is for DJ to decide.
- **Fixed numbers remain** for the Examples, the lettered results and Remark 9 (option A1).

### Numbering concordance (ground rule 5): Draft 1 → Draft 2

| Object | Draft 1 | Draft 2 |
|---|---|---|
| Dirichlet-kernel equation (§2.3A) | (2.16), a duplicate of the (2.16) in §2.5 | (2.13A) |
| Literature review | §8, with §8.1 *Before 1992* and §8.2 *After 1992* | unnumbered, after §1: *Work up to 1997*, *Work since 1997* |
| Summary of results and open questions | — | §8 |
| PGL(3) appendix | Appendix B, §§B.1–B.7 | Appendix A, §§A.1–A.7 |
| PGL(3) equations | (B.1)–(B.4) | (A.1)–(A.4) |
| Observation, Table | Observation B.2, Table B.1 | Observation A.2, Table A.1 |
| Glossary | Appendix A | unnumbered, after Appendix A |
| Revision notes | Appendix C | this log |
| New example | — | Example 2.5 |

All other section, result, remark and equation numbers are unchanged. For the concordance with the **1997** numbering, see C.2 of the former Appendix C below.

### Moved from the Acknowledgments

The Draft 1 Acknowledgments read, with numbers resolved:

> *2026:* The 2026 revision benefited from two referee reports on drafts of it, prepared with the help of AI models. The first was written with Claude (Anthropic). The second was written by ChatGPT (OpenAI) at the first author's request, and we thank it for a careful and useful report. The counterexamples in Remarks 2026.1 and 2026.4, the correction to the SL(2) example in §6.2, the insistence that Casselman's input in higher rank be treated as an essential hypothesis, and the request for a detailed rank-two example (which led to the checks of Lemmas 3.5A–C and to Appendix B) all come from it.

("Appendix B" here is now Appendix A.)

### Former Appendix C

Reproduced from Draft 1, converted from LaTeX by script. Section, result and remark numbers are those of Draft 1, so "Appendix B" is now Appendix A and "§8" is now the unnumbered literature review. The LaTeX math is written as `$…$`. The conversion has not been proofread against the Draft 1 PDF.

### Revision notes and concordance with the 1997 version (former Appendix C)

This appendix records the history of the paper and how the 2026 version differs from the 1997 one. § C.1 summarizes the substantive changes and the status of each main result; § C.2 is a concordance from the 1997 numbering to the 2026 text; § C.3 records, by location, what the 1997 text said where it has been corrected. The item-by-item list of corrections is in the file `CHANGES.md`.

#### C.1 About this revision

We give the history of the text, list the substantive changes, and tabulate the status of each main statement as of November 2026.

**History.** The paper was published in Pacific J. Math. **154** (1992), 103–129 [Jo92]. In October 1997 a corrected and extended version was circulated; it added §2.5 on $(G,M)$-families, Proposition 3.7, §4.1, Proposition 4.3 and all of §5 (the 1997 footnotes recording this are merged into this paragraph). This 2026 version is built from a literal transcription of the 1997 text and its errata log (both in `original-1997/`).

**What changed.** Typos, misquoted normalizations and wrong references have been corrected silently; they are listed item by item in `CHANGES.md`. The substantive changes are:

1. the constant and the chamber in Macdonald's formula (Lemma 2.1) and the $\delta_P^{1/2}$ factor in Casselman's asymptotics (Lemma 3.3);
1. Lemma 3.5 is replaced by Brion's vertex decomposition (Lemma 3.5A);
1. Proposition 3.6 is restated as "vertex terms plus a $T$-independent remainder" and given a new, direct proof (the 1997 inductive argument did not control the $T$-independent remainder);
1. Proposition 4.2 and Theorem 4.5 are restated: $I(\chi,\phi)$ is defined as the $T$-independent part of the truncated kernel, and the spectral identity is proved under an explicit regularity hypothesis (R);
1. an example (§6.2, $SL(2)$) shows that (R) can fail and that the spectral side then needs atoms; the 1997 claim that $I(\chi,\gamma)$ is a rational function is corrected accordingly (Conjecture 4.6);
1. §5 is updated: the fundamental lemma is a theorem, and the 1997 closing question becomes the conditional Proposition 5.2;
1. following a second referee report: the standing hypothesis is semisimple $G$ (more generally, anisotropic center), as in 1992 (Remark 2026.1); Lemma 2.8 holds only when the coroot lattice is saturated (Remark 2026.4); Casselman's input (C) is stated explicitly; the combinatorics of Proposition 3.6 is proved in full (Lemmas 3.5B, 3.5C) and checked in rank two; and (R) is proved for $PGL(2)$ (Lemma 6.1A);
1. a computation on the building of $PGL(3)$ (Appendix B) shows that (R) fails in rank two even when $Z(G)$ is connected, while the conclusion of Theorem 4.5(b) still holds there. This leads to the weaker hypothesis (R$'$) of Remark 2026.20, and Conjecture 4.6(b) no longer asserts (R).

New material: worked examples for $PGL(2)$ and $SL(2)$ (§6), the derivation from Arthur's local trace formula ("Route B", §7), a literature review before and after 1992 (§8), a glossary (Appendix A) and the $PGL(3)$ computation (Appendix B).

**Status.**

| Statement | Status (November 2026) |
|---|---|
| Truncated identity, Theorem 4.5(a) | proved, for $G$ satisfying (H) |
| Brion decomposition, Lemmas 3.5A–C | proved; checked for $SL(3)$, $PGL(3)$ |
| Vertex decomposition of $J^T$, $I^T$ (Props. 3.6, 4.2) | proved in rank one; in rank $\ge2$ conditional on Casselman's input (C); (4.7A) confirmed for one $\gamma$ in $PGL(3)$ (App. B) |
| Spectral identity, Theorem 4.5(b) | proved under (C) and (R); holds numerically for one $\gamma$ in $PGL(3)$, where (R) fails (App. B) |
| Hypothesis (R) | proved for $PGL(2)$ (Lemma 6.1A); fails for $SL(2)$ (§6.2) and for $PGL(3)$ (App. B) |
| Weaker hypothesis (R$'$), Remark 2026.20 | proposed; consistent with the $PGL(3)$ data |
| $SL(2)$ atom, Proposition 6.4 | proved, all $q$ |
| Shape of the spectral measure, Conjecture 4.6 | verified for $PGL(2)$, $SL(2)$; numerically for one $\gamma$ in $PGL(3)$; open in general |
| $\kappa$-spectral measure, $\kappa$ of order $n$, Prop. 5.1 | proved (from the fundamental lemma); normalizations checked for $SL(2)$ |
| $\kappa$-spectral measure, general $m\mid n$, Prop. 5.2 | conditional on a stable Theorem 4.5 for $H_m$ |
| Lemma 2.8 | proved when $\mathbb{Z}\Delta^\vee$ is saturated; false for $PGL(2)$ |
| Route B (§7) | proposed route; normalizations not checked |

The numerical checks are `examples/pgl2/pgl2_check.py`, `examples/sl2/sl2_check.py`, `examples/rank2/brion_check.py` and `examples/pgl3/pgl3_check.py` (run all with `python3 run_checks.py` at the top of the repository).

#### C.2 Concordance with the 1997 version

The table below tells a reader of the 1997 version where each of its results went.

Section, equation and result numbers are those of 1997 (new items carry letters or the numbers 6.$n$, 7.$n$). The item-by-item disposition of the errata log `transcription_log.md` is in `CHANGES.md`. In summary:

| 1997 | 2026 |
|---|---|
| Lemma 2.1, 2.2 | corrected constant $Q_G$ and chamber (Remark 2026.3) |
| Lemma 2.4, Cor. 2.5, Remark 1 | $[W_M\backslash W]$; "irreducible" deleted; direct-sum statement |
| §2.5 (Lemmas 2.6–2.9) | kept in place, notation fixed; explanatory role only |
| (3.1), Lemmas 3.2–3.4 | opposite parabolic, $\delta_P^{1/2}$, $A^-_P(\epsilon)$, new proof of 3.2 |
| Lemma 3.5, (3.5)–(3.6), Remark 6 | replaced by Lemma 3.5A |
| (3.7), (3.8) | $Q_a\in\mathbb{Q}$; (3.8) via Lemma 3.5A |
| Prop. 3.6, proof (3.9)–(3.23) | 2026 statement and proof (Remark 2026.10) |
| §4.1, (4.1), Lemma 4.1 | omitted (unverified, unused); see Remark 2026.12 |
| Prop. 4.2, 4.3 | 2026 form; $I(\chi,\phi)$ = $T$-independent part |
| Theorem 4.5 | (a) unconditional, (b) under (R); new Conjecture 4.6 |
| (4.10), (4.11) | Weyl discriminant, measures fixed |
| §5 | rewritten: (5.1)–(5.4A), Props. 5.1–5.2 |
| — | new: §§6–8 (examples, Route B, literature), Apps. A, B |

#### C.3 Notes on corrections, by location

The body of the paper describes the mathematics as it now stands. This subsection records, by location, the corresponding statements of the 1997 version (and of the first 2026 draft, where a referee report led to a change) that were corrected. Typographical corrections are listed only in `CHANGES.md`.

- **§1, before (1.1)** The 1997 text said "Ad-finite" for "compactly generated support modulo conjugation".
- **§1, after (1.5)** The explicit formula (1.5) was to be the subject of [Jo97], announced in 1997 as "in preparation" but never written up.
- **§1** The 1997 version asserted that $dI_\gamma=I(\chi,\gamma)\,d\mu(\chi)$ with $I(\cdot,\gamma)$ a rational function, for every $G$. This is false for $SL(2)$ (§6.2).
- **Remark 2026.1 (scope)** The first 2026 draft allowed arbitrary reductive $G$, with $G(F)^1$ in place of $G(F)$; a referee pointed out the $GL(2)$ counterexample. The 1992 paper also assumed (H).
- **§2.0** Notation: the 1997 text used $\Delta^\vee$, $\hat\alpha$, $\alpha^\wedge$ and $R^\wedge$ for overlapping objects; wrote $\fa_B$ or $\cA_{A,\mathbb{R}}$ for $\fa_0$; wrote $X_M$, $X^M$ with the subscripts interchanged in one place; wrote sums "over $W/W_M$" that should be read over $[W_M\backslash W]$; and gave three different, ill-typed definitions of $\chi_\lambda$.
- **§2.1** The 1997 text wrote $\ip{\alpha^\vee,\beta}=2\delta_{\alpha\beta}$ (the left side is the Cartan matrix), and used the lattice $\{\lambda:\lambda(\hat\alpha)\in\mathbb{Z}\}$ in (2.6), which is correct only for adjoint $G$ and has the wrong scaling; it also conflated $\Th$ with $\Thu$.
- **Remark 2026.2 ($c_\alpha$)** The 1997 text printed $q_{\alpha/2}^{+1/2}$ in the first factor of $c_\alpha$.
- **Remark 2026.3 (Lemma 2.1)** The 1997 statement read $\Gamma_\chi(a)=Q^{-1}\delta_B^{1/2}(a)\sum_wc(w\chi)(w\chi)(a)$ for all $a\in A(F)$, with $Q=\sum_w(IwI:I)$: the constant was inverted and the formula was stated for all $a$, with the coefficient belonging to the opposite chamber. With $Q=1+q$, Plancherel inversion fails for $PGL(2)$ (the diagonal entries become $q$).
- **Remark 1** The 1997 text said that $r_{M,G}\circ i_{G,A}(\chi)$ is always semisimple.
- **§2.5** The 1997 text said this subsection was "not needed". Its Lemma 2.9 attached an index $r$ to the family and left a dangling $P$ on the right.
- **Remark 2026.4 (Lemma 2.8)** The first 2026 draft stated Lemma 2.8 without the saturation hypothesis; a referee supplied the $PGL(2)$ counterexample.
- **Remark 2026.6 ((3.1))** In 1997, (3.1) used the Jacquet module for $P$ instead of $\bar P$ in the second slot, omitted $\delta_P^{1/2}(a)$, and did not make $\epsilon$ depend on the level.
- **Lemma 3.2** The 1997 proof argued that the pairing is "of the form $\sum a_{w,w'}\ip{z_w,z'_{w'}}_0$" for any bilinear form, and then derived a contradiction from an inequality that $M$-invariance does not forbid.
- **Remark 2026.7 (Lemma 3.3)** The 1997 statement paired $R_MT_wf$ with $R_MT_wf'$ for arbitrary $f,f'$, omitted $\delta_P^{1/2}(a)$, was stated on $A^-(\epsilon)$, and had $c(w\chi)$ where $c((w\chi)^{-1})$ belongs. The factor $w^G_\ell w^M_\ell$ in the 1997 text (log item 3.61) presumably comes from Waldspurger's opposite-parabolic conventions.
- **Remark 2026.8** The 1997 text asserted that $T$ can be chosen with $\nu_A^{-1}(\cA_A(T)^c)\subset A^-(\epsilon)$.
- **Lemma 3.5A** Lemma 3.5A replaces the 1997 Lemma 3.5, which was false.
- **Remark 2026.9 (Lemma 3.5A)** The 1997 Lemma 3.5 asserted that the $\omega$-th term carries the factor $\prod_\alpha\chi(a_\alpha)^{T_\alpha}$ times a $T$-independent function (false already for $SL(2)$), and used the coordinates $\ip{a,\alpha}$, unimodular only for adjoint $G$.
- **(3.7)** The 1997 text wrote $Q_a\in\mathbb{Z}$.
- **(3.8)** The 1997 formula (3.8) used the incorrect Lemma 3.5.
- **Remark 2026.10 (Proposition 3.6)** The 1997 Proposition 3.6 claimed $J^T=\sum_{w,w'}C^T(\chi,\chi',w,w')\ip{T_wu,T_{w'}u'}_G$ with coefficients independent of $u,u'$, computable from Lemma 3.5. Its inductive proof ((3.9)–(3.23) of 1997, via the functions $\xi(M,D,T,U)$ and Langlands' combinatorial lemma) shows only that $J^T-F(T)=J^U-F(U)$ for an explicit $F$, which leaves a $T$-independent constant undetermined, and the structural claim for arbitrary $u,u'$ is unsupported (log items 3.46, 3.69). The 2026 proof keeps the same ingredients but replaces the induction on Levi subgroups by a direct partition of the dominant cone and Brion's theorem.
- **§4.1** The 1997 §4.1 defined $Q^T(\chi,\chi',w,w',\phi)=\tr[T_w^*T_{w'}\pi_\chi(\phi)]\,C^T(\chi,\chi'^{-1},w,w')$, with $C^T$ the coefficients of the 1997 Proposition 3.6, and asserted (Lemma 4.1) that, suitably normalized, these form a $(G,A)^\sim$-family. Lemma 4.1 was not verified, and the present argument does not use it, so the subsection is omitted. Its purpose was to show that the singularities of the vertex terms cancel in the sum over $P$; Remark 2026.12 explains why that is not enough. A referee's suggestion (M8(b): smoothness of the $(G,A)^\sim$-sum plus the Riemann–Lebesgue lemma) does not suffice for the same reason.
- **Proposition 4.2(a)** The 1997 proof expanded $\pi(g)\Phi_{K,\chi}$, whose level grows with $g$, and had $u_j^*$ in place of $u_j$ in (4.7).
- **Proposition 4.2(b)** The first 2026 draft argued by confluence, passing to the limit $\chi'\to\chi^{-1}$.
- **Remark 2026.11 (Proposition 4.2)** The 1997 Proposition 4.2 stated $I(\chi,\phi)=\lim_{\chi'\to\chi}\sum_{w,w'}Q^T(\chi,\chi',w,w',\phi)\tilde\theta(w\chi/w'\chi')^{-1}$ "independent of $T$" (with $Q^T$ as in the note on §4.1), justified by "follows from Proposition 3.6"; that justification does not apply. It also claimed $G$-admissibility of $\phi\mapsto I(\chi,\phi)$.
- **Remark 2026.13 (Theorem 4.5)** Part (a) is the first line of the 1997 Theorem 4.5. Its second line, with $I(\chi,\phi)$ "independent of $T$", rested on the unsupported claim noted for Proposition 4.2. The first 2026 draft expected (R) to hold whenever $Z(G)$ is connected; Appendix B shows that it fails for $PGL(3)$.
- **Remark 2026.14 (Conjecture 4.6)** The first 2026 draft of Conjecture 4.6(b) also asserted that (R) holds when $Z(G)$ is connected.
- **(4.10)** The 1997 text wrote "$\Delta(t)^2\,\mathrm{meas}(T(F))$" in one line and not in the next, and used $T$ for these tori.
- **§5** §5 was added in 1997 and has been rewritten. The 1997 computation (5.3) wrote $f$ for $\phi$ in the integrand, and its sign conventions for $\kappa$ were inconsistent; its (5.2)–(5.4) integrated over $S(F)\backslash G'(F)$ although the integrand lives on $G(F)$; it described $H_m$ as $\mathrm{Res}_{E/F}(GL(m)/E)$ and, for $m=n$, as "an elliptic Cartan of $GL(n)$"; and it called the fundamental lemma a conjecture (it was one in 1997). Proposition 5.2 answers, conditionally, the question with which the 1997 version closed.
- **Remark 6.2** That $I(\cdot,\gamma)$ is not locally integrable against $d\chi$ may explain why the 1992 abstract called it a "distribution" while the 1997 text called it a "rational function".
- **Remark 6.3** The constant $|B_r|$ is the remainder $J_G$ that the 1997 induction could not produce; the second term has the shape predicted by the 1997 Proposition 4.2.
- **§6.2** The first 2026 draft used $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ for all $q$; a referee pointed out that it is split when $q\equiv1\bmod4$.
- **Throughout** Section and result numbers follow the 1992/1997 version; items new in 2026 carry letters (Lemma 3.5A, §2.1A, Example 2.3A) or the numbers 6.$n$, 7.$n$. Citations follow the 1997 bibliography with 2026 labels; the original paper is [Jo92].

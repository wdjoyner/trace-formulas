# Draft 4 revision log — November 11, 2026

## Aim

Extend Draft 3 from compact induction at the standard vertex stabilizer
\(K^{(0)}=\mathrm{SL}_2(\mathcal O_F)\) to the second \(\mathrm{SL}_2(F)\)-vertex orbit
\(K^{(1)}=D K^{(0)}D^{-1}\), with \(D=\mathrm{diag}(\varpi,1)\).

## Mathematical changes

1. **Two maximal compact vertex stabilizers.** Introduced \(v_0,v_1\),
   \(K^{(0)},K^{(1)}\), their pro-\(p\) radicals, the two integral unramified elliptic tori
   \(T^{(0)},T^{(1)}\), and explicit identifications of the finite reductive quotients
   with \(\mathrm{SL}_2(\mathbb F_q)\). These stabilizers are not \(\mathrm{SL}_2(F)\)-conjugate.
2. **Additional splitting assumption.** Assumed an independent continuous homomorphic
   splitting \(s_1:K^{(1)}\to\widetilde G\) in addition to \(s_0\). This is an explicit
   hypothesis, **not** asserted automatically for arbitrary extensions. The proof does
   not claim conjugation by \(D\in\mathrm{GL}_2(F)\) lifts to \(\widetilde G\).
3. **Mixed-splitting lemma.** On the pro-\(p\) intersections
   \(K^{(i)}_+\cap xK^{(j)}x^{-1}\), conjugated splittings agree because continuous
   homomorphisms to the prime-to-\(p\) center \(\mu_n\) vanish. The two lifts of
   \(-I\) coincide and are central when \(n\) is odd.
4. **Cross-orbit theorem (Theorem 7.5).** For both \(i,j\in\{0,1\}\) and every
   \(t\in(T^{(i)})^{\mathrm{reg}}\), established, conditional on both compact splits,
   \[\Theta_{\widetilde\pi_{j,\theta^{\langle n\rangle}}}(s_i(t^n))
   =\Theta_{\pi_{j,\theta}}(t).\]
   If \(t\) has regular elliptic reduction, the cross-orbit character vanishes.
   If the reduction is central, the common fixed ball meets both vertex orbits.
5. **Complementary character formula (Theorem 7.6).** For \(\rho_i(t)=zI\),
   \(r=r_i(t)\ge1\), the inducing parity changes the leading sign:
   \[\Theta_{\pi_{j,\theta}}(t)
   =\theta(z)((-1)^{r+1+j-i}q^r-1).\]
6. **Two-orbit sum (Corollary 7.7).** For all regular \(t\in T^{(i)}\),
   \[\Theta_{\pi_{0,\theta}}(t)+\Theta_{\pi_{1,\theta}}(t)
   =-\theta(\rho_i(t))-\theta(\rho_i(t)^{-1}).\]
   Near the center the \(q^r\) terms cancel, giving \(-2\theta(z)\). The
   metaplectic analogue follows by summing the two comparison identities.
7. **Expanded \(\mathbb Q_7\) example.** Added second-orbit values \(-8,48,-344\)
   at depths \(r=1,2,3\), opposite to first-orbit values \(6,-50,342\), and
   verified that each sum is \(-2\).

## Internal checks

- Both diagonal and cross-orbit character sums were independently checked by
  summing the \((q+1)q^{d-1}\) vertices on the relevant parity spheres, for
  \(q=7,13,19\) and \(1\le r\le6\).
- The LaTeX source was compiled twice with `pdflatex`; output has 13 pages,
  with resolved internal references and no overfull boxes.
- The final PDF pages were rendered and visually inspected for text overflow
  and page-layout issues.

## Limitations and next checks

- **Cocycle-specific splittings:** For an application to a named Kubota or
  Brylinski–Deligne cover, give an explicit reference or construction for the
  splitting over \(K^{(1)}\) and check its chosen normalization.
- **No new classification:** The ordinary two-orbit sum is consistent with
  classical Sally–Shalika and more recent endoscopic character literature;
  no originality claim has been established.
- **Excluded:** exceptional quadratic parameters, ramified elliptic tori,
  positive-depth supercuspidals, full stable character relations and a
  fundamental lemma.
- **External refereeing encouraged:** In particular, independently verify
  Lemma 7.3 (mixed splitting) and Theorem 7.5 (cross-orbit identity).

---

# Draft 5 revision log — November 11, 2026

## Aim

Revise Draft 4 in response to the referee report by Claude (Anthropic).
The revision was prepared by Argon (Gemini); a short list of corrections
by Claude was applied afterwards as a separate commit.

## Changes made by Argon (commit "draft 5 ... as received")

1. **Splittings are now a proposition, not a hypothesis.** Proposition 1.1:
   the cover splits uniquely over \(K^{(0)}\) and \(K^{(1)}\), by
   Hochschild–Serre and the vanishing of
   \(H^1,H^2(\mathrm{SL}_2(\mathbb F_q),\mu_n)\).
2. **Unified two-orbit exposition.** \(v_i,K^{(i)},T^{(i)},s_i,\rho_i\) are
   introduced at the start; the one-orbit theorem and its separate proof
   are gone. Main results are Theorems 1.2 (direct identity and \(n\)-th
   power identity) and 1.3 (explicit formulas and packet sum).
3. **Role of the power map stated plainly** (Remark 1.4): the preimage of
   \(T^{(i)}\) is abelian, so the \(n\)-th power identity is the direct
   identity composed with an automorphism; the split torus is named as the
   first real test.
4. **\(\mathrm{GL}_2\) interpretation of the packet sum** (Remark 5.1).
5. **Citations for the Frobenius character formula**, a literature review
   section, a glossary and symbol index; draft-history language removed
   from the body.

## Corrections applied by Claude after review (second commit)

- Proof of Prop. 1.1: Schur multiplier statement restricted to odd
  \(q\ge5\) (it is false at \(q=4\)); noted why the Ext term vanishes.
- Remark 5.1: \(\sigma_\theta\) must first be extended to a cuspidal
  representation of \(\mathrm{GL}_2(\mathbb F_q)\); the "index 2" statement
  replaced by the correct double-coset statement; the intermediate
  arithmetic in the displayed sum corrected (the total \(-2\theta(zI)\) was
  already right).
- Open problem (i): removed the suggestion to use Jacquet modules of
  supercuspidals (they vanish). Open problem (iii): ramified tori fix an
  edge, not just its barycenter.
- Reference [Bl92] corrected to Blondel, Mém. SMF 18 (1985).
- Introduction: \(zI+\varpi^rA\) changed to \(zI(I+\varpi^rA)\) to match
  Lemma 4.2; abstract no longer calls elements reducing to \(-I\)
  "topologically unipotent"; typo "Moveover".
- Layout: Table 1 and the symbol index no longer overflow the margins;
  the source now compiles with no overfull boxes (19 pages).

## Not yet verified

- Pinpoint citations: Howard–Weissman Prop. 2.3 and Thm. 3.5;
  Sally 1988 Thm. 1.9 and Eq. (1.10); Bushnell–Henniart "Appendix A, §A.3,
  Thm. A.4" and §19; Bonnafé Table 5.4; Digne–Michel §15.9;
  Cunningham–Gordon §2.3 Eq. (2-6). These should be checked against the
  sources before the paper is circulated.
- Remark 5.1's statement that the Sally–Shalika/Aubert–Plymen characters
  near the identity are \(-1\pm f(t)\) with \(f(t)=(-1)^rq^r\) agrees with
  Theorem 1.3 but has not been compared line by line with those papers.

---

# Style-revision Draft 2 — November 12, 2026

## Scope and provenance

This is **Draft 2 in the editorial/style-revision sequence**, made on top of the mathematics recorded above as Draft 5 (November 11, 2026). The title-page draft number is deliberately 2. The manuscript filename remains `character_relations_depth_zero.tex`, per Section 9 of `joyner-math-paper-style-guide.md`; Git history records the change. The original notes date from approximately **2000**, whereas the companion published paper [Jo99] appeared in 1999. No theorem is represented as a new theorem of this editorial revision.

The instructions governing this revision explicitly **prohibited changes to mathematical statements, hypotheses, proof steps, status labels, and existing labels**. Accordingly, all 29 original `equation` environments and all existing theorem, proposition, lemma, proof, and remark environments were compared literally with the original source and are unchanged. Every one of the 50 original `\label` identifiers and every existing `\cite` key is retained. Existing semicolons were not removed; the preference against semicolons was applied only to new prose. There were no `definition` theorem environments in the source; substantive concepts newly explained in the background are accompanied by concrete examples. The pre-existing mathematical Drafts 4 and 5 log entries above are preserved without modification.

## Baseline before edits (GitHub blob `bacb69bf03a29afd6a95df7ccd49722973b705f8`)

The original source was fetched from `main`, byte-for-byte verified against the referenced Git blob, and compiled twice with `pdflatex` on November 12, 2026. **Both passes succeeded.** The baseline PDF was 19 pages, US Letter, with no compilation errors, undefined references, or overfull boxes. The second-pass TeX log reported **four underfull-box warnings** (two around lines 180–181, one around lines 198–200, one around lines 513–514). The source used `mathptmx`, already had a literature review and glossary, but lacked an early background and notation section, a summary of results, and distributed concrete examples.

## Changed material: complete editorial inventory

1. **Preamble.** Retained the `article` document class and the existing 12pt US Letter/one-inch geometry settings. Replaced `mathptmx` by `newtxtext,newtxmath`; added T1 font encoding and `microtype`. Added `\numberwithin{equation}{section}` to comply with the style guide. Retained all pre-existing theorem definitions and math macros.
2. **Title and date.** Retained the original title. Added the subtitle text **“Draft 2”** and **“Corrected and expanded version”**. Set the date line to **“Original draft: 2000. Corrected and expanded draft: 2026”**, with the revision date November 12, 2026.
3. **Author line and original-manuscript provenance.** Kept the same three listed authors and their order, **David Joyner, Argon, and ChatGPT**. Added the required email `wdjoyner@gmail.com` and a `\thanks` footnote identifying the notes of approximately 2000 and the published companion.
4. **Abstract opening.** Reworded only the opening AI-disclosure sentences to remove first-person informal wording and point to the acknowledgments and revision log. The substantive abstract claims are preserved verbatim.
5. **Literature review.** Reordered existing literature summaries into two orienting subsections, **“Foundations through 2000”** and **“Developments after 2000”**; preserved the substance and original `\cite` keys. Moved the treatment of post-2000 sources into the latter subsection and added short context and a pointer to the running example. The introductory section remains first.
6. **Early background.** Inserted `\section{Background}` after the literature review, with orienting subsections on the local field/tree, tame covers/genuine representations, and depth-zero types/character sums. See the separately enumerated mathematical-exposition additions below.
7. **Early notation.** Inserted `\section{Notation}` before the technical body. **Moved**, without changing its entries, the old glossary's **Symbol index** table to this section; the glossary's terminology entries remain at the end. Added an orienting sentence and a running-example explanation of `\mathbb{Q}_7`, `\mathbb{Z}_7`, and `\mathbb{F}_7`.
8. **Section openings.** Added orienting paragraphs at the beginning of the introduction, both new literature-review subsections, all three background subsections, notation, the three main technical sections, the worked-example section, summary, and glossary terminology subsection. The existing introductory sentences and all intervening mathematics remain in place.
9. **Concrete examples.** Added concise examples in the introduction, literature review, all three background subsections, notation, vertex-splittings/types, fixed-ball geometry, character-proof section, open-problems section, and summary. These use the paper's **existing** setting `F=\mathbb{Q}_7`, `q=7`, `n=3` and values already calculated in the original worked example.
10. **End matter.** Preserved the existing worked-example section and the list of open problems, adding only orientation/example prose. Inserted a **Summary of results** section before the glossary. The glossary terminology entries remain unchanged, and the symbol index has moved to notation. Retained the acknowledgments at the end, before the bibliography.
11. **Acknowledgments and provenance.** Replaced draft-history details formerly embedded in the acknowledgments with a concise record of the actual roles of Sol-ChatGPT (earlier drafting and current editorial revision), Argon-Gemini (earlier mathematical preparation and referee report), and Fable-Claude (referee report). Added statements that AI review is **not an independent mathematical certification** and that the revision log gives further details. Earlier detailed history survives in the log above.
12. **References.** The pre-existing BibTeX-style `\bibitem` identifiers and displayed labels already met the `initials + two-digit year` convention. **No bibliographic key, citation, or existing bibliography entry was changed**, and no cross-reference label was deleted.
13. **Scope safeguards.** Did not edit a mathematical statement, proof, hypothesis, status label, theorem environment, equation environment, named mathematical claim, or existing label. Retained all mathematical results under their previous epistemic status. Did not introduce any new mathematical result or add a computer checker.

## Every newly added mathematical exposition/example (for independent refereeing)

Each of the following is newly authored and requires independent mathematical review even though it is intended only to clarify results already proved in the paper. There are **no newly established mathematical results** in this editorial revision.

1. **Introduction:** the `F=\mathbb{Q}_7, n=3, q=7, |\bar T|=8` running-example paragraph; the orienting explanation of two vertex orbits and comparison identities.
2. **Literature review introduction:** the example pointer with `F=\mathbb{Q}_7, n=3`; the two period-specific orienting summaries.
3. **Background / local field and tree:** explanation of valuation, residue field, lattices, and vertex stabilizers; the explicit lattice pair `\mathbb{Z}_7^2`, `\operatorname{diag}(7,1)\mathbb{Z}_7^2` and the 8-regular tree.
4. **Background / covers and genuine representations:** description of tame central extensions, splitting maps and genuine central action; the `p=7,n=3` example contrasting faithful `\mu_3` action with trivial pullback action.
5. **Background / depth-zero types:** exposition of inflation, compact induction and fixed-coset character sums; the `q=7,|\bar T|=8,\dim\sigma_\theta=6,\chi_\theta(I)=6` example.
6. **Notation:** running-example identifications `\OO=\mathbb{Z}_7`, `\kk=\mathbb{F}_7`, `q=7`, `n=3`. The 14-row notation table itself was moved rather than rewritten.
7. **Vertex splittings, finite-field data, and depth-zero types:** explanatory paragraph connecting the splitting proposition to the inducing data; the `\chi_\theta(I)=6` finite-field example for both vertex orbits.
8. **Fixed-ball geometry:** orienting link to compact-induction sums; the sphere sizes 8 and 56 and their opposite/equal vertex-orbit parity at distances one and two.
9. **Character relations and closed formulas:** orienting description of matching fixed-coset sums; the existing depth-one values 6 and -8 and their sum -2, with a pointer to the original worked example.
10. **Worked example:** brief orientation of the existing complete `\mathbb{Q}_7` calculation, without modifying its matrix formulas, table, or proof-related explanations.
11. **Open problems:** explicit contrast between the treated unramified elliptic torus and a ramified elliptic torus, referring back to the original open-problems item about an edge-fixed analysis.
12. **Summary of results:** prose recapitulation of Proposition `prop:unique-splittings` and Theorems `thm:main` and `thm:explicit`; the concrete depth-one 6, -8 and -2 example, with cross-reference to the original table. These statements merely restate pre-existing results.
13. **Glossary opening:** orienting cross-references to the early background and notation; no glossary definition or mathematical terminology entry was substantively changed.

## [DECIDE] defaults and approved exceptions

- **Document class:** retained `article` (existing-file default).
- **Times package:** adopted `newtxtext,newtxmath` (preferred default); no fallback needed.
- **Glossary placement:** end, immediately before acknowledgments (default).
- **AI author line:** retained existing author line and clarified individual roles in acknowledgments (prompt-compatible default).
- **Approved §3.3 exception:** examples are required in substantive mathematical sections, not administrative acknowledgment, bibliography, or glossary sections. The glossary has an orientation paragraph.
- **Approved §§3.6–3.7 exception:** mathematical hypotheses and proof steps were not changed, per the stronger prompt prohibition.
- **Approved §6.1 exception:** any newly discovered mathematical issue must be referred for approval rather than silently fixed.
- **Approved §6.6 exception:** unverified claims remain under their original labels; verification limits are recorded here instead of changing status labels to `Remark 2026.n`.
- **Approved §8.2 exception:** the repository's `revision_log.md` is the authoritative log under its paper-specific §9 rule rather than creating a second LaTeX log.

## Final compilation and limits of verification

On November 12, 2026, the revised source compiled **twice** with `pdflatex`, yielding a **21-page, US Letter PDF**. Second pass: **0 errors, 0 undefined references, 0 overfull boxes, 0 underfull boxes**. The local TeX distribution emitted non-fatal `mathrsfs` font-size-substitution warnings because exact requested sizes were not installed; these did not stop compilation. The title page was visually inspected.

Independently checked mechanically: same original 50 label names, no deleted or renamed bibliography or citation keys, original theorem/proposition/lemma/proof/remark environments byte-for-byte unchanged, all 29 original displayed `equation` environments byte-for-byte unchanged, full reference resolution, section numbering, and PDF dimensions. This is **not an independent mathematical referee report**. The original source's pinpoint citations were not checked against the printed referenced works in this editorial pass; the unverified Howard–Weissman, Sally, Bushnell–Henniart, Bonnafé, Digne–Michel, Cunningham–Gordon and Sally–Shalika/Aubert–Plymen pinpoint claims listed above remain **unverified**. No computational script was rerun because no mathematical result was modified or newly asserted. Every new explanatory mathematical passage above is explicitly flagged for a subsequent referee.

## Old-to-new concordance (all changed labels)

All original label names are preserved and references were compiled. The following gives every original numbered label whose displayed number changes; unchanged labels are omitted. Original equations were globally numbered, while Draft 2 numbers equations within sections. Blank lines separate unchanged-section and renumbered-section groups only for readability.

| Label | Old number | Style Draft 2 number |
|---|---:|---:|
| `eq:cover` | 1 | 1.1 |
| `eq:coprime` | 2 | 1.2 |
| `eq:D-def` | 3 | 1.3 |
| `eq:Ki-def` | 4 | 1.4 |
| `eq:Ki-plus` | 5 | 1.5 |
| `eq:si-def` | 6 | 1.6 |
| `eq:Ti-def` | 7 | 1.7 |
| `eq:Tbar-def` | 8 | 1.8 |
| `eq:theta-power` | 9 | 1.9 |
| `eq:central-sign` | 10 | 1.10 |
| `eq:pi-defs` | 11 | 1.11 |
| `eq:direct-identity` | 12 | 1.12 |
| `eq:main-identity` | 13 | 1.13 |
| `eq:explicit-far` | 14 | 1.14 |
| `eq:explicit-near` | 15 | 1.15 |
| `eq:packet-sum` | 16 | 1.16 |
| `sec:types` | 3 | 5 |
| `lem:splittings-compat` | 3.1 | 5.1 |
| `eq:pro-p-compat` | 17 | 5.1 |
| `eq:center-pro-p-compat` | 18 | 5.2 |
| `prop:finite` | 3.2 | 5.2 |
| `eq:elliptic-finite` | 19 | 5.3 |
| `eq:central-finite` | 20 | 5.4 |
| `eq:unipotent-finite` | 21 | 5.5 |
| `prop:types` | 3.3 | 5.3 |
| `sec:tree` | 4 | 6 |
| `eq:sphere-count` | 22 | 6.1 |
| `lem:power` | 4.1 | 6.1 |
| `eq:ri-def` | 23 | 6.2 |
| `lem:anisotropic` | 4.2 | 6.2 |
| `eq:leading-expansion` | 24 | 6.3 |
| `prop:ball` | 4.3 | 6.3 |
| `eq:fixed-ball` | 25 | 6.4 |
| `eq:conj-matrix` | 26 | 6.5 |
| `sec:proofs` | 5 | 7 |
| `eq:frobenius-ordinary` | 27 | 7.1 |
| `eq:frobenius-genuine` | 28 | 7.2 |
| `rem:GL2-packet` | 5.1 | 7.1 |
| `rem:discriminant` | 5.2 | 7.2 |
| `sec:example` | 6 | 8 |
| `eq:tr-Q7` | 29 | 8.1 |
| `sec:open` | 7 | 9 |

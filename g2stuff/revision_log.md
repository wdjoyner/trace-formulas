# Revision log: on the transfer of Shalika germs for G₂

This log accompanies `revised/g2-shalika-germs-2026.tex`. It records the drafts of the 2026 revision, the AI usage, which results are original and which are new, the verification levels, and the sources that could not be consulted. It follows `../joyner-math-paper-style-guide.md`, Sections 6, 8 and 9.

Files in the git history track the drafts. File names carry no draft number (style guide, Section 9).

## Drafts and stages

| Draft | Date | What | Record |
|---|---|---|---|
| 0 | 2026-11-13 | Literal amsart transcription of the summer 1994 manuscript, referee report (Claude), and verification scripts | `original-1994/`, `transcription/`, `referee/`, `scripts/` (PR #15) |
| 1 | 2026-11-13 | Corrected and expanded edition: every item of the referee report addressed or flagged; Theorems 6.1, 7.2, 8.3 restated as conditional germ identities; new Propositions 3.4A, 3.7, Table 4.3A, Table A.6; literature review, summary, glossary | `revised/g2-shalika-germs-2026.tex`, `revised/CHANGES.md` |

**Source variants.** The body follows `g2new5.tex` and `g2new9.tex`. The variants `g2new5d.tex` (one parenthetical sentence in the proof of Lemma 5.14 and one word in §5) and `g2new9d.tex` (hypotheses (4) and (6) of Conjecture 9.1, and a closing sentence) are described in Remark 2026.40 and in the transcription. It is not known which version is later.

## AI usage

- **Claude (Anthropic, Opus 5.5)**, co-author.
  - As referee, it wrote the referee report on the 1994 manuscript (`referee/g2_referee_report.tex`).
  - As co-author and reviser, it made the transcription and drafted Draft 1: the corrections, the new statements and proofs, Remarks 2026.1–2026.44, the literature review, summary, glossary and acknowledgments, and `revised/CHANGES.md`.
  - It wrote and ran the verification scripts in `scripts/`.
  - It checked some bibliographic entries against publisher and arXiv records (see below).
- **D. Joyner** wrote the 1994 manuscript, directed the revision, and is responsible for the final text.

AI review is not an independent certification of the results. No second, independent referee has read Draft 1.

## Verification levels

As in the referee report:
- **L1**: checked here, by hand or by an exact computation whose script is in `scripts/`.
- **L2**: checked against a secondary account (for example a machine summary of a source), not the source itself.
- **L3**: taken on trust from a source that was not consulted.

| Item | Level | How |
|---|---|---|
| Patch formulas of §3, Igusa forms of §4, (7.3), (7.4), (8.1), (8.4), (8.5) | L1 | `g2_patch_jacobians.py` (SymPy) |
| Regularity of the twelve patches (Proposition 3.4A) | L1 | `g2_patch_regularity.py` |
| Covering up to codimension 2; branches and Igusa constants (Table 4.3A) | L1 | `g2_toric_divisors.py` |
| Normality of Z (Proposition 3.7): 658,651 lattice points | L1 | `g2_saturation_full.py` |
| Singular faces of the fan; candidate exceptional divisors (Remark 2026.23) | L1 | `g2_exceptional_divisors.py` |
| H¹(F,T) and endoscopic roots for all elliptic tori (Table A.6) | L1 | `g2_tori_endoscopy.py` |
| Lemma 3.5 (new proof), Lemma 3.6, Lemma 5.6, Lemma 4.4 for G₂, A.5 | L1 | by hand |
| Lie(Z(H)) = 0 and centralizers are Levi subgroups (Remark 2026.29) | L1 | by hand |
| Count of étale cubic algebras (Remark 2026.44) | L1 | by hand |
| Hales' descent in [Ha89] and the explicit SO(4) computation | L2 | machine summary only |
| [Ha92a] Ch. I, II, V, VI (cocycle t_*, θ = 1, Dynkin lines, Prop. 9.1) | L3 | quoted from 1994 |
| [Ha92b] Lemma 6.1 (Lemma 5.19) | L3 | not consulted |
| [La83] Lemma 2.12 and the principal value formulas | L3 | not consulted |
| Corollary 8.8 (normalizations in (0.1), Formula 0.6 and [GH16]) | L3 | not checked in detail |

## Original and new results (style guide, rule 6.5)

**Original (1994), kept with corrections:** §0: Conjecture 0.0A (Matching of germs, from [LS89]), Lemma 0.4, Formula 0.6, Lemma 0.8 (now with a proviso). §1: Lemmas 1.5, 1.12, 1.21, Corollary 1.6, Definition 1.16 (corrected), (1.8)–(1.22). §2: Lemmas 2.10, 2.15, (2.1)–(2.17). §3: the patch construction, Conjecture 3.4, Lemmas 3.5 and 3.6 (corrected), Notation 3.3d. §4: the patch list, the Igusa forms (corrected), Table 4.3 (corrected), Lemma 4.4 (corrected). §5: Lemmas 5.6, 5.7, 5.10, 5.14 (now a hypothesis), 5.17, 5.19 (as quoted). §§6–8: Lemma 6.4, the computations (6.2)–(6.5), (7.1)–(7.5), (8.1)–(8.7). §9: Conjecture 9.1 (restated). Appendix A.1–A.7.

**Restated:** Theorems 6.1, 7.2 and 8.3 are now conditional germ identities (Remarks 2026.29, 2026.31, 2026.34, 2026.36). Lemma 3.7 is now Proposition 3.7 (for G₂) and Conjecture 3.7A.

**Removed:** the decomposition f = f₁ + f₂ before Lemma 5.19; the sentence "spurious divisors do not contribute" in Lemma 5.14; the complete-intersection claim of Lemma 3.7; the untypeset material after `\enddocument` in four source files.

**New in 2026:**
- Statements: Conjecture 0.0 as stated, Definition 1.3, Proposition 3.4A, Proposition 3.7, Conjecture 3.7A, Hypotheses (X_r) (Remark 2026.29), Corollary 8.8.
- Tables and figures: Table 4.3A, Table A.6, the Dynkin curve figure.
- Proofs: Lemma 3.5, Lemma 5.6, Proposition 3.4A, Proposition 3.7, Corollary 8.8, A.5, A.6.
- Sections: the literature review, the notation table, the summary of results and open problems, the glossary.
- Remarks 2026.1–2026.44.

**Numbering.** The 1994 numbering is kept. New items carry letters or follow the last 1994 number of their section, so no concordance is needed.

## Sources that could not be consulted, or were not checked (style guide, rule 4.3)

- [Ha92b] (Hales, U(3)): Lemma 6.1, the source of Lemma 5.19, was not consulted.
- [Ha89] (Hales, GSp(4)): consulted only through a machine summary (L2).
- [Ha92a] (Hales, subregular germ): all quoted results are taken from the 1994 text (L3), including the formula t₁t_σ = α^∨(ξ) in the proof of Lemma 5.17 (Remark 2026.28).
- [La83], [LS83]: the principal value formalism and [La83, Lemma 2.12] are quoted, not checked (Remark 2026.33).
- [As98]: the count of F-classes in the subregular class could not be compared with Assem's (Remark 2026.44).
- [SV00]: cited for the triality theorem without checking the exact formulation (Remark 2026.41).
- [Ha92a], [Ha89]: the 1994 claims that Conjecture 3.4 is known for A_n and C_n, and false for D_n, were not checked (Remark 2026.15).
- The two works cited only in `g2new9d.tex` as [A] and [H4] are not identified.
- **Bibliography.** Checked in the referee report against publisher or library records: [Ra72], [Ro80], [She89], [Ha89], [Ha92b], [La83], [LS83]. Checked in this draft against publisher or arXiv records: [As00], [Ts15]. The data for [As98], [GH16], [Wa97], [Ng10], [Wa01], [De02], [Ha94] are as recorded during the referee report. The remaining entries carry over the 1994 data with page ranges and publication details added from standard references; they have not been individually checked.

## Next steps (for Draft 2)

1. Compute Δ₀(X) and the fiber integrals I_E(X,u), and prove (X₂) directly (the most promising case).
2. Recompute the exponents e_σ in (8.7) with the short roots of H₁.
3. Choose a toric resolution of Z (for example with Sage's `ToricVariety.resolve()`) and settle the proviso of Lemma 0.8.
4. Show that the β = 11/3 contribution vanishes.
5. Add worked examples to §§1–4 (style guide, Section 6), which Draft 1 has only in §§0, 1 and 3.
6. Ask an independent referee to read Draft 1.

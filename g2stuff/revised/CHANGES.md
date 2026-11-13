# Changes from the 1994 manuscript

Companion to `g2-shalika-germs-2026.tex` (Draft 1). Prepared by Claude (Anthropic) for D. Joyner, 2026-11-13.

For each item of the referee report [`../referee/g2_referee_report.tex`](../referee/g2_referee_report.tex), this file records what Draft 1 does with it. "R n" refers to **Remark 2026.n** in the paper. Those remarks mark every substantive change and everything not fully verified.

**Dispositions:**
- **fixed**: corrected silently in the text
- **fixed (R n)**: corrected, with a remark
- **conditional (R n)**: the statement is kept, but now depends on a stated hypothesis
- **open (R n)**: the gap is stated, not closed
- **removed**: deleted

Numbering of sections, equations and results is the 1994 numbering. Items added in 2026 carry letters (Conjecture 0.0A, Proposition 3.4A, Table 4.3A, (4.2A), Conjecture 3.7A) or new numbers at the end of a section (Corollary 8.8). So no concordance table is needed.

## The Remarks 2026.n

| R | Where | Topic | Kind |
|---|---|---|---|
| 1 | §0 | The matching is now known (Waldspurger, Ngô, Gordon–Hales) | context |
| 2 | §0 | Langlands' steps 1–3 and the definition of S″ | correction |
| 3 | §0 | Lemma 0.8: the new proviso on other branches | gap stated |
| 4 | §1 | Definition 1.3: a well-defined φ | new definition |
| 5 | §1 | (1.8): sign conventions | correction |
| 6 | §1 | Definition 1.16 of S″ | correction |
| 7 | §1 | (1.18) | correction |
| 8 | §1 | (1.22): w(γ), w(ζ); eight functions on a 7-dimensional variety | correction |
| 9 | §2 | The cocycle condition | correction |
| 10 | §2 | Normalization of (2.8) | correction |
| 11 | §2 | The Dynkin curve (new figure) | new |
| 12 | §2 | (2.11)–(2.14) are schematic; z should be read as −z | gap stated |
| 13 | §3 | Patch formulas (three misprints; fifth patch redundant) | correction, verified by script |
| 14 | §3 | The regular branch is E_Δ, not E_∅ | correction |
| 15 | §3 | Conjecture 3.4: claims for A_n, C_n, D_n not checked | unverified |
| 16 | §3 | Lemma 3.5: Σ_{Δ−S₁} for Σ_{S₁}; new proof | correction |
| 17 | §3 | Lemma 3.6: ρ ≥ σ, and the comparability hypothesis | correction |
| 18 | §3 | Lemma 3.7 becomes Proposition 3.7 (G₂) and Conjecture 3.7A; complete intersection claim withdrawn | correction |
| 19 | §4 | Redundancy among branches: seven branches in all | correction |
| 20 | §4 | Observation (II): valuation argument, no proviso needed | simplification |
| 21 | §4 | Igusa forms: w(ε), w(ζ) denominators; β = 11/3, not 10/3 | correction, verified by script |
| 22 | §4 | Lemma 4.4: rank ℓ, "3-regular", meaning of "induced" | correction |
| 23 | §4 | Exceptional divisors of a toric resolution; β = 2 example | gap stated |
| 24 | §5 | Renamed symbols (υ, c_f, q^{−N}, k) | readability |
| 25 | §5 | Lemma 5.7: principal-part index; proof still a sketch | correction |
| 26 | §5 | Lemma 5.10(c): the chain of classes | correction |
| 27 | §5 | Lemma 5.14: four gaps; treated as a hypothesis | conditional |
| 28 | §5 | Lemma 5.17: H¹ not always cyclic; "(5.10)" misreference | correction |
| 29 | §5 | **The main gap**: Lemma 5.19 does not apply; Hypotheses (X_r) | conditional |
| 30 | §6 | E_{∅,α,γ} = E_α: two β = 2 divisors, not three | correction |
| 31 | §6 | Theorem 6.1 restated as a germ identity, conditional on (X₁) | conditional |
| 32 | §6 | Lemma 6.4: reworded argument | readability |
| 33 | §6 | (6.5b) prefactor; fiber forms not rechecked; choice of E_α or E_β | correction; unverified |
| 34 | §7 | Theorem 7.2, conditional on (X₂); quadratic tori not treated | conditional |
| 35 | §7 | (7.3), (7.4): corrected differentials and coefficient | correction, verified by script |
| 36 | §8 | Theorem 8.3, conditional on (X₃); short-reflection S₃ tori not treated | conditional |
| 37 | §8 | The roots of H₁ = PGL(3) are the short roots | correction |
| 38 | §8 | (8.1), (8.4), (8.5), (8.6) | correction, verified by script |
| 39 | §8 | Corollary 8.8: (X_r) hold a posteriori, given Gordon–Hales | new; level 3 |
| 40 | §9 | Conjecture 9.1 restated; variant g2new9d | correction |
| 41 | A.2 | k×j = −i; the bilinear form; triality for rotations | correction |
| 42 | A.5 | Endoscopic groups: new argument | correction |
| 43 | A.6 | All elliptic tori (Table A.6); the 1994 computations | correction, verified by script |
| 44 | A.7 | Rao's lemma for an odd grading; 6 or 8 classes, not 7 | gap stated |

## Major issues of the referee report

| Issue | Disposition |
|---|---|
| 1. Hales' reduction lemma does not apply | **conditional (R 29, 31, 34, 36).** Lemma 5.19 is kept as quoted, with the exponent 2(r − \|Σ_H^+\|). Its use is replaced by Hypotheses (X_r), stated precisely in R 29. Theorems 6.1, 7.2 and 8.3 are conditional on them. Corollary 8.8 shows that (X_r) holds, given Gordon–Hales; a direct proof is the main open problem. |
| 2. The support hypotheses are never satisfied | **fixed (R 29, 31).** The theorems are now germ identities; the decomposition f = f₁ + f₂ is removed. An equivalent formulation with μ_{O′}(f) = 0 is noted. |
| 3. The roots of PGL(3) | **fixed (R 37, 42).** Σ_{H₁}^+ = {α, γ, δ}. The long-root pseudo-Levi SL(3) is used only for coordinates on O₃. The exponents in (8.7) must be recomputed (open). |
| 4. Missing elliptic endoscopic data | **fixed in A.6 (R 43); open in §§6–8.** Table A.6 lists all elliptic tori. The quadratic and short-reflection S₃ tori are not treated in Theorems 6.1, 7.2, 8.3 (R 31, 34, 36). |
| 5. Which divisors contribute | (a) **fixed (R 30).** (b) **fixed (R 21).** (c) **open:** the β = 11/3 term must cancel (§4, after Table 4.3A). (d) **open (R 23, R 3):** exceptional and spurious divisors are the proviso of Lemma 0.8. The gaps in Lemma 5.14 are **conditional (R 27).** |
| 6. The X-dependence and the measures | **partly fixed (R 35, 38); open.** The forms (7.3), (7.4), (8.1), (8.4), (8.5) are corrected and checked by script. The exponents f_σ, e_σ in (7.5), (8.7) and the factor Δ₀(X) are not computed; that is (X₂), (X₃). |
| 7. Lemma 3.5, Lemma 4.4 and the "regular branch" | **fixed (R 14, 16, 22).** Lemma 3.5 has a new proof. |
| 8. The definition of S″ and Y″ | **fixed (R 2, 6).** |
| 9. Lemma 3.7 and the singular locus | **fixed (R 18, 23).** Proposition 3.7 for G₂ (saturation script and Hochster); Conjecture 3.7A in general; the complete-intersection claim withdrawn. |
| 10. Section 1 foundations | **fixed (R 4–8).** |
| 11. Section 2 computations | **fixed (R 9–12)**, with (2.11)–(2.14) marked schematic. |
| 12. The appendix | **fixed (R 41–44)**, except that Assem's count is not reconciled (R 44, open). The untypeset weighted Dynkin diagrams are dropped (they remain in `../original-1994/g2newapp.tex`). |

## Minor issues of the referee report

| Location | Item | Disposition |
|---|---|---|
| §0 | T′_G ∩ {1} | fixed |
| §0 | Property (e) | fixed |
| §0 | Δ(γ_H, γ_λ) with Φ(γ_G, f) | fixed |
| §0 | "lemma 5.18" | fixed |
| §0 | \|D_H\| | fixed |
| §0 | "Langland's" | fixed |
| §0, §3 | "Cohen-Macauley" | fixed |
| §0 | Lemma 0.8 "proven in §§4–5" | conditional (R 3) |
| §0 | "blowing up four times" | removed; replaced by the toric resolution (§3, R 23) |
| §1 | "Lemma 1.2 below"; tag (1.3) | fixed (Definition 1.3) |
| §1 | [Sp3] | removed |
| §1 | Lemma 1.21 imprecise | reworded |
| §2 | "§1.1"; X⁰ | fixed |
| §3 | \off prints O_F | fixed |
| §3 | three patch misprints | fixed (R 13) |
| §3 | Lemma 3.6 | fixed (R 17) |
| §3 | Conjecture 3.4 claims | unverified (R 15) |
| §3 | [Sp] | removed |
| §4 | doubled ∧ | fixed |
| §4 | w(ε), w(ζ) | fixed (R 21) |
| §4 | Lemma 4.4 "3-regular" | fixed (R 22) |
| §4 | Observation (II) | fixed (R 20) |
| §5 | Lemma 5.10(c) | fixed (R 26) |
| §5 | Lemma 5.7 index | fixed (R 25) |
| §5 | Lemma 5.17 references | fixed (R 28); the source of ξ in [Ha92a] not checked |
| §5 | Lemma 5.19 exponent | fixed (R 29) |
| §6 | E_{∅,α,γ} = E_α | fixed (R 30) |
| §6 | (6.5b) prefactor | fixed (R 33) |
| §6 | E_α or E_β "depending on T_G" | open (R 33) |
| §6 | exp(\bar F X) | fixed (O_F) |
| §7 | Σ_{O₃} in (7.3); exponent 3/2 | fixed (R 35); the exponent is explained, its normalization not justified |
| §7 | F-rationality of E_{∅,α,δ} | fixed (it is the only branch on Z with β = 3) |
| §8 | (8.6) \|λ\|³ | fixed (R 38) |
| §8 | "conjecture 3.4 (which we proved in §3)" | fixed (Proposition 3.4A) |
| §9 | variant g2new9d; [A], [H4] | noted (R 40) |
| A.6 | s_ζ not simple | fixed (R 43) |
| untypeset | "Lemma 9.1", duplicate "Lemma 1.21" | removed (untypeset text not carried over) |
| throughout | spelling | fixed |

## Other changes

- **Front and back matter** (style guide §§2–3, 6): new title block with the subtitle "Draft 1. Corrected and expanded version", authors David Joyner and Claude, the date line "Original draft: 1994. Corrected and expanded draft: 2026", an abstract with an AI disclosure, a literature review split at 1994, a notation table, a summary of results and open problems, a glossary, acknowledgments and a corrected bibliography. The old USNA address is removed.
- **Bibliography.** Ranga Rao is pp. 505–510; Rogawski [Ro80] is the Compositio paper; Shelstad's title is "A formula for regular unipotent germs"; page ranges added. New entries: [As98], [As00], [De02], [GH16], [Ha94], [Ng10], [SV00], [Ts15], [Wa97], [Wa01]. Uncited entries of 1994 ([Mu88], [Sp69]) are dropped.
- **Untypeset text** after `\enddocument` in four source files (the comparison with H-side subregular germs after §6, the "Igusa forms on Y₁" after §4, the weighted Dynkin diagrams after the appendix, and material after §2) is not carried over. It remains in `../original-1994/` and, switchable, in the transcription.
- **Scripts.** `../scripts/g2_patch_jacobians.py` gains the §7 checks for (7.3) and (7.4).

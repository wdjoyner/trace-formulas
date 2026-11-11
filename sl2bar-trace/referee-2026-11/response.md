# Response to the referee report of November 2026 (ChatGPT)

Report: [`report-chatgpt.md`](report-chatgpt.md), on `revised/preview.tex` and Sections 2–6 as of 2026-11-11.
Response by D. Joyner and Claude. Statement numbers are those of the revised `preview.pdf` (75 pages).

We thank the referee. The main objection is correct and has been repaired. Every claim in the report was checked independently before acting on it; the outcome is below.

## Summary

| Report item | Verdict | Action |
|---|---|---|
| 1.1 Kubota's cocycle is not continuous | Correct | Lemma 2.1 rewritten; topology defined intrinsically; new Example 2.A, Lemma 2.2(i) |
| 1.2 "(w,1)² acts trivially" | Withdrawn by the referee; we agree with the withdrawal | Sentence expanded so the scope is explicit |
| 1.3 e₃(g,1) is not locally constant | Correct | Test-function spaces redefined (§2.1.4, §2.2, §3.1) |
| §3, proof of Lemma 3.1(c): "continuous ⇒ open kernel" | Correct | Proof replaced (no-small-subgroups argument) |
| §4, coefficients a^G(S,u_ξ) defined, not computed | Accepted | Stated in Theorems 4.11, 5.16, 6.11 and in §1.3 |
| §5, b versus b′ | Accepted, and settled | New Lemma 5.7; Theorem 5.8(c) now says V_b ≅ r⁺_{ψ_{−b}} |
| §6, real factors only for sgn^ε | Accepted | New Lemma 6.6(c) |
| §6, bad-place factors imported | Accepted | Three-way distinction added in §6.2; theorem statements qualified |
| §6, "every term explicit" | Correct, an overstatement | Replaced by a precise statement |
| M(w,0) = −1: explain the zero and the generation step | Accepted | Proof of Proposition 6.13 rewritten in four steps |
| Editorial 1–6 | Accepted | Section 1, roadmaps, Glossary, Appendix A, "Status of the results" subsections |
| Overfull line | Fixed | It was in Lemma 3.5 (Section 3), not in Section 2 |

## 1. Correctness

**1.1 (continuity of the cocycle).** The referee is right, and the example is right: β(−1, n̄(c)) = (c,−1)_v. More generally β(a(t), n̄(c)) = (c,t)_v, so β is discontinuous at (a(t),1) for every non-square t, over every local field other than ℂ (Example 2.A; this also covers fields such as ℚ₅ in which −1 is a square). Changes:

- Lemma 2.1 now has three parts: (a) β is a Borel cocycle; (b) it is not continuous, but β ≡ 1 on U × U for an explicit open neighborhood U of 1 (U = {a > 0, d > 0} over ℝ, U = K_m over a non-archimedean field); (c) the cover has exactly one group topology in which the sets (V,1), V ⊂ U, are a base of neighborhoods of the identity. Existence is Kubota's and Moore's theorem (Mackey's in general); that their topology has this description is proved (a local section of a covering is a local homomorphism, and near 1 every element is a square).
- The pairs (g,ζ) are called Borel coordinates throughout. Lemma 2.2(i) lists the sections that *are* continuous and are the only ones used analytically: on N and its conjugates, on A, on K_m, and k ↦ (k,κ(k)) on K.
- The adelic cocycle is no longer called continuous. The adelic cover carries the quotient topology of the restricted product (§2.2, "Topology").

**1.3 (test functions).** Correct, including the example: e₃(k_j,1) = κ₃(k_j) = (−1)^j while k_j → −1. C_c^∞ of a cover is now the space of smooth compactly supported anti-genuine functions *on the topological group*; for p < ∞ this is bi-invariance under the image of some K_m. The text says explicitly that g ↦ f(g,1) need not be continuous, and uses e_p as the example. Section 3 is changed the same way. One refinement to the report: for the split torus the old and new definitions agree, because a ↦ (a,1) is continuous on A (the Hilbert symbol is locally constant); for anisotropic tori, e.g. SO(2), they do not. Later sections needed no change beyond wording: they use the coordinates only to integrate and to restrict to the sections of Lemma 2.2(i).

**1.2.** We agree with the referee's own correction. The statement is in Lemma 6.6(a), at a finite non-dyadic place with unramified data, where (w,1)² = (−1,1) is central, lies in A(𝒪_v)\*, and acts by π_v(−1,1) = 1. The proof now says this, and says that it would fail at a real place and that part (b) does not use it.

## 2. Additional points

**Lemma 3.1(c).** The kernel of a continuous character need not be open. New argument: a neighborhood W of 1 on which |χ̄ − 1| < 1 contains the image of ∏_{v∉S} T(𝒪_v)\*, a subgroup, whose image in ℂ^× lies in the disc |z − 1| < 1 and is therefore trivial.

**b versus b′ (Theorem 5.8(c)).** Now settled: **b′ = −b**. New Lemma 5.7 computes the action of the cover of A in the Weil representation ω_{ψ′} (normalized by n(u) ↦ ψ′(ux²)) directly in Kubota's model: ω(a(t),ζ)φ(x) = ζ·χ_{ψ′₋₁}(a(t),1)·|t|^{1/2}φ(tx). The proof writes a(t) as a product of unipotent lifts, which act without ambiguity, and finds the sign (−1,t)_v from the cocycle. Comparing constant terms gives V_b ≅ r⁺_{ψ_{−b}}. Two independent confirmations are in `checks/sec5_n2_check.py`: the cocycle identity at v = ∞, 2, 3, 5, 7, and the weight ½ of the ground state at the real place. Example 5.B was corrected accordingly (the Gaussian is e^{−2πξ²} in this normalization). With the other common normalization, n(u) ↦ ψ′(½ux²), the statement reads V_b ≅ r⁺_{ψ_{−2b}}.

**Real normalizing factors.** Lemma 6.6(c): a general unitary χ_v = sgn^ε|·|^{iτ} is the twist π_{v,iτ}, and all formulas hold with λ + iτ in place of λ; r_v = √2·e^{iπm₀/2}·L_v(2λ,χ_v²)/L_v(2λ+1,χ_v²). For k = ℚ, τ_∞ = 0; for other fields it need not be.

**Existence, explicit formula, global compatibility.** These are now separated in §6.2. Existence is Theorem 6.5 and is all the construction uses. Explicit formulas hold outside S_bad(μ). Compatibility is automatic: for any local choices M = m·R_S and m has the properties of Corollary 6.7(b); but m is a known function only up to the factors at S_bad(μ). Theorem 6.11 and the paragraph after it now say exactly which terms depend on the two unevaluated ingredients (a^G(S,u_ξ) and the bad-place r_v) and which do not. We added pointers to Szpruch and Goldberg–Szpruch for local coefficients and Plancherel measures on covers of SL(2); we have **not** derived r_v at the dyadic places from them.

**M(w,0) = −1.** The proof is now in four steps: the zero of 1/ζ_k^{S}(2λ+1) at λ = 0 kills every Whittaker coefficient (the character is squared in the denominator, so every ramified class sees the pole of ζ_k); E equals its constant term; N(𝔸) and N̄(𝔸) generate G(𝔸), by bounded elementary generation of SL(2) over fields and local rings, so |F| is constant; homogeneity under A forces F = 0.

## 3. Readability

1. *Overview.* New Section 1: overview with the final formula, literature review, a table of what is proved and what is cited, and conventions.
2. *Notation table.* Glossary at the end (notation and terms); φ_A and Φ_A are distinguished there and in the new opening of Section 6.
3. *Running example.* §1.4 collects k = ℚ, S = {∞, 2} with pointers to the examples in each section.
4. *Historical corrections.* All comparisons with the 1995 notes and the 1997 manuscript were moved out of Sections 2–6 into Appendix A, organized by statement.
5. *"What rests on citation".* Every section now ends with a subsection "Status of the results"; Sections 2 and 3 gained the citation remark they lacked.
6. *Invariance.* Section 6 opens with "Why a correction term, and why this one".

Also: a roadmap and a table of objects at the start of Section 4, and a diagram at the start of Section 5.

## 4. Points where we differ from the report, or that remain open

- The overfull box was in Section 3 (the last sentence of Lemma 3.5), not in the proof of the local Iwasawa decomposition. Two overfull boxes under 0.5 pt remain.
- The referee could not run the checks. They are in `revised/checks/`; all pass (sec2: 114, sec3: 35, sec4: 19, sec5: 50, sec6: 33). They are evidence, not proofs.
- Not done: the coefficients a^G(S,u_ξ); explicit r_v at dyadic and ramified places; "T ≥ 0 suffices" on the spectral side (Remark 2026.13); Section 7 (stable form).
- Renumbering caused by this revision: Section 5 statements from 5.7 on move up by one (old Theorem 5.7 is 5.8, …, old Theorem 5.15 is 5.16); Section 5 equations from (5.5) on move up by two; Examples 2.A, 2.B are now 2.B, 2.C; Remarks 2026.n are renumbered (old 2026.2 is in Appendix A).

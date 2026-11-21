# Referee report on Draft 2 by Claude

Notes prepared by Claude (Anthropic) for David Joyner, November 21, 2026.
Draft 2 of "A hitch-hiker's guide to genuine invariant distributions on metaplectic covers of SL(2) over a p-adic field", refereed for correctness first and readability second. The report also assesses Gemini's report (`report-gemini.md`) item by item.

Theorem numbers follow the compiled Draft 2. Line numbers refer to the Draft 2 `.tex` source.

**Corrections after the report was written.** Two points below were later found to be wrong and are marked "Correction" in place: item 9 of the new issues (the unipotent section), and the advice to move the notation table. See also `../revision_log.tex`, Draft 3 section.

## Summary and recommendation

Recommendation: major revision. The main logical chain in Section 8 is sound. Section 3.2 and Section 6 have five substantive errors, and three of them are not in Gemini's report.

What is correct and well done:

- The paper is honest about its status. Unverified claims are flagged, and the algebraic factorization (Proposition 8.3, Lemma 8.5, Theorem 8.6) is kept apart from the conditional topological statement (Theorem 8.8).
- The proof of Theorem 8.8 is correct under its stated hypotheses. Lemma 8.10 (the Schwartz lemma on a torus) is correct: the exponent condition 2N − κ > d and the Laplacian signs both check out.
- The cocycle formula in Section 3.1 is correct. The two expressions for β agree, using (−1, c)ₙ² = 1.
- Lemma 5.1 and the discriminant computation in Section 5 are correct.
- The draft compiles cleanly with pdflatex (18 pages, no errors, no undefined references), compiled with mathptmx substituted for newtx.

The five substantive errors:

1. Harish-Chandra's Ξ is defined incorrectly. As written, the integral collapses to δ_B(x)^(−1/2) (line 246).
2. The bilinear pairing of Lemma 6.3 is not well defined for n > 2, because the contragredient of a genuine representation is not genuine. This is the root cause of the sesquilinearity problem that Gemini found in Lemma 6.4.
3. Proposition 6.6 and Corollary 6.7 are missing the hypothesis that the unitary part of the inducing datum is Weyl-fixed.
4. Theorems 6.9 and 6.10 leave out the irreducible I(χ) with χ^w = χ when n is even.
5. The endpoint conflict in Remark 6.8 can be settled. The Langlands quotient theorem for covers gives ker T = π_sp and im T = π_nt, which supports the later 2026 draft over the 1994 conjecture.

## Assessment of Gemini's report

I agree with almost all of Gemini's report and recommend adopting it. I disagree on one point ("|x| large" in K(μ)). Two points I accept only in part. One finding should be moved earlier, to Lemma 6.3.

Corrected item numbers. Gemini's "Theorem 6.9" ("the special representation") is Theorem 6.10, and its "Theorem 6.8" is Theorem 6.9. Its "Theorem 8.5" is Theorem 8.6, and its "Theorem 8.7" (the "compactsmooth" typo) is Theorem 8.8. Its "Lemma 8.8" is Lemma 8.10, and its "Remark 8.9" (the case n = 1) is Remark 8.11.

| Gemini item | Verdict | Comment |
| --- | --- | --- |
| Sesquilinear vs bilinear (Lemma 6.4, Cor. 6.7); define T = T_w₀ | Agree, and extend | The defect starts in Lemma 6.3, where the bilinear pairing is already ill-defined for n > 2 (new issue 2). Fix 6.3 with a sesquilinear pairing, and 6.4 and 6.7 then follow. |
| μ(x) = μ₀(x)\|x\|^s written on F^× | Agree | μ lives on the cover. Write μ(h̃(x)) for a fixed section h̃ on C, and record how genuineness on μₙ fixes the rest. |
| I(μ) used for I(χ_μ) | Agree | One sentence defining I(μ) := I(χ_μ) is enough. |
| K(μ)(ii): scalar χ(h(x),1) vs the ν-dimensional χ_μ | Agree | Condition (ii) must use μ and a shift in the Ā-variable, not a scalar factor. |
| K(μ)(ii): "\|x\| large" should be "small" | Disagree | K(μ) is the noncompact (line) picture f(x,a) = φ(w̄⁻¹u_x, a), not the Kirillov model. By the Bruhat identity w₀u_x = h(1/x) u(−x) u⁻(1/x), φ(w₀u_x) behaves like \|x\|⁻¹ μ(h̃(x))⁻¹ φ(1) as \|x\| → ∞. So "large" is correct. The Kirillov remark applies only after the Fourier transform f^∧. |
| δ in V(μ)(ii) should be δ_B^(1/2) | Agree | This matches §6.1, and makes the integrand of Lemma 6.3 have weight δ_B = \|a\|². |
| Unmatched parenthesis after Lemma 6.3 | Agree | Line 467. |
| A^n vs A^ν | Agree | On the diagonal, β(h(a),h(b)) = (b,a)ₙ, so the commutator of the lifts of h(a) and h(b) is (a,b)ₙ^(−2). The center of Ā is therefore the preimage of A^ν. The parameter space (§3.2) and the restriction in §8.1 should both use A^ν. |
| Ind typo in §8.1 | Agree | Line 651. |
| Algebraic dual = continuous dual on C_c^∞ | Agree | C_c^∞(Ḡ) has countable dimension, and the inductive-limit topology is the finest locally convex one. Say so once in §8.2, and Theorem 8.6's caveat can shrink to one clause. |
| "Laplacian sign error" (Lemma 8.10) | Partly agree | There is no sign error, as Gemini itself concedes. The surviving point is minor: W acts on each unramified circle by inversion z → z⁻¹, which is an isometry. |
| "the special representation" (Thm 6.10) | Agree | Already for n = 2 there are several special representations: the odd Weil representations, one for each square class. Write "a special representation". |
| n = 1 in Remark 8.11 vs n > 1 in §3.1 | Agree | One clause is enough. |
| Typos (compactsmooth, froms, centre, corps, non-Archimedean, Théorie, intégrales, "an d×d") | Agree | All verified as present in the source. |
| \rm, \it, Ind, diag in §8.1; F vs \F | Agree | §8.1 is the only section still in 1994 TeX style. The source has 9 instances of SL(2,F) and 7 of SL(2,\F). Drop the \F alias. |
| Uncited bibitems: Ar81, Be75, Da99, HC84, Jo88, JM00, Me98, Cl26, Vi81 | Agree | The list is exact. Cite Vi81 at Remark 5.3 and Cl26 in the Acknowledgments. Remove the others unless a real use exists. |
| \verify macro and commented notes | Agree | The macro is defined but never used. Commented notes at lines 431, 480, 492, 702 and 949. Lines 431 (Moen's exception) and 480 (sesquilinearity) carry real content and should become text. |
| Replace "2026d" with [Cl26] | Partly agree | Remove the internal label. But Cl26 is Claude's October 2026 review notes on the 2000 paper. If the "2026d" draft is a separate document, give it its own bibitem. |
| Soften the opening of §8 | Agree | Line 615 says "We classify", which conflicts with Remarks 8.1 and 8.2. |
| Move the §4 notation table | Correction: disagree | The style guide (§2, item 5) puts notation near the beginning, so keep the table where it is and trim the duplication instead. |

## New mathematical issues

Items 1–5 are errors that change statements. Items 6–10 are smaller corrections or easy improvements. None of them appear in Gemini's report.

### 1. Harish-Chandra's Ξ (§3.2, line 246)

δ_B is extended to G by δ_B(bk) = δ_B(b), so it is right K₀-invariant. The defining integral therefore collapses:

```latex
\int_{K_0}\delta_B(xk)^{-1/2}\,dk \;=\; \delta_B(x)^{-1/2}.
```

The result is not bi-K₀-invariant and grows along B, so the seminorms υ_k are wrong as written. The intended function is the spherical matrix coefficient of the unitary principal series I(1):

```latex
\Xi(x)=\int_{K_0}\delta_B(kx)^{1/2}\,dk .
```

### 2. The pairing in Lemma 6.3 is ill-defined for n > 2

For φ ∈ V(μ), conditions (i) and (ii) give φ((1,ζ)g, a) = ζ·φ(g, a). A product φ₁φ₂ of two such functions therefore picks up ζ². It is then neither a function on B̄\Ḡ nor on Ā/C̄ unless ζ² = 1, that is, unless n ≤ 2.

The conceptual reason: the contragredient of a genuine representation has central character ζ → ζ⁻¹, so no genuine I(μ^w) can be the contragredient of I(μ) once n > 2.

Suggested fix: use the sesquilinear pairing ⟨φ₁, φ₂⟩ = ∫∫ φ₁ φ̄₂. It pairs I(χ_μ) with its Hermitian dual I(χ_μ'), where μ' = (μ̄)⁻¹ is genuine again. For real exponents with a Weyl-fixed unitary part, μ' agrees with μ^w (up to conjugation by Ā), which recovers Aritürk's setting. Lemma 6.4 and Corollary 6.7 then go through with the Hermitian form.

### 3. Proposition 6.6 and Corollary 6.7 lack a Weyl-fixed hypothesis

For SL(2) itself, I(μ₀|·|^s) with real s ∈ (0,1) is unitarizable only when μ₀ = 1 (when μ₀² ≠ 1 it is not even Hermitian). The analogue on the cover is that the unitary part χ_(μ₀) must be W-fixed, and s(μ) must be real.

### 4. Gap in Theorems 6.9 and 6.10 for n even

Proposition 6.1(a) says I(χ) is irreducible for every unitary χ when n is even. Both theorems list principal series only with χ^w ≠ χ, and the "reducible" item occurs only for n odd. So the irreducible I(χ) with χ^w = χ and n even appears nowhere. Fix: "χ^w ≠ χ, or n even".

### 5. The endpoint conflict in Remark 6.8 can be resolved

For Re s > 0, the integral defining T_w converges, and its image is the Langlands quotient of I(χ_μ). Its kernel is the unique irreducible subrepresentation. At the reducibility point, the Langlands quotient is the non-tempered constituent and the subrepresentation is square-integrable. Hence

```latex
\ker T_{w_0}\simeq\pi_{sp},\qquad \operatorname{im}T_{w_0}\simeq\pi_{nt}.
```

So the later 2026 draft is right, and the 1994 conjecture describes the operator in the opposite direction, I(μ^w) → I(μ). Sanity check at n = 1: I(|·|) contains the Steinberg representation as a subrepresentation and has the trivial representation as its quotient, and T kills Steinberg. The Langlands quotient theorem for covers is in Ban–Jantzen, Glas. Mat. 48 (2013) 313–334. The one thing left to confirm is that s = 1/n is the reducibility point in the paper's normalization of s.

### 6. Remarks 5.2 and 5.3(a) can be proved

Remark 5.2 follows from the commutator (a,b)ₙ^(−2). On C = ϖ^ℤ O^(×ν) the commutator vanishes, and (·,·)ₙ² = (·,·)_ν is nondegenerate on F^×/F^(×ν), a group of order ν². A subgroup of index ν on which it vanishes is therefore maximal. Remark 5.3(a) is elementary: split the integral over A^ν\Ḡ into a finite sum over A^ν\Ā and an integral over Ā\Ḡ. When a is not central in Ā, b → [b,a] is a nontrivial character of Ā/A^ν, and the inner sum vanishes. For 5.3(b), cite Vi81.

### 7. Π(C̄)_u is not a compact torus (§8.1, line 643)

It is a countable disjoint union of circles, and Remark 8.1 itself speaks of "each circle". The torus X in Lemma 8.10 is then one circle per component.

### 8. Characters are anti-genuine (line 263)

Since π(1,ζ) = ζ, the character satisfies Θ_π((1,ζ)x) = ζΘ_π(x). By the paper's definition (f(g,ς) = ς⁻¹f(g,1)), this is anti-genuine. It is the product f·Θ_π that is μₙ-invariant.

### 9. Splitting over unipotents and K₀ (line 227)

Correction: the report originally said that u → (u,1) is not a homomorphism on the lower unipotent subgroup. That is wrong. There β = (A, A/(A−1))ₙ with A = (c₁+c₂)/c₁, which is 1 by the Steinberg relation, and the same holds on every conjugate of N₀ (checked exactly in `../scripts/genuine_torus_check.py`). Draft 2's statement is correct, and only the one-line reason should be added.

For the splitting over K₀ when p ∤ n, cite Kubota or KP84 rather than Ge76, which treats n = 2. The splitting is not k → (k,1).

### 10. Smaller corrections

- Line 224: w₀ has order 4, so "need not have order two" should read "does not".
- Line 545: irreducible tempered implies unitary is a general fact, not a case-by-case check.
- Line 273: PW_t is defined as the image of the trace transform, so "⊂ PW_t" in Theorem 8.6 is an equality.
- Line 484 (Lemma 6.5): J_μ is a matrix, so the statement should refer to the image of T_w₀. The range 0 ≤ Re s includes Re s = 0, where the integral does not converge.
- Example 8.12 says the conditional Theorem 8.8 "implies" the Plancherel statement, and duplicates Example 9.1. Merge them.
- Line 399: check that [Jo98] really classifies the supercuspidals for all p and n.
- Li12: the arXiv version 1107.1865v3 (November 2024) adds "Corrections pour §4.1". Check whether §§5.4–5.8 depend on §4.1.

## Readability and structure

- Status labels: Sections 5 and 8.1 demote unverified claims to Remarks, but Section 6 keeps unproved, partly wrong statements as Lemma, Proposition and Theorem. Use one convention.
- Proof formatting is mixed; use the amsthm proof environment throughout.
- Duplication: 𝒥 is defined twice (§3.2, §8.2); "C ⊂ A maximal with C̄ abelian" appears twice (§6.2, §8.1); the f(1) example appears twice.
- Notation: elements of Π(Ā) are called characters but are ν-dimensional; Lemma 5.1 introduces h(a) and never uses it; define D(t) := D(pr t).
- Example 6.12 could compute C, the index, and the dimension of χ_μ for F = ℚ₇, n = 3.
- The Introduction's roadmap skips Section 7, and the restriction p ∤ 2n belongs in the Introduction too.
- Literature: add Ban–Jantzen (2013) and Kaplan–Szpruch (arXiv:2206.06905).
- Glossary: "Cocenter" is not used in the body; the label on the unnumbered Glossary resolves to "9".
- Acknowledgments should credit Gemini as referee and Claude for this report, and point to the revision log.
- Title page: align with the style guide ("Draft 3. Corrected and expanded version"; "Original draft: 1994. Corrected and expanded draft: 2026").

## Verification levels

Level 1 (independent derivation): items 1–8 and the corrected item 9. Level 2 (source consulted): Ban–Jantzen (2013), abstract and introduction only; Li (2012), table of contents of the arXiv version. Level 3 (memory): the content of Aritürk, Flicker–Kazhdan and Moen.

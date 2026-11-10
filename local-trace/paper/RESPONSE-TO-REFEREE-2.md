# Response to the second referee report

Report: [`referee-report-2.md`](referee-report-2.md) (prepared with ChatGPT at the author's request, on the version of 2026-11-10 morning).
Response prepared by Claude (Anthropic) for D. Joyner, 2026-11-10.

"R n" refers to the dated **Remark 2026.n** in the revised paper. The referee's two counterexamples are correct, and both are now recorded in the paper and credited to the report (Acknowledgements).

## M1. Semisimple versus reductive — **accepted**

The GL(2) counterexample is correct: for f = 𝟙_{πK} the support of f misses G(F)^1, so f^∨ ≡ 0 although f ≠ 0.

What we changed:
- We restored the 1992 hypothesis as a standing hypothesis (H): G is semisimple, or more generally reductive with anisotropic center (A_G = 1). This still covers the endoscopic groups H_m of §5.
- G(F)^1 is replaced by G(F) throughout.
- (3.3) needs no quotient, and the Weyl integration formula (4.10)–(4.11) needs no A_G.
- Levi subgroups enter only through Macdonald's formula and Casselman's asymptotics, which hold for reductive groups.

The counterexample is recorded in Remark 2026.1, together with a note on what a general reductive version would need.

## M2. Lemma 2.8 — **accepted, and refined**

The PGL(2) counterexample is correct: 1/(1 − z²) has a pole at z = −1, which no L^∨-translate of θ_B produces. The parenthetical "proof" in the earlier draft was also wrong, because a compactly supported η with Σ_r η(λ+r) = 1 cannot be concentrated near 0.

What we changed:
- Lemma 2.8 is now stated under the hypothesis that the coroot lattice is saturated in X_*(A) (e.g. SL(n), simply connected G; also GL(N), the case of [Wa89a]), with a complete proof.
- Lemma 2.9 carries the same hypothesis.
- §7.4 no longer invokes Lemma 2.8; it says explicitly that no general dictionary is claimed.

We note (R4) that the extra hyperplane z = −1 is the same phenomenon that produces the SL(2) atom in §6.2.

## M3. Proposition 3.6 in higher rank — **accepted; partly completed, partly made explicitly conditional**

- **Step 1.** The proof now says explicitly that S_P and E_P depend only on c = c(n), not on T, so the coefficients C^P_{w,w',e} are T-independent.
- **Step 2 (Casselman).** We agree this is an essential input. It is now stated as **(C)** in §3.1. (C) is Casselman's theorem when P = B, so it holds in rank one. For intermediate P it asks for the asymptotic on A^-_P(ε). We could not find this form in the literature, and the obvious reduction to the split center A_M runs into a circularity in the level (R6). Propositions 3.6 and 4.2, and Theorem 4.5(b), are therefore stated as **conditional on (C) in rank ≥ 2**. The introduction and the status table say so.
- **Step 3 (positivity).** This is now a separate **Lemma 3.5C**, with proof. It uses the non-negativity of inverse Cartan matrices and of the off-diagonal Cartan entries.
- **Step 4 (half-open faces).** This is now **Lemma 3.5B**: Brion's theorem for half-open polytopes (via inclusion–exclusion over closed faces and the valuation property), and in degenerate form for characters on the polar divisors (via a one-parameter perturbation ψ e^{εξ}). Lemma 3.5A and Step 3 of Proposition 3.6 now cite these lemmas instead of "standard inclusion–exclusion".
- **Rank-two check.** The new script `examples/rank2/brion_check.py` checks Lemma 3.5A exactly, in rational arithmetic, for SL(3) and for PGL(3), whose dominant cone is not unimodular. It covers both weightings (c = 1 and Macdonald's Q_λ) and the degenerate character ψ = 1. It also confirms that the strict inequalities matter. As the referee suggested, this tests the combinatorics independently. It does not test (C), and a check of Hypothesis (R) on the building of PGL(3) remains to be done.

## M4. Proposition 4.2 — **accepted**

- **Confluence.** The confluence argument is gone. We now apply Proposition 3.6 directly with χ′ = χ^{-1} (which is regular), using the degenerate form of Brion's theorem (Lemma 3.5B(ii)). That form already produces polynomial coefficients. Rationality in χ holds off an explicit finite union of subtori where the degeneracy pattern changes.
- **Introduction.** It no longer says that Proposition 4.2 proves G-admissibility. It says: K-invariance is proved; G-invariance holds under (R) (Corollary 4.5A); G-admissibility is expected but not proved.

## §3 of the report: Theorem 4.5 and Conjecture 4.6 — **accepted**

- **(R) is strong.** The text after Hypothesis (R) now says that it is a strong condition with representation-theoretic content, and that it fails at a reducibility point for SL(2).
- **Functional, distribution, measure.** A new paragraph in §4.3 distinguishes the three:
  - Theorem 4.5(a) gives only a linear functional Λ_φ on Satake transforms.
  - The naive bound grows exponentially in T, so even being a distribution is not automatic.
  - Being a measure is part of Conjecture 4.6(a).
- **§7.4.** Rewritten as "a proposed route to Conjecture 4.6". It lists the three steps that would have to be carried out.

## §4 of the report: worked examples — **accepted**

- **PGL(2).** New **Lemma 6.1A** proves (R) for PGL(2) for arbitrary bi-K_n-invariant φ on the elliptic set, not only for the centered orbital kernels. The proof sorts vertices by branch and depth relative to the fixed-point set of h, uses the fact that this data is locally constant in h, and uses the identity c_α(χ^{-1})ρ/(1−y) = (Q/2)(1 − q^{-1}y)^{-1}.
- **SL(2) scope.** The referee is right that [[0,−1],[1,0]] is split when q ≡ 1 mod 4. §6.2 now uses any γ ∈ SL(2,𝒪) with characteristic polynomial irreducible mod π (depth-zero unramified elliptic), so Proposition 6.4 holds for every q. The specific matrix is used only when q ≡ 3 mod 4, as in the q = 3 checks. The same caveat is added in §6.1.

## §5 of the report: endoscopy — **accepted**

- **Normalizations and (5.11).** The orbital-integral and transfer-factor normalizations are now stated. The fundamental lemma is written first in the Langlands–Shelstad form (5.10), as a sum over the G(F)-classes in the stable class with transfer factors. It is then specialized to (5.11), using Δ(γ_H, x^{-1}γx) = κ(x)Δ(γ_H, γ). A constant c_S now appears explicitly. The sign convention κ versus κ^{-1} is flagged in R15.
- **𝔇(S).** It is now G′(F)/Ḡ(F)S′(F), where Ḡ(F) is the image of SL(n,F) (kernel μ_n(F)), and Ḡ(F) carries the push-forward measure.
- **Ramified κ.** New **Lemma 5.0** shows that ramified κ give Φ^κ_f ≡ 0 for spherical f. The argument conjugates by diag(u,1,…,1) with η(u) ≠ 1. Conjecture 4.6(c) cites it.
- **Proposition 5.1 versus 5.2.** Proposition 5.1 (κ of order n) is marked unconditional. The prose after Proposition 5.2 is now explicitly conditional, and the status table separates the two.

## §6 of the report: readability — **partly accepted**

**Done:**
- "What is proved / conditional / conjectural" summary in §1.
- Status table updated.
- 1997 acknowledgements moved to an Acknowledgements section at the end.
- §7.1–7.4 are now `\subsection`s and appear in the table of contents.
- A pointer suggests reading the §6 examples before §§3–4.

**Not done, deliberately:**
- Reordering sections (literature first, examples before §3).
- Moving the historical errata out of the main text.

The 2026 version keeps the 1997 section, equation and result numbering, because the errata log and `CHANGES.md` are keyed to it. Reordering would break that correspondence. We can produce a reorganized "reader's edition" later if wanted.

## §7 of the report: bibliography — **accepted**

All entries previously marked "not verified" were checked (Ar87, Cl90, Ko80, Ko82, Ko86, LS87, Sa63, OS13), and the flags are removed. OS13 now has pages 664–714.

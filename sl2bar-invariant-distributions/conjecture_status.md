# Conjecture status and theorem-dependency inventory (Draft 2)

Companion to `sl2bar-invariant-distributions.tex`. Theorem numbers are Draft 2 numbers (consecutive within sections). The first column of the table in Section 1 uses the 1994 numbers. The concordance is in `revision_log.md`, Section 9. Notation: F ⊃ Q_p finite with μ_n ⊂ F, ν = n/gcd(n,2), tame means p ∤ n.

Status labels: **P** proved in the paper · **D** deduced in the paper from cited theorems · **C** cited · **K** conditional · **O** open · **U** quoted, not verified.

## 1. The conjectures of the 1994 manuscript

| 1994 item | 1994 formulation | Present statement | Status | Sources | Still open |
|---|---|---|---|---|---|
| Conj. 2.17 | C*(G) is CCR for a finite cover of a reductive p-adic group | Theorem 2.25, unchanged | C (proof outlined) | Kaplan–Szpruch Thm 3.4; Bernstein 1974 | nothing |
| (implicit, §2.3) | Results of Bernstein–Zelevinsky II §2 and Casselman carry over to covers | Lemma 2.31, Prop. 2.32 | C | Kaplan–Szpruch §3 | nothing |
| Conj. 3.3 | n even ⇒ I(σ) irreducible for all unitary σ, all p | Theorem 3.6: true if p ∤ n, or n ≡ 2 mod 4 | C | Moen Thm 1(b); Goldberg–Szpruch Thm 5.2; Szpruch 2019 Prop. 5.5; Luo | 4 ∣ n and p = 2 (Conjecture 10.1) |
| Conj. 3.5 | n odd ⇒ irreducible if σ^w ≠ σ, reducible with two constituents if σ^w = σ | Theorem 3.8 (corrected): reducible iff χ_σ is a nontrivial quadratic character; all p | C | Szpruch 2019 Prop. 5.5; Szpruch 2024 Prop. 1; Luo | nothing |
| Conj. 3.13 | det J_μ = 0 iff μ = ∣·∣^s, s = 1/n | Theorem 3.23 (corrected): T_σ not injective iff χ_σ = ∣·∣; tame | D | 3.14 (Goldberg–Szpruch), 3.15 (Heiermann), 3.12 | wild case; explicit J_μ |
| Conj. 3.15 | J_μ positive definite and I(μ) unitary for 0 < s < 1/n | Theorem 3.25: for each σ_0 with χ_{σ_0} = 1; not unitary for s > 1/n; tame | D | 3.14, 3.15 | wild case |
| Conj. 3.16 | image of J_μ special, square-integrable, spherical; kernel non-tempered | Theorem 3.27 (corrected): kernel special and not spherical; image non-tempered, unitary, spherical; tame | D, part (d) C | 3.15, Ban–Jantzen, 3.12 | ellipticity of the characters; wild case |
| Expectation (1) | π_sp is the only non-cuspidal square-integrable representation | Corollary 3.28: one for n odd, [F^×:F^{×2}] for n even | D | 3.16, 3.3 | — |
| Expectation (2) | π_sp is tempered | Theorem 3.29 | D | — | — |
| Expectation (3) | non-tempered unitary = π_nt and complementary series | Theorem 3.29 | D | 3.15 | wild case |
| Conj. 4.8 | tempered ⇒ unitary; square-integrable ⇒ tempered | Proposition 4.12 | C | Li 2012 §2; Ban–Jantzen | nothing |

## 2. The three Paley–Wiener theorems

| | Admissible (Theorem 5.10) | Unitary (Theorem 5.14) | Tempered (Theorem 5.17) |
|---|---|---|---|
| Test functions | C_c^∞ | C_c^∞ | Schwartz space |
| Domain of the transform | Π_ad | Π_u | Π_t |
| Algebraic or topological | algebraic | algebraic | topological |
| Shape on a principal-series orbit | Laurent polynomial in z | restriction of a Laurent polynomial to ∣z∣ = 1 and to real points | smooth function on ∣z∣ = 1 |
| Relations at reducible points | sum over constituents is the value of the polynomial (PW2) | (U2), (U3), (U4) | none beyond smoothness of the sum |
| Necessity | **P**, all p | **P**, tame | **P** given continuity of the Abel transform |
| Surjectivity onto full induced data and cuspidals | **P**, p ∤ 2n (Lemma 5.4, Theorem 5.10(b)) | follows | **K** |
| Separation of constituents | **C** (BDK for covers, as asserted by Li 2014 §3.4) | **C** | **K** (Li 2012 Thm 5.6.10) |
| Injectivity modulo commutators | **C** (Li 2012 Thm 5.8.10) | same | **K**, outline |
| Restrictions on n, p | none for the statement; explicit list of reducible points needs p ∤ n | p ∤ n | none for the statement |

Key relation between the first two: restriction PW_ad → PW_u is a bijection (Theorem 5.14(b), **P**).

## 3. Dependency inventory

"Uses" lists what the proof needs. "Used by" lists what cites it. See also Figure 2 of the paper.

| Result | Status | Uses | Used by |
|---|---|---|---|
| 2.1 Kubota cocycle | C | Hilbert symbol | everything |
| 2.2 torus cocycle | P | 2.1 | 2.3, 2.7, 2.12, 2.13, 3.3, 3.12 |
| 2.3 splittings, center of the cover | P / C | 2.2 | 3.3, 3.11, 3.12, 4.9 |
| 2.7 center of the torus | P | (H1)–(H3), index formula | 2.8, 2.10, 2.18, 3.3 |
| 2.8, 2.10 the subgroup C_0 | P | 2.7 | 3.18–3.22 (models) |
| 2.12 Weyl action, 2.13 power section | P | 2.2 | 3.1, 3.3, 3.12 |
| 2.18 Stone–von Neumann | P | 2.7 | all of §3, 4.14 |
| 2.22 torus characters | P | 2.18 | 4.14, 5.4 |
| 2.25 CCR | C | Kaplan–Szpruch 3.4 | 2.27 only |
| 2.31, 2.32 geometric lemma | C | Kaplan–Szpruch | 3.10, 3.16, 3.27, 3.29 |
| 3.3 Weyl-fixed data | P | 2.3(e), 2.12, 2.13 | 3.8, 3.16, 3.23, 3.28, 8.x |
| 3.11, 3.12 Gindikin–Karpelevich | P | 2.3(b), 2.2, 2.13 | 3.13, 3.27(c), check of 3.14, 8.x |
| 3.14 Plancherel measure | C | — | 3.16, 3.25 |
| 3.15 rank-one theory | C | — | 3.16, 3.23, 3.25, 3.27, 3.29 |
| 3.16 reducibility | D | 3.3, 3.14, 3.15 | 3.23, 3.28, 3.29, 5.11 |
| 3.23 degenerate points | D | 3.16, 3.15 | 3.25, (U4) |
| 3.24 Langlands quotient | C | — | 3.27 |
| 3.25 complementary series | D | 3.14, 3.15, 3.10 | 3.29, (U3) |
| 3.27 endpoint constituents | D | 3.15, 3.24, 3.12, 3.25 | 3.28, 3.29, (U4) |
| 3.29 unitary and tempered duals | D | 3.15, 3.16, 3.25, 3.27 | 5.14, 5.17 |
| 3.32 pseudo-coefficients | P | Schur orthogonality | 5.10(b) |
| 4.8 vanishing off the center | P | 2.3(f) | 4.14 |
| 4.9(1) image of the Abel transform | P, p ∤ 2n | 2.3(b),(e) | 5.4(b), 4.14 |
| 4.14 character of I(σ) | P | 2.22, 4.13 | 5.4, 5.10 |
| 5.3 Mellin transform on the center | P | — | 5.4 |
| 5.4 PW for principal series | P | 4.9, 4.14, 5.3 | 5.10 |
| 5.10 admissible PW | P (a),(b); C (c),(d) | 5.4, 3.32, Kaplan–Szpruch; BDK, Li | 5.14, 5.11 |
| 5.14 unitary PW | P (a),(b); C (c) | 5.10, 3.29 | — |
| 5.17 tempered PW | P (a); K (b),(c) | 4.9(2), 5.8, 3.29; Li 2012 | 6.2, 6.4 |
| 6.1 circle distributions | P | Fourier series | 6.2 |
| 6.2 dual of PW_t | P | 6.1, Definition 5.16 | 6.4 |
| 6.4 invariant tempered distributions | K | 5.17(b),(c), 6.2, 4.4 | — |
| 6.5 factorization | P | 4.4 | 6.4 |

## 4. What each open item blocks

| Open item | Blocks |
|---|---|
| Conjecture 10.1 (4 ∣ n, p = 2) | Theorem 3.6 for all p; list of reducible points and index set of Theorem 5.17 in that case |
| Wild Plancherel measure for ramified data | Theorems 3.16–3.29 for p ∣ n |
| Remark 2026.3 (χ^n = χ_σ in general) | Remark 8.5 only; Theorems 3.16–3.29 use only the unramified and Weyl-fixed cases |
| Separation property (Problem 10.3) | Unconditional Theorem 5.10(c), 5.14(c) |
| Schwartz theorem (Problem 10.4) | Unconditional Theorems 5.17(b),(c) and 6.4 |
| Lemma 4.9(1) for p ∣ 2n | Lemma 5.4(b), Theorem 5.10(b) in that case |

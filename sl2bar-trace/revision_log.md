# Revision log: metaplectic trace formula for SL(2)

This log tracks every item of the 2026 referee report ([Claude Docs](https://claude.ai/artifact/7MmqhX7GnoJNup9xbb9RNG)) through the revision. Section numbers refer to `original-1995/cctrace_new.tex` as compiled; item numbers match the report.

## Decisions

- **n = 2 only** (decided 2026-11-10). The revision treats the 2-fold cover of SL(2) over a number field k. Several general-n items become moot; they are marked *moot (n = 2)* below. For n = 2, μ₂ ⊂ k always holds, real places occur, and the archimedean covers are Mp(2,ℝ).
- Sections 4–6 are to be presented as Wen-Wei Li's theorems for covers (Li I–IV), specialized to SL(2). The explicit SL(2) formulas are the paper's contribution.
- Unverified claims are kept, marked with a Remark (2026).

## Stages

| Stage | Scope | Status |
|---|---|---|
| 0 | Clean source tree: `cctrac3b.tex` from `book7d.tex`, remove Scientific Word macros, `\numberwithin`, `\label`/`\ref`/`\cite`, bibliography fixes. No mathematical changes. | Pending |
| 1 | §2 foundations: κ-splitting, global cover, genuine conventions, center, NAK, measures, GL(2) cover | Pending |
| 2 | §3 rank 0 (much simpler for n = 2: the cover of A is abelian) | Pending |
| 3 | §4 and `cctrac3b.tex`: geometric side | Pending |
| 4 | §5 spectral side: residual (Weil representation) spectrum, ramified χ, M_B^T | Pending |
| 5 | §6 invariant form | Pending |
| 6 | §7 stable(r) form | Pending |
| 7 | Consistency pass, independent re-referee, literature review, title page | Pending |

## Items

Status values: open, fixed, moot (n = 2), deferred.

### Major issues I: the cover, conventions, global construction (stage 1)

| # | Location | Issue | Status |
|---|---|---|---|
| I.1 | Lemma 2.2(b), before Lemma 2.4, Lemma 2.8, §2.1.4, §7.4 | Splitting over K is k ↦ (k, κ(k)), not k ↦ (k,1) | open |
| I.2 | Lemma 2.2(c) | Splitting over K_m needs the correct threshold, not m ≥ n | open |
| I.3 | §2.2 | Global cocycle ∏ β_v diverges; use β_v·∂κ_v; tie (2.9) to that normalization | open |
| I.4 | §2.2, §3.1 | Global cover is a quotient, not a subgroup, of ∏′ of the local covers | open |
| I.5 | §2.1.4 vs §3.1 | Genuine conventions make R(f) vanish; adopt anti-genuine test functions (Li) | open |
| I.6 | Lemmas 2.2(e), 2.3(e), 2.6(d) | Center need not be a direct product ((−1,−1)₂ can be −1) | open |
| I.7 | Lemmas 2.4, 2.9 | NAK: a is determined modulo A ∩ K; H(g) is what is well defined | open (book1 fixes the global case) |
| I.8 | Lemma 2.2(g), (h) | Abelian preimage of T needs proof or citation; (h) notation and statement | open |
| I.9 | §2.1.3 | A_G = 1; A_B for Res_{k/Q}; H uses the norm, not the max | open |
| I.10 | §2.1.5 | Iwasawa measure: δ_B(a) for g = kan, δ_B(a)⁻¹ for g = nak | open |

### Major issues II: the trace formula

| # | Location | Issue | Stage | Status |
|---|---|---|---|---|
| II.1 | §3.4 | Stabilizer is {x : (x,δ)² = 1} | 2 | moot (n = 2) |
| II.2 | Thm 3.2 | Restate as correspondence of automorphic spectra | 2 | open (trivializes for n = 2) |
| II.3 | (3.18) | Hasse principle for N-th powers | 2 | moot (n = 2: N = 1) |
| II.4 | Lemmas 3.3–3.4 | Mackey/Clifford; citation of [GeKn] | 2 | moot (n = 2) |
| II.5 | (4.4) | Weight v_O must be 2T − H(x) − H(wx) (book7d has it) | 3 | open |
| II.6 | (4.5), §5.4(a) | Unipotent terms in central classes (book7d, book7f have them) | 3 | open |
| II.7 | Lemma 4.4, Cor. 4.5–4.7 | Proof incomplete; cite [A2, §7], [A12] | 3 | open |
| II.8 | Prop. 4.8 | Polynomiality claim too strong, unproved | 3 | open |
| II.9 | Intro, §5 | Residual spectrum not empty (even Weil representation, [Ge2]) | 4 | open |
| II.10 | Thm 5.31, §5.4(b) | Ramified χ (μ^w = μ) omitted | 4 | open |
| II.11 | Example 5.32 | Sign is right; factor 2 wrong: 2T·I − ½M⁻¹M′ | 4 | open |
| II.12 | Lemmas 5.28–5.29 | Not proved; cite Maass–Selberg ([MW2], Li III) | 4 | open |
| II.13 | Examples 5.5, 5.24, 5.25 | E_G vs E_B confusion; equivalence of cuspidal data | 4 | open |
| II.14 | §6.1 | Conjectures 6.2–6.6 are now Li II/IV; Aoki at ℝ (book7gnw) | 5 | open |
| II.15 | Example 6.1 | u′_B = −H_B(ky) | 5 | open |
| II.16 | §6.4(b) | m′/m term missing (book7g/7gnw item (e) has it) | 5 | open |
| II.17 | (6.7) | Circular definition of φ(σ,X) | 5 | open |
| II.18 | §7.2 | GL(2) action on the cover; non-abelian preimage of T₁ | 6 | open |
| II.19 | Prop. 7.1, Lemma 7.3 | T(Q) not discrete in T(A_S); index 2 (Hasse norm theorem) | 6 | open |
| II.20 | §7.4 | D(A/F): A·Z vs A₁; global index undefined | 6 | open |
| II.21 | (7.17) | Divergent sum over rational unipotent classes | 6 | open |
| II.22 | (7.13), book7d | v_A at p-adic places is log max(1,\|n\|) | 3, 6 | open |
| II.23 | §7 | Results deferred to [J1], [J3]; Lemma 7.18; Remark 7.17 | 6 | open (book3b supplies several proofs) |

### Appendix: cctrac3b.tex = book7d.tex (stage 3)

| # | Issue | Status |
|---|---|---|
| A.1 | Fine expansion for covers: cite Li I, not only [A12] | open |
| A.2 | J_A(z,f) needs the r_A^G(z,a) J_G(az,f) correction | open |
| A.3 | Centralizer list; class of ±1 is not semisimple; centralizers in the cover | open |
| A.4 | Weight normalization: log δ = 2H | open |
| A.5 | J_unip must be the polynomial evaluated at T = 0 | open |
| A.6 | v_A at p-adic places | open (same as II.22) |
| A.7 | Minor slips | open |

### Also from book3b.tex (local comparisons, for stage 6)

| # | Issue | Status |
|---|---|---|
| C.1 | Matrix identity in the v_A claim is wrong; correct factorization w·n(x) = n(−x⁻¹)·diag(x⁻¹,x)·n̄(x⁻¹) | open |
| C.2 | #L(π) with k_v^×/k_v^{×n} | moot (n = 2) |
| C.3 | Real Hilbert symbol misdefined | open |
| C.4 | L-group of the 2-fold cover is SL(2,ℂ), not PGL(2,ℂ) | open |

### Minor issues, cross-references, bibliography (stage 0 unless noted)

The full lists are in the referee report: the minor-issues table, the stale cross-references, and the bibliography corrections table. Stage 0 fixes the cross-references and the bibliography; the minor mathematical slips are fixed in the stage of their section.

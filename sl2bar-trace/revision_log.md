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
| 1 | §2 foundations: κ-splitting, global cover, genuine conventions, center, NAK, measures, GL(2) cover | Done 2026-11-10: `revised/sec2-foundations.tex`, checked by `revised/checks/sec2_n2_check.py` (see *Stage 1 notes*). Written before stage 0, as a standalone file for the stage-0 master to `\input`. |
| 2 | §3 rank 0 (much simpler for n = 2: the cover of A is abelian) | Done 2026-11-10: `revised/sec3-rank0.tex`, checked by `revised/checks/sec3_n2_check.py` (see *Stage 2 notes*) |
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
| I.1 | Lemma 2.2(b), before Lemma 2.4, Lemma 2.8, §2.1.4, §7.4 | Splitting over K is k ↦ (k, κ(k)), not k ↦ (k,1) | fixed in §2 (Lemma 2.2(b), K*_p, Hecke unit (2.8)); §7.4 in stage 6 |
| I.2 | Lemma 2.2(c) | Splitting over K_m needs the correct threshold, not m ≥ n | fixed: β ≡ 1 on K_m once 1+ϖ^m𝒪 ⊂ F^{×2} (proof given); m ≥ 1 non-dyadic, m ≥ 2e+1 dyadic. Remark 2026.1: K₂ ⊂ SL₂(ℤ₂) splits via (c,d)₂ (numerical) |
| I.3 | §2.2 | Global cocycle ∏ β_v diverges; use β_v·∂κ_v; tie (2.9) to that normalization | fixed: σ_v = β_v·∂κ_v (2.10)–(2.11); splitting γ ↦ (γ, κ_A(γ)) (Lemma 2.6(a)); old (2.9) compared in Remark 2026.2; Example 2.B (Jacobi symbol) |
| I.4 | §2.2, §3.1 | Global cover is a quotient, not a subgroup, of ∏′ of the local covers | fixed in §2 (also for G(Q_p)) and §3.1 |
| I.5 | §2.1.4 vs §3.1 | Genuine conventions make R(f) vanish; adopt anti-genuine test functions (Li) | fixed: Li's convention stated in §2.1.4; for n = 2 genuine and anti-genuine coincide, so R(f) does not vanish (Remark 2026.4) |
| I.6 | Lemmas 2.2(e), 2.3(e), 2.6(d) | Center need not be a direct product ((−1,−1)₂ can be −1) | fixed: local center cyclic of order 4 iff (−1,−1)_v = −1; global center not a direct product when k has a real place |
| I.7 | Lemmas 2.4, 2.8 | NAK: a is determined modulo A ∩ K; H(g) is what is well defined | fixed (Lemmas 2.4, 2.8). The report says 2.9; the global NAK lemma is 2.8 as compiled |
| I.8 | Lemma 2.2(g), (h) | Abelian preimage of T needs proof or citation; (h) notation and statement | fixed: (g) proved for every abelian subgroup (symmetry of the quadratic symbol). (h): the report's objection does not hold, see *Stage 1 notes*; statement kept, proof supplied, notation clash removed |
| I.9 | §2.1.3 | A_G = 1; A_B for Res_{k/Q}; H uses the norm, not the max | fixed (§2.1.3, (2.5), Lemma 2.8) |
| I.10 | §2.1.5 | Iwasawa measure: δ_B(a) for g = kan, δ_B(a)⁻¹ for g = nak | fixed in §2 (2.9); the Siegel-domain measure in §4.1.1 in stage 3 |

### Major issues II: the trace formula

| # | Location | Issue | Stage | Status |
|---|---|---|---|---|
| II.1 | §3.4 | Stabilizer is {x : (x,δ)² = 1} | 2 | moot (n = 2): the cover of A is abelian; general n summarized in Remark 2026.6 |
| II.2 | Thm 3.2 | Restate as correspondence of automorphic spectra | 2 | fixed: Theorem 3.2 is a bijection χ ↦ χ̄₀·χ onto genuine automorphic characters, after a choice χ̄₀ that cannot be avoided (Example 3.A); for T = A, the canonical choice is Weil's χ_ψ (Lemma 3.3) |
| II.3 | (3.18) | Hasse principle for N-th powers | 2 | moot (n = 2: N = 1); noted in Remark 2026.6 |
| II.4 | Lemmas 3.3–3.4 | Mackey/Clifford; citation of [GeKn] | 2 | moot (n = 2): the Clifford–Mackey part is removed; the cocycle remark is answered by (3.1) |
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
| II.18 | §7.2 | GL(2) action on the cover; non-abelian preimage of T₁ | 1, 6 | partly fixed: cover of GL(2) and its action defined in §2.3 (Lemma 2.10), with the commutator formula (2.14); its use in §7 in stage 6 |
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

## Stage 1 notes (2026-11-10)

**Files.** `revised/sec2-foundations.tex` is the new Section 2. It builds on its own through `revised/preview.tex` (originally `stage1-preview.tex`; PDF committed). `revised/checks/sec2_n2_check.py` verifies every explicit n = 2 formula in exact rational arithmetic at v = ∞, 2, 3, 5, 7. It runs in about 2 seconds and is picked up by the top-level `run_checks.py`.

**Numbering.** Lemmas 2.1–2.9 keep their 1995 numbers and order. New: Lemma 2.10 (GL(2) cover), Examples 2.A and 2.B, and Remarks 2026.1–2026.5. Equations are now numbered (2.1)–(2.14). In the compiled 1995 text, Lemma 2.8 is the global NAK lemma and Lemma 2.9 is the heights lemma. The report swaps these, in items I.1 ("Lemma 2.8"), I.7 ("Lemma 2.9") and the minor item "Lemma 2.8(d)".

**Where this revision departs from the report.**
- *Lemma 2.2(h).* The report says u ↦ (u,1) is not a homomorphism on lower-triangular unipotents for Kubota's cocycle. It is: for u_s = g n(s) g⁻¹ the c-entry is linear in s, so β(u_{s₁},u_{s₂}) = ((s₁+s₂)/s₁, (s₁+s₂)/s₂), which is 1 by the Steinberg relation. This holds for every n, not only n = 2. The splitting over any unipotent subgroup is unique, since Hom(F, μ₂) = 1. So the 1995 statement (g,ζ)(n,1)(g,ζ)⁻¹ = (gng⁻¹,1) is correct for all g; the script checks it on random g. Only the clash of n (cover degree vs. matrix) needed fixing.
- *I.2.* No condition on the off-diagonal entries is needed. β ≡ 1 on K_m as soon as the diagonal entries are squares, by the Steinberg relation (proof in Lemma 2.2(c)).

**Found in this stage, not in the report.**
- The torus T_θ: the matrix [[a, bθ],[b, a]] has determinant a² − θb², not a² + θb².
- 1995 Lemma 2.5(b) claims H(kxk′) = H(x). H is left N-invariant and right K-invariant, but not left K-invariant. Restated.
- G(Q_p)-bar is also a quotient (not a subgroup) of ∏_{v|p} of the local covers. Local heights now use the product over v | p, matching the global norm.
- Lemma 2.7: the 1995 statement uses K = ∏_{p≤∞} K_p, which is not open, and a disjoint union. Restated with K_f compact open and a single quotient, with the lift Γ̃ ⊂ G(ℝ)-bar made explicit.

**Minor §2 items from the report fixed here:** ν(π) = 1, |π| = q⁻¹; Lemma 2.2(d), archimedean relevance (complex places are split); the remark after Lemma 2.2 ("comapct", SU(2)) absorbed into Lemma 2.2(d); β_p index; Lemma 2.4 parenthesis and K_p; ϖ is the fundamental coweight, α^∨ = X_α; the Hecke algebra for p odd, matching Lemma 2.2(b); Lemma 2.5 split into a local lemma and Lemma 2.8(b); Lemma 2.7; Lemma 2.9(d) with N = 1; "spherical" now means "equal to the unit element e_v, defined with K*_v".

**Still resting on citation and numerics only** (Remark 2026.5): Lemma 2.2(b) (Kubota's κ-splitting), Lemma 2.10(a)–(b) (the GL(2) cocycle and its splitting over GL(2,𝒪)), and Remark 2026.1 (K₂ over ℚ₂).

**Deferred.** Which GL(2) cover (σ or the Kazhdan–Patterson twist σ′) §7 needs: stage 6 (Remark 2026.3). The §3.1 quotient statement and conventions: stage 2.

## Stage 2 notes (2026-11-10)

**Files.** `revised/sec3-rank0.tex` is the new Section 3. `revised/preview.tex` (renamed from `stage1-preview.tex`) now builds Sections 2–3 together, with the PDF committed. `revised/checks/sec3_n2_check.py` adds 35 checks, and `checks/padic_lib.py` holds the Hilbert-symbol helpers shared by both scripts.

**What changed, and why.** For n = 2 the cover of every torus is abelian (Lemmas 2.2(g), 2.6(e)), so the Clifford–Mackey machinery of the 1995 §3.2 is not needed. The rank-0 trace formula is Poisson summation on T(ℚ)\T(𝔸)¹ after multiplying by one genuine automorphic character χ̄₀ (Theorem 3.4, Lemma 3.5). The section is now stated for every maximal ℚ-torus T, because §7 applies it to anisotropic tori. The cover is abelian but not split, so a choice of χ̄₀ is unavoidable (Example 3.A: over ℚ, every genuine character takes the value ±i on a lift of a(−1)_∞). For T = A, Weil's character χ_ψ(a(t),ζ) = ζ∏_v γ_v(t)/γ_v(1) is the canonical choice, depending only on ψ (Lemma 3.3). Stage 4 will need it again for the Weil representation.

**Numbering map (1995 → 2026).**

| 1995 (compiled) | 2026 |
|---|---|
| Lemma 3.1 (factorizability, [Ge2]) | Lemma 3.1(c), with a proof |
| Theorem 3.2 (correspondence) | Theorem 3.2 |
| Lemma 3.3, Remark 3.4, Lemma 3.5, Remarks 3.6–3.7 (Clifford–Mackey, C_p) | removed; Remark 2026.6 for general n |
| Theorem 3.8 (kernel, spectral decomposition) | Theorem 3.4(a) |
| Theorem 3.9 (trace formula) | Theorem 3.4(b), equation (3.3) |
| Remark 3.10 (conjugation by (x,δ)²) | removed (trivial for n = 2) |
| Lemma 3.11 (local maps f̄_p ↦ f_p) | Lemma 3.5(a), (b) |
| Lemma 3.12 (orbital integrals = f(δ)) | Lemma 3.5(c) |
| Claims 1–2 | replaced by Lemma 3.5 |
| (3.21)–(3.22), I^A_O and I^A_χ | (3.4), §3.3 |
| — | new: Lemma 3.3 (Weil's χ_ψ), Examples 3.A, 3.B, Remarks 2026.6–2026.7 |

The report's §3 numbers do not match the compiled 1995 text. Its "Theorem 3.6" is Theorem 3.9, "Remark 3.7" is Remark 3.10, "Lemma 3.8(c)" is Lemma 3.11(c), and "Lemmas 3.3–3.4" are Lemmas 3.3 and 3.5.

**Minor §3 items from the report.** All are fixed or moot:
- "μ_n acts on G(𝔸) = 𝔸_k^×" and the undefined A(𝔸)¹: fixed in §3.1.
- β(g₁,g₂) for β(g,g′) in (3.3): fixed by (3.1).
- C_p = A(ℝ)^N and (3.9): removed.
- (3.12), (3.14) variables and the centralizer: removed, since centralizers are everything.
- Σ_x for ∫ in (3.15) and Theorem 3.9, and s_𝔸(δ) inside a local factor in (3.16): moot, since orbital integrals are point values.
- Lemma 3.8(c) counting measure: moot.
- Claims 1–2 limit index and interchange: replaced.
- "§4.3.1 below": the Hecke algebra is now defined in §3.1 and §3.3.

**Still resting on citation and numerics only** (Remark 2026.7): Lemma 3.3(a)–(b), Weil's identity for γ_v and the product formula. Both are checked numerically for k = ℚ at v = ∞, 2, 3, 5, 7 (product formula on random a ∈ ℚ^×), and the odd-p closed form for p ≤ 31.

**For later stages.** `cctrace4.tex` cites "Π_u as in section 3.2", which is now §3.1 (stage 4). `cctrace6.tex` cites I^A_O and I^A_χ from "section 3.4", which are now (3.4) in §3.3 (stage 5). Proposition 7.1 of `cctrace7.tex` should use Theorem 3.4 for anisotropic T (stage 6).

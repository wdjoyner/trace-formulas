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
| 3 | §4 and `cctrac3b.tex`: geometric side | Done 2026-11-10: `revised/sec4-geometric.tex`, checked by `revised/checks/sec4_n2_check.py` (see *Stage 3 notes*) |
| 4 | §5 spectral side: residual (Weil representation) spectrum, ramified χ, M_B^T | Done 2026-11-10: `revised/sec5-spectral.tex`, checked by `revised/checks/sec5_n2_check.py` (see *Stage 4 notes*) |
| 5 | §6 invariant form | Done 2026-11-11: `revised/sec6-invariant.tex`, checked by `revised/checks/sec6_n2_check.py` (see *Stage 5 notes*) |
| 6 | §7 stable(r) form | Pending |
| 5R | Response to the second referee report (ChatGPT, on Sections 2–6): topology of the cover and test functions, b′ = −b, Section 1 (overview, literature review), Glossary, Appendix A (comparisons with 1995), acknowledgements | Done 2026-11-11: see *Second referee report* below and `referee-2026-11/` |
| 7 | Consistency pass after stage 6; Introduction and literature review to be extended to Section 7. (The independent re-referee, the literature review, the title page and the Introduction for Sections 2–6 were done in 5R.) | Pending |

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
| I.10 | §2.1.5 | Iwasawa measure: δ_B(a) for g = kan, δ_B(a)⁻¹ for g = nak | fixed in §2 (2.9) and in the Siegel-domain paragraph of §4.2 |

### Major issues II: the trace formula

| # | Location | Issue | Stage | Status |
|---|---|---|---|---|
| II.1 | §3.4 | Stabilizer is {x : (x,δ)² = 1} | 2 | moot (n = 2): the cover of A is abelian; general n summarized in Remark 2026.6 |
| II.2 | Thm 3.2 | Restate as correspondence of automorphic spectra | 2 | fixed: Theorem 3.2 is a bijection χ ↦ χ̄₀·χ onto genuine automorphic characters, after a choice χ̄₀ that cannot be avoided (Example 3.A); for T = A, the canonical choice is Weil's χ_ψ (Lemma 3.3) |
| II.3 | (3.18) | Hasse principle for N-th powers | 2 | moot (n = 2: N = 1); noted in Remark 2026.6 |
| II.4 | Lemmas 3.3–3.4 | Mackey/Clifford; citation of [GeKn] | 2 | moot (n = 2): the Clifford–Mackey part is removed; the cocycle remark is answered by (3.1) |
| II.5 | (4.4) | Weight v_O must be 2T − H(x) − H(wx) (book7d has it) | 3 | fixed: Prop. 4.6, J^T_O = c_k ∫ f(y⁻¹μy)(2T + v_A(y)) dy with v_A = −H(y) − H(wy) ≥ 0 (Lemma 4.3(c)) |
| II.6 | (4.5), §5.4(a) | Unipotent terms in central classes (book7d, book7f have them) | 3, 4 | fixed in §4: Prop. 4.8 (explicit, via the zeta integral Z(f,s)) and Thm 4.11(a) (fine form); in §5: Thm 5.15(a) uses Thm 4.11(a) in full; in §6: Thm 6.11(a) |
| II.7 | Lemma 4.4, Cor. 4.5–4.7 | Proof incomplete; cite [A2, §7], [A12] | 3 | fixed: Thm 4.5, proved directly for this group class by class (T ≥ 0), with [A2, §§7–8], [A3], [Li I] cited for the general case |
| II.8 | Prop. 4.8 | Polynomiality claim too strong, unproved | 3 | fixed: J^T_O := ∫ k^T_O = ∫ j^T_O (Thm 4.5(b)); each is linear in T, explicitly (Props. 4.6–4.8) |
| II.9 | Intro, §5 | Residual spectrum not empty (even Weil representation, [Ge2]) | 4, 7 | fixed in §5: Thm 5.7, one even Weil representation V_b for each b ∈ k^×/k^{×2}, the residue at λ = ½ of the Eisenstein series of χ_{ψ_b}; Example 5.B (θ(z)). The Introduction is rewritten in stage 7 |
| II.10 | Thm 5.31, §5.4(b) | Ramified χ (μ^w = μ) omitted | 4 | fixed: Lemma 5.3 (μ^w = μ iff μ = χ_{ψ_b}), Thm 5.13(c) (residual part, ½ of the continuous term, and ¼ tr(M(w,0)I(μ₀,f))), Thm 5.15(e). Sign: confirmed in stage 5 against Arthur, Gelbart–Jacquet and a direct numerical check, and M(w,0) = −1 (Prop. 6.13); see *Stage 5 notes* |
| II.11 | Example 5.32 | Sign is right; factor 2 wrong: 2T·I − ½M⁻¹M′ | 4 | fixed: M_B^T = 2T − M⁻¹ dM/dλ (5.10) in the coordinate λ(X) = λX, for every k (the α^∨ = d factor cancels against vol(𝔞/ℤα^∨) = d); the T-coefficient is checked against §4 (Prop. 5.16) |
| II.12 | Lemmas 5.28–5.29 | Not proved; cite Maass–Selberg ([MW2], Li III) | 4 | fixed: Thm 5.11 cites [A3], Li III, and the false claims (compact support; "continuous, hence integrable") are corrected; Lemma 5.12 (Maass–Selberg) is stated for T ≥ 0 with a proof sketch |
| II.13 | Examples 5.5, 5.24, 5.25 | E_G vs E_B confusion; equivalence of cuspidal data | 4 | fixed: cuspidal data and their equivalence (§5.1, Lemma 5.3); kernels K_{B,χ}, K_{G,χ} (Prop. 5.8) |
| II.14 | §6.1 | Conjectures 6.2–6.6 are now Li II/IV; Aoki at ℝ (book7gnw) | 5 | fixed: the normalization (1995 Conj. 6.10) is Theorem 6.5 (Arthur, Li II), explicit at the unramified and real places (Lemma 6.6); the trace Paley–Wiener conjectures (1995 Conj. 6.3, 6.4, 6.7, 6.8) are not needed for this group, because the only proper Levi has an abelian cover; Li IV is cited for the general theory |
| II.15 | Example 6.1 | u′_B = −H_B(ky) | 5 | fixed: Lemma 6.1(a), Example 6.A; the variance formulas that depend on the sign are proved (Lemmas 6.2–6.4) and checked numerically |
| II.16 | §6.4(b) | m′/m term missing (book7g/7gnw item (e) has it) | 5 | fixed: Thm 6.11(e)–(f) and Cor. 6.14; the global factor m is identified in Cor. 6.7 (L(2λ,χ²)/L(2λ+1,χ²) outside finitely many places) |
| II.17 | (6.7) | Circular definition of φ(σ,X) | 5 | fixed: the corrected definition is stated after Thm 6.9; φ_A(f) is shown to lie in the space (Thm 6.9(a)), and the 1995 claim that this space equals the Paley–Wiener space of the cover of A is corrected (Example 6.C) |
| II.18 | §7.2 | GL(2) action on the cover; non-abelian preimage of T₁ | 1, 6 | partly fixed: cover of GL(2) and its action defined in §2.3 (Lemma 2.10), with the commutator formula (2.14); its use in §7 in stage 6 |
| II.19 | Prop. 7.1, Lemma 7.3 | T(Q) not discrete in T(A_S); index 2 (Hasse norm theorem) | 6 | open |
| II.20 | §7.4 | D(A/F): A·Z vs A₁; global index undefined | 6 | open |
| II.21 | (7.17) | Divergent sum over rational unipotent classes | 6 | open |
| II.22 | (7.13), book7d | v_A at p-adic places is log max(1,\|n\|) | 3, 6 | fixed in §4 (Lemma 4.9: log max(1,\|y\|) finite, ½log(1+y²) real, log(1+\|y\|²) complex); (7.13) in stage 6 |
| II.23 | §7 | Results deferred to [J1], [J3]; Lemma 7.18; Remark 7.17 | 6 | open (book3b supplies several proofs) |

### Appendix: cctrac3b.tex = book7d.tex (stage 3)

| # | Issue | Status |
|---|---|---|
| A.1 | Fine expansion for covers: cite Li I, not only [A12] | fixed: Thm 4.11 |
| A.2 | J_A(z,f) needs the r_A^G(z,a) J_G(az,f) correction | fixed: Lemma 4.10, with r(t) = Σ log\|t² − t⁻²\|_v and the explicit limit Σ_v ∫Φ_v(y) log\|2y\|_v dy ∏_{w≠v} Φ̂_w(0); the divergence without r is checked |
| A.3 | Centralizer list; class of ±1 is not semisimple; centralizers in the cover | fixed: Lemma 4.1 (for n = 2 the centralizer in the cover is the full preimage) |
| A.4 | Weight normalization: log δ = 2H | fixed: everything is written with H (Prop. 4.6) |
| A.5 | J_unip must be the polynomial evaluated at T = 0 | fixed: Prop. 4.8; here the integral converges at T = 0, so both definitions agree |
| A.6 | v_A at p-adic places | fixed (Lemma 4.9; same as II.22) |
| A.7 | Minor slips | fixed: f_∞ ∈ C_c^∞ (§4.4); \symbol{126} gone; covers marked throughout; fine expansion summed over (G,S)-classes (Thm 4.11) |

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

## Stage 3 notes (2026-11-10)

**Files.** `revised/sec4-geometric.tex` is the new Section 4. It merges the 1995 §4 (`cctrace3.tex` = `book7c.tex`) with the file `cctrac3b.tex` that the 1995 master inputs, which is `book7d.tex` (§§9.3–9.5 of the 1997 book). `revised/preview.tex` now builds Sections 2–4, with the PDF committed. `revised/checks/sec4_n2_check.py` adds 19 checks (about 3 seconds; needs SymPy, which brings mpmath).

**What changed, and why.** Lemma 4.3(b) is the inequality H(x) + H(γx) ≤ 0 for γ ∈ G(ℚ) ∖ B(ℚ). It follows from Hadamard's inequality applied to the bottom rows e₂x and e₂γx, together with the product formula. For T ≥ 0 it gives:
- at most one δ ∈ B(ℚ)\G(ℚ) with H(δx) > T;
- Arthur's partition (Lemma 4.4), with T₀ = 0;
- v_A ≥ 0.

So for this group every step of the coarse expansion can be checked directly, and Theorem 4.5 is proved class by class:
- **Hyperbolic classes** (Prop. 4.6): J^T_O = c_k ∫ f(y⁻¹μy)(2T + v_A(y)) dy. The equality ∫k^T_O = ∫j^T_O is Arthur's §8 argument, made absolutely convergent by Poisson summation on N(ℚ)\N(𝔸).
- **Elliptic classes** (Prop. 4.7): independent of T.
- **Central classes** (Prop. 4.8): J^T = vol·f(1) + c_k Φ̂(0) T + FP_{s=1} Z(f,s), where Z is a zeta integral of the K-averaged unipotent function Φ. It decomposes over ξ ∈ k^×/k^{×2} into products of local unipotent orbital integrals (Lemma 4.10(c)).

The local distribution J_A(z,f) at a central element is Arthur's limit with the r^G_A correction, computed explicitly (Lemma 4.10). The fine expansion (Theorem 4.11) is stated as Arthur's and Li's theorem specialized to SL(2). Parts (b) and (c) are deduced from Propositions 4.6 and 4.7. In part (a) the coefficients a^G(S,u_ξ) are not computed (Remark 2026.9).

**Numbering map (1995 → 2026).** The 1995 numbers are those of `cctrace_new.tex` as compiled. `cctrac3b.tex` was missing, so its items are named by content. Later sections cite them as "Proposition 4.18" (the fine expansion), "Example 4.14" (J_A(z,f)) and "Proposition 4.16/4.19".

| 1995 | 2026 |
|---|---|
| §4.1, kernel K_P, Lemma 4.1 | (4.1)–(4.2), Lemma 4.2 |
| §4.1.1 Siegel domain, Lemma 4.2 | Lemma 4.3 and the Siegel-set paragraph of §4.2 |
| Lemma 4.3 (partition), (4.2) | Lemma 4.4, (4.5) |
| Lemma 4.4, Cors. 4.5–4.7, Prop. 4.8, Cor. 4.9 | Theorem 4.5 |
| (4.3)–(4.4), weight v_O | Prop. 4.6, (4.6)–(4.7) |
| (4.5), semisimple non-regular classes | Prop. 4.8 |
| book7d §9.3.1 (spaces ℋ_N(…)_Γ) | §4.4, *Test functions* |
| book7d §9.4, centralizer display | Lemma 4.1 |
| book7d §9.4, Theorem (weighted orbital integrals) | Prop. 4.6 |
| book7d §9.5, J_M(γ,f), r_M, v_M | (4.11)–(4.12), Lemma 4.9, Remark 2026.8 |
| book7d Example J_A(z,f) ("Example 4.14") | Lemma 4.10 |
| book7d Definition J_unip and its Example | Prop. 4.8 |
| book7d Definition a^M(S,γ), Proposition [A12, Thm 8.1] ("Proposition 4.18") | Theorem 4.11 |
| book7d last Example (1 ∈ O) | Theorem 4.11(a) |
| — | new: Example 4.A (k = ℚ), Remarks 2026.8–2026.10 |

**Where this revision departs from the report.**
- *II.7.* The report suggests citing [A2, §7] and [A12] for the per-class estimates. For SL(2) they are proved here instead, so Corollaries 4.5–4.7 (the T^{−C} bounds) are no longer needed and are dropped. Arthur and Li are cited for the general case.
- *Item II.8 asks which of k^T_O and j^T_O defines J^T_O.* Both integrals converge absolutely for T ≥ 0 and are equal (Theorem 4.5(b)).
- *Item A.5.* With the normalizations here, the book's definition (truncation at T₀ = 0) is correct. The truncated integral converges at T = 0, by Lemma 4.3. The general definition (evaluate the polynomial) is also stated.

**Found in this stage, not in the report.**
- **§2 normalization of α (fixed in `sec2-foundations.tex`).** For k ≠ ℚ the simple root of (B, A_B) is α = (2/d)χ₁, so α(X) = 2X/d and α^∨ = d, with d = [k:ℚ]. The stage-1 text had α = 2χ₁ and X_α = 1, which holds only for k = ℚ. δ_B = e^{2H} for every k. Remark 2026.8 compares our Lebesgue measure on 𝔞 (for which 𝔞/ℤα^∨ has volume d) with Arthur's (volume 1). **Stage 4 must use this**: the identification ς(α^∨) in Example 5.32 (item II.11) was derived for k = ℚ.
- **book7d claims ℋ_ac = ℋ_mod = ℋ for both G and A.** This holds for G (A_G = 1) but not for A, since 𝔞_A ≠ 0.
- **Weighted orbital integral at complex places.** The weight there is log(1 + |y|²) in the normalization of §2, not √(1+|n|²).

**Minor §4 items from the report:**
- Lemma 4.1: K_P = Σ K_{P,O}; one kernel convention, f(x⁻¹γy); proof rewritten.
- §4.1.1: the constants u ≥ ½ and T₀ > √3/2 are dropped; ω no longer means two things; there is a single parameter T ≥ 0 instead of T₀ > T₁; the unused N is gone.
- Cors. 4.6–4.7: the misplaced absolute value no longer arises, since the corollaries are replaced.
- §4.2: ς is no longer used for unipotent elements.
- "(1.10)", "(1.12)": stale references removed.

**Still resting on citation only** (Remark 2026.9):
- Theorem 4.11(a), including the coefficients a^G(S,u_ξ);
- the unramified orbital integrals used for 4.11(b)–(c);
- the comparison of r(t) with the general definition of r^G_A in [A7] (Remark 2026.8).

**For later stages.**
- *Stage 4:* §5.4(a) must use Theorem 4.11(a) in full. `cctrace5.tex` cites "lemma 4.7" for the partition, which is now Lemma 4.4. The α^∨ normalization above affects M_B^T (II.11).
- *Stage 5:* §6.4(a) and the "invariant version of Proposition 4.18" must use Theorem 4.11.
- *Stage 6:*
  - compute a^G(S,u_ξ) from Prop. 4.8 (the ξ-decomposition of Z(f,s) has infinite fibers over k_S^×/k_S^{×2}; this is item II.21);
  - replace (7.13) by Lemma 4.9;
  - use J_A(z,f) of Lemma 4.10 in §7.

## Stage 4 notes (2026-11-10)

**Files.** `revised/sec5-spectral.tex` is the new Section 5. It merges `cctrace4.tex` (= `book7e.tex`, §§5.1–5.2) and `cctrace5.tex` (= `book7f.tex`, §§5.3–5.4). `revised/preview.tex` now builds Sections 2–5, with the PDF committed; it gained a `corollary` environment, which the stage-0 master also needs. `revised/checks/sec5_n2_check.py` adds 45 checks (about 3 seconds; needs SymPy and mpmath).

**What changed, and why.**
- **The Weyl action on the cover of A** (Lemma 5.3). Conjugation by w sends (a(t),ζ) to (a(t⁻¹),ζ). This is not inversion, which is (a(t),1)⁻¹ = (a(t⁻¹),(t,−1)). Weil's character satisfies χ_ψ^w = χ_ψ, so for μ = χ_ψ·χ we get μ^w = χ_ψ·χ⁻¹. Hence the ramified classes (μ^w = μ) are exactly the χ_{ψ_b}, b ∈ k^×/k^{×2}. For SL(2) itself they are the μ with μ² = 1.
- **The intertwining operator** (Lemma 5.6). The unramified local factor on the double cover is L_v(2λ,χ_v²)/L_v(2λ+1,χ_v²), against L_v(λ,χ_v)/L_v(λ+1,χ_v) for SL(2). It is computed by an explicit Iwasawa decomposition of the lift of w⁻¹n(y): the odd shells cancel, because the integrand there is a constant times the quadratic character of the unit part. So M(w,λ) = m^S(μ,λ)·M_S(λ) with m^S = L^S(2λ,χ²)/L^S(2λ+1,χ²). In Re λ > 0 it has a pole only when χ² = 1, and then only at λ = ½.
- **The residual spectrum** (Theorem 5.7, item II.9). It is one even Weil representation V_b for each b ∈ k^×/k^{×2}: the residues at λ = ½ of the Eisenstein series of χ_{ψ_b}. Their constant terms have order e^{H/2}. For k = ℚ, b = 1 this is θ(z) = Σ q^{n²} (Example 5.B). That V_b is nonzero and lives in the class χ_b is proved here; that V_b is irreducible and isomorphic to r⁺_{ψ_{b′}} is cited ([Ge2], [GPS80], [Wa80]).
- **The kernels** (Prop. 5.8, item II.13). For cuspidal χ there is no Eisenstein series. For χ ∈ 𝒳_A, K_{G,χ} carries the factor ½ = n(A_B)⁻¹ and a sum over both members of χ. The term that the 1995 notes put in K_{G,χ} belongs to K_{B,χ}.
- **Truncation** (Lemma 5.9). For T ≥ 0, Λ^T is idempotent and self-adjoint, by the height inequality of Lemma 4.3(b). Λ^T E is rapidly decreasing, not compactly supported (item II.12).
- **The terms J_χ^T** (Theorem 5.13). They are derived from the Maass–Selberg relations (Lemma 5.12, with a proof sketch for T ≥ 0): (a) m(π) tr π(f); (b) the integral of tr(M_B^T I) with M_B^T = 2T − M⁻¹ dM/dλ (item II.11); (c) for ramified χ_b, the residual trace, ½ of the continuous term, and ¼ tr(M(w,0)I(μ₀,f)) (item II.10). The last comes from the cross terms of the Maass–Selberg relation in the limit T → ∞.
- **The global normalizing factor** (Corollary 5.14). tr(M⁻¹M′ I) = (m^S)′/m^S · tr I_S + tr(M_S⁻¹M_S′ I_S), where (m^S)′/m^S = 2(L^S)′/L^S(2λ,χ²) − 2(L^S)′/L^S(2λ+1,χ²). Stage 5 needs this for the m′/m term (item II.16).
- **The trace formula** (Theorem 5.15). The central classes use Theorem 4.11(a) in full (item II.6). The spectral side has the residual and ramified terms.
- **A consistency check** (Prop. 5.16). The T-coefficients of the spectral and geometric sides agree: both are c_k Σ_{γ∈A(ℚ)} F_f(γ), where F_f is the Abel transform. This checks the factor 2T and the ½ = n(A_B)⁻¹ against §4, which was derived independently. With the 1995 values (4T, n(A) = 1) the two sides would differ by a factor of 4.

**Numbering map (1995 → 2026).** The 1995 numbers are those of `cctrace_new.tex` as compiled (with `cctrac3b.tex` = `book7d.tex`). Equations are now numbered (5.1)–(5.10).

| 1995 (compiled) | 2026 |
|---|---|
| Lemma 5.1 | Lemma 5.1 (corrected) |
| Example 5.2 (factorization) | Lemma 5.2 |
| Prop. 5.3 | Lemma 5.1, Prop. 5.4(a) |
| associate parabolics, 𝒳, Example 5.4 | *Cuspidal data* paragraph, Lemma 5.3 |
| (5.2)–(5.4), Corollary 5.5, Prop. 5.6 | Prop. 5.4 |
| §5.2 definitions ℋ_P, I_P, E, M(s,·) | (5.1)–(5.3) |
| Prop. 5.7, the bases ℬ_P(π)_χ, L^∧_𝒫 | ℬ(μ) before Prop. 5.8 (a basis of ℋ_B(μ), independent of λ) |
| Theorem 5.8 (Langlands) | Theorem 5.5 |
| Lemma 5.9, Remark 5.10, Theorem 5.11, Examples 5.17–5.22 | Prop. 5.8 |
| truncation, Example 5.12, Lemmas 5.13–5.14 | (5.7), Lemma 5.9 |
| Lemma 5.15, Example 5.16 | (5.8), Lemma 5.10 |
| Lemma 5.23, Remark 5.24, Lemmas 5.25–5.26 | Theorem 5.11 |
| Theorem 5.27, Example 5.28 | Theorem 5.13, (5.10) |
| §5.4 | Theorem 5.15 |
| — | new: Lemma 5.6, Theorem 5.7, Lemma 5.12, Corollary 5.14, Prop. 5.16, Examples 5.A–5.C, Remarks 2026.11–2026.13 |

The report's §5 numbers do not match the compiled text: its "Example 5.5" is Example 5.4, its "Examples 5.24, 5.25" are Examples 5.21, 5.22, its "Lemmas 5.28–5.29" are Lemmas 5.23 and 5.25, its "Theorem 5.31" is Theorem 5.27, and its "Example 5.32" is Example 5.28. The 1995 text cites itself with yet other numbers ("Lemma 5.28 above" for Lemma 5.23, "Lemma 5.19 above" for Lemma 5.13).

**Where this revision departs from the report.**
- *II.11.* The report's 2T·I − ½M⁻¹M′ (in the 1995 coordinate ς) is (5.10) in our coordinate λ = 2ς, for k = ℚ. For general k, Arthur's formula has vol(𝔞/ℤα^∨) = d and θ(ζ) = dζ, so d cancels: the stage-3 correction α^∨ = d does not change M_B^T, provided the volume is computed with the same measure dX. The script checks this for d = 1, 2, 3.
- *II.10.* The report calls the ramified term "the −¼ tr(M(w,0)I_B(μ,f)) term of Jacquet–Langlands and Gelbart–Jacquet". In J_χ we get **+**¼ tr(M(w,0)I(μ₀,f)). This agrees with the sign of the discrete term in Arthur's fine spectral expansion [A14, Thm 8.2]; it is derived in the proof of Theorem 5.13(c), and the limit is checked numerically. At the end of stage 4 this had not been reconciled with [JL] and [GJ]. It was reconciled in stage 5 (see *Stage 5 notes*, "The sign of the ramified term"): the two signs describe the same term on opposite sides of the formula.
- *II.12.* Besides the citations the report asks for, Lemma 5.12 gives the Maass–Selberg relation for this group with a proof sketch (unfolding plus Lemma 5.9). The rest of the 1995 Lemma 5.23 (K^T_χ = J^T_χ) is just the self-adjointness of Λ^T; what is actually needed is Theorem 5.11(c).

**Found in this stage, not in the report.**
- n(A_B), the number of chambers in 𝔞, is 2, not 1 as stated in the 1995 Theorem 5.8. This is the ½ in K_{G,χ}.
- The 1995 measures on i𝔞* are inconsistent: (1/2πi) in Theorem 5.8(b), (1/2π) in the norm on L^∧_𝒫. The measure here is dt/2π.
- The 1995 Example 5.18 imposes φ(ag) = π(a)φ(g) for all a ∈ A(𝔸)-bar, so λ is folded into π and the factor δ_B^{1/2} is missing. Here φ is A_B(ℝ)⁰-invariant and λ enters through φ_λ.
- The 1995 Example 5.2 says *all* genuine unitary representations factor (it should say irreducible). It calls π_p unramified if it has an overline{K_p}-fixed vector, which no genuine representation has; the right condition is a K_p^*-fixed vector.
- On the double cover, w-conjugation of the cover of A is not inversion (Lemma 5.3(b)). The 1995 notes assume the SL(2) picture.
- The intertwining integral converges for Re λ > ½, not only for Re λ > 1 (Lemma 5.6).
- Arthur's Theorem 5.11 is for "T sufficiently large". On the geometric side T ≥ 0 suffices (§4); on the spectral side Lemmas 5.9 and 5.12 hold for T ≥ 0, but we have not checked Theorem 5.11 itself in that range (Remark 2026.12).

**Minor §5 items from the report.** All fixed:
- the stale references in the §5 intro ("Lemma 1.7", "(4.5)", "Proposition 4.14", "Theorem 6.15", "4.1.1");
- Lemma 5.1 (finite multiplicity, direct integral);
- in §5.3, K_{P,χ}(δx,δx) in the definition of k^T_χ, and the unfinished sentence after (5.9) (it belonged to a claim that is now dropped);
- in §5.4, S and 𝔸_S are now defined in §4.4, and "given in section 5" now points to §4.

**Still resting on citation and numerics only** (Remark 2026.12):
- Lemma 5.1, Prop. 5.4 and Theorem 5.5 [L2, MW2];
- the wave-packet formula (5.6) and the absolute convergence in Prop. 5.8;
- Lemma 5.9(c);
- Theorem 5.11 [A3, Li III], including the interchange of integrals used for Theorem 5.13;
- the analytic continuation in Lemma 5.12;
- Theorem 5.7(c) [Ge2, GPS80, Wa80].

Which b′ (b, −b, or b times a fixed factor) labels the Weil representation in V_b depends on the normalization of ω_ψ, and is not fixed here. Lemma 5.6(b) is proved in the text and also checked numerically at p = 3, 5, 7.

**For later stages.**
- *Stage 5:*
  - §6 takes J_χ from Theorem 5.13 and Theorem 5.15(d)–(e).
  - The m′/m term (item II.16) is Corollary 5.14.
  - The new residual term tr(R(f)|V_b) and the ramified term ¼ tr(M(w,0)I(μ₀,f)) need invariant forms.
  - `cctrace6.tex` cites "Example 5.32" (line 681), which is now Theorem 5.13 and (5.10); "subsection 5.1.1" (line 143), which is now the *Test functions* paragraph of §4.4; "(5.16)" for τ (line 97), which is now (2.6)–(2.7); and "(5.27) … Example 5.23" (line 287), which has to be identified from context.
- *Stage 6:* `cctrace7.tex` cites "Example 5.26, (5.28)" (line 876), which is now Theorems 5.13 and 5.15. The stable form must account for the residual Weil representations V_b: their local packets {r⁺, r⁻} are Waldspurger's.
- *Stage 7 (or stage 0):* the master needs `\newtheorem{corollary}`. The Introduction's claim that there is no residual term must go (item II.9).

## Stage 5 notes (2026-11-11)

**Files.** `revised/sec6-invariant.tex` is the new Section 6, from `cctrace6.tex` (= `book7g.tex`; `book7gnw.tex` is a later version of the same chapter). `revised/preview.tex` now builds Sections 2–6, with the PDF committed. `revised/checks/sec6_n2_check.py` adds 33 checks (about 20 seconds; needs mpmath). `revised/checks/cover_lib.py` holds the cover helpers of `sec5_n2_check.py` (cocycles, Weil index, the spherical vector on w⁻¹n(y)), copied unchanged so that later scripts can import them. One sentence was added to `sec5-spectral.tex` (the comparison with [GJ] after Theorem 5.13).

**The sign of the ramified term** (checked before starting, as requested). The term +¼ tr(M(w,0)I(μ₀,f)) of Theorem 5.13(c) is correct. Three independent confirmations:
- *Arthur.* In the fine spectral expansion the discrete term has the positive coefficient |W₀ᴹ||W₀|⁻¹|det(s−1)|⁻¹ = ½·½ (Arthur [A14, Thm 8.2]; the same coefficient a_{M,s} appears in Müller–Speh's statement of the spectral side, arXiv:math/0211030).
- *Gelbart–Jacquet.* Their formula for GL(2) ([GJ, §6], as quoted with its numbers (6.34)–(6.37) in Badulescu's notes, arXiv:1904.09517) has the trace of R(f) on the discrete spectrum alone on the left, and on the right +(1/4π)∫tr(M(−iy)M′(iy)π_iy(f))dy − ¼ tr(M(0)π₀(f)). Moving both to the spectral side gives −(1/4π)∫tr(M⁻¹M′I) + ¼ tr(M(0)I), which is Theorem 5.15(e) term for term, including the ½ in front of the integral. So the report's "−¼" and our "+¼" are the same term on opposite sides. The classical Selberg trace formula agrees: the spectral side carries +¼φ(½)h(0), which is often written as −¼φ(½)h(0) on the geometric side.
- *First principles.* The script integrates |Λ^Y E(z,½+ir)|² over the modular surface for the Eisenstein series of SL(2,ℤ), from its Fourier expansion, and compares with the Maass–Selberg relation (5.9): agreement to 9 digits with the cross terms as stated, and a difference of about 2.7 with the opposite sign.

[JL] itself was not consulted; the statement about it in the report is covered by [GJ], which follows it.

**What changed, and why.**
- **The approach.** G has rank one and the cover of its only proper Levi A is abelian. So Arthur's construction of invariant distributions needs only Fourier inversion on the cover of A(ℚ_S), and everything in Section 6 except the normalization of the local intertwining operators is proved directly. Arthur [A6, A9, A10] and Li [II, IV] are cited for the general statements.
- **Non-invariance** (§6.1). u′_B(k,y) = −H(ky) (item II.15). Lemma 6.2: J_O(f^y) = J_O(f) + J^A_O(f_{B,y}) and J_χ(f^y) = J_χ(f) + J^A_χ(f_{B,y}), where J^A_O and J^A_χ are the two sides of the rank-0 trace formula of Section 3. Lemma 6.3: J_A(γ,f^y) = J_A(γ,f) + f_{B,y}(γ) + f_{B,y}(wγw⁻¹), and J_A(z,f^y) = J_A(z,f) + 2f_{B,y}(z). Lemma 6.4: for any intertwining family ℳ(λ), I(y)ℳ⁻¹ℳ′I(y)⁻¹ = ℳ⁻¹ℳ′ + H_y + ℳ⁻¹H_yℳ; this one identity gives the variance of every spectral term.
- **Normalization** (§6.2, item II.14). Theorem 6.5 states the properties (N1)–(N4) of the normalized operators R_v = r_v⁻¹M_v (Arthur [A11], Li II). Lemma 6.6 makes r_v explicit at the unramified places, r_v = L_v(2λ,χ_v²)/L_v(2λ+1,χ_v²), and at the real places: on the K-type of weight m the unnormalized operator is e^{iπm/2}·π2^{1−λ}Γ(λ)/(Γ((λ+1+m)/2)Γ((λ+1−m)/2)), and with r_v ∝ L_ℝ(2λ)/L_ℝ(2λ+1) the normalized operator is 1 on the weight ±½ and a finite product of factors (c−λ)/(c+λ) on the others. Corollary 6.7 defines the global factor m(μ,λ) and gives m′/m.
- **The invariant distributions** (§6.3). φ_A(f,π) = −tr(R_S⁻¹R_S′ I(π,f)), Φ_A(γ,f) is its inverse Fourier transform, and I_A(γ,f) = J_A(γ,f) − Φ_A(γ,f). Theorem 6.9 proves that I_A(γ,·) and I_A(z,·) are invariant. Φ_A(·,f) is compactly supported on each set {H_S = X} but not on the cover of A(ℚ_S); Example 6.C computes it at a real place (the Abel transform smoothed by kernels Σe^{−c|X|}).
- **The invariant trace formula** (§6.4). Theorem 6.11: Σ I_O = Σ I_χ with I_O = J_O − ½c_k Σ_γ Φ_A(γ,f) and I_χ = J_χ − ½Σ_μ (1/2π)∫φ_A; the corrections cancel by Poisson summation (Lemma 6.10). The spectral terms for χ ∈ 𝒳_A are −(1/2π)∫(m′/m) tr I (item II.16), plus the residual and ramified terms, which are already invariant.
- **The ramified term** (new). Proposition 6.13: M(w,0) = −1 on ℋ_B(χ_{ψ_b}) for every b, and the Eisenstein series of a ramified class vanishes at λ = 0. Proof: the Whittaker coefficients are L^S(λ+½,χη_a)/L^S(2λ+1,χ²) times entire local factors (Lemma 6.12), so they vanish at λ = 0 when χ² = 1; the constant term is then an automorphic function equal to (φ + M(w,0)φ)e^H, which must be 0. So the ramified term is −¼ tr I(χ_{ψ_b,0},f) (Corollary 6.14). For k = ℚ and b = ±1, ±2 the script confirms M(w,0) = −1 by a separate computation from local residues at ∞ and 2.

**Numbering map (1995 → 2026).** The 1995 numbers are those of `cctrace_new.tex` as compiled. Equations are now numbered (6.1)–(6.14).

| 1995 (compiled) | 2026 |
|---|---|
| f_{Q,y}, u′_Q, Example 6.1 | (6.1)–(6.3), Lemma 6.1, Example 6.A |
| Definition 6.2 (transpose), the spaces I_N(…)_Γ, (6.7) | the paragraph *The space containing φ_A(f)* after Theorem 6.9 |
| Conjectures 6.3, 6.4, 6.7, 6.8 (trace Paley–Wiener) | not needed; see the Section 6 introduction and the remark after Theorem 6.9 |
| Theorems 6.5, 6.9 (the maps φ_M), Example 6.6 | (6.11), Proposition 6.8 |
| Conjecture 6.10 (normalized operators) | Theorem 6.5, Lemma 6.6 |
| Lemma 6.11, Example 6.12, Lemma 6.13, Example 6.14 ((G,S)-classes) | Section 4.5 (Theorem 4.11); not repeated |
| m(χ,η), R(χ,η), φ_A(f,χ) | (6.10), Corollary 6.7, (6.11) |
| (6.13)–(6.18), Propositions 6.15, 6.16 (I = J − J′) | (6.12)–(6.14), Theorem 6.9, Lemma 6.10 |
| Proposition 6.17 (invariant fine expansion) | Theorem 6.11(a)–(c) |
| R_M(π_λ,P₀), Example 6.18 | the display after (6.11) (sign corrected) |
| J_M(π,X,f), I_M(π,X,f), Example 6.19, Proposition 6.20, Example 6.21 | the paragraph *Weighted characters* after Theorem 6.9 |
| Theorem 6.22 | Theorem 6.11(d)–(f), Corollary 6.14 |
| §6.4 | Theorem 6.11 |
| — | new: Lemmas 6.2–6.4, Lemma 6.6, Corollary 6.7, Lemma 6.10, Lemma 6.12, Proposition 6.13, Corollary 6.14, Examples 6.B–6.D, Remarks 2026.14–2026.16 |

The report's §6 numbers do not match the compiled text: its "Conjectures 6.2–6.5" are Conjectures 6.3, 6.4, 6.7, 6.8, its "Conjecture 6.6" is Conjecture 6.10, and its "Thm 6.23" is Theorem 6.22.

**Where this revision departs from the report.**
- *II.14.* The report asks that the conjectures be cited as Li II and Li IV. Li IV is conditional on an invariant Paley–Wiener hypothesis at real places (verified by Li for two-fold covers of Sp(2n), which covers this group). For SL(2) the hypothesis is not needed at all, so the section does not depend on it. The report also mentions Aoki's theorem at the real place, which `book7gnw.tex` cites as `\cite{Ao}`; the book's bibliography (`book9.tex`) has no such entry, and the reference is not used here.
- *II.16.* The report writes the surviving term as −(1/4π)∫(m′/m)(μ_it) tr I_B(μ_it,f) dt. That is the contribution of one μ; per class it is −(1/2π)∫ for an unramified class (two members) and −(1/4π)∫ for a ramified one, as in Theorem 6.11(e)–(f).
- *II.10.* See "The sign of the ramified term" above.

**Found in this stage, not in the report.**
- The 1995 R_A(π_λ,P₀) = R⁻¹ dR/dλ has the wrong sign: the limit of the (G,A)-family is −R⁻¹R′, as for M_B^T = 2T − M⁻¹M′.
- At an archimedean place f^y is not K-finite when f is, so invariance has to be stated on C_c^∞, not on the Hecke algebra.
- The 1995 claim I_ac(A) = I(A) = I_mod(A) for the torus is false (the analog of the stage-3 finding for ℋ_ac): φ_A(f) is not the Fourier transform of a compactly supported function.
- The condition |D(γ_v)|_v = 1 is needed for the unramified splitting I_A(γγ_v, f⊗e_v) = I_A(γ,f) (Theorem 6.9(d)): for a unit t with t² ≡ 1 mod ϖ the weighted orbital integral of the unit element is not 0.
- M(w,0) = −1 for all ramified classes (Proposition 6.13). For SL(2) this holds only for the trivial character; for a nontrivial quadratic character M(w,0) is not scalar [LL]. The double cover has no analog of that phenomenon in the principal series.
- The unramified Whittaker integral on the cover is 1 + (−a,ϖ)_v χ_v(ϖ)q^{−λ−½} (Lemma 6.12(c)); the constant c of the proof of Lemma 5.6(b) is (−1,ϖ)_v γ_v(ϖ).

**Minor §6 items from the report.** All fixed:
- §6 intro: "(3.1)" is now Theorem 5.15; "One of the objects to this subsection" is gone; f_S versus f^S follows Section 4.4.
- Conjecture 6.6(1) [compiled: 6.10(1)]: the intertwining property has I_{P′} on the right; it is (N1) of Theorem 6.5.
- After Conjecture 6.6: Sally's memoir is about the universal cover of SL(2,ℝ); for the double cover the real operators are explicit (Lemma 6.6(b)).
- Theorem 6.23 [compiled: 6.22]: v_π is ν_π; the theorem is replaced by Theorem 6.11 and Corollary 6.14.
- The stale references in `cctrace6.tex` listed in the Stage 4 notes: "Example 5.32" is (5.10); "subsection 5.1.1" is the *Test functions* paragraph of §4.4; "(5.16)" is (2.6)–(2.7); "(5.27) … Example 5.23" is the term J_χ of Theorem 5.13, into which Corollary 6.7(a) is substituted in the proof of Theorem 6.11.

**Still resting on citation and numerics only** (Remarks 2026.14, 2026.15):
- Theorem 6.5 at the bad places (dyadic places, places where ψ_v or μ_v is ramified): the factors r_v are Li's and are not explicit. The expected choice, L_v(2λ,χ_v²)/L_v(2λ+1,χ_v²) times an exponential, has not been verified there. I_A(γ,f) and m′/m depend on the choice; the trace formula holds for each choice.
- In Lemma 6.6(a): generic irreducibility of the local principal series, the adjoint formula, and rationality.
- The estimates behind Proposition 6.8(a) for functions that are not K-finite.
- In Lemma 6.2: the interchange of integrals on the spectral side.
- The definition (6.13) has not been compared with Li IV in detail.
- As before: S must be large for the given f_S, and the coefficients a^G(S,u_ξ) are not computed.

**For later stages.**
- *Stage 6:*
  - the stable form starts from Theorem 6.11 and Corollary 6.14. `cctrace7.tex` §7.8(g) has the m′/m term, now Theorem 6.11(e)–(f);
  - the discrete part is Σ m_disc(π) tr π(f) − ¼ Σ_b tr I(χ_{ψ_b,0},f). Since M(w,0) = −1, the principal series contributes no multiplicity-type term; the packet structure has to come from the Weil representations V_b (Waldspurger) and from the cuspidal spectrum;
  - I_A(γ,f) depends on the normalizing factors; the comparison with GL(2)-conjugation in §7 should use the same choice on both sides;
  - Lemma 6.12 (Whittaker coefficients L^S(λ+½,χη_a)/L^S(2λ+1,χ²)) is the SL(2) case of the Shimura correspondence at the level of Eisenstein series and may be useful there.
- *Stage 7 (or stage 0):* the master needs the bibliography entries added to `preview.tex` in this stage ([A6], [A10], [A11], [GJ], [Li II], [Mo2], [Sa]). The Introduction should say that the invariant formula is unconditional for this group. Making the dyadic normalizing factor explicit would give m = Λ(2λ,χ²)/Λ(2λ+1,χ²) exactly.

## Second referee report (2026-11-11)

An independent referee report on `revised/preview.tex` (Sections 2–6) was written by ChatGPT: `referee-2026-11/report-chatgpt.md`. The point-by-point response is `referee-2026-11/response.md`. Authors are now "D. Joyner and Claude"; ChatGPT is credited in the Acknowledgements.

**Files.** New: `revised/sec1-introduction.tex` (overview, literature review, proved/cited table, running example), `revised/appA-comparison.tex` (all comparisons with the 1995 notes and the 1997 manuscript, moved out of the body), `revised/glossary.tex`. Changed: all five section files, `preview.tex` (abstract, table of contents, acknowledgements, 36 new bibliography entries), `checks/sec2_n2_check.py` (+10 checks), `checks/sec5_n2_check.py` (+5 checks). The PDF is now 75 pages.

**Mathematical changes.**
- *Topology (report 1.1, 1.3).* Kubota's cocycle is Borel, not continuous: β(a(t), n̄(c)) = (c,t)_v. Lemma 2.1 now fixes the topology of the cover by a base of neighborhoods (V,1), V ⊂ U, where β ≡ 1 on U × U; new Example 2.A; new Lemma 2.2(i) (the continuous sections). C_c^∞ of a cover is defined on the topological group, not through g ↦ f(g,1); the unit e_p is the standard counterexample to the old definition. The adelic cover has the quotient topology of the restricted product. Section 3 follows.
- *Lemma 3.1(c).* The proof no longer claims that a continuous character has open kernel.
- *b′ = −b.* New Lemma 5.7: in Kubota's model, with ω_{ψ′}(n(u)) = ψ′(ux²), ω(a(t),ζ)φ(x) = ζ χ_{ψ′₋₁}(a(t),1)|t|^{1/2}φ(tx). Hence V_b ≅ r⁺_{ψ_{−b}} (Theorem 5.8(c)); Example 5.B corrected (Gaussian e^{−2πξ²}). This closes the open item of the Stage 4 notes.
- *Normalizing factors.* Lemma 6.6(c) treats χ_v = sgn^ε|·|^{iτ} at real places. §6.2 separates existence, explicit formula and global compatibility.
- *M(w,0) = −1.* Proof of Proposition 6.13 expanded (four steps; bounded elementary generation of SL(2,𝔸)).
- *Claims.* "Every term explicit" is gone. Theorems 4.11, 5.16, 6.11 say that a^G(S,u_ξ) and the r_v at S_bad(μ) are defined, not evaluated.

**Renumbering.** Section 5: statements from 5.7 on move up by one, equations from (5.5) on by two. Section 2: Examples 2.A, 2.B → 2.B, 2.C. Remarks: old 2026.2 is in Appendix A; 2026.3, 2026.4 → 2026.2, 2026.3; new 2026.4 (status of §2) and 2026.7 (status of §3); from old 2026.7 on, add one. The numbering maps in the stage notes above use the old numbers.

**Still open after this round.** The coefficients a^G(S,u_ξ); explicit r_v at dyadic and ramified places (Szpruch and Goldberg–Szpruch are now cited but not used); T ≥ 0 on the spectral side; Li IV's definitions versus (6.13); stage 0 and stage 6.

**Literature review.** Bibliographic data for the new entries were checked online on 2026-11-11, except [He], [JL], [Sel], [Sh], [Shi], [Mat], [BD], [Wa81], which are standard and were entered from memory, and [J88], [GPS83], which follow `book-1997/book9.tex`. Worth a glance by DJ: the title of [J88].

# Revision log: metaplectic trace formula for SL(2)

This log tracks every item of the 2026 referee report ([Claude Docs](https://claude.ai/artifact/7MmqhX7GnoJNup9xbb9RNG)) through the revision. Section numbers refer to `original-1995/cctrace_new.tex` as compiled; item numbers match the report.

## Decisions

- **n = 2 only** (decided 2026-11-10). The revision treats the 2-fold cover of SL(2) over a number field k. Several general-n items become moot; they are marked *moot (n = 2)* below. For n = 2, μ₂ ⊂ k always holds, real places occur, and the archimedean covers are Mp(2,ℝ).
- Sections 4–6 are to be presented as Wen-Wei Li's theorems for covers (Li I–IV), specialized to SL(2). The explicit SL(2) formulas are the paper's contribution.
- Unverified claims are kept, marked with a Remark (2026).

## Stages

| Stage | Scope | Status |
|---|---|---|
| 0 | Clean source tree: `cctrac3b.tex` from `book7d.tex`, remove Scientific Word macros, `\numberwithin`, `\label`/`\ref`/`\cite`, bibliography fixes. No mathematical changes. | Done 2026-11-11 (see *Stage 0 notes*): `clean-1995/` compiles; the master of the revised paper is `revised/sl2bar-trace-2026.tex` (was `preview.tex`). The conversion of the hand-typed 1995 cross-references to `\label`/`\ref` was dropped as superseded |
| 1 | §2 foundations: κ-splitting, global cover, genuine conventions, center, NAK, measures, GL(2) cover | Done 2026-11-10: `revised/sec2-foundations.tex`, checked by `revised/checks/sec2_n2_check.py` (see *Stage 1 notes*). Written before stage 0, as a standalone file for the stage-0 master to `\input`. |
| 2 | §3 rank 0 (much simpler for n = 2: the cover of A is abelian) | Done 2026-11-10: `revised/sec3-rank0.tex`, checked by `revised/checks/sec3_n2_check.py` (see *Stage 2 notes*) |
| 3 | §4 and `cctrac3b.tex`: geometric side | Done 2026-11-10: `revised/sec4-geometric.tex`, checked by `revised/checks/sec4_n2_check.py` (see *Stage 3 notes*) |
| 4 | §5 spectral side: residual (Weil representation) spectrum, ramified χ, M_B^T | Done 2026-11-10: `revised/sec5-spectral.tex`, checked by `revised/checks/sec5_n2_check.py` (see *Stage 4 notes*) |
| 5 | §6 invariant form | Done 2026-11-11: `revised/sec6-invariant.tex`, checked by `revised/checks/sec6_n2_check.py` (see *Stage 5 notes*) |
| 6 | §7 stable(r) form | Done 2026-11-11: `revised/sec7-stable.tex`, checked by `revised/checks/sec7_n2_check.py` (see *Stage 6 notes*). Also: Section 1, Appendix A and the Glossary extended to Section 7; the unipotent coefficients of Theorem 4.11(a) computed; two corrections in Sections 4 and 5 |
| 5R | Response to the second referee report (ChatGPT, on Sections 2–6): topology of the cover and test functions, b′ = −b, Section 1 (overview, literature review), Glossary, Appendix A (comparisons with 1995), acknowledgements | Done 2026-11-11: see *Second referee report* below and `referee-2026-11/` |
| 7 | Consistency pass after stage 6, and a second look at Section 7. (The independent re-referee, the literature review, the title page and the Introduction for Sections 2–6 were done in 5R; the Introduction, Appendix A and the Glossary were extended to Section 7 in stage 6.) | Done 2026-11-11 (see *Stage 7 notes*): cross-references, citations and numbering checked mechanically; three corrections in Section 7 (the condition (N5), the paragraph on Waldspurger's packets, Example 7.E); Proposition 7.5 now proved on the regular set; title page. **Section 7 still has no independent referee report**: none was in `referee-2026-11/` |
| 8 | Style-guide pass: preamble, title page, AI disclosure, citation keys, literature review, Section 8, examples, Appendix A moved to this log | Done 2026-11-12 (see *Stage 8* below) |

## Items

Status values: open, fixed, moot (n = 2), deferred.

### Major issues I: the cover, conventions, global construction (stage 1)

| # | Location | Issue | Status |
|---|---|---|---|
| I.1 | Lemma 2.2(b), before Lemma 2.4, Lemma 2.8, §2.1.4, §7.4 | Splitting over K is k ↦ (k, κ(k)), not k ↦ (k,1) | fixed in §2 (Lemma 2.2(b), K*_p, Hecke unit (2.8)); in §7 the identification of K with (K,1) is no longer used, and Lemma 7.1(e) shows that Ad(h) preserves K* for h ∈ Z·GL(2,𝒪) |
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
| II.6 | (4.5), §5.4(a) | Unipotent terms in central classes (book7d, book7f have them) | 3, 4 | fixed in §4: Prop. 4.8 (explicit, via the zeta integral Z(f,s)) and Thm 4.11(a) (fine form); in §5: Thm 5.15(a) uses Thm 4.11(a) in full; in §6: Thm 6.11(a); the coefficients a^G(S,u_ξ) are computed in stage 6 (Prop. 7.10) |
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
| II.18 | §7.2 | GL(2) action on the cover; non-abelian preimage of T₁ | 1, 6 | fixed: cover of GL(2) and its action defined in §2.3 (Lemma 2.10); Ad(h) made explicit (Lemma 7.1); the sign by which T₁ acts on the lifts of γ is (det h, det(1+γ)) (Lemma 7.2); stable conjugacy is the twisted action h⋆x (§7.2), which removes the ambiguity. The choice between the two covers of GL(2) does not matter (Remark 2026.2) |
| II.19 | Prop. 7.1, Lemma 7.3 | T(Q) not discrete in T(A_S); index 2 (Hasse norm theorem) | 6 | fixed: Theorem 7.7 is adelic, with the factor ½ from the Hasse norm theorem and class field theory. Poisson summation on T (1995 Prop. 7.2 as compiled) is not used for the cover; see *Stage 6 notes* |
| II.20 | §7.4 | D(A/F): A·Z vs A₁; global index undefined | 6 | fixed: for a hyperbolic element the stable class is the conjugacy class, so there is no sum over D(A/·); F^×/F^{×2} acts on the two lifts by (a,t), and I_A transforms by that character (Prop. 7.9) |
| II.21 | (7.17) | Divergent sum over rational unipotent classes | 6 | fixed: Prop. 7.10 expands the zeta integral in the quadratic Hecke characters unramified outside S (a finite sum), which gives a^G(S,u_ξ) = ½(c_S + Σ_{κ≠1} κ_S(ξ) L^S(1,κ)) |
| II.22 | (7.13), book7d | v_A at p-adic places is log max(1,\|n\|) | 3, 6 | fixed in §4 (Lemma 4.9: log max(1,\|y\|) finite, ½log(1+y²) real, log(1+\|y\|²) complex); §7 uses Lemma 4.9 and has no separate formula |
| II.23 | §7 | Results deferred to [J1], [J3]; Lemma 7.18; Remark 7.17 | 6 | fixed or marked, statement by statement (see the table in *Stage 6 notes*): the variance lemmas are proved (Lemma 7.8, Prop. 7.9, under the new condition (N5)); the lemmas about characters of tori are dropped (tori are not endoscopic groups of the cover); the germ lemmas at ±1 are not proved and are listed as open in §7.8; Remark 7.19 (as compiled) is false in general; Conjecture 7.24 (as compiled) is false as stated |

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
| C.1 | Matrix identity in the v_A claim is wrong; correct factorization w·n(x) = n(−x⁻¹)·diag(x⁻¹,x)·n̄(x⁻¹) | fixed: not needed (the weight is Lemma 4.3/4.9; its variance under GL(2) is Lemma 7.8(a)); recorded in Appendix A |
| C.2 | #L(π) with k_v^×/k_v^{×n} | moot (n = 2) |
| C.3 | Real Hilbert symbol misdefined | fixed: (H3) of §2; recorded in Appendix A |
| C.4 | L-group of the 2-fold cover is SL(2,ℂ), not PGL(2,ℂ) | fixed: paragraph *The dual group* in §7.2 |

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

## Stage 6 notes (2026-11-11)

**Files.** `revised/sec7-stable.tex` is the new Section 7, from `cctrace7.tex` (= `book7h.tex`) and the parts of `book3b.tex` about conjugation by GL(2). `revised/preview.tex` now builds Sections 1–7, with the PDF committed (100 pages); it has four new bibliography entries ([HI13], [How], [Mak], [Th08]). `revised/checks/sec7_n2_check.py` adds 28 checks (about 3 seconds; needs mpmath). Also changed: `sec1-introduction.tex` (overview, literature, table, running example), `appA-comparison.tex` (new subsection on Section 7), `glossary.tex`, and small edits in `sec2`–`sec6` listed below.

**What changed, and why.** The 1995 section follows Labesse–Langlands: stable conjugacy is conjugation by G₁ = GL(2), the endoscopic groups are the elliptic tori, and the κ-orbital integrals are to be handled by Poisson summation on the tori. For the double cover the first step already fails, and the new section is built on what replaces it.

- **Conjugation by GL(2)** (§7.1). Ad(h) is the unique automorphism of the cover over g ↦ hgh⁻¹ (Lemma 7.1). For δ_a = diag(a,1): Ad(δ_a)(g,ζ) = (δ_a g δ_a⁻¹, ζ) if c ≠ 0 and (δ_a g δ_a⁻¹, (a,d)_v ζ) if c = 0. On the cover of A it is multiplication by the character (a,t)_v; on the lifts of −1 it is the sign (a,−1)_v. If h commutes with a semisimple γ ≠ −1, then Ad(h)(γ,ζ) = (γ, (det h, det(1+γ))_v ζ) (Lemma 7.2). The proof: with z = 1+γ, γ·det(z) = z² in the commutative algebra F[γ], and the commutator of a scalar λ with h in the cover of GL(2) is (λ, det h)_v. So GL(2)-conjugation can carry a lift of γ to the other lift (always for a(t) with t not a square; for elements near −1 in the torus of ℚ₃(√3), Example 7.A).
- **Stable conjugacy** (§7.2). h⋆x = (det h, det(1+x))_v · Ad(h)x is an action of GL(2,F) on the elements of trace ≠ −2. Its orbits are the stable classes. Lemma 7.3: the function Δ_ψ(g,ζ) = ζ (c, D⁺)_v γ_v(D⁺)/γ_v(1), D⁺ = det(1+g), c ≠ 0, extends to a genuine class function on the regular semisimple set, constant on the ⋆-orbits; the proof is algebraic (invariance under n(u), a(s), w, the last by (X, Y²−X)_v = 1). On the cover of A it is the complex conjugate of Weil's character χ_ψ. Proposition 7.5: Δ_ψ·|D⁺|^{−1/2} is the character of r⁺_ψ − r⁻_ψ, so the definition is that of Adams and Li. This uses the kernel of ω(g,1) in Kubota's model (Lemma 7.4), γ(c)⁻¹|c|^{−1/2}ψ((αx²−2xy+dy²)/c), whose constant is confirmed by composing kernels: the Weil indices reproduce Kubota's cocycle exactly.
- **κ-orbital integrals** (§7.3). In a GL(2)-class there are two combinations of orbital integrals, J^st and J^κ (κ = κ_E). Lemma 7.6(c): J^κ(x, f) = J^st(z̃x, f(z̃⁻¹·)) for a lift z̃ of −1, because det(1+γ)·det(1−γ) = −4θy², so η_γ η_{−γ} = κ_E·(·,−1)_v. This is the elementary form of the relation between Li's two endoscopic data (1,0) and (0,1).
- **Elliptic regular terms** (§7.4, Theorem 7.7). Rational elements conjugate under GL(2,k) are stably conjugate at every place, by the product formula for η_γ; this is what the twist is for. Then Σ_{O elliptic} J_O(f) = S_ell(f) + S_ell(f₋), with S_ell(f) = ½ Σ_γ vol · J^st(γ, f) stable and f₋(x) = f(s(−1)x). This is the shape of Li's theorem [Li15, Thm 5.2.6] for n = 1 (two data, ι = ½ each).
- **Hyperbolic terms** (§7.5). Theorem 6.9 extends from conjugation by the cover to Ad(h), h ∈ GL(2,k_S): I_A(x, f∘Ad(h)) = I_A(Ad(h)x, f) (Lemma 7.8, Proposition 7.9). This needs a new condition (N5) on the normalizing factors: r_v(π_v κ_a, λ)/r_v(π_v, λ) is independent of λ. So I_A(a(t), ·) transforms by (det h, t)_S. It is not stable, and the section says so.
- **Unipotent coefficients** (§7.6, Proposition 7.10). For S ⊃ {∞, 2, ram ψ} with 𝒪_S principal: Z(f,s) = ½ Σ_κ L^S(s,κ) Z_S(Φ_S,κ_S,s) over the 2^{|S_k|} quadratic Hecke characters unramified outside S. Taking the finite part at s = 1 proves Theorem 4.11(a) from Proposition 4.8 and gives a^G(S,u_ξ) = ½(c_S + Σ_{κ≠1} κ_S(ξ) L^S(1,κ)), where ζ_k^S(s) = ρ_S/(s−1) + c_S + …. For k = ℚ, S = {∞,2}: c_S = (γ_E + log 2)/2 and the L-values are π/4, log(1+√2)/√2, π/(2√2) (Example 7.E). This closes the item "coefficients a^G(S,u_ξ)" that was open after stages 3–5 and 5R.
- **Spectral side** (§7.7). GL(2,k) acts on automorphic forms, with V_b ↦ V_{ab} (Lemma 7.11). The theta functions of ψ_{−b} span Θ_b ≅ ⊕_{Πε_v = 1} ⊗ r^{ε_v}, and tr(R(f)|Θ_b) = ½Θ^st_b(f) + ½Θ^st_b(f₋) with Θ^st_b = Π_v (tr r⁺ − tr r⁻) stable (Proposition 7.12). The terms of the continuous spectrum are stable.
- **The stable(r) form** (§7.8, Theorem 7.13) collects this, and lists what is missing for I(f) = S(f) + S(f₋): the germ formulas at ±1, the stabilization of the weighted terms, the transfer to SO(3), and the packets of the cuspidal spectrum.

**Numbering map (1995 → 2026).** The 1995 numbers are those of `cctrace_new.tex` as compiled. Equations are now numbered (7.1)–(7.14).

| 1995 (compiled) | 2026 |
|---|---|
| Definition of stable conjugacy, Remark 7.1 | §7.2 (replaced by the twisted action), Lemma 7.3, Proposition 7.5 |
| (7.1), (7.2), (7.25), §7.8 (a)–(i) | Theorem 7.13 and the paragraph after it |
| §7.2: endoscopic groups, D(T/F), D(T/ℚ), D(T/𝔸) | paragraph *The dual group* in §7.2; F^×/NE^× in §7.3; 𝔸_k^×/N𝔸_E^× in §7.4 |
| Proposition 7.2 (Poisson summation on T), Remark 7.3, Corollary 7.4 | not used (Lemma 7.6(c) replaces them); Theorem 3.4 remains available for tori |
| (7.5)–(7.8), Lemma 7.5 | (7.7), (7.10), Lemma 7.6, Theorem 7.7 |
| §7.4: (7.9)–(7.11), Lemma 7.6 | Proposition 7.9 (equivariance; stability not claimed) |
| Lemma 7.7 (F^∨ = \|a₁−a₂\| J_G) | proof of Proposition 7.9(c) (and of Theorem 6.9(a)) |
| Lemmas 7.8, 7.9, 7.23 (the operator N(g); variance under G₁) | Lemma 7.8 |
| (7.13), (7.14), Remark 7.10 | Lemma 4.9 and (4.12); nothing new |
| §7.5: (7.15), Lemma 7.11 | Theorem 6.11(a), Proposition 7.10(c) |
| Definitions 7.12, 7.13 (Φ^{T/κ}) | (7.7); the factor is Δ_ψ (Lemma 7.3) |
| Lemmas 7.14–7.16, Remark 7.17 (germs at ±1) | not proved; §7.6 (last paragraph) and §7.8 (i) |
| (7.17) | Proposition 7.10(a)–(c) |
| (7.18) | (6.11) |
| Definition 7.18 (L(π)), Remark 7.19 | Lemma 7.11, Proposition 7.9(c), Lemma 7.4; see Appendix A |
| Lemmas 7.20, 7.21, Remark 7.22, (7.19)–(7.21) | dropped (characters of tori) |
| (7.22)–(7.24): S₁, S₂, S₃; Conjecture 7.24 | Φ_A, J_A, J^κ_unip; Theorem 7.13(c) and the paragraph after the theorem |
| — | new: Lemmas 7.1–7.4, Proposition 7.5, Lemma 7.6(c), Proposition 7.10, Lemma 7.11, Proposition 7.12, Examples 7.A–7.E, Remarks 2026.18–2026.20, condition (N5) |

The report's §7 numbers do not match the compiled text (it does not count the remarks): its "Proposition 7.1" is Proposition 7.2, "Lemma 7.3" is Lemma 7.5, "Lemma 7.6" is Lemma 7.7, "Lemma 7.9" is Lemma 7.9, "Def. 7.11" is Definitions 7.12–7.13, "Lemmas 7.11, 7.12" are Lemmas 7.14, 7.15, "Lemma 7.13" is Lemma 7.15 or 7.16, "Remark 7.17" is Remark 7.19, "Lemma 7.18" is Lemma 7.20, "Lemma 7.20" is Lemma 7.23, and "Conjecture 7.21" is Conjecture 7.24.

**Where this revision departs from the report.**
- *II.18.* The report asks to "resolve the non-abelian preimage of T₁" before (7.5)–(7.7) make sense. The resolution is not a choice of cover: the character by which T₁ acts on the lifts of γ is (det h, det(1+γ)), it is not trivial on the norms in general, and the definition of stable conjugacy has to change. The report's remark that δ ↦ I_O(f^δ) is defined on D(T/F) "only up to a character" is exactly this.
- *II.19.* The report asks that Proposition 7.1 (Poisson summation on T) be stated over T(𝔸). For the cover it is not needed at all: the κ-orbital integrals are stable orbital integrals of f₋.
- *II.20.* The report suggests that F^×/F^{×2} in D(A/F) may be deliberate and must be justified. It cannot be: there is nothing to sum over for a hyperbolic class. What is true is the equivariance of Proposition 7.9.
- *II.21.* The report points to Arthur's coefficients a^G(S,u) and to the zeta regularization of [LL] as two ways out. They are the same computation here, and it gives the coefficients.
- *II.23.* The report asks that the deferred statements be cited from published versions or marked conditional. [J1] and [J3] were not written. The statements are now proved, dropped or listed as open, as in the table above.
- *"Present Section 7 explicitly as a program."* Done in §7.8: the theorem states what is proved, and the paragraph after it what is missing. The section does not claim a stabilization.
- The report recommends [Li11] as "the relevant comparison point". The comparison is made at the level of definitions (stable conjugacy, Proposition 7.5) and of shape (Theorem 7.7 against [Li15, Thm 5.2.6]); the transfer itself is not used.

**Found in this stage, not in the report.**
- **(5.5) (fixed in `sec5-spectral.tex`).** In Kubota's model ω_{ψ′}(w,1)φ(x) = γ′(1)⁻¹ ∫ φ(y) ψ′(−2xy) dy. The stage-4 text had c·∫ φ(y) ψ′(2xy) dy with an unspecified constant c; the two differ by the reflection x ↦ −x, which is not a scalar. Lemma 5.7 and its proof are not affected (the reflection commutes with multiplication operators), but Lemma 7.4 needs the correct form.
- **Theorem 4.11(a) (fixed in `sec4-geometric.tex`).** The integral of Lemma 4.10(c) depends on the representative ξ of the class u_ξ, through |c|_S⁻² for ξ ↦ ξc². J_G(zu_ξ, f_S) is now |ξ|_S times that integral, which depends only on the class; with this normalization the coefficients a^G(S,u_ξ) are well defined.
- **Remark 2026.2 (updated in `sec2-foundations.tex`).** Section 7 uses the cover of GL(2) only through Ad(h), which does not depend on the choice between σ and σ′.
- The 1995 Conjecture 7.24 (S₁ + S₂ + S₃ is invariant under G₁(𝔸_S)) is false for the cover as stated: the term of a(t) is multiplied by (det h, t)_S.
- The 1995 Remark 7.19 (#L(π) = Π #(k_v^×/k_v^{×2}) for every genuine π) is false in general: I(π)∘Ad(δ_a) = I(πκ_a) ≅ I(π) when χ_v² = (a,·)_v.
- `book3b.tex` asserts that the genuine orbital integral at a lift of a(t) vanishes unless t is an N-th power. For n = 2 it does not vanish; its average over the GL(2)-orbit does (Lemma 7.6(b)).
- The part of the trace formula that is invariant under all of GL(2,k_S), which the 1995 notes take as the stable part, sees only the γ for which det(1+γ) is a square or θ times a square at the places of S.

**Edits to earlier sections.** `sec2`: Remark 2026.2, the sentence after Lemma 2.10, two cross-references. `sec3`: one sentence in the introduction. `sec4`: the normalization of J_G(zu_ξ, f_S) before Theorem 4.11; "not evaluated" replaced by pointers to Proposition 7.10 (roadmap table, Theorem 4.11(a), the paragraph after it, Remark 2026.10). `sec5`: (5.5) and the sentence in the proof of Lemma 5.7; Theorem 5.16(a). `sec6`: the paragraph after Theorem 6.11 and Remark 2026.16 (one unevaluated ingredient instead of two). No numbering changed in Sections 2–6.

**Minor §7 items from the report.** All fixed or moot:
- "Lemma 7.3(a) is about I^st_O, not SI_O": Theorem 7.7 and (7.11).
- "The index [D(T/ℚ):D(T/𝔸_S)] should be inverted": it is the factor ½.
- "Lemma 7.13's statement has a missing '=' and a γ-dependent constant inside a limit": the lemma is not kept.
- "(7.25) vs (7.1)–(7.2)": one statement, Theorem 7.13.
- The stale references in `cctrace7.tex` listed in earlier notes: "Example 5.26, (5.28)" (line 876) is Theorems 5.14 and 5.16; "section 2.7" is Section 3; "Proposition 6.20", "Proposition 4.19", "Example 4.14" are Theorem 6.11(a), Theorem 4.11 and Lemma 4.10.

**Still resting on citation and numerics only** (Remarks 2026.18, 2026.19):
- Proposition 7.5: that the character of the Weil representation is computed by integrating the kernel over the diagonal ([Mak], [Th08]); our derivation of (7.6) from (7.5) is formal. Checked: the real place (Example 7.B), the Weil representation of SL(2,𝔽_p) (Example 7.C), the split torus, and the algebraic properties of Δ_ψ. Not compared with the formulas of [Th08] directly.
- The condition (N5): shown for the explicit factors; for Li's factors at the bad places it is assumed, with an indication of why it can be arranged (Remark 2026.18).
- Lemma 7.1(c) through the cocycle (2.13) on GL(2) ([K2], numerics); it is also checked directly as a homomorphism for β.
- Proposition 7.12(a): convergence and square-integrability of theta functions.
- All statements about [Li11], [Li15], [Li21] in the text are comparisons, not used in proofs. Bibliographic data for [HI13], [How], [Mak], [Th08] were checked online on 2026-11-11; [Li11] and [Li15] were consulted for the definitions and for Théorème 5.2.6 (first part of each paper only).

**Not done.** The germ formulas for κ-orbital integrals at ±1 on the cover (1995 Lemmas 7.14–7.16); the stabilization of I_A; the transfer to SO(3) and the comparison of Δ_ψ with Li's transfer factor; the cuspidal spectrum; Proposition 7.10 when 𝒪_S is not principal (it should follow from Poisson summation on 𝔸_k^×/k^×𝔸_k^{×2}).

**For later stages.**
- *Stage 7:*
  - an independent referee report on Section 7; the points most in need of a second look are Proposition 7.5 (formal step), Lemma 7.8(c) with (N5), and the paragraph on Waldspurger's theorem after Proposition 7.12;
  - the acknowledgements say that ChatGPT refereed Sections 2–6, which is still accurate;
  - the title of the paper ("basic theory" in 1995) and of Section 7 ("stable(r) form");
  - Remark 2026.9 (r(t) against the general definition in [A7]) and Remark 2026.13 (T ≥ 0 on the spectral side) are unchanged.
- *Stage 0:* the master needs `\input{sec7-stable}` and the four new bibliography entries. No new environments.
- *Possible follow-up, outside the stages:* identify J^st with Li's stable orbital integral on SO(3) for the unit of the Hecke algebra (a direct fundamental lemma for this group), which with Theorem 7.7 would give the elliptic part of the Shimura–Waldspurger correspondence in trace-formula form.

## Stage 7 notes (2026-11-11)

**Scope.** A consistency pass over `revised/` (Sections 1–7, Appendix A, Glossary, `preview.tex`, READMEs), and a second reading of Section 7 aimed at the three points listed under "For later stages → Stage 7" and at the list "Still resting on citation and numerics only" in the Stage 6 notes. No referee report on Section 7 was found in `referee-2026-11/` (it holds only `report-chatgpt.md` on Sections 2–6 and `response.md`), so there is nothing to respond to and `response.md` is unchanged. The second reading below was done by Claude in a new session, with the stage-6 text as the only input; it is not an independent report, and the paper says that Section 7 has not been refereed independently (Remark 2026.19).

**Consistency checks (mechanical).** All pass on the stage-6 text, and again after the edits:
- `preview.tex` builds with no LaTeX warning, no undefined or duplicate label, no overfull box; 102 pages.
- Every `\cite` key has a `\bibitem` and every `\bibitem` is cited (80 entries with the new [Th13]).
- No statement number of this paper is typed by hand: every number in the prose that is not a `\ref` refers to the 1995 notes or to another paper (35 lines in Appendix A, 11 elsewhere).
- No stale "stage", "not yet", "to be written" wording in the body. The three remaining "defined but not evaluated" (abstract, §1.3, §6.4) are about the normalizing factors at the bad places, which is still true.
- Section 1 against the theorems: the display in §1.1 agrees with Theorem 6.11 and Corollary 6.14 (signs, the factors ½ and ¼, 1/2π); Theorem 7.13(a) agrees with Theorem 6.11(a)–(c) and Proposition 7.10(c); the running example agrees with Examples 7.A, 7.B, 7.D, 7.E.
- Appendix A and the Glossary cover every statement and symbol of Section 7.
- All check scripts pass: sec2 114, sec3 35, sec4 19, sec5 50, sec6 33, sec7 33 (28 + 5 new).

**The three points flagged in stage 6.**

1. *Proposition 7.5 (the formal step).* The step is now a proof. For f supported in the regular set one reduces by conjugation to f supported where c ≠ 0. At a finite place ω(f) has finite rank and a Schwartz kernel, so its trace is the integral of the kernel over the diagonal; the integrals of ψ(Dξ²/c) over the lattices ϖ^{−M}𝒪 are independent of M for M ≥ M₀, uniformly on the support of f, which justifies the interchange. At an archimedean place the same is done with a Gaussian cut-off and dominated convergence; there the trace-class property and the Schwartz kernel are cited. What is still cited at every place is the regularity theorem (the character is a locally integrable function on the whole group), which is needed to call Θ⁺ − Θ⁻ a stable character and for the second formula for Θ^st_b in §7.7; the statement of the proposition now separates the two. Two comparisons were added after the proof. (a) The character of ω itself, new equation (7.7), equals (−c, D⁻)·γ(1)γ(det(g−1))|det(g−1)|^{−1/2}, which is Thomas's formula [Th08, Theorem 1C]; that theorem is stated up to sign, so this is agreement up to the sign it leaves open. (b) ω(−1,1) = γ(1)²P gives Θ⁺(x) − Θ⁻(x) = γ(1)^{−2} Θ_ω((−1,1)x), the form of [Th13, Theorem D], and (7.7) at (−1,1)x does give (7.6). Both are in the script. Not done: matching the normalization of the Weil index in [Th08], [Th13] with ours, and a comparison with [Mak].

2. *Lemma 7.8(c) and the condition (N5).* The computation in the proof is correct; it was redone independently (the relation M(π′,λ)A(λ) = c(λ)A(−λ)M(π,λ) with c(λ) = π^w(b̃)|a|^{−λ}, the derivative, the cancellation of log|a|). Two things were wrong around it.
   - **Remark 2026.18 (corrected).** The recipe "redefine r_v(π_vκ_a, λ) = c(λ) r_v(π_v, λ)" contradicts (N5): c(λ) contains |a|^{−λ}, so the quotient depends on λ, and with that choice the term log|a| in the proof does not cancel. The correct equivalent of (N5) is R_v(π_vκ_a, λ) = C·|a|^{−λ} A(−λ) R_v(π_v, λ) A(λ)^{−1}. The recipe also ignored (N2): when π^w = πκ_{a₀} with a₀ not a square (χ² = (a₀,·) ≠ 1), the factor of π itself is constrained, so transport along the orbits of k_v^×/k_v^{×2} does not by itself produce factors with (N1)–(N5).
   - **"The factors can be chosen with (N5)" (withdrawn).** This is not proved. (N5) is now stated as a hypothesis at the places where the factors are not explicit. It holds for the explicit factors (always at the real and complex places), and whenever r_v depends on π_v only through χ_v² up to a constant.
   - New in Lemma 7.8: part (c) is stated without (N5), with the extra term −d_a(π,λ) tr I(π′_λ, f), d_a = Σ_v (r_v′/r_v(π_vκ_a, λ) − r_v′/r_v(π_v, λ)), so that one sees exactly what (N5) removes; new part (d): r(π,λ)r(π^w,−λ) and the same product for πκ_a agree up to a constant sign, so (N5) is compatible with (N2).
   - Proposition 7.9(c) (stability of the principal series characters) does not use (N5); this is now said. Section 1 (table in §1.3 and the paragraph after it) now says that the statements about the weighted terms and the I_χ are under (N5).

3. *The paragraph on Waldspurger's theorem after Proposition 7.12 (corrected).* It said that the stable character of a packet is Π_v (tr π_v⁺ − tr π_v⁻). That is right for the theta packets and wrong for the packets of cuspidal σ, where the stable combination is the sum. Two cases are verified in the text: the packet {sp, r⁻} of the Steinberg representation (tr sp + tr r⁻ = tr I − (tr r⁺ − tr r⁻), a difference of stable characters), and the real discrete series packets (weights m, m+2, … and −m, −m−2, …: the sum of the characters on k̃_θ is −sin((m−1)θ)/sin θ, even; the difference is i cos((m−1)θ)/sin θ, odd). In both kinds of packet the two members have opposite central characters, so the unstable combination for f is the stable one for f₋ up to a constant. The description of the real packets (which discrete series go together) and the labels π^± were not checked against [Wa91]; the text says so.

**Other corrections in Section 7.**
- *Example 7.E.* "a^G(S,u_{−1}) ≈ −0.31886" was mislabeled: that value belongs to the class with ξ_∞ < 0 and ξ₂ = 1. The class of the rational number −1 has the coefficient of ξ = 1, because the κ ∈ 𝔛_S are trivial on 𝒪_S^×. Added: a^G(S,u_{ξε}) = a^G(S,u_ξ) for ε ∈ 𝒪_S^×, so the 16 classes carry four values (1.57726, 0.16864, −0.15668, −0.31886).
- *Lemma 7.3.* Δ_ψ has values in μ₄, not only μ₈ ((γ(D)/γ(1))² = (D,−1)_v). Changed in the lemma, the list of results and the Glossary.
- New citation [Th13] (T. Thomas, "Weil representation and transfer factor", Algebra Number Theory 7 (2013), 1535–1570; data checked online 2026-11-11, the paper read only through its introduction and statements): the action of the similitude group on the cover (§7.1) and the character of ρ₊ − ρ₋.

**Renumbering.** One new equation, (7.7); the old (7.7)–(7.14) are now (7.8)–(7.15). Lemma 7.8 has a new part (d). No statement number changed. The equation numbers in the Stage 6 notes are the old ones.

**The remaining stage-7 items of the Stage 6 notes.**
- *Acknowledgements.* Unchanged: ChatGPT refereed Sections 2–6, which is still accurate. Remark 2026.19 now says that Section 7 has not been refereed independently.
- *Titles.* The working subtitle "Sections 1–7, revised for the double cover (draft)" is replaced by the title "A hitch-hiker's guide to the metaplectic trace formula for SL(2): the double cover", dated "Draft of November 2026", with a line naming the 1995 notes ("… : basic theory") as the source. The title of Section 7, "The trace formula in stable(r) form", is kept; its first paragraph says what the word means and that nothing is transferred. Both are DJ's to change.
- *Remark 2026.9* (r(t) against the general definition in [A7]). Still not compared with [A7]. A sentence was added: the trace formula here does not depend on the comparison, because Proposition 7.10(c) derives the central terms of Theorem 4.11 from Proposition 4.8 with J_A(z,f) as defined in Lemma 4.10(b), when 𝒪_S is principal.
- *Remark 2026.13* (T ≥ 0 on the spectral side). Unchanged, and nothing depends on it: J_χ(f) is the value at T = 0 of a polynomial that is identified for large T.

**Still resting on citation and numerics only, after this stage.**
- Proposition 7.5: the regularity theorem at all places; at the archimedean places the trace-class property and the Schwartz kernel of ω(f).
- (N5) at the places where the normalizing factors are not explicit: a hypothesis. Everything under it: Proposition 7.9(a),(b), Lemma 7.11(c) for I_χ, Theorem 7.13.
- Lemma 7.1(c) through the cocycle (2.13) on GL(2) ([K2], numerics), with the direct check as a homomorphism for β.
- Proposition 7.12(a): convergence and square-integrability of theta functions.
- The statements about [Li11], [Li15], [Li21] and about Waldspurger's packets: comparisons, not used in proofs.

**Open, for DJ.**
- An independent referee report on Section 7 (by another model or a person). The places to look first: the new proof of Proposition 7.5; whether (N5) holds for Li's factors, or for factors defined through the local coefficients of Szpruch and Goldberg–Szpruch; the description of the packets after Proposition 7.12.
- Stage 0: done after this stage, see *Stage 0 notes*.
- The mathematical items listed under "Not done" in the Stage 6 notes are unchanged.

## Stage 0 notes (2026-11-11)

Stage 0 was planned as the first stage and done last. By then every section had been rewritten in `revised/`, so it has two parts.

**The 1995 notes, compiling: `clean-1995/`.** Copies of `cctrace_new.tex`, `cctrace2`–`7.tex`, `cctracer.tex` from `original-1995/` (which stays as received), with:
- `cctrac3b.tex` supplied as a copy of `book-1997/book7d.tex` (`\symbol{126}` → `\sim`);
- `\Bbb` → `\mathbb` (845), `\frak` → `\mathfrak` (108);
- equations numbered by section; as received they compile as (1)–(127);
- the duplicate bibliography entry [Sh] removed; the unused class option `amsfonts` removed.

It builds with `pdflatex` (81 pages, no errors, no warnings, no undefined citations). No mathematical change was made. There were no Scientific Word macros to remove in these files; only `cctrace1.tex`, the older master, needs `tcilatex`, and it is not copied.

**Not done, deliberately.** The 1995 text has no `\label`/`\ref`; its cross-references are typed by hand with the Scientific Word numbers, which do not all agree with the compiled ones (Section 7 compiles with equations (7.1)–(7.30)). Converting them, and correcting the 1995 bibliography entry by entry, would be work on a text that the revision replaces. The numbering maps in the stage notes above remain the bridge. With `cctrac3b.tex` present Section 4 gains statements 4.10–4.16 at its end; the numbers in Sections 5–7 do not change.

**The master of the revised paper.** `revised/preview.tex` is renamed `revised/sl2bar-trace-2026.tex` (PDF likewise) and is the master. Earlier notes in this log say `preview.tex`. Title page, at DJ's request: the sentence naming the 1995 notes is a `\thanks` footnote to the title, and the date line reads "Original draft: 1995, Corrected and expanded draft: 2026".

**Status.** All stages are closed. Open items are those listed at the end of the Stage 7 notes, first of all an independent referee report on Section 7.

## Referee report on Section 7, and response (2026-11-11)

ChatGPT refereed Section 7: `referee-2026-11/report-chatgpt-section7.md`. The answer, item by item, is `referee-2026-11/response-section7.md`. In short:

- **One error of statement:** Theorem 7.13(c) called sums of distributions with different characters eigendistributions. Reworded. (N5) is now assumed only in part (c).
- **Proposition 7.5:** the two-lattice argument is written out; new Lemma 7.5′ (vanishing of the integrals of ψ(aξ²) over distant shells, with the dyadic case); at the archimedean places a direct proof that the kernel is a Schwartz function replaces the citation; the comparison with [Th08] now says that it does not confirm the sign.
- **(N5):** still a hypothesis. Remark 2026.18 no longer cites [GS16] in support (that paper assumes the residue characteristic prime to n; checked), and formulates the needed statement as a problem. New reference [Sz16].
- **Packets after Proposition 7.12:** conventions stated; the general stable-sum statement is marked as expected, not proved; [GS12, §5] and [Ad, §15] cited on the referee's authority.
- **Exposition:** a paragraph separating equivariance, stability and transfer at the start of the section; the comparison with Li's Théorème 5.2.6 is now of coefficients only; Example 7.A(e) (the referee's); a table in Example 7.E; the PID hypothesis in the statement of Proposition 7.10; a dependency paragraph before Theorem 7.13.

No statement or equation number changed (the new lemma is numbered 7.5′). 105 pages. `sec7_n2_check.py`: 35 checks. Remark 2026.19 and the Acknowledgements now say that Section 7 was refereed.

**Still open:** existence of factors with (N1)–(N5) at the dyadic and ramified places; a reference or proof for the stable-sum statement for all cuspidal packets (not used in proofs); the unverified pinpoint citations listed at the end of the response.

## After the referee round: (N5), the citations, the stable-sum statement (2026-11-11)

The three items listed under "Still open" above. Branch `sl2bar-sec7-open-items`.

**1. (N5) is no longer a hypothesis.** New Proposition 7.8′ (after Lemma 7.8; numbered with a prime so that no number changes).
- *(a), (b): existence, proved in the paper.* Let ρ(π,λ) be the scalar M_v(π^w,−λ)M_v(π,λ) and ω(π) = π((w,1)²) ∈ μ₄. Then M_v(π,λ)* = ω(π)M_v(π^w,−λ) on iℝ, so ρ = ω̄·p with p ≥ 0; p is the same for π and πκ_a (Lemma 7.8(d)). Let h_π be the rational function of z = q^{−λ} with |h_π|² = p on |z| = 1, no zeros or poles in |z| < 1, h_π(0) > 0 (it exists and is unique). The factors r_v(π,λ) = c(ω(π))h_π(q^{−λ}), c(ζ)² = ζ̄, satisfy (N1)–(N5), and agree with the explicit factors at the unramified places. What is quoted: rationality of M_v on the K-types [Li II] and generic irreducibility. The obstruction noted in the Stage 7 notes (the constraint from (N2) when π^w = πκ_{a₀}) is met because h_{π^w}(z) is the conjugate of h_π(z̄).
- *(c): the explicit form, quoted from Szpruch.* p(π,λ) = C·L(2λ,χ²)L(−2λ,χ⁻²)/L(1+2λ,χ²)L(1−2λ,χ⁻²) with C > 0, at every finite place, dyadic included. So r_v = constant × L_v(2λ,χ²)/L_v(2λ+1,χ²) with **no exponential factor**, the global factor is m(μ,λ) = c·Λ(2λ,χ²)/Λ(2λ+1,χ²), and S_bad(μ) plays no role from Section 7.5 on. This answers the problem formulated in Remark 2026.18 of the previous draft.
- *What was read.* arXiv:1609.08122 (= [Sz16]): formula (5.8) gives the Plancherel measure for n = 2 with the constant q^{e(ψ₂)−e(χ²)}, with no restriction on the residue characteristic, derived from [Sz09]; the general Theorem 5.7 there (n ≢ 0 mod 4) is proved only for odd n, and is not used. [Sz09] was read as Chapter 8 of Szpruch's thesis, arXiv:1004.3516 (new reference [Sz10]): Theorem 8.1 gives the local coefficient as k_χ q^{d_χ s} × L-factors of χ and χ², 2-adic fields included, and the proof of Theorem 10.1 there uses the product formula in the form needed. Both were read through a text extraction of the arXiv PDFs, statement by statement, not line by line; the journal version of [Sz09] was not opened.
- *Independent check.* New in `sec7_n2_check.py`: the Tate-type integrals ∫γ_ψ(u)⁻¹χ(u)ψ(u)|u|^s d^×u (the inverse local coefficients, by Szpruch) are evaluated for ℚ₂ and all 16 characters of conductor dividing 32, and for ℚ₃, ℚ₅ and the tamely ramified characters; the product for (χ,s) and (χ⁻¹,−s) is constant × the L-quotient in χ² in every case, and the constant is a positive number times a fourth root of unity, as ρ = ω̄p requires. At the real place the script checks the adjoint relation and that the explicit factor √2 e^{iπm₀/2}L(2λ)/L(2λ+1) has the shape c(ω)h. Not rederived: Szpruch's identification of the integrals with the local coefficients.
- *Consequences in the text.* Remark 2026.18 rewritten. Proposition 7.9 and Theorem 7.13(c) keep (N5) in their statements, with the remark that the factors of Proposition 7.8′ have it. Section 6 is unchanged except for Remark 2026.15 and one sentence in §6.4, which now point to Proposition 7.8′; the abstract and Section 1 say that the explicit factors at the bad places are taken from Szpruch. **For DJ:** Section 6 could now be rewritten with the explicit m(μ,λ) and without S_bad(μ); this was not done, because it changes Theorem 6.11(e),(f) and the examples for k = ℚ and deserves its own pass.
- Not done: whether the factors of [Li II] have (N5) (no longer needed).

**2. The citations.** Opened in this session (arXiv or publisher PDFs, through text extraction; statements only):
- [GS12] Gan–Savin. §5 is "Interlude: results of Waldspurger"; Theorems 5.1–5.3 are the local statements; the example after Theorem 5.2 gives the packet of the Steinberg representation as {Θ_ψ(St_{V⁺}), Θ_ψ(1_{V⁻})} = {ω°_ψ, St_ψ}, with 0 → St_ψ → I(|·|^{1/2}) → ω^e_ψ → 0, and says that the two members of a packet have different central characters. **The referee's pointer and labeling are confirmed.** The global multiplicity formula is *not* in [GS12, §5]; the text now cites it as the case n = 1 of [GI, Theorem 1.4].
- [Th08] Thomas (arXiv:math/0610644v3). Theorem 1C is stated up to sign: confirmed. §12.2 is the proof of Theorem 2A and does contain the trace-class statement and the diagonal formula for the kernel (12.2.1, Lemma 12.2): the referee's pointer is confirmed, and the text mentions it. New information: Theorem 2A gives the character *without* sign ambiguity, on a Maslov-index model of Mp(V); we have not carried our section over to that model, and the text says so. Normalization: Thomas's γ(a) is the Weil index of x ↦ ψ(½ax²), so his formulas are ours for his character ψ(2x); stated in the text. Thomas asserts local integrability as known without a reference; the text now cites [Mak], [Li II, §4] and Harish-Chandra for it.
- [Sch] Schultz's thesis, [Luo], [GI]: see item 3.
- **Not opened:** [Wa80], [Wa91] (not available online to this session); [Ad] (only its review and the account in [Sch], which confirm that the last section treats (SO(3), SL̃(2,ℝ)) and that the lifting takes stable discrete series to stable genuine discrete series; the pinpoint "§15, (15.7)–(15.8)" is removed from the text); the journal version of [Sz09]; [Th13] beyond what the Stage 7 notes record. A session with these PDFs attached is still the way to close them.

**3. The stable-sum statement for cuspidal packets.** A reference was found, and with it a three-line derivation in the sense of this section. The character identity (new equation (7.16)) Θ_{π⁺} + Θ_{π⁻} = (Θ⁺_ψ − Θ⁻_ψ)·Θ_σ∘t is Adams's lifting for ℝ, Schultz's Theorem 5.35 for p-adic fields (p = 2 not excluded), and the case s = 1 of Luo's endoscopic character identities for tempered parameters of Mp(2n) (J. Reine Angew. Math. 768 (2020)), where the packets are those of Gan–Savin. Given it, the sum is ⋆-invariant: the first factor by Proposition 7.5, the second because it depends only on the eigenvalues. The text states this, marks (7.16) as quoted, and says what was not matched (normalizations of the transfer factor and of the correspondence t; in [Sch] the identification of the packets with Waldspurger's is stated without proof). The case s = −1 of [Luo] gives the difference as the transfer for the other endoscopic datum. Still not used in any proof.

**Renumbering.** One new equation, (7.16), in §7.7; no earlier number changes, and no statement number changes (the new proposition is 7.8′). New references [Luo], [Sz10]. 108 pages. `sec7_n2_check.py`: 38 checks (35 before). All ten scripts pass; the paper builds with no warning.

**Still open.**
- The sources not opened (item 2).
- Rewriting Section 6 with the explicit global factor (item 1).
- Matching the normalizations of [Li11], [Luo], [Sch] with ours, i.e. identifying Δ_ψ with Li's transfer factor on the nose; and the mathematical items under "Not done" in the Stage 6 notes.

## Stage 8: style-guide pass (2026-11-12)

The paper was brought into line with `../joyner-math-paper-style-guide.md` (Draft 2, November 11, 2026), following the audit of November 11 and DJ's instructions of November 12. No statement, proof, hypothesis or status label was changed. Draft number 1.

**Compiling.** Before the pass: 108 pages, no errors, no LaTeX warnings, no undefined references, 3 overfull boxes and 16 underfull boxes. After it: 110 pages, no errors, warnings or undefined references, **no overfull boxes**, and 43 underfull boxes (badness only, most of them in the narrow columns of the glossary tables; the guide does not ask for these to be removed). All 11 scripts of `run_checks.py` pass, including the new `examples_n2_check.py` (13 checks).

### Decisions (DJ, 2026-11-12) and defaults used

- Title: the original title, *A hitch-hiker's guide to the metaplectic trace formula for SL(2): basic theory*, is restored (rule 6.2). The restriction to the double cover is stated in the `\thanks` note and in the abstract.
- The literature review is an unnumbered section after Section 1, so that no theorem or equation number changes.
- Appendix A moved into this log (below). Its `\label{sec:appendix-1995}` is the one label that could not be kept. The four references to it now point to the revision log or were removed with the sentences they ended.
- Rule 3.4: five new examples, for the most complex definitions without one, not an example for every definition.
- Rule 3.2 applied to subsubsections as well.
- Notation near the beginning: the Notation subsection at the start of Section 2. The glossary keeps its notation table.
- American spelling is not applied to published titles: [Ar88a] keeps "behaviour".
- [DECIDE] defaults: document class `article` (kept). Fonts: newtx preferred, but newtx is not installed in the build environment and could not be downloaded, so the fallback `mathptmx` is used. The newtx line is in the preamble as a comment. Glossary placement: at the end, before the Acknowledgments. Author line: the prompt said nothing, so "D. Joyner and Claude" is kept. A version for arXiv or a journal would need Claude moved to the acknowledgments.

### Changes, by step

1. **Preamble.** `12pt,letterpaper`, `fontenc` T1, `mathptmx`, `geometry` with one-inch margins (was 11pt, 1.1in, Computer Modern). New operators `\Ad`, `\vol`, `\sgn`, `\Ind`, `\Resid` (`\DeclareMathOperator`), replacing about 130 occurrences of `\mathrm{Ad}`, `\mathrm{vol}`, `\mathrm{sgn}`, `\mathrm{Ind}`, `\mathrm{Res}` (rule 1.8). `\Resid` is the residue, because `\Res` is restriction of scalars.
2. **Title page, abstract, acknowledgments.** Title as above, subtitle "Draft 1. Corrected and expanded version", date line "Original draft: 1995. Corrected and expanded draft: 2026" (rules 6.2, 6.3). The `\thanks` note names the 1995 notes (January 1995, slightly revised June 2002), the date of the revision (November 2026) and the restriction to n = 2. Author line with `wdjoyner@gmail.com` (rule 5.1). New first sentences of the abstract: the AI disclosure, with a pointer to the Acknowledgments (rule 5.2). The Acknowledgments were rewritten (rules 5.3–5.5): they name Claude (referee of the 1995 notes, co-author and reviser, author of the scripts) and ChatGPT (independent referee of Sections 2–6 and of Section 7), state that AI review is not an independent certification, and point to this log. "Acknowledgements" is now "Acknowledgments" everywhere (rule 1.4). The item-by-item account of the ChatGPT reports that stood in the Acknowledgments moved here (*Moved from the Acknowledgments* below).
3. **Citation keys** (rule 1.7). 61 of the 83 keys changed, to author initials plus two-digit year. Where two works by the same authors share a year, both get a letter, in the order of the old bibliography: Ar88a = [A7], Ar88b = [A9], Ar88c = [A10]; Li12a = [Li II], Li12b = [Li12]; Li14a = [Li I], Li14b = [Li IV]. The key Li12 (the fundamental lemma) changed for that reason. Every `\cite` was updated (one split across two lines, in the former Appendix A, was found by hand), and the bibliography is now sorted by key, chronologically within an author. Keys in the earlier sections of this log, in `../referee-2026-11/` and in the READMEs are records and were left unchanged; the table below translates.
4. **Structure and revision history** (Section 2 of the guide, rule 6.4).
   - The former §1.2 *Literature* is now the unnumbered *Literature review*, after Section 1, in two parts: *Work up to 1995* and *Work since 1995*, then *The place of this paper*. The sentences are those of §1.2, sorted by date. Sentences that mixed the two periods were split ([KP84]/[BD01]; [GS12], [GI18]; [Ar05]; [Me01, Me02]; [KP84]/[Mc12], [Ga14]), with minimal connecting words. Work of 1995 ([MW95]) is counted as "up to 1995". New: a two-sentence opening paragraph.
   - New Section 8, *Summary of results and open questions* (`sec8-summary.tex`).
   - Order at the end: Section 8, Glossary, Acknowledgments, References.
   - Appendix A removed from the paper (the file `appA-comparison.tex` is deleted; it is in git history), and reproduced below.
   - Comparisons with the 1995 notes and attributions to the referee removed from the body. They are recorded under *Removed from the body* below.
   - Hand-typed section numbers replaced by `\ref` (rule 1.5): §2.2 ("Section 3"), §2.2 ("Sections 4 and 5"), §4 opening ("Sections 5–7"), §3 opening ("Section 6"), §5.2 ("Section 6"), and the title of §3.3, "Distributions for Section 6", now "Distributions for the invariant form".
   - §1.4 *Conventions*: the sentence pointing to Appendix A now points to the revision log, and two sentences point to the literature review, Section 8 and the Glossary.
5. **Orienting paragraphs** (rule 3.2), one or two sentences each, at the start of: Section 2's Notation subsection; §§2.1.1–2.1.5 and 2.2.1–2.2.4; §§3.1, 3.2, 3.3; §§4.1–4.5; §§5.1–5.4; §6.4; §7.4; §1.4; and the six "Status of the results" subsections. Also one sentence added to the first paragraph of §1.1. These describe content only.
6. **Script references.** Remarks 2026.11 (verification for Section 4) and 2026.20 (verification for Section 7) now name `checks/examples_n2_check.py` and say that Example 7.D has no numerical check.

### New mathematical text, for refereeing (ground rule 2)

These are the only additions with mathematical content. Each needs an independent check.

1. **Example 4.A** (`ex:trunc-Q`, §4.2). k = ℚ, the upper half plane: H(x) = ½ log Im z, H(γx) = ½ log Im γz for γ ∈ SL(2,ℤ), the height inequality as Im z · Im γz ≤ 1, disjoint horoballs for T ≥ 0, and F^G(·,T) as the cutoff of the fundamental domain at height e^{2T}. *Checked numerically* (random points, cosets up to |c|,|d| ≤ 40).
2. **Example 4.C** (`ex:JA-hyp-p`, §4.4). p odd, f_p = e_p, γ = (a(t),1) with t a unit: J_G(γ,e_p) = 1 and J_A(γ,e_p) = (m − (1−p^{−m})/(p−1)) log p, with p^{−m} = |1−t^{−2}|_p. Includes the conjugation (n(y),1)⁻¹(a(t),1)(n(y),1) = (a(t)n((1−t^{−2})y),1) in the cover. *Checked* (the conjugation exactly in the cover at p = 3, 5, 7; the integral by a sum over cosets of ℤ_p).
3. **Example 4.D** (`ex:JA-central-p`, §4.4). p odd, f_p = e_p: Φ_p = 1_{ℤ_p}, and the p-term of J_A(z,f_S) in Lemma 4.10(b) is −(log p)/(p−1) times ∏_{w≠p} Φ̂_w(0). *Checked* (the membership in K* exactly, the series numerically).
4. **Example 7.D** (`ex:kappa-unram`, §7.3). Unramified elliptic γ at a non-dyadic place: the two terms of J^st and J^κ for e_v, the vanishing of the second, and an illustration of Lemma 7.6(c) with z̃ = (−1,1). Derived from Lemma 7.6(d) and its proof. *Not checked numerically.*
5. **Example 7.F** (`ex:uprime-gl2`, §7.5). δ = diag(p,1) at an odd p: u′_B(k̃,δ) = −H_1(kδ) = ±½ log p according as d is a unit or not, the measure 1/(p+1) of the second set, and a consistency check of Lemma 7.8(a) at x = 1. *Checked* (exactly, at p = 3, 5, 7).
6. **Section 8** (`sec8-summary.tex`). A restatement of the main results with the status the text gives them (taken from the "Status of the results" remarks), and seven open questions, each already named in Section 1, Section 7 or a status remark. The referee should check that no status is stated more strongly than in the body.
7. **Literature review, opening paragraph**, and the sentence that work of 1995 counts as "up to 1995". Not mathematical, but new.
8. **Orienting paragraphs** (step 5 above): new prose. Two claim a fact: §5.2 ("identifies the residual spectrum") and §4.3 ("Each class contributes a polynomial in T of degree at most one"). Both repeat statements of the section.

### Semicolons

Rule 3.8 was applied to new text only. Three existing sentences lost a semicolon because the clause after it was revision history and was removed: Remark 2026.6 (§3.3, "These are referee items II.1–II.4; none of them arises…"), the first paragraph of §7.5, and the paragraph after the proof of Proposition 7.10.

### Removed from the body (rule 6.4)

The mathematics in each of these places is unchanged. Only the comparison or attribution was removed.

- §1.2 (formerly §1.3), paragraph on the stable form: "The 1995 notes defined stable conjugacy on the cover as conjugation by GL(2), following [LL79]; Section 7 shows that this has to be twisted, …". It now says "Section 7 shows that stable conjugacy on the cover is conjugation by GL(2) twisted by a sign, …".
- §5 opening: "Three things are new compared with the 1995 notes" became "Three features of the double cover stand out", and "…with μ^w = μ, which the 1995 notes omit" lost the relative clause.
- Remark 2026.6 (§3.3): "These are referee items II.1–II.4; none of them arises for n = 2" became "These questions do not arise for n = 2".
- Example 7.A(e): "(This example is due to the referee.)" removed. The example was supplied by ChatGPT in its report on Section 7.
- After Lemma 7.6: "Part (b) explains a statement of the 1995 notes: … (Appendix A)" became "By part (b), …".
- §7.5, first paragraph: "; this is the correct form of the variance formulas that the 1995 notes state for conjugation by GL(2)" removed.
- After Proposition 7.10: "; in the 1995 notes they were written as a sum over the rational unipotent classes, which diverges (Appendix A)" removed. The divergence is stated at the start of §7.6.
- After Theorem 7.13: "is the property that the 1995 notes called 'κ-stable'" and "which the 1995 notes took as the stable part" removed.

**Left in place on purpose:** statements of scope that name the 1995 notes (Section 2 opening and Notation, Remark 2026.3, §1.4, the literature review); Remark 2026.9, which says a comparison was checked only against `book7d.tex` (a verification status); Remark 2026.8, which lists that a script checks the 1995 cocycle on A; and the `% [Claude]` comments in the source.

### Numbering concordance (ground rule 5)

No theorem, lemma, proposition, corollary, remark or equation number changed. Every `\label` except `sec:appendix-1995` is kept. Changes:

| Object | Old | New |
|---|---|---|
| §1.2 Literature | 1.2 | unnumbered *Literature review*, after Section 1 |
| What is proved here and what is cited | 1.3 | 1.2 |
| A running example | 1.4 | 1.3 |
| Conventions | 1.5 | 1.4 |
| Example (`ex:unip-Q`), unipotent constant term | 4.A | 4.B |
| Example (`ex:order4-stable`), elements of order 4 | 7.D | 7.E |
| Example (`ex:unip-coeff`), the 16 coefficients | 7.E | 7.G |
| Appendix A | A | removed (below) |
| Summary of results and open questions | — | 8 |
| New examples | — | 4.A, 4.C, 4.D, 7.D, 7.F |

### Citation keys (old → new)

| Old key | New key | Old key | New key | Old key | New key |
|---|---|---|---|---|---|
| Ad | Ad98 | How | Ho10 | Mo2 | Mo88 |
| Ar05 | Ar05 | JL | JL70 | MW2 | MW95 |
| A2 | Ar78 | J88 | Jo88 | Ni | Ni75 |
| A3 | Ar80 | Kn | Kn02 | PR | PR94 |
| A6 | Ar81 | KP | KP84 | Re | Re99 |
| A14 | Ar82 | KP2 | KP86 | Ro | Ro83 |
| A12 | Ar86 | K1 | Ku67 | R | Ro90 |
| A7 | Ar88a | K2 | Ku69 | Sa | Sa67 |
| A9 | Ar88b | L2 | La76 | Sav | Sa88 |
| A10 | Ar88c | Li11 | Li11 | Sch | Sc98 |
| A11 | Ar89 | LiII | Li12a | Sel | Se56 |
| BD | BD01 | Li12 | Li12b | Se | Se73 |
| CF | CF67 | LiIII | Li13 | Sh | Sh73 |
| FK | FK86 | LiI | Li14a | Shi | Sh75 |
| F | Fl79 | LiIV | Li14b | Sz09 | Sz09 |
| Fl | Fl80 | Li15 | Li15 | Sz10 | Sz10 |
| Gao | Ga14 | Li19 | Li19 | Sz16 | Sz16 |
| Ge2 | Ge76 | Li21 | Li21 | Ta | Ta67 |
| GGW | GGW18 | Li24 | Li24 | Th08 | Th08 |
| GI | GI18 | LL | LL79 | Th13 | Th13 |
| GJ | GJ79 | Luo | Lu20 | Wa80 | Wa80 |
| Go | Go62 | Ma57 | Ma57 | Wa81 | Wa81 |
| GPS80 | GPS80 | Mat | Ma69 | Wa91 | Wa91 |
| GPS83 | GPS83 | Mak | Ma99 | We18 | We18 |
| GS12 | GS12 | McN | Mc12 | We64 | We64 |
| GS16 | GS16 | Me2 | Me01 | W1 | We74 |
| He | He83 | Me1 | Me02 | W2 | We82 |
| HI13 | HI13 | M | Mo68 |  |  |

### Moved from the Acknowledgments

The Acknowledgments of the previous draft described the ChatGPT reports item by item. That text follows, with the numbers of this draft written out.

We thank ChatGPT (OpenAI) for refereeing the November 2026 draft of
Sections 2–6. Its report showed that the earlier draft treated Kubota's
cocycle as continuous and defined test functions through the section
$g\mapsto(g,1)$, which is not continuous; Lemma 2.1,
Example 2.A, Lemma 2.2(i) and the
definitions in Sections 2.1.4, 2.2
and 3.1 are the result. It also found the gap in the
proof of Lemma 3.1(c), asked for the matching of
parameters now proved in Lemma 5.7 and
Theorem 5.8(c), and for the treatment of general unitary
characters in Lemma 6.6(c). The introduction, the
roadmaps, the glossary and Appendix A (now *Comparison with the 1995 notes* below) follow its
suggestions. The errors that remain are the authors'.

ChatGPT also refereed Section 7 in a second report. It
found that Theorem 7.13(c) called sums of distributions with
different characters eigendistributions; asked for
Lemma 7.5′ and for the two-lattice and kernel arguments in the
proof of Proposition 7.5; pointed out that [GS16]
does not cover the dyadic places, so that it cannot support the
condition (N5) there; and supplied Example 7.A(e) and the
references for the packets after Proposition 7.12.

### Comparison with the 1995 notes (former Appendix A)

Sections 2–7 revise Sections 2–7
of the 1995 notes *A hitch-hiker's guide to the metaplectic trace
formula for $SL(2)$: basic theory* (D. Joyner, January 1995, revised June
2002), and the parts of Chapter 9 of the 1997 book manuscript *An
application of Arthur's invariant trace formula for $SL(2)$* from which
they came. This section, formerly Appendix A of the paper, records, statement by statement, what the
revision replaces and what it corrects. File names such as
`book7d.tex` refer to that manuscript. Item numbers such as
“II.5” or “A.2” refer to the first referee report on the 1995 notes
(Claude, November 2026); the list of items, and the tables matching the
1995 numbers with the present ones, are in the file
`revision_log.md` that accompanies the source. Nothing in it is used in the body of the paper.

##### Section 2: the cover

- **Section 2.1, the cover of $G(\mathbb{Q}_p)$.** The 1995 notes call $\overline{G(\mathbb{Q}_p)}$ a subgroup of $\prod_{v\mid p}\overline{SL(2,k_v)}$; it is a quotient.

- **The height $H$, (2.5).** The 1995 notes define $H$ with the maximum of the $|t_v|_v$, $v\mid p$, in place of their product. The product is forced by $\langle H(x),\chi_1\rangle=\log|\chi_1(\tilde a)|$ (Section 2.1.3).

- **Section 2.1.3.** The 1995 notes call the fundamental coweight $\varpi$ the dual root. An earlier draft of this revision had $\alpha=2\chi_1$ and $X_\alpha=1$, which is correct only for $k=\mathbb{Q}$ (Remark 2026.9).

- **Section 2.1.4, genuine and anti-genuine.** The 1995 notes use genuine functions in §2.1.4 and $\pi(g,\zeta)=\zeta^{-1}\pi(g,1)$ in §3.1. For $n=2$ both conventions agree with Li's; for general $n$ they do not (Remark 2026.3).

- **Section 2.1.4, the unit element.** The 1995 notes identify $K_p$ with $\{(k,1)\}$, which suggests the function $(k,\zeta)\mapsto\zeta^{-1}$ as the unit of the Hecke algebra; the unit is $e_p$ of (2.8). An earlier draft of this revision defined $C_c^\infty(\overline{G(\mathbb{Q}_p)})_-$ by requiring $g\mapsto f(g,1)$ to be smooth; that definition excludes $e_p$ and was replaced after the 2026 referee report by ChatGPT.

- **The integration formula (2.9).** The 1995 notes have $\delta_B(a)^{1/2}$ for $g=kan$; the exponent must be $1$ for $g=kan$ and $-1$ for $g=nak$. In Section 4 they have $\delta(a)$ for $x=nak$.

- **Lemma 2.6(a), the splitting over $G(\mathbb{Q})$.** The 1995 notes define the splitting as $\gamma\mapsto(\gamma,
s_\mathbb{A}(\gamma)^{-1})$, with $s_v(\gamma)^{-1}=(c,d)_v$ when $v$ is finite,
$cd\ne0$ and $n\nmid\operatorname{ord}_v(c)$, and with the cocycle $\prod_v\beta_v$.
That product does not converge, and the formula belongs to a different
normalization. In the normalization (2.11),
$\kappa_\mathbb{A}$ of (2.12) replaces $s_\mathbb{A}^{-1}$. For $n=2$ the two
agree at every non-dyadic $v$ with $\gamma\in K_v$: if $\operatorname{ord}_v(c)>0$ is
even, or if $\operatorname{ord}_v(c)=0$, both $(c,d)_v$ and $\kappa_v(\gamma)$ are $1$.
They differ only at the finitely many places where $\gamma\notin K_v$,
and at dyadic places.

##### Section 3: rank 0

- **The cocycle on $A$, (3.1).** The 1995 formula $\beta(g_1,g_2)=(g_1^{-1},g_2^{-1})(-g_1g_2^{-1},g_1^{-1}g_2^{-1})$ on $A$ reduces to (3.1) for $n=2$.

- **Lemma 3.1.** This replaces Lemma 3.1 of the 1995 notes, which cited [Ge76] for factorizability of genuine representations of the restricted product. For $n=2$ the statement concerns the quotient and needs no citation.

- **Theorem 3.2.** This is the $n=2$ form of Theorem 3.2 of the 1995 notes, restated as a correspondence of automorphic spectra. The 1995 statement matches genuine representations with characters $\chi^N$, $N=n/\gcd(n,2)$; for $n=2$, $N=1$, and the matching requires the choice of $\bar\chi_0$, which the 1995 text did not make.

- **Theorem 3.4.** This replaces Theorems 3.8 and 3.9 of the 1995 notes, whose orbital integrals reduce to the values $f(\delta)$ for $n=2$.

- **Lemma 3.5.** This replaces Lemmas 3.11 and 3.12 and the argument through Claims 1 and 2 of the 1995 notes. The local maps $\bar f_v\mapsto f_v$ involve no sum over $T(\mathbb{Q}_p)_\delta\backslash T(\mathbb{Q}_p)$ and no factor $s_\mathbb{A}(\delta)$, because there is no conjugation.

##### Section 4: the geometric side

- **Lemma 4.1.** The 1995 text lists the centralizer $G$ for $\gamma=\pm1$ among the centralizers of semisimple classes that are “anisotropic modulo the center” and calls all such classes unramified. Neither holds for $\pm1$: $G$ is isotropic, and $\mathcal O_{\pm1}$ contains $\pm$(unipotent) elements. The vanishing of genuine orbital integrals for general $n$ is `book3b.tex`, Lemma 5.2.

- **Lemma 4.2.** This is Lemma 4.1 of the 1995 notes with $K_P=\sum_{\mathcal O}
K_{P,\mathcal O}$ (not $\sum K_{\mathcal O}$) and with one kernel
convention, $f(x^{-1}\gamma y)$, throughout; no passage to the
archimedean place is needed for the convergence.

- **Lemma 4.3.** Part (b) replaces Lemma 4.2 of the 1995 notes, which has an unused $N$ and only the bound $\le1$, cited from [Ar78]. The constants $u\ge1/2$ and $T_0>\sqrt3/2$ of the 1995 text are the classical ones for $SL(2,\mathbb{Z})$ over $\mathbb{Q}$ and are not used.

- **Lemma 4.4.** This is Lemma 4.3 and (4.2) of the 1995 notes, there with two parameters $T_0>T_1$ in reversed roles and with a function $F^B$ that is identically $1$ for $SL(2)$.

- **Theorem 4.5.** The theorem replaces Lemma 4.4, Corollaries 4.5–4.7, Proposition 4.8 and Corollary 4.9 of the 1995 notes. Their proof of Lemma 4.4 omits the terms $\gamma\notin B(\mathbb{Q})$ and the sum over $\mu\in A(\mathbb{Q})$, and the per-class bounds in Corollaries 4.5–4.7 are not established there. Proposition 4.8 claims polynomiality for $K^T_{\mathcal O}$ and $J^T_{\mathcal O}$ separately, without a proof. Part (b) of the theorem shows that for this group both integrals exist and coincide, and part (d) gives the polynomials.

- **Proposition 4.6.** The 1995 weight $v_{\mathcal O}(x,T)=2(T-H(x))$ (item II.5 of the first referee report) is not left $A(\mathbb{A})$-invariant; the $w$-term was lost in passing from the sum over $\delta$ in (4.3) to $\hat\tau_B(H(\eta x)-T)$ in (4.4). The weight $2T-\log\delta(x)-\log\delta(wx)$ of `book7d.tex` has the right shape but the wrong normalization, since $\log\delta_B=2H$ (item A.4).

- **Proposition 4.8.** The 1995 formula (4.5) keeps only the $f(\mu)$-term of a central class (item II.6). In `book7d.tex`, $J_{\mathrm{unip}}$ is defined by truncating at $T_0=0$, which is correct here only because the integral converges at $T=0$; in general it must be the polynomial evaluated at $0$ (item A.5).

- **Section 4.4, test functions.** `book7d.tex` takes $f_\infty$ in $C^\infty$ rather than $C_c^\infty$, and asserts that Arthur's spaces of almost compactly supported and moderate functions coincide with $\mathcal H$ for both $G$ and $A$; for $A$ this fails.

- **Lemma 4.9.** At a $p$-adic place the weight is $\log\max(1,|y|_p)$, not
$\log\sqrt{|1+y^2|_p}$ as in `book7d.tex` and (7.13) of the 1995
notes (items II.22, A.6); the latter is the real formula.

- **Lemma 4.10.** The Example in `book7d.tex` sets $r_A=1$ and takes the plain limit of $J_A(az,f)$, which diverges (item A.2).

- **Theorem 4.11.** This is the corrected form of the Proposition of `book7d.tex` (cited in the 1995 Section 6 as “Proposition 4.18”), which credits the result for covers to [Ar86, Thm. 8.1]; Arthur proves it for connected reductive groups, and for covers it is Li's theorem [Li14a] (item A.1). The sums there run over the rational class $\mathcal O$ instead of the $(G,S)$-classes (item A.7). In the 1995 text, 5.4(a) has only $a^G(S,z)f(z)+\tfrac12a^A(S,z)J_A(z,f)$; Theorems 5.16(a) and 6.11(a) use Theorem 4.11(a) in full.

##### Section 5: the spectral side

- **Lemma 5.1.** Lemma 5.1 of the 1995 notes asserts that the right regular representation
on $L^2(\Gamma\backslash G)$ decomposes into irreducibles “each occurring
with finite multiplicity” for every discrete $\Gamma$ in a unimodular
$G$. That is false in general (take $\Gamma=1$); what holds is a direct
integral decomposition for $G$ of type I, and finite multiplicities in
the discrete part for lattices in reductive groups, as above.

- **Lemma 5.2.** This corrects Example 5.2 of the 1995 notes, which says that all genuine
unitary representations are factorizable (it should say irreducible),
that $\pi_v$ is unramified when it has a $\overline{K_v}$-fixed vector
(genuine representations have none; the condition is a $K_v^*$-fixed
vector), and which treats $\overline{G(\mathbb{A})}$ as a restricted product rather than a
quotient of one (item I.4).

- **Cuspidal data.** This replaces Example 5.4 of the 1995 notes, which says that two
parabolics with Levi $A$ are associate only if they are opposite (but $B$
is associate to itself), and that $(A,\rho)\sim(A,\rho')$ only if
$\rho=\rho'^w$; the correct condition is $\rho=\rho'$ or $\rho=\rho'^w$
(item II.13).

- **Proposition 5.4.** The proposition replaces (5.2)–(5.4), Corollary 5.5 and Proposition 5.6 of the 1995 notes. The 1995 description of $L^2(M(\mathbb{Q})\backslash\overline{M(\mathbb{A})^1})_\chi$ through the spaces $\Psi(P_1,P,\chi)$ is Langlands' original one; for $SL(2)$ the description in Proposition 5.4 is all that is used.

- **The space $\mathcal H_B(\mu)$, (5.1).** In Example 5.18 of the 1995 notes the condition $\varphi(ag)=\pi(a)\varphi(g)$ is imposed for all $a\in\overline{A(\mathbb{A})}$, so that the parameter $\lambda$ is part of $\pi$ and the factor $\delta_B^{1/2}$ is missing.

- **Theorem 5.5.** This is Theorem 5.8 of the 1995 notes, specialized to $P=B$, with three corrections. The measure on $i\mathfrak a^*$ is $dt/2\pi$ (the 1995 text has $(1/2\pi i)^{\dim A}$ in (b) and $(1/2\pi)^{\dim A}$ in the norm of $L^\wedge_{\mathcal P}$). The number $n(A_B)$ of chambers in $\mathfrak a$ is $2$, not $1$. And the theorem is stated for one $\mu$, the spectral decomposition being Proposition 5.4.

- **Lemma 5.6.** The 1995 notes leave $M(s,\pi)$ unnormalized (item II.16).

- **Theorem 5.8.** The theorem corrects the Introduction of the 1995 notes, which says that the formula has no term corresponding to the residual term [LL79, (5.5)] (item II.9).

- **Proposition 5.9.** This replaces Lemma 5.9, Theorem 5.11 and Examples 5.17–5.22 of the 1995
notes. Examples 5.21–5.22 there put the term
$I_B(\pi,f)\phi(x)\delta_B(x)\overline{\phi(y)}$ into $K_{G,\chi}$; it
belongs to $K_{B,\chi}$, and for $\chi$ cuspidal there is no Eisenstein
series in $K_{G,\chi}$ (item II.13). Example 5.20 omits $\lambda$ and the
measure. The 1995 definition of $k^T_\chi$ has $K_{P,\chi}(x,x)$ where
$K_{P,\chi}(\delta x,\delta x)$ is meant (as in `book7f.tex`).

- **Lemma 5.10.** This replaces Lemma 5.13 of the 1995 notes (proved there by reference to
the non-metaplectic case) and makes the range of $T$ explicit.
Lemma 5.14 and Example 5.12 there are the case $P=G$ of \cite[Lemma 1.5]
{Ar80}; for $SL(2)$ that identity is (5.9) itself, since
$\hat\tau_B=\tau_B$, and we do not repeat it.

- **Lemma 5.11.** This is Lemma 5.15 and Example 5.16 of the 1995 notes; their reference
“lemma 4.7” for the partition is Lemma 4.4.

- **Theorem 5.12.** The theorem replaces Lemmas 5.23, 5.25 and 5.26 of the 1995 notes, whose proofs are incomplete (item II.12). The proof of Lemma 5.23 asserts that $\Lambda^T_2K_\chi(x,x)$ is compactly supported; it is only rapidly decreasing (Lemma 5.10(c)). The proof of Lemma 5.25 (“$K_P$ is continuous, hence integrable”) does not give integrability. And the equality $K^T_\chi=J^T_\chi$ claimed there, of $\int\Lambda^T_2K_\chi$ and $\int\sum E\,\overline{\Lambda^TE}$, is a consequence of Lemma 5.10(b), not the content of Arthur's [Ar80, Lemma 2.4]; what is needed is (c), which compares them with $\int k^T_\chi$.

- **Theorem 5.14.** Theorem 5.14 replaces Theorem 5.27 and Example 5.28 of the
1995 notes. Three things change.

- *The factor of $T$* (item II.11). Arthur's formula
  \[
  M_B^T=\operatorname{vol}(\mathfrak a/\mathbb{Z}\alpha^\vee)\lim_{\zeta\to0}
  \sum_{s\in\{1,w\}}\frac{e^{(s\zeta)(T)}M(s,\lambda)^{-1}
  M(s,\lambda+\zeta)}{\theta(s\zeta)},
  \]
  with $\theta(\zeta)=\zeta(\alpha^\vee)=d\zeta$
  and $\operatorname{vol}(\mathfrak a/\mathbb{Z}\alpha^\vee)=d$ for our $dX$
  (Remark 2026.9), gives (5.12) for every $k$; the factor
  $d$ cancels, so the correction $\alpha^\vee=d$ (Remark 2026.9) does not change
  $M_B^T$ once the volume is taken with the same measure. The 1995
  computation identifies $\varsigma(T)=2\varsigma T$ and
  $\varsigma(\alpha^\vee)=2\varsigma$ (correct for $k=\mathbb{Q}$, where
  $\lambda=2\varsigma$), takes the volume to be $1$, and then omits the
  division by $\varsigma(\alpha^\vee)$; the limit is
  $2T-\frac12M^{-1}\frac{dM}{d\varsigma}$, which is (5.12), not
  $4T-M^{-1}M'$. The sign is right, as the 1995 text suspected and as
  in [LL79]; Proposition 5.17 confirms the factor.
- *Ramified classes* (item II.10). The 1995 Theorem 5.27 assumes
  $\chi$ unramified, and its Example 5.28 says correctly that $(A,\mu)$
  is unramified if and only if $\mu^w\ne\mu$, but the classes with
  $\mu^w=\mu$ never appear. By Lemma 5.3(d) they are the
  $\chi_b$, and they carry the residual spectrum and the term
  $\frac14\operatorname{tr}(M(w,0)I(\mu_0,f))$. In Arthur's fine
  expansion [Ar82, Thm. 8.2], [Li13] this is the term
  $|W^A_0||W^G_0|^{-1}|\det(w-1)_{\mathfrak a}|^{-1}
  \operatorname{tr}(M(w,0)I(\mu_0,f))$, with $|W^A_0||W^G_0|^{-1}=\frac12$
  and $|\det(w-1)_{\mathfrak a}|=2$. In the trace formula for $GL(2)$
  of [GJ79, §6] the same term is written $-\frac14\operatorname{tr}
  (M(0)\pi_0(f))$, next to $+\frac1{4\pi}\int\operatorname{tr}(M(-iy)M'(iy)
  \pi_{iy}(f))\,dy$: that formula has the trace of $R(f)$ on the discrete
  spectrum alone on one side, and moving both terms to the spectral side
  gives the signs of Theorem 5.16(e). The sign of the cross terms
  in (5.11), from which it comes, is also checked numerically on
  the Eisenstein series of $SL(2,\mathbb{Z})$ (Remark 2026.17),
  and $M(w,0)$ is computed in Proposition 6.13.
- The lines “$M_G^T(\pi)_\chi=1$” and “($P=B$, $\chi=(G,\rho)$)
  $M_B^T(\pi)_\chi=1$” of Example 5.28 are dropped: for cuspidal $\chi$
  there is no $B$-term.

- **Theorem 5.16.** In the 1995 notes, Section 5.4 lists (a) as
$a^G(S,z)f(z)+\frac12a^A(S,z)J_A(z,f)$, without the unipotent terms
$a^G(S,u_\xi)J_G(zu_\xi,f_S)$; `book7f.tex` has them in the form
$\sum_{\gamma\in\mathcal O}a^G(S,\gamma)J_G(\gamma,f)$, a sum over the
rational class instead of the $(G,S)$-classes (items II.6, A.7).
Item (e) there is $\frac12\int\operatorname{tr}(M_A(\pi)_\chi I_B(\pi,f)_
\chi)\,d\pi$ over $\chi\in\mathcal X\smallsetminus\mathcal X_G$ with
$M_A=M_A^T|_{T=0}$, without the residual and ramified terms. Section 5.4
also uses $S$ and $\mathbb{A}_S$ before Section 6 defines them; they are now
defined in Section 4.4, and “given in section 5”
refers to Section 4.

##### Section 6: the invariant form

- **The introduction of Section 6.** Compared with Section 6 of the 1995 notes:

- Conjectures 6.3, 6.4, 6.7, 6.8 and 6.10 there (the trace
  Paley–Wiener theorems and the normalization of intertwining
  operators) are no longer hypotheses: 6.10 is a theorem of
  Li [Li12a], and the others are not needed for this group
  (item II.14).
- The weight $u'_B(k,y)$ is $-H(ky)$, not $|H(ky)|$ (item II.15,
  Lemma 6.1).
- The invariant spectral terms attached to $\chi\in\mathcal X_A$ do
  not vanish. The logarithmic derivative $m'/m$ of the global normalizing
  factor survives (item II.16), and $m$ is identified:
  $m'/m=2\frac{L'}{L}(2\lambda,\chi^2)-2\frac{L'}{L}(2\lambda+1,\chi^2)$
  up to finitely many local terms (Corollary 6.7).
- The residual terms $\operatorname{tr}(R(f)|_{V_b})$ and the ramified
  terms of Theorem 5.14(c), which the 1995 notes do not have,
  are already invariant. The ramified term is made explicit: $M(w,0)=-1$
  on $\mathcal H_B(\chi_{\psi_b})$, so it equals
  $-\frac14\operatorname{tr}I(\chi_{\psi_b,0},f)$
  (Proposition 6.13).
- The function $\varphi_A(f)$ that carries the correction is not the
  Fourier transform of a compactly supported function on $\overline{A(\mathbb{Q}_S)}$
  (Example 6.C); the 1995 definition (6.7) of the space
  that contains it is circular (item II.17), and its claim that this
  space equals the Paley–Wiener space of $\overline{A(\mathbb{Q}_S)}$ is false.

- **Lemma 6.1.** Example 6.1 of the 1995 notes computes $u'_B(k,y)=|H_B(ky)|$ (item II.15); the correct value is $-H(ky)$.

- **Theorem 6.5.** The theorem replaces Conjecture 6.10 of the 1995 notes; property (1) there, $R_{P'|P}(\chi)I_P(\chi,x)=I_P(\chi,x)R_{P'|P}(\chi)$, should have $I_{P'}$ on the right, as in (N1). At the real places the 1995 notes refer to Sally [Sa67], who treats the universal cover of $SL(2,\mathbb{R})$.

- **Corollary 6.7.** Part (a) is the relation $M^{-1}M'=m^{-1}m'+R^{-1}R'$ of Sections 6.1.1
and 6.2 of the 1995 notes, where the factor $m$ of $R_{\bar B|B}(\sigma)=
m(\sigma)^{-1}M_{\bar B|B}(\sigma)$ is not identified; (c) identifies
it.

- **The map $\varphi_A$, (6.11).** The 1995 notes have $R_A(\pi_\lambda,P_0)=+R^{-1}\frac{d}{d\lambda}R$, without the minus sign.

- **Theorem 6.9.** The step that needs the trace Paley–Wiener theorem for a Levi subgroup $L$ is where Conjectures 6.3–6.8 of the 1995 notes enter; for $L=A$ they are not needed. The 1995 condition (6.7) defining the space that contains $\varphi_A(f)$ is circular: it has $\phi(\sigma,X)$ on both sides (item II.17). The 1995 notes assert that $\mathcal I_{\mathrm{ac}}(\overline{A(\mathbb{A}_S)})=\mathcal I(\overline{A(\mathbb{A}_S)})$, the space of Fourier transforms of compactly supported functions; this is false, because $\mathfrak a_A\ne0$ (Example 6.C). The vanishing of $I_A(\pi,X,f)$ is Proposition 6.20 and Example 6.21 there.

- **Theorem 6.11.** In Section 6.4 of the 1995 notes, (a) has $\frac12a^A(S,z)I_A(z,f)$ and the sum
over $(G,S)$-classes of $a^G(S,\gamma)I_G(\gamma,f)$, as here
($I_G=J_G$), and (b), (c) agree with ours. The spectral item (b) there,
$\frac12\int a^A(\pi)I_A(\pi,f)\,d\pi$ with the remark that $I_A(\pi,f)=0$
for tempered $\pi$, is identically zero (item II.16). The book version
(`book7g.tex`, item (e)) has $\int a^G(\pi)\operatorname{tr}\pi(f)\,
d\pi$ with $a^G(I_A(\sigma))=-m'(\sigma)/m(\sigma)$, which is (e) above;
neither has the residual and ramified terms of (f). Theorem 6.22 there
(Arthur's [Ar88c, Cor. 4.5]; $v_\pi$ should be $\nu_\pi$) is the
statement that $I_\chi(f)=\int a^G(\pi)I_G(\pi,f)\,d\pi$, the term $M=A$
being $0$.

##### Section 7: the stable(r) form

Section 7 replaces Section 7 of the 1995 notes
(`cctrace7.tex`, which is `book7h.tex`) and uses the parts
of `book3b.tex` (“Local comparisons on the groups”) that concern
conjugation by $GL(2)$. The 1995 section was a program modeled
on [LL79], with most proofs referred to preprints that were not
written; the items below say what became of each part.

- **Stable conjugacy (Section 7.2).** The 1995 notes call two elements of the cover stably conjugate if they are conjugate by an element of $G_1(F)=GL(2,F)$, and a distribution stably invariant if $T(f^y)=T(f)$ for all $y\in G_1(\mathbb{A}_S)$. The cover of $G_1(F)$ is said there to be “defined using the cocycle $\beta$”, which is defined only on $SL(2)$ (item II.18); Section 2.3 fixes one. With that definition the two lifts of $\gamma$ are stably conjugate whenever $\eta_\gamma$ is not trivial on the norms (Lemma 7.2), every stably invariant distribution vanishes on genuine functions supported near such elements, and the functions $\delta\mapsto I_{\mathcal O}(f^\delta)$ of (7.5)–(7.8) are defined on $D(T/F)=T_1(F)\backslash G_1(F)/G(F)$ only up to the character $\eta_\gamma$. The action $\star$ of (7.3) removes the ambiguity.

- **Endoscopic groups.** Section 7.2 of the 1995 notes takes the Cartan subgroups of $SL(2)$ as the endoscopic groups of the cover, as for $SL(2)$ in [LL79], and writes the “endoscopic terms” (7.2) as $\frac14\sum_H\sum_\theta\langle\theta,f^H\rangle$ over characters $\theta$ of the elliptic tori $H$. For the double cover the elliptic endoscopic groups are two copies of $SO(3)$ [Li11], and the $\kappa$-orbital integrals are not functions to which Poisson summation on the torus is applied: they are stable orbital integrals of $f_-$ (Lemma 7.6(c)). Accordingly Proposition 7.2 (Poisson summation on $T$), Corollary 7.4, Lemma 7.20, Lemma 7.21 and the sums (7.20)–(7.21) over characters $\theta$ of tori have no counterpart here. In `book3b.tex` the $L$-group of the cover is said to be $PGL(2,\mathbb{C})$ (item C.4); it is $SL(2,\mathbb{C})$ (Section 7.2).

- **Theorem 7.7.** This replaces (7.3)–(7.8), Lemma 7.5 and the elliptic part of (7.20). Three corrections (item II.19): $T(\mathbb{Q})$ is not discrete in $T(\mathbb{A}_S)$, so the statement is adelic; the index $[D(T/\mathbb{Q}):D(T/\mathbb{A}_S)]^{-1}$ is the factor $\frac12$, by the Hasse norm theorem and class field theory; and Lemma 7.5(a), as stated, is about $I^{\mathrm{st}}_{\mathcal O}$, not $SI_{\mathcal O}$. The local sets $D(T/F)$ are $F^\times/N E^\times$.

- **Proposition 7.9 and Lemma 7.8.** Section 7.4 of the 1995 notes forms $D(A/F)$ with $A\cdot Z$ in place of the centralizer of $A$ in $G_1$, which gives $F^\times/F^{\times2}$, and sums over it with an index $[D(A/\mathbb{Q}):D(A/\mathbb{A}_S)]$ that is not defined, since $\mathbb{Q}^\times/\mathbb{Q}^{\times2}$ does not embed in a finite group (item II.20). For a hyperbolic element the stable class is the conjugacy class; the group $F^\times/F^{\times2}$ acts on its two lifts through $(a,t)_v$ (Lemma 7.1(d)), and Proposition 7.9(b) is what remains of (7.9)–(7.10). Lemma 7.6 there (stability of $SI_{\mathcal O}$ for these classes) is not proved and is not claimed here (see the remark after Remark 2026.18). Lemma 7.7 is the identity $\operatorname{tr}I(\pi,f)=\int\pi(\tilde a)J_G(\tilde a,f)\,d\tilde a$ used in Proposition 7.9(c). Lemmas 7.8, 7.9 and 7.23, on the operator $N(g)$ of multiplication by $\log\delta(kg)$ and the variance of $J_A$ and of $\operatorname{tr}(R^{-1}R'I_A(\sigma,f))$ under $g\in G_1(F)$, are Lemma 7.8; the 1995 statements omit the change $\gamma\mapsto\operatorname{Ad}(\delta)\gamma$, $\sigma\mapsto\sigma\kappa_a$ and the condition (N5). In the proof sketched in `book3b.tex` the matrix identity for $wn(x)$ is wrong (item C.1); the correct factorization is $wn(x)=n(-x^{-1})\,a(x^{-1})\,\bar n(x^{-1})$, and the weight is $v_A=-H(x)-H(wx)$ (Lemma 4.3). The identification of $K$ with the subset $(K,1)$ of the cover in Section 7.4 (item I.1) is not used.
- **Proposition 7.8′.** New. The 1995 notes take normalizing factors from Arthur's general theorem and do not ask how they behave under $\pi\mapsto\pi\kappa_a$; the variance formulas of their Section 7.4 need the property (N5). The proposition constructs factors with (N1)–(N5) from the scalar $M_v(\pi^w,-\lambda)M_v(\pi,\lambda)$, and identifies them with $L_v(2\lambda,\chi_v^2)/L_v(2\lambda+1,\chi_v^2)$ up to a constant by the computations of Szpruch [Sz09; Sz16], which postdate the notes.

- **The weight (7.13).** The formula $v_A=\sum_v\log\sqrt{|1+n_v^2|_v}$ holds only at real places (item II.22); see Lemma 4.9.

- **Proposition 7.10.** This replaces Section 7.5 of the 1995 notes. Equation (7.17) there sums over the rational unipotent classes $a\in\mathbb{Q}^\times/\mathbb{Q}^{\times2}$ and diverges, and its middle equality is wrong (item II.21); the correct expansion is over the finitely many quadratic Hecke characters unramified outside $S$, with the coefficients $L^S(1,\kappa)$. Definitions 7.12 and 7.13 use the transfer factor $\lambda(E/F,\psi)\kappa\bigl((\gamma_1-\gamma_2)/(\gamma_1^0-\gamma_2^0)\bigr)$ of [LL79] for $SL(2)$; for the cover the corresponding function is $\Delta_\psi$ of Lemma 7.3. Lemmas 7.14–7.16 (smoothness of the normalized $\kappa$-orbital integrals on the torus and their limits at $\pm1$) are not proved, here or there; the statement of Lemma 7.15 lacks an equality sign and has a constant depending on $\gamma$ inside a limit.

- **Proposition 7.12 and Lemma 7.11.** Definition 7.18 of the 1995 notes introduces the set $L(\pi)$ of the $\pi\circ\operatorname{Ad}(g)$, $g\in G_1(F)$, and Remark 7.19 asserts that it has $\prod_{v\mid p}\#(k_v^\times/k_v^{\times2})$ elements for every genuine $\pi$ (item II.23; item C.2). This is not so in general: $I(\pi)\circ\operatorname{Ad}(\delta_a)=I(\pi\kappa_a)$ (Proposition 7.9(c)), which is equivalent to $I(\pi)$ when $\pi\kappa_a=\pi^w$, that is, when $\chi_v^2=(a,\cdot)_v$; and $r^\pm_{\psi}\circ\operatorname{Ad}(\delta_a)=r^\pm_{\psi_a}$ (Lemma 7.4). The sets $L(\pi)$ are not the packets of the cover; those are Waldspurger's, of which Proposition 7.12 treats one family. Lemma 7.20 states no assertion.

- **Theorem 7.13.** This replaces (7.1), (7.25) and the list (a)–(i) of Section 7.8. The distributions $S_1$, $S_2$, $S_3$ of (7.22)–(7.24) are, in the present notation, the correction $\Phi_A$, the weighted orbital integrals $J_A$ (the two together are the terms $I_A$) and the unipotent terms $J^\kappa_{\mathrm{unip}}$. Conjecture 7.24, that $S_1+S_2+S_3$ is invariant under $G_1(\mathbb{A}_S)$, does not hold for the cover as stated: by Proposition 7.9(b) the term of $a(t)$ is multiplied by $(\det h,t)_S$. What replaces it is the equivariance in Theorem 7.13(c), and Li's stabilization [Li21]. The term (g) of Section 7.8, with $m'/m$, is Theorem 6.11(e)–(f).

- **`book3b.tex`.** Its first lemmas assert that the orbital integral of a genuine function at a lift of $a\in A(F)$ vanishes unless $a$ is an $N$-th power. For $n=2$ the centralizer of the lift is the full preimage of $A$ (Lemma 4.1) and the orbital integral does not vanish; what vanishes for non-squares is its average over the $G_1(F)$-orbit (Lemma 7.6(b)). The correspondence $\chi\leftrightarrow\bar\chi$ between characters of $A(F)$ and genuine characters of its cover, defined there by cases, is multiplication by Weil's character $\chi_\psi$ (Lemma 3.5), whose inverse is the restriction of $\Delta_\psi$ to the cover of $A$ (Lemma 7.3(c)). The real Hilbert symbol is misdefined there as the sign of the first argument (item C.3); see (H3).


### What was not done, and what could not be verified

- Rule 3.4 for every definition: about 40 further definitions have no example of their own (§§2.1.3–2.1.5, 2.2, 3.2–3.3, 4.2 (kernels), 4.4 (D(γ)), 4.5, 5.3, 6.3, 7.5 (H_1) and others).
- Rules 3.5–3.7 (symbols defined at first use, hypotheses before theorems, no skipped steps) and Section 4 of the guide were not re-checked. That would be a referee pass, and this pass makes no mathematical changes.
- Rule 8.4 (scripts cited by commit hash): not done. The paper names the scripts by path.
- The fonts: built with `mathptmx`, not newtx. Under newtx the line breaks will differ, and the build should be rechecked for overfull boxes.
- The Markdown above, from the former Appendix A, writes the paper's LaTeX math as `$…$`, which GitHub renders. It was converted by script. The `\ref`s were resolved from the compiled draft. It has not been proofread against the PDF of the previous draft.
- Layout. Five overfull boxes in the 12pt build were removed without manual line breaks and without changing wording: equation (2.3) uses `\quad` instead of `\qquad`; the local integral Z_v after (4.9) and the kernel K_{G,χ} in Proposition 5.9(a) became displays; the proof of Lemma 6.3 has its parts (a), (b), (c) as separate paragraphs; the three identities in Proposition 7.8′(a) are set on two lines (`gather*`). Underfull boxes were left.

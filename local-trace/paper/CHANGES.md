# Changes from the 1997 version

Companion to `local-trace-formula-2026.tex`. Prepared by Claude (Anthropic) for D. Joyner, 2026-11-10.

For each item of the errata log [`../original-1997/transcription_log.md`](../original-1997/transcription_log.md), this file records what the 2026 revision does with it. "R n" refers to the dated **Remark 2026.n** in the paper. Those remarks mark every substantive change and everything not fully verified.

**Dispositions:**
- **fixed**: corrected silently in the text
- **fixed (R n)**: corrected, with a dated remark
- **superseded**: the passage is replaced by new text
- **removed**: deleted (not needed)

## The Remarks 2026.n

| R | Topic | Kind |
|---|---|---|
| 1 | scope: semisimple G (anisotropic center) | correction (referee 2, M1) |
| 2 | exponent in c_α | correction; non-split case not re-derived |
| 3 | Lemma 2.1: constant Q_G and chamber | correction; verified in rank one |
| 4 | Lemma 2.8 | false without saturation of the coroot lattice; restated and proved (referee 2, M2) |
| 5 | §2.5 lemmas | Lemmas 2.7, 2.9 not re-checked against [Wa89a]; unused |
| 6 | Casselman's asymptotics (3.1), input (C) | (C) essential, unverified for intermediate parabolics |
| 7 | Lemma 3.3 | correction; restated with the opposite parabolic |
| 8 | false claim on p. 18 | deleted |
| 9 | Lemma 3.5A (Brion) | proved (Lemmas 3.5B–C); checked for SL(3), PGL(3) |
| 10 | Proposition 3.6 | new proof; conditional on (C) in rank ≥ 2 |
| 11 | Lemma 4.1 and regularity | not used; (G,A)~-smoothness is insufficient |
| 12 | Proposition 4.2 | new form; confluence replaced by Lemma 3.5B(ii) |
| 13 | Theorem 4.5 | (a) unconditional, (b) under (C) and (R) |
| 14 | Conjecture 4.6 | new; verified for PGL(2), SL(2) |
| 15 | §5 | rewritten; normalizations checked only for SL(2) |
| 16 | §6.2 SL(2) | proved for all q; also verified numerically and symbolically |
| 17 | §7 Route B | proposed route; normalizations not checked |
| 18 | literature | all entries checked |

## Main mathematical changes

1. **Macdonald's formula** (Lemma 2.1): the constant is Q_G = Σ(IwI:I)^{-1}, and on the chamber A^- the coefficient of (wχ)(a) is c((wχ)^{-1}). [R3]
2. **Casselman's asymptotics** ((3.1), Lemmas 3.3–3.4): opposite parabolic, δ_P^{1/2}, regions A^-_P(ε), with ε depending on the level. [R6, R7]
3. **Lemma 3.5** (false) is replaced by **Lemma 3.5A**, Brion's vertex decomposition over the vertices T_Q. [R9]
4. **Proposition 3.6** has a new statement (vertex terms ψ(T_Q)·R plus a T-independent remainder J_G) and a new direct proof (partition of the dominant cone plus Brion), replacing the 1997 induction. [R10]
5. **Proposition 4.2**: I^T is an exponential polynomial in T, and I(χ,φ) is *defined* as its T-independent part. [R12]
6. **Theorem 4.5**: (a) the truncated identity holds unconditionally; (b) the spectral identity holds under the new **Hypothesis (R)**. [R13]
7. **Correction to the main claim.** For SL(2), (R) fails and the spectral measure has an atom at the unramified quadratic character (Proposition 6.4, verified numerically). New Conjecture 4.6 describes the general shape. [R14, R16]
8. **§5** is rewritten: signs of κ, the group 𝔇(S), the endoscopic groups H_m, the fundamental lemma (now a theorem), and Propositions 5.1–5.2, which answer the 1997 closing question. [R15]

## New material

- §2.0 Conventions
- §6 Worked examples: PGL(2) (Theorem 6.1) and SL(2) (Proposition 6.4)
- §7 Route B (from Arthur's local trace formula)
- §8 Literature review
- Appendix A Glossary
- Appendix B Concordance

New numerical check: [`../examples/sl2/sl2_check.py`](../examples/sl2/sl2_check.py).

## Item-by-item disposition of the errata log

### 0. Transcription notes
| # | Disposition |
|---|---|
| 0.1–0.7 | not applicable (the revision is newly typeset, with `\cite`-style labels and ⟨ ⟩ brackets) |
| 0.8 | the footnote history is merged into "About this revision" (G5) |

### 1. Abstract and Introduction
| # | Disposition |
|---|---|
| 1.1 | fixed (reductive G, G(F)^1) |
| 1.2 | fixed; the abstract is rewritten (compact torus vs. complex torus; atoms) |
| 1.3, 1.4, 1.7 | fixed (§§3–4, §5, §4) |
| 1.5, 1.6, 1.8, 1.9, 1.10 | fixed |
| 1.11 | fixed ([Wa91]) |
| 1.12 | fixed (Naval Academy Research Council; supplied by the author) |
| 1.13 | fixed ("compactly generated support modulo conjugation", [Ka86, §4]) |

### 2. Notation and background
| # | Disposition |
|---|---|
| 2.1 | fixed (M_0 = Z_G(A)) |
| 2.2, 2.10, 2.39, 2.43 | fixed (Arthur's notation: Δ^∨ coroots, Δ̂ = {ϖ_α}; one lattice L^∨) |
| 2.3, 2.5, 2.15, 2.16, 2.17, 2.19, 2.22, 2.27, 2.28, 2.32, 2.35, 2.47, 2.48 | fixed (typos) |
| 2.4 | fixed (criteria restricted to split G) |
| 2.6 | fixed (P_∅ = B, M_∅ = M_0) |
| 2.7 | fixed (X = X_P + X^P, §2.0) |
| 2.8 | fixed (τ̂ defined by the fundamental weights) |
| 2.9 | fixed (free generation only for simply connected G) |
| 2.11, 2.12, 2.13, 2.14, 2.23, 2.24 | fixed ((2.6)–(2.7) rewritten: complex torus T̂, compact torus T̂^u, lattice L^∨) |
| 2.18 | fixed (R2) |
| 2.20, 2.21 | fixed (R3) |
| 2.25, 2.26 | fixed (f_1^∨ f̄_2^∨; polarization with f_1 + i f_2) |
| 2.29 | fixed (W_M\W, minimal-length representatives, throughout) |
| 2.30 | fixed |
| 2.31 | fixed ("irreducible" deleted) |
| 2.33, 2.34 | fixed (Remark 1 restated as a direct-sum statement and moved after the proof) |
| 2.36, 2.37, 2.44, 2.45 | fixed (one definition, χ_λ(a) = q^{−⟨ν_A(a),λ⟩}; hyperplanes via α^∨) |
| 2.38 | fixed ((G,M)-families defined) |
| 2.40, 2.41, 2.42 | fixed |
| 2.46 | fixed (Lemma 2.9 restated as the proof via Lemma 2.8 gives it; R5) |
| 2.49 | fixed (role of §2.5 explained; R5, R11) |

### 3. Inner products of matrix coefficients
| # | Disposition |
|---|---|
| 3.1, 3.2 | fixed (R6) |
| 3.3 | fixed (proof of Lemma 3.1) |
| 3.4, 3.5, 3.6 | fixed |
| 3.7, 3.8, 3.9, 3.10 | superseded (new proof of Lemma 3.2 via cuspidal support and multiplicity one) |
| 3.11, 3.12, 3.13, 3.14 | fixed (Lemma 3.3 restated; R7) |
| 3.15 | fixed (Remark 4 restated) |
| 3.16–3.21 | fixed (proof of Lemma 3.3) |
| 3.22–3.28 | fixed (Lemma 3.4 restated and reproved) |
| 3.29 | fixed (K_n normal in K) |
| 3.30 | fixed (section title) |
| 3.31 | fixed (claim deleted; R8) |
| 3.32, 3.33, 3.35, 3.37, 3.38, 3.39 | superseded (Lemma 3.5A; R9) |
| 3.34, 3.36 | superseded |
| 3.40 | fixed ((3.7): Q_a = Q_G/Q_{W_a} ∈ ℚ) |
| 3.41, 3.42 | fixed ((3.8) restated) |
| 3.43, 3.44, 3.45 | superseded (Proposition 3.6, 2026 form) |
| 3.46 | superseded (the structural claim is dropped; R10) |
| 3.47 | removed (Remark 7 not needed) |
| 3.48 | fixed (Proposition 3.7 with κ\|_{M_0}) |
| 3.49–3.69 | superseded (the 1997 inductive proof is replaced; R10. Note that the new Proposition 3.6 uses equation number (3.9), which in 1997 was inside the proof) |

### 4. Integrating the kernel
| # | Disposition |
|---|---|
| 4.1, 4.4, 4.5, 4.6 | removed (the 1997 paragraph after (4.1) is replaced) |
| 4.2, 4.7, 4.8 | fixed |
| 4.3 | fixed (θ̃ removed from (4.1)) |
| 4.9, 4.10, 4.11 | fixed ("truncated orbital integral"; §5; G′(T) defined) |
| 4.12, 4.26 | superseded (Proposition 4.2 and Theorem 4.5, 2026 form; R12, R13) |
| 4.13, 4.14, 4.15 | fixed |
| 4.16, 4.21 | fixed (T_w^* is the transpose; compact picture) |
| 4.17, 4.18, 4.19 | fixed (basis of the K_n-fixed vectors; u_j, not u_j^*, in (4.7)) |
| 4.20, 4.22 | fixed |
| 4.23 | fixed (f ∈ C_c^∞ in (4.8), f ∈ ℋ(G,K) from Lemma 4.4 on) |
| 4.24, 4.25 | fixed |
| 4.27, 4.28 | fixed (Weyl discriminant \|D(s)\|; tori renamed S) |

### 5. κ-stable trace formula on SL(n)
| # | Disposition |
|---|---|
| 5.1, 5.2, 5.3, 5.4, 5.7 | fixed ((5.1) rewritten) |
| 5.5, 5.8 | fixed |
| 5.6 | fixed ((5.2)–(5.4) rewritten with 𝔇(S); R15) |
| 5.9 | removed (parenthetical) |
| 5.10, 5.17 | fixed (fundamental lemma: Kazhdan, Waldspurger, Hales, Ngô) |
| 5.11, 5.12 | fixed |
| 5.13, 5.14 | fixed (H_m = ker(N∘det) ⊂ Res_{E/F} GL(n/m); norm-one torus) |
| 5.15 | fixed (Theorem 4.5 stated for reductive G; Proposition 5.2 assumes a stable version for H; R15) |
| 5.16 | superseded (Proposition 5.1) |
| 5.18 | fixed (stable orbital integral SΦ^H) |
| 5.19 | fixed (ι for the L-embedding) |

### 6. Bibliography
| # | Disposition |
|---|---|
| 6.1, 6.2, 6.5, 6.7, 6.9–6.14 | fixed |
| 6.3 | removed ([BD] was never cited) |
| 6.4 | fixed (order) |
| 6.6 | fixed (unpublished notes, 1974/1995) |
| 6.8 | fixed ([Jo97]: announced in 1997, never written up or published, as confirmed by the author) |
| 6.15 | fixed (citation updated; the lemma number is no longer needed) |
| 6.16 | fixed (references added) |

### 7. Global items
| # | Disposition |
|---|---|
| G1 | fixed (§2.0) |
| G2 | fixed (T only for truncation; tori M_0, S; 𝟙_E; Q_G) |
| G3 | fixed (road map in §1) |
| G4 | fixed (§6) |
| G5 | fixed ("About this revision") |
| G6 | fixed (Appendix A, §8) |

### 8. Additions from the PGL(2) example
| # | Disposition |
|---|---|
| 8.1, 8.2 | fixed (Lemma 2.1; R3) |
| 8.3 | superseded: correct for PGL(2), false for SL(2) (Theorem 6.1, Proposition 6.4, Conjecture 4.6) |
| 8.4 | fixed (Theorem 4.5 and §6.1; R13) |
| 8.5 | fixed (Proposition 3.6: remainder J_G; Remark 6.3) |

## Other corrections found during the revision

- `common/references.bib`: Beuzart-Plessis (2020) is Astérisque **418**, not 417 (AMS bookstore; SMF catalogue, DOI 10.24033/ast.1120).
- The referee report's suggested repair M8(b) (smoothness of the (G,A)~-sum plus Riemann–Lebesgue) is insufficient. The (G,A)~-sum is smooth for each T but not uniformly in T, and the SL(2) example shows the limit can be a point mass. [R11]

## Changes of 2026-11-10 (second pass, at the author's request)

- Title page: "Revised, corrected and updated", authors David Joyner and Claude, dates 1992 / November 2026.
- NARC expanded (Naval Academy Research Council); the remark asking for it is removed, so the later remarks are renumbered (Remark 2026.1–2026.16).
- Bibliography labels changed to the form [Xn]: author letters plus the last two digits of the year (e.g. [Cas1] → [Cas80], [W] → [Wa89a], [Key] → [Ke82], [J] → [Jo97]). Entries are sorted by label.
- [Jo97] is now cited in §1 as the unpublished paper announced in 1997.
- The literature review (§8) is split at 1992, the year of publication, instead of 1997.

## Changes of 2026-11-10 (third pass: second referee report)

The report and a point-by-point response are in [`RESPONSE-TO-REFEREE-2.md`](RESPONSE-TO-REFEREE-2.md). In summary:

- **Scope (M1).** The standing hypothesis is now (H): G semisimple, or more generally with anisotropic center, as in 1992. G(F)^1 is replaced by G(F) throughout. [R1]
- **Lemma 2.8 (M2).** Restated under saturation of the coroot lattice and proved; the PGL(2) counterexample is recorded; Lemma 2.9 carries the same hypothesis, and §7.4 no longer invokes it. [R4]
- **Proposition 3.6 (M3).**
  - Casselman's input (C) is stated explicitly, and the proposition is conditional on it in rank ≥ 2.
  - New Lemma 3.5B (Brion's theorem for half-open polytopes and degenerate characters) and Lemma 3.5C (positivity) supply the combinatorial steps in full.
  - Step 1 now says explicitly that the regions do not depend on T.
  - New numerical check: `examples/rank2/brion_check.py` (SL(3), PGL(3)). [R6, R9, R10]
- **Proposition 4.2 (M4).** The confluence argument is replaced by a direct application of Lemma 3.5B(ii) with χ′ = χ^{-1}. The introduction no longer claims G-admissibility. [R12]
- **Theorem 4.5 and Conjecture 4.6.**
  - (R) is described as a strong hypothesis.
  - New paragraph distinguishing a functional, a distribution and a measure on the spectral side.
  - §7.4 is rewritten as a proposed route, not a proof. [R13, R14, R17]
- **§5.**
  - 𝔇(S) uses the image of SL(n,F).
  - Normalizations are stated, and the fundamental lemma is given in the Langlands–Shelstad sum form (5.10) before specializing to (5.11).
  - New Lemma 5.0: ramified κ do not contribute.
  - Proposition 5.1 (unconditional) is separated from Proposition 5.2 (conditional). [R15]
- **§6.**
  - The SL(2) example now uses any depth-zero unramified elliptic γ, so it works for every q. [[0,−1],[1,0]] qualifies only when −1 is a non-square mod π.
  - New Lemma 6.1A proves (R) for PGL(2) for arbitrary test functions φ. [R16]
- **Exposition.**
  - "What is proved" summary in §1; status table updated.
  - Acknowledgements moved to the end.
  - §7.1–7.4 are now real subsections.
  - All "not verified" bibliography flags removed after checking; OS13 pages added.

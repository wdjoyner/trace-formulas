# Route B: spherical orbital integrals from Arthur's local trace formula — outline

*Outline of a companion paper to the revised "Simple local trace formulas for unramified p-adic groups" (`../paper/`). Draft of 10 November 2026, D. Joyner and Claude.*

**Working title.** *The spectral measure of an elliptic orbital integral, via Arthur's local trace formula.*

**One-sentence summary.** Apply Arthur's local trace formula to a test function f₁ ⊗ f₂, with f₁ spherical and f₂ supported on the regular elliptic set. Most terms then vanish. What survives expresses the elliptic orbital integrals of spherical functions as an integral over the unitary unramified characters, with:
- an absolutely continuous part, given by a weighted character;
- a singular part, given by Arthur's elliptic tempered virtual characters that have K-fixed vectors. These live exactly where the R-groups are non-trivial.

The companion paper ("Route A") derives the same identity by truncation and Brion's theorem, but in general it proves the full identity only under the regularity Hypothesis (R). Route B aims at the general statement, Conjecture 4.6. Route A, in turn, supplies explicit formulas that Route B does not.

---

## 0. Abstract (draft)

Let G be an unramified semisimple p-adic group with hyperspecial maximal compact subgroup K. For γ regular elliptic and f spherical, we show that the orbital integral O_γ(f) can be written as ∫ f^∨ dI_γ, where:
- f^∨ is the Satake transform of f;
- dI_γ is a finite signed measure on the unitary unramified characters modulo W;
- dI_γ = I(χ,γ) dμ(χ) + dI_γ^sing, where dμ is the Plancherel measure, the density I(χ,γ)ρ(χ) is a weighted character of the unramified principal series, and dI_γ^sing is a finite sum of measures on proper subtori, one for each elliptic tempered virtual character with a K-fixed vector.

When Z(G) is connected the singular part vanishes. For SL(n) it is given by κ-orbital integrals, which are push-forwards from elliptic endoscopic groups. The proof specializes Arthur's local trace formula and his description of elliptic tempered characters. Finally, the density is compared with the T-independent part of the truncated kernel of the companion paper, and the examples PGL(2), SL(2), PGL(3) and SL(3) are worked out.

---

## 1. Introduction

1. **The problem.** We study the spectral expansion (1.5) of the companion paper,

   O_γ(f) = ∫_{Θ̂ᵘ/W} f^∨(χ) dI_γ(χ),  for f ∈ H(G,K),

   together with its smeared form T_φ(f) = ∫ f^∨ dI_φ. The aim is to explain what kind of object dI_γ is.
2. **What Route A gives**, with pointers into the companion paper:
   - Theorem 4.5(a): the identity holds exactly with the truncated kernel I^T.
   - Proposition 4.2: the T-independent part I(χ,φ).
   - Theorem 4.5(b): the full identity, under (R).
   - §6: the PGL(2) and SL(2) examples (no singular part, and an atom, respectively).
   - Appendix B: PGL(3), where (R) fails but there is no singular part.
3. **What Route B adds.** An existence theorem for dI_φ that needs no regularity hypothesis, with a representation-theoretic description of both parts.
4. **Statements.** These are targets; the status of each is in §11.
   - **Theorem A** (existence). dI_φ is a finite complex measure on Θ̂ᵘ/W (Conjecture 4.6(a)).
   - **Theorem B** (absolutely continuous part). I(χ,φ)ρ(χ) = c_G · J_{M₀}(χ⁻¹, φ). Here J_{M₀} is Arthur's weighted character, built from the canonically normalized unramified intertwining operators, and c_G = (−1)^{dim A₀/A_G}/|W| (Conjecture 7.3).
   - **Theorem C** (singular part). dI_φ^sing = Σ_{M ⊋ M₀} Σ_τ (measure on a subtorus of dimension dim A_M), where τ runs over the elliptic tempered virtual characters of M that have (K ∩ M)-fixed vectors. In particular dI_φ^sing = 0 when all R-groups of the unitary unramified principal series are trivial, e.g. when Z(G) is connected (Conjecture 4.6(b)).
   - **Theorem D** (SL(n)). For SL(n), dI_φ^sing is a sum of push-forwards of stable spectral measures of elliptic endoscopic groups (Conjecture 4.6(c), Proposition 5.2).
5. **Why this is useful.** It is an introduction to Arthur's local harmonic analysis through a case where every term can be made explicit, and it gives an independent proof of the companion paper's identity.
6. **Plan of the paper.**

## 2. Background on the unramified principal series

1. Unramified characters, Satake transform, Macdonald's formulas. Brief, citing §§2.1–2.3A of the companion paper.
2. **Normalized intertwining operators.**
   - The operators J_{P'|P}(χ) and their normalization R_{P'|P}(χ) = r_{P'|P}(χ)⁻¹ J_{P'|P}(χ).
   - In the unramified case the normalizing factors are explicit: ratios of abelian L-functions L(0, α^∨∘χ)/L(1, α^∨∘χ) over the reduced roots.
   - With this normalization R fixes the spherical vector, which is the key to §5.
   - Compare Arthur's canonical normalization of weighted characters [Ar98] and Langlands' normalizing factors [La76].
3. **R-groups.**
   - Knapp–Stein theory, and Keys' computation for unramified principal series of Chevalley groups [Ke82].
   - When Z(G) is connected the R-groups are trivial.
   - For SL(n), R(χ) is cyclic of order dividing n, and it is non-trivial on explicit subtori.
4. **(G,M)-families and weighted characters.**
   - Arthur's (G,M)-families [Ar81] and the limit c_M.
   - The weighted characters J_M(π, f) = tr(R_M(π,P) I_P(π, f)) [Ar89b].
   - Explicit form for M = M₀ and unramified π: the operator R_{M₀}(χ, P) acts on the K-fixed vector by a logarithmic derivative of products of c-functions.

## 3. Arthur's local trace formula

1. **The setting.** The representation R of G(F) × G(F) on L²(G(F)), the kernel K_f, Arthur's truncation u(x,T), and the asymptotic polynomial J^T(f) [Ar89a], [Ar91].
2. **The non-invariant formula** [Ar91]: geometric expansion (weighted orbital integrals J_M(γ, f)) = spectral expansion (weighted characters J_M(π, f)).
3. **The invariant form** [Ar91, §§? to fix] and the elliptic reformulation via the virtual characters T_ell(M) [Ar93]. This is the form used below.
4. **Splitting and descent formulas** for distributions on G(F) × G(F) [Ar88]. These include the coefficients d_M^G(L₁, L₂).
5. **Convergence and the Schwartz space.** These matter when the test function is not compactly supported: the trace Paley–Wiener theorem for Schwartz functions [Ar94b], and Waldspurger's exposition of the Plancherel formula [Wa03].

## 4. The geometric side for f₁ spherical and f₂ elliptic

1. The diagonal kernel x ↦ K_f(x,x) is compactly supported modulo A_G (Kazhdan [Ka86]; Lemma 4.4 of the companion paper). So J^T(f) is constant for large T and equals T_φ(f).
2. **Vanishing of the terms with M ≠ G.** The weighted orbital integrals J_M(γ, f₁ ⊗ φ) vanish for M ≠ G, because φ is zero off the elliptic set. A check is needed for singular γ and for the measure-zero boundary.
3. The surviving M = G term is the Weyl integration formula (4.10)–(4.11) of the companion paper.

## 5. The spectral side

1. **Splitting.** For f = f₁ ⊗ f₂, Arthur's splitting formula writes J_M(π, f) as Σ_{L₁,L₂} d_M^G(L₁,L₂) J_M^{L₁}(π, f₁,Q₁) J_M^{L₂}(π^∨, f₂,Q₂).
2. **f₁ spherical.**
   - The normalized operators fix the spherical vector, so J_M^{L₁}(π, f₁) = 0 for L₁ ≠ M. This forces L₂ = G.
   - tr π(f₁) ≠ 0 only if π has a (K ∩ M)-fixed vector.
   - Gap to check: the weighted characters of f₁ for L₁ ⊋ M vanish only once the logarithmic derivatives of the normalizing factors are accounted for. Carry this out with the explicit factors of §2.2.
3. **f₂ elliptic.**
   - φ is cuspidal, so only elliptic spectral data contribute in the L₂ = G factor.
   - Use Arthur's description [Ar93]: the spectral side becomes a sum over M and τ ∈ T_ell(M) of tr τ(f₁) · J_M(τ^∨, φ), integrated over the unramified twists of τ.
4. **Classification of the surviving τ.** These are the elliptic tempered virtual characters of Levi subgroups with K-fixed vectors.
   - M = M₀: all unitary unramified χ, integrated over Θ̂ᵘ. This gives the absolutely continuous part.
   - M ⊋ M₀: τ comes from unramified principal series of M whose R-group contains an elliptic element. Such τ live on subtori of dimension dim A_M.
   - References: Keys [Ke82] for R-groups; Reeder [Re01] and Opdam–Solleveld [OS13] for the elliptic theory of Iwahori-spherical representations.
5. **Result.** The spectral measure, with its absolutely continuous and singular parts.

## 6. Main theorem and proof

1. Statement (Theorems A–C).
2. **Proof.** Equate §4 and §5. Use density of the Satake transforms in C(Θ̂ᵘ/W) to identify measures. Show that the total variation is finite; this needs a uniform bound on J_M(τ^∨, φ) for φ of fixed level.
3. **Normalizations.** All constants, signs and measures, collected in one place:
   - |W₀^M|/|W₀^G|;
   - (−1)^{dim A_M/A_G};
   - measures on T_ell(M);
   - the Plancherel density, which converts dχ into dμ.

## 7. Comparison with Route A

1. **The two truncations.**
   - Arthur's u(x,T) and the set G(T) of Route A are both defined by the convex hull of W·T.
   - Route A's vertex terms ψ(T_Q) R_Q are periodic versions of Arthur's e^{λ(T_Q)} c_Q(λ)/θ_Q(λ).
   - Limitation: Lemma 2.8 gives the dictionary only when the coroot lattice is saturated (Remark 2026.4).
2. **Proof of Theorem B.** Show that the T-independent part I(χ,φ) of Proposition 4.2 equals c_G J_{M₀}(χ⁻¹, φ)/ρ(χ).
   - Plan: compute both as constant terms of exponential polynomials in T. In rank one, the constant term of Σ_Q e^{λ(T_Q)} c_Q(λ)/θ_Q(λ) at λ = 0 is a logarithmic derivative of an intertwining operator, which is visible in (6.5) of the companion paper.
3. **What Hypothesis (R) means in Arthur's terms.** (R) asks each oscillatory term to be regular. This is stronger than "no singular part". In PGL(3) (Appendix B), the oscillatory coefficients have poles on the non-root subtori z_i³ = 1, but these poles cancel in pairs. This is consistent with Theorem C, because the R-groups of PGL(3) are trivial. Explain the weaker condition (R′) of Remark 2026.20 from this point of view.

## 8. Endoscopy: SL(n)

1. κ-orbital integrals, the groups H_m, and transfer.
   - The fundamental lemma is a theorem (Ngô and others; companion §5).
   - Arthur's local character relations [Ar96] and the transfer of weighted orbital integrals [Ar99].
2. **Stabilization of the local trace formula.** Arthur's stable trace formula papers I–III (2001–2003), and Peng's explicit stable local trace formula (arXiv:1608.00055) as a model.
3. **Theorem D.** The singular part of dI_γ for SL(n) is a sum, over the unramified κ of 𝔇(S), of push-forwards of the stable spectral measures of H_m. This removes the hypothesis of Proposition 5.2 of the companion paper.
4. The case where κ has order n (H a torus), which gives explicit atoms (Proposition 5.1).

## 9. Examples

1. **PGL(2).**
   - Compute J_{M₀}(χ⁻¹, φ) explicitly for each elliptic type (U_r), (R_r), (R′).
   - Compare with Theorem 6.1 of the companion paper: verify Theorem B in rank one, with constants.
   - Check: `examples/pgl2/pgl2_check.py`, extended.
2. **SL(2).** There is one virtual character τ = π⁺ − π⁻ at χ₀ in T_ell(G). Verify that tr τ(f) = f^∨(χ₀) and that J_G(τ^∨, φ) is the κ-orbital integral, giving the atom ½ f^∨(χ₀) of Proposition 6.4.
3. **PGL(3).** The R-groups are trivial, so Theorem C predicts no singular part, as found numerically in Appendix B. Compute the weighted character for the depth-0 element γ and compare it with the closed form (B.4).
4. **SL(3)** (new). Take an elliptic γ from the norm-one torus of the unramified cubic extension.
   - The R-groups are non-trivial at the isolated characters χ = (1, ζ, ζ²), with ζ a primitive cube root of unity. At these points a 3-cycle in W fixes χ and acts on 𝔞₀ without fixed vectors, so it is elliptic.
   - Theorem C predicts atoms there, of total mass given by the κ-orbital integral for κ of order 3 (Proposition 5.1).
   - Numerical check on the building of SL(3), adapting `examples/pgl3/building.py` to vertices of a single type.
5. Optionally, GL(n) (Waldspurger [Wa89a]), to compare normalizations.

## 10. Literature

- Arthur's local harmonic analysis program:
  - "Towards a local trace formula" [Ar89a];
  - "A local trace formula" [Ar91];
  - "On elliptic tempered characters" [Ar93];
  - "On the Fourier transforms of weighted orbital integrals" [Ar94a];
  - the trace Paley–Wiener theorem for Schwartz functions [Ar94b];
  - "On local character relations" [Ar96];
  - "Canonical normalization of weighted characters and a transfer conjecture" [Ar98];
  - "On the transfer of distributions: weighted orbital integrals" [Ar99];
  - the stable trace formula.
- The Plancherel formula [Wa03]; Kazhdan's cuspidal geometry [Ka86]; the trace Paley–Wiener theorem [BDK86].
- Later local trace formulas: twisted (Mœglin–Waldspurger), relative (Feigon; Delorme–Harinck; Beuzart-Plessis [BP20]), and on symmetric spaces (e.g. H. Li, arXiv:2105.00087).

## 11. Status and work plan

| Step | Content | Status / difficulty |
|---|---|---|
| §4 | geometric side reduces to M = G | routine; check singular γ |
| §5.2 | vanishing for L₁ ≠ M with spherical f₁ | needs the explicit normalizing factors; moderate |
| §5.3–5.4 | elliptic reduction, classification of τ | uses [Ar93], [Ke82], [Re01]; moderate |
| §6.2 | finiteness of the measure | uniform bounds on weighted characters at fixed level; hard part of Theorem A |
| §6.3 | normalizations | tedious; must be checked against PGL(2) and SL(2) numerically |
| §7.2 | Theorem B (Route A = Route B) | main new content; rank one first, then rank two via PGL(3) |
| §8 | Theorem D | depends on the stabilization of the local trace formula; cite rather than reprove |
| §9.4 | SL(3) atoms | new computation; extends the PGL(3) code |

Suggested order:
1. §9.1–9.2, rank-one normalizations, done numerically.
2. §§4–5.
3. §7.2 in rank one.
4. §9.3–9.4, rank-two checks.
5. §6, measure theory.
6. §8.

## References (to be checked before use)

Already in the companion paper's bibliography: [Ar81], [Ar88], [Ar89] (= [Ar89a] here), [Ar91], [Ar93], [BDK86], [BP20], [Ka86], [Ke82], [OS13], [Re01], [Wa03], [Wa89a].

Additional:
- [Ar89b] J. Arthur, *Intertwining operators and residues I. Weighted characters*, J. Funct. Anal. 84 (1989), 19–84.
- [Ar94a] J. Arthur, *On the Fourier transforms of weighted orbital integrals*, J. reine angew. Math. 452 (1994), 163–217.
- [Ar94b] J. Arthur, *The trace Paley–Wiener theorem for Schwartz functions*, Contemp. Math. 177 (1994), 171–180.
- [Ar96] J. Arthur, *On local character relations*, Selecta Math. (N.S.) 2 (1996), 501–579.
- [Ar98] J. Arthur, *Canonical normalization of weighted characters and a transfer conjecture*, C. R. Math. Rep. Acad. Sci. Canada 20 (1998), 35–52 (some sources give pp. 33–52).
- [Ar99] J. Arthur, *On the transfer of distributions: weighted orbital integrals*, Duke Math. J. 99 (1999), 209–283.
- J. Arthur, *A stable trace formula* I–III (2002–2003); volumes and pages to be added.
- [La76] R. P. Langlands, *On the functional equations satisfied by Eisenstein series*, LNM 544 (1976): normalizing factors. To check.
- Z. Peng, *Multiplicity formula and stable trace formula*, arXiv:1608.00055.
- H. Li, *A local trace formula for p-adic infinitesimal symmetric spaces: the case of Guo–Jacquet*, arXiv:2105.00087.

# sl2bar-trace/revised

The 2026 revision of *A hitch-hiker's guide to the metaplectic trace formula for SL(2)*, restricted to the double cover (n = 2). It is written section by section, following the stages in [`../revision_log.md`](../revision_log.md).

| File | Contents |
|---|---|
| `sec2-foundations.tex` | Section 2 (stage 1): Kubota's cocycle, the splittings over N, K and K_m, the center, preimages of tori, NAK and heights, Weyl chambers, anti-genuine functions, measures, the adelic cover and its splitting over G(ℚ), and a double cover of GL(2) |
| `sec3-rank0.tex` | Section 3 (stage 2): covers of tori, genuine characters, Weil's character χ_ψ, the rank-0 trace formula (Poisson summation twisted by a genuine automorphic character), and the distributions I^A used in Section 6 |
| `sec4-geometric.tex` | Section 4 (stage 3): equivalence classes, kernels, the height inequality H(x) + H(γx) ≤ 0 and truncation with T₀ = 0, the coarse geometric expansion proved class by class (hyperbolic: weight 2T + v_A; elliptic; central: unipotent term via a zeta integral), the local distributions J_A(γ,f), J_A(z,f), and the fine expansion (Arthur, Li) |
| `sec5-spectral.tex` | Section 5 (stage 4): cuspidal data and the Weyl action on the cover of A (ramified classes = Weil characters χ_{ψ_b}), Eisenstein series, the intertwining operator and its normalizing factor L^S(2λ,χ²)/L^S(2λ+1,χ²), the residual spectrum (even Weil representations), kernels, truncation, Maass–Selberg, J_χ^T with M_B^T = 2T − M⁻¹M′, the ramified term ¼ tr(M(w,0)I), and the trace formula |
| `sec6-invariant.tex` | Section 6 (stage 5): non-invariance (u′_B = −H(ky), the variance of J_O, J_χ, J_A(γ) and of the weighted characters), normalized intertwining operators (explicit at unramified and real places) and the global factor m, the map φ_A and the invariant distributions I_A(γ,f) built by Fourier inversion on the abelian cover of A, the invariant trace formula with the m′/m term, and the ramified term (M(w,0) = −1, via Whittaker coefficients) |
| `preview.tex`, `.pdf` | Standalone build of the revised sections, with bibliography |
| `checks/sec2_n2_check.py` | Exact checks of the explicit n = 2 formulas in Section 2 |
| `checks/sec3_n2_check.py` | Checks of Section 3: the cocycle on A, and Weil indices from Gauss sums (local identity, odd-p closed form, product formula over ℚ) |
| `checks/sec4_n2_check.py` | Checks of Section 4 for k = ℚ: Iwasawa heights, the height inequality, the weight v_A and its local form, the weight integral, J_A(z,f) at ℝ and ℚ₃ with and without the correction term, and the unipotent constant term of Example 4.A |
| `checks/sec5_n2_check.py` | Checks of Section 5 for k = ℚ: the Weyl action on the cover of A and χ_ψ^w = χ_ψ, the unramified intertwining integral on the double cover at p = 3, 5, 7 (shell by shell), Arthur's limit for M_B^T (any d) and the 1995 normalization, the Maass–Selberg diagonal limit, the ramified cross term → F(0)/4, the residue of Example 5.B, and the local facts behind Prop. 5.16 |
| `checks/sec6_n2_check.py` | Checks of Section 6 for k = ℚ: the sign of the ramified term (Maass–Selberg on the Eisenstein series of SL(2,ℤ), by integration over the modular surface), u′_B, the variance of v_A and of J_A at ℝ, the conjugation identity for M⁻¹M′ in the principal series of SL(2,ℝ), the real K-type formulas and their normalization, the unramified Whittaker integral on the cover at p = 3, 5, 7, 11, and M(w,0) = −1 for b = ±1, ±2 from local residues |
| `checks/cover_lib.py` | Shared helpers from Section 6 on: the cocycles, the product in the cover, the Weil index and Weil's character, the spherical vector on w⁻¹n(y) (copied from `sec5_n2_check.py`) |
| `checks/padic_lib.py` | Shared helpers: p-adic valuations and the quadratic Hilbert symbol of rationals |

Build: `latexmk -pdf preview.tex`. Check: `python3 checks/sec2_n2_check.py`, …, `python3 checks/sec6_n2_check.py` (Sections 4 and 5 need SymPy, Section 6 needs mpmath and takes about 20 seconds), or `python3 run_checks.py` from the repository root.

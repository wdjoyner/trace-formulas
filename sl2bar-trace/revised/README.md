# sl2bar-trace/revised

The 2026 revision of *A hitch-hiker's guide to the metaplectic trace formula for SL(2)*, restricted to the double cover (n = 2). It is written section by section, following the stages in [`../revision_log.md`](../revision_log.md).

| File | Contents |
|---|---|
| `sec2-foundations.tex` | Section 2 (stage 1): Kubota's cocycle, the splittings over N, K and K_m, the center, preimages of tori, NAK and heights, Weyl chambers, anti-genuine functions, measures, the adelic cover and its splitting over G(ℚ), and a double cover of GL(2) |
| `sec3-rank0.tex` | Section 3 (stage 2): covers of tori, genuine characters, Weil's character χ_ψ, the rank-0 trace formula (Poisson summation twisted by a genuine automorphic character), and the distributions I^A used in Section 6 |
| `sec4-geometric.tex` | Section 4 (stage 3): equivalence classes, kernels, the height inequality H(x) + H(γx) ≤ 0 and truncation with T₀ = 0, the coarse geometric expansion proved class by class (hyperbolic: weight 2T + v_A; elliptic; central: unipotent term via a zeta integral), the local distributions J_A(γ,f), J_A(z,f), and the fine expansion (Arthur, Li) |
| `preview.tex`, `.pdf` | Standalone build of the revised sections, with bibliography |
| `checks/sec2_n2_check.py` | Exact checks of the explicit n = 2 formulas in Section 2 |
| `checks/sec3_n2_check.py` | Checks of Section 3: the cocycle on A, and Weil indices from Gauss sums (local identity, odd-p closed form, product formula over ℚ) |
| `checks/sec4_n2_check.py` | Checks of Section 4 for k = ℚ: Iwasawa heights, the height inequality, the weight v_A and its local form, the weight integral, J_A(z,f) at ℝ and ℚ₃ with and without the correction term, and the unipotent constant term of Example 4.A |
| `checks/padic_lib.py` | Shared helpers: p-adic valuations and the quadratic Hilbert symbol of rationals |

Build: `latexmk -pdf preview.tex`. Check: `python3 checks/sec2_n2_check.py`, `python3 checks/sec3_n2_check.py` and `python3 checks/sec4_n2_check.py` (need SymPy), or `python3 run_checks.py` from the repository root.

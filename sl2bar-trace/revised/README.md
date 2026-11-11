# sl2bar-trace/revised

The 2026 revision of *A hitch-hiker's guide to the metaplectic trace formula for SL(2)*, restricted to the double cover (n = 2). It is written section by section, following the stages in [`../revision_log.md`](../revision_log.md).

| File | Contents |
|---|---|
| `sec2-foundations.tex` | Section 2: Kubota's cocycle, the splittings over N, K and K_m, the center, preimages of tori, NAK and heights, Weyl chambers, anti-genuine functions, measures, the adelic cover and its splitting over G(ℚ), and a double cover of GL(2) (stage 1) |
| `stage1-preview.tex`, `.pdf` | Standalone build of Section 2 with its bibliography |
| `checks/sec2_n2_check.py` | Exact checks of every explicit n = 2 formula in Section 2 (Hilbert symbols over ℝ, ℚ₂, ℚ₃, ℚ₅, ℚ₇; random rational elements; fixed seed) |

Build: `latexmk -pdf stage1-preview.tex`. Check: `python3 checks/sec2_n2_check.py` (needs SymPy), or `python3 run_checks.py` from the repository root.

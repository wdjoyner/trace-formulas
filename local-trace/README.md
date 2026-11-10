# local-trace

*Simple local trace formulas for unramified p-adic groups*, by David Joyner.

- Published: Pacific J. Math. **154** (1992), no. 1, 103–129.
- Corrected and extended version: October 1997 (`original-1997/`).
- 2026 revision: in progress (`paper/`).

For G unramified over a p-adic field F, K hyperspecial, f spherical and γ regular elliptic, the paper seeks a spectral expansion of the elliptic orbital integral

    ∫ f(g⁻¹γg) dg  =  ∫ f^∨(χ) I(χ,γ) dμ(χ),

where f^∨ is the Satake transform and dμ the spherical Plancherel measure. The method is Waldspurger's (GL(N), Astérisque 171–172, 1989): truncation, Casselman asymptotics, Macdonald's formula, and an Arthur–Langlands combinatorial lemma.

## Layout

| Path | Contents |
|---|---|
| `original-1997/local-trace-formula-1997-scan.pdf` | The 1997 version as received (35 pp.) |
| `original-1997/local-trace-formula-transcription.tex` / `.pdf` | Literal LaTeX transcription — errors and typos reproduced as printed |
| `original-1997/transcription_log.md` | Errata log: every typo, error and gap, with location and suggested fix |
| `original-1997/referee_report_ltf.tex` / `.pdf` | Referee report (2026) |
| `examples/pgl2/` | PGL(2) worked example + verification script |
| `paper/` | Revised paper (planned) |
| `arthur/` | Route B: the identity from Arthur's local trace formula (planned) |

## Plan for the revision ("Route A")

Repair the original argument rather than replace it:

1. Fix the normalizations and misquoted inputs (errata log §§2–3, 8).
2. Replace Lemma 3.5 by the vertex (Brion) decomposition.
3. Restate Prop. 3.6 as "cone terms + T-independent remainder", for vectors of fixed level.
4. Prove Theorem 4.5 by the exact-vanishing argument of the PGL(2) example.
5. Prove the regularity of I(χ,φ)·dμ in rank ≥ 2 via (G,A)~-families (the main new step; PGL(3) numerical check first).
6. Update §5 (the fundamental lemma is now a theorem).
7. Add a glossary, a literature review (before and after 1997), the PGL(2) example, and a short section on Route B.

# local-trace

*Simple local trace formulas for unramified p-adic groups*, by David Joyner.

- Published: Pacific J. Math. **154** (1992), no. 1, 103–129.
- Corrected and extended version: October 1997 (`original-1997/`).
- 2026 revision: `paper/` (first complete draft, November 2026).

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
| `examples/sl2/` | SL(2) check: the atom at the quadratic unramified character |
| `examples/rank2/` | Exact rank-two check of the Brion vertex decomposition (SL(3), PGL(3)) |
| `examples/pgl3/` | PGL(3) on the Bruhat–Tits building: rank-two test of Hypothesis (R) (Appendix A of the paper) |
| `paper/` | Revised paper (2026, Draft 2), `CHANGES.md` (Draft 1), second referee report and response |
| `revision_log.md` | Revision log: drafts, AI usage, original vs. new results, concordance, former Appendix C of the paper |
| `arthur/` | Route B: companion paper `route-b-draft.tex` (Draft 3, a working draft) with its own `revision_log.md`; a sketch is §7 of the revised paper |

## Plan for the revision ("Route A") and its status

Repair the original argument rather than replace it:

1. Fix the normalizations and misquoted inputs (errata log §§2–3, 8). **Done.**
2. Replace Lemma 3.5 by the vertex (Brion) decomposition. **Done** (Lemma 3.5A).
3. Restate Prop. 3.6 as "cone terms + T-independent remainder", for vectors of fixed level. **Done**, with a new direct proof.
4. Prove Theorem 4.5. **Done** under Hypothesis (R): rapid decay of the oscillatory terms (exact vanishing in rank one).
5. Regularity in rank ≥ 2. **Partly done.** (R) is false in general: SL(2) has an atom (Conjecture 4.6). It also fails for PGL(3), where nevertheless there is no singular part (Appendix A). The weaker (R′) (Remark 2026.20) is proposed. Open: a proof of (R′).
6. Update §5 (the fundamental lemma is now a theorem). **Done.**
7. Add a glossary, a literature review (before and after 1997), the PGL(2) example, and a short section on Route B. **Done**, plus an SL(2) example.

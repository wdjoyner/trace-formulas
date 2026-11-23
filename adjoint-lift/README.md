# Adjoint lift: twisted orbital integrals for PGL(3)

**David Joyner, “On twisted orbital integral identities for PGL(3) over a p-adic field.”**  
*Canadian Journal of Mathematics* **42** (1990), no. 6, 1098–1130.  
[Published article (DOI)](https://doi.org/10.4153/CJM-1990-059-6)

## Summary

This paper studies local **twisted orbital-integral identities** arising in the **symmetric-square (adjoint) lift** from representations of `GL(2)` to `GL(3)`, formulated via a twisted trace formula for `PGL(3)` over a nonarchimedean local field `F`. It compares twisted orbital integrals on `PGL(3,F)` with orbital integrals on the related groups `SL(2,F)` and `PGL(2,F)`, using the norm maps and matching elements of spherical Hecke algebras.

The paper follows a geometric route to the **unit-element cases of the fundamental lemmas**:

1. **Section 1 — Framework.** Describes the adjoint lift, the Jacquet–Shalika norm maps, twisted conjugacy, stable and unstable (`κ`-weighted) orbital integrals, and the fundamental identities to be proved.
2. **Section 2 — Split case.** Uses Satake transforms and character calculations to treat the split orbital-integral identities.
3. **Section 3 — Nonsplit reduction.** Translates the remaining identities into counting problems involving fixed points and lattice classes in Bruhat–Tits buildings.
4. **Section 4 — The `SL(2)` side.** Presents Langlands' geometric counting argument for the unit Hecke function.
5. **Section 5 — The `PGL(2)` side.** Completes the second building-counting calculation for the unit Hecke function, supplying the contribution identified as original by the author.

The principal nonsplit building arguments assume **odd residue characteristic** (`p ≠ 2`). As explained in the paper, much of the method is due to R. Langlands; Section 5 is the author's original contribution.

## Files

- [`adjoint_lift_combined.tex`](adjoint_lift_combined.tex) — a single, compilable LaTeX transcription assembled from `adjoint_lift0.tex` through `adjoint_lift5.tex`, with the ancillary `adjoint_lift_pics.tex` source preserved after `\\end{document}` to avoid duplicating figures. The mathematical text was not revised during assembly.
- [`adjoint_lift_referee_report.tex`](adjoint_lift_referee_report.tex) — independent mathematical and readability review dated 23 November 2026, with specific issues, evidence, and proposed editorial corrections.

The source is an archival transcription of a previously published paper, **not a newly corrected proof**. In particular, the referee report identifies mathematical statements and normalizations needing verification; it does not assert that the underlying published orbital-integral identity is false. The report is a targeted audit, not a full independent check of every geometric counting argument.

## Compiling with pdfLaTeX

From this directory, with a modern TeX distribution (including `newtxtext` and `newtxmath`):

```sh
pdflatex -interaction=nonstopmode adjoint_lift_combined.tex
pdflatex -interaction=nonstopmode adjoint_lift_combined.tex

pdflatex -interaction=nonstopmode adjoint_lift_referee_report.tex
pdflatex -interaction=nonstopmode adjoint_lift_referee_report.tex
```

Both documents use **12-point Times-style fonts** and **US letter paper**. The combined article produces approximately 40 pages; the report approximately 8 pages.

## Editorial note

The supplied manuscript is the author's 2003 LaTeX transcription of the 1990 publication, with historical attributions retained. For any corrected edition, distinguish (a) differences introduced by transcription from (b) issues already present in the published article, and record corrections in a separately labeled errata document rather than silently modifying this historical source.

# Draft 6 revision notes — Direct comparison of SL(2) with its metaplectic cover

**Source:** Draft 5 `direct-comparison-SL2.tex` and Carbon's referee report supplied
November 23, 2026.

## Mathematical corrections made

1. **Local `GL(2)` cocycle (§2.1):** removed the exceptional rule
   `v(z,g)=1` at the real place. The expression with `(z,d)_2` when `c=0`
   now applies uniformly, and the obstruction in the old definition is explained.
2. **Global splitting (§2.2):** distinguished the restricted-product local
   coordinates, in which rational points have the diagonal representatives
   `((gamma,1))_v`, from the modified-cocycle model, in which the splitting is
   `(gamma,s_A(gamma)^{-1})`.
3. **Genuineness:** consistently wrote `zeta` for the central character
   (since `zeta=zeta^{-1}` on `mu_2`); renamed the Weil character genuine
   rather than anti-genuine.
4. **Weyl integration (§4.3.3):** retained the full `|D(t)|` normalization
   in `Phi_f = |D| O_f` (consistent with the displayed Weyl integration
   formula), and distinguished it from `F_f=|D|^{1/2} O_f`.
5. **Weil representation (§4.7):** proved that the parity-dependent Fourier
   formula is the restriction of the Weil representation; corrected the real
   Fresnel phase to depend on `sgn(qa)`; eliminated the wrong constant
   phases and extraneous normalization factors in the claimed
   kernel-trace formula. Replaced the previous unverified real/p-adic
   corollaries with precisely conditional statements.
6. **Global theorem (§5.3):** inserted a self-contained explanation that
   `L(s,Ad(Pi))` is holomorphic at `s=1` even for dihedral `Pi`, using the
   simple pole of `L(s,Pi × Pi^∨)` and of `zeta_k(s)`.

## Exposition and typography

- Clarified the torus-character lemma, Satake target, unipotent splitting,
  and Gelbart's second discrete-series parameterization.
- Replaced "five" p-adic correspondences with "several" pending a
  complete enumeration.
- Fixed an `M_1` variable in Appendix B, clarified Arthur's terminology,
  and distinguished the `GL(2)` cocycle `beta_1` in Appendix A.
- Fixed reported LaTeX typos, improved angle-bracket and sum delimiters,
  modernized underlined bibliography typography, and alphabetized
  the late-added entries.
- Verified Arthur's *Annals* 114 (1981), 1–74; Langlands,
  *Annals of Mathematics Studies* 96 (1980); Waldspurger,
  *Forum Math.* 3 (1991), 219–307.
- **Disagreed with Carbon's proposed Li citation:** the author's own
  publication list gives *Astérisque* **464** (2026), not
  *J. Reine Angew. Math.* **801** (2023). Updated `[Li3]` accordingly.
  See https://www.wwli.asia/docs/publications/ .

## Intentionally left conditional / unverified

The formal diagonal-kernel character calculation still depends on a
principal-value conjecture. The real phase formula does not, on its
own, establish equality with Adams's character normalization. The
precise normalization of the Waldspurger unramified correspondence
and the original source-dependent local Weil identifications merit
independent checking by a specialist. Carbon's confidence in the
pole-counting theorem is reassuring, but it is not an independent
formal verification of the full paper.

## Build test

`pdflatex -interaction=nonstopmode -halt-on-error direct-comparison-SL2_draft6.tex`

Compiled successfully with 12-point Times-like fonts and US letter paper.
Cross-references resolved on repeated runs. Result: 81 pages.

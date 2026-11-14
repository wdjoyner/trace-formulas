# Changelog for `g2-shalika-germs-2026.tex`

**Manuscript:** D. Joyner, *"On the transfer of Shalika germs for $G_2$"*  
**Repository Directory:** `g2stuff/` in `wdjoyner/trace-formulas`  
**Current Revision:** Draft 3 (November 14, 2026)  
**Prepared by:** Gemini ("Carbon") for Drafts 2–3; Claude for Draft 1 and for the check of Draft 3 recorded in `../revision_log.md`.

This document records the mathematical corrections, closed-form derivations, structural additions, and typesetting updates made across the 2026 revisions (Drafts 1, 2, and 3) relative to the summer 1994 AMS-TeX sources (`g2new0.tex`–`g2new9.tex`, variants `g2new5d.tex` and `g2new9d.tex`, and `g2newapp.tex`).

## Overview of Revision Passes

| Revision Stage | Date | Summary of Scope |
| :--- | :--- | :--- |
| **Draft 1** | Nov 2026 | Transcription of 1994 AMS-TeX to `amsart` 12pt; proof of toric normality, Cohen–Macaulayness, and codimension-one patch regularity of $Z$ (Propositions 3.4A, 3.7); Table 4.3A of Igusa constants; diagnosis of why Hales's center-descent reduction lemma fails for $G_2$; biquadratic transfer factor $\Delta_0(Y)$ (Proposition 7.6); complete Smith-normal-form table of elliptic tori (Table A.6); literature review, summary, and glossary. |
| **Draft 2** | Nov 14, 2026 | Second referee pass: repaired misidentified base vs. fiber coordinates in §§5, 7, 8 via Kirillov–Kostant symplectic Pfaffians and rational Leray fiber forms ($X$-degrees $+2$ and $+3$); corrected subregular representative in §6; fixed endoscopic torus embeddings (A.13)–(A.13') in §A.3; proved Lemma 4.4 orbit images, subregular Dynkin curve line types (§2), dual cone $f$-vector `(1,11,43,82,84,46,12,1)`, and $H^1(F,S_3)$ subregular class counts; ensured portable `pdflatex` and `lualatex` compilation without `enumitem`. |
| **Draft 3** | Nov 14, 2026 | Third pass: computed exact all-order Lemma 1.21 polynomials `(1.21a)`, exact star gallery identities `(1.21b)`, and exact constants $(c_1,\dots,c_7)=(-1,2,3,-3,-3,1,3)$ in `(1.22)` (resolving the 8-vs.-7 coordinate count of Remark 2026.8); computed exact Chevalley commutators, parabolic conjugations `(2.11)` and `(2.13)`, Galois actions `(2.12)` and `(2.14)` (with $n_0=1$ identically), Weyl conjugations `(2.16)`–`(2.17)`, and special-fiber Galois involutions (Proposition 2.14A), proving $D_6$-Galois invariance of both Leray fiber volume forms `(7.4)` and `(8.5)`. |

## Draft 3 Changes (Exact Coordinate, Star Gallery & Galois Computations)

All computations in Draft 3 use the fixed positive root ordering $\Sigma_G^+ = (\alpha,\beta,\gamma,\delta,\epsilon,\zeta)$ ($\alpha$ short, $\beta$ long) and the explicit $8\times 8$ triality Chevalley basis $\{h_\alpha,h_\beta,X_{\pm\rho}\} \subset \mathfrak{so}(8)$ of §A.4 with $X_{-\rho} = {}^t X_\rho$.

1. **Section 1 — Exact All-Order Expansion of Lemma 1.21 (`Eq. (1.21a)`):**
   - Added display `(1.21a)` giving the exact factored polynomials for $x(\alpha), x(\beta), x(\gamma), x(\delta), x(\epsilon), x(\zeta)$ in $t_0^{n_-} = t_0 \prod_{\rho\in\Sigma_G^+}\theta_\rho(x(\rho))$ for $n_- = \prod_{\rho\in\Sigma_G^+}\theta_\rho(n_\rho)$.
2. **Section 1 — Exact Star Gallery Relations (`Eq. (1.21b)`) and Resolution of Remark 2026.8 (`rem:1.22`):**
   - Derived from $B_-^{w_+ n_-} = B_-^{n_W} \Longleftrightarrow w_+ n_- n_W^{-1} \in B_-$ along the gallery $W_0,\, W_1 = s_\beta W_0,\, W_2 = s_\beta s_\alpha W_0$ (with wall $\rho_2 = s_\beta^{-1}\alpha = \gamma$ of simple-root type $\alpha$, denoted $z(\sigma_\beta^{-1}W_0,\alpha)$ in 1994):
     $$n_\alpha = \frac{1}{z(W_0,\alpha)}, \qquad n_\beta = \frac{1}{z(W_0,\beta)}, \qquad n_\gamma = \frac{1}{z(W_0,\beta)\,z(s_\beta W_0,\gamma)}.$$
   - Recorded in Remark 2026.8 the remaining three triangular gallery equations relating $n_\delta, n_\epsilon, n_\zeta$ to the gallery wall coordinates $(b_1,a_2,b_3,a_4,b_5)$.
   - **Resolved the $8$-versus-$7$ coordinate count on $Y_1(B_+,B_-)$:** Because $n_\gamma$ is algebraically determined by $z(W_0,\beta)$ and $z(s_\beta W_0,\gamma)$, eliminating $n_\gamma$ leaves the $6$ independent birational coordinates $(z(W_0,\alpha),z(W_0,\beta),z(s_\beta W_0,\gamma),n_\delta,n_\epsilon,n_\zeta)$ on $S(B_+,B_-)$, giving $6 + 1 = 7$ independent coordinates with $\lambda$ on the $7$-dimensional variety $Y_1(B_+,B_-)$.
3. **Section 1 — Exact Constants in `Eq. (1.22)` and $\lambda \to 0$ Limits of $w(\rho)$:**
   - Replaced undetermined constants $c_1,\dots,c_7$ in `(1.22)` and $w(\gamma), w(\delta), w(\epsilon), w(\zeta)$ with their exact values $(c_1,c_2,c_3,c_4,c_5,c_6,c_7) = (-1, 2, 3, -3, -3, 1, 3)$ (compare [Hales 1989](https://www.numdam.org/article/AST_1989__171-172__195_0.pdf), §7, Lemmas 7.13–7.15, and [Hales 1992a](https://iacobus.usc.gal/nde/fulldisplay/alma991013513907807712/34CISUG_USC:NDE/gl), Ch. II).
   - Removed the spurious factor $z(\sigma_\beta^{-1}W_0,\alpha)$ from the denominator of the $c_1$-term in 1994's display of $x(\gamma)$ (since $n_\alpha n_\beta = (z(W_0,\alpha)z(W_0,\beta))^{-1}$), restoring the exact $\lambda = 0$ limit $w(\gamma)|_{\lambda=0} = \frac{\gamma(X)}{\alpha(X)\beta(X)}\frac{z(W_0,\alpha)}{z(s_\beta W_0,\gamma)} - \frac{1}{\beta(X)}$.
4. **Section 2 — Exact Chevalley Commutators and Parabolic Conjugations (`Eqs. (2.11)` & `(2.13)`):**
   - Replaced all schematic structure constants (`c_1..c_4`, `d_1..d_3`, `e`, `c`, `d`) and omitted reordering ellipses in `(2.11)` and `(2.13)` with exact closed-form expressions.
   - Clarified that in `(2.11)`, $t = \alpha^\vee(1 + x(\alpha)z)$ already stands on the left of the ordered product and therefore does not rescale $\phi_\rho^\alpha$ for $\rho \neq \alpha$, whereas in `(2.13)` moving $t = \beta^\vee(u_\beta)$ ($u_\beta = 1 + x(\beta)z$) past $\theta_\alpha(x(\alpha))$ rescales $x(\alpha) \mapsto u_\beta x(\alpha)$.
   - Corrected the Baker–Campbell–Hausdorff coefficients in $\theta_\gamma(x)^{\theta_{-\beta}(z)} = \exp(x X_\gamma - xz X_\alpha) = \theta_\alpha(-xz)\theta_\gamma(x)\theta_\delta(x^2 z)\theta_\epsilon(x^3 z^2)\theta_\zeta(-2x^3 z)$ (replacing the 1994 schematic coefficients $2czx^2, 3c^2 z^2 x^3, 3czx^3$).
5. **Section 2 — Exact Galois Actions (`Eqs. (2.12)` & `(2.14)`) and Cancellation $n_0 = 1$ in `(2.9)`:**
   - Proved that for $c_{\sigma_\rho} = 1$ and $z_{\sigma_\rho} = \sigma_\rho(z(W_0,\rho))$, conjugating $\sigma_\rho(b)$ by $m_{\sigma_\rho} = \theta_{-\rho}(z_{\sigma_\rho})$ cancels the lower-triangular factor $n_0 \in N_+$ identically ($n_0 = 1$ in `(2.9)`) and restores the torus component $\sigma_\rho(t_0)\rho^\vee(\rho(t_0)) = t_0$.
   - Corrected `(2.12)` and `(2.14)` so $\sigma_\rho$ is not applied a second time to $z_{\sigma_\rho}$: $\sigma_\rho : x(\tau) \mapsto \phi_\tau^\rho(\sigma_\rho(\underline{x}), -z_{\sigma_\rho}) = \sigma_\rho(\phi_\tau^\rho(\underline{x}, -z(W_0,\rho)))$.
6. **Section 2 — Special-Fiber Galois Involutions and Leray Measure Invariance (`Proposition 2.14A`):**
   - Added **Proposition 2.14A** giving the $\lambda \to 0$ birational Galois involutions on $(z(\alpha),z(\beta),w(\gamma),w(\delta),w(\epsilon),w(\zeta))$ with denominators $D_\alpha = 1 + 3\alpha(X)\sigma(w(\gamma)) - 3\alpha(X)^2\sigma(w(\delta)) + \alpha(X)^3\sigma(w(\epsilon))$ and $D_\beta = 1 - \beta(X)\sigma(w(\gamma))$ (the $G_2$ analogue of [Hales 1989](https://www.numdam.org/article/AST_1989__171-172__195_0.pdf), Eq. (5.10), p. 225).
   - Verified that their Jacobians satisfy $\det J = D_\rho^{-4}$ on $E_{\emptyset,\alpha,\delta}$ and $\det J = D_\alpha^{-6}, D_\beta^{-11}$ on $E_{\emptyset,\beta,\zeta}$, proving exact $D_6$-Galois invariance of both rational Leray fiber volume forms `(7.4)` and `(8.5)`.
7. **Section 2 — Exact Weyl Conjugations (`Eqs. (2.16)` & `(2.17)`):**
   - Computed all Carter signs $\eta_{\rho,\tau}$ and all quadratic/cubic reordering terms in `(2.16)` and `(2.17)` explicitly.
8. **Section 0, Section 7 (`Remark 2026.23` / `rem:7.status`), Summary, and Acknowledgments:**
   - Updated Remark 2026.36 (`rem:7.status`) to reflect that algebraic inputs `(i)` (`(1.22)`) and `(iii)` (§2 Galois action) are now proved in closed form, leaving only `(ii)` (the explicit cocycle $t_*$ from [Hales 1992a](https://iacobus.usc.gal/nde/fulldisplay/alma991013513907807712/34CISUG_USC:NDE/gl), Ch. I, Cor. 5.4 and 5.7; cf. [Hales 1994](https://publicationsthomashales.wordpress.com/wp-content/uploads/2016/03/twisted-endoscopy-gl4-gl5.pdf)) and evaluation of the principal value integral $J(X)$.

## Draft 2 Changes (Differential Forms, Subregular Orbit, Torus Maps & Cone Faces)

1. **Sections 5, 7, and 8 — Kirillov–Kostant Base Forms and Rational Leray Fiber Forms (`Eqs. (5.15)`–`(5.16)`, `(7.3)`–`(7.4)`, `(8.1)`, `(8.4)`–`(8.5)`):**
   - Replaced the 1994 limit formulas for $\omega_{\mathcal{O}_2}$ and $\omega_{\mathcal{O}_3}$, which confused fiber coordinates in $\ker(d\pi|_E)$ with unipotent orbit coordinates and introduced non-rational fractional powers $|x(\delta)|^{1/2}|w(\delta)|^{-3/2}|z(\beta)|^{-3/2}$.
   - On $E_{\emptyset,\alpha,\delta}$ ($\mathcal{O}_2 = \tilde{A}_1$, $\dim \mathcal{O}_2 = 8$), proved via the Kirillov–Kostant symplectic Pfaffian that $|\pi^*\omega_{\mathcal{O}_2}| = |x(\delta)|\,dx(\delta)\,dx(\epsilon)\,dx(\zeta)\,dv(\alpha)\,dv(\gamma)\,dv(\delta)\,dv(\epsilon)\,dv(\zeta)$ and derived the rational Leray fiber $4$-form
     $$|\omega_{E_{\emptyset,\alpha,\delta}(u)}| = \frac{1}{|w(\delta)|^2|z(\beta)|^2}\,dz(\beta)\,dw(\gamma)\,dw(\delta)\,dv(\beta),$$
     which has exact homogeneity degree $+2$ under $X \mapsto cX$ (matching [Hales 1989](https://www.numdam.org/article/AST_1989__171-172__195_0.pdf), §6, pp. 239–243).
   - On $E_{\emptyset,\beta,\zeta}$ ($\mathcal{O}_3 = A_1$, $\dim \mathcal{O}_3 = 6$), proved using $[X_{-\alpha}, X_\zeta] = 0$ and the symplectic Pfaffian that $|\pi^*\omega_{\mathcal{O}_3}| = |x(\zeta)|^2\,dx(\zeta)\,dv(\beta)\,dv(\gamma)\,dv(\delta)\,dv(\epsilon)\,dv(\zeta)$ and derived the rational Leray fiber $6$-form
     $$|\omega_{E_{\emptyset,\beta,\zeta}(u)}| = \frac{1}{|w(\zeta)|^3|z(\alpha)|^2}\,dz(\alpha)\,dw(\gamma)\,dw(\delta)\,dw(\epsilon)\,dw(\zeta)\,dv(\alpha),$$
     which has exact homogeneity degree $+3$ under $X \mapsto cX$ (fixing the wrong $|c|^1$ scaling of the 1994 display), and restored the sign $-$ in `(8.1)`.
   - Updated `(5.15)` and `(5.16)` in the sketch of Lemma 5.14 to match `(7.4)` and `(8.5)`, and proved in Remark `rem:5.14` that the $X$-homogeneity degrees $+2$ and $+3$ now hold unconditionally.
2. **Section 6 — Subregular Unipotent Representative:**
   - Replaced $u = \exp(X_\alpha + X_{\alpha+\beta})$ (which lies in $\tilde{A}_1$ of dimension $8$) with $u = \exp(X_\beta + X_{2\alpha+\beta})$ (which lies in the $1$-regular subregular class $G_2(a_1)$ of dimension $10$, consistent with §A.7).
3. **Appendix A.3 & A.4 — Endoscopic Torus Embeddings (`(A.13)`–`(A.13')`) and Chevalley Conventions:**
   - Replaced the 1994 maps `(A.13)`, `(A.13')`, and `(A.13'')` (which pulled back to long roots for $\mathrm{PGL}(3)$ and non-root characters $2\delta, 2\gamma, 2\zeta$ for $A_1\times A_1$) with `(A.13)` $t \mapsto \mathrm{diag}(a_1,a_2,1) \bmod \mathbb{G}_m$ on $H_1 = \mathrm{PGL}(3)$ (pulling back to the short roots $\{\alpha,\gamma,\delta\}$) and `(A.13')` on $H_2 = (\mathrm{SL}(2)\times\mathrm{SL}(2))/\{\pm 1\}$ via $u^2 = a_3 = \alpha$, $v^2 = a_1 a_2 = \zeta$, $uv = a_1 = \delta$, $vu^{-1} = a_2 = \gamma$, documented in Remark `rem:A3`.
   - Added explicit specification $X_{-\sigma} := {}^t X_\sigma$ in §A.4 and drew the missing connecting edges in the two $D_4$ Dynkin diagrams of §§A.1 and A.3.
4. **Sections 0, 2, 3, 4, 5, 9, and Appendix A.7 — Proofs of Open Remarks & Combinatorial Counts:**
   - Defined **endoscopically Richardson** unipotent classes explicitly in §0 and §9 (`Conjecture 9.1`).
   - Verified Figure 1 (`rem:dynkin`) across all Bruhat cells of $G_2/P_\alpha$ and $G_2/P_\beta$, finding 1 short-root line $\ell_\alpha$ and 3 long-root lines $\ell_\beta',\ell_\beta'',\ell_\beta'''$ at $t_0 \in \{0,\pm\sqrt{3}\}$.
   - Consulted [Hales 1989](https://www.numdam.org/article/AST_1989__171-172__195_0.pdf) directly: noted in Remark `rem:3.4` that Lemma 4.2 of [Hales 1989](https://www.numdam.org/article/AST_1989__171-172__195_0.pdf) (pp. 212–217) proves Conjecture 3.4 for $\mathrm{Sp}(2n)$ of arbitrary rank, and cited §2 (Props. 2.4(1), 2.11, 2.14, pp. 199–204) directly in Remark `rem:main-gap`.
   - Restored the missing minus sign on $\omega_{Z,U}$ for $Z_{\emptyset,\alpha,\gamma}$ in §4, proved $\pi(E_{\emptyset,\alpha,\delta}) = \overline{\tilde{A}_1}$ and $\pi(E_{\emptyset,\beta,\zeta}) = \overline{A_1}$ in Lemma 4.4, and corrected the face counts of $\sigma = \mathrm{cone}(S)^\vee$ in Remark `rem:exceptional` from `(262, 32)` to `268` faces of $\dim \ge 2$ (`f = (1,11,43,82,84,46,12,1)`) with `38` singular faces.
   - Justified Ranga Rao's theorem for the odd grading of $h_{\alpha+\beta}$ in §A.7 (`rem:A7`) via weight-$1$ cocharacters $\beta^\vee$ and $\zeta^\vee$, and proved via tame generators of $\Gal(\overline{F}/F)$ that $H^1(F,S_3)$ has $8$ classes for $q\equiv 1\pmod 3$ and $6$ classes for $q\equiv 2\pmod 3$.
5. **Preamble & Portability Cleanup:**
   - Replaced `enumitem` with standard `enumerate.sty` + native list specifications, added `\texorpdfstring` to all section headings with math, consolidated `\author{David Joyner}` with AI assistance documented in `\thanks`, abstract, and Acknowledgments, and removed internal `(level 1/2/3)` working tags from the manuscript body.

## Draft 1 Baseline Changes from the 1994 Sources

1. **Section 0 & Section 5 (Main Strategy & Reduction Lemma):** Identified that Reduction Lemma 5.19 ([Ha92b], Lemma 6.1, as quoted in 1994; the 1994 cross-reference to [Hales 1989](https://www.numdam.org/article/AST_1989__171-172__195_0.pdf), Prop. 2.11, is to a different statement) fails for $H_1 = \mathrm{PGL}(3)$ and $H_2 = (\mathrm{SL}(2)\times\mathrm{SL}(2))/\{\pm 1\}$ since $\Lie Z(H) = 0$; removed impossible compact-support test-function decompositions; reformulated Conjecture 0.0, Conjecture 0.0A, Lemma 0.8, Lemma 5.14, and Theorems 6.1, 7.2, 8.3 with explicit hypotheses $(\mathrm{X}_r)$ and cited Waldspurger (1997), Ngô (2010), and [Gordon & Hales 2016](https://muse.jhu.edu/article/609681/summary) (`Corollary 8.8`).
2. **Sections 1–2:** Fixed $\phi: X_0 \to T_G$ in Definition 1.3 (`rem:phi`); corrected wall-chamber pair and sign conventions in `(1.8)`–`(1.10)` and `(1.18)`; replaced "image of $S_0$" in Definition 1.16 with $z_1(W,\rho)\neq 0$ (`rem:Spp`); fixed $g^{-1}\sigma(g)\in N_G(T_G)$ and $\Gal(E/F)$ in §2 (`rem:2.cocycle`) and corrected `(2.6)`, `(2.8)`, `(2.9)` (`rem:2.8`).
3. **Sections 3–4:** Corrected $w(\zeta)$ on $x(\beta)\neq 0$ and $x(\gamma)\neq 0$ and removed redundant fifth patch (`rem:3.patches`); fixed $E_\Delta$ vs. $E_\emptyset$ (`rem:3.regular-branch`); corrected $\Sigma_{\Delta-S_1}^+$ in Lemma 3.5 (`rem:3.5`) and $\rho\ge\sigma$ plus comparability in Lemma 3.6 (`rem:3.6`); proved Proposition 3.4A and Proposition 3.7 ($Z$ normal and Cohen–Macaulay) and withdrew the 1994 complete-intersection claim (`rem:3.7`); corrected $\omega_{Z,U}$ denominators and $b(E_{\emptyset,\alpha,\epsilon}) = 11$ ($\beta = 11/3$) in §4 (`rem:4.forms`) and added Table 4.3A.
4. **Sections 7–8 & Appendix A:** Added Proposition 7.6A, Example 7.6B, and Corollary 7.6C (numbered 7.6, 7.7, 7.8 in Draft 1) computing the biquadratic transfer factor $\Delta_0(Y) = c'(P(Y),d_\alpha)_F$; corrected $|\lambda|^3$ in `(8.6)` and $\Sigma_{H_1}^+ = \{\alpha,\gamma,\delta\}$ (short roots) in §8 (`rem:8.roots`); fixed Cayley cross product $k\times j = -i$ and norm trace form in §A.2 (`rem:A2`), $X_{\alpha+\beta}$ sign note in §A.4, root/weight lattice derivations in §A.5 (`rem:A5`), Weyl matrices and all 7 elliptic torus classes in §A.6 (`Table A.6`, `rem:A6`).

## Companion SymPy Verification Suite (`g2stuff/scripts/`)

| Script File | Dependencies | Verified Manuscript Results |
| :--- | :--- | :--- |
| `verify_g2_chevalley_and_endoscopy.py` | `sympy` | Root/coroot lattices, Weyl subgroups & Table A.6 SNF; §A.4 Chevalley basis over $\mathbb{Z}$; §A.3 torus embeddings `(A.13)`–`(A.13')`; orbit dimensions & $\mathfrak{sl}_2$-triples; Bruhat-cell proof of Figure 1 Dynkin curve; §7 Legendre symbols ($5 \le p \le 23$). |
| `verify_g2_toric_and_forms.py` | `sympy`, `numpy`, `scipy` | Cone facets, §3–§4 regular patches (`Prop. 3.4A`), Igusa constants (`Table 4.3A`); LP enumeration of dual cone $\sigma$ $f$-vector `(1,11,43,82,84,46,12,1)` (`268` faces of $\dim\ge 2$, `38` singular, `5` minimal); `Lemma 4.4` orbit ranks; Kirillov–Kostant Pfaffians & Leray fiber forms `(7.3)`–`(7.4)` and `(8.4)`–`(8.5)`. |
| `verify_g2_coordinates_and_galois.py` | `sympy` | Exact all-order Lemma 1.21 (`(1.21a)`), gallery relations (`(1.21b)` & `Remark 2026.8`), constants in `(1.22)` & $w(\rho)|_{\lambda=0}$; exact $8\times 8$ rational-matrix verification of `(2.11)`–`(2.14)` ($n_0=1$) and `(2.16)`–`(2.17)`; `Proposition 2.14A` involutions & pullback invariance of `(7.4)` and `(8.5)`. |

## Small edits made by Claude when committing Draft 3 (Nov 14, 2026)

- §5, source of Lemma 5.19: noted that [Hales 1989, Prop. 2.11] is a quasi-split reduction to the centralizer of a semisimple element, not the reduction lemma.
- Open problems: added item (8), whether Hales' product case [Hales 1989, Prop. 2.14] gives a route to (X₁), (X₂) for H₂.
- Acknowledgments: restored the sentence "AI review is not an independent certification…" required by the style guide.
- Scripts: corrected remark and result numbers in the docstrings of the three `verify_*.py` files; fixed the face count in `g2_exceptional_divisors.py` (it skipped faces with more than 7 rays and σ itself; it now gives 268 and 38, agreeing with Draft 2); marked the 1994-style orbit forms in `g2_patch_jacobians.py` as superseded.

---

# Draft 1: disposition of the referee report on the 1994 manuscript

This section records Draft 1 and is kept unchanged except as noted here. Remark numbers 2026.1–45 are the same in Drafts 1–3. Later drafts changed some items: Proposition 7.6, Example 7.7 and Corollary 7.8 are now 7.6A, 7.6B, 7.6C; the forms (7.3)–(7.4) and (8.4)–(8.5) of Draft 1 (rows R 35, R 39) were replaced in Draft 2 by Kirillov–Kostant orbit forms and rational Leray fiber forms; the face counts in R 23 are now 268 and 38; and the constants in (1.22) and the formulas of §2 were computed exactly in Draft 3.

Companion to `g2-shalika-germs-2026.tex` (Draft 1). Prepared by Claude (Anthropic) for D. Joyner, 2026-11-13 (updated the same day with the §7 addendum on the transfer factor).

For each item of the referee report [`../referee/g2_referee_report.tex`](../referee/g2_referee_report.tex), this file records what Draft 1 does with it. "R n" refers to **Remark 2026.n** in the paper. Those remarks mark every substantive change and everything not fully verified.

**Dispositions:**
- **fixed**: corrected silently in the text
- **fixed (R n)**: corrected, with a remark
- **conditional (R n)**: the statement is kept, but now depends on a stated hypothesis
- **open (R n)**: the gap is stated, not closed
- **removed**: deleted

Numbering of sections, equations and results is the 1994 numbering. Items added in 2026 carry letters (Conjecture 0.0A, Proposition 3.4A, Table 4.3A, (4.2A), Conjecture 3.7A) or new numbers at the end of a section (Corollary 8.8). So no concordance table is needed.

## The Remarks 2026.n

| R | Where | Topic | Kind |
|---|---|---|---|
| 1 | §0 | The matching is now known (Waldspurger, Ngô, Gordon–Hales) | context |
| 2 | §0 | Langlands' steps 1–3 and the definition of S″ | correction |
| 3 | §0 | Lemma 0.8: the new proviso on other branches | gap stated |
| 4 | §1 | Definition 1.3: a well-defined φ | new definition |
| 5 | §1 | (1.8): sign conventions | correction |
| 6 | §1 | Definition 1.16 of S″ | correction |
| 7 | §1 | (1.18) | correction |
| 8 | §1 | (1.22): w(γ), w(ζ); eight functions on a 7-dimensional variety | correction |
| 9 | §2 | The cocycle condition | correction |
| 10 | §2 | Normalization of (2.8) | correction |
| 11 | §2 | The Dynkin curve (new figure) | new |
| 12 | §2 | (2.11)–(2.14) are schematic; z should be read as −z | gap stated |
| 13 | §3 | Patch formulas (three misprints; fifth patch redundant) | correction, verified by script |
| 14 | §3 | The regular branch is E_Δ, not E_∅ | correction |
| 15 | §3 | Conjecture 3.4: claims for A_n, C_n, D_n not checked | unverified |
| 16 | §3 | Lemma 3.5: Σ_{Δ−S₁} for Σ_{S₁}; new proof | correction |
| 17 | §3 | Lemma 3.6: ρ ≥ σ, and the comparability hypothesis | correction |
| 18 | §3 | Lemma 3.7 becomes Proposition 3.7 (G₂) and Conjecture 3.7A; complete intersection claim withdrawn | correction |
| 19 | §4 | Redundancy among branches: seven branches in all | correction |
| 20 | §4 | Observation (II): valuation argument, no proviso needed | simplification |
| 21 | §4 | Igusa forms: w(ε), w(ζ) denominators; β = 11/3, not 10/3 | correction, verified by script |
| 22 | §4 | Lemma 4.4: rank ℓ, "3-regular", meaning of "induced" | correction |
| 23 | §4 | Exceptional divisors of a toric resolution; β = 2 example | gap stated |
| 24 | §5 | Renamed symbols (υ, c_f, q^{−N}, k) | readability |
| 25 | §5 | Lemma 5.7: principal-part index; proof still a sketch | correction |
| 26 | §5 | Lemma 5.10(c): the chain of classes | correction |
| 27 | §5 | Lemma 5.14: four gaps; treated as a hypothesis | conditional |
| 28 | §5 | Lemma 5.17: H¹ not always cyclic; "(5.10)" misreference | correction |
| 29 | §5 | **The main gap**: Lemma 5.19 does not apply; Hypotheses (X_r) | conditional |
| 30 | §6 | E_{∅,α,γ} = E_α: two β = 2 divisors, not three | correction |
| 31 | §6 | Theorem 6.1 restated as a germ identity, conditional on (X₁) | conditional |
| 32 | §6 | Lemma 6.4: reworded argument | readability |
| 33 | §6 | (6.5b) prefactor; fiber forms not rechecked; choice of E_α or E_β | correction; unverified |
| 34 | §7 | Theorem 7.2, conditional on (X₂); quadratic tori not treated | conditional |
| 35 | §7 | (7.3), (7.4): corrected differentials and coefficient | correction, verified by script |
| 36 | §7 | Status of (X₂): Proposition 7.6, Example 7.7, Corollary 7.8 (new); what remains | new; level 1 |
| 37 | §8 | Theorem 8.3, conditional on (X₃); short-reflection S₃ tori not treated | conditional |
| 38 | §8 | The roots of H₁ = PGL(3) are the short roots | correction |
| 39 | §8 | (8.1), (8.4), (8.5), (8.6) | correction, verified by script |
| 40 | §8 | Corollary 8.8: (X_r) hold a posteriori, given Gordon–Hales | new; level 3 |
| 41 | §9 | Conjecture 9.1 restated; variant g2new9d | correction |
| 42 | A.2 | k×j = −i; the bilinear form; triality for rotations | correction |
| 43 | A.5 | Endoscopic groups: new argument | correction |
| 44 | A.6 | All elliptic tori (Table A.6); the 1994 computations | correction, verified by script |
| 45 | A.7 | Rao's lemma for an odd grading; 6 or 8 classes, not 7 | gap stated |

## Major issues of the referee report

| Issue | Disposition |
|---|---|
| 1. Hales' reduction lemma does not apply | **conditional (R 29, 31, 34, 37).** Lemma 5.19 is kept as quoted, with the exponent 2(r − \|Σ_H^+\|). Its use is replaced by Hypotheses (X_r), stated precisely in R 29. Theorems 6.1, 7.2 and 8.3 are conditional on them. Corollary 8.8 shows that (X_r) holds, given Gordon–Hales; a direct proof is the main open problem. |
| 2. The support hypotheses are never satisfied | **fixed (R 29, 31).** The theorems are now germ identities; the decomposition f = f₁ + f₂ is removed. An equivalent formulation with μ_{O′}(f) = 0 is noted. |
| 3. The roots of PGL(3) | **fixed (R 38, 43).** Σ_{H₁}^+ = {α, γ, δ}. The long-root pseudo-Levi SL(3) is used only for coordinates on O₃. The exponents in (8.7) must be recomputed (open). |
| 4. Missing elliptic endoscopic data | **fixed in A.6 (R 44); open in §§6–8.** Table A.6 lists all elliptic tori. The quadratic and short-reflection S₃ tori are not treated in Theorems 6.1, 7.2, 8.3 (R 31, 34, 37). |
| 5. Which divisors contribute | (a) **fixed (R 30).** (b) **fixed (R 21).** (c) **open:** the β = 11/3 term must cancel (§4, after Table 4.3A). (d) **open (R 23, R 3):** exceptional and spurious divisors are the proviso of Lemma 0.8. The gaps in Lemma 5.14 are **conditional (R 27).** |
| 6. The X-dependence and the measures | **partly fixed (R 35, 36, 39); open.** For the 2-regular biquadratic case, Δ₀(X) is computed (Proposition 7.6) and (X₂) is reduced to the explicit identity (7.7) (Corollary 7.8). The forms (7.3), (7.4), (8.1), (8.4), (8.5) are corrected and checked by script. The exponents f_σ, e_σ in (7.5), (8.7) and the factor Δ₀(X) are not computed; that is (X₂), (X₃). |
| 7. Lemma 3.5, Lemma 4.4 and the "regular branch" | **fixed (R 14, 16, 22).** Lemma 3.5 has a new proof. |
| 8. The definition of S″ and Y″ | **fixed (R 2, 6).** |
| 9. Lemma 3.7 and the singular locus | **fixed (R 18, 23).** Proposition 3.7 for G₂ (saturation script and Hochster); Conjecture 3.7A in general; the complete-intersection claim withdrawn. |
| 10. Section 1 foundations | **fixed (R 4–8).** |
| 11. Section 2 computations | **fixed (R 9–12)**, with (2.11)–(2.14) marked schematic. |
| 12. The appendix | **fixed (R 42–45)**, except that Assem's count is not reconciled (R 45, open). The untypeset weighted Dynkin diagrams are dropped (they remain in `../original-1994/g2newapp.tex`). |

## Minor issues of the referee report

| Location | Item | Disposition |
|---|---|---|
| §0 | T′_G ∩ {1} | fixed |
| §0 | Property (e) | fixed |
| §0 | Δ(γ_H, γ_λ) with Φ(γ_G, f) | fixed |
| §0 | "lemma 5.18" | fixed |
| §0 | \|D_H\| | fixed |
| §0 | "Langland's" | fixed |
| §0, §3 | "Cohen-Macauley" | fixed |
| §0 | Lemma 0.8 "proven in §§4–5" | conditional (R 3) |
| §0 | "blowing up four times" | removed; replaced by the toric resolution (§3, R 23) |
| §1 | "Lemma 1.2 below"; tag (1.3) | fixed (Definition 1.3) |
| §1 | [Sp3] | removed |
| §1 | Lemma 1.21 imprecise | reworded |
| §2 | "§1.1"; X⁰ | fixed |
| §3 | \off prints O_F | fixed |
| §3 | three patch misprints | fixed (R 13) |
| §3 | Lemma 3.6 | fixed (R 17) |
| §3 | Conjecture 3.4 claims | unverified (R 15) |
| §3 | [Sp] | removed |
| §4 | doubled ∧ | fixed |
| §4 | w(ε), w(ζ) | fixed (R 21) |
| §4 | Lemma 4.4 "3-regular" | fixed (R 22) |
| §4 | Observation (II) | fixed (R 20) |
| §5 | Lemma 5.10(c) | fixed (R 26) |
| §5 | Lemma 5.7 index | fixed (R 25) |
| §5 | Lemma 5.17 references | fixed (R 28); the source of ξ in [Ha92a] not checked |
| §5 | Lemma 5.19 exponent | fixed (R 29) |
| §6 | E_{∅,α,γ} = E_α | fixed (R 30) |
| §6 | (6.5b) prefactor | fixed (R 33) |
| §6 | E_α or E_β "depending on T_G" | open (R 33) |
| §6 | exp(\bar F X) | fixed (O_F) |
| §7 | Σ_{O₃} in (7.3); exponent 3/2 | fixed (R 35); the exponent is explained, its normalization not justified |
| §7 | F-rationality of E_{∅,α,δ} | fixed (it is the only branch on Z with β = 3) |
| §8 | (8.6) \|λ\|³ | fixed (R 39) |
| §8 | "conjecture 3.4 (which we proved in §3)" | fixed (Proposition 3.4A) |
| §9 | variant g2new9d; [A], [H4] | noted (R 41) |
| A.6 | s_ζ not simple | fixed (R 44) |
| untypeset | "Lemma 9.1", duplicate "Lemma 1.21" | removed (untypeset text not carried over) |
| throughout | spelling | fixed |

## Other changes

- **Front and back matter** (style guide §§2–3, 6): new title block with the subtitle "Draft 1. Corrected and expanded version", authors David Joyner and Claude, the date line "Original draft: 1994. Corrected and expanded draft: 2026", an abstract with an AI disclosure, a literature review split at 1994, a notation table, a summary of results and open problems, a glossary, acknowledgments and a corrected bibliography. The old USNA address is removed.
- **Bibliography.** Ranga Rao is pp. 505–510; Rogawski [Ro80] is the Compositio paper; Shelstad's title is "A formula for regular unipotent germs"; page ranges added. New entries: [As98], [As00], [De02], [GH16], [Ha94], [Ng10], [SV00], [Ts15], [Wa97], [Wa01]. Uncited entries of 1994 ([Mu88], [Sp69]) are dropped.
- **Untypeset text** after `\enddocument` in four source files (the comparison with H-side subregular germs after §6, the "Igusa forms on Y₁" after §4, the weighted Dynkin diagrams after the appendix, and material after §2) is not carried over. It remains in `../original-1994/` and, switchable, in the transcription.
- **Transfer factor (new subsection at the end of §7).** The 1994 display of Δ in (0.1) is only Δ_III₁Δ_IV. Proposition 7.6 computes the rest near the identity for the biquadratic tori: Δ₀(X) = c·(P(X), d_α)_F with P = βγδε(X). Example 7.7 shows that this is not constant when both quadratic subfields of the splitting field are ramified. Corollary 7.8 makes (X₂) the explicit identity (7.7) for the κ-weighted fiber integral (Remark 2026.36). A pointer was added after the display of Δ in §0, and in Remark 2026.29.
- **Scripts.** `../scripts/g2_patch_jacobians.py` gains the §7 checks for (7.3) and (7.4); `../scripts/g2_transfer_factor_biquadratic.py` is new (root data for Proposition 7.6 and the Hilbert symbols of Example 7.7 over Q_p).
- **Bibliography.** [Ser79] added.

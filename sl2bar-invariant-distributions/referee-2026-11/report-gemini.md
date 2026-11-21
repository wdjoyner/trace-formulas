# Referee report on Draft 2 by Gemini ("Carbon")

Received November 21, 2026, and reproduced verbatim below. Theorem numbers in this report are sometimes off by one or two from the compiled Draft 2; see `report-claude.md` for the corrected numbers and an item-by-item assessment.

---

**Referee Report & Actionable Revision Prompt**

### 1. Mathematical & Technical Errors (High Priority)

* **Sesquilinear vs. Bilinear Mismatch (§6.2, Lemma 6.4 & Corollary 6.7):** In Lemma 6.4, $\langle \varphi_1, T\varphi_2 \rangle$ uses the complex-bilinear pairing of Lemma 6.3 (linear in $\varphi_2$), whereas the right-hand side $\int f_1^\wedge \overline{(Jf_2^\wedge)}$ is conjugate-linear in $\varphi_2$. Replace the left-hand side with an explicitly defined sesquilinear/Hermitian pairing (e.g., $\langle \varphi_1, T\varphi_2 \rangle_{\mathrm{Herm}}$ for unitary/real-axis parameters where $\bar{\mu} = \mu^{\bw}$), and define $T = T_{w_0}$ explicitly (currently $T$ drops the subscript $w$ without notice).


* **Domain/Type Errors in §6.2:**
* $\mu \in \Pi(\bC)$ is a genuine character of $\bC \subset \bA$, yet the text repeatedly writes $\mu(x) = \mu_0(x)\vert{}x\vert{}^s$ for $x \in \F^\times$. Fix by writing $\mu(\tilde{h}(x))$ for a specified splitting/section on $C$ (or on $A^\nu$), ensuring genuineness on $\mu_n$ is respected.


* Lemmas 6.2, 6.3, 6.5, Proposition 6.6, and Corollary 6.7 write $I_{\bA}(\mu)$, whereas §6.1 defines $I_{\bA}(\chi)$ for $\chi \in \Pi(\bA)$. Change $I_{\bA}(\mu)$ to $I_{\bA}(\chi_\mu)$ (or explicitly define $I_{\bA}(\mu) := I_{\bA}(\chi_\mu)$).


* In the definition of $K(\mu)$, condition (i) has $f: \F \times \bA \to \C$ with $f(x, a_1a_2)$, which is fine, but condition (ii) writes $\chi(h(x), 1)$ where $\chi = \chi_\mu$ is a *multidimensional* representation of $\bA$ (dimension $d = [\bA : \bC]$), not a scalar character, while $f(x,a) \in \C$. Clarify whether condition (ii) uses $\mu((h(x),1))$ for $h(x) \in C$ (or $\vert{}x\vert{}$ large/small in the Kirillov model). Also check $\vert{}x\vert{}$ large vs. $\vert{}x\vert{}$ small: in standard $p$-adic Kirillov models on $\F^\times$, asymptotic behavior near $0$ ($\vert{}x\vert{}$ small) is governed by Jacquet modules while compact support holds for $\vert{}x\vert{}$ large.


* In $V(\mu)$ condition (ii), $\delta(a_1)$ should be $\delta_B(a_1)^{1/2}$ (matching §6.1) or explicitly normalized so Lemma 6.3's integrand has weight $\delta_B = \vert{}a\vert{}^2$.


* In Lemma 6.3's parenthetical remark, there is an unmatched parenthesis: `\vphi(\begin{psmallmatrix}a&*\\0&a^{-1}\end{psmallmatrix},\varsigma)g)` is missing a `(` after `\vphi`.




* **Torus Parameterization Clash (§3.2 vs. §5 vs. §8.1):** Section 3.2 defines $X(\bA)$ via $A^n$, Section 5 uses $A^\nu$ ($\nu = n$ or $n/2$), and Section 8.1 restricts $\mu$ to $\operatorname{diag}(x, x^{-1}) \in A^n$. Note that the center of $\bA$ has projection $A^\nu$, not $A^n$, when $n$ is even. Reconcile $A^n$ vs. $A^\nu$ throughout. Also fix the typo `Ind_{\overline{C}}^{A}\mu` in §8.1 (missing overline on $A$: should be `\Ind_{\bC}^{\bA}\mu`).


* **Algebraic vs. Continuous Duals in §8.2:** Section 1 defines an invariant distribution as a *continuous* linear functional on $C_c^\infty(\bG)$ (note: on $p$-adic $C_c^\infty(\bG)$ with the standard inductive limit topology of finite-dimensional spaces, *every* linear functional is continuous). Explicitly state in §8.2 that because $C_c^\infty(\bG)$ carries the finest locally convex topology, its algebraic dual $C_c^\infty(\bG)'$ coincides with its continuous dual (the space of distributions). This closes the apparent logical gap between §1 ("continuous") and Theorem 8.5 ("algebraic duals").


* **Laplacian Sign Error in Lemma 8.8 (§8.3):** With $\Delta = \sum_j \partial^2/\partial x_j^2$, we have $\Delta(e^{ik\cdot x}) = -\vert{}k\vert{}^2 e^{ik\cdot x}$, so $(1 - \Delta)^N e^{ik\cdot x} = (1 + \vert{}k\vert{}^2)^N e^{ik\cdot x}$. This part is correct, **however** in the prose right before Lemma 8.8, ensure $W$ acting by isometries preserves $\Delta$ on $X = \R^d/(2\pi\Z)^d$ under the chosen identification of $\Pi(\bC)_u$ with $X$.


* **Theorem 6.9 / Classification Completeness:** Theorem 6.9 writes "*the* special representation $\pi_{sp}$", whereas twisted genuine characters $\mu = \mu_0 \vert{}\cdot\vert{}^{1/n}$ (with $\mu_0^2 = 1$ or Weyl-self-conjugate unitary twists) generally yield multiple special/non-tempered representations (one per eligible ramified/unramified twist). Change "the special representation $\pi_{sp}$" to "a special representation" in Theorem 6.9 (matching Theorem 6.8's "a 'special' or 'trash' representation").


* **Section 8.4 Remark ($n=1$):** Section 3.1 explicitly assumes $n > 1$, whereas Remark 8.9 says "Assume $\bG = G$ ($n=1$)". Note briefly that $n=1$ relaxes the standing $n>1$ convention of §3.1.



---

### 2. LaTeX, Notation, and Readability Fixes (Medium Priority)

* **Typos:**
* Page 11 (proof of Theorem 8.7): `compactsmooth` $\to$ `compact smooth`.


* Bibitem `\bibitem{GS75}`: `automorphic froms` $\to$ `automorphic forms`.


* Bibitem `\bibitem{Be84}`: `Le center de Bernstein` $\to$ `Le centre de Bernstein`, and `un corp local` $\to$ `un corps local`.


* Bibitem `\bibitem{BZ76}`: `non-archimedian` $\to$ `non-Archimedean` (and `Zelevinski` $\to$ `Zelevinsky` if standardizing).


* Bibitem `\bibitem{Sc50}`: `Theorie` $\to$ `Th\'eorie`.


* Bibitem `\bibitem{Vi81}`: `integrales` $\to$ `int\'egrales`.


* §6.2, Lemma 6.4: `an $d\times d$ matrix` $\to$ `a $d\times d$ matrix`.




* **Formatting & Macros:**
* In §8.1, replace antiquated `\rm`, `\it`, `Ind`, and `diag` with `\mathrm`, `\emph`, `\Ind`, and `\operatorname{diag}`.


* Unify field notation: §3.1 sets $F = \F$, and the paper oscillates randomly between $SL(2, F)$ and $SL(2, \F)$. Pick $F$ (standard) or $\F$ everywhere and eliminate the redundant alias.


* Unused bibliography entries: The following `\bibitem`s are never `\cite`d in the text: `Ar81`, `Be75`, `Da99`, `HC84`, `Jo88`, `JM00`, `Me98`, `Cl26`, `Vi81`. Either cite them where appropriate (e.g., `Cl26` in Acknowledgments, `Vi81` near orbital integrals in §5) or remove them.


* Unused macro: `\verify` is defined in the preamble, and several `% \verify{...}` comments remain in the source. Clean up or convert any remaining substantive `% \verify` notes (especially Proposition 6.1's exceptional character note and Lemma 6.4's sesquilinearity note) into explicit text/remarks.





---

### 3. Structural & Expository Improvements (Low Priority)

* **Meta-Commentary Cleanup:** In Remark 6.8 ("The supplied corrected 2026d draft asserted...") and Section 7 ("The corrected 2026d paper replaces..."), internal version labels like `2026d` are opaque to external readers. Replace `2026d` with "an earlier 2026 revision [Cl26]" (which also gives `\bibitem{Cl26}` a proper citation).


* **Redundant Introductions in §8:** The opening paragraph of §8 says *"We classify the image of $C_c^\infty(\bG)$ and of $\calC(\bG)$..."* as an unconditional claim, contradicting Remark 8.1 and Remark 8.2 which explicitly state those images are *unverified* proposals. Soften the opening sentence of §8 to *"We review the proposed image of $C_c^\infty(\bG)$ and $\calC(\bG)$... and establish the algebraic factorization..."*


* **Section 4 Placement:** Section 4 (a full-page notation table) interrupts the mathematical flow right after §3.2 just defined the exact same notation. Consider moving the Section 4 table to an appendix alongside the Glossary, or merging it cleanly with the Glossary.
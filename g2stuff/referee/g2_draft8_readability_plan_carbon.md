## Editorial Action Plan: Readability & Whitespace Expansion

**Target Objective:** Increase vertical whitespace, eliminate inline mathematical wall-of-text eyestrain, and clarify nested prose in `g2_shalika_germs_2026.tex` (expanding total length by ~5–8 pages). Preserve all mathematical content, `\label`/`\ref`/`\tag` numbering, and theorem statements exactly. Use `\[ ... \]` or `align*` (never `$$ ... $$`).

---

### Part 1: Inline Expressions to Promote to Display Math (`\[ ... \]` / `align*`)

1. **\S0 (Notation & Detailed Outline):**
* **Harish-Chandra orbit dimension:** Extract $\dim{\mathcal O} = \dim G_u\setminus G = \dim G - \mathrm{rk}(G) - 2r = 2\vert{}\Sigma^+_G\vert{} - 2r$ (below $\Gamma_{\mathcal O}(\exp(\lambda^2 X))$) into `\[ ... \]` and place the definitions of $G_u$, $r=\dim{\mathcal B}_u$, and $\Sigma^+_G$ in a clean trailing sentence.
* **Normalized germ scaling:** Display $\Gamma^*_{\mathcal O}(\gamma) := \vert{}D_G(\gamma)\vert{}\Gamma_{\mathcal O}(\gamma)$ and $\Gamma^*_{\mathcal O}(\exp(\lambda^2 X)) = \vert{}\lambda\vert{}^{2r}\Gamma^*_{\mathcal O}(\exp(X))$ right before `(0.1A)`.
* **Transfer factor invariance:** Display $\Delta_{G/H}^{T_G,\kappa}(\gamma_H,\gamma'_G) = \kappa(\inv(\gamma_G,\gamma'_G))\Delta_{G/H}^{T_G,\kappa}(\gamma_H,\gamma_G)$ above the definition of $\Gamma_{\mathcal O}^{T,\kappa}(\gamma)$.


2. **\S1 & \S2 (Coordinates & Galois Action):**
* **Unipotent decompositions (\S1, Coordinates on $Y''$):** Display $g = g_0 t_+ n_- n_+$ alongside $(t^g, (B_G(W)^g)_W) = (t'_+ n'_-, (B_-^{n_W})_W)^{n_+}$ rather than burying $t^g=(t'_+n'_-)^{n_+}$ inline.
* **Galois conjugation factors (\S2):** Before `(2.11)` and `(2.13)`, display the auxiliary definitions $t = \alpha^\vee(1+x(\alpha)z),\quad y_\alpha = -\frac{x(\alpha)z^2}{1+x(\alpha)z}$ and $t = \beta^\vee(u_\beta),\quad u_\beta = 1+x(\beta)z,\quad y_\beta = -\frac{x(\beta)z^2}{u_\beta}$.
* **Special-fiber Galois denominators (\S2, Prop. 2.14A):** Pull $D_\alpha := 1 + 3\alpha(X)\sigma(w(\gamma)) - 3\alpha(X)^2\sigma(w(\delta)) + \alpha(X)^3\sigma(w(\eps))$ in (a) and $D_\beta := 1 - \beta(X)\sigma(w(\gamma))$ in (b) out of the prose into standalone displays before the coordinate transformation blocks.


3. **\S3 & \S4 (Regular Patches & Toric Divisors):**
* **Four regular patches of $Z$ (\S3):** Convert the four dense inline paragraphs ($x(\alpha)\neq 0$, $x(\beta)\neq 0$, $x(\gamma)\neq 0$, $w(\zeta)\neq 0$) into four two-line `align*` blocks showing the 6 dependent coordinates on each patch.
* **Monomial identities on $Z$ (\S3):** Display the three key identities $x(\delta)z(\alpha)^2 = x(\beta)w(\delta)$, $x(\epsilon)z(\alpha)^3 = x(\beta)w(\epsilon)$, and $x(\zeta)z(\alpha)^3z(\beta) = x(\beta)w(\zeta)$.
* **Proof of Lemma 3.5:** Display $x(\rho) = \lambda w(\rho)\prod_{\alpha\notin S_1} z(\alpha)^{-m_\rho(\alpha)}$ and the generator dimension count $1 + (\ell-\vert{}S_1\vert{}) + (p-\vert{}\Sigma^+_{\Delta-S_1}\vert{}) + (\vert{}\Sigma^+_{\Delta-S_1}\vert{} - (\ell-\vert{}S_1\vert{})) = p+1 = \dim Z$.
* **Toric form $\omega_Z$ (\S4, before Table 4.3A):** Display $m_\omega = (7,-10,-6,1,1,1,1)$ and $\omega_Z = \lambda^7 z(\alpha)^{-10} z(\beta)^{-6} w(\gamma) w(\delta) w(\epsilon) w(\zeta)\, \frac{d\lambda}{\lambda}\wedge\cdots\wedge\frac{dw(\zeta)}{w(\zeta)}$.
* **Proof of Lemma 4.4:** Display the three explicit $b$-factorizations on $E_{\emptyset,\beta,\zeta}$, $E_{\emptyset,\alpha,\delta}$, and $E_{\emptyset,\alpha,\zeta}$ alongside the commutator relations $[X_\alpha,X_\delta]=3X_\epsilon$, $[X_\gamma,X_\delta]=3X_\zeta$.


4. **\S5 (Igusa Expansion & Cocycle):**
* **Normal-crossings assumptions `(5.1)`–`(5.3)`:** Display $\lambda = \upsilon \prod_i \mu_i^{a_i}$, $f(\mu_1,\dots,\mu_n) = c_f \prod_i \kappa_i(\mu_i)$, and $\omega = \prod_i \mu_i^{b_i-1}\, d\mu_1\wedge\cdots\wedge d\mu_n$ inside the itemized list.
* **Proof of Lemma 5.17:** Display the leading-minor cocycle formula $t_0 T_\sigma = \alpha^\vee(z(W_0,\alpha))$ and the class-field composition $\kappa(\tilde{t}_*) = \theta(\phi_T(\tilde{t}_*))$.


5. **\S7 ($2$-Regular Germ & Biquadratic Tori):**
* **Hales coordinates & kernel (\S7, Fiber form on $E_{\emptyset,\alpha,\delta}$):** Display $b = \theta_\delta(x(\delta))\theta_\epsilon(x(\epsilon))\theta_\zeta(x(\zeta))$, the kernel relation $dv(\beta) + x(\epsilon)\,dx(\zeta) = 0$, and the Hales coordinate split:

$$\text{Base } \mathcal O_2: \bigl(x(\delta),x(\epsilon),x(\zeta),v(\alpha),v(\gamma),v(\delta),v(\epsilon),v(\zeta)\bigr), \qquad \text{Fiber } E_{\emptyset,\alpha,\delta}(u): \bigl(z(\beta),w(\gamma),w(\delta),v(\beta)\bigr).$$


* **Proof of Prop. 7.6E:** Display $\lambda = \ell_E z(\alpha)^2$ with $\ell_E := x(\delta)z(\beta)/w(\delta)$, $D_E := \beta\gamma\, w(\delta) - 2F_0$, and the $L/F$-norm identities $N_{L/F}(\alpha\zeta) = -d_\alpha d_\zeta u^2 v^2$, $N_{L/F}(\gamma\epsilon) = P(X)$, and $\omega_{K/L}(c(X)) = (-d_\alpha d_\zeta, d_\alpha)_F (P(X), d_\alpha)_F$.
* **Prop. 7.6G setup:** Display the fiber cutting equations ($x(\delta)=1$, $x(\epsilon)=x(\zeta)=0$, $v(\rho)=0$ for $\rho\neq\beta$) and align the four polynomial definitions $D_\alpha^0$, $F_0$, $H$, $D_{-1}$, and $D_{s_\zeta}$ in a clean multi-line `align*` block before part (a).
* **Proof of Thm. 7.6H:** Display the Jacobian identity $\det\frac{\partial(U,\log V)}{\partial(w(\gamma),w(\delta))} = \frac{\alpha\zeta\, H}{F_0^2\, G}$ in (a)–(b), the intermediate rational expression for $\Phi_E\vert{}_{u_0}$ in (c), and the factored integral $J'(X) = \vert{}d_\alpha d_\zeta\vert{}_F^{-1/2} \vert{}\alpha(X)\zeta(X)\vert{}_F\, \vert{}I_t\, I_s\, I_\xi\vert{}$ along with the explicit definitions and values of $I_t$, $I_s$, and $I_\xi$ in (d).


6. **\S8 ($3$-Regular Germ & Cubic Tori):**
* **Orbit vs. fiber coordinate split (\S8, Fiber form on $E_{\emptyset,\beta,\zeta}$):** Display $\pi(y) = (n_+')^{-1}\theta_\zeta(x(\zeta))n_+'$ and display the 6 orbit coordinates vs. 6 fiber coordinates in parallel with \S7.
* **Prop. 8.3D:** Display the asymptotic equivalences for $p_1$, $p_2$, $q_1$, and $q_2$ as a two-line `align*` block instead of inline prose. In the proof, display the $(\tau^2)^*$ polynomial composition identity.
* **Prop. 8.3E:** Display the chamber-hexagon definition of $(\eta_0,\dots,\eta_5)$ in the statement, display the four cubic differences $m_1, m_2, d_{024}, d_{135}$ in an `align*` block in (b), and display the quadratic discriminant factorization in the proof.
* **Prop. 8.3F:** Display $\omega_{\mathcal Q_3}$ at the end of (b) as its own equation rather than inline after `(8.7f)`, and display the linear rational expression for $(\eta_2-\eta_0)/(\eta_4-\eta_0)$ in the proof.
* **Prop. 8.3G (Split quadric cone & $R_{\mathrm{cone}}$):**
* In (a), display the birational inverse $j_2 = \frac{(1-k_2)(k_0+k_1)}{(Y+1)(Y+k_0)}$ and the non-vertex $F$-point.
* In (b), display $Q_0$, $A_{\mathrm{num}}$, $W_\alpha$, $S_F := Q_0^3/A_{\mathrm{num}}^2$, and $\Lambda_F := \tr_{K/F}(\alpha(X)W_\alpha)$ in an `align*` block before `(8.7h)`.
* At the end of (b), display the Igusa norm regulator factorization and $R_{\mathrm{cone}}$:

$$N_{K/F}\!\Bigl(\frac{z(\alpha)^3}{w(\zeta)}\Bigr) = N_{K/F}(\beta(X))^2\, d_{024}^3\, R_{\mathrm{cone}}, \qquad R_{\mathrm{cone}} := -\frac{N_{K/F}(Y+k_0)^2 N_{K/F}(k_0+1)^2 N_{K/F}(1-k_0)^2}{64(Y+1)^3 N_{K/F}(Q_0)\,\Lambda_F^3}.$$




* **Conjecture 8.3H Heuristic Derivation:** Display the formal factorization $J_3(X) = \vert{}\alpha(X)\gamma(X)\delta(X)\vert{}_F \cdot I_{\mathbb P^1(K)} \cdot J_{\mathcal Q_3}(X)$, the integral $J_{\mathcal Q_3}(X)$, and the evaluated values of $B_1'(1)$, $B_2(1)$, and $\vert{}J_{\mathcal Q_3}(X)\vert{}$ across the unramified and tamely ramified cases.
* **Appendix B (Remark 2026.27 / `rem:1.22`):** Display the three triangular gallery equations for $n_\delta, n_\epsilon, n_\zeta$ in item (iii) instead of running them inline.





---

### Part 2: Dense Sentences & Paragraphs to Restructure for Clarity

1. **Definition of "Endoscopically Richardson" (\S0, Introduction):**
* *Issue:* Buried mid-paragraph in a 9-line sentence with nested parentheticals.
* *Action:* Break the paragraph before "The $2$- and $3$-regular classes..." and state the definition cleanly with displayed conditions:
> The $2$- and $3$-regular classes of $G_2$ are not Richardson in $G_2$, but are **endoscopically Richardson**. Specifically, for an endoscopic group $H$ of $G$, we call a unipotent class $\ooo$ of $G$ *endoscopically Richardson* (with respect to $H$) if:
> 1. $\dim\ooo = \dim G - \dim H$ (equivalently, $r(\ooo) = \vert{}\Sigma_H^+\vert{}$), and
> 2. $\ooo = \Ind_M^G(1)$ is induced in Spaltenstein's sense `\cite{Spa82}` from the trivial class of a pseudo-Levi subgroup $M \subset G$ having the same rank and dimension as $H$.
> 
> 




2. **Paragraph Immediately Following Eq. `(0.1)` (\S0):**
* *Issue:* A 25-line solid block defining $\Delta_{G/H}^{T_G,\kappa}$, $\Delta_0(X)$, ${\mathcal O}^{st}$, $\gamma_\lambda$, $V_f$, $t_*$, $\phi^{-1}(\gamma_\lambda)^\Gamma$, and $\vert{}\omega\vert{}/\vert{}\phi^*(d\lambda)\vert{}$ in one breath.
* *Action:* Split into two short paragraphs (first covering the transfer factor decomposition $\Delta_{III_1}\Delta_{IV}$ vs. $\Delta_0(X)$, second introducing a bulleted list for the remaining components of `(0.1)`: the sum over ${\mathcal O}^{st}$, the curve parameter $\gamma_\lambda \in C \cap V_f$, the cocycle $t_*$, and the $\Gamma$-fixed fiber measure).


3. **"Status of the results in this revision" Bullet List (\S0):**
* *Issue:* The first `\item` (*Proved:*) is a single 19-line semicolon-separated sentence spanning half a page.
* *Action:* Subdivide the *Proved* item into 4 thematic sub-bullets: (i) *Toric geometry of $Z$ and branches* (\S\S3–4), (ii) *Differential forms and Galois actions* (\S\S1–2, 6–8), (iii) *Biquadratic $2$-regular matching $(\mathrm X_2)$* (\S7), and (iv) *Cubic $3$-regular reduction and group-theoretic tables* (\S8, App. A).


4. **Galois Cancellation Argument (\S2, between `(2.11)` and `(2.12)`):**
* *Issue:* Dense 12-line inline chain of group-element identities verifying $n_0=1$.
* *Action:* Break into step-by-step sentences and display the conjugation cancellation $\theta_{-\alpha}(-z)\,\sigma_\alpha(t_0)\,\theta_{-\alpha}(z) = \sigma_\alpha(t_0)\,\theta_{-\alpha}\bigl(z(1-\alpha(t_0)^{-1})\bigr)$ so the reader can visually see $\theta_{-\alpha}(y_\alpha)$ and $\alpha^\vee(\alpha(t_0))$ cancel.


5. **Remark 2026.7 (`rem:exceptional` in \S4):**
* *Issue:* Overly compressed paragraph mixing cone face-vector combinatorics, singular face counts, and subdivision ray examples.
* *Action:* Split into two paragraphs—Paragraph 1 covering the fan $\sigma$, the face vector $(1,11,43,82,84,46,12,1)$, and the 5 minimal singular faces; Paragraph 2 covering toric subdivision rays $u$, the example $u=(3,2,2,2,3,5,7)$ (displayed), and why exceptional divisors with $\beta \in \{2,3,4\}$ yield the proviso of Lemma 0.8.


6. **Remark 2026.11 (`rem:main-gap` in \S5):**
* *Issue:* Long, unbroken historical diagnosis of why Hales's Reduction Lemma 5.19 fails for $G_2$.
* *Action:* Split into three crisp paragraphs: (1) Why $\Lie Z(H)=0$ and why Levi centralizers in $G_2$ cannot equal $SL(3)$ or $SO(4)$; (2) Comparison with Hales's $GSp(4)$ strategy in `\cite{Ha89}` and minor 1994 normalization fixes; (3) Introduction of $I_E(X,u)$ and Hypothesis $(\mathrm X_r)$.


7. **Proof of Proposition 7.6D (\S7):**
* *Issue:* Dense paragraph tracking leading principal minors, cocycle conditions, and Tate–Nakayama restriction $H^1(F,T) \to H^1(L,T)$ simultaneously.
* *Action:* Split into two paragraphs (Paragraph 1: Bruhat minor computation giving $T_\tau = \alpha^\vee(R)^{-1}\beta^\vee(Q)^{-1}$ with $R,Q \in L^\times$; Paragraph 2: Tate–Nakayama restriction $x \mapsto x + s_\alpha x$ displayed, showing $\beta^\vee \mapsto \alpha^\vee$ and $\alpha^\vee \mapsto 0$).


8. **Proof of Theorem 7.6H(d) (\S7, $p$-adic Principal-Value Evaluation):**
* *Issue:* A 30-line wall of text computing boundary regularizations and three separate $p$-adic integrals ($I_t, I_s, I_\xi$) across ramified and unramified subcases inline.
* *Action:* Split into four short blocks:
* *Boundary regularization:* How $e(1,3)=1$ and `LS83` make boundary unit rescalings evaluate to $\vert{}c(X)\vert{}^{a_{E'}s}\vert{}_{s=0}=1$.
* *Integral $I_t$:* Display $I_t = \int_{\OF}[(t^2-d_\alpha d_\zeta, d_\alpha)_F - 1]\,dt$ and list the $v_F(d_\alpha d_\zeta)=1$ vs. $v_F(d_\alpha)=v_F(d_\zeta)=1$ evaluations.
* *Integrals $I_s$ and $I_\xi$:* Display both integrals and state their $v_F(d_\zeta)=0,1$ values.
* *Assembly:* Multiply $\vert{}d_\alpha d_\zeta\vert{}_F^{-1/2}\vert{}I_t I_s I_\xi\vert{}$ to conclude `(7.13)`.




9. **Acknowledgments (\S Back Matter):**
* *Issue:* A single 42-line paragraph chronicling Drafts 1 through 8 sequentially.
* *Action:* Break into 3 readable paragraphs: (1) 1994 origins; (2) Drafts 1–6 mathematical reconstructions and symbolic scripts; (3) Drafts 7–8 editorial completion, open-problem framing, and author responsibility statement.





---

### Part 3: Global Layout Adjustments for Breathing Room

* Add `\setlength{\jot}{6pt}` in the preamble so multi-line `split` and `align*` blocks (`(1.21a)`, `(1.22)`, `(2.11)`, `(2.13)`, Prop. `2.14A`, `(8.7d)`) have generous vertical line spacing between fractions.
* Add `\renewcommand{\arraystretch}{1.25}` to the Notation `longtable` so superscripts/subscripts do not crowd horizontal rules or adjacent rows.
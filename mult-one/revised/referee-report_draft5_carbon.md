## Referee Report: *Direct comparison of $SL(2)$ with its metaplectic cover* (Draft 5)

### 1. Summary and Overall Assessment

This monograph is an unusual, refreshingly transparent, and mathematically instructive work. Originating from an unpublished 1995 manuscript that attempted to deduce multiplicity one for $SL(2)$ from Waldspurger's multiplicity one theorem for the 2-fold metaplectic cover $\overline{SL(2)}$ via a direct ("element-by-element" / odd) comparison of trace formulas, the present Draft 5 completely pivots to establish the exact opposite: **such a direct global correspondence does not exist** (Theorem 5.7).

The core mathematical insight is clean and illuminating:

* **Locally on the split torus**, the direct ("odd") comparison works well—one can bijectively match characters of $A(F)$ with genuine characters of $\overline{A(F)}$ (after choosing $\eta_\varpi$ with $\eta_\varpi^2 = (\varpi,\varpi)^{-1}$), match test functions preserving Fourier transforms, and obtain an isomorphism of spherical Hecke algebras and an equality of principal series traces (Chapter 4, §§4.3.1, 4.3.2, 4.3.4).


* **Globally**, this Satake isomorphism matches unramified parameters up to sign ($t = \pm t'$), whereas the true automorphic Shimura–Waldspurger correspondence followed by restriction from $PGL(2)$ to $SL(2)$ squares the parameters ($t = t'^2$, corresponding to the degree-2 projection $SL(2,\mathbb{C}) \to PGL(2,\mathbb{C})$ on dual groups).


* Using Labesse–Langlands, Waldspurger's correspondence, the Gelbart–Jacquet symmetric square lift, and Jacquet–Shalika Rankin–Selberg theory, **Theorem 5.7** proves cleanly via a pole-counting contradiction at $s=1$ for $L^{S'}(s, \mathrm{Ad}(\Pi) \times \mathrm{Ad}(\Pi))$ that *no* genuine cuspidal automorphic representation of $\overline{SL(2,\mathbb{A})}$ matches any cuspidal $\pi$ of $SL(2,\mathbb{A})$ under the direct Satake isomorphism at almost all places. Consequently, the formal trace-formula hypotheses (Hypotheses 5.3 and 5.5) that would imply multiplicity one (Proposition 5.6) are mutually inconsistent (Corollary 5.8).



The manuscript is mathematically sound in its main claims, remarkably honest about unverified 1995 legacy material (via the `Remark 2026.n` convention), and valuable both as a cautionary tale in functoriality/trace-formula comparisons and for its explicit local calculations.

However, **several subtle sign/cocycle conventions and residual mathematical glitches from the 1995 text remain in the local chapters**, and **readability suffers in places from abrupt transitions between polished 2026 prose and raw 1995 notes**. Below is a detailed breakdown of mathematical corrections, verification of the flagged `2026.n` remarks, and structural/editorial recommendations.

---

### 2. Mathematical Issues and Necessary Corrections

#### A. Critical Sign / Convention Mismatches in Local Chapters

1. **Genuine vs. Anti-genuine Characters ($\zeta$ vs. $\zeta^{-1}$ vs. $\varsigma$):**
* In equation (2.5) (`eq:genuine`), a function $f$ on $\overline{G(F)}$ is defined to be **genuine** if $f(g,\varsigma) = \varsigma f(g,1)$. Since $\varsigma \in \mu_2 = \{\pm 1\}$, $\varsigma = \varsigma^{-1}$, so mathematically $\zeta$ and $\zeta^{-1}$ are identical on $\mu_2$.


* *However*, writing $\zeta^{-1}$ in Lemma 4.2 (`eq:chi-eps`: $\overline{\chi}_\epsilon(a(x),\zeta) = \zeta^{-1}\chi_1(x)$) and in §4.3.2 ($\zeta^{-1}\chi_1(x)$) while writing $\zeta \chi_1$ in the very last sentence of Lemma 4.2 ("extending $\zeta\chi_1$") and $\zeta\chi_\psi(x)\mu(x)$ in §5.3 is jarring. Since $\mu_2 = \{\pm 1\}$, $\zeta^{-1} = \zeta$, and you should replace $\zeta^{-1}$ with $\zeta$ throughout §§4.3.1–4.3.2 so the reader doesn't hunt for a hidden 4th root of unity.


* Relatedly, in §4.7.3 (p. 24), the text states: *"there is an anti-genuine function $\Theta_\epsilon(g)$ on $\overline{G(F)}$"*. Over $\mu_2 = \{\pm 1\}$, "genuine" and "anti-genuine" are the exact same condition ($f(g,-1) = -f(g,1)$)! That terminology is a holdover from $n$-fold covers ($n > 2$, as in Flicker [Fl]) where $\mu_n$ has conjugate characters. For a 2-fold cover, replace "anti-genuine" with "genuine" (or add a parenthetical noting they coincide for $n=2$).




2. **Global Splitting Cocycle Formula in §2.2 (Page 8):**
* You define $\beta'_v(g_1,g_2) = \beta_v(g_1,g_2) s_v(g_1) s_v(g_2) s_v(g_1 g_2)^{-1}$, where $\kappa_v(k) = (k, s_v(k))$ is the splitting on $K_{0,v}$. Let us check the homomorphism condition for $\kappa_v$ under multiplication $(k_1, s_v(k_1))(k_2, s_v(k_2)) = (k_1 k_2, \beta_v(k_1,k_2) s_v(k_1) s_v(k_2))$. For this to equal $(k_1 k_2, s_v(k_1 k_2))$, we must have $\beta_v(k_1,k_2) = s_v(k_1)^{-1} s_v(k_2)^{-1} s_v(k_1 k_2)$ (which over $\{\pm 1\}$ is $s_v(k_1)s_v(k_2)s_v(k_1k_2)$).


* Consequently, $\beta'_v(k_1, k_2) = 1$ on $K_{0,v} \times K_{0,v}$, which is **correct** (since $s_v \in \{\pm 1\}$).


* **However**, look at Lemma 2.4 and the sentence after it: *"the splitting... is given by $\gamma \mapsto (\gamma, s_{\mathbb{A}}(\gamma)^{-1})$"*. Wait: if you work in the model $G(\mathbb{A}) \times \mu_2$ equipped with the modified cocycle $\beta_{\mathbb{A}} = \prod_v \beta'_v$, then by Kubota's reciprocity law ($\prod_v \beta_v(\gamma_1, \gamma_2) = 1$ for $\gamma_1, \gamma_2 \in G(k)$), we have:



$$\beta_{\mathbb{A}}(\gamma_1, \gamma_2) = \left(\prod_v \beta_v(\gamma_1,\gamma_2)\right) s_{\mathbb{A}}(\gamma_1) s_{\mathbb{A}}(\gamma_2) s_{\mathbb{A}}(\gamma_1\gamma_2)^{-1} = s_{\mathbb{A}}(\gamma_1) s_{\mathbb{A}}(\gamma_2) s_{\mathbb{A}}(\gamma_1\gamma_2)^{-1}.$$



Therefore, in the $(G(\mathbb{A}) \times \mu_2, \beta_{\mathbb{A}})$ coordinates, $(\gamma_1, \varsigma_1)(\gamma_2, \varsigma_2) = (\gamma_1\gamma_2, \beta_{\mathbb{A}}(\gamma_1,\gamma_2)\varsigma_1\varsigma_2)$, and the splitting of $G(k)$ is $\gamma \mapsto (\gamma, s_{\mathbb{A}}(\gamma)^{-1})$ (which equals $(\gamma, s_{\mathbb{A}}(\gamma))$ since $s_{\mathbb{A}}(\gamma) \in \{\pm 1\}$!), **whereas** in the quotient-of-restricted-product model $\bigl(\prod'_v \overline{SL_2(k_v)}\bigr)/Z_0$ (using $\beta_v$ locally), the diagonal embedding $\gamma \mapsto \prod_v (\gamma, 1) \bmod Z_0$ is *already* a homomorphism (by Hilbert reciprocity $\prod_v \beta_v(\gamma_1,\gamma_2) = 1$) and lies in the restricted product because $(\gamma, 1) = \kappa_v(\gamma)(1, s_v(\gamma))$ with $s_v(\gamma)=1$ almost everywhere!
* Please clarify which coordinate model Lemma 2.4's formula $\gamma \mapsto (\gamma, s_{\mathbb{A}}(\gamma)^{-1})$ refers to (namely, the $\beta_{\mathbb{A}}$ coordinates where $\kappa_v(K_{0,v}) = K_{0,v} \times \{1\}$). Mixing the two models without warning is a classic trap in metaplectic literature (and specifically impacts the hyperbolic check in §5.4, p. 35, where you write *"An element $\gamma = a(x)$ of $G(k)$ has the local components $(a(x),1)$ in the cover, since $s_v(a(x))=1$"* — which is true in both models precisely because $s_v(a(x))=1$).




3. **Weyl Integration Formula Normalization in §4.3.3 (Page 17):**
* Look closely at the definition of $\Phi_f(t)$ in §4.3.3:

$$\text{"let } \Phi_f(t) = |D(t)|\, O_f(t)\text{"}$$



followed immediately by the Weyl integration formula:

$$\Theta_\pi(f) = \sum_{T \in \mathcal{T}} \frac{1}{|W_T|} \int_{T(F)} \Theta_\pi(t) \Phi_f(t)\, dt.$$


* **This has the wrong exponent on $\vert{}D(t)\vert{}$ if $\Theta_\pi(t)$ is the unnormalized character!** In Harish-Chandra's Weyl integration formula, the Jacobian is $\vert{}D(t)\vert{}$:

$$\int_{G(F)} \Theta_\pi(x) f(x)\, dx = \sum_{T \in \mathcal{T}} \frac{1}{|W_T|} \int_{T(F)} \Theta_\pi(t) |D(t)| O_f(t)\, dt.$$



Wait: let us check §4.5.4 (p. 20–21)! In §4.5.4, $\Theta_{\pi_m}(r(\theta)) = -\operatorname{sgn}(m) \frac{e^{im\theta}}{e^{i\theta}-e^{-i\theta}}$, which has **one** factor of $|e^{i\theta}-e^{-i\theta}| = |D(r(\theta))|^{1/2}$ in the denominator. For the integrand $\Theta_{\pi_m}(r(\theta)) \Phi_f(r(\theta))$ in §4.5.4 to be smooth (and for Definition 4.9 / Lemma 4.11 to work, where $\Phi_{\overline{f}}(\overline{r}(2\theta)) = (e^{i\theta}+e^{-i\theta})\Phi_f(r(\theta))$ cancels *one* factor of $e^{i\theta}+e^{-i\theta}$ rather than $|e^{i\theta}+e^{-i\theta}|^2$!), **$\Phi_f$ in §4.5.4 is clearly the Harish-Chandra `'F_f'` invariant integral $\epsilon_R(t) \Delta(t) O_f(t)$ (which has $|D(t)|^{1/2}$, or $(e^{i\theta}-e^{-i\theta})$, NOT $|D(t)| = |e^{i\theta}-e^{-i\theta}|^2$)!**


* Let's double check this! For $SL(2,\mathbb{R})$, $\vert{}D(r(\theta))\vert{} = \vert{}(e^{i\theta}-e^{-i\theta})(e^{-i\theta}-e^{i\theta})\vert{} = \vert{}e^{i\theta}-e^{-i\theta}\vert{}^2 = 4\sin^2\theta$. In the Weyl integration formula:

$$\int_{SL(2,\mathbb{R})} \Theta_\pi(g) f(g)\, dg = \frac{1}{2} \int_A \Theta_\pi(a) |D(a)| O_f(a)\, da + \frac{1}{|W(G,K)|} \int_K \Theta_\pi(k) |D(k)| O_f(k)\, dk.$$



Wait: if $\Theta_{\pi_m}(r(\theta)) = -\operatorname{sgn}(m)\frac{e^{im\theta}}{e^{i\theta}-e^{-i\theta}}$, and you multiply by $|D(r(\theta))| O_f(r(\theta)) = |e^{i\theta}-e^{-i\theta}|^2 O_f(r(\theta))$, then at $2\theta$:

$$|D(\overline{r}(2\theta))| = |e^{2i\theta}-e^{-2i\theta}|^2 = |e^{i\theta}-e^{-i\theta}|^2 |e^{i\theta}+e^{-i\theta}|^2.$$



If $\Phi_f(t)$ were defined as $|D(t)| O_f(t)$, then:
1. In §4.5.4, $\Phi_f(r(\theta)) = 4\sin^2\theta \cdot O_f(r(\theta))$ would *vanish* at $\theta = 0, \pi$ instead of having a jump discontinuity, and near $\theta = \pi/2$, $\Phi_{\overline{f}}(\overline{r}(2\theta)) = |D(\overline{r}(\pi))| O_{\overline{f}}(\overline{r}(\pi))$ would vanish to order 2 ($4\cos^2\theta$ times a singular orbital integral); more importantly, let's check whether Lemma 4.11's proof is internally consistent!
2. Look at the proof of Lemma 4.11 (p. 21): it literally substitutes $\Phi_{\overline{f}}(\overline{r}(2\theta)) = (e^{i\theta}+e^{-i\theta}) \Phi_f(r(\theta))$ into $\int_0^{2\pi} \Theta_{\overline{\pi}}(\overline{r}(2\theta)) \Phi_{\overline{f}}(\overline{r}(2\theta)) \frac{d\theta}{2\pi}$! Algebraically, Lemma 4.11 *is* 100% internally consistent with the Weyl integration formula written in §4.3.3 **IF AND ONLY IF** $\Phi_f(t)$ is defined as $|D(t)| O_f(t)$!


3. Wait—let's check the jump/smoothness claim in **Remark 4.10(1)** and the **Example on p. 21** under $\Phi_f(t) := |D(t)| O_f(t)$!
* Near $\theta = \pi/2$, $r(\pi/2) = w$ is regular elliptic in $SL(2,\mathbb{R})$, so $O_f(r(\theta))$ is smooth near $\theta = \pi/2$, and $\vert{}D(r(\theta))\vert{} = 4\sin^2\theta$ is smooth and equal to $4$ at $\theta = \pi/2$. Thus $\Phi_f(r(\theta)) = \vert{}D(r(\theta))\vert{} O_f(r(\theta))$ is indeed smooth near $\theta = \pi/2$!
* What about $\Phi_{\overline{f}}(\overline{r}(\varphi)) = \vert{}D(\overline{r}(\varphi))\vert{} O_{\overline{f}}(\overline{r}(\varphi))$ as $\varphi \to \pi$ (where $\overline{r}(\pi) = (-I, \pm 1)$ is central/singular)? By Harish-Chandra's theory of orbital integrals on $SL(2,\mathbb{R})$, for a smooth function $\overline{f}$, the signed invariant integral `'F_{\overline{f}}(\overline{r}(\varphi)) = (e^{i\varphi}-e^{-i\varphi}) O_{\overline{f}}(\overline{r}(\varphi)) = 2i\sin\varphi , O_{\overline{f}}(\overline{r}(\varphi))$ has a finite jump discontinuity at $\varphi = \pi$ (proportional to $\overline{f}(\overline{r}(\pi))$), whereas $|D(\overline{r}(\varphi))| O_{\overline{f}}(\overline{r}(\varphi)) = |2\sin\varphi| \cdot |2i\sin\varphi \, O_{\overline{f}}(\overline{r}(\varphi))| = O(|\varphi - \pi|)$ automatically vanishes to first order as $\varphi \to \pi$!
* **Aha! Look at the sign of $\Phi_{\overline{f}}$ in Definition 4.9 and Remark 4.10(2)!**
By definition in §4.3.3, $\Phi_f(t) = |D(t)| O_f(t)$. What happens when we replace $\theta$ by $\theta + \pi$?


* $r(\theta + \pi) = -r(\theta)$. Since $-I$ is central in $SL(2,\mathbb{R})$, if $f(-g) = f(g)$ (even), then $\Phi_f(r(\theta+\pi)) = \Phi_f(r(\theta))$.
* On the cover, $\overline{r}(2(\theta+\pi)) = \overline{r}(2\theta + 2\pi) = \overline{r}(2\theta)(I, -1)$. Since $\overline{f}$ is **genuine**, $O_{\overline{f}}(\overline{r}(2\theta)(I,-1)) = -O_{\overline{f}}(\overline{r}(2\theta))$, while $|D(\overline{r}(2\theta+2\pi))| = |D(\overline{r}(2\theta))|$. Therefore:



$$\Phi_{\overline{f}}(\overline{r}(2(\theta+\pi))) = -\Phi_{\overline{f}}(\overline{r}(2\theta))!$$


* Now check Definition 4.9 (even):

$$\Phi_{\overline{f}}(\overline{r}(2\theta)) = (e^{i\theta}+e^{-i\theta}) \Phi_f(r(\theta)) = 2\cos\theta \, \Phi_f(r(\theta)).$$



Replace $\theta \mapsto \theta + \pi$: the LHS flips sign (since $\overline{f}$ is genuine), and on the RHS $2\cos(\theta+\pi) = -2\cos\theta$ *also* flips sign, forcing $\Phi_f(r(\theta+\pi)) = +\Phi_f(r(\theta))$! This matches Remark 4.10(2)!


* **HOWEVER**, there is a serious realization/existence problem if $\Phi_f(t) = |D(t)| O_f(t)$ vs. Harish-Chandra's `'F_f(t) = (e^{i\theta}-e^{-i\theta}) O_f(r(\theta))$: Look at $\theta \to \pi$ (so $r(\pi) = -I$ is central in $G$, and $\overline{r}(2\pi) = (I,-1)$ is central in $\overline{G}$). For a genuine function $\overline{f}$ with **vanishing hyperbolic orbital integrals**, Harish-Chandra's jump condition at central elements says that `'F_{\overline{f}}(\overline{r}(\varphi)) = 2i\sin\varphi , O_{\overline{f}}(\overline{r}(\varphi))$ is **smooth** across $\varphi = 0, \pi, 2\pi, 3\pi$ (because the jump of `'F` at a central element equals the jump of the hyperbolic orbital integral, which is zero!).
Wait: if `'F_{\overline{f}}(\overline{r}(\varphi)) = 2i\sin\varphi , O_{\overline{f}}(\overline{r}(\varphi))$ is smooth across $\varphi = \pi$, then since $\Phi_{\overline{f}}(\overline{r}(\varphi)) = 4\sin^2\varphi \, O_{\overline{f}}(\overline{r}(\varphi)) = -2i|\sin\varphi|\operatorname{sgn}(\sin\varphi) \, 'F_{\overline{f}}(\overline{r}(\varphi))$, wait:

$$\Phi_{\overline{f}}(\overline{r}(\varphi)) = |2\sin\varphi| \cdot \frac{'F_{\overline{f}}(\overline{r}(\varphi))}{i\operatorname{sgn}(\sin\varphi)}!$$



Look at the Example on p. 21: you construct $\Phi_f(r(\theta)) = \sin(\theta) g(\theta)$. Because $|\sin\varphi|$ has a corner (non-smooth absolute value!) unless $'F_{\overline{f}}(\overline{r}(\pi)) = 0$, note that in the Example on p. 21, for $\theta \in (\pi, 2\pi)$, $\sin\theta < 0$, while $|D(r(\theta))| = 4\sin^2\theta \ge 0$! Wait: if $g(\theta+\pi) = -g(\theta)$ as stated in the Example on p. 21, then $\Phi_f(r(\theta+\pi)) = \sin(\theta+\pi)g(\theta+\pi) = (-\sin\theta)(-g(\theta)) = +\sin\theta g(\theta) = \Phi_f(r(\theta))$, which is fine, **and** near $\theta = \pi/2$, $\varphi = 2\theta$ is near $\pi$: if $\Phi_{\overline{f}}(\overline{r}(\varphi)) = \sin(\varphi) g(\varphi/2)$, notice that $\sin(\varphi)$ changes sign smoothly across $\varphi = \pi$, meaning:



$$O_{\overline{f}}(\overline{r}(\varphi)) = \frac{\Phi_{\overline{f}}(\overline{r}(\varphi))}{|D(\overline{r}(\varphi))|} = \frac{\sin(\varphi) g(\varphi/2)}{4\sin^2\varphi} = \frac{g(\varphi/2)}{4\sin\varphi},$$



so $'F_{\overline{f}}(\overline{r}(\varphi)) = 2i\sin\varphi \, O_{\overline{f}}(\overline{r}(\varphi)) = \frac{i}{2} g(\varphi/2)$, which **is** smooth across $\varphi = \pi$! That's actually completely valid!
*Still*, calling $\Phi_f(t) = |D(t)| O_f(t)$ the "normalized elliptic orbital integral" (Notation table, p. 6, and §4.3.3, p. 17) is nonstandard and potentially confusing, because in §3.1.2 and §4.2.1 the "normalized orbital integral" $F_f$ is defined with $|D|^{1/2}$, and in standard literature (Harish-Chandra, Labesse–Langlands, Adams [Ad2], Bouaziz) the normalized orbital integral $\Phi_f$ or $F_f$ is defined with $|D(t)|^{1/2}$ (or the Weyl denominator $\Delta(t)$), in which case the Weyl integration formula has $|D(t)|^{1/2} \Theta_\pi(t) F_f(t)$. Explicitly alerting the reader in §4.3.3 that $\Phi_f(t) = |D(t)| O_f(t)$ uses the full first power $|D(t)|$ (unlike $F_f$ on $A$, which uses $|D(a)|^{1/2}$) will prevent readers from thinking there is a typo in the Weyl integration formula.










4. **Check of the Verification Requests (`Remark 2026.n`):**
As referee, I checked the mathematical content of the key `2026.n` remarks so you can either upgrade them or refine them:
* **Remark 2026.5 (`rem26:A00-norm`, Lemma 5.6, p. 31–32):** There is a subtle point to verify in step (ii) of the proof of Lemma 5.6!


* In §4.7.2 (iii), $r_+(h(a), \zeta)\phi(x) = \zeta |a|^{1/2} \omega(a) \phi(ax)$.


* Be careful about **left vs. right actions and Jacquet modules**! The Jacquet module $V_N = V / V(N)$ carries a representation of $\overline{A}$ via $r_+(h(a),\zeta)$. Since $r_+(n(b),1)\phi(x) = \psi(bq(x))\phi(x)$, for $\phi \in \mathcal{S}(F)_+$, does $\phi \mapsto \phi(0)$ factor through $V_N$? Wait: $(r_+(n(b),1)\phi - \phi)(0) = (\psi(bq(0)) - 1)\phi(0) = 0$ since $q(0) = 0$! Yes! So $\ell(\phi) = \phi(0)$ is indeed an $N(F)$-invariant functional on $r_+$!
* On this functional $\ell$, how does $\overline{A}$ act? For $t = (h(a), \zeta)$, $(t \cdot \ell)(\phi)$ or $\ell(r_+(t)\phi) = \zeta |a|^{1/2} \omega(a) \phi(0) = \zeta |a|^{1/2} \omega(a) \ell(\phi)$.


* By Frobenius reciprocity $\operatorname{Hom}_{\overline{G}}(r_+, \operatorname{Ind}_{\overline{B}}^{\overline{G}}(\delta_B^{1/2}\overline{\chi})) \cong \operatorname{Hom}_{\overline{B}}(r_+, \delta_B^{1/2}\overline{\chi})$, we need $\delta_B^{1/2}(h(a)) \overline{\chi}(h(a),\zeta) = \zeta |a|^{1/2} \omega(a)$. Since $\delta_B(h(a)) = |a|^2$ (equation (2.6)), $\delta_B^{1/2}(h(a)) = |a|$, so $\overline{\chi}(h(a),\zeta) = \zeta |a|^{-1/2} \omega(a)$, giving $|\overline{\chi}(a(x),1)| = |x|^{-1/2}$.


* **Everything in step (ii) of Lemma 5.6 is completely accurate!** And in step (iii), Gelbart–Jacquet [GJ2] indeed gives $|s_v| < 1/4$ (in fact Kim–Sarnak gives $7/64$, though [GJ2] already gives $< 1/4$ over any number field via the Rankin–Selberg of $\mathrm{Ad}\,\Pi$), so $|2s_v| < 1/2$, strictly smaller than $1/2$. Thus **Lemma 5.6 is completely solid.**




* **Remark 2026.6 (`rem26:nonexist`, Theorem 5.7, p. 32–33):** Let us check (W), (GJ), and (JS) carefully!
* **(W):** In Waldspurger [Wa1, Wa2] (and [PS]), for $\overline{\pi}' \subset \mathcal{A}_{00}$ and fixed additive character $\psi$, $\sigma = \mathrm{Wald}_\psi(\overline{\pi}')$ is indeed an automorphic representation of $PGL(2,\mathbb{A})$ whose local component at unramified places (where $\overline{\pi}'_v$ is the spherical constituent of $I_A(\chi_{\psi_v}\mu_v)$) is the unramified representation $\pi(\mu_v, \mu_v^{-1})$ of $PGL(2, k_v)$.


* **WAIT A SECOND! Check whether $\sigma = \mathrm{Wald}_\psi(\overline{\pi}')$ is ALWAYS CUSPIDAL on $PGL(2,\mathbb{A})$!**
Let us be **very careful** here! Could $\overline{\pi}' \subset \mathcal{A}_{00}$ lift via $\mathrm{Wald}_\psi$ to an **Eisenstein / non-cuspidal** representation of $PGL(2,\mathbb{A})$?
Let's recall Waldspurger's theorem ([Wa1, Théorème 1 & Proposition 26], [PS, Theorem 2]):
For $\overline{\pi}' \subset \mathcal{A}_{00}$ (i.e., a genuine cuspidal representation **orthogonal to all elementary theta series $\Theta_0$**), $\mathrm{Wald}_\psi(\overline{\pi}')$ is **ALWAYS a cuspidal automorphic representation of $PGL(2,\mathbb{A})$**! Why? Because the theta lift from $\overline{SL(2)}$ to $PGL(2) = SO(2,1)$ can fail to be cuspidal *only* if its constant term along the Borel of $SO(2,1)$ is nonzero, and by Rallis's tower property, the constant term of the $(1,2)$-theta lift is the $(1,0)$- or $(1,1)$-theta lift, which corresponds precisely to pairing with one-dimensional theta series $\Theta_0$! (Equivalently, in [Wa1], $\mathcal{A}_{00}$ is *defined* as the orthogonal complement of the elementary theta series, and Waldspurger proves $\mathrm{Wald}_\psi$ maps irreducible subspaces of $\mathcal{A}_{00}$ into cuspidal automorphic representations of $PGL(2,\mathbb{A})$!)
* **WAIT A SECOND! Check a SECOND potential edge case in the proof of Theorem 5.7:**
Look at the lines after (JS) on page 33:
*"Since $\sigma$ and $\Pi$ are cuspidal, $L^{S'}(s, \sigma \times \sigma^\vee)$ and $L^{S'}(s, \Pi \times \Pi^\vee)$ have simple poles at $s=1$ by (JS). By (GJ), $L^{S'}(s, \mathrm{Ad}\,\sigma)$ and $L^{S'}(s, \mathrm{Ad}\,\Pi)$ are holomorphic at $s=1$, so the right side of (5.6) is holomorphic at $s=1$."*
**HOLD ON! Is $L^{S'}(s, \mathrm{Ad}\,\Pi)$ ALWAYS holomorphic at $s=1$ when $\Pi$ is a dihedral/CM cuspidal representation?!**
Let us check this right now! This is a crucial point in automorphic $L$-functions:
Suppose $\Pi$ is a cuspidal automorphic representation of $GL(2,\mathbb{A})$ of **CM / dihedral type**, i.e., $\Pi \cong \Pi \otimes \eta$ for a nontrivial quadratic Hecke character $\eta$ of $k^\times \backslash \mathbb{A}^\times$!
By Gelbart–Jacquet [GJ2, Theorem 9.3]:


* $\mathrm{Ad}(\Pi)$ is cuspidal on $GL(3,\mathbb{A})$ if and only if $\Pi$ is *not* dihedral ($\Pi \not\cong \Pi \otimes \eta$ for all $\eta \neq 1$).
* If $\Pi$ *is* dihedral ($\Pi = \mathrm{Ind}_E^k \theta$ for a quadratic extension $E/k$ with quadratic character $\eta = \eta_{E/k}$, so $\Pi \cong \Pi \otimes \eta$), then $\mathrm{Ad}(\Pi)$ is the isobaric sum:

$$\mathrm{Ad}(\Pi) = \eta \boxplus \tau,$$



where $\eta \neq 1$ is a **nontrivial** quadratic Hecke character of $GL(1,\mathbb{A})$ and $\tau$ is a unitary representation of $GL(2,\mathbb{A})$ (either cuspidal, or $\eta_1 \boxplus \eta_2$ for two *nontrivial* quadratic characters $\eta_1, \eta_2$ if $\Pi$ is biquadratic/tetrahedral—wait: for $GL(2)$, $\mathrm{Sym}^2(\mathrm{Ind}_E^k \theta) = \eta_{E/k} \boxplus \mathrm{Ind}_E^k(\theta/\theta^\sigma)$; if $\theta/\theta^\sigma$ itself factors through $N_{E/k}$, i.e., $\theta^\sigma/\theta = \chi \circ N_{E/k}$, then $\mathrm{Ind}_E^k(\chi \circ N_{E/k}) = \chi \boxplus \chi\eta_{E/k}$. Could $\chi = 1$? If $\theta^\sigma = \theta$, then $\theta$ factors through $N_{E/k}$, so $\Pi = \mathrm{Ind}_E^k \theta$ is **NOT cuspidal**!).
* Let us check whether $1$ (the trivial character of $GL(1)$) can *ever* be an isobaric summand of $\mathrm{Ad}(\Pi)$ when $\Pi$ is cuspidal!
By $L^{S'}(s, \Pi \times \Pi^\vee) = \zeta_k^{S'}(s) L^{S'}(s, \mathrm{Ad}\,\Pi)$:
Since $\Pi$ is **irreducible cuspidal** on $GL(2,\mathbb{A})$, by Jacquet–Shalika (JS), $L^{S'}(s, \Pi \times \Pi^\vee)$ has a **simple** pole (order 1!) at $s=1$!
Meanwhile, $\zeta_k^{S'}(s)$ *already* has a simple pole (order 1!) at $s=1$!
Therefore, $L^{S'}(s, \mathrm{Ad}\,\Pi) = \frac{L^{S'}(s, \Pi \times \Pi^\vee)}{\zeta_k^{S'}(s)}$ is **ALWAYS holomorphic (and nonzero!) at $s=1$**, even in the dihedral/CM case (because $\eta \neq 1$, so $L^{S'}(s, \eta)$ is holomorphic at $s=1$)!


* And on the LHS of (5.6): even if $\mathrm{Ad}(\Pi) = \eta \boxplus \tau$ or $\eta_1 \boxplus \eta_2 \boxplus \eta_3$ (for distinct nontrivial quadratic characters $\eta_i$, when $\theta/\theta^\sigma$ has order 2), $\mathrm{Ad}(\Pi)$ is still an isobaric sum of unitary cuspidal representations $\tau_1, \dots, \tau_r$, and $\prod_{i,j} L^{S'}(s, \tau_i \times \tau_j^\vee)$ has a pole of order $\sum_i m_i^2 \ge r \ge 1$ at $s=1$ (in fact order 1 if non-CM, order 2 if generic CM, order 3 if biquadratic CM), whereas the RHS of (5.6) is **always holomorphic** at $s=1$!
* **Verdict on Theorem 5.7:** That proof is **rock-solid, remarkably slick, and completely unconditional on Ramanujan or non-CM hypotheses!** You might add one brief parenthetical remarking why $L^{S'}(s, \mathrm{Ad}\,\Pi)$ is holomorphic at $s=1$ ("since both $L^{S'}(s, \Pi\times\Pi^\vee)$ and $\zeta_k^{S'}(s)$ have simple poles at $s=1$"), which makes that deduction immediately self-contained from (GJ) and (JS)!




* **Remark 2026.8 (`rem26:where-fails`, §5.4, p. 36):** Let's check the intertwining scalar $\overline{c}(s,\mu)$ on the cover!
* In §5.4 (p. 35), you write:

$$\overline{c}(s,\mu) = \frac{L(2s, \mu^2)}{L(1+2s, \mu^2)}.$$



Let us verify the exponent $2s$ vs. $s$!
Suppose the genuine principal series is $I_A(\chi_\psi \mu |\cdot|^s)$, so at an odd unramified place $v$, the unramified parameter is $t'_v = \mu_v(\varpi_v) |\varpi_v|_v^s = \mu_v(\varpi_v) q_v^{-s}$.
By Gelbart–Sally [GS, Theorem 1] and Gelbart [Ge2, Proposition 3.12 / Theorem 3.13] (and Moen [Mo1]), the unramified local factor of the intertwining operator on $I_A(\chi_{\psi_v} \mu_v |\cdot|^s)$ is:

$$\frac{1 - \mu_v(\varpi_v)^2 q_v^{-2s-1}}{1 - \mu_v(\varpi_v)^2 q_v^{-2s}} = \frac{L_v(2s, \mu_v^2)}{L_v(2s+1, \mu_v^2)}.$$



Check at the pole! As stated in Chapter 3 (§3.2.2–3.2.3), the complementary series for $I_A(\chi_\psi |\cdot|^s)$ runs over $0 < s < 1/2$ and reduces at $s = 1/2$. Indeed, $L(2s, \mu^2)$ has its pole at $2s = 1 \iff s = 1/2$ when $\mu^2 = 1$ (i.e., $\mu$ is quadratic)!


* **Everything in §5.4's formula $\overline{c}(s,\mu) = \frac{L(2s,\mu^2)}{L(1+2s,\mu^2)}$ matches the normalization $I_A(\chi_\psi \mu |\cdot|^s)$ of Chapter 3!**







---

#### B. Specific Mathematical Inaccuracies and Glitches to Fix

1. **Formula (2.2) (`eq:beta1`, Page 7) and Appendix A (Page 40):**
* Look at the definition of $v(z, g)$ in §2.1 (p. 7):

$$v(z,g) = \begin{cases} 1, & c \neq 0,\ F \neq \mathbb{R}, \\ (z, d)_2, & c = 0, \end{cases} \quad \text{and } v = 1 \text{ if } F = \mathbb{R}.$$


* **Wait:** If $F = \mathbb{R}$ and $c = 0$, the displayed piece says $(z, d)_2$ while the text after it says "and $v = 1$ if $F = \mathbb{R}$". Even worse: if $v = 1$ identically when $F = \mathbb{R}$, is $\beta_1$ in (2.2) actually a **2-cocycle** on $GL_2(\mathbb{R})$?!
Let's test this on diagonal matrices in $GL_2(\mathbb{R})$! Take $g_1 = d(1, -1)$ and $g_2 = d(-1, 1)$ in $GL_2(\mathbb{R})$.


* $p(g_1) = d(1, -1)^{-1} d(1, -1) = I_2$, $\det g_2 = 1$? Wait: $\det d(-1,1) = -1$.
* Take $g_1 = d(-1, 1)$ (so $\det g_1 = -1$, $p(g_1) = d(-1, -1) = -I_2$) and $g_2 = d(1, -1)$ (so $\det g_2 = -1$, $p(g_2) = I_2$).
* With $v = 1$: $\beta_1(g_1, g_2) = \beta((-I_2)^{d(1,-1)}, I_2) = \beta(-I_2, I_2) = 1$.
* Now swap $g_1$ and $g_2$: $g_2 g_1 = d(-1, -1) = g_1 g_2$ (diagonal matrices commute in $GL_2(\mathbb{R})$!). Let's check $g_1 = d(1, -1), g_2 = d(1, -1)$ vs $g_1 = d(-1, 1), g_2 = d(-1, 1)$:
Take $h_1 = d(-1, 1)$, $h_2 = d(1, -1)$, $h_3 = d(-1, 1)$. Check the 2-cocycle identity $\beta_1(h_1, h_2) \beta_1(h_1 h_2, h_3) = \beta_1(h_1, h_2 h_3) \beta_1(h_2, h_3)$:
* $p(h_1) = -I_2$, $p(h_2) = I_2$, $p(h_3) = -I_2$.
* $h_1 h_2 = -I_2 \in SL_2(\mathbb{R})$, so $\det(h_1 h_2) = 1$, $p(h_1 h_2) = -I_2$.
* $h_2 h_3 = -I_2 \in SL_2(\mathbb{R})$, so $\det(h_2 h_3) = 1$, $p(h_2 h_3) = -I_2$.
* If $v \equiv 1$:
* LHS: $\beta_1(h_1, h_2) \beta_1(-I_2, h_3) = \beta(-I_2, I_2) \cdot \beta(-I_2, -I_2) = 1 \cdot (-1,-1)_{\mathbb{R}} = -1$.
* RHS: $\beta_1(h_1, -I_2) \beta_1(h_2, h_3) = \beta(-I_2, -I_2) \cdot \beta(I_2, -I_2) = (-1,-1)_{\mathbb{R}} \cdot 1 = -1$.


* Now test $h_1 = w = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \in SL_2(\mathbb{R})$, $h_2 = d(1, -1)$, $h_3 = d(1, -1)$ (so $h_2 h_3 = I_2$):
* Cocycle identity requires: $\beta_1(w, h_2) \beta_1(w h_2, h_2) = \beta_1(w, I_2) \beta_1(h_2, h_2)$.
* Since $p(h_2) = I_2$, RHS is $\beta(w, I_2) \beta(I_2, I_2) = 1 \cdot 1 = 1$.
* On LHS: $p(w) = w$, $w^{d(1,-1)} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = -w$, so $\beta_1(w, h_2) = \beta(-w, I_2) v(-1, w)$. Note $\beta(-w, I_2) = (x(-w)/x(-w), x(-w)/x(I_2)) = (1, -1) = 1$.
* Next, $w h_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $\det(w h_2) = -1$, so $p(w h_2) = d(1,-1) \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = -w$. Then $p(w h_2)^{d(1, \det h_2)} = (-w)^{d(1,-1)} = w$. So $\beta_1(w h_2, h_2) = \beta(w, I_2) v(-1, -w) = 1 \cdot v(-1, -w)$.
* Wait: now test $h_1 = d(1,-1)$, $h_2 = d(-1,-1) = -I_2$, $h_3 = d(1,-1)$!
* $h_1 h_2 = d(-1, 1)$, $h_2 h_3 = d(-1, 1)$.
* LHS $= \beta_1(d(1,-1), -I_2) \beta_1(d(-1,1), d(1,-1)) = [\beta(I_2, -I_2) v(1, I_2)] \cdot [\beta(-I_2, I_2) v(-1, -I_2)] = v(-1, -I_2)$.
* RHS $= \beta_1(d(1,-1), d(-1,1)) \beta_1(-I_2, d(1,-1)) = [\beta(I_2, -I_2) v(-1, I_2)] \cdot [\beta(-I_2, I_2) v(-1, -I_2)] = v(-1, I_2) v(-1, -I_2)$.
* Now test $h_1 = n(1)$ or $h_1 = w$, $h_2 = d(1,-1)$, $h_3 = w$!
* $h_1 h_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $p(h_1 h_2) = -w$, $\det h_3 = 1$, so $\beta_1(w h_2, w) = \beta(-w, w) v(1, -w)$. Here $(-w)w = I_2$, $x(-w) = -1, x(w) = 1, x(I_2) = 1$, so $\beta(-w, w) = (1/-1, 1/1) = (-1, 1) = 1$. And $\beta_1(w, h_2) = \beta(-w, I_2) v(-1, w) = v(-1, w)$. So **LHS $= v(-1, w)$**.
* $h_2 h_3 = d(1,-1) w = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$, $\det(h_2 h_3) = -1$, $p(h_2 h_3) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = w$.
* $\beta_1(h_2, w) = \beta(I_2, w) v(1, I_2) = 1$.
* $\beta_1(w, h_2 w) = \beta(w^{d(1,-1)}, p(h_2 w)) v(-1, w) = \beta(-w, w) v(-1, w) = 1 \cdot v(-1, w)$. Wait: what if $h_1 = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$ or $h_1 = a(-1) = -I_2$, $h_2 = w$, $h_3 = d(1,-1)$?
* $h_1 h_2 = -w$, $\beta_1(-I_2, w) = \beta(-I_2, w) = (-1/-1, -1/1) = (1,-1) = 1$. $\beta_1(-w, d(1,-1)) = \beta(w, I_2) v(-1, -w) = v(-1, -w)$. So **LHS $= v(-1, -w)$**.
* $h_2 h_3 = w d(1,-1) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $p(h_2 h_3) = -w$, $\det(h_2 h_3) = -1$.
* $\beta_1(w, d(1,-1)) = \beta(-w, I_2) v(-1, w) = v(-1, w)$.
* $\beta_1(-I_2, h_2 h_3) = \beta((-I_2)^{d(1,-1)}, -w) v(-1, -I_2) = \beta(-I_2, -w) v(-1, -I_2)$. Now compute $\beta(-I_2, -w)$: $(-I_2)(-w) = w$, $x(-I_2) = -1$, $x(-w) = -1$, $x(w) = 1$. So $\beta(-I_2, -w) = (1/(-1), 1/(-1))_2 = (-1, -1)_2$!
* Look at **LHS = RHS**:

$$v(-1, -w) = (-1, -1)_2 \cdot v(-1, w) \cdot v(-1, -I_2)!$$


* **BINGO!** Look at what happens over $F = \mathbb{R}$ (or *any* field with $(-1,-1)_2 = -1$, including $F = \mathbb{Q}_2$ or $\mathbb{R}$)!
* Over $F \neq \mathbb{R}$: $c(-w) = -1 \neq 0$, $c(w) = 1 \neq 0$, so your formula gives $v(-1, -w) = 1$ and $v(-1, w) = 1$, while $c(-I_2) = 0, d(-I_2) = -1$, so $v(-1, -I_2) = (-1, -1)_2$! Thus RHS $= (-1,-1)_2 \cdot 1 \cdot (-1,-1)_2 = 1 = $ LHS!
* **Over $F = \mathbb{R}$**: $(-1,-1)_{\mathbb{R}} = -1$, so if you set $v \equiv 1$ when $F = \mathbb{R}$, then **LHS $= +1$ while RHS $= (-1,-1)_{\mathbb{R}} \cdot 1 \cdot 1 = -1$! So $\beta_1$ is NOT a 2-cocycle on $GL_2(\mathbb{R})$ if $v = 1$!**
* Why did that happen? Because in Gelbart [Ge2, §2.1, p. 19] and Kubota, $v(z, g) = 1$ for $c \neq 0$ and $(z, d)_2$ for $c = 0$ works **uniformly for ALL local fields $F$ (including $F = \mathbb{R}$)**! Setting $v=1$ for $F=\mathbb{R}$ was a copy-error in the 1995 draft (confusing $s_v = 1$ at $F=\mathbb{R}$ with $v = 1$ at $F=\mathbb{R}$)! Removing the exception "$F \neq \mathbb{R}$" and "and $v=1$ if $F=\mathbb{R}$" fixes the 2-cocycle completely!
















* Also in Appendix A (p. 40), in the 1995 proof of Remark 2026.9, the text writes $\beta(r, k)$ and $\beta(rk, r^{-1})$ for $r = \operatorname{diag}(r_1, r_2) \in GL(2,F)$ instead of $\beta_1(r, k)$ and $\beta_1(rk, r^{-1})$ (and writes $(r, \zeta)^{-1} = (r^{-1}, (r_1,r_2)_2 \zeta^{-1})$, whereas under $\beta_1$, $\beta_1(r, r^{-1}) = \beta(I_2, I_2) v(r_1^{-1}r_2^{-1}, d(1,1)) = 1$? Wait: $p(r) = d(r_1, r_1^{-1})$! So $d$ of $p(r)$ is $r_1^{-1}$, giving $\beta_1(r, r^{-1}) = (r_1, r_1) (r_1 r_2, r_1) = (r_1, r_2)$ — good!). Still, writing $\beta_1$ instead of $\beta$ in those three lines on p. 40 avoids confusion since $\beta$ was only defined on $SL_2(F)$.




2. **Section 4.7.2 & 4.7.3 (Weil Representation Formulas, Pages 23–26):**
* Look at §4.7.2 (p. 23):

$$\text{"We define the Weil representation } r_\epsilon = r_{\psi, q, \epsilon} \text{ of } \overline{G(F)} \text{ on } L^2(F)_\epsilon \text{ by... (ii) } r_\epsilon(w,\zeta)\phi(x) = \zeta \cdot \frac{1}{2} \gamma(q) (\hat{\phi}_q(x) + \epsilon \hat{\phi}_{-q}(x))\text{"}$$



Wait: if $\phi \in L^2(F)_\epsilon$, i.e., $\phi(-y) = \epsilon \phi(y)$, then:

$$\hat{\phi}_{-q}(x) = \int_F \phi(y) \psi(-2qxy)\, dy = \int_F \phi(-y) \psi(2qxy)\, dy = \epsilon \hat{\phi}_q(x)!$$



So $\frac{1}{2}(\hat{\phi}_q(x) + \epsilon \hat{\phi}_{-q}(x)) = \frac{1}{2}(\hat{\phi}_q(x) + \epsilon^2 \hat{\phi}_q(x)) = \hat{\phi}_q(x)$! That's why $r_\epsilon$ *automatically* agrees with the restriction of $r$ to $L^2(F)_\epsilon$ (no need to "assume" it in the line *"We will assume that $r_\epsilon$ agrees with the restriction of $r$ to $L^2(F)_\epsilon$"* on p. 23—it's a 1-line identity!).


* **HOWEVER, look at the sign error in $k_\epsilon(x,y)$ and $k_\epsilon(x,x)$ at the top of page 24!**
At the bottom of page 23, you derived:

$$r_\epsilon(g,1)\phi(x) = (-c,-1)|c|^{-1/2}\omega(-c)\gamma(q)\, \psi\!\left(\frac{a}{c}q(x)\right) \int_F \phi(y) \psi\!\left(\frac{d}{c}q(y)\right) \psi_q\!\left(-\frac{2}{c}xy\right) dy.$$



Symmetrizing $\psi_q(-\frac{2}{c}xy)$ for $\phi \in L^2(F)_\epsilon$ ($\phi(-y) = \epsilon \phi(y)$) replaces $\psi_q(-\frac{2}{c}xy)$ by:

$$\frac{\psi_q(-\frac{2}{c}xy) + \epsilon \psi_q(\frac{2}{c}xy)}{2} = \frac{\psi_{-q}(\frac{2}{c}xy) + \epsilon \psi_q(\frac{2}{c}xy)}{2}.$$



Now set $y = x$ to compute $k_\epsilon(x,x)$, using $q(x) = qx^2$:
* First term in numerator: $\psi\!\left(\frac{a+d}{c} qx^2\right) \psi_{-q}\!\left(\frac{2}{c} x^2\right) = \psi\!\left(\frac{a+d-2}{c} q x^2\right) = \psi_q\!\left(\frac{a+d-2}{c} x^2\right) = \psi_{-q}\!\left(-\frac{a+d-2}{c} x^2\right)$. (Matches your formula!)
-Wait: now look at the **Gaussian integral on page 25** and **Proposition on page 26**:
* On page 25, you set $\tau(x) = \exp(\pi i q x) = \psi_q(x)$, and write:

$$\int_{\mathbb{R}} \tau_a(x^2)\, d_\tau x = |a|^{-1/2} \exp\!\left(\frac{\pi i}{4} \operatorname{sgn}(q)\right).$$



**STOP AND CHECK THE SIGN OF $a$!**
By Lemma 4.16, $\int_{\mathbb{R}} \exp(\pi i q a x^2)\, d_L x = \exp\!\left(\frac{\pi i}{4} \operatorname{sgn}(qa)\right) |qa|^{-1/2}$!
Since $d_\tau x = |q|^{1/2} d_L x$, we get:

$$\int_{\mathbb{R}} \tau_a(x^2)\, d_\tau x = |a|^{-1/2} \exp\!\left(\frac{\pi i}{4} \operatorname{sgn}(qa)\right) = |a|^{-1/2} \gamma(qa), \quad \text{NOT } |a|^{-1/2} \gamma(q)!$$



Look at what happened when $a < 0$: your formula on p. 25 dropped $\operatorname{sgn}(a)$ inside $\exp(\frac{\pi i}{4} \operatorname{sgn}(qa))$!
* Because of that dropped $\operatorname{sgn}(a)$, look at the display right below it on page 25:

$$\gamma(q) \int_{\mathbb{R}} \left(\psi_{-q}\!\left(-\frac{a+d-2}{c}x^2\right) + \epsilon \psi_q\!\left(\frac{a+d+2}{c}x^2\right)\right) d_\tau x = \gamma(q)\gamma(-q)\left|\frac{a+d-2}{c}\right|^{-1/2} + \epsilon \gamma(q)^2 \left|\frac{a+d+2}{c}\right|^{-1/2}.$$



Let's test this! In the first term, the phase is $\psi_{-q}(-\frac{a+d-2}{c} x^2) = \psi(q \frac{a+d-2}{c} x^2)$! For $g = r(\theta)$, $a = d = \cos\theta$, $c = \sin\theta$, so:

$$\frac{a+d-2}{c} = \frac{2(\cos\theta - 1)}{\sin\theta} = -2\tan(\theta/2), \qquad \frac{a+d+2}{c} = \frac{2(\cos\theta + 1)}{\sin\theta} = 2\cot(\theta/2).$$



Notice that for $0 < \theta < \pi$, $\frac{a+d-2}{c} = -2\tan(\theta/2) < 0$ is **NEGATIVE**, so $\operatorname{sgn}(q \frac{a+d-2}{c}) = -\operatorname{sgn}(q)$, which happens to give $\gamma(-q)$ ONLY when $0 < \theta < \pi$! When $-\pi < \theta < 0$ (or $\pi < \theta < 2\pi$), $\frac{a+d-2}{c} > 0$, so its Gaussian integral gives $\gamma(+q)$, NOT $\gamma(-q)$! And similarly for $\frac{a+d+2}{c} = 2\cot(\theta/2)$, which is positive for $0 < \theta < \pi$ (giving $\gamma(q)$) **but negative for $\pi/2 < \theta < \pi$**!
Wait: check $\theta \in (\pi/2, \pi)$! For $\theta = 2\pi/3 \in (\pi/2, \pi)$, $\cot(\theta/2) = \cot(\pi/3) = 1/\sqrt{3} > 0$ (still positive!), whereas for $\theta \in (\pi, 2\pi)$, $\cot(\theta/2) < 0$!
That is **why** in Remark 4.20 (p. 26) you noticed that your Corollary only agreed with Adams's formula for $0 < \theta < \pi$ (and had to invoke conjugation by $w$ for $-\pi < \theta < 0$), and **why** Adams's formula in Remark 4.21 has $\cos(\theta/2)$ and $\sin(\theta/2)$ *without* absolute values (changing signs across $\theta = \pi, 2\pi$) whereas your Corollary on p. 26 had $|\sin(\theta/2)|$ and $|\cos(\theta/2)|$!
* Similarly, in the **Proposition on page 26**, $\kappa(\psi_\alpha)$ with $\alpha = \frac{a+d-2}{c}q$: for $\psi_{-q}(-\frac{a+d-2}{c}x^2) = \psi(q\frac{a+d-2}{c}x^2) = \psi_\alpha(x^2)$, the prefactor in front of $\kappa(\psi_\alpha)$ is simply $\gamma(q)$ (NOT $\gamma(q)\gamma(-q) = 1$!), because $\gamma(-q)$ came from wrongly evaluating the archimedean Gaussian integral in the p-adic formula! Check: in $k_\epsilon(x,x)$ on p. 24, there is a single factor of $\gamma(q)$ outside both terms; integrating over $F$ gives $\frac{1}{2}\gamma(q)\bigl(\kappa(\psi_\alpha) + \epsilon \kappa(\psi_\beta)\bigr)$ (times $(-c,-1)\vert{}c\vert{}^{-1/2}\omega(-c)$, with $dx = d_{\psi_q}x$). There is no $\vert{}q\vert{}^{1/2}$ or $\gamma(-q)$ in the p-adic integral of $k_\epsilon(x,x)\, d_{\psi_q}x$!
* Since §4.7.3 ("Integrating the kernel") is not used anywhere else in the monograph (only formula (iii) of §4.7.2 is used in Lemma 5.6, and §4.7.4 uses Lemma 4.11 rather than §4.7.3), you should either fix $\gamma(qa)$ on p. 25 and the Proposition on p. 26, or label the Proposition and Corollaries of §4.7.3 as `Remark 2026.n [1995 heuristic calculation]` so no reader cites the faulty sign/prefactor in the p-adic/real Weil character formula.








3. **Minor Mathematical Slips:**
* **Page 5 (`local_formulas_check.py`) & Lemma 2.2 (p. 7):** Check Lemma 2.2: $(g,\varsigma)^{-1} = (g^{-1}, (a,a)_2 \varsigma^{-1})$ for $g = \operatorname{diag}(a, a^{-1})$. Let's verify: $x(g) = a^{-1}$, $x(g^{-1}) = a$, $x(I_2) = 1$, so $\beta(g, g^{-1}) = (1/a^{-1}, 1/a)_2 = (a, a^{-1})_2 = (a, a)_2$. Correct!


* **Page 10, Lemma in §3.1.2:** In $\Theta_\pi(x) = \frac{\chi(a)+\chi(a^w)}{\vert{}a_1-a_2\vert{}}$ for $x = a^g$, $a \in \overline{A(F)}$, you did not specify how $a_1, a_2$ relate to $a$ until 8 lines later ("for $a$ over $\operatorname{diag}(a_1,a_2)$"). Also, strictly speaking, $\vert{}D(a)\vert{}^{1/2} = \vert{}a_1 - a_2\vert{} / \vert{}a_1 a_2\vert{}^{1/2} = \vert{}a_1 - a_2\vert{}$ since $a_1 a_2 = 1$ in $SL(2)$—stating "where $a$ lies over $\operatorname{diag}(a_1, a_2) \in A(F)$" inside the lemma makes it self-contained.


* **Page 18, §4.3.4 (`S_0 f(\chi)`):** Display (4.9) writes:

$$\mathcal{H}(\overline{G(F)}, K)_{gen} \to \mathcal{A}_{cl.fcn}(PGL(2, \mathbb{C})), \quad f \mapsto S_0 f(\chi) = \operatorname{tr} I_A(\chi)(f).$$



Wait: on the genuine Hecke algebra of $\overline{G(F)}$, $\chi$ is a *genuine* unramified character of $\overline{A(F)}$, and as explained in §5.4 ("Diagnosis", p. 36), the dual group of $\overline{SL(2)}$ is $SL(2,\mathbb{C})$ (though under the *direct* correspondence it identifies with class functions on the dual group $PGL(2,\mathbb{C})$ of $SL(2)$). Clarify whether $\mathcal{A}_{cl.fcn}(PGL(2,\mathbb{C}))$ is meant via the identification of Lemma 4.6.


* **Page 18, Display (4.10):** In $Sf(a) = \delta(a)^{1/2} \int_{N(F)} f(an)\, dn$, note that $a \in \overline{A(F)}$ and $n$ is embedded via $n \mapsto (n, 1) \in \overline{G(F)}$, and in (4.11) the target is written $\mathcal{H}(\overline{A(F)}, K \cap A(F))^W_{gen}$ whereas 6 lines below it is more accurately written $\mathcal{H}(\overline{A(F)}, \kappa(K \cap A(F)))^W_{gen}$. Make (4.11) use $\kappa(K \cap A(F))$ as well.


* **Page 20, §4.5.2 (Gelbart's parameterization):** Both tables list 4 rows of representations and say *"These representations exhaust $\Pi(\overline{SL(2,\mathbb{R})})_{ds}$. Another parameterization is as follows:"*. Note that in Gelbart [Ge2, p. 75], those two 4-row tables are dual/intertwined realizations (for $\lambda = \frac{k}{2}-1 > 0$ vs. $\lambda = -\frac{k}{2}+1 < 0$ in the principal series $\rho(\lambda, \tau)$), and **neither** table's notation ($B_\pm^{\pm 1/2}(\pm k/2)$) is ever used again in §4.5.4 (which instead introduces $\overline{\pi}_{k/2}^\pm$ directly by $\overline{K}$-types!). Either briefly connect $B_\pm^{\pm 1/2}$ to $\overline{\pi}_{k/2}^\pm$ or cut the unused second table to streamline §4.5.


* **Page 42, Appendix B (§B.1.2, `L^2(M(k)\backslash M(\mathbb{A})^1)_\chi`):** Item 3 on page 42 reads: *"$\psi(amk)$, as a function of $m \in M$, belongs to $L^2(M(k)\backslash M(\mathbb{A})^1)_{cusp,\chi}$"* — that should be **$m \in M_1(k)\backslash M_1(\mathbb{A})^1$** and **$L^2(M_1(k)\backslash M_1(\mathbb{A})^1)_{cusp,\chi}$** (since $P_1 = M_1 N_1 \subset P$, as in item 1 two lines above!).


* **Page 43, Lemma B.2:** *"For $G=SL(2)$, each $(G,\pi) \in \chi \in \mathcal{X}$ is unramified. Moreover, $(A,\mu) \in \chi \in \mathcal{X}$ is unramified if and only if $\mu^w \neq \mu$."* Be careful with terminology! Elsewhere in the book, "unramified" means $K_v$-spherical! Here, in Arthur's terminology ([A2, A3]), "unramified" means *unramified in the sense of Weyl group stabilizer* ($W(\mathfrak{a}_M)_{\text{reg}}$, i.e., $\mu^w \neq \mu$). Add "(in Arthur's sense, i.e., trivial Weyl stabilizer)" so the reader does not confuse it with local sphericality!





---

### 3. Readability, Structure, and Exposition

#### Strengths

* **Chapter 1 (Introduction) and Chapter 5 (Global consequences)** are exceptionally clear, well-organized, and engaging. In particular, **§1.1 (Motivation)**, **§5.3 (The Satake correspondence is not global)**, and **§5.4 (Where the global comparison fails)** do a masterful job explaining *why* the naive geometric intuition ("$\overline{SL(2)}$ is a cover of $SL(2)$, so compare orbital integrals over the same elements of $SL(2)$") works on the split torus and fails on anything involving the root/coroot.


* **Running Example ($\Delta$ of weight 12 vs. weight $13/2$):** Carrying Ramanujan's $\Delta$ function through §§1.1, 1.2, 5.1, 5.3, 5.6, and 5.7 anchors the abstract adelic machinery in concrete classical modular forms and greatly aids readability.


* **Notation Table (§1.6) and Glossary:** Both are accurate, concise, and helpful for non-specialists or graduate students.



#### Structural and Stylistic Suggestions for Readability

1. **Harmonize the Voice Between Chapters 1 & 5 and Chapters 2–4:**
* Chapters 1 and 5 read like a modern, cohesive 2026 research monograph, whereas parts of Chapters 2, 3, and 4 still read like stitched-together 1995 lecture/working notes. For example:


* **§1.4 (Outline, p. 5):** Still uses the 1995 phrasing *"We shall describe, in the p-adic case with $p \neq 2$, five correspondences..."* (repeated verbatim in §4.1, p. 12: *"five correspondences between functions..."*). Yet if a reader actually counts the $p \neq 2$ correspondences left in Chapter 4 after moving supercuspidals to Appendix A and marking Savin's Iwahori claim as unverified, it is unclear what the "five correspondences" are (odd hyperbolic, even hyperbolic, odd elliptic, even elliptic, Satake? Or Iwahori?). Either enumerate the five explicitly in §4.1 or drop the word "five".


* **§4.7 (p. 22, "On the character of the Weil representation"):** Opens with informal 1995 scratchpad prose: *"(This integral does not converge absolutely...)"* with a literal three-dot ellipsis. Cleaning up that parenthetical (e.g., *"This integral converges only as a principal value, not absolutely."*) will improve the polish.


* **Chapter 2 & Chapter 3 ultra-short subsections:** Several subsections consist of a single 3-line lemma without proof or transition (e.g., §§3.2.1, 3.2.2, 3.2.4, §§4.2.2, 4.2.3, 4.2.4). Merging §§4.2.2–4.2.4 into a single subsection *"4.2.2 Elliptic, hyperbolic, and unipotent orbital integrals"* would eliminate choppy page layout and repetitive boilerplate (`By Lemma 2.3(...), we have... We have \int ... where \gamma = (g,1)...`).






2. **Clarify the Book Class vs. Article Format:**
* At ~48 pages, using `\documentclass[12pt,letterpaper]{book}` creates many half-empty pages at chapter breaks, requires manual creation of an `abstract` environment, and puts an abstract *before* `\tableofcontents` in a book. If this is intended for arXiv or a memoir-style publication (e.g., *Memoirs of the AMS* or a standalone monograph), `book` or `memoir` (`openany` option to avoid blank recto/verso pages in a 48-page draft) works well; if intended for a journal (e.g., *Experimental Mathematics*, *Rocky Mountain J. Math.*, or *New York J. Math.*), `amsart` with `\section` instead of `\chapter` would be much cleaner and more compact.




3. **Typography and LaTeX Polish:**
* **Underlining in the Bibliography (`\underline{...}` and `\underbar{...}`):** The bibliography uses 1995 typewriter-era `\underline` and `\underbar` for volume numbers and book titles, which produces uneven baselines (especially when split across lines, as in `[AC]`, `[BJ]`, `[Ge2]`, `[HM]` with `\newline`!). Replace `\underline` / `\underbar` with `\emph{...}` for book titles and `\textbf{...}` for journal volume numbers.


* **Bibliography Ordering & Typos:**
* Entries `[GS2]` through `[Zh]` at the end of the bibliography (pp. 49–50) are out of alphabetical order (`Gan–Savin`, `Jacquet–Shalika`, `Li`, `Shahidi`, `Takeda–Wood`, `Zhang` appear *after* `Silberger [S]`, followed by `Waldspurger` and `Weil`). Re-sort alphabetically by label/author.


* `[J1]`: typo `"of of"` in `"The metaplectic analog of of Kazhdan's endoscopic lift"`.


* `[A3]` (`\bibitem[A3]{A6}`): missing page numbers (`1-97`? Actually *Ann. of Math.* **114** (1981), 1–74).


* `[L3]` (`\bibitem[L3]{L4}`): missing year `1980` and volume `96` (*Base Change for GL(2)*, Annals of Math. Studies **96**, Princeton Univ. Press, 1980).


* `[Wa2]`: missing page numbers (`261--352`? Actually *Forum Math.* **3** (1991), 219–307).


* `[Li3]`: `arXiv:2109.06581` has since been published: *J. Reine Angew. Math.* (Crelle) **801** (2023), 1–99 (or check exact publication details if updating post-2021 preprints).




* **Minor LaTeX Typos in the Main Text:**
* Page 19, §4.5.1: `$\overline{M} = <\gamma >$` uses ASCII `<` and `>` instead of `\langle \gamma \rangle` (and similarly `$<\ ,\ >$` in Remark 4.17 on p. 24—use `\langle \cdot, \cdot \rangle`).


* Page 21, proof of Lemma 4.11: `${\rm \sgn}(m)$` (`\sgn` is already an operator via `\DeclareMathOperator{\sgn}{sgn}`, so `\rm` is redundant).


* Page 25: `a $8^{th}$ root of unity` $\to$ `an $8^{\text{th}}$ root of unity`, and `$fixed$` $\to$ `\emph{fixed}`.


* Page 28, Remark 4.28: `\overline{\pi_{nt,i}}` (bar covers subscript) vs `\overline{\pi}_{nt,i}` two lines above.


* Page 39, Remark 5.10 / Appendix A (`prop:164`): *"Strongly cuspidal of level $m \ge 1$ representation $\sigma$"* $\to$ *"strongly cuspidal representation $\sigma$ of level $m \ge 1$"*.


* Page 40, Proposition A.2: `[\sum_{...} \chi_{\overline{\sigma}}^\circ(gxg^{-1})]` — brackets `[...]` are unscaled `\left[ ... \right]` around a big `\sum`.







---

### 4. Summary Recommendation

This is an honest, mathematically interesting, and pedagogically valuable manuscript that rescues a failed 1995 trace-formula strategy by turning it into a sharp negative theorem (Theorem 5.7) and diagnosing the exact root-datum / dual-group mechanism ("same torus, doubled coroot") behind the failure.

Once the local glitches noted in **Section 2** are fixed—most importantly:

1. Removing the $F=\mathbb{R}$ exception $v=1$ in formula (2.2) so $\beta_1$ is actually a 2-cocycle on $GL_2(\mathbb{R})$,
2. Fixing (or flagging as heuristic) the sign $\operatorname{sgn}(qa)$ and p-adic prefactor in the Weil kernel integration of §4.7.3,
3. Unifying $\zeta$ vs. $\zeta^{-1}$ and "genuine" vs. "anti-genuine", and clarifying the $|D(t)|$ vs. $|D(t)|^{1/2}$ convention in §4.3.3,
4. Cleaning up the minor LaTeX and bibliography items in **Section 3**,

the manuscript will be both mathematically sound and a pleasure to read.

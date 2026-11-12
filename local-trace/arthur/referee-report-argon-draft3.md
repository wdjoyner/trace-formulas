### Referee Report on *"The spectral measure of an elliptic orbital integral, via Arthur's local trace formula (Draft 3)"*

#### 1. General Assessment

This paper develops a very clean, conceptual alternative ("Route B") to the truncation method of the companion paper `[JC26]` ("Route A") for determining the spectral measure $dI_\gamma$ of a regular elliptic orbital integral $O_\gamma(f)$ on the spherical Hecke algebra $\Hc(G,K)$. By specializing Arthur's local trace formula `[Ar91, Ar93]` to a test function $f \otimes \phi$ with $f \in \Hc(G,K)$ spherical and $\phi \in C_c^\infty(G_{\ellr})$ supported on the regular elliptic set, the authors show that the geometric side collapses to the single term $M=G$ (Proposition 5.1), while the spectral side collapses—via the splitting formula and the vanishing of normalized spherical weighted characters (Lemma 3.2)—to an absolutely continuous weighted character on $\Thu$ plus a finite sum of smooth measures supported on subtori arising from elliptic elements of $R$-groups (Theorems A–C and Theorem 7.1). Section 9 then works out the combinatorics of $R$-groups and elliptic virtual characters for $SL(n)$ (Lemma 9.1 and Proposition 9.2) and establishes an exact dictionary between those elliptic data and the supports of $\kappa$-orbital integrals from endoscopy (Proposition 9.5).

The manuscript is exceptionally well organized and transparent about what is proved, what is quoted, and what remains to be verified in the `Status` blocks and Section 12 `(N1)`–`(N8)`. The running rank-one examples (`Examples 3.1, 3.3, 3.5, 3.6, 4.2, 5.2, 6.4, 7.4`) and the comprehensive notation table (`Table 1`) and glossary (`Appendix A`) make a technically demanding subject highly readable.

Below, I first show how several of the main open technical caveats in Draft 3—most notably **Remark 4.1 / Status 7.2 / (N1) in rank $\ge 2$**, the **sign question in Section 4.4**, **Lemma 6.3 / (N3)**, and the **$W$-invariance question after Corollary 8.3**—can actually be resolved right now using standard properties of $(G,M)$-families and unramified representations. I then note a measure-normalization discrepancy in `\eqref{e:Dprime}` and list minor expository and typographical suggestions.

---

#### 2. Major Mathematical Points and Simplifications

##### 2.1. Resolution of Remark 4.1 and Status 7.2: Why there are no extra Levi correction terms in rank $\ge 2$

In the Abstract, Introduction, Remark 4.1 (`r:norm`), Status 7.2 (`st:main`), and Item `(N1)`, the draft cautions that Arthur's spectral expansion `\eqref{e:spec}` uses *unnormalized* weighted characters $J_M(\pi, f) = \tr(\mathcal{J}_M(\pi, P) I_P(\pi, f))$, whereas Lemma 3.2 (`l:sphvanish`) requires the *normalized* intertwining operators $R_{Q\vert{}P}$. Remark 4.1 applies the product formula for $(G,M)$-families to $J_{Q\vert{}P}(\pi) = r_{Q\vert{}P}(\pi) R_{Q\vert{}P}(\pi)$ and worries that in rank $\ge 2$, intermediate Levi subgroups $M \subsetneq L \subsetneq G$ might contribute non-vanishing correction terms to Theorem B and Theorem 7.1.

In fact, **no such intermediate correction terms arise in any rank**, because the normalizing factors on $G(F) \times G(F)$ cancel identically before splitting:

1. In `[Ar91, (12.7) and §12, Remark 1]`, for a representation $\pi = \pi_1 \otimes \tilde{\pi}_2 \in \Pi_{\mathrm{disc}}(M)$ (where $\pi_1, \pi_2$ lie in the same $L$-packet or are equal to a constituent of an induced representation from $\sigma$, and $\tilde{\pi}_2 = \pi_2^\vee$), Arthur defines the family on $I_{\bar{P}}(\pi_1) \otimes I_P(\tilde{\pi}_2)$ using the opposite parabolics $\bar{Q}\vert{}\bar{P}$ on the first factor and $Q\vert{}P$ on the second factor.
2. For any unitary representation $\sigma$ of $M(F)$ and $\Lambda \in i\fa_M^*$, the canonical normalizing factors satisfy the unitarity/contragredient relation

$$r_{\bar{Q}\vert{}\bar{P}}(\sigma_\Lambda) \, r_{Q\vert{}P}(\tilde{\sigma}_\Lambda) = 1 \qquad (\text{or a constant independent of }\Lambda),$$



so the normalized scalar $(G,M)$-families $r_{\bar{Q}}(\Lambda, \sigma, \bar{P}) = r_{\bar{Q}\vert{}\bar{P}}(\sigma)^{-1} r_{\bar{Q}\vert{}\bar{P}}(\sigma_\Lambda)$ and $r_Q(\Lambda, \tilde{\sigma}, P) = r_{Q\vert{}P}(\tilde{\sigma})^{-1} r_{Q\vert{}P}(\tilde{\sigma}_\Lambda)$ multiply to $1$ identically for all $Q \in \cP(M)$ and $\Lambda \in i\fa_M^*$. (For unramified $\chi \in \Thu$, this is immediate from `\eqref{e:rnorm}`: the roots positive for $\bar{P}$ and negative for $\bar{Q}$ are the negatives of those positive for $P$ and negative for $Q$, and $(\chi_\Lambda)_{-\alpha} = (\chi^{-1}_{-\Lambda})_\alpha$.)
3. Consequently, as Arthur notes in `[Ar91, p. 80, Remark 1]`, the unnormalized $(G \times G, M \times M)$-family $\mathcal{J}_Q(\Lambda, \pi, P)$ on the product group is **already equal** to the tensor product of the two **normalized** $(G,M)$-families on the individual factors:

$$\mathcal{J}_Q(\Lambda, \pi, P) = \mathcal{R}_{\bar{Q}}(\Lambda, \pi_1, \bar{P}) \otimes \mathcal{R}_Q(-\Lambda, \pi_2^\vee, P).$$



(Indeed, the individual unnormalized families on a single factor $G$ have poles on the unitary axis whenever $\chi_\alpha = 1$, so one *must* split $\mathcal{J}_Q(\Lambda, \pi, P)$ into the normalized families on each factor in `\eqref{e:split}`.)
4. Once `\eqref{e:split}` is applied to the tensor product of the two normalized families (`[Ar91, §10]`), Lemma 3.2 (`l:sphvanish`) applies directly to the normalized weighted character $J_M^{L_1}(\pi_1, f_{1,Q_1})$ on the spherical factor $f_1 = f \in \Hc(G,K)$ and forces $J_M^{L_1}(\pi_1, f_{1,Q_1}) = 0$ for all $L_1 \supsetneq M$ **in every rank**!
5. This forces $L_1 = M$ and $L_2 = G$ in `\eqref{e:split}`, leaving only the single normalized weighted character $J_M(\pi^\vee, \phi)$ on the second factor. Thus the formulas of Theorem B and Theorem 7.1 hold as stated in **all ranks** without extra intermediate Levi terms.

##### 2.2. Resolution of the Sign Question in Section 4.4 (`\eqref{e:split}`)

At the end of Section 4.4 (page 7), the paper notes: *"The signs that come from the twist by $-\Lambda$ in the first factor have not been checked"*.
Notice that in the proof of Proposition 6.1 (`p:split`), Lemma 3.2 kills every term in `\eqref{e:split}` with $L_1 \ne M$. For the surviving term $L_1 = M$, the space $\fa_M^{L_1} = \fa_M^M = \{0\}$ has dimension $0$. Thus, in the splitting formula `[Ar88, Cor. 7.4]`, no derivatives with respect to $\Lambda$ are taken on the first factor $L_1 = M$ (the family on $M$ has a single parabolic $M \in \cP^M(M)$ and equals the identity operator $1$ at $\Lambda = 0$). Any sign $(-1)^{\dim \fa_M^{L_1}}$ coming from replacing $\Lambda$ by $-\Lambda$ on the first factor is therefore $(-1)^0 = +1$.

##### 2.3. Completing the Proof of Lemma 6.3 (`l:noDS`, Item `(N3)`)

Lemma 6.3 states that a square-integrable representation of $L(F)$ with $\dim \fa_{M_0}^L > 0$ has no vector fixed by the hyperspecial subgroup $K \cap L(F)$, and the Status box notes that the lower bound from Macdonald's formula needs care at non-regular $\chi$ where terms can cancel. Here are two short, complete proofs that avoid any cancellation issues at non-regular $\chi$:

* **Proof 1 (via Macdonald's Plancherel theorem):** Suppose an irreducible $(K \cap L)$-spherical representation $\sigma$ of $L(F)$ is square-integrable modulo $A_L(F)$. Then $\sigma$ is a unitary spherical representation with Satake parameter $\chi \in \Thu$, and its normalized spherical matrix coefficient $\Gamma_\chi^L$ lies in $L^2(A_L(F) \backslash L(F))$. For every $h \in \Hc(L, K \cap L)$, convolution gives $h * \Gamma_\chi^L = h^\vee(\chi)\Gamma_\chi^L$, which means the 1-dimensional space $\mathbb{C}\Gamma_\chi^L$ spans an atom at $\chi \in \Thu / W^L$ for the spherical Plancherel measure $d\mu_L$ of $L(F)$. However, by Macdonald's theorem `[Ma71]`, $d\mu_L(\chi) = \rho_L(\chi)\,d\chi$ is absolutely continuous with respect to Haar measure on the torus $\Thu$ of positive dimension $\dim \fa_{M_0}^L > 0$, hence has no atoms—a contradiction.
* **Proof 2 (via Casselman's square-integrability criterion `[Ca95, Thm. 4.4.6]`):** In Arthur's $\Tdisc(M)$, $\sigma$ is a tempered square-integrable representation of $L(F)$. If $\sigma$ has a non-zero $(K \cap L)$-fixed vector, it embeds as a subrepresentation of an unramified principal series $I_{B_L}^L(\chi)$ with $\chi \in \Thu$ (since $\sigma$ is tempered). By Frobenius reciprocity, every normalized exponent of the Jacquet module $\sigma_{N_0}$ is of the form $w\chi$ ($w \in W^L$), which satisfies $\vert{}w\chi(a)\vert{} = 1$ for all $a \in A(F)$. By Casselman's criterion `[Ca95, Thm. 4.4.6]`, square-integrability modulo $A_L(F)$ requires $\vert{}\omega(a)\vert{} < 1$ on $A_0^- \setminus A_L(F)K_A$ for every exponent $\omega$ of $\sigma_{N_0}$, which is impossible when $\dim \fa_{M_0}^L > 0$.

##### 2.4. Proof of the $W$-Invariance after Corollary 8.3 (`c:pgl2`)

Following Corollary 8.3 (page 9), the authors note: *"If the weighted character is $W$-invariant, that is, if $J_A(\chi, \phi) = J_A(\chi^{-1}, \phi)$, then the right side is $-\frac{1}{2} J_A(\chi^{-1}, \phi)$, as in Conjecture 8.1. We expect this invariance, but we have not checked it."*

This $W$-invariance holds in general (`[Ar89b, Prop. 4.3]`) and is very easy to see both conceptually and in rank one:

* **General argument:** For $w \in W$, the normalized intertwining operator $R_{P\vert{}w^{-1}P}(w\chi)$ composed with the translation isomorphism $I_P(\chi) \xrightarrow{\sim} I_{w^{-1}P}(w\chi)$ gives a unitary equivalence $I_P(\chi) \simeq I_P(w\chi)$ that intertwines $I_P(\chi, \phi)$ with $I_P(w\chi, \phi)$ and conjugates $\mathcal{R}_Q(\Lambda, w\chi, P)$ into $\mathcal{R}_Q(\Lambda, \chi, w^{-1}P)$. Passing to the limit at $\Lambda = 0$ and taking the trace gives $J_{M_0}(w\chi, \phi) = \tr(\mathcal{R}_{M_0}(\chi, w^{-1}P) I_P(\chi, \phi))$, which equals $J_{M_0}(\chi, \phi)$ because $J_{M_0}(\chi, \phi)$ is independent of the choice of $P \in \cP(M_0)$ (\S 3.3).


* **Direct rank-one check (from Example 3.5):** In Example 3.5, $\mathcal{R}_A(\chi, B) = -v\, R_{\bar{B}\vert{}B}(\chi)^{-1} \frac{d}{d\xi} R_{\bar{B}\vert{}B}(\chi_\Lambda)\big\vert{}_{\xi=0}$ where $\xi = \Lambda(\alpha^\vee)$. Replacing $\chi$ by $w\chi = \chi^{-1}$ replaces $\chi_\Lambda$ by $(\chi^{-1})_\Lambda = (\chi_{-\Lambda})^{-1} = w(\chi_{-\Lambda})$. Conjugating by the unitary involution $R_{\bar{B}\vert{}B}(\chi)$ swaps $B$ and $\bar{B}$ (which replaces $R_{\bar{B}\vert{}B}$ by $R_{B\vert{}\bar{B}} = R_{\bar{B}\vert{}B}^{-1}$) while $\Lambda \mapsto -\Lambda$ flips the sign of $\frac{d}{d\xi}$. Because $\frac{d}{d\xi}(R^{-1}) = -R^{-1} \frac{dR}{d\xi} R^{-1}$, the two minus signs cancel inside the trace against $I_B(\chi, \phi)$, yielding $J_A(\chi^{-1}, \phi) = J_A(\chi, \phi)$.



Including this short verification allows Corollary 8.3 to state $I(\chi, \phi)\rho(\chi) = -\frac{1}{2}J_A(\chi^{-1}, \phi)$ directly.

##### 2.5. Measure Normalizations and $\vol(S(F))$ in Proposition 5.1(b) and `\eqref{e:Dprime}`

There is a subtle convention mismatch regarding $\vol(S(F))$ between Section 4.2/5.1 and Equation `\eqref{e:Dprime}` in Section 9.4:

1. In `\eqref{e:main}` (page 2) and Proposition 5.1(b) (page 7), the orbital integral is defined as the integral over all of $G(F)$:

$$O_\gamma(f) = \int_{G(F)} f(g^{-1}\gamma g)\,dg,$$



rather than over the quotient $G_\gamma(F)\backslash G(F)$.


2. In Section 4.2 (page 6), $J_M(\gamma, f)$ is written with integrals over $A_M(F)\backslash G(F)$, while in `[Ar91, (12.1)]` Arthur integrates over $G_\gamma(F)\backslash G(F)$ and normalizes the Haar measure on $T(F)/A_M(F)$ to have total mass $1$ for every elliptic maximal torus $T$ of $M$. Under Arthur's convention $\vol(T(F)/A_M(F)) = 1$, the two integrals coincide numerically.


3. However, in Section 9.4 (page 12), Equation `\eqref{e:Dprime}` reintroduces an explicit factor $\vol(S(F))$ in the numerator:

$$\sum_{\zeta \ne 1} c_{\tau_\zeta} \tr \tau_\zeta^\vee(\phi) = \sum_S \frac{\vol(S(F))}{\vert{}W(G,S)\vert{}} \int_{S(F)} \vert{}D(s)\vert{} \left(\frac{1}{n} \sum_{\kappa \ne 1} \Delta_\kappa(s_H, s)^{-1}\right) O_s(\phi)\,ds,$$



and the text immediately below `\eqref{e:Dprime}` states that by the Weyl integration formula, this means the virtual character $\sum_{\zeta \ne 1} c_{\tau_\zeta}\Theta_{\tau_\zeta^\vee}(s)$ equals $\vol(S(F)) \frac{1}{n} \sum_{\kappa \ne 1} \Delta_\kappa(s_H, s)^{-1}$ on $S(F)$.


4. Let us check the power of $\vol(S(F))$ in the Weyl integration formula when $O_s(\phi) = \int_{G(F)} \phi(x^{-1}sx)\,dx$:
If $ds$ is a Haar measure on $S(F)$ of total mass $\vol(S(F))$ and $d\dot{x} = dx/ds$ is the quotient measure on $S(F)\backslash G(F)$, then $O_s(\phi) = \vol(S(F)) \int_{S(F)\backslash G(F)} \phi(x^{-1}sx)\,d\dot{x}$. Therefore, for any class function $h$ (such as a virtual character $\Theta$),

$$\int_{G(F)} h(x)\phi(x)\,dx = \sum_S \frac{1}{\vert{}W(G,S)\vert{}} \int_{S(F)} \vert{}D(s)\vert{} h(s) \left(\int_{S(F)\backslash G(F)} \phi(x^{-1}sx)\,d\dot{x}\right) ds = \sum_S \frac{1}{\vert{}W(G,S)\vert{}\vol(S(F))} \int_{S(F)} \vert{}D(s)\vert{} h(s) O_s(\phi)\,ds.$$



Thus, if $O_s(\phi)$ is the integral over $G(F)$ and $ds$ has mass $\vol(S(F))$, then $\frac{1}{\vol(S(F))}$ (not $\vol(S(F))$) appears in front of $\int_{S(F)} \vert{}D(s)\vert{} h(s) O_s(\phi)\,ds$ (or if $ds$ is normalized to mass $1$, no $\vol(S(F))$ factor appears in $\Theta(s)$).
5. Similarly, it is worth clarifying whether $\Delta_\kappa(s_H, s)$ in `\eqref{e:kappadecomp}` and `\eqref{e:Dprime}` denotes the cohomological sign $\kappa(\mathrm{inv}(s_H, s)) \in \mu_n$ (so that $\vert{}\Delta_\kappa\vert{} = 1$, as used when saying *"If all transfer factors are $1$, the weight of the point mass is $\frac{n-1}{n}$"*) or the full Langlands–Shelstad transfer factor `[LS87]`, which includes the discriminant factor $\Delta_{IV} = \vert{}D_G(s)\vert{}^{1/2} / \vert{}D_H(s_H)\vert{}^{1/2}$.



##### 2.6. Uniqueness of the Permutation $w$ in Proposition 9.2 and Corollary 9.3

The proof of Proposition 9.2 (`p:slnell`, page 10) is very clean and rigorous, and the discussion of $SL(4)$ at $z=(1,1,-1,-1)$ on page 10 nicely motivates Arthur's canonical representative of $r \in R_\chi^M$. One small detail is worth making explicit to make Corollary 9.3 (`c:slnindex`) completely transparent:

* In Proposition 9.2(c), the statement reads: *"$r$ is the class of a permutation $w$ that is a single $m$-cycle on each block, and $c(w) = \zeta$"*. A reader might wonder whether, for a fixed $\chi \in T_m$ and a fixed primitive $m$-th root of unity $\zeta$, there is only *one* such class $r \in R_\chi^{M_m}$ or $(m-1)!^d$ of them.


* Because the $m$ coordinates of $z$ within each block form a single coset $w_j \mu_m$, they are **pairwise distinct** inside each block. Therefore:
1. $W_\chi^{M_m, \circ} = 1$ holds for **every** $\chi \in T_m$ (even if two different blocks share the same coset, since the roots of $M_m$ only compare coordinates within the same block); and
2. The equation $z_{w^{-1}(i)} = \zeta z_i$ **uniquely determines** the permutation $w \in W^{M_m}$ from $\zeta$ (in fact, via the isomorphism $c: R_\chi^{M_m} \to \mu_m$ on the diagonal copy of $\mu_m$).
Stating this explicitly in one sentence at the end of the proof of Proposition 9.2 makes Corollary 9.3 immediate.



---

#### 3. Readability, Exposition, and Minor Corrections

1. **Overloading of the symbol $\pi$ in Section 4.2 vs. Section 4.4 and Proposition 6.1:**
* In Section 4.2 (`\eqref{e:spec}`), $\pi = \pi_1 \otimes \pi_2$ is a representation of $M(F) \times M(F)$.


* In Section 4.4 (`\eqref{e:split}`) and Proposition 6.1 (`p:split`), $\pi$ denotes a representation of $M(F)$, so the representation of $M(F) \times M(F)$ on the left-hand side of `\eqref{e:split}` is actually $\pi \otimes \pi^\vee$ (or $\pi^\vee \otimes \pi$).


* Adding a brief remark in Section 4.4 explaining this shorthand (writing $J_M(\pi, f_1 \otimes f_2)$ for $J_M(\pi \otimes \pi^\vee, f_1 \otimes f_2)$ when $\pi$ is a representation of $M(F)$) will prevent any confusion.


2. **How $M = G$ fits into the sum over $M \supsetneq M_0$ in Theorem 7.1 (`t:main`):**
* In Section 6.3 (`\S\ref{s:class}`), the surviving contributions are listed in three bullets: $M = M_0$, $M \supsetneq M_0$, and $M = G$.


* In Theorem 7.1 (page 8), the singular part is written as a single sum over $M \supsetneq M_0$ of integrals over $i\fa_M^* / L_M^\vee$. When $\dim \fa_0^G > 0$, $M = G$ is included in $M \supsetneq M_0$ as the case where $i\fa_G^* / L_G^\vee = \{0\}$ is a point (with counting measure) and $J_G(\tau^\vee, \phi) = \tr \tau^\vee(\phi)$, where $c_{G,\tau}$ is the constant denoted $c_\tau$ in Example 7.4 and Section 9.4. Mentioning this explicitly right after Theorem 7.1 will tie Section 6.3, Theorem 7.1, and Example 7.4 together smoothly.




3. **Verification of the Bibliography Status Box in Section 2.2 (page 3):**
* The Status box at the end of Section 2.2 notes that the page ranges of `[Ar01, Ar02, Ar03]`, `[MW16]`, and `[Wa10]` remain to be verified. All five entries in the bibliography (`[Ar01]` pp. 157–220; `[Ar02]` pp. 175–277; `[Ar03]` pp. 769–873; `[MW16]` Vols. 1–2, Progress in Math. 316–317, 2016; `[Wa10]` pp. 1180–1290) are already exact.




4. **Minor Typographical Adjustments:**
* **Page 10, Proposition 9.2 (`p:slnell`)**: Item (a) ends with a period (`$M=M_m$.`), while items (b) and (c) begin with lowercase words (`on each block...`, `$r$ is the class...`). Either capitalize `(b) On each block...` or use semicolons after (a) and (b).


* **Page 11, Lemma 9.4 (`l:iota`)**: In the proof sketch, $\operatorname{Res}_{E/F} GL(d)$ is used for the endoscopic group $H_m$; it may help the reader to note that for $m=n$ ($d=1$), $H_n = S_n$ is the elliptic norm-one torus $\ker(N_{E/F}: E^\times \to F^\times)$ used in the "Prime $n$" paragraph on page 12.


* **Page 12, Section 10.1 (`\S\ref{s:pgl2}`)**: In the displayed formula for $I(\chi, \gamma)\rho(\chi)$, the side condition reads $(y = e^{i\theta})$. Since $y = \chi_\alpha(\pi) = z^2$ was defined back in Example 3.3 (page 5), reminding the reader `(where $y = \chi_\alpha(\pi) = e^{i\theta}$ as in Example 3.3)` will save them from looking back to find $y$.





Would you like me to draft the revised LaTeX snippets incorporating the simplifications for Remark 4.1, Lemma 6.3, and Corollary 8.3?
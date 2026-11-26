The core mathematics in the manuscript—the Hilbert-symbol edge discrepancy $\ell(\bar a)$, the weighted fixed-vertex trace sum, the parity factor $\ell(z)^{j-i}$, the fixed-ball radius $r$, and the numerical examples over $\mathbb Q_7$ and $\mathbb Q_5$—is completely sound. Below is a concise, actionable list of mathematical clarifications, structural cleanups, and prose edits ready to paste into your editing agent.

### 1. Mathematical Clarifications & Missing Details

* **Section 3.1 (Extended cocycle multiplication law):** Equation (3.4) defines the extended cocycle $\beta'(g,h)$ on $G'=\mathrm{GL}_2(F)$, and the proof of Proposition 3.2 computes $\beta'(D,h(u))/\beta'(h(u),D)$, but the group multiplication law on $\widetilde{G'}$ is never explicitly stated. Add one sentence defining $(g,\zeta)(h,\xi)=(gh,\zeta\xi\beta'(g,h))$ on $G'\times\mu_2$, and note explicitly that $\widetilde D^{-1}=(D^{-1},\beta'(D,D^{-1})^{-1})$ cancels out in the commutator $(D,1)(h(u),1)(D,1)^{-1}(h(u),1)^{-1}$ because $D$ and $h(u)$ commute in $G'$.


* **Section 3.3 (Pro-$p$ radical $I^+$ description):** The text states: *"Its pro-$p$ radical $I^+$ is the inverse image of the lower unipotent subgroup under reduction"*. Because $I$ already has upper-right entry in $\varpi\OO$, "reduction modulo $\varpi$" is only defined on $K_0$, and even in $K_0$ one must specify that diagonal entries reduce to $1$ (not $\pm 1$). Revise to define $I^+$ explicitly in coordinates: matrices $\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in K_0$ with $a\equiv d\equiv 1\pmod\varpi$ and $b\in\varpi\OO$ (equivalently, the preimage under mod-$\varpi$ reduction $K_0\to\mathrm{SL}_2(\kk)$ of the lower triangular unipotent subgroup).


* **Section 4.1 (Trace normalization / Haar measure in Theorem 4.1):** In the proof of Theorem 4.1, the transition from the operator trace $\tr\pi_j(f)=\int_G f(g)\Theta_{\pi_j}(g)\,dg$ to the pointwise sum $\sum_{tv=v}\tr\sigma_v(t)$ implicitly requires matching the Haar measure on $G$ (and $\Mp$) with the measure used on $K_w$ when integrating over a small neighborhood $U\subset K_w$ of $t$. Add a brief sentence stating that for $U\subset K_w$ small enough, $g\in U$ fixes $v=hv_j$ if and only if $g\in K_v$ (which holds uniformly on $U$ by the ball-shrinking step), so each fixed coset $hK_j$ contributes $\int_U f(g)\tr\sigma_v(g)\,dg$ under the identical Haar normalization on $G$ (and lifted Haar measure on $\Mp$), cancelling $\operatorname{vol}(U)$.


* **Section 5.2 (Inflation to $K_1$ depends on choice of isomorphism):** The text says *"Inflate $\sigma_\theta$ to each $K_j$ by reduction in its own coordinates"*. Because $\mathrm{SL}_2(\kk)$ has outer automorphisms coming from $\mathrm{GL}_2(\kk)$ conjugation by non-square determinant elements, swapping the two Deligne–Lusztig representations $\sigma_\theta^\pm$ within a geometric conjugacy class changes the character at unipotent elements $zu$ unless specified! Fortunately, $\chi_\theta(zu)=-\theta(z)$ is **identical** for both irreducible components when $\theta^2\ne 1$ (only non-generic $\theta^2=1$ splits unipotent traces via Gauss sums). Add a one-sentence remark in Section 5.2 noting that while conjugation by $D$ identifies $K_1/K_1^+\simeq\mathrm{SL}_2(\kk)$ via an outer automorphism when $\ell(-1)=-1$ or on unipotent orbits, the regular cuspidal character $\chi_\theta$ of degree $q-1$ is invariant under $\mathrm{GL}_2(\kk)$-conjugation (its values at $zI$, $zu$, and $\bar\tau\in\bar T_1$ depend only on trace/eigenvalues for $\theta^2\ne 1$).


* **Section 7.2 (Ramified elliptic elements and Lemma 4.2):** Section 7.2 states that in a ramified quadratic extension $E/F$, a norm-one element $t\in E^1\setminus\{\pm 1\}$ fixes an edge, and its reduction automatically satisfies Lemma 4.2 ($z=\pm 1$). Add one phrase explaining *why* every element of $E^1$ in a ramified extension has central/unipotent reduction ($t\equiv \pm 1\pmod{\varpi_E}$ because $\mathcal O_E/\varpi_E\simeq\kk$, so $N_{E/F}(t)=1\implies \bar t^2=1$).



### 2. Notation, Style, and Formatting Fixes

* **Notation Table vs. Body Unused/Missing Symbols:**
* `K_i^+` appears in the Section 1.3 Notation table, is never defined by formula, and in Section 7.1 is abruptly written as `K_0(m)` instead. Define $K_i^+ = \ker(K_i\to\mathrm{SL}_2(\kk))$ in Section 2.1 or 3.2, and align `K_0(1) = K_0^+` with `K_0(m)` in Section 7.1.


* `\mu_2` is used repeatedly starting in Lemma 3.1, whereas Section 1 defines $\ker P=\{\pm 1\}$. Either add $\mu_2=\{\pm 1\}$ to Section 1 / Notation table or standardize on $\{\pm 1\}$.




* **Remark Numbering Redundancy:** `\newtheorem{remark}[theorem]{Remark}` already numbers remarks as *Remark 6.1* and *Remark 7.1*, so `[Remark 2026.1: split regular elements]` renders clumsily as **"Remark 6.1 (Remark 2026.1: split regular elements)."** Change the optional arguments in `\begin{remark}[...]` to `[Split regular elements]` and `[Higher levels]`.


* **Exponent Parity Notation $\ell(z)^{j-i}$:** Because $i,j\in\{0,1\}$, $j-i$ can be $-1$. Since $\ell(z)\in\{\pm 1\}$, $\ell(z)^{-1}=\ell(z)$ is mathematically valid, and it also makes $\ell(z)^{j-i}$ well-defined, though readers sometimes pause at negative exponents on characters when scanning quickly. No change required, or optionally mention once after Corollary 1.1 / 4.3 that $\ell(z)\in\{\pm 1\}$ so $\ell(z)^{j-i}=\ell(z)^{\vert{}j-i\vert{}}$.



### 3. Glossary Polish & Readability

* **Awkward phrasing in *Stable packet sum* entry:** The second sentence currently reads: *"The ordinary depth-zero pair has this interpretation, unlike the unweighted genuine sum asserted nowhere in this paper"*. Replace the defensive phrasing *"asserted nowhere in this paper"* with a cleaner mathematical statement: *"The ordinary depth-zero pair forms a stable packet whose character sum is constant near $\pm I$, whereas the unweighted genuine sum fails to cancel when $\ell(z)=-1$; a $\ell(z)^{j-i}$-weighted sum restores constancy."*


* **Expand 1–2 short Glossary entries for uniform depth:** Most glossary items have two substantial sentences, while **Lattice** (*"Its homothety class is a vertex."*) and **Central extension** (*"The double cover has kernel $\mu_2$."*) have very clipped second sentences. Expand those two slightly so every glossary entry provides self-contained context (e.g., for **Lattice**, mention that $\mathrm{GL}_2(F)$ acts transitively on lattices and adjacent lattices correspond to index-$q$ inclusions; for **Central extension**, mention that topological central extensions of $G$ by $\mu_2$ are classified via local symbol cocycles such as Kubota's).
# Full regularity does not exclude the repeated-polar locus

**November 15, 2026. Independent mathematical follow-up to Draft 6.** The main manuscript, \`revised/g2-shalika-germs-2026.tex\`, is unchanged. This note answers the outstanding regularity question from \`cubic-galois-descent-ls-resonance-2026-11-15.md\`.

## Theorem

Let \(F\) be a nonarchimedean local field of residual characteristic at least \(5\); let \(K/F\) be cyclic cubic; and let \(T/F\) be the elliptic cyclic-cubic maximal torus in §8 of the \(G_2\) Shalika-germ manuscript. Put \(u=\alpha(X)\in K\), for \(X\in\mathfrak t(F)\). The manuscript specifies
\[
\tau u=-\delta(X),\quad \tau^2u=\gamma(X),\quad
\gamma=\alpha+\beta,\quad \delta=2\alpha+\beta.
\]
Hence \(\mathrm{Tr}_{K/F}(u)=0\).

**(a)** The map \(X\mapsto u\) identifies \(\mathfrak t(F)\) with the two-dimensional trace-zero plane \(K^0\). Every nonzero \(X\in\mathfrak t(F)\) is regular for **all twelve roots** of \(G_2\).

**(b)** Writing \(a=\alpha(X)\), \(b=\beta(X)\), \(A_0=a\), \(A_1=-2a-b\), \(A_2=a+b\), \(\Delta=A_0-A_1\) and \(M=A_0+A_1-2A_2\), the repeated-polar discriminant satisfies
\[
\boxed{\mathscr D(X)=M^2+3\Delta^2
      =12(3a^2+3ab+b^2)
      =6\mathrm{Tr}_{K/F}(u^2)\in F.}
\]

**(c)** For a nonzero (hence regular) \(X\), \(\mathscr D(X)=0\) **if and only if** \(F\) contains a primitive cube root \(\xi\) of unity and \(u\) belongs to one of the two nontrivial \(\tau\)-eigenspaces:
\[
\tau u=\xi u\qquad\text{or}\qquad\tau u=\xi^2u.
\]
When \(\mu_3\subset F\), these two eigenspaces correspond to exactly **two distinct \(F\)-lines** in \(\mathfrak t(F)\), and every nonzero point on them is regular. When \(\mu_3\not\subset F\), \(\mathscr D=0\) holds only for \(X=0\).

## Proof of full regularity

If \(\alpha(X)=0\), Galois conjugation makes \(\delta(X)=\gamma(X)=0\), so \(\beta(X)=0\) and \(X=0\). Thus \(X\mapsto\alpha(X)\) is an injective \(F\)-linear map into \(K^0\), hence an isomorphism because both dimensions are two.

For nonzero \(u=\alpha(X)\), the short-root values, up to signs, are \(u,\tau u,\tau^2u\). The long-root values, up to signs, are
\[
\beta(X)=\tau^2u-u,\qquad
\epsilon(X)=u-\tau u,\qquad
\zeta(X)=\tau^2u-\tau u.
\]
Every conjugate is nonzero. No two conjugates can coincide: if \(\tau u=u\) (or \(\tau^2u=u\)), then \(u\in F\); its trace zero forces \(3u=0\), hence \(u=0\), a contradiction. So all roots are nonzero.

## Proof of the discriminant classification

Direct substitution gives \(\Delta=3a+b=\epsilon(X)\ne0\) and \(M=-3(a+b)=-3\gamma(X)\). Thus the displayed formula follows by expansion. If \(\mathscr D=0\), then \((M/\Delta)^2=-3\) with \(M/\Delta\in K\). A cubic extension has no quadratic subfield. Therefore \(\sqrt{-3}\in F\), equivalently \(\mu_3\subset F\).

Conversely, if \(\mu_3\subset F\), the regular representation of \(\mathrm{Gal}(K/F)\cong C_3\) splits as three one-dimensional character spaces; the trace-zero plane is the sum of its two nontrivial eigenspaces. For a nonzero eigenvector \(\tau u=\xi u\),
\[
\mathscr D(X)=6u^2(1+\xi^2+\xi^4)=0.
\]
The same holds for the \(\xi^2\)-eigenline; these are all the nontrivial zeros of the binary quadratic form.

## Field criterion and an explicit counterexample to exclusion

For residual characteristic at least \(5\), Hensel's lemma gives
\[
\mu_3\subset F\quad\Longleftrightarrow\quad q\equiv1\pmod3.
\]
Therefore the repeated-polar locus occurs for **all tame ramified cyclic cubic types**, and for **unramified cyclic cubic types when \(q\equiv1\pmod3\)**. It is absent in the unramified cases \(q\equiv2\pmod3\).

For a concrete unramified example let \(F=\mathbb Q_7\), choose a primitive \(\xi\in F\) with \(\xi^2+\xi+1=0\), and let \(K=F(\theta)\), \(\theta^3=2\). The reduction \(Z^3-2\) is irreducible over \(\mathbb F_7\), so \(K/F\) is unramified cubic; it is cyclic because \(\xi\in F\). Take \(\tau\theta=\xi\theta\) and the unique \(X\in\mathfrak t(F)\) such that \(\alpha(X)=\theta\). Then
\[
\begin{array}{c|rrrrrr}
\text{root}&\alpha&\beta&\gamma&\delta&\epsilon&\zeta\\\hline
\text{value}/\theta&1&\xi^2-1&\xi^2&-\xi&1-\xi&\xi^2-\xi
\end{array}
\]
and all six displayed values are nonzero, yet
\[
\boxed{\mathscr D(X)=6\theta^2(1+\xi^2+\xi^4)=0.}
\]
The scaled elements \(7^n X\) are regular and arbitrarily close to zero, with the same vanishing discriminant.

## Implication for Claim 8.3H

The repeated-polar situation cannot be removed by requiring \(X\) to be regular, elliptic, or sufficiently small. The preceding [Galois descent and LS resonance note](cubic-galois-descent-ls-resonance-2026-11-15.md) found a trivial-character logarithmic pole on the first exceptional divisor in that situation, outside the ordinary nonresonant Langlands–Shelstad local construction. The calculation here **confirms that this case genuinely falls within the manuscript's stated regularity hypotheses**. It does **not** show that the global cubic germ identity \((X_3)\) is false. An invariant extension of regularization or a demonstrated global cancellation remains necessary.

## Verification, references, and attribution

The standalone [exact SymPy checker](../scripts/verify_g2_polar_regular.py) verifies the discriminant identity, the long/short root formulas, the absence of common root-hyperplane factors, both cube-root eigendirections, and the \(\mathbb Q_7\) residue calculations. A separately typeset three-page LaTeX/PDF note is available as a conversation attachment.

References: D. Joyner, Claude, and Gemini, *On the transfer of Shalika germs for \(G_2\)*, Draft 6 (2026), §8, especially Theorem 8.3, Proposition 8.3A, and Claim 8.3H; R. Langlands and D. Shelstad, *On principal values on \(p\)-adic manifolds*, Lecture Notes in Math. 1041 (1984), 250–279.

This note is AI-aided mathematical research, not independent human refereeing.
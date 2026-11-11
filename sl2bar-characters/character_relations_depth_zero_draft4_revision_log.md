# Draft 4 revision log — November 11, 2026

## Aim

Extend Draft 3 from compact induction at the standard vertex stabilizer
\(K^{(0)}=\mathrm{SL}_2(\mathcal O_F)\) to the second \(\mathrm{SL}_2(F)\)-vertex orbit
\(K^{(1)}=D K^{(0)}D^{-1}\), with \(D=\mathrm{diag}(\varpi,1)\).

## Mathematical changes

1. **Two maximal compact vertex stabilizers.** Introduced \(v_0,v_1\),
   \(K^{(0)},K^{(1)}\), their pro-\(p\) radicals, the two integral unramified elliptic tori
   \(T^{(0)},T^{(1)}\), and explicit identifications of the finite reductive quotients
   with \(\mathrm{SL}_2(\mathbb F_q)\). These stabilizers are not \(\mathrm{SL}_2(F)\)-conjugate.
2. **Additional splitting assumption.** Assumed an independent continuous homomorphic
   splitting \(s_1:K^{(1)}\to\widetilde G\) in addition to \(s_0\). This is an explicit
   hypothesis, **not** asserted automatically for arbitrary extensions. The proof does
   not claim conjugation by \(D\in\mathrm{GL}_2(F)\) lifts to \(\widetilde G\).
3. **Mixed-splitting lemma.** On the pro-\(p\) intersections
   \(K^{(i)}_+\cap xK^{(j)}x^{-1}\), conjugated splittings agree because continuous
   homomorphisms to the prime-to-\(p\) center \(\mu_n\) vanish. The two lifts of
   \(-I\) coincide and are central when \(n\) is odd.
4. **Cross-orbit theorem (Theorem 7.5).** For both \(i,j\in\{0,1\}\) and every
   \(t\in(T^{(i)})^{\mathrm{reg}}\), established, conditional on both compact splits,
   \[\Theta_{\widetilde\pi_{j,\theta^{\langle n\rangle}}}(s_i(t^n))
   =\Theta_{\pi_{j,\theta}}(t).\]
   If \(t\) has regular elliptic reduction, the cross-orbit character vanishes.
   If the reduction is central, the common fixed ball meets both vertex orbits.
5. **Complementary character formula (Theorem 7.6).** For \(\rho_i(t)=zI\),
   \(r=r_i(t)\ge1\), the inducing parity changes the leading sign:
   \[\Theta_{\pi_{j,\theta}}(t)
   =\theta(z)((-1)^{r+1+j-i}q^r-1).\]
6. **Two-orbit sum (Corollary 7.7).** For all regular \(t\in T^{(i)}\),
   \[\Theta_{\pi_{0,\theta}}(t)+\Theta_{\pi_{1,\theta}}(t)
   =-\theta(\rho_i(t))-\theta(\rho_i(t)^{-1}).\]
   Near the center the \(q^r\) terms cancel, giving \(-2\theta(z)\). The
   metaplectic analogue follows by summing the two comparison identities.
7. **Expanded \(\mathbb Q_7\) example.** Added second-orbit values \(-8,48,-344\)
   at depths \(r=1,2,3\), opposite to first-orbit values \(6,-50,342\), and
   verified that each sum is \(-2\).

## Internal checks

- Both diagonal and cross-orbit character sums were independently checked by
  summing the \((q+1)q^{d-1}\) vertices on the relevant parity spheres, for
  \(q=7,13,19\) and \(1\le r\le6\).
- The LaTeX source was compiled twice with `pdflatex`; output has 13 pages,
  with resolved internal references and no overfull boxes.
- The final PDF pages were rendered and visually inspected for text overflow
  and page-layout issues.

## Limitations and next checks

- **Cocycle-specific splittings:** For an application to a named Kubota or
  Brylinski–Deligne cover, give an explicit reference or construction for the
  splitting over \(K^{(1)}\) and check its chosen normalization.
- **No new classification:** The ordinary two-orbit sum is consistent with
  classical Sally–Shalika and more recent endoscopic character literature;
  no originality claim has been established.
- **Excluded:** exceptional quadratic parameters, ramified elliptic tori,
  positive-depth supercuspidals, full stable character relations and a
  fundamental lemma.
- **External refereeing encouraged:** In particular, independently verify
  Lemma 7.3 (mixed splitting) and Theorem 7.5 (cross-orbit identity).

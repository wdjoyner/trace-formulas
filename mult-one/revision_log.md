# Revision log: *Direct comparison of SL(2) with its metaplectic cover* (formerly *Multiplicity one for SL(2)*)

## Stages

- **1995.** The Scientific Word manuscript `aabook.tex` with its `\input` files (not in this repository).
- **Draft 1** (Claude, November 20, 2026). Carbon (Gemini) had refereed the merged 1995 draft. In Draft 1 the files are merged into one pdflatex file, the main theorem is stated conditionally (the author's decision), and mechanical fixes are applied. In git, see commit `045016f`. Its log is the last section of this file.
- **Draft 3** (Claude, November 20, 2026). A style-guide pass with no mathematical changes. See the next section.
- **Draft 2** (Claude, November 20, 2026). This is the response to the referee report on Draft 1 in `revised/referee-report_draft1.md`. The author believes that report was written by ChatGPT (OpenAI). The section "Draft 2" below covers Draft 1 → Draft 2. Its theorem numbers refer to Draft 2. See the concordance in the Draft 3 section.

- **Draft 4** (Claude, November 23, 2026). Response to Claude's referee report on Draft 3 (`revised/referee-report_draft3.tex`). The main result is restated: the hypotheses of the Draft 3 theorem are inconsistent. See the section "Draft 4".
- **Draft 5** (Claude, November 23, 2026). Motivation section, new title, and a section tracing where the comparison fails. See the section "Draft 5".

The sections below are in reverse order: Draft 5, Draft 4, Draft 3, Draft 2, Draft 1. Theorem numbers in each section refer to the draft named there.

## Draft 5: motivation, new title, and where the comparison fails

Draft 5 (Claude, November 23, 2026) follows three requests by the author.

- **Motivation.** The author explained the question behind the text: the cover of SL(2) is known to correspond to PGL(2) (Weil, Shimura, Waldspurger); why is a direct correspondence with SL(2) wrong, and how far off is it? A new Section 1.1 "Motivation" states this, and the abstract is rewritten around it.
- **Title.** Changed from *Multiplicity one for SL(2)* to *Direct comparison of SL(2) with its metaplectic cover*. The directory was renamed from `mult1sl2/` to `mult-one/`, and the manuscript file from `multiplicity-one-SL2.tex` to `direct-comparison-SL2.tex`.
- **New Section 5.4, "Where the global comparison fails".** It traces the proposed argument through the trace formula. The direct comparison is globally consistent on the split torus (Weil's product formula for the Weil index gives the matching of regular hyperbolic terms and of traces of principal series). It fails for the intertwining operators (L(s, mu) against L(2s, mu^2)), for the residual spectrum (trivial representation against the even theta representations), and for the cuspidal spectrum (Theorem 5.16). Diagnosis: the same torus, with the coroot doubled.

Unverified in Draft 5, and marked as Remark 2026.12: the formula for the intertwining scalar on the cover, the description of its residual spectrum, and the form of Weil's product formula, all quoted from memory. The references [Shi] (Shimura 1973) and [We3] (Weil 1964), and the statement that Shimura's proof used Rankin's method and Weil's converse theorem, are also from memory. Siegel's historical role is not discussed.

Other changes: the script `scripts/referee_check.py` was added (it is run by `run_checks.py`), and the lemma numbers in the docstring of `scripts/local_formulas_check.py` were updated to Draft 5.

Theorem numbers in the "Draft 4" section below are the same in Draft 5. Sections of Chapter 5 after 5.3 moved down by one, and Chapter 1 gained a new Section 1.1.

## Draft 4: the main result restated

### Summary

Draft 4 was prepared by Claude (Anthropic) from Claude's referee report on Draft 3
(`revised/referee-report_draft3.tex`). The main change: the conditional main theorem of
Draft 3 (Theorem 7.9) is now Proposition 5.10 (`thm:main`), and the main result is the new
Theorem 5.16 (`thm:nonexist`): no genuine cuspidal representation corresponds to a given
cuspidal representation of SL(2) under the Satake correspondence of Definition 4.23. Hence
Hypotheses LH and GH are inconsistent (Corollary 5.17).

### AI usage

- Claude refereed Draft 3 and wrote Draft 4, including the statement and proof of
  Theorem 5.16, Lemmas 4.6 (`lem:Wequiv`) and 5.14 (`lem:square`), Remarks 4.7, 5.4 and
  2026.11 (`rem:even`), and the counterexample in Remark A.2.
- None of this has been checked by a specialist.

### Sources not consulted directly

Quoted from memory in Draft 4:

- Waldspurger [Wa1], [Wa2]: the correspondence Wald_psi on A_00, its compatibility with
  unramified principal series, and the fact that the even Weil representation has a
  one-dimensional image (used in Theorem 5.16 and Remark 5.4).
- Gelbart-Jacquet [GJ2]: the adjoint lift and its properties.
- Jacquet-Shalika [JS], Shahidi [Sha]: poles and nonvanishing of Rankin-Selberg L-functions at s=1.
- Li [Li1] (bibliographic data and the statement on characters), Gan-Savin [GS2]
  (bibliographic data), Arthur [A4] (8.1) (form of the correction term in section 4.2.5).
- Bibliographic corrections made from memory: [LL] volume 31; [M1], [M2] year 1984;
  [Ad1] Israel J. Math. 98 (1997).
- Checked on the web: Chai-Zhang (genericity condition), Zhang's addendum (title, volume),
  Li [Li2], [Li3].

### Changes in Draft 4

Structure
- Chapters 4 (supercuspidal correspondence) and 6 (trace formulas) are now Appendices A and B.
  Old Chapter 5 is Chapter 4; old Chapter 7 is Chapter 5, retitled "Global consequences".
- Abstract, section 1.1 and section 1.4 rewritten. Section 7.5 of Draft 3 ("Remarks on the
  1995 argument"), the list of errors in section 1.1, and the list of errors in the dyadic
  section were moved to this log (below).
- Corollary 7.16 of Draft 3 (`cor:main`) was deleted.

Mathematics
- New: Lemma 4.6 (Weyl group compatibility), Remark 4.7 (dependence on the uniformizer and
  eta; failure to preserve unitarity), Lemma 5.14, Theorem 5.16, Corollary 5.17, Remark on the
  even correspondence, Remark 5.4.
- Hypothesis LH: (LH1) and (LH2) are now imposed only on local components of cuspidal
  representations and of representations in A_00. Hypothesis GH is now stated for A_00.
  Reason: as stated in Draft 3, (LH1) and (LH2) fail for the real elliptic classes (Remark 5.4).
- Remark 2026 on Lemma 5.15 (`rem26:A00-norm`): the claim that any bound better than
  |s_v| < 1/2 suffices was wrong; what is needed is |s_v| != 1/4.
- Remark A.2: the supercuspidal relation (A.4) is false when q = 3 mod 4 (explicit element).
- Section 4.2.5: the weighted orbital integral at central elements diverges as written in
  Draft 3; correction term added.
- Lemma 3.2: stated for all characters (irreducibility not needed). Lemma 3.4: removed a
  duplicated normalizing factor.
- Lemma 2.3(b): the splitting is unique; proof of 2.3(h) added.
- Section 4.7 (Weil representation): kernel corrected off the diagonal; factor 1/2 restored;
  exponent typo in the real elliptic corollary; phase in the n-dimensional Fresnel integral.
- Appendix B: caveat paragraph on omitted terms; A(k) for A(A) in the sums; global volume;
  M_B^T for M_A^T; duplicate clause removed.

Notation and wording
- w_varpi for the matrix (0 varpi; 1 0); calligraphic I for the Iwahori subgroup; Pi(H),
  Pi_u(H), I_A(chi) defined in section 3.1.
- Chai-Zhang statement corrected; Li and Gan-Savin added to the literature review.

### Not done (decisions for the author)

- The "Remark 2026.n" naming is unchanged.
- [J1]: the volume (66 vs 61) was not changed.
- Uncited bibliography entries ([AC], [Bl], [Bo], [HC1], [L2], [Sa], [Sch]) were kept.
- Appendix B was not rewritten into a correct statement of the trace formulas.
- Most overloaded symbols (nu, epsilon, tau, psi, chi, S, T, q) are unchanged.
- The convention v = 1 at the real place in the GL(2) cocycle (section 2.1) is unchecked.

### Material moved from Draft 3

#### Section 1.1 of Draft 3 (status of the main result, with the list of 1995 errors)

```latex
\section{Status of the main result}

This section states what is known about multiplicity one for $SL(2)$, what the 1995 draft claimed, and what this revision proves.


Multiplicity one for the cuspidal spectrum of $SL(2)$ was conjectured
by Labesse and Langlands \cite{LL}, \cite{Lab}, and was proved by
Ramakrishnan \cite{Ra}. D. Blasius has shown that the analog of the
multiplicity one result is false for $SL(n)$, $n>2$ \cite{Blas}.
Strong multiplicity one fails for $SL(2)$ \cite{LL}; Chai and Zhang
\cite{CZ} (see also \cite{Zh}) proved a qualified form of it, for pairs
of cuspidal representations which also agree at the archimedean places
and at the places above $2$. We stress that the following four
properties are different and are not used interchangeably here:
multiplicity one (each cuspidal representation occurs at most once),
strong multiplicity one (a cuspidal representation is determined by
almost all of its local components), the local theta correspondence,
and the description of global near-equivalence classes (``Waldspurger
packets'') on the metaplectic cover \cite{Wa1}, \cite{Wa2}, \cite{PS}.

The 1995 draft of this text claimed an unconditional proof of
multiplicity one for $SL(2)$ by a comparison of trace formulas.
On re-examination, several steps of that argument are incomplete:
\begin{itemize}
\item at the dyadic places, the generalized Hecke algebra argument of the
1995 draft contains errors, and the orbital integral identity it
needed was derived from a global argument that presupposed the
equality of the cuspidal spectral sides (see \S\ref{sec:dyadic});
\item at the archimedean places, the matchings of \S\ref{sec:realA} and
\S\ref{sec:realds} control only some of the representations
(for instance, the elliptic matchings see only functions whose
orbital integrals vanish on the hyperbolic set);
\item at odd places, several of the local character relations are
incomplete (see Remark~\ref{rem:sc-caveat} and
Remark~\ref{rem:savin-caveat}), the correspondence of characters of
the diagonal torus in the 1995 draft was inconsistent when
$(\varpi,\varpi)_2=-1$ (corrected in \S\ref{sec:charsA}), and the
spherical Hecke algebra isomorphism gives the matching of hyperbolic,
but not of elliptic, orbital integrals (Remark~\ref{rem:satake-oi});
\item in the global argument, weighted orbital integrals cannot be
matched for arbitrary corresponding pairs
(Remark~\ref{rem:weighted-noninv}); and the final step of the 1995
argument contained two further gaps (see \S\ref{sec:1995-argument}).
\end{itemize}
This revision therefore states the main result conditionally, and
isolates exactly what is assumed.

Informally, the main result (Theorem~\ref{thm:main}) is as follows.
Fix a cuspidal automorphic representation $\pi=\otimes_v\pi_v$ of
$SL(2,\mathbb{A})$, and let $S=S(\pi)$ be the finite set consisting of the
archimedean places, the dyadic places, and the odd places $v$ at which
$\pi_v$ is not spherical with respect to $K_{0,v}=SL(2,{\cal O}_v)$.
Assume:
\begin{itemize}
\item (Hypothesis~\ref{hyp:GH}) for global functions $f$ on
$SL(2,\mathbb{A})$ and genuine global functions $\overline{f}$ on the cover
which correspond at every place (by the Satake correspondence outside
$S$, and through prescribed local classes of pairs at the places of
$S$), the traces of the cuspidal spectra agree after restriction to
each archimedean infinitesimal character $\nu$:
$\tr R_{cusp}^\nu(f)=\tr \overline{R}{}_{cusp}^{\,\nu}(\overline{f})$;
\item (Hypothesis~\ref{hyp:LH}) at each $v\in S$, the local class of
pairs separates characters, detects $\pi_v$, and transfers each genuine
irreducible representation to at most one irreducible representation
of $SL(2,k_v)$, with only finitely many genuine infinitesimal
characters over each infinitesimal character of $SL(2,k_v)$ when $v$
is archimedean.
\end{itemize}
Then $\pi$ occurs with multiplicity one, and $\pi$ corresponds to a
unique genuine cuspidal automorphic representation $\overline{\pi}$ of
the cover. The local hypothesis is verified here at odd places where
$\pi_v$ is spherical with respect to a hyperspecial maximal compact
subgroup (Proposition~\ref{prop:LH-spherical}).
Chapters \ref{ch:sc} and \ref{ch:local} contain partial results toward
the local hypothesis at other places, which we record together with
their limitations in \S\ref{sec:LH-status}.

The refinement by infinitesimal characters in Hypothesis~\ref{hyp:GH} is
needed because the cuspidal spectrum at a fixed level and with fixed
$K_\infty$-types is infinite (Remark~\ref{rem:why-refine}). Hypothesis~\ref{hyp:GH} is a strong assumption: it
contains most of the global comparison that the 1995 project hoped to
establish.

The proof of Theorem~\ref{thm:main} uses Waldspurger's multiplicity one
theorem for the cover, which is a statement about the space ${\cal A}_{00}$
of genuine cusp forms orthogonal to the elementary theta series. We show
(Lemma~\ref{lem:A00}) that the genuine representations which arise in
the proof lie in ${\cal A}_{00}$; this step uses the Labesse--Langlands
description of the cuspidal spectrum of $SL(2)$ by restriction from
$GL(2)$ and the Gelbart--Jacquet bound toward the Ramanujan conjecture
for $GL(2)$. The proof does not use the failure, or any weak form, of
strong multiplicity one for the cover.

\begin{example}
Let $k={\mathbb Q}$ and let $\pi$ be a cuspidal automorphic representation of
$SL(2,{\mathbb A})$ in the restriction of the representation $\Pi$ of
$GL(2,{\mathbb A})$ generated by the cusp form $\Delta$ of weight $12$. Since
$\Delta$ has level one, $\Pi_p$ is unramified at every prime $p$. If
$\tau(p)\neq0$, the restriction of $\Pi_p$ to $SL(2,{\mathbb Q}_p)$ is
irreducible, so $\pi_p$ has a vector fixed by $SL(2,{\mathbb Z}_p)$. Hence
$S(\pi)$ consists of the real place, the place $2$, and possibly some odd
primes $p$ with $\tau(p)=0$. By Lehmer's conjecture there are no such
primes. We use this $\pi$ as a running example.
\end{example}


```

#### Section 5.4 of Draft 3 (why the 1995 dyadic argument was withdrawn)

```latex
In the 1995 draft, this section attempted to construct, following
Howe and Moy \cite[ch.~3]{HM}, an injection of a metaplectic generalized
Hecke algebra $\overline{\cal H}_k$ (supported on a ``maximal split
subset'' $\overline{G_s}$ of $\overline{G}$) into the generalized Hecke
algebra ${\cal H}(G//B_k)$ of a deep filtration subgroup $B_k$ of the
Iwahori subgroup, and to deduce from it a matching of orbital integrals
and of characters at dyadic places. That argument is withdrawn in this
version, for the following reasons.

\begin{enumerate}
\item The presentation of ${\cal H}(G//B_k)$ included the braid relation
$f_{s_1}*f_{s_2}*f_{s_1}=f_{s_2}*f_{s_1}*f_{s_2}$, where
$s_1=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ and
$s_2=\left(\begin{smallmatrix}0&-\varpi^{-1}\\\varpi&0\end{smallmatrix}\right)$.
Since $s_1s_2=\operatorname{diag}(-\varpi,-\varpi^{-1})$ has infinite order, the affine
Weyl group of $SL(2)$ is infinite dihedral and
$s_1s_2s_1\neq s_2s_1s_2$, so this relation does not hold. (It is the
analog of a relation valid for $GL(n)$, $n\geq 3$.)

\item The set
$X=\{g\in G\ |\ c\in F^{\times 2},\ d=0\ {\rm or}\ d\in F^{\times 2}\}$
was claimed to lie in a maximal subset $G_s$ of $G$ which is closed under
inversion and on which the cocycle $\beta$ is trivial. However, the
lower left entry of $g^{-1}$ is $-c$, so $X$ is not closed under inversion
when $-1\notin F^{\times 2}$ (as for $F={\mathbb Q}_2$), and the proof
computed $\beta(g_1,g_2^{-1})$ rather than $\beta(g_1,g_2)$.

\item The map
$N\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)=
\left(\begin{smallmatrix}a\epsilon_d^{-1}&b\epsilon_c^{-1}\\
c\epsilon_c&d\epsilon_d\end{smallmatrix}\right)$,
where $\epsilon_x$ denotes a fixed representative in ${\cal O}$ of the
square class of $x$, is not defined when $c=0$ or $d=0$, does not
map the Iwahori subgroup into itself when $c$ has odd valuation (since
then $b\epsilon_c^{-1}\notin{\cal O}$ in general), and is not
multiplicative.

\item The restrictions of genuine functions to $\overline{G_s}$ do not
form a convolution algebra, since $G_s$ is not a subgroup. The
computation of $\overline{f}_{g_1}*\overline{f}_{g_2}$ dropped cocycle
factors at points $x$ of $B_kg_2B_k$ outside $G_s$, and the
definition of the functions $\overline{f}_g$ ignored the splitting of
$\overline{B_k}$, which need not be $b\mapsto (b,1)$.

\item An injection of algebras does not by itself induce a map on
irreducible modules, so the claimed surjection
${\cal H}(G//B_k)^\wedge\rightarrow{\cal H}(\overline{G}//B_k)^\wedge$
with matching traces does not follow.

\item The orbital integral identity at a dyadic place was derived from
a global argument which assumed that the spectral sides of the two trace
formulas agree. That agreement is what Chapter~\ref{ch:global} needs to
establish, so the argument is circular.
\end{enumerate}

The generalized Hecke algebra material is revised separately in the
author's paper \cite{J3}.


```

#### Section 7.5 of Draft 3 (remarks on the 1995 argument)

```latex
\section{Remarks on the 1995 argument}\label{sec:1995-argument}

The 1995 draft stated an unconditional theorem asserting, for each
``global transfer'' (a choice of local matchings at all places), a
correspondence between cuspidal automorphic representations of
$G({\mathbb{A}})$ and genuine ones of $\overline{G({\mathbb{A}})}$, and
deduced multiplicity one. Besides its dependence on the local results
discussed in \S\ref{sec:LH-status} and on the trace identity of
Remark~\ref{rem:GH}, the final step of that argument had two gaps.

\begin{enumerate}
\item It fixed a finite set $V$ of places containing the archimedean
places, derived an identity of the form (\ref{eq:S-identity}) with
$S$ replaced by $V$, and then took $V=\{v_0\}$ for a single finite
unramified place $v_0$. This is not permitted, since $V$ must contain the
archimedean places, and the character identities it then used were only
assumed at finite places.

\item To obtain a single genuine representation on the right side of
the identity, it used a count attributed to Waldspurger \cite{Wa2}
(via \cite{PS}) of the genuine cuspidal representations
$\overline{\pi}'$ with $\overline{\pi}'_v\cong\overline{\pi}_v$ for all
$v\notin V$: namely $1$ if $\Sigma\subset V$ and
$2^{|\Sigma|-|\Sigma\cap V|-1}$ otherwise, where $\Sigma$ is the set of
places where $\overline{\pi}_v$ is a discrete series representation and
$|\Sigma\cap V|$ is assumed even. But $V$ was chosen to contain at most
one place of $\Sigma$, so the count as stated is $2^{|\Sigma|-1}$, which
is greater than $1$ as soon as $|\Sigma|\geq 2$.
\end{enumerate}

The proof of Theorem~\ref{thm:main} avoids both points: the set $S$ is
never shrunk, and uniqueness on the metaplectic side comes from the
injectivity in (LH2) together with Waldspurger's multiplicity one
theorem, rather than from a count of near-equivalent representations.

\begin{example}
If $|\Sigma|=3$ and $V\cap\Sigma=\emptyset$, the count quoted in item~2 is
$2^{3-0-1}=4$, so it does not single out one representation.
\end{example}


```

## Draft 3: style-guide pass

Claude, November 20, 2026, at the author's request. Draft 3 brings the text into line with `joyner-math-paper-style-guide.md` (Draft 2 of the guide, November 11, 2026). **No mathematical statement, proof, or hypothesis was changed.** The only exceptions are the reworded sentences listed under "Wording", which remove draft comparisons without changing their content.

The source compiles with `pdflatex` (three passes, 72 pages) with no warnings, no overfull boxes, and no undefined references or citations. The exact checks in `scripts/local_formulas_check.py` pass.

### Changes, by rule of the style guide

- **§1.8 Operators.** sgn, Ind, Cent, vol, diag and Fix are now set with `\operatorname` or `\DeclareMathOperator`. All 67 `\over` fractions were already converted in Draft 2.
- **§1, default preamble.** Added `microtype` and `hyperref` (`hidelinks`). Section titles containing mathematics use `\texorpdfstring`. The fonts stay `mathptmx`, the guide's fallback, because `newtx` is not installed in the build environment, so a newtx build could not be tested.
- **§2.3 Literature review.** New §1.2, split into work before and after 1995. Each cited work gets a one- or two-sentence summary saying how it relates to this text.
- **§2.7 Summary.** New §7.6, "Summary of results and open questions". It lists what is proved, what is assumed, and five open questions.
- **§2.8 Glossary.** New unnumbered chapter before the Acknowledgments. It has 30 entries, each an independent short summary with no cross-references.
- **§2.9, §5.4 Acknowledgments.** Moved from the end of Chapter 1 to the end of the text, before the references. They now state that AI review, including the referee reports, is not an independent certification of the results, and they mention the Draft 3 pass. The abstract's pointer was updated.
- **§3.2 Orienting paragraphs.** Added a one- to three-sentence orienting paragraph to 39 sections and subsections that began directly with a definition or formula.
- **§3.3 Examples.** Added 18 examples, so that every section explaining a concept now has one. The cusp form Δ of weight 12 serves as a running example: Examples 1.1, 7.14, 7.17, 7.18 and 7.20. The new examples:
  - the exceptional set S(π) for Δ, which involves Lehmer's conjecture;
  - an example of the Conventions section;
  - principal series characters vanish on the elliptic set;
  - the complementary series at s = 1/4;
  - depth-zero supercuspidals in Chapter 4 (two examples);
  - the fixed-point counts q = 1 and q + 2;
  - the unit elements as a corresponding pair;
  - the hyperbolic orbital integral of 1_K;
  - Q₂, where (−I,1)² = (I,−1);
  - the Steinberg representation (Iwahori-fixed, not hyperspecial);
  - the Fresnel integral;
  - only the genuine spectrum contributes to the metaplectic trace formula;
  - the reducible unramified principal series and K₀/K₁;
  - the status of the running example at ∞ and at 2;
  - the count 2^{|Σ|−1} with |Σ| = 3;
  - the running example in the summary.

  The numerical and algebraic assertions in these examples are checked by the script (fixed points, Fresnel, Q₂) or are direct consequences of cited facts.
- **§3.8 Semicolons.** 44 semicolons joining clauses in prose were replaced by periods or commas. Semicolons that remain are inside headings of the form "(1995 draft; …)", in list items, and in 1995 text where removing them would change the wording substantially.
- **§4.4, §8.4 Scripts.** New `scripts/local_formulas_check.py`, run by the repository's `run_checks.py`. It gives exact checks of:
  - Lemma 5.3 over ℚ₃, ℚ₅, ℚ₂ and ℝ;
  - Lemma 5.4 over ℚ₃ and ℚ₅;
  - the Hilbert-symbol examples and the ℚ₃ example;
  - Lemma 5.15;
  - the table in the proof of Lemma 5.29, for k = 3, 5, 7, 13;
  - the small examples.

  The paper cites the script in §1.3.
- **§5.1 Author line.** Added `wdjoyner@gmail.com`.
- **§6.3 Title page.** Added a `\thanks` footnote identifying the original manuscript (Scientific Word files `aabook.tex`, `aabook1`–`aabook6`, `aabookrf.tex`, dated April 9, 1995) and this revision. The subtitle is now "Draft 3".
- **§6.4 Revision history out of the body.** Removed 16 draft-to-draft comparisons from the body, such as "(Draft 1 had …)", "(Added in Draft 2.)", "(Added 2026.)" and "(The 1995 draft had a plus sign …)". Where a comparison carried mathematical content, it was rephrased as a plain statement. For example, "a product of the unmodified β_v is not finite", or "matching on a single elliptic Cartan is not enough in the p-adic case". The comparisons themselves are recorded in the Draft 2 section of this log. Three kinds of 1995 material were kept in the body, because they analyze what the 1995 argument gets wrong and not just how the text changed:
  - §5.4, on the dyadic places;
  - §7.5, "Remarks on the 1995 argument";
  - the "1995 draft" provenance tags on unverified statements.
- **§6.6 "Remark 2026.n".** The Draft 2 **Claim** environment is replaced by a separately numbered "Remark 2026.n" environment (no date or color in the label beyond the required "2026"). These items are now Remark 2026.n:
  - the six 1995 Claims;
  - Remarks 5.21 and 5.23 of Draft 2, which contain unverified assertions;
  - the remark on the normalizations in Lemma 7.12;
  - two new remarks, on the discrete-series labels (2026.6) and on the case of the cover in Lemma 7.10 (2026.10).

  §1.3 explains the convention.
- **§6.8, §1.9 Concordance.** See the table below. Theorem and lemma numbers in Chapter 7 are unchanged from Draft 2 (Theorem 7.9, Hypotheses 7.3 and 7.6, Lemma 7.12). The new examples shift the numbers in Chapters 3–5. Moving the Claims to their own counter shifts some numbers after them.

### Wording

The following sentences were reworded only to remove draft comparisons or semicolons. Their mathematical content is unchanged.
- §2.1.2: the remark on pulling back Haar measures to anisotropic tori.
- §2.2: the finiteness of the product of the modified cocycles.
- §5.3.2: why the real matching factor cannot depend on ε.
- §5.3.3: the number of anisotropic Cartan subgroups.
- §5.5: the factor (e^{iθ}+e^{−iθ})^{−1} in Remark 5.27(1).
- §5.7: why the p-adic even Weil representation is not supercuspidal.
- Remark 7.7(1).

### Not changed, by decision or because a rule is marked [DECIDE] or paper-specific

- **Document class (§1, [DECIDE]).** The class stays `book`, the class of the existing file. Numbering is within chapters (Theorem 7.9), which is the book-class form of §1.6.
- **Fonts (§1, [DECIDE]).** The fonts stay `mathptmx`. See above.
- **Citation keys (§1.7).** The keys stay in the 1995 style (Ad1, A2, Fl, GJ78, …). The guide's provenance note says rule 1.7 was stated for one paper only. Changing the keys can be done in a later pass if wanted.
- **Revision log format (§8.2).** The log stays Markdown, `revision_log.md`, as the repository's paper-specific rule (§9) prescribes.
- **Outline and Notation sections (§3.3).** These sections explain no concept, so they have no example.
- **Precise pinpoint citations (§4.3).** Theorem and page numbers were not added for the older 1995 citations. The sources not consulted are listed in the Draft 2 section and in the Draft 1 log.

### New citations in Draft 3

None. The literature review cites only works already in the bibliography. Its summaries of [Wa2], [GPS], [Mo1], [M1], [M2], [JL], [L4], [Sav] and [TW] rest on the descriptions in the 1995 text and in the Draft 1 and Draft 2 logs. The summary of [Ra] rests on its abstract. The summary of [CZ] and [Zh] rests on their abstracts as found during the Draft 2 revision. None of these sources were consulted in full.

### Concordance of numbered items

The table covers every numbered environment. "—" means the item did not exist in that draft. Draft 2's "Claim" items are Draft 3's "Remark 2026.n".

| Draft 1 | Draft 2 | Draft 3 | Label or first words |
|---|---|---|---|
| — | — | Example 1.1 | Let … and let … be a cuspidal automorphic rep… |
| — | — | Example 1.2 | The supercuspidal character relation of the 1… |
| Lemma 2.1 | Lemma 2.1 | Lemma 2.1 | `lem:kubota` |
| Lemma 2.2 | Lemma 2.2 | Lemma 2.2 | `lem:Ainv` |
| Lemma 2.3 | Lemma 2.3 | Lemma 2.3 | `lem:facts` |
| Remark 2.4 | Remark 2.4 | Remark 2.4 | These well-known facts were proven in or foll… |
| — | Example 2.5 | Example 2.5 | The unit element of … (for the measure giving… |
| — | Example 2.6 | Example 2.6 | Let … be places of …. The element of the rest… |
| Lemma 2.5 | Lemma 2.7 | Lemma 2.7 | `lem:Gk-split` |
| Lemma 3.1 | Lemma 3.1 | Lemma 3.1 | There exists a genuine locally constant funct… |
| Lemma 3.2 | Lemma 3.2 | Lemma 3.2 | Assume … and suppose that …. The characte |
| Remark 3.3 | Remark 3.3 | Remark 3.3 | As noted above, on the regular set, this char… |
| Lemma 3.4 | Lemma 3.4 | Lemma 3.4 | If … then [ F^() =|a_1-a_2|J_G(,f), ] for $ |
| — | — | Example 3.5 | Let … and let … with … regular elliptic. Then… |
| Theorem 3.5 | Theorem 3.5 | Theorem 3.6 | (Moen ) If … then … is irreducible for all $ … |
| Lemma 3.6 | Lemma 3.6 | Lemma 3.7 | If … and … then … is unitary. |
| Lemma 3.7 | Lemma 3.7 | Lemma 3.8 | If … and … then there is an irreducible const… |
| — | — | Example 3.9 | Take …. By the lemma on complementary series,… |
| — | — | Example 4.1 | Let … be a cuspidal representation of …, infl… |
| Remark 4.3 | Remark 4.3 | Remark 4.2 | `rem:sc-caveat` |
| — | — | Example 4.3 | For …, a strongly cuspidal representation of … |
| Proposition 4.4 | Proposition 4.4 | Proposition 4.4 | If … is induced from a finite dimensional r |
| Lemma 4.5 | Lemma 4.5 | Lemma 4.5 | Let … and let … _^z(x):=_ |
| — | — | Example 4.6 | The fixed-point count in the proof of the lem… |
| — | — | Example 5.1 | The simplest corresponding pair consists of t… |
| — | — | Example 5.2 | Let … be odd, …, and …. For regular …, the no… |
| — | Lemma 5.1 | Lemma 5.3 | `lem:Acocycle` |
| — | Lemma 5.2 | Lemma 5.4 | `lem:genuine-chars` |
| Definition 5.1 | Definition 5.3 | Definition 5.5 | Let … be given. We say that $_ ( |
| — | Example 5.4 | Example 5.6 | Let …, …, and …. Then …, so $ |
| Definition 5.2 | Definition 5.5 | Definition 5.7 | `def:corrA` |
| Lemma 5.3 | Lemma 5.6 | Lemma 5.8 | `lem:FT-match` |
| Definition 5.4 | Definition 5.7 | Definition 5.9 | We say that … corresponds oddly on the hyperb… |
| Definition 5.5 | Definition 5.8 | Definition 5.10 | We say … correspond evenly on the hyperbolic … |
| — | Remark 5.10 | Remark 5.11 | `rem:weighted-noninv` |
| Proposition 5.7 | Proposition 5.11 | Proposition 5.12 | `prop:hyp-ps` |
| — | Example 5.12 | Example 5.13 | Let …, …, …, and let … be the characteristic … |
| Definition 5.8 | Definition 5.13 | Definition 5.14 | `def:corrA-real` |
| — | Lemma 5.14 | Lemma 5.15 | `lem:realA-match` |
| Definition 5.9 | Definition 5.15 | Definition 5.16 | We say that … corresponds oddly on the hyperb… |
| Remark 5.10 | Remark 5.16 | Remark 5.17 | The 1995 draft added here that, by a direct c… |
| Definition 5.12 | Definition 5.17 | Definition 5.18 | `def:ell-corr` |
| Lemma 5.13 | Lemma 5.18 | Lemma 5.19 | `lem:ell-odd` |
| Lemma 5.14 | Lemma 5.19 | Lemma 5.20 | The set … is in natural 1-1 correspondence wi… |
| — | Definition 5.20 | Definition 5.21 | `def:satake-corr` |
| — | Example 5.22 | Example 5.22 | For the unit elements … and … of the two Heck… |
| Lemma 5.16 | Lemma 5.24 | Lemma 5.23 | Finally, if … are the respective unit element… |
| Remark 5.17 | Remark 5.25 | Remark 5.24 | (1) The construction of does not extend to … … |
| — | — | Example 5.25 | Let …. Since …, the cocycle gives …, s |
| Definition 5.18 | Definition 5.26 | Definition 5.26 | `def:realds-corr` |
| — | Remark 5.27 | Remark 5.27 | `rem:realds-consistency` |
| — | Example 5.28 | Example 5.28 | Let … with … smooth, …-periodic and supp |
| Lemma 5.19 | Lemma 5.29 | Lemma 5.29 | `lem:realds` |
| Remark 5.20 | Remark 5.30 | Remark 5.30 | First, we recall from , page 660, that [ _ _m… |
| Remark 5.23 | Remark 5.33 | Remark 5.31 | `rem:savin-caveat` |
| — | — | Example 5.32 | The Steinberg representation of … has a nonze… |
| Lemma 5.24 | Lemma 5.34 | Lemma 5.33 | If [ g=( cc a & b c & d ) ] has determinant 1 |
| Conjecture 5.25 | Conjecture 5.35 | Conjecture 5.34 | On the regular elements of the ``big cell'' …… |
| Remark 5.26 | Remark 5.36 | Remark 5.35 | This conjecture implies [ c _(g,1) =(-c,-1)|c |
| Lemma 5.27 | Lemma 5.37 | Lemma 5.36 | `lem:gauss` |
| Remark 5.28 | Remark 5.38 | Remark 5.37 | If … is the usual inner product on … then [ _… |
| Proposition 5.29 | Proposition 5.39 | Proposition 5.38 | (Assume the conjecture above.) If … then [ _ … |
| Corollary 5.30 | Corollary 5.40 | Corollary 5.39 | (Assume the conjecture above) If … and … is e… |
| Remark 5.31 | Remark 5.41 | Remark 5.40 | Note that …. According to , page 36, $ |
| Remark 5.32 | Remark 5.42 | Remark 5.41 | This should be compared with the formulas in … |
| Corollary 5.33 | Corollary 5.43 | Corollary 5.42 | (Assume the conjecture above) If … is p-adic … |
| Remark 5.34 | Remark 5.44 | Remark 5.43 | This should be compared with the formulas in … |
| Lemma 5.37 | Lemma 5.45 | Lemma 5.44 | `lem:ds-3/2` |
| Lemma 5.35 | Lemma 5.46 | Lemma 5.45 | If … correspond evenly on the elliptic set in… |
| Remark 5.36 | Remark 5.47 | Remark 5.46 | Indeed, it seems likely that implies that if … |
| Remark 5.39 | Remark 5.49 | Remark 5.47 | If … correspond oddly on the elliptic set the… |
| — | — | Example 5.48 | For …, Lemma is the Fresnel integral $_ Re^ix… |
| Example 6.1 | Example 6.1 | Example 6.1 | Let … |
| Definition 6.2 | Definition 6.2 | Definition 6.2 | Let …. Define … as follows: if …, let … |
| Lemma 6.3 | Lemma 6.3 | Lemma 6.3 | For …, each … is unramified. Moreover, $(A,) |
| — | — | Example 6.4 | Only the genuine part of the cuspidal spectru… |
| Definition 7.1 | Definition 7.1 | Definition 7.1 | `def:exceptional` |
| Definition 7.2 | Definition 7.2 | Definition 7.2 | `def:corresponding` |
| Hypothesis 7.4 | Hypothesis 7.3 | Hypothesis 7.3 | `hyp:LH` |
| — | Definition 7.4 | Definition 7.4 | `def:infchar` |
| — | Example 7.5 | Example 7.5 | Let …, and let … be a cuspidal automorphic re… |
| Hypothesis 7.3 | Hypothesis 7.6 | Hypothesis 7.6 | `hyp:GH` |
| — | Remark 7.7 | Remark 7.7 | `rem:why-refine` |
| Remark 7.5 | Remark 7.8 | Remark 7.8 | `rem:GH` |
| Theorem 7.6 | Theorem 7.9 | Theorem 7.9 | `thm:main` |
| Lemma 7.7 | Lemma 7.10 | Lemma 7.10 | `lem:finiteness` |
| Lemma 7.8 | Lemma 7.11 | Lemma 7.11 | `lem:tensor` |
| — | Lemma 7.12 | Lemma 7.12 | `lem:A00` |
| Remark 7.9 | Remark 7.14 | Remark 7.13 | Hypothesis is only used for … and for pairs w… |
| — | — | Example 7.14 | For the running example … of (from …), … cont… |
| Proposition 7.10 | Proposition 7.15 | Proposition 7.15 | `prop:LH-spherical` |
| Corollary 7.11 | Corollary 7.16 | Corollary 7.16 | `cor:main` |
| — | — | Example 7.17 | Let … be odd and let … be the unramified quad… |
| — | — | Example 7.18 | For the running example, … is one of the disc… |
| — | — | Example 7.19 | If … and …, the count quoted in item2 is …, |
| — | — | Example 7.20 | For the running example … (from …), the open … |
| Proposition 4.1 | Claim 4.1 | Remark 2026.1 | Fix a strongly cuspidal of level … representa… |
| Corollary 4.2 | Claim 4.2 | Remark 2026.2 | Suppose that …. The character relation above … |
| Lemma 5.6 | Claim 5.9 | Remark 2026.3 | `lem:weighted-small` |
| — | Remark 5.21 | Remark 2026.4 | `rem:satake-oi` |
| Remark 5.15 | Remark 5.23 | Remark 2026.5 | `rem:weighted-units` |
| — | — | Remark 2026.6 | `rem26:ds-labels` |
| Theorem 5.21 | Claim 5.31 | Remark 2026.7 | `claim:savin` |
| Corollary 5.22 | Claim 5.32 | Remark 2026.8 | The isomorphism … induces a set-theor |
| Lemma 5.38 | Claim 5.48 | Remark 2026.9 | (a) If … correspond evenly on the elliptic se… |
| — | — | Remark 2026.10 | `rem26:finiteness-cover` |
| — | Remark 7.13 | Remark 2026.11 | The proof of Lemma uses the bound … only thro… |
| Definition 5.11 | removed | removed | We say that … corresponds oddly on … to $ |

## Draft 2: response to the referee report on Draft 1

The source compiles with `pdflatex` (three passes, 64 pages), with no warnings, no overfull boxes, and no undefined references or citations.

### 1. Response to the referee, point by point

| Referee item | Verdict | What was done |
|---|---|---|
| 1.1 False finiteness lemma | **Agree.** At fixed level and fixed K∞-types the cuspidal spectrum is infinite (Weyl law). Harish-Chandra's finiteness holds only once the infinitesimal character is also fixed. | Lemma 7.10 is restated with a fixed archimedean infinitesimal character ν. Hypothesis GH is refined to an identity for each ν (Definition 7.4, Hypothesis 7.6). A new condition (LH4) requires finitely many genuine infinitesimal characters over each linear one. The proof of Theorem 7.9 fixes ν = ν∞(π) and is otherwise unchanged. Remark 7.7 explains why the refinement is needed, shows that the refined GH implies the Draft 1 form, and sketches (without carrying it out) how Arthur's multipliers might derive the refined form from the unrefined one. This is the "strengthening of GH" that the referee anticipated. |
| 1.2 p-adic torus characters inconsistent | **Agree** (checked: (3,3)₃ = −1). | §5.3.1 is rewritten. Lemma 5.1 computes the cocycle on A and shows that conjugation by w sends (a,1) to (a⁻¹,1). Lemma 5.2 proves the genuine-character formula, which Draft 1 left to the reader. The correspondence is now ε = η_ϖ·ϑ with η_ϖ² = (ϖ,ϖ)⁻¹. The Fourier computation is redone with every Hilbert symbol shown; Draft 1 had also dropped the factor (x_a,ϖ)⁻¹ and written ε for ϑ. The matching of functions becomes φ̄ = η_ϖ⁻¹(x_a,ϖ)φ on the odd coset. The new Lemma 5.6 includes a converse and Weyl compatibility. Prop. 5.11 now has a real proof. Two worked examples over ℚ₃ are added. |
| 1.3 Real Hilbert symbol and real matching | **Agree with both parts.** The boxed −i is correct. | The symbol is corrected. Lemma 5.14 proves the matching φ̄ = −iφ for x < 0, as an "if and only if". |
| 1.4 Only one anisotropic Cartan used | **Agree.** | §5.3.3 is rewritten. The Weyl formula sums over all anisotropic Cartans (for p odd, two classes for each of the three quadratic extensions). The definitions require matching on every one of them. Lemma 5.18 states the needed character relation as a hypothesis on every elliptic Cartan. "Vanish off the elliptic set" is replaced by "vanishing hyperbolic orbital integrals". |
| 1.5 Scope of Waldspurger's theorem | **Agree.** The theorem is for 𝒜₀₀; I confirmed this from Piatetski-Shapiro's "Work of Waldspurger" (re-TeXed copy online, Theorem 1.1). | New Lemma 7.12 shows that the π̄′ arising in the proof is not isomorphic to any elementary theta constituent, so all of its copies lie in 𝒜₀₀. The argument uses Labesse–Langlands (π comes from a cuspidal Π on GL(2)), the Gelbart–Jacquet bound \|s\| < 1/4, and the Jacquet module of the even Weil representation (exponent 1/2 versus < 1/2). A remark asks that the normalizations be rechecked. |
| 1.6 Division by 2cos θ | **Agree.** | Definition 5.26 now states the three matchings in multiplied form. Remark 5.27 shows two consequences: Φ_f̄ must vanish over −I, and "even/odd" forces Φ_f to be even or odd under −I, which matches the central characters. Example 5.28 is added. Lemma 5.29 is recomputed with the explicit character substitutions and a table; I verified it symbolically with sympy. **Note:** I fixed the labels as "ε = + means holomorphic". In that convention the 1995 statements differ from mine by ε ↦ −ε together with swapping +odd and −odd, which is an orientation flip. The content is the same, but whether this agrees with Gelbart's labels has not been checked. |
| 1.7 Satake does not give orbital-integral matching | **Agree.** | Remark 5.21: Satake gives the spectral matching, and hyperbolic orbital integrals via F_f = Sf. Elliptic orbital integrals of spherical functions (a fundamental lemma) are not established and are now listed as part of what GH assumes. The Satake correspondence is defined explicitly through the torus matching (Definition 5.20). |
| 1.8 Hecke algebra lacks compact support | **Agree.** I found a second problem in the same definition. | Compact support is now required. Draft 1 imposed bi-K-invariance on f(g,1), but it should be invariance under the splitting κ(K). An example (the unit element) shows why this matters. |
| 1.9a Global cover as a subgroup | **Agree.** | §2.2 is rewritten: the global cover is the restricted product modulo Z₀ = {(ς_v) : ∏ς_v = 1}. The cocycle is written with the modified β′_v, since the product of the unmodified β_v is not finite. An example is added. |
| 1.9b Savin theorem stated as a theorem | **Agree.** | It is now Claims 5.31–5.32 (unverified; PGL(2) versus SL(2)). |
| 1.9c Measures on anisotropic tori | **Agree.** | T(F) is compact, so it is normalized to volume 1. The pull-back construction is withdrawn. |
| §2 Status of Theorem 6.1 | Agree with the referee's description. | The Introduction now says that GH is strong and that Draft 1 overlooked the infinitesimal-character issue. |
| §3 Organization and claims | Agree. | A new §1.2 "Conventions on the status of statements" introduces a **Claim** environment for unverified 1995 statements, with the qualification attached to the statement. Converted to Claims: the supercuspidal proposition and its corollary, the Savin theorem and its corollary, the p-adic non-tempered lemma, and the weighted-orbital-integral lemma. |
| §3 Proofs too short | Partly agree. | The real discrete-series lemma now has a full calculation. The weighted-orbital-integral lemma **cannot be proved as stated** (see §2 below), so it is demoted with an explanation rather than expanded. The real non-tempered lemma now has a proof derived from Lemma 5.29. |
| §3 Notation | Agree. | ϖ is the uniformizer throughout, and π is used only for representations. The set of Cartan representatives is renamed 𝒯. The real/p-adic correspondences χ_i are renamed c_i. The ordinary-character parameter is renamed ϑ. A notation table is added (§1.4). |
| §3 Bibliography and literature | Agree. | Added Chai–Zhang (PJM 285 (2016) 345–374) and Zhang (PJM 292 (2018)). Adams [Ad2] is updated to Duke Math. J. 92 (1998) 129–178. Added Gelbart–Jacquet 1978, Gelbart–Piatetski-Shapiro (Invent. 1980), Harish-Chandra LNM 62, Borel–Jacquet, and Arthur's Paley–Wiener paper. The Introduction now distinguishes multiplicity one, strong multiplicity one, the theta correspondence, and Waldspurger packets. |
| §4 LaTeX | Agree. | `proof:` is replaced by the `proof` environment (17 places). `\tr` is now `\operatorname{tr}`, and every `eqnarray` is now `align`. All 67 `\over` are converted to `\frac`. Overfull boxes: 0. |

### 2. Further corrections not raised by the referee

1. **Weighted orbital integrals (Claim 5.9 / Remark 5.10).** The 1995 lemma says that weighted orbital integrals of *any* corresponding pair correspond. That cannot hold. Adding to f̄ a function ḡ − ḡ^y that has vanishing orbital integrals keeps the pair corresponding, but it changes J_A by ∫ ḡ(x⁻¹ax)(v_A(x) − v_A(xy)) dx, because J_A is non-invariant. The same objection applies to the real remark in §5.3.2. A correct version must restrict to specially constructed pairs or use Arthur's invariant distributions I_M. Neither statement is used in Chapter 7.
2. **Haar measure.** The formula dg = δ_B(a)^{1/2} dk da dn (g = kan) is corrected to δ_B(a) dk da dn.
3. **The p-adic even Weil representation** was called supercuspidal. It is not, since it has a nonzero Jacquet module.
4. **Real non-tempered lemma.** This was stated without proof. It now has a proof from Lemma 5.29 and the Grothendieck-group identities.
5. Smaller fixes: the reference "correspond evenly in the sense of §5.3.3" in the real Weil section now points to the real definition. The garbled formula "F(χ) = (I_A(χ,f))" is cleaned up. Prop. 5.11 is stated as a trace identity.

### 3. Original versus new results

- **From the 1995 draft, corrected:** the character correspondences on A (p-adic and real), the matching definitions, the elliptic and real discrete-series correspondences, the Satake correspondence, and the structure of the conditional argument in Chapter 7.
- **New in Draft 2:** Lemmas 5.1, 5.2, 5.6 and 5.14; the proof of Prop. 5.11; Lemma 5.18 in its corrected form; the computation in Lemma 5.29 and Remark 5.27; the proof of the real non-tempered lemma; Definition 7.4 and the refined Hypothesis 7.6; (LH4); Lemma 7.12; Remarks 5.10, 5.21 and 7.7.

### 4. Sources not consulted directly in this revision

These were cited from memory or from secondary listings and have not been checked against the originals:

- Harish-Chandra LNM 62 and Borel–Jacquet (for the finiteness theorem). It is also unchecked whether Moeglin–Waldspurger covers finite central covers.
- Arthur, Acta Math. 150 (1983), cited for multipliers.
- Gelbart–Jacquet 1978 (the bound |s| < 1/4).
- Gelbart–Piatetski-Shapiro, Invent. Math. 59 (1980) (structure of the elementary theta space).
- Labesse–Langlands (cuspidal π of SL(2) comes from a cuspidal Π of GL(2)).
- Waldspurger [Wa1], whose 𝒜₀₀ scope was confirmed only through Piatetski-Shapiro's exposition.
- Cartier (F_f = Sf for spherical f).
- Gelbart's labels in [Ge2] and Adams' labels in [Ad2].
- Adams [Ad1]. I found no confirmed publication data, so it remains a "preprint".
- Manderscheid [M1]–[M3] and Moen [Mo1]. Their publication data were not updated.
- The page range of Zhang's 2018 PJM paper. I confirmed only the starting page, 283.

### 5. Open items for Draft 3

1. Check the normalizations in Lemma 7.12(ii) against [Ge2] and [GePS].
2. Either carry out the multiplier argument of Remark 7.7(2), or keep the refined GH as an assumption.
3. Correct the supercuspidal character relation (Remark 4.3), on every anisotropic Cartan.
4. Reconcile the discrete-series labels with [Ge2] and [Ad2].
5. Write out the cocycle bookkeeping for F_f̄ = Sf̄ on the cover (Remark 5.21).
6. House style: the per-section examples are now present in Chapters 2, 5 and 7, but not yet in Chapters 3, 4 and 6.

## Draft 1: from the 1995 manuscript to Draft 1

> This is the Draft 1 log as written on November 20, 2026, supplied by the author. Its theorem, section, and line numbers refer to Draft 1 (commit `045016f`), not to Draft 2. Several items it lists as "flagged but not changed" or "not yet done" are addressed in Draft 2 (sections 1 and 2 above). For example, the claim in Chapter 5 that "this defines a character" is now Lemma 5.2, and the 1995 proof sketches are now Claims or have full proofs.

Source: the 1995 Scientific Word manuscript `aabook.tex` with its input files
`aabook1.tex`, `aabook3.tex`, `aabook4.tex`, `aabook2a.tex`–`aabook2e.tex`,
`aabook5.tex`, `aabook6.tex`, `aabookrf.tex` (title-page date 4-9-95).
Output: the single file `multiplicity-one-SL2.tex` (pdflatex, 12pt Times, letter, American English).

### AI usage

- **Carbon (Google Gemini)** refereed the merged 1995 draft (three reports, Nov 20, 2026).
- **Claude (Anthropic)**:
  - merged the source files into one pdflatex file and replaced the Scientific Word macros;
  - assessed Carbon's reports, separating the points that hold from those that don't;
  - made the corrections listed below and rewrote the Introduction, Section 5.4 and Chapter 7 so that the main result is stated conditionally.
- **The author** decided to state the main result conditionally (Nov 20, 2026).

### Decision: conditional main result

The 1995 draft claimed an unconditional proof of multiplicity one for SL(2).
That theorem is true. Labesse and Langlands conjectured it, and Ramakrishnan
proved it (Ann. of Math. 152 (2000)). The 1995 argument, however, has gaps:

- dyadic places (Section 5.4);
- archimedean places;
- several local character relations at odd places;
- the global step in Chapter 7.

Draft 1 replaces it by:

- **Hypothesis 7.3 (GH):** a global trace identity tr R_cusp(f) = tr R̄_cusp(f̄) for corresponding pairs.
- **Hypothesis 7.4 (LH):** local spectral transfer (separation, transfer with injectivity, detection) at each place of S(π).
- **Theorem 7.6:** under GH and LH at the places of S(π), m(π) = 1, and π corresponds to a unique genuine cuspidal π̄.
- **Proposition 7.10:** LH holds at odd places where π_v is K_0- or K_1-spherical.
- **Corollary 7.11:** consequences for π that are hyperspecial-spherical at every odd place.
- **Section 7.4:** what Chapters 3–5 provide toward LH, and what is missing.
- **Section 7.5:** the two gaps in the final step of the 1995 argument.

#### New in Draft 1 versus original

- **New:** the formulation of GH and LH, the proof of Theorem 7.6 (finiteness → Artin's lemma at unramified places → transfer → tensor linear independence → Waldspurger's multiplicity one), Proposition 7.10, Corollary 7.11, and Sections 7.4–7.5. Theorem 7.6 does not use Waldspurger's near-equivalence count.
- **Original (1995), corrected:** Chapters 2–6, apart from Section 5.4 and Section 5.6.

### Changes, by chapter

#### Front matter and Introduction
- Title-page subtitle "Draft 1 / Corrected and expanded version", with the date line "Original draft: 1995. Corrected and expanded draft: 2026".
- The abstract was rewritten. It opens with an AI-disclosure sentence and states the conditional result.
- The Introduction was rewritten and now contains:
  - a new §1.1 on the status of the result (Labesse–Langlands, Ramakrishnan, Blasius, and what is incomplete in 1995);
  - an outline updated to the current chapter numbers;
  - Acknowledgments, now including the AI roles.

#### Chapter 2
- ν(π) = q^{-1} → ν(π) = 1, with |π|_F = q^{-1}.
- In β_1: v(deg g_2, ·) → v(det g_2, ·). Also "cocyle" → "cocycle".
- Non-split torus: a² + b²θ = 1, a,b ∈ F^× → a² − b²θ = 1, a,b ∈ F (the determinant of [[a, bθ],[b, a]]).
- Lemma 2.3(d): a leftover "n = 2" was removed.
- Global cocycle:
  - β_p → β_v.
  - "converges by Lemma 3(b)" was replaced by a remark: one should use the cohomologous cocycle β_v·s_v(g_1)s_v(g_2)s_v(g_1g_2)^{-1}, which is trivial on K_{0,v} × K_{0,v} for almost all v [K2].
  - "an 2-fold" → "a 2-fold".
- Cross-references now use \label/\ref: "equations (2.1-2.3)", "(2.9)", "2.1.4", "Lemma 3(...)", and "part (a) of the above lemma" (the lemma has no parts).
- Typo: "measue" → "measure".

#### Chapter 3
- Typos: "representations theory", "chracter".
- Cross-references now point to the correct chapter.

#### Chapter 4
- σ̄ := σ ⊗ 1 is not genuine. It was replaced by σ ⊗ ε (ε = identity character of μ_2), and μ_n → μ_2.
- Hilbert symbols (·,·)_n → (·,·)_2.
- References to "(2.3)" now point to §2.1 and the multiplication formula.
- Small typos fixed.
- **New Remark 4.3 (caveat):**
  - The splitting K̄_i ≅ K_i × μ_2 is k ↦ (k, s_i(k)), not k ↦ (k, 1).
  - So σ̄((k,ζ)) = ζ s_i(k) σ(k), but the proof treats s_i as trivial.
  - The function (x,ζ) ↦ ζχ_π(x) is not obviously a class function.
  - The proposition is not used in Chapter 7.

#### Chapter 5
- Introduction: the real case now points to §5.3.2 and §5.5, and the p = 2 case to the new §5.4.
- §5.2: "Orbital integrals - vanishing theorems" (there are no vanishing theorems) → "Orbital integrals: definitions".
- The weight v_A was stated for F = Q_p or R as log √|1+n²|_F. That fails p-adically (it is log 0 if n² = −1). It is now:
  - log (1+|n|²)^{1/2} for archimedean F;
  - log max(1, |n|_F) for non-archimedean F.
  - Normalization constants were not rechecked against Arthur.
- The centralizer references were corrected: Lemma 3(h)/(g) → Lemma 2.3(g)/(f) (T̄, Ā abelian).
- "(2.6)" → the conjugation formula plus Lemma 2.3(h).
- "J_M(γ,f)= =lim" → "J_A(γ,f) = lim".
- §5.3.1:
  - "The p=2 case is similar" was removed. It is false as stated: over Q_2, (−I,1)² = (I,−1), so Ā_2(F) is not a direct product.
  - "for n = 2" headings and hypotheses were removed.
  - The definition of corresponding functions on A used f where φ was meant.
- §5.3.2: in the boxed equation, f(a,1) → f̄(a,1).
- §5.3.3: "chapter 4 below" → Chapter 4 above, with a pointer to Remark 4.3.
- **§5.4 (aabook2b.tex) is withdrawn.** It was replaced by a short section listing the reasons:
  - the braid relation is false (s_1s_2 has infinite order);
  - X is not closed under inversion when −1 is a non-square, and the wrong β was computed;
  - N is undefined when c = 0 or d = 0, does not preserve the Iwahori subgroup, and is not multiplicative;
  - restrictions to G_s do not form a convolution algebra, cocycle factors were dropped, and the splitting of B̄_k was ignored;
  - an algebra injection does not induce the claimed map on irreducible modules;
  - the global orbital-integral argument is circular.
  - The section closes with a remark on Takeda–Wood (p = 2, partner SO(3) ≅ PGL(2)).
- **§5.6 (aabook2d.tex):**
  - Savin's theorem and its corollary are kept "as stated in the 1995 draft".
  - New Remark 5.23: in later work the metaplectic cover of SL(2) = Sp(2) is paired with SO(3) ≅ PGL(2), not SL(2), so the statement should be checked against [Sav]. It is not used in Chapter 7.
  - The reference to the withdrawn orbital-integral identity ("§4.4.2") was removed.
  - A missing ^∧ in the corollary was added.
- **§5.7 (aabook2e.tex):**
  - Lemma references were fixed ("Lemma 3" → the Gaussian integral lemma).
  - "in the sense of then" was filled in with §5.3.1 and §5.3.3.
  - "§5.3" → §5.5; "chapter 7 below" → Chapter 4.
  - "Lebesque" → "Lebesgue"; "has be choosen" → "has been chosen".

#### Chapter 6
- Base field: Q was replaced by the number field k throughout, for example M(Q), M_1(Q), A_1(Q), P_1(Q).
- Example 6.1: the weight Σ log √|1+t_v²|_v used the torus parameter t_v. It is now the local weights v_{A,v} of §5.2.1, which are in n_v.
- A doubled comma was removed, and "given by the previous example" was corrected.

#### Chapter 7
- **Rewritten entirely.** The 1995 text is preserved in the original `aabook6.tex`.
- Sign correction: the decomposition-of-measures identity is now (7.1):

  tr R̄(f̄) − tr R(f) = Σ J_χ(f) − Σ J_χ(f̄)

  (the 1995 draft had + in front of the f̄-sum).
- Base field: G(Q)\G(A) → G(k)\G(A).

#### Bibliography
- Added: [Ra] Ramakrishnan 2000; [TW] Takeda–Wood 2018; [J3] Joyner, NYJM 4 (1998), the generalized Hecke algebra paper.
- Restored (cited but commented out in 1995): [Ad1], [H], [Rao], [Shal].
- Typos fixed: "froms", "Irreducibiliy", "Pac. J. Mth.", "Correspondence de Shimura" → "Correspondance", "invarinat", a mismatched quote.

#### Throughout
- archimedian → archimedean; choosen → chosen; Iwawori → Iwahori; arbitary → arbitrary; "the the" → "the"; 1980's → 1980s.

### Flagged but not changed

- **Ch 6, Definition of M_P^T:** the case "χ = (G,ρ), M_B^T = 1" is listed twice. The second case was probably meant for P = B and a different χ.
- **Ch 6:** the factor vol(R/Z) and the J2 date (1996, cited from a 1995 manuscript) are unchanged.
- **Ch 5, §5.3.1:**
  - the claim that the formula defines a character is "left to the reader";
  - "corresponds evenly on the hyperbolic set" is defined via a map t that is introduced only later (§5.3.3).
- **Ch 3:** "the argument of [Ar] sketched above" refers to nothing sketched in the text.
- **Several 1995 proofs** remain "proof: … □" sketches ("a direct calculation", "left to the reader"). These include Lemma 5.6 (weighted orbital integrals for small support) and the claim that every unitary genuine unramified representation is a principal series.
- **Three overfull boxes** (Corollary 5.22, Conjecture 5.25, one display in §6.1) are present in the 1995 layout.

### Sources not consulted directly during this revision

The following were used only as cited in the 1995 text or through their abstracts, not read:

- [Sav] Savin, Local Shimura correspondence;
- [Wa1], [Wa2] Waldspurger;
- [Fl] Flicker;
- [HM] Howe–Moy;
- [M1]–[M3] Manderscheid;
- [GS] Gelbart–Sally;
- [Mo1], [Mo2] Moen;
- [Kut] Kutzko.

In particular:

- The statement of Waldspurger's multiplicity one theorem for the cover, which Theorem 7.6 relies on, was taken from the 1995 text.
- The remark that Savin's partner group is SO(3) ≅ PGL(2) rests on the Takeda–Wood abstract and on the Gan–Savin results it describes.
- Ramakrishnan's theorem was checked against the published abstract (Ann. of Math. 152 (2000) 45–111) and arXiv:math/0007203.

### Style-guide conformance (joyner-math-paper-style-guide.md)

**Done:**
- AI-disclosure opening of the abstract;
- Acknowledgments with AI roles and a pointer to this log;
- Draft/date lines;
- the restriction (conditional result) stated in the abstract and Introduction;
- 12pt Times, letter size, American English, compiles with pdflatex.

**Not yet done:**
- glossary;
- background section more detailed than the glossary;
- at least one example per section;
- a separate literature review section (§1.1 partly serves).

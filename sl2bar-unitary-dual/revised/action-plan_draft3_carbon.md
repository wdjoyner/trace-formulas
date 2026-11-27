<!-- Carbon-Gemini's action plan for Draft 4, written after reviewing Draft 3. Received November 27, 2026. Reproduced as received. The revision log (Section 1) answers it. -->

# Action Plan: Prepare Draft 4 (`sl2-unitary-dual-draft4.tex` + `revision_log.tex`)

Revise the attached Draft 3 manuscript into **Draft 4** alongside a separate LaTeX file **`revision_log.tex`**, adhering strictly to `joyner-math-paper-style-guide.md` and the specific overrides below.

## 1. Move All Revision History & Error Comparisons to `revision_log.tex` (Style Guide §6.4, §8.2)
Shift the focus of the main text entirely to clear mathematical exposition:
* **Title & Footnote:** Update subtitle to `Draft 4. Corrected and expanded version`. Update `\thanks` to identify the July 21, 1999 unpublished manuscript (cited in `\cite{Jo01}`) and Draft 4's date, moving the Draft 1–3 timeline to `revision_log.tex`.
* **Abstract & Section 1:** Remove "Instead we compare each unitary-dual claim..." from the Abstract. Remove **Table 1 (`tab:status`)**, the paragraph *"Relation to the 1999 and 2001 unitary-dual accounts"*, and $s_{\mathrm{old}}$ references from Section 1, relocating them to `revision_log.tex`.
* **Body Cleanup:** Strip comparative/error-tracking commentary from the main text and move to `revision_log.tex`:
  * **Remark `rem:image-jo01`:** Keep the intrinsic 3-quotient normalization comparison (`\eqref{eq:three-quotients}`); move 1999/2001 manuscript comparisons to the log.
  * **Subsection `subsec:complementary` & Remark `uv:complementary`:** Define complementary series and endpoints directly in the paper's parameter $s$ ($s=1$ for odd $n$, $s=1/2$ for even $n$). Move `eq:s-conversion` ($s = d s_{\mathrm{old}}$) and the critique of the unproved 1999 $\mathrm{GL}(2,F)$ extension step to `revision_log.tex`.
  * **Caution `caution:inverse`:** Frame mathematically (why $\operatorname{tr}\chi(a)+\operatorname{tr}\chi(a^{-1})$ fails genuine $\mu_n$-equivariance for $n>2$) without framing it as a correction of 1999 claim (g).
  * **Open Question (1):** Restate directly: *"For $\gcd(p,2n)=1$, determine the exact complementary series intervals, endpoint constituents, and their unitarity for general $n$."*
* **Acknowledgments & Log Deliverables:** Keep a concise AI disclosure in Acknowledgments pointing to `revision_log.tex`. In `revision_log.tex`, include: (a) Table 1 (`tab:status`) and 1999/2001 error-correction notes, (b) original vs. newly established results (§6.5), (c) a section/equation concordance table (§6.8), and (d) exact notes on unconsulted sources (§4.3).

## 2. Structural Reorganization: Fold Literature Review & Notation into Section 1
Override Style Guide §2 top-level ordering as follows (keeping `\label` names stable per §1.9):
* Make **Notation** an unnumbered or numbered subsection of Section 1 (`\subsection{Notation}\label{sec:notation}`), defining core symbols early so they are available before Literature Review and Background.
* Make **Literature review** a subsection of Section 1 (`\subsection{Literature review}\label{sec:literature}`), retaining the pre-1999 and post-1999 split cleanly without subsection numbering clutter (use `\paragraph{Work before 1999.}` and `\paragraph{Work from 1999 on.}`).
* Renumber subsequent top-level sections cleanly: **2. Background**, **3. The covering torus**, **4. Split orbital integrals and their image**, **5. Principal series and known unitary representations**, **6. Principal-series characters**, **7. A restricted and normalized split-torus transfer**, **8. Summary of results and open questions**, **9. Glossary**, **Acknowledgments**, **References**. Update Section 1's Outline paragraph accordingly.

## 3. Cohesive Running Example Strategy (Why NOT $\mathbb{Q}_2$ or $\mathbb{Q}_3$ Alone)
*Note on field choice:* The paper's standing hypotheses require $|\mu_n(F)|=n$ and $\gcd(p,2n)=1$ for the $K$-splitting and trace/transfer theorems.
* **$F=\mathbb{Q}_2$ is excluded** from all main trace/orbital theorems because $p=2$ violates $\gcd(p,2n)=1$ (wild dyadic splitting).
* **$F=\mathbb{Q}_3$** only contains $\mu_2=\{\pm 1\}$ ($q-1=2$), forcing $n=2$. For $n=2$, $d=1$: $\widetilde{A}$ is abelian (hiding the central nonabelian torus phenomenon!) and $n \equiv 2 \pmod 4$ is excluded from Theorem `thm:transfer`.
* **Action:** 
  1. Add a 2-sentence remark in Section 1 (*Standing hypotheses*) explicitly noting why $F=\mathbb{Q}_2$ ($p=2$) and $F=\mathbb{Q}_3$ ($n\le 2$, abelian $\widetilde{A}$) fall outside the nonabelian tame transfer regime.
  2. Use **$F=\mathbb{Q}_5, n=4$ ($d=2$)** or **$F=\mathbb{Q}_7, n=3$ ($d=3$)** as a **single unified running example** across *every* section—picked up in Background, Covering Torus, Orbital Integrals, Principal Series, Characters, Transfer, and summarized in `tab:running`. (Prefer unifying on **$F=\mathbb{Q}_5, n=4, d=2$**—or keeping **$F=\mathbb{Q}_7, n=3, d=3$** and adding an explicit $2\times 2$ or $3\times 3$ matrix realization of $\chi_\lambda(\tilde{h}(\varpi))$ and $\chi_\lambda(\tilde{h}(u))$ in Section `sec:torus` so the reader sees concrete matrices, not just abstract induction.)
  3. Include a brief contrast computation for **$F=\mathbb{Q}_3, n=2$** in Remark `rem:weil` showing explicitly where $\nu(h(t))=(h(t),1)$ fails to be a homomorphism because $\beta(h(3),h(-1))=(-1,3)_2 = -1 \ne 1$.

## 4. Add a Visual TikZ Diagram of the Genuine Unitary Dual
Add `\usepackage{tikz}` (and `\usetikzlibrary{arrows.meta,positioning,decorations.pathreplacing}`) to the preamble. In the Principal Series / Unitary Dual section (`sec:unitary`), include a clean, well-labeled `figure` environment illustrating the genuine unitary dual parameter space (parameterized by $\lambda_s(\zeta\tilde{h}(u)) = \lambda_0(\zeta\tilde{h}(u))|u|^{s/d}$ mod Weyl action $s \leftrightarrow -s$, $\lambda_0 \leftrightarrow \lambda_0^w$):
* **Vertical tempered axis ($\operatorname{Re}(s)=0$,modulo $W$):** Draw a solid vertical line/ray representing unitary principal series $\mathrm{I}(\chi_{\lambda_0})$:
  * Mark generic Weyl-regular points ($\lambda_0^w \ne \lambda_0$) as irreducible unitary points.
  * Mark $\lambda_0^w = \lambda_0$: highlight the split into two inequivalent irreducible tempered summands when $n$ is odd and $\lambda_0$ projects to a nontrivial quadratic character (`GS16`), vs. irreducible when $n$ is even or $\lambda_0$ is trivial.
* **Horizontal real complementary axis ($s \in \mathbb{R}$ for $\lambda_0^w = \lambda_0$):** Draw a horizontal segment `(0, s_0)` ($s_0 = 1/2$ for $n=2$; $s_0 = 1/3$ in Aritürk's normalization / converted $s$ for $n=3$; dashed/shaded for general $n$ to reflect `Remark 2026.n` status) representing the **complementary series**, terminating at **endpoint $s_0$** with two distinct nodes: the square-integrable (Steinberg/Weil-type) subrepresentation and the non-tempered spherical quotient.
* **Discrete isolated cluster:** Draw discrete nodes alongside for **genuine supercuspidal representations** (`Jo99`, `Ma84a`).
* Use visual styling (solid = proved here, dashed = cited/open in general $n$) so the diagram visually encodes both geometry and proof status.

## 5. Fix Style Guide Violations Discovered in Draft 3
Audit and fix every violation below before compiling:
1. **Unnumbered subsections where numbers aren't cross-referenced (§1.6):** Subsection headings like `2.1 Work before 1999`, `2.2 Work from 1999 on`, `5.1 The commutator...`, `6.1 The correct quotient`, `6.2 The constant term...`, `7.2 Reducibility`, `7.5 Supercuspidal...` are never referenced by `\ref`. Convert subsections that have no `\label`/`\ref` to `\subsection*{...}` (or `\paragraph` in Lit Review). Keep numbers *only* on subsections referenced via `\ref` (`subsec:hilbert`, `subsec:kubota`, `subsec:genuine`, `subsec:haar`, `subsec:orbital-linear`, `subsec:ps-linear`, `subsec:svn`, `subsec:complementary`, `subsec:intertwining`).
2. **Missing orienting paragraphs (§3.2):** Every section and subsection MUST open with a short orienting paragraph stating what it does and why:
   * Add an orienting paragraph at the top of **Glossary** (`sec:glossary`).
   * In `subsec:svn`, `subsec:complementary`, `subsec:intertwining`, and `6.2 (The constant term...)`, separate the opening orienting sentences from the mathematical setup/definitions that currently run together in one paragraph.
3. **Every section/subsection needs a concrete example (§3.3):**
   * Add a brief concrete example in `subsec:complementary` (e.g., evaluating $\lambda_s(\tilde{h}(\varpi^d))$ at the endpoint for $n=2$ over $\mathbb{Q}_3$ or $n=3$ over $\mathbb{Q}_7$) — currently it has none.
   * Ensure the Literature Review and Summary sections smoothly connect to the running example.
4. **Precise theorem/section numbers on citations (§4.3):** Fix bare citations lacking specific locators:
   * `\cite{Ne86}` in `subsec:hilbert` $\to$ cite exact chapter/section for Hilbert symbol properties.
   * `\cite{Si79}` at `eq:weyl` $\to$ cite exact theorem/section for the Weyl integration formula.
   * `\cite{BZ76,BZ77}` in `subsec:ps` and `Remark 2026.1` (`uv:geometric`) $\to$ supply exact section/theorem numbers for exactness of Jacquet functor and Frobenius reciprocity, or log any unconsulted source in `revision_log.tex`.
   * `[Mo]` (`\bibitem[Mo]{Mo}`): style guide §1.7 mandates author initials + 2-digit year (`MoXX`). Verify year if known or document the undated preprint exception in `revision_log.tex`.
5. **Script reference (§4.4, §8.4):** Where `scripts/kubota_torus_check.py` is mentioned after Lemma `lem:splitting`, cite the repository path/commit hash placeholder cleanly (note that Lemma `lem:splitting` already has a complete hand proof, which satisfies §4.4).
6. **Compilation check (§1.1–1.4):** Compile both `sl2-unitary-dual-draft4.tex` and `revision_log.tex` with `pdflatex` (twice for refs/TOC). Verify American English spelling, zero undefined references, and zero overfull `\hbox` warnings (rewording rather than inserting manual line breaks). State which **[DECIDE]** defaults were used (`article` class retained from Draft 3; `newtxtext,newtxmath` default; Notation in Sec 1 + Glossary before Acknowledgments).

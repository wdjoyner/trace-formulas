# adjoint-lift

*On the twisted adjoint lifting for p-adic PGL(3)*, by David Joyner, ChatGPT (OpenAI), and Claude (Anthropic), Draft 3 (November 26, 2026). A corrected and expanded version of D. Joyner, "On twisted orbital integral identities for PGL(3) over a p-adic field," Canad. J. Math. 42 (1990), 1098–1130.

## Summary

The symmetric-square (adjoint) lifting from PGL(2) to PGL(3) can be studied through a twisted trace formula for PGL(3), twisted by the outer automorphism g ↦ J ᵗg⁻¹ J. Its two twisted endoscopic groups are SL(2) and PGL(2), and the local input it needs is a pair of fundamental lemmas: identities between twisted orbital integrals on PGL(3) and ordinary orbital integrals on the endoscopic group, for matching spherical functions. The 1990 paper proved these identities for the unit element of the Hecke algebra when the residual characteristic is odd. The SL(2) case follows Langlands' unpublished notes, and the PGL(2) case, which needs a sign (a κ-orbital integral) and a transfer factor, was the paper's own contribution. The method reduces each orbital integral to a count of fixed vertices: of a twisted element on the building of PGL(3), and of the norm element on the tree of PGL(2).

The 2026 revision keeps that argument (Sections 2–4) and adds elementary geometry and combinatorics that explain where its numbers come from (Sections 5–10):

- **Folding and parity.** Duality folds an apartment of the PGL(3) building onto a line. Lattice types modulo 3, and vertex parity on the tree, give necessary conditions for a vertex to be fixed.
- **The normalizing factor.** Q = (1+q⁻¹)(1+q⁻¹+q⁻²) is q⁻³ times the number of complete flags in 𝔽_q³, that is, the Poincaré polynomial of S₃ at q⁻¹.
- **Hecke recurrences.** Distance operators on the tree, and two-step paths in the PGL(3) building, satisfy explicit recurrences.
- **Ball counts.** A ball about a vertex of the tree has qᵐ more vertices than a ball about an edge midpoint, and the two parity classes of a ball of radius m also differ by qᵐ. This is the power qᵐ that appears in the PGL(2) identity.
- **Fixed vertices in the Levi subcomplex.** For block-diagonal representatives, the fixed vertices that lie in the Levi subcomplex are found exactly from the tree (Proposition 5.8).
- **A running example over ℚ₃.** Four explicit elements, with every fixed vertex written down, are carried through the paper. They confirm the unit-element identities in four cases and show several places where the historical text needs to be restated.

The new combinatorial identities do not by themselves prove the signed fundamental lemma. The characteristic-leaf correspondence, the transfer-factor sign, and the measure normalizations remain open obligations, listed in the To Do section.

## Files

| File | What it is |
|---|---|
| `adjoint_lift_revisit.tex`, `.pdf` | The paper |
| `adjoint_lift_revisit_revision_log.tex`, `.pdf` | Revision log: what changed in each draft, a numbering concordance, what is proved and what is only computed, and the AI contributions |
| `scripts/running_example_q3_check.py` | Enumerates the vertices of the building of PGL(3, Q₃) near the standard vertex and lists those fixed by the twisted elements of the paper's running example |

## Status

Working draft, not refereed. The elementary results of Sections 5–9 have complete proofs. The historical building lemmas of Section 2, the transfer-factor sign, and the measure normalizations are not independently verified; the To Do section of the paper lists what remains. The running example confirms the unit-element identities in four cases over Q₃ and records several places where the historical text needs to be restated (see the revision log).

## Running the check

```
python3 scripts/running_example_q3_check.py      # radius 3, a few seconds
python3 scripts/running_example_q3_check.py 4    # radius 4, about a minute
```

It needs only the Python standard library.

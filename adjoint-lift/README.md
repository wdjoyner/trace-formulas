# adjoint-lift

*On the twisted adjoint lifting for p-adic PGL(3)*, by David Joyner, ChatGPT (OpenAI), and Claude (Anthropic), Draft 3 (November 26, 2026). A corrected and expanded version of D. Joyner, "On twisted orbital integral identities for PGL(3) over a p-adic field," Canad. J. Math. 42 (1990), 1098–1130.

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

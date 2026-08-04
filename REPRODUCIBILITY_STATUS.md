# Reproducibility status

**Status: original workflow recovered; clean-machine reproduction pending.**

Recovered materials include the modified CAMB Python/Fortran tree, `sat_locked_background.inc`, final parameter and result cards, spectra, diagnostics, PlanckLens scripts, and official Planck 2018 lensing comparison files.

Validated during packaging:
- Python source syntax checks pass.
- Archived headline-result verification passes.
- A clean Fortran rebuild advanced through the modified equations source; the packaging environment timed out before the final linker stage.

Therefore the repository is substantially reproducible, but should not yet claim independent clean-machine verification until another system completes the build and reruns the full sequence.

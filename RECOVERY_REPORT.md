# Original Computational Materials Recovery Report

Recovered from the user's ChatGPT file library on 2026-08-03.

## Recovered original workflow

- `CAMB_locked_saturation_complete_workflow.zip`
  - modified CAMB Python and Fortran source tree
  - compiled `camb/camblib.so`
  - `fortran/sat_locked_background.inc`
  - modified `fortran/equations.f90` and `fortran/results.f90`
  - CAMB configuration files
  - run scripts, PlanckLens workflow, final spectra, and reports
- `saturation_final_camb_diagnostics_results.zip`
  - final diagnostics JSON/CSV files
  - locked-vs-control spectra
  - derived parameter card
- `saturation_planck_official_lensing_results.zip`
  - official nine-bin Planck 2018 window files
  - covariance and bandpower files
  - locked/control lensing spectra
  - executable bandpower script and final results
- `derived_parameter_card.csv`
- `planck_2018_lensing_bandpower_results.json`

## Important provenance note

These are surviving original generated archives from the earlier computational work, not newly invented replacements. They should be preserved unchanged as provenance artifacts. The separate reconstructed reference repository may be used for simplified inspection, but these recovered archives are the primary source for exact reproduction attempts.

## Recommended next steps

1. Preserve SHA-256 checksums of all recovered archives.
2. Extract the workflow on Linux with Python 3.10+, gfortran, NumPy, SciPy, pandas, Matplotlib, CAMB dependencies, and PlanckLens dependencies.
3. Read the workflow's included README and result reports before rebuilding.
4. Run CAMB tests, then the final theta, diagnostics, and Planck lensing scripts.
5. Compare outputs against the included JSON and CSV result files.

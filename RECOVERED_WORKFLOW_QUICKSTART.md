# Recovered Original Workflow — Quick Start

This repository now contains the surviving original modified CAMB workflow used in the final locked calculation.

## 1. Requirements

- Linux or macOS
- Python 3.10+
- `gfortran`
- NumPy, SciPy, pandas, matplotlib

## 2. Build the recovered CAMB source

```bash
cd original_workflow/CAMB_locked_saturation_complete_workflow
find fortran forutils -type f \( -name "*.d" -o -name "*.o" -o -name "*.mod" -o -name "*.a" -o -name "*.so" \) -delete
rm -rf fortran/Releaselib fortran/Debuglib forutils/Releaselib forutils/Debuglib forutils/Debug
python setup.py make
pip install -e .
```

The clean-source build was exercised during package preparation. Compilation advanced through the modified `fortran/equations.f90` and its included `sat_locked_background.inc`; the validation environment timed out before the complete linker stage, so a full clean-machine rebuild remains an independent check.

## 3. Verify the archived locked result card

```bash
python scripts/verify_recovered_results.py
```

This checks the archived final values for `100 theta_*`, `r_drag`, `sigma8`, `S8`, and lensing chi-square against the manuscript values.

## 4. PlanckLens analytic TT reconstruction

```bash
cd original_workflow/CAMB_locked_saturation_complete_workflow
python scripts/run_plancklens_workflow.py \
  --spectrum inputs/locked_cmb_total_cls.csv \
  --output outputs/plancklens/locked_tt_n0.csv \
  --summary outputs/plancklens/locked_tt_n0.json \
  --lmax-cmb 2048 --lmax-out 400 --lmin-cmb 100 \
  --beam-fwhm 6 --noise-t 35
```

## Provenance

The `original_workflow/` directory contains recovered original source and output files from the earlier calculation. The separate `src/locked_saturation/` package is a later reference reconstruction and should not be confused with the recovered original workflow.

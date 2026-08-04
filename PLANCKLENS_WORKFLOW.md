# PlanckLens reconstruction workflow

This branch adds the uploaded `plancklens` source as an optional stage after the final locked CAMB calculation.

## Scope

The workflow computes quadratic-estimator responses and analytic Gaussian reconstruction noise (`N0`) from CAMB TT/TE/EE/BB spectra. It is useful for locked-versus-control lensing-reconstruction forecasts.

It is **not** the official Planck likelihood and does not replace `clik`/Cobaya likelihood data.

## Included paths

- `vendor/plancklens/` — uploaded PlanckLens source and compiled Fortran response modules.
- `vendor/plancklens_compat/` — minimal `healpy` compatibility layer for analytic spectra-only forecasts.
- `scripts/run_plancklens_workflow.py` — reusable TT quadratic-estimator `N0` driver.
- `inputs/locked_cmb_total_cls.csv` — final F1 locked CAMB lensed CMB spectra.
- `inputs/matched_lcdm_total_cls.csv` — matched flat-LambdaCDM CAMB control spectra.
- `outputs/plancklens/` — smoke-test outputs and summaries.

## Analytic forecast

From the repository root:

```text
python scripts/run_plancklens_workflow.py \
  --spectrum inputs/locked_cmb_total_cls.csv \
  --output outputs/plancklens/locked_tt_n0.csv \
  --summary outputs/plancklens/locked_tt_n0.json \
  --lmax-cmb 2048 --lmax-out 400 --lmin-cmb 100 \
  --beam-fwhm 6 --noise-t 35
```

Run the same command with the matched-control spectrum for a direct reconstruction-noise comparison.

## Full map reconstruction

Install real `healpy`, provide Planck maps/simulations and masks, set `PLENS` to writable storage, and use the PlanckLens parameter files. The compatibility module included here deliberately supports only the spectra-based analytic forecast path.

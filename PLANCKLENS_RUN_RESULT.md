# PlanckLens workflow run result

The uploaded PlanckLens source has been written into the final locked CAMB workflow.

## Executed stage

- Analytic TT quadratic estimator: `ptt`
- CAMB spectra converted from D_ell to C_ell
- Gaussian reconstruction noise N0 computed for locked and matched-control spectra
- CMB lmax: 512
- Reconstruction Lmax: 400
- CMB lmin: 30
- Beam: 6 arcmin
- Temperature noise: 35 uK-arcmin

Both calculations completed with finite outputs.

## Locked versus control

| L_range   |   mean_N0_ratio_locked_over_control |   median_N0_ratio |   min_N0_ratio |   max_N0_ratio |   mean_change_pct |
|:----------|------------------------------------:|------------------:|---------------:|---------------:|------------------:|
| 8-40      |                             1.22321 |           1.22301 |        1.22202 |        1.22513 |           22.3212 |
| 41-100    |                             1.23556 |           1.23409 |        1.22531 |        1.25121 |           23.5563 |
| 101-200   |                             1.27948 |           1.28561 |        1.25194 |        1.29077 |           27.9485 |
| 201-400   |                             1.17078 |           1.18279 |        1.02815 |        1.28569 |           17.0782 |

Mean locked/control N0 ratio over 8 <= L <= 400:

- ratio = 1.212734
- change = +21.273%

The locked spectrum gives a higher TT reconstruction-noise forecast under this common filtering setup. This is a forecast-level diagnostic, not an official Planck likelihood.

## Workflow boundary

The included compatibility layer supports the analytic spectra-only path. Full Planck map reconstruction still requires real `healpy`, Planck maps/simulations, masks, and writable `PLENS` storage.

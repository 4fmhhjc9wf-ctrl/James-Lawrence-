# Final internal CAMB diagnostics

No model parameter was changed. Final F1: a_lock=2.05e-4, blend=0.67 W0, residual factor=1.000, canonical C,phi perturbations.

## Spectral residuals

TT and EE are ordinary fractional RMS residuals. TE uses the stable cross-spectrum metric DeltaTE/sqrt(TT_control EE_control).

| Band     |   ell_min |   ell_max |   TT_RMS_fractional_residual_pct |   TE_RMS_normalized_residual_pct |   EE_RMS_fractional_residual_pct |   TT_mean_fractional_residual_pct |   TE_mean_normalized_residual_pct |   EE_mean_fractional_residual_pct |
|:---------|----------:|----------:|---------------------------------:|---------------------------------:|---------------------------------:|----------------------------------:|----------------------------------:|----------------------------------:|
| Low      |         2 |        29 |                         28.203   |                         12.0318  |                          6.92636 |                         27.8148   |                        11.8059    |                        -6.70582   |
| Acoustic |        30 |       600 |                         10.4141  |                          8.15566 |                          5.93036 |                         -1.45578  |                         1.32124   |                         0.0678384 |
| Damping  |       601 |      1500 |                          2.97862 |                          2.37492 |                          4.23336 |                          0.334195 |                         0.155973  |                         2.27338   |
| High     |      1501 |      2500 |                          1.72588 |                          1.07479 |                          2.24869 |                         -0.162574 |                        -0.0869991 |                        -0.96466   |

## Overall amplitudes and shape

| spectrum   |   best_fit_locked_over_control_amplitude |   post_rescaling_RMS_shape_residual_pct | single_rescaling_description   |
|:-----------|-----------------------------------------:|----------------------------------------:|:-------------------------------|
| TT         |                                 0.945852 |                                 7.89618 | not sufficient                 |
| EE         |                                 1.02326  |                                 4.37061 | not sufficient                 |
| TE         |                                 0.980183 |                                 4.10436 | not sufficient                 |

## Derived-parameter card

| Model                          |   100_theta_star |   r_drag_Mpc |   z_star |   z_drag |   D_A_zstar_Mpc_physical |   D_M_zstar_Mpc_comoving |   sigma8 |   Omega_m |       S8 |   H0_km_s_Mpc |   Omega_b_h2 |   Omega_c_h2 |   n_s |   A_s |   1e9_A_s |   tau |   max_abs_deltaC |   max_abs_deltaphi |   age_Gyr |   r_star_Mpc |    z_eq |
|:-------------------------------|-----------------:|-------------:|---------:|---------:|-------------------------:|-------------------------:|---------:|----------:|---------:|--------------:|-------------:|-------------:|------:|------:|----------:|------:|-----------------:|-------------------:|----------:|-------------:|--------:|
| Final locked F1                |          1.04103 |      149.96  |  1089.69 |  1058.51 |                  12.9568 |                  14131.9 | 0.77968  |  0.314114 | 0.79781  |          67.4 |        0.022 |      0.12005 | 0.965 | 2e-09 |         2 | 0.054 |        0.0351441 |          0.0486029 |   13.9734 |      147.117 | 3395.24 |
| Matched flat LambdaCDM control |          1.04232 |      147.503 |  1090.38 |  1059.07 |                  12.7212 |                  13883.7 | 0.794561 |  0.314114 | 0.813037 |          67.4 |        0.022 |      0.12005 | 0.965 | 2e-09 |         2 | 0.054 |      nan         |        nan         |   13.802  |      144.713 | 3395.24 |

## Decision

The requested internal CAMB campaign is complete. Further quantitative acceptance or exclusion requires external TT/TE/EE and lensing likelihood data.

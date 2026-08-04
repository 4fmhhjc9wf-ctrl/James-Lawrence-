# CMB lensing diagnostic — final cleaned saturation reference

## Run configuration

- a_lock = 2.05e-4
- blend width = 0.67 W0
- residual factor = 1.000
- canonical C, phi perturbations
- CAMB lmax = 2500
- lens_potential_accuracy = 1

## Derived values

| Quantity | Locked | Matched LambdaCDM control |
|---|---:|---:|
| 100 theta_* | 1.041033411 | 1.042322022 |
| r_drag (Mpc) | 149.960135 | 147.502609 |
| sigma8 | 0.779680 | 0.794561 |
| S8 | 0.797810 | 0.813037 |

## Lensing-potential comparison

| ell_range   |   mean_PP_ratio_locked_over_control |   median_PP_ratio |   min_PP_ratio |   max_PP_ratio |   rms_fractional_shape_scatter_pct |   ratio_slope_across_bin |   mean_suppression_or_enhancement_pct |
|:------------|------------------------------------:|------------------:|---------------:|---------------:|-----------------------------------:|-------------------------:|--------------------------------------:|
| 40–100      |                             1.00979 |           1.00956 |        1.00595 |        1.0145  |                          0.249086  |              -0.00854251 |                              0.978717 |
| 100–400     |                             1.00493 |           1.00432 |        1.00209 |        1.01021 |                          0.247037  |               0.0069613  |                              0.493371 |
| 400–1000    |                             1.01823 |           1.01898 |        1.01021 |        1.02293 |                          0.36569   |               0.0126438  |                              1.82267  |
| 1000–2000   |                             1.02231 |           1.02248 |        1.02088 |        1.02319 |                          0.0730036 |              -0.00251283 |                              2.23141  |

Weighted mean PP ratio over 40 <= ell <= 2000:

- locked/control = 1.020886
- change = 2.089%
- shape scatter around one amplitude = 0.645%

For comparison, a simple sigma8-squared rescaling would predict 0.962894.

## Field amplitudes

- max |delta C| = 0.035144
- max |v_C| = 0.037369
- max |delta phi| = 0.048603
- max |v_phi| = 0.066167

## Interpretation

The locked CMB lensing potential is not suppressed by the lower S8. It is mildly enhanced, at roughly the one-to-two percent level depending on multipole, and the ratio is not perfectly scale independent. This is not a catastrophic discrepancy, but it fails the package's hoped-for clean suppression test. The altered distance and growth kernels in the locked background outweigh the naive sigma8-squared expectation.

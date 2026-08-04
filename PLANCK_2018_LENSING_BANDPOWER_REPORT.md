# Planck 2018 lensing bandpower test

## Dataset

Official Planck supplementary conservative lensing dataset:

`smicadx12_Dec5_ftl_mv2_ndclpp_p_teb_consext8_CMBmarged`

- 9 bins
- 8 <= L <= 400
- official bin windows
- official 9 x 9 CMB-marginalized covariance

## Fixed-model results

| Model | chi2 | dof | p-value |
|---|---:|---:|---:|
| Final locked F1 | 10.7379 | 9 | 0.2941 |
| Matched LambdaCDM control | 12.0022 | 9 | 0.2132 |

Delta chi2 (locked minus control):

`-1.2643`

The locked model is modestly better on this direct nine-bin statistic.

## Profiled global lensing amplitude

| Model | best A | chi2 | dof | p-value |
|---|---:|---:|---:|---:|
| Final locked F1 | 1.04357 | 8.3883 | 8 | 0.3965 |
| Matched control | 1.05046 | 8.8939 | 8 | 0.3513 |

## Scope

This is a direct Gaussian likelihood of the published PP bandpowers using the official covariance and window functions. The optional model-dependent linear CMB-response correction from TT/TE/EE is not included, because reproducing that term exactly requires the original CosmoMC likelihood evaluator and its fiducial-spectrum bookkeeping. The CMB-marginalized covariance is used.

|   bin |   L_min |   L_max |   L_eff |   Planck_PP |   Planck_error_display |   locked_PP |   control_PP |   locked_minus_data_sigma_diag |   control_minus_data_sigma_diag |   locked_over_control |
|------:|--------:|--------:|--------:|------------:|-----------------------:|------------:|-------------:|-------------------------------:|--------------------------------:|----------------------:|
|     1 |       8 |      40 |   28.07 |  1.4696e-07 |              1.321e-08 | 1.33547e-07 |  1.31335e-07 |                      -1.00318  |                       -1.16861  |               1.01684 |
|     2 |      41 |      84 |   63.57 |  1.3223e-07 |              6.808e-09 | 1.21335e-07 |  1.20046e-07 |                      -1.55123  |                       -1.73475  |               1.01074 |
|     3 |      85 |     129 |  106.31 |  1.0031e-07 |              5.019e-09 | 9.37441e-08 |  9.32259e-08 |                      -1.27227  |                       -1.37267  |               1.00556 |
|     4 |     130 |     174 |  150.55 |  7.037e-08  |              4.585e-09 | 7.16717e-08 |  7.1474e-08  |                       0.279596 |                        0.237129 |               1.00277 |
|     5 |     175 |     219 |  195.27 |  5.291e-08  |              4.565e-09 | 5.62628e-08 |  5.61401e-08 |                       0.729414 |                        0.702717 |               1.00219 |
|     6 |     220 |     264 |  240.4  |  4.206e-08  |              4.888e-09 | 4.54927e-08 |  4.53491e-08 |                       0.700169 |                        0.670875 |               1.00317 |
|     7 |     265 |     309 |  285.88 |  4.296e-08  |              4.41e-09  | 3.76901e-08 |  3.75024e-08 |                      -1.19251  |                       -1.23498  |               1.005   |
|     8 |     310 |     354 |  331.45 |  3.936e-08  |              4.677e-09 | 3.18086e-08 |  3.15835e-08 |                      -1.61252  |                       -1.6606   |               1.00713 |
|     9 |     355 |     400 |  377.28 |  2.553e-08  |              4.491e-09 | 2.71784e-08 |  2.69303e-08 |                       0.366667 |                        0.311492 |               1.00921 |

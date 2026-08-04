# Planck 2018 lensing compressed-likelihood diagnostic

This run uses the final F1 locked model without retuning.

## Method

The official Planck 2018 `clik` likelihood package is not installed in this runtime, and the uploaded ZIP contains documentation only.  
Therefore this is a **compressed external diagnostic**, not the full Planck likelihood.

Two published Planck 2018 lensing constraints are used:

1. Conservative 8 <= L <= 400 CMB-marginalized lensing amplitude:
   A_phi = 1.011 +/- 0.028.
2. Lensing-only parameter combination:
   sigma8 * Omega_m^0.25 = 0.589 +/- 0.020.

The locked/control C_L^phiphi ratio is compressed over 8 <= L <= 400 using transparent mode-count weights (2L+1).

## Results

| Model                     |   chi2_lensing_amplitude |   Delta_chi2_vs_control |   Aphi_prediction |   sigma8_Omega_m_0p25 |   chi2_combo |
|:--------------------------|-------------------------:|------------------------:|------------------:|----------------------:|-------------:|
| Matched LambdaCDM control |                 0.154337 |                 0       |           1       |              0.594839 |    0.0852223 |
| Locked final F1           |                 0.032767 |                -0.12157 |           1.00593 |              0.583698 |    0.0702815 |

Locked weighted lensing-amplitude ratio over 8 <= L <= 400:

- A_phi,locked / A_phi,control = 1.005932
- shape scatter about one amplitude = 0.446%

Amplitude-only result:

- chi2_control = 0.1543
- chi2_locked = 0.0328
- Delta chi2 = -0.1216

Published lensing-only combination:

- control prediction = 0.594839
- locked prediction = 0.583698
- chi2_control = 0.0852
- chi2_locked = 0.0703
- Delta chi2 = -0.0149

## Interpretation

On the compressed Planck lensing-amplitude statistic, the locked model is slightly closer to the published central amplitude than the matched control.  
On the published sigma8*Omega_m^0.25 statistic, the locked model is slightly worse than the control, but still well within one standard deviation.

These two compressed statistics do not replace the official Planck `clik` likelihood, which also includes band-power covariance and cosmology-dependent normalization corrections.

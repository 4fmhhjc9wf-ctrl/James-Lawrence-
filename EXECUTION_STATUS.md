# Official Planck 2018 lensing likelihood — execution status

The uploaded package was merged into the final F1 CAMB branch.

## What was found

The package contains only:

- README.md
- INSTRUCTIONS.md
- QUICK.md

It does not contain the official Planck likelihood data, Cobaya, a `clik` installation, a Python driver, or executable source patches.

## Environment check

- CAMB 2.0.1: available
- Cobaya: not installed
- GetDist: not installed
- `planck_2018_lensing.native`: not found
- `planck_2018_lensing.CMBMarged`: not found
- Planck likelihood data package: not found

## Result

The official full likelihood was not executed because its external likelihood implementation and data are absent.

No model or cosmological parameter was changed.

The previous compressed Planck lensing diagnostic remains the available result:

- locked/control lensing amplitude: 1.00593
- compressed Δχ² locked minus control: -0.1216

That compressed result is not a replacement for the official likelihood.

## Exact missing dependency

To complete the requested run, provide a Cobaya packages directory containing either:

- `planck_2018_lensing.native`, or
- `planck_2018_lensing.CMBMarged`

together with a working Cobaya installation, or upload a self-contained likelihood package and driver.

# Instructions — Official Planck Lensing Likelihood

## 1. Install / locate the likelihood
If Cobaya is already available:

```bash
# Cobaya will fetch the required data files on first use
# or you can pre-download the Planck 2018 baseline likelihood package
```

The relevant likelihood names are:
- `planck_2018_lensing.native`          (standard)
- `planck_2018_lensing.CMBMarged`       (CMB-marginalized, for pure lensing comparison)

Both implement the official conservative multipole range \(8\le L\le400\).

## 2. Produce the spectra
From the final cleaned CAMB branch (\(a_{\rm lock}=2.05\times10^{-4}\)) and from the matched \(\Lambda\)CDM control, output the lensing potential spectrum \(C_L^{\phi\phi}\) (or the equivalent that Cobaya/CAMB passes to the likelihood) over at least \(L=8\) to \(L=400\).

Keep all other settings identical to the previous final run.

## 3. Evaluate the likelihood
Run the likelihood on both models with identical settings (same \(A_{\rm Planck}\) or calibration treatment if required).

Report:

| Model                  | \(\chi^2_{\rm lensing}\) | \(\Delta\chi^2\) vs control |
|------------------------|---------------------------|-----------------------------|
| Matched \(\Lambda\)CDM |                           | 0                           |
| Locked final F1        |                           |                             |

## 4. Minimal Cobaya-style call (conceptual)
```python
# pseudo-code structure
from cobaya.model import get_model

info = {
    "likelihood": {
        "planck_2018_lensing.native": None
        # or "planck_2018_lensing.CMBMarged": None
    },
    "theory": {
        "camb": {
            "path": "/path/to/your/final_locked_camb",
            "extra_args": { ... your locked settings ... }
        }
    },
    "params": { ... fixed to the final reference values ... }
}

model = get_model(info)
logp_locked = model.loglike(...)   # or the equivalent for fixed spectra
```

(Adjust to whatever interface you already use for feeding pre-computed \(C_\ell\) into the likelihood.)

## 5. Rules
- Do **not** retune any cosmological or saturation parameters.
- Use the exact final cleaned point.
- Document whether you used the standard or the CMB-marginalized version.
- If the full data package cannot be obtained, fall back to the already-completed compressed diagnostic and state that explicitly.

## 6. Expected outcome range
From the compressed test we already know the locked model is ~0.6 % higher in the Planck multipole range and was slightly preferred (\(\Delta\chi^2\sim-0.12\)). The full likelihood should give a result of the same sign and similar magnitude unless the detailed covariance and linear corrections change the picture.
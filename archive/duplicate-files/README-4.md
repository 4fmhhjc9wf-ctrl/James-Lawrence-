# Full Planck 2018 Lensing Likelihood Integration

**Goal**  
Replace the previous compressed diagnostic with the official Planck 2018 lensing likelihood (conservative MV, \(8\le L\le400\)) evaluated on the final cleaned locked model and on the matched \(\Lambda\)CDM control.

**Recommended practical route**  
Use Cobaya’s native implementation (`planck_2018_lensing.native` or `planck_2018_lensing.CMBMarged`). It does not require compiling the old clik library and is the modern standard way to run the official Planck lensing likelihood.
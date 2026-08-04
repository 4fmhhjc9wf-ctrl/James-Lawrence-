from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import chi2 as chi2_dist

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
locked = pd.read_csv(HERE / "lensing_locked.csv").set_index("ell")
control = pd.read_csv(HERE / "lensing_control_clean.csv").set_index("ell")
bp = np.loadtxt(DATA / "smicadx12_Dec5_ftl_mv2_ndclpp_p_teb_consext8_bandpowers.dat")
obs = bp[:, 4]
cov = np.loadtxt(DATA / "smicadx12_Dec5_ftl_mv2_ndclpp_p_teb_consext8_CMBmarged_cov.dat")
inv = np.linalg.inv(cov)

def bin_pp(spec):
    out = []
    for i in range(1, 10):
        w = np.loadtxt(DATA / f"window{i}.dat")
        ell = w[:, 0].astype(int)
        out.append(np.sum(w[:, 1] * spec.loc[ell, "PP"].to_numpy()))
    return np.asarray(out)

for name, spec in [("locked", locked), ("control", control)]:
    pred = bin_pp(spec)
    delta = pred - obs
    chi2 = float(delta @ inv @ delta)
    print(name, "chi2=", chi2, "p=", chi2_dist.sf(chi2, 9))

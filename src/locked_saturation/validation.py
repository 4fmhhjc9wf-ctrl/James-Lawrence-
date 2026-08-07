import math
LOCKED={
'acoustic_scale':1.041033,'reference_acoustic_scale':1.0411,
'omega_m0':0.314114,'sigma8':0.779680,'S8':0.79781,
'lensing_chi2':10.7379,'control_lensing_chi2':12.0022,
'DM_star':14131.86,'z_star':1089.691,'DA_star':12.9568,
}

def locked_arithmetic():
    acoustic_pct=(LOCKED['acoustic_scale']-LOCKED['reference_acoustic_scale'])/LOCKED['reference_acoustic_scale']*100
    s8=LOCKED['sigma8']*math.sqrt(LOCKED['omega_m0']/0.3)
    delta=LOCKED['lensing_chi2']-LOCKED['control_lensing_chi2']
    da=LOCKED['DM_star']/(1+LOCKED['z_star'])
    return {'acoustic_fractional_percent':acoustic_pct,'S8_recomputed':s8,
            'lensing_delta_chi2':delta,'DA_star_recomputed_Mpc':da}

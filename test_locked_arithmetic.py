from locked_saturation.validation import locked_arithmetic

def test_reported_arithmetic():
 x=locked_arithmetic()
 assert abs(x['acoustic_fractional_percent']-(-0.0064355))<1e-5
 assert abs(x['S8_recomputed']-0.79781)<2e-6
 assert abs(x['lensing_delta_chi2']-(-1.2643))<1e-10
 assert abs(x['DA_star_recomputed_Mpc']-12.9568)<1e-4

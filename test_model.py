import numpy as np
from locked_saturation.model import ModelParameters,potential,potential_grad,auxiliaries,rhs

def test_minimum():
 p=ModelParameters(); assert potential_grad(p.C_s,0,p)==(0.0,0.0); assert abs(potential(p.C_s,0,p)-p.V_inf)<1e-14

def test_expansion_transfer_zero():
 p=ModelParameters(); y=np.array([1,1,p.C_s,0,0,0,0.3,1e-4]); assert auxiliaries(y,p)['gamma']==0

def test_rhs_finite():
 p=ModelParameters(); y=np.array([1,-1,p.C_s,0.1,0.1,0.1,1,10]); assert np.isfinite(rhs(0,y,p)).all()

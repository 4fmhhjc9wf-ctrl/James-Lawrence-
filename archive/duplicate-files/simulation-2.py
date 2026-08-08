from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from .model import ModelParameters, rhs, auxiliaries, friedmann_residual


def demo_initial_state(p:ModelParameters)->np.ndarray:
    """Construct a consistent demonstrative contracting state near saturation.

    This is not claimed to be the manuscript's unavailable original initial state.
    """
    a=2.2e-5; C=0.918318; PiC=0.055327; phi=0.02; Piphi=0.01
    # assign most density to radiation near 0.995 rho_s
    rho_target=0.995*p.rho_s
    field=0.5*(PiC**2+Piphi**2)+__import__('locked_saturation.model',fromlist=['potential']).potential(C,phi,p)
    rho_m=1e-6*rho_target
    rho_r=rho_target-rho_m-field
    h2=(rho_target/3)*(1-rho_target/p.rho_s)
    H=-np.sqrt(max(h2,0.0))
    return np.array([a,H,C,PiC,phi,Piphi,rho_m,rho_r],float)


def integrate(method:str='DOP853',t_end:float=2e-5,p:ModelParameters|None=None):
    p=p or ModelParameters(); y0=demo_initial_state(p)
    def bounce(t,y): return y[1]
    bounce.direction=1; bounce.terminal=False
    sol=solve_ivp(lambda t,y:rhs(t,y,p),(0,t_end),y0,method=method,rtol=1e-10,atol=1e-12,
                  max_step=t_end/3000,events=bounce,dense_output=False)
    rows=[]
    for i,t in enumerate(sol.t):
        y=sol.y[:,i]; q=auxiliaries(y,p)
        rows.append(dict(t=t,a=y[0],H=y[1],C=y[2],PiC=y[3],phi=y[4],Piphi=y[5],
                         rho_m=y[6],rho_r=y[7],rho_C=q['rho_C'],rho=q['rho'],p=q['pressure'],
                         gamma=q['gamma'],constraint_residual=friedmann_residual(y,p)))
    return sol,pd.DataFrame(rows)


def write_run(outdir:Path,method:str='DOP853'):
    outdir.mkdir(parents=True,exist_ok=True)
    sol,df=integrate(method=method)
    df.to_csv(outdir/f'background_{method.lower()}.csv',index=False)
    summary={'method':method,'success':bool(sol.success),'message':sol.message,'n_steps':len(sol.t),
             'bounce_times':[float(x) for x in (sol.t_events[0] if sol.t_events else [])],
             'max_abs_constraint_residual':float(df.constraint_residual.abs().max()),
             'max_normalized_constraint_residual':float((df.constraint_residual.abs()/df[['H','rho']].assign(H2=df.H**2,rho3=df.rho/3)[['H2','rho3']].max(axis=1).clip(lower=1.0)).max()),
             'min_scale_factor':float(df.a.min()),'final_H':float(df.H.iloc[-1])}
    import json
    (outdir/f'summary_{method.lower()}.json').write_text(json.dumps(summary,indent=2))
    return summary

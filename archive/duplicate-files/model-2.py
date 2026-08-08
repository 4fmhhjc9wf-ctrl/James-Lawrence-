"""Core equations transcribed from Appendix A/B of the manuscript.

This module implements the effective background system. It does not claim to
reconstruct the unavailable original source code or modified CAMB patch.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

@dataclass(frozen=True)
class ModelParameters:
    V_inf: float = 2.187987
    rho_s: float = 1.58199e15
    mC2: float = 1.827221
    lam: float = 0.802722
    C_s: float = 0.95
    A0: float = 1.0
    gamma0: float = 0.2
    rho_gamma: float = 1.0e12
    transfer_power: float = 4.0
    H_c: float = 1.0e5


def potential(C: float, phi: float, p: ModelParameters) -> float:
    d = C - p.C_s
    return p.V_inf + 0.5*p.mC2*d*d + 0.25*p.lam*d**4 + p.A0*(1.0-math.cos(phi))


def potential_grad(C: float, phi: float, p: ModelParameters) -> tuple[float,float]:
    d = C - p.C_s
    return p.mC2*d + p.lam*d**3, p.A0*math.sin(phi)


def transfer_selector(H: float, p: ModelParameters) -> float:
    if H >= 0.0:
        return 0.0
    x = H/p.H_c
    # stable logistic 1/(1+exp(x))
    if x > 700: return 0.0
    if x < -700: return 1.0
    return 1.0/(1.0+math.exp(x))


def transfer_rate(H: float, rho_m: float, rho_r: float, p: ModelParameters) -> float:
    if H >= 0.0:
        return 0.0
    Wm = transfer_selector(H,p)
    ratio=max((rho_m+rho_r)/p.rho_gamma,0.0)
    s = ratio**p.transfer_power/(1.0+ratio**p.transfer_power)
    return Wm*(-3.0*H + p.gamma0*s)


def auxiliaries(y: np.ndarray, p: ModelParameters) -> dict[str,float]:
    a,H,C,PiC,phi,Piphi,rho_m,rho_r = map(float,y)
    K2=PiC*PiC+Piphi*Piphi
    V=potential(C,phi,p)
    rho_C=0.5*K2+V
    p_C=0.5*K2-V
    rho=rho_m+rho_r+rho_C
    pressure=rho_r/3.0+p_C
    gamma=transfer_rate(H,rho_m,rho_r,p)
    h2_constraint=(rho/3.0)*(1.0-rho/p.rho_s)
    return dict(K2=K2,V=V,rho_C=rho_C,p_C=p_C,rho=rho,pressure=pressure,
                gamma=gamma,h2_constraint=h2_constraint)


def rhs(t: float, y: np.ndarray, p: ModelParameters) -> np.ndarray:
    a,H,C,PiC,phi,Piphi,rho_m,rho_r = map(float,y)
    q=auxiliaries(y,p)
    dVC,dVphi=potential_grad(C,phi,p)
    g=q['gamma']; rho=q['rho']; pressure=q['pressure']
    return np.array([
        a*H,
        -0.5*(rho+pressure)*(1.0-2.0*rho/p.rho_s),
        PiC,
        -(3.0*H+g)*PiC-dVC,
        Piphi,
        -(3.0*H+g)*Piphi-dVphi,
        -3.0*H*rho_m,
        -4.0*H*rho_r+g*q['K2'],
    ],dtype=float)


def friedmann_residual(y: np.ndarray,p:ModelParameters)->float:
    q=auxiliaries(y,p)
    return float(y[1]**2-q['h2_constraint'])

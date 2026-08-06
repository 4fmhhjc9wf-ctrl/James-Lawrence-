"""Locked Saturation Cosmology: Effective background model implementation.

This package implements the effective background equations documented in
Appendices A and B of the manuscript, providing:

- ModelParameters: Configuration for the canonical two-field potential
- potential(): The effective potential V(C, phi)
- potential_grad(): Derivatives of V with respect to (C, phi)
- auxiliaries(): Derived quantities (densities, pressure, constraints)
- rhs(): Right-hand side of the evolution equations
- friedmann_residual(): Friedmann constraint diagnostic

The simulation module provides numerical integration using scipy.integrate.solve_ivp.
The validation module contains regression tests against reported values.
"""

__version__ = "1.0"

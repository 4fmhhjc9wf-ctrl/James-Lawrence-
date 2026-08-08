# Executive Summary

**Locked Saturation Cosmology / Gravitational Saturation**

This is the browser-readable version of the Executive Summary and is intended to work well on desktop and mobile devices.

Locked Saturation Cosmology is a computationally implemented phenomenological gravitational model being investigated as a possible common description of galaxy-scale mass discrepancies and late-time cosmological acceleration.

The purpose of this repository is to make the proposal inspectable, reproducible, and independently testable.

## Core formulation

The current formulation uses a saturation variable `C`:

```text
μ(C) = 1 - C
```

with

```text
0 ≤ C < 1
```

A stable residual potential is represented locally by

```text
V(C) = V∞ + 1/2 m²(C - C*)²
```

with

```text
C* < 1
m² > 0
```

After freeze-out, the background cosmological implementation uses

```text
H² = (8π G_eff / 3) (ρ_m + ρ_r + V∞)
```

with

```text
G_eff = G / μ*
μ* = 1 - C*
```

The weak-field phenomenological response currently used in the galaxy-scale implementation is

```text
μ(x) = x / sqrt(1 + x²)
```

The implementation has undergone internal numerical and computational checks, but those checks are not presented as independent confirmation of the physical theory.

Independent reproduction, observational comparison, statistical model comparison, perturbation analysis, lensing, structure growth, and falsification remain appropriate scientific tests.

---

## Document options

**[Open formatted Executive Summary PDF](https://cdn.jsdelivr.net/gh/4fmhhjc9wf-ctrl/James-Lawrence-@main/docs/reviewer/Executive_Summary.pdf)**

The page you are currently reading is the recommended mobile-friendly version.

[Back to main repository](../../README.md)

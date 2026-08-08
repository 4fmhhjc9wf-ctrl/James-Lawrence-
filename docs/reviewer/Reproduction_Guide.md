# Reproduction Guide

This page provides a browser-readable starting point for reproducing the computational work.

## Minimum independent reproduction

A reviewer should determine:

1. whether the locked arithmetic tests reproduce;
2. whether the model tests reproduce;
3. whether the code implements the documented equations;
4. whether reported galaxy-scale outputs can be regenerated;
5. whether cosmological calculations can be regenerated;
6. whether the Fortran/CAMB implementation compiles and behaves as documented;
7. whether reported results survive reasonable robustness tests; and
8. whether an independently written implementation produces compatible results.

## Core implementation

```text
src/locked_saturation/
```

## Primary Locked Saturation tests

```text
test_model.py
test_locked_arithmetic.py
```

## Important principle

Independent evaluation should rely on checked-in source, documented inputs, scripts, tests, and regenerated outputs rather than screenshots or reported numerical values alone.

A failure to reproduce a calculation should be recorded as a result.

---

**[Open the formatted Reproduction Guide PDF](Reproduction_Guide.pdf?raw=1)**

[Back to main repository](../../README.md)

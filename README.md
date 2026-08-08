# Locked Saturation Cosmology

**Computational Implementation, Manuscript, and Independent Review Materials**

**Author:** James Lawrence  
**Affiliation:** Independent Researcher

This repository contains the current computational implementation and review package for **Locked Saturation Cosmology / Gravitational Saturation**, a phenomenological gravitational model being tested as a possible common description of galaxy-scale mass discrepancies and late-time cosmological acceleration.

The purpose of this repository is to make the proposal **inspectable, reproducible, and independently testable**.

The calculations and validation contained here demonstrate what the present implementation does. They should not be interpreted as independent confirmation of the physical theory. Independent reproduction, observational comparison, and scientific criticism remain essential.

---

## Start Here

> **PDF note:** The links below open the original PDF files directly. This avoids GitHub's built-in PDF preview, which may fail on some mobile browsers even when the PDF itself is valid.

If you are encountering this project for the first time, the recommended reading order is:

1. **[Executive Summary](https://raw.githubusercontent.com/4fmhhjc9wf-ctrl/James-Lawrence-/main/docs/reviewer/Executive_Summary.pdf)**  
   Short overview of the hypothesis, implementation, and current results.

2. **[Independent Reviewer Guide](https://raw.githubusercontent.com/4fmhhjc9wf-ctrl/James-Lawrence-/main/docs/reviewer/Independent_Reviewer_Guide.pdf)**  
   What should be checked and how to approach an independent evaluation.

3. **[Reviewer Roadmap](https://raw.githubusercontent.com/4fmhhjc9wf-ctrl/James-Lawrence-/main/docs/reviewer/Reviewer_Roadmap.pdf)**  
   Navigation through the repository and validation material.

4. **[Technical Synopsis](https://raw.githubusercontent.com/4fmhhjc9wf-ctrl/James-Lawrence-/main/docs/reviewer/Technical_Synopsis.pdf)**  
   Compact technical description of the current model.

5. **[Reproduction Guide](https://raw.githubusercontent.com/4fmhhjc9wf-ctrl/James-Lawrence-/main/docs/reviewer/Reproduction_Guide.pdf)**  
   Instructions for independently reproducing the computational checks.

6. **[QA Audit](https://raw.githubusercontent.com/4fmhhjc9wf-ctrl/James-Lawrence-/main/docs/reviewer/QA_Audit.pdf)**  
   Quality-assurance and validation material.

7. **[Current Manuscript — Review Copy](https://raw.githubusercontent.com/4fmhhjc9wf-ctrl/James-Lawrence-/main/docs/reports/Locked_Saturation_Cosmology_v1.1_Review_Copy.pdf)**  
   Long-form presentation of the model and its interpretation.

---

## What Is Being Tested?

The working hypothesis is that gravitational response has a finite saturation degree of freedom.

In the current formulation, a saturation variable `C` modifies gravitational response through

```text
μ(C) = 1 - C
```

with

```text
0 ≤ C < 1.
```

A stable residual potential is represented locally by

```text
V(C) = V∞ + 1/2 m²(C - C*)²
```

with

```text
C* < 1
m² > 0.
```

After freeze-out, the background cosmological implementation takes the form

```text
H² = (8π G_eff / 3) (ρ_m + ρ_r + V∞)
```

with

```text
G_eff = G / μ*
```

and

```text
μ* = 1 - C*.
```

For the weak-field phenomenological response currently used in the galaxy-scale implementation,

```text
μ(x) = x / sqrt(1 + x²).
```

The central question is whether a compact gravitational-saturation framework can continue to reproduce relevant behavior across different gravitational regimes without requiring a separate adjustable mechanism for each scale.

---

## Current Scientific Status

This project should presently be regarded as a:

**Computationally implemented phenomenological model undergoing independent evaluation.**

The repository contains numerical tests, diagnostic outputs, galaxy-scale work, cosmological calculations, CAMB/Fortran integration, reproducibility material, and reviewer-facing documentation.

The implementation has survived a number of internal numerical and computational checks.

That is significant for evaluating the implementation, but it is **not equivalent to independent confirmation of the physical theory**.

Questions that remain appropriate for independent investigation include:

- independent reproduction of the reported calculations;
- observational model comparison;
- parameter inference and statistical comparison with established models;
- full perturbation behavior;
- theoretical consistency of the complete dynamical system;
- lensing and structure-growth predictions;
- robustness against independent numerical implementations;
- identification of observations capable of falsifying the model.

These are scientific questions rather than repository-cleanup questions, and they should remain open until independently tested.

---

## Repository Map

The repository is organized so that scientific documentation and generated results can be separated from the underlying computational source.

```text
.github/workflows/
    Automated validation and maintenance workflows

archive/
    Archived duplicate or legacy material retained where useful for provenance

docs/reviewer/
    Executive summary
    Independent reviewer guide
    Reviewer roadmap
    Technical synopsis
    Reproduction guide
    QA audit

docs/reports/
    Current manuscript
    Longer technical reports
    Supporting PDF and TeX material

docs/research-notes/
    Dated research and development notes

notebooks/
    Jupyter notebooks

results/diagnostics/
    Generated diagnostic and result files

scripts/
    Reproduction, analysis, and utility scripts

src/locked_saturation/
    Core Locked Saturation Python implementation
```

The repository root also contains CAMB/Fortran source and build files required by the computational implementation.

Those files are intentionally left in their validated build locations rather than being moved merely for cosmetic organization.

---

## Core Implementation

The principal Locked Saturation Python package is located at:

```text
src/locked_saturation/
```

The primary Locked Saturation validation tests are:

```text
test_model.py
test_locked_arithmetic.py
```

The repository also contains the Fortran/CAMB implementation and associated build infrastructure used for cosmological calculations.

---

## Automated Validation

The active GitHub Actions setup has intentionally been reduced to three workflows.

### `python-tests.yml`

Routine continuous validation.

It checks the Locked Saturation Python implementation and tests across the supported Python environments and performs associated syntax/toolchain checks.

### `full-fortran-build.yml`

Deeper Fortran/CAMB build validation.

This workflow exists to verify that the cosmological implementation can still be built from the checked-in source.

### `authoritative-repository-cleanup-v7.yml`

Manual repository-maintenance and deep-validation workflow.

This is **not part of the physical model**.

It was retained because it provides a known maintenance path that can isolate the Locked Saturation tests, validate the Python implementation, and perform a full CAMB/Fortran build without contaminating the repository worktree with temporary build products.

---

## Reproducing the Work

A reviewer should begin with the:

**[Reproduction Guide — Open PDF Directly](https://raw.githubusercontent.com/4fmhhjc9wf-ctrl/James-Lawrence-/main/docs/reviewer/Reproduction_Guide.pdf)**

and then work from the checked-in implementation, scripts, tests, and documented inputs.

Independent evaluation should not rely solely on screenshots, summaries, or reported numerical values.

At minimum, an independent reproduction should determine:

1. whether the locked arithmetic tests reproduce;
2. whether the model tests reproduce;
3. whether the implementation actually corresponds to the equations stated in the documentation;
4. whether the reported galaxy-scale outputs can be regenerated;
5. whether the cosmological calculations can be regenerated;
6. whether the Fortran/CAMB implementation compiles and behaves as documented;
7. whether reported results survive reasonable robustness tests; and
8. whether an independently written implementation produces compatible results.

A failure to reproduce a result is useful information and should be documented rather than hidden.

---

## How the Results Should Be Interpreted

There are three different things in this repository that should not be confused with one another.

### 1. The equations and implementation

These can be inspected directly.

A reviewer can determine whether the source code implements the equations it claims to implement.

### 2. The computational results

These can be reproduced, challenged, or falsified numerically.

A successful calculation establishes that the implementation produced that result under the stated conditions.

### 3. The physical interpretation

This requires independent scientific judgment.

Agreement between a calculation and an observation does not by itself establish that the proposed physical explanation is unique or correct.

The model therefore should ultimately be judged not by the confidence of its presentation, but by whether its equations and predictions continue to survive independent attempts to reproduce and falsify them.

---

## Why the Repository Contains CAMB Source

Part of this project involves testing the cosmological implementation within a CAMB/Fortran environment.

Consequently, the repository contains a substantial amount of Fortran source and supporting material associated with that computational framework.

Those files should not be mistaken for newly authored components of the Locked Saturation hypothesis merely because they are present in the repository.

The model-specific implementation, modifications, documentation, tests, and results should be distinguished from the upstream scientific software infrastructure on which portions of the numerical work depend.

Applicable upstream attribution and licensing requirements should be preserved.

---

## Independent Review

Independent reproduction and criticism are explicitly welcome.

Useful criticism should, wherever possible, identify the specific:

- equation;
- assumption;
- parameter;
- dataset;
- numerical method;
- implementation choice;
- statistical comparison; or
- reported result

that is being challenged.

That allows disagreements to become testable questions.

If the model fails a legitimate independent test, that failure belongs in the scientific record of the project.

If it survives, that result should likewise be documented without claiming more than the test establishes.

---

## A Note on the Origin of the Project

This work was developed outside a conventional academic research program.

Computational intelligence has been used as a formalization, programming, checking, and analysis tool during development.

The physical hypothesis, mechanical interpretation, selection of questions being investigated, and responsibility for the claims presented as the author's are those of **James Lawrence**.

The use of computational tools is disclosed so that reviewers can judge the work from its equations, implementation, reproducibility, and empirical performance rather than from assumptions about how the mathematics or code were produced.

No institutional authority is offered as evidence that the model is correct.

The repository is provided so that the work can instead be examined directly.

---

## Citation

Citation metadata is provided in:

[`CITATION.cff`](CITATION.cff)

Please use the repository's current citation information when referring to this implementation.

---

## Licensing and Attribution

Licensing information is contained in the repository's license files.

Because this repository incorporates and modifies existing scientific software infrastructure, downstream users should preserve all applicable upstream copyright notices, attribution, and licensing requirements.

---

## Bottom Line

This repository presents a specific gravitational hypothesis in a form intended to be run rather than merely discussed.

The implementation exists.

The tests can be inspected.

The calculations can be rerun.

The assumptions can be challenged.

The remaining question is whether the model continues to survive when those checks are performed independently.

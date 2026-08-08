# Reviewer Roadmap

This page provides browser-readable navigation through the review package.

## Recommended order

1. [Executive Summary](Executive_Summary.md)
2. [Independent Reviewer Guide](Independent_Reviewer_Guide.md)
3. [Technical Synopsis](Technical_Synopsis.md)
4. [Reproduction Guide](Reproduction_Guide.md)
5. [QA Audit](QA_Audit.md)
6. [Current Manuscript](Manuscript_Access.md)

## Repository areas

```text
docs/reviewer/
    Reviewer-facing documentation

docs/reports/
    Current manuscript and technical reports

docs/research-notes/
    Research and development notes

src/locked_saturation/
    Core Locked Saturation implementation

scripts/
    Reproduction and analysis scripts

results/diagnostics/
    Generated diagnostic outputs

notebooks/
    Jupyter notebooks

.github/workflows/
    Automated validation workflows
```

The repository root also contains CAMB/Fortran source and supporting build infrastructure used in the cosmological implementation.

Upstream scientific software should be distinguished from model-specific modifications, tests, documentation, and results.

---

**[Open the formatted Reviewer Roadmap PDF](Reviewer_Roadmap.pdf?raw=1)**

[Back to main repository](../../README.md)

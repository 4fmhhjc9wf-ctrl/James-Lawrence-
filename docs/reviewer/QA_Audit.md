# QA Audit

This is the browser-readable entry point for quality assurance and validation material.

## What QA can establish

Repository QA can check whether:

- required files are present;
- source code parses and builds;
- specified tests run successfully;
- numerical calculations are internally reproducible;
- generated outputs correspond to the checked-in implementation;
- build and test workflows remain functional.

## What QA cannot establish by itself

Successful internal validation does not establish that the physical interpretation is unique or correct.

Independent scientific evaluation still requires observational comparison, statistical model comparison, theoretical consistency checks, independent numerical implementations, and attempts at falsification.

## Active validation structure

The repository identifies three principal workflow roles:

```text
python-tests.yml
    Routine Python validation

full-fortran-build.yml
    Deeper Fortran/CAMB build validation

authoritative-repository-cleanup-v7.yml
    Manual maintenance and deep-validation workflow
```

Repository-maintenance workflows should not be mistaken for components of the physical theory.

---

**[Open the formatted QA Audit PDF](QA_Audit.pdf?raw=1)**

[Back to main repository](../../README.md)

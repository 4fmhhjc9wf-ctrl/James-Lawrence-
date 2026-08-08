# Independent Reviewer Guide

This page provides a browser-readable starting point for independent evaluation of Locked Saturation Cosmology.

## What a reviewer should check

A useful independent review should distinguish among:

1. the equations;
2. the implementation of those equations;
3. the numerical results produced by that implementation; and
4. the physical interpretation assigned to those results.

Reviewers are encouraged to identify the specific equation, assumption, parameter, dataset, numerical method, implementation choice, statistical comparison, or reported result being challenged.

## Priority questions

An independent reviewer should determine whether:

- the checked-in code corresponds to the equations stated in the documentation;
- the locked arithmetic tests reproduce;
- the primary model tests reproduce;
- the galaxy-scale calculations can be regenerated;
- the cosmological calculations can be regenerated;
- the CAMB/Fortran implementation builds and behaves as documented;
- the results survive reasonable robustness tests;
- an independently written implementation produces compatible results;
- the framework makes distinguishable or falsifiable predictions.

Internal computational checks are evidence about the implementation, not independent proof of the physical theory.

A failed reproduction is scientifically useful and should be documented rather than hidden.

---

**[Open the formatted Independent Reviewer Guide PDF](Independent_Reviewer_Guide.pdf?raw=1)**

[Back to main repository](../../README.md)

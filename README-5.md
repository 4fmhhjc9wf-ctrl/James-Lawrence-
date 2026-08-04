# Locked Gravitational Saturation Cosmology

**Author:** James Lawrence  
**Affiliation:** Independent Researcher, Florida, United States  
**Current release:** Version 1.1 review copy (August 3, 2026)

## Recovered original computational workflow

The repository now includes the surviving original modified CAMB source, locked background include table, final spectra, diagnostics, and Planck-lensing workflow under `original_workflow/`. See [`RECOVERED_WORKFLOW_QUICKSTART.md`](RECOVERED_WORKFLOW_QUICKSTART.md). These recovered files supersede the earlier statement that the original executable workflow was unavailable.


## Overview

This repository accompanies the technical manuscript:

> *Locked Gravitational Saturation Cosmology: A Nonsingular Bounce, Canonical Organizational Fields, and a Locked Expansion History*

The work presents an **effective cosmological model** in which a high-density saturation response produces a finite-density bounce and canonical organizational fields approach a late residual state. The expanding branch is used to calculate background, acoustic, growth, CMB, and lensing observables.

This repository is being released to support independent technical review, criticism, and reproduction attempts. It does **not** claim that the model has been independently verified, accepted by a journal, or uniquely derived from a fundamental microscopic theory.

## Manuscript

The complete review copy is located at:

- [`manuscript/Locked_Saturation_Cosmology_v1.1_Review_Copy.pdf`](manuscript/Locked_Saturation_Cosmology_v1.1_Review_Copy.pdf)

The deposited PDF includes a copyright notice and a Version 1.1 clarification notice. Its SHA-256 digest is recorded in [`manuscript/SHA256.txt`](manuscript/SHA256.txt).

## Principal reported results

The manuscript reports, from one locked expansion history:

| Quantity | Reported value |
|---|---:|
| Acoustic scale, `100 theta*` | `1.041033` |
| Drag sound horizon, `r_drag` | `149.960 Mpc` |
| Growth amplitude, `sigma8` | `0.779680` |
| Weak-lensing combination, `S8` | `0.79781` |
| Planck 2018 lensing statistic | `chi-square = 10.7379` for 9 bins |
| Lensing p-value | `0.294` |

These are author-reported outputs pending independent reproduction.

## Start here

- [Executive Summary](docs/Executive_Summary.pdf)
- [Technical Synopsis](docs/Technical_Synopsis.pdf)
- [Reviewer Roadmap](docs/Reviewer_Roadmap.pdf)
- [Independent Reviewer Guide](docs/Independent_Reviewer_Guide.pdf)
- [QA Audit](docs/QA_Audit.pdf)
- [Reproduction Guide](reproduction/Reproduction_Guide.pdf)

## Executable reference implementation

The repository now includes a tested Python transcription of the effective background equations documented in Appendices A and B. It provides:

- the canonical two-field potential and derivatives;
- the contraction-only transfer term;
- matter, radiation, and field evolution equations;
- the modified Friedmann derivative equation and constraint diagnostic;
- demonstrative bounce integrations using both DOP853 and Radau;
- regression tests for several arithmetic relations reported in the manuscript.

Run:

```bash
pip install -r requirements.txt
pip install -e .
pytest -q
python scripts/run_reference_reproduction.py
```

This is a reference reconstruction, not a recovered copy of the original calculation. Exact reproduction of the final CAMB, BAO, growth, and lensing outputs remains blocked by numerical inputs and source artifacts that are not present in the manuscript or conversation archive. The missing items are documented explicitly in [`REPRODUCIBILITY_STATUS.md`](REPRODUCIBILITY_STATUS.md).

## Requested review

Independent reviewers are invited to examine:

1. Mathematical consistency and conservation.
2. Regularity and limiting behavior at the bounce.
3. The relationship between the canonical field action and the imposed effective high-density constraint.
4. Background integration and locked-history construction.
5. Perturbation and Boltzmann implementation.
6. Numerical reproducibility.
7. Statistical interpretation of the observational comparisons.
8. Scope and wording of stability and phenomenological claims.

Issues may be submitted using the repository's issue templates.

## Citation

Please use the metadata in [`CITATION.cff`](CITATION.cff), or cite:

> Lawrence, James. *Locked Gravitational Saturation Cosmology: A Nonsingular Bounce, Canonical Organizational Fields, and a Locked Expansion History*. Version 1.1, 2026.

## Copyright and use

Copyright © 2026 James Lawrence. The manuscript text, figures, tables, and original presentation are protected by copyright. Permission is granted for downloading, reading, scholarly review, criticism, citation, and fair use. No permission is granted to republish the manuscript in full, sell copies, or misrepresent authorship.

Scientific ideas, equations, methods, and factual results are not made proprietary by this notice. See [`LICENSE.md`](LICENSE.md).

## AI and computational assistance disclosure

Computational intelligence was used under the author's direction to assist with mathematical formalization, numerical development, drafting, organization, and quality assurance. The author retains responsibility for the hypothesis, interpretation, claims, deposited materials, and responses to review.

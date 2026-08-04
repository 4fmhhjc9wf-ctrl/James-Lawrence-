# Executable reference code

This repository contains the reference implementation and supporting data for "Locked Saturation Cosmology".

Quickstart (developer-friendly)

1. Create and activate a virtualenv (recommended):

   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .\.venv\Scripts\activate  # Windows (PowerShell)

2. Install the package and test dependencies:

   pip install -e .
   pip install -r requirements.txt

3. Run the test suite:

   pytest -q

4. Run the reference reproduction script (small example):

   python run_reference_reproduction.py

Helpful docs and notes

- Reproducibility & running instructions: REPRODUCTION.md and REPRODUCIBILITY_STATUS.md
- Large data files and PDFs are present in this repository for reproducibility; they are not removed by this change. New large files are ignored via .gitignore.
- Fortran sources (.f90) and Python bindings live at the repository root. There are several legacy README and documentation files — see docs/ARCHIVE.md (added in the PR) for where legacy content will be kept.

If you need me to:
- Add CI to compile Fortran sources, say so (Fortran compilation in CI can be slow and may need tuning).
- Remove or move large binary files to Git LFS or releases (this rewrites history and requires explicit approval).


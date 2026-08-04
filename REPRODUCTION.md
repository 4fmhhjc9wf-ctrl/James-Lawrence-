# Running the reference reconstruction

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
pytest -q
python scripts/run_reference_reproduction.py
```

Outputs are written to `outputs/demo/`.

## Interpretation

Passing tests means the source transcription, basic conservation structure, solver execution, and locked arithmetic checks work as documented. It does not mean the final CAMB spectra have been reproduced. Exact reproduction requires the missing numerical inputs and original CAMB modification files listed in `REPRODUCIBILITY_STATUS.md`.

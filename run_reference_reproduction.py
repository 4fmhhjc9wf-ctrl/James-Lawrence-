from pathlib import Path
import json
from locked_saturation.simulation import write_run
from locked_saturation.validation import locked_arithmetic
out=Path('outputs/demo'); out.mkdir(parents=True,exist_ok=True)
results={'locked_arithmetic':locked_arithmetic(),'runs':[]}
for method in ('DOP853','Radau'):
    results['runs'].append(write_run(out,method))
(out/'reference_reproduction_summary.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))

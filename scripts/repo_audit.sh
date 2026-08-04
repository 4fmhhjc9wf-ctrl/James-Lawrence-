#!/usr/bin/env bash
# Simple repository audit script — non-destructive
# Outputs:
#  - todo_fixme.txt : list of TODO/FIXME occurrences
#  - large_files.txt : list of tracked files > 5MB
#  - py_syntax_errors.txt : python files that fail compilation
#  - fortran_sources.txt : list of Fortran source files

set -euo pipefail
out_dir="repo_audit_output"
mkdir -p "$out_dir"

echo "Scanning for TODO/FIXME..."
git grep -nE "TODO|FIXME" -- . || true > "$out_dir/todo_fixme.txt"

echo "Listing tracked files larger than 5MB..."
# Use git ls-files to restrict to tracked files
python - <<'PY'
import subprocess,sys
files = subprocess.check_output(['git','ls-files']).decode().splitlines()
large = []
import os
for f in files:
    try:
        sz = os.path.getsize(f)
    except OSError:
        continue
    if sz > 5*1024*1024:
        large.append((f, sz))
for f,sz in sorted(large, key=lambda x: x[1], reverse=True):
    print(f"{sz}\t{f}")
PY
> "$out_dir/large_files.txt"

echo "Checking Python syntax for all tracked .py files..."
python - <<'PY'
import subprocess,sys
files = subprocess.check_output(['git','ls-files','*.py']).decode().splitlines()
errors = []
for f in files:
    try:
        subprocess.check_output([sys.executable,'-m','py_compile',f], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        errors.append((f, e.output.decode()))
for f, out in errors:
    print('---', f)
    print(out)
    print()
if not errors:
    print('No python syntax errors found.')
PY
> "$out_dir/py_syntax_errors.txt"

echo "Listing Fortran source files (extensions .f .f90 .f95)..."
git ls-files | grep -E "\.(f|f90|f95)$" || true > "$out_dir/fortran_sources.txt"

echo "Audit complete. Output directory: $out_dir"
ls -lh "$out_dir" || true

exit 0

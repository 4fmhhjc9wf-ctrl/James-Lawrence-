from pathlib import Path
import argparse,json
from .simulation import write_run
from .validation import locked_arithmetic

def main():
 p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='cmd',required=True)
 r=sub.add_parser('demo-background'); r.add_argument('--out',default='outputs/demo'); r.add_argument('--method',choices=['DOP853','Radau'],default='DOP853')
 sub.add_parser('validate-locked-arithmetic')
 a=p.parse_args()
 if a.cmd=='demo-background': print(json.dumps(write_run(Path(a.out),a.method),indent=2))
 else: print(json.dumps(locked_arithmetic(),indent=2))

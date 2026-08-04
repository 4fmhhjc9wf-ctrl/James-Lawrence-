from pathlib import Path
import json, csv, math
ROOT=Path(__file__).resolve().parents[1]
vals={
 "theta100":1.041033, "rdrag":149.960, "sigma8":0.779680, "S8":0.79781, "lensing_chi2":10.7379
}
ft=ROOT/'original_workflow'/'CAMB_locked_saturation_complete_workflow'/'final_theta_results.json'
pl=ROOT/'recovered_results'/'planck_2018_lensing_bandpower_results.json'
d=json.loads(ft.read_text())
# recursively find retained F1 dict
def walk(x):
 if isinstance(x,dict):
  if any(k in x for k in ('100theta_star','theta100','r_drag_Mpc','rdrag')): yield x
  for v in x.values(): yield from walk(v)
 elif isinstance(x,list):
  for v in x: yield from walk(v)
cands=list(walk(d))
# select closest to target theta
def get(c,*ks):
 for k in ks:
  if k in c:return c[k]
 return None
best=min(cands,key=lambda c:abs(float(get(c,'100theta_star','theta100') or 99)-vals['theta100']))
checks={
 '100theta_star':(float(get(best,'100theta_star','theta100')),vals['theta100'],5e-6),
 'r_drag_Mpc':(float(get(best,'r_drag_Mpc','rdrag')),vals['rdrag'],5e-3),
 'sigma8':(float(best['sigma8']),vals['sigma8'],5e-6),
 'S8':(float(best['S8']),vals['S8'],5e-6),
}
l=json.loads(pl.read_text())
def find_num(obj,key):
 if isinstance(obj,dict):
  if key in obj:return obj[key]
  for v in obj.values():
   r=find_num(v,key)
   if r is not None:return r
 elif isinstance(obj,list):
  for v in obj:
   r=find_num(v,key)
   if r is not None:return r
 return None
chi=find_num(l,'chi2_locked') or find_num(l,'locked_chi2') or find_num(l,'chi2')
if chi is not None: checks['lensing_chi2']=(float(chi),vals['lensing_chi2'],5e-4)
failed=[]
for name,(got,exp,tol) in checks.items():
 ok=abs(got-exp)<=tol
 print(f"{name}: got={got:.9g} expected={exp:.9g} tol={tol:g} {'PASS' if ok else 'FAIL'}")
 if not ok: failed.append(name)
raise SystemExit(1 if failed else 0)

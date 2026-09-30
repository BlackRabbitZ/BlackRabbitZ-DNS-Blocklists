#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
META=ROOT/'metadata'/'domain-classification.csv'; STATE=ROOT/'metadata'/'classifier-state.json'; Q=ROOT/'review'/'classifier-quarantine.tsv'; C=ROOT/'sources'/'classified'
def main():
 errors=[]
 if not META.exists():errors.append('metadata/domain-classification.csv missing')
 if not STATE.exists():errors.append('metadata/classifier-state.json missing')
 if not C.exists():errors.append('sources/classified missing')
 privacy=defaultdict(list)
 if META.exists():
  with META.open(encoding='utf-8') as f:
   for r in csv.DictReader(f):
    if r['status']=='accepted':privacy[r['domain']].append(r['category'])
  dup={d:cats for d,cats in privacy.items() if len(set(cats))>1}
  if dup:errors.append(f'{len(dup)} privacy domains have more than one canonical category (example {next(iter(dup.items()))})')
 if STATE.exists():
  try:json.loads(STATE.read_text())
  except Exception as e:errors.append(f'classifier-state invalid JSON: {e}')
 for p in C.glob('*/*.txt') if C.exists() else []:
  lines=[x.strip() for x in p.read_text(encoding='utf-8',errors='ignore').splitlines() if x.strip() and not x.startswith('#')]
  if lines!=sorted(set(lines)):errors.append(f'{p.relative_to(ROOT)} not sorted/unique')
 if errors:
  print('CLASSIFIER VALIDATION FAILED',file=sys.stderr)
  for e in errors:print(' -',e,file=sys.stderr)
  return 1
 print('Classifier validation OK: canonical privacy ownership, state and classified caches are consistent.')
 return 0
if __name__=='__main__':raise SystemExit(main())

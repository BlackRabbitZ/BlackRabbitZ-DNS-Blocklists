#!/usr/bin/env python3
"""Audit existing manually curated privacy lists without changing them."""
from __future__ import annotations
import csv,json
from pathlib import Path
from classifier import Evidence,classify,load_rules
ROOT=Path(__file__).resolve().parents[1]; MANUAL=ROOT/'sources'/'manual'; OUT=ROOT/'review'/'manual-classification-audit.csv'
def domains(p):
 out=[]
 for line in p.read_text(encoding='utf-8',errors='ignore').splitlines():
  s=line.strip().lower().rstrip('.')
  if s and not s.startswith(('#','!')) and '.' in s:out.append(s.split()[0])
 return out
def main():
 rules=load_rules(); privacy=set(rules['privacy_categories']); rows=[]
 for p in sorted(MANUAL.glob('*.txt')):
  if p.stem not in privacy:continue
  for d in domains(p):
   dec=classify(d,[Evidence(p.stem,'manual-existing','','direct')],rules)
   if dec.status!='accepted' or dec.category!=p.stem:
    rows.append((d,p.stem,dec.category or '',dec.status,dec.confidence,dec.reason))
 OUT.parent.mkdir(parents=True,exist_ok=True)
 with OUT.open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(['domain','current_category','suggested_category','status','confidence','reason']);w.writerows(rows)
 print(f'Manual audit: {len(rows):,} entries need review. No manual list was modified.')
 return 0
if __name__=='__main__':raise SystemExit(main())

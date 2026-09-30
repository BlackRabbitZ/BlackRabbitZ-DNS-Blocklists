#!/usr/bin/env python3
"""Deterministically build public categories from manual + classified upstream data."""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CATEGORY_DIR=ROOT/'lists'/'categories'; MANUAL_DIR=ROOT/'sources'/'manual'; CLASSIFIED_DIR=ROOT/'sources'/'classified'
CONFIG=ROOT/'scripts'/'upstream-sources.json'; ALLOWLIST=ROOT/'config'/'allowlist.txt'; CRITICAL=ROOT/'config'/'critical-services.txt'; STATE=ROOT/'metadata'/'classifier-state.json'
DOMAIN_RE=re.compile(r'^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$',re.I)
TRACKER_SPECIALISED={'telemetry','social-trackers','mobile-tracking','affiliate-tracking','consent-cmp','windows-telemetry','apple-telemetry','android-telemetry','linux-telemetry','nas-telemetry','server-telemetry','native-tracking','smart-tv','iot','gaming-telemetry'}
TELEMETRY_SPECIALISED={'mobile-tracking','windows-telemetry','apple-telemetry','android-telemetry','linux-telemetry','nas-telemetry','server-telemetry','smart-tv','iot','gaming-telemetry'}
def extract(line:str)->str|None:
 d=line.strip().lower().rstrip('.')
 if not d or d.startswith(('#','!','@@')):return None
 if d.startswith('||') and '^' in d:d=d[2:].split('^',1)[0]
 if ' #' in d:d=d.split(' #',1)[0].strip()
 if d.startswith('*.'):d=d[2:]
 d=d.split()[0] if d.split() else ''
 return d if DOMAIN_RE.fullmatch(d) else None
def read(p:Path)->set[str]: return {x for line in p.read_text(encoding='utf-8',errors='ignore').splitlines() if (x:=extract(line))} if p.exists() else set()
def protected(d:str,roots:set[str])->bool:return any(d==r or d.endswith('.'+r) for r in roots)
def collect(cat:str)->set[str]:
 s=read(MANUAL_DIR/f'{cat}.txt'); folder=CLASSIFIED_DIR/cat
 if folder.exists():
  for p in sorted(folder.glob('*.txt')):s.update(read(p))
 return s
def header(path:Path,cat:str,count:int)->list[str]:
 old=path.read_text(encoding='utf-8',errors='ignore').splitlines() if path.exists() else [];out=[]
 for line in old:
  if line.strip()=='' or line.startswith('#'):
   if line.startswith('# Entries:'):line=f'# Entries: {count}'
   if not line.startswith('# Auto-updated:'):out.append(line)
   continue
  break
 if not out:out=['# BlackRabbitZ DNS Blocklists',f'# Category: {cat}','# Author: BlackRabbitZ','# Repository: https://github.com/BlackRabbitZ/BlackRabbitZ-DNS-Blocklists','# License: GPL-3.0-only for project-original material; third-party notices: THIRD_PARTY.md',f'# Entries: {count}']
 if not any(x.startswith('# Entries:') for x in out):out.append(f'# Entries: {count}')
 while out and out[-1]=='':out.pop()
 return out
def main()->int:
 if not STATE.exists() or not CLASSIFIED_DIR.exists():
  print('ERROR: classifier output missing. Run scripts/classify-upstreams.py first.')
  return 2
 cfg=json.loads(CONFIG.read_text(encoding='utf-8'));cats={p.stem for p in MANUAL_DIR.glob('*.txt')}|set(cfg.get('categories',{}))|{p.name for p in CLASSIFIED_DIR.iterdir() if p.is_dir()}
 allow=read(ALLOWLIST);critical=read(CRITICAL);sets={c:collect(c) for c in sorted(cats)}
 for c in sets:sets[c]={d for d in sets[c] if not protected(d,allow)}
 for c,settings in cfg.get('categories',{}).items():
  if settings.get('protect_critical',False) and c in sets:sets[c]={d for d in sets[c] if not protected(d,critical)}
 # Safety net for older manual data: broad lists must not duplicate specialised privacy/device lists.
 specialised=set().union(*(sets.get(c,set()) for c in TRACKER_SPECIALISED))
 if 'trackers' in sets:sets['trackers'].difference_update(specialised)
 st=set().union(*(sets.get(c,set()) for c in TELEMETRY_SPECIALISED))
 if 'telemetry' in sets:sets['telemetry'].difference_update(st)
 for c,domains in sets.items():
  p=CATEGORY_DIR/f'{c}.txt';p.parent.mkdir(parents=True,exist_ok=True);h=header(p,c,len(domains));p.write_text('\n'.join(h+['',*sorted(domains)])+'\n',encoding='utf-8',newline='\n')
 print(f'Built {len(sets)} category lists from manual + classified upstream data.')
 return 0
if __name__=='__main__':raise SystemExit(main())

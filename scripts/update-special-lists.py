#!/usr/bin/env python3
"""Manueller Updater fuer optionale Speziallisten.

WICHTIG: Dieses Script wird von keinem GitHub-Workflow automatisch ausgefuehrt.
Es veraendert nur die explizit ausgewaehlten Ziel-Dateien.

Beispiele:
  python scripts/update-special-lists.py --list
  python scripts/update-special-lists.py hagezi_dynamic_dns hagezi_badware_hoster
  python scripts/update-special-lists.py --all --dry-run
"""
from pathlib import Path
import argparse, ipaddress, json, re, urllib.request
ROOT=Path(__file__).resolve().parents[1]
CFG=json.loads((ROOT/'config/special-upstreams.json').read_text(encoding='utf-8'))
DOMAIN=re.compile(r'^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$',re.I)

def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'BlackRabbitZ-DNS-Blocklists/manual-updater'})
    with urllib.request.urlopen(req,timeout=120) as r: return r.read().decode('utf-8','replace')

def parse(text,fmt):
    out=set()
    if fmt=='misp_json':
        obj=json.loads(text); vals=obj.get('list',[])
    else: vals=text.splitlines()
    for raw in vals:
        s=str(raw).strip()
        if not s or s.startswith(('#','!','[')): continue
        if fmt=='hosts':
            p=s.split(); s=p[-1] if len(p)>1 else p[0]
        elif fmt=='ips':
            try: out.add(str(ipaddress.ip_network(s,strict=False))); continue
            except ValueError: continue
        s=s.lower().rstrip('.')
        if DOMAIN.match(s): out.add(s)
    return sorted(out)

def write(target,items,meta,dry):
    p=ROOT/target
    if dry:
        print(f'[DRY] {target}: {len(items):,} Eintraege <- {meta["url"]}')
        return
    p.parent.mkdir(parents=True,exist_ok=True)
    prefix='#' if meta['format']!='ips' else '#'
    head=[
      '# BlackRabbitZ DNS Blocklists - manuell aktualisierte Spezialliste',
      f'# Upstream: {meta["url"]}', f'# Upstream license: {meta.get("license","siehe Upstream")}',
      f'# Entries: {len(items)}', '# Update mode: manual; kein automatischer Workflow', '#'
    ]
    p.write_text('\n'.join(head+items)+'\n',encoding='utf-8')
    print(f'OK {target}: {len(items):,}')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('names',nargs='*'); ap.add_argument('--all',action='store_true'); ap.add_argument('--list',action='store_true'); ap.add_argument('--dry-run',action='store_true')
    a=ap.parse_args()
    if a.list:
        for n,m in CFG.items(): print(f'{n:34} -> {m["target"]}')
        return
    names=list(CFG) if a.all else a.names
    if not names: ap.error('Mindestens eine Liste angeben oder --all verwenden.')
    for n in names:
        if n not in CFG: print('UNBEKANNT:',n); continue
        m=CFG[n]
        try: items=parse(fetch(m['url']),m['format']); write(m['target'],items,m,a.dry_run)
        except Exception as e: print(f'FEHLER {n}: {e}')
if __name__=='__main__': main()

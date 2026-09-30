#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, os, re, shutil, tempfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from classifier import Evidence, classify, load_rules

ROOT=Path(__file__).resolve().parents[1]
UPSTREAM=ROOT/'sources'/'upstream'
CLASSIFIED=ROOT/'sources'/'classified'
CONFIG=ROOT/'scripts'/'upstream-sources.json'
META=ROOT/'metadata'
REVIEW=ROOT/'review'
DOMAIN_RE=re.compile(r'^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9_-]{0,61}[a-z0-9])?$',re.I)

def extract(line:str)->str|None:
    s=line.strip().lower().rstrip('.')
    if not s or s.startswith(('#','!','@@')): return None
    if s.startswith('||') and '^' in s: s=s[2:].split('^',1)[0]
    if ' #' in s: s=s.split(' #',1)[0].strip()
    if s.startswith('*.'): s=s[2:]
    s=s.split()[0] if s.split() else ''
    return s if DOMAIN_RE.fullmatch(s) else None

def read(path:Path)->set[str]:
    if not path.exists(): return set()
    return {d for line in path.read_text(encoding='utf-8',errors='ignore').splitlines() if (d:=extract(line))}

def slug(source:dict)->str:
    name=re.sub(r'[^a-z0-9]+','-',str(source.get('name','source')).lower()).strip('-')[:56] or 'source'
    digest=hashlib.sha256(str(source.get('url','')).encode()).hexdigest()[:8]
    return f'{name}-{digest}'

def source_map(config:dict)->dict[tuple[str,str],dict]:
    out={}
    for cat,settings in config.get('categories',{}).items():
        for src in settings.get('sources',[]): out[(cat,slug(src))]=src
    return out

def main()->int:
    config=json.loads(CONFIG.read_text(encoding='utf-8'))
    rules=load_rules(); privacy=set(rules['privacy_categories'])
    smap=source_map(config)
    evidence_by_domain=defaultdict(list)
    source_domains=defaultdict(set)
    passthrough=defaultdict(set)
    origins=defaultdict(set)

    for path in sorted(UPSTREAM.glob('*/*.txt')):
        origin=path.parent.name; sid=path.stem; src=smap.get((origin,sid),{})
        ev=Evidence(origin,str(src.get('name',sid)),str(src.get('url','')),str(src.get('trust','direct')))
        for domain in read(path):
            origins[domain].add(origin)
            if origin in privacy:
                evidence_by_domain[domain].append(ev)
            else:
                passthrough[origin].add(domain)

    tmp=Path(tempfile.mkdtemp(prefix='classified-',dir=str(ROOT/'sources')))
    rows=[]; qrows=[]; counts=defaultdict(int)
    try:
        # Non-privacy/security/content categories remain independent and may overlap by design.
        for cat,domains in passthrough.items():
            p=tmp/cat/'passthrough.txt'; p.parent.mkdir(parents=True,exist_ok=True)
            p.write_text('\n'.join(sorted(domains))+'\n',encoding='utf-8')
            counts[cat]+=len(domains)
            for d in domains: rows.append((d,cat,100,'passthrough','non-privacy category',','.join(sorted(origins[d]))))

        for domain,evidences in sorted(evidence_by_domain.items()):
            dec=classify(domain,evidences,rules)
            origin_text=','.join(sorted({e.category for e in evidences}))
            if dec.status=='accepted' and dec.category:
                # One canonical privacy category per domain.
                p=tmp/dec.category/'classified.txt'; p.parent.mkdir(parents=True,exist_ok=True)
                source_domains[(dec.category,'classified')].add(domain)
                counts[dec.category]+=1
            else:
                qrows.append((domain,dec.status,str(dec.confidence),dec.reason,origin_text,dec.vendor,dec.function))
            rows.append((domain,dec.category or '',dec.confidence,dec.status,dec.reason,origin_text))

        for (cat,_),domains in source_domains.items():
            p=tmp/cat/'classified.txt'; p.parent.mkdir(parents=True,exist_ok=True)
            p.write_text('\n'.join(sorted(domains))+'\n',encoding='utf-8')

        # Transactional replacement.
        backup=CLASSIFIED.with_name('classified.previous')
        if backup.exists(): shutil.rmtree(backup)
        if CLASSIFIED.exists(): CLASSIFIED.rename(backup)
        tmp.rename(CLASSIFIED)
        if backup.exists(): shutil.rmtree(backup)

        META.mkdir(parents=True,exist_ok=True)
        with (META/'domain-classification.csv').open('w',newline='',encoding='utf-8') as f:
            w=csv.writer(f); w.writerow(['domain','category','confidence','status','reason','origin_categories']); w.writerows(rows)
        REVIEW.mkdir(parents=True,exist_ok=True)
        with (REVIEW/'classifier-quarantine.tsv').open('w',encoding='utf-8',newline='') as f:
            f.write('domain\tstatus\tconfidence\treason\torigin_categories\tvendor\tfunction\n')
            for r in qrows: f.write('\t'.join(map(str,r))+'\n')
        state={'generated_at':datetime.now(timezone.utc).isoformat(),'classified_domains':sum(counts.values()),'quarantined':len(qrows),'categories':dict(sorted(counts.items()))}
        (META/'classifier-state.json').write_text(json.dumps(state,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        print(f"Classifier OK: {sum(counts.values()):,} classified/passthrough entries, {len(qrows):,} quarantine rows.")
        for cat,n in sorted(counts.items()): print(f"  {cat:24s} {n:>9,}")
        return 0
    except Exception:
        if tmp.exists(): shutil.rmtree(tmp,ignore_errors=True)
        raise
if __name__=='__main__': raise SystemExit(main())

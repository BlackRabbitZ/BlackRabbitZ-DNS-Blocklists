from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
DOMAIN=re.compile(r'^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$',re.I)
errors=[]

def domains(path):
    with path.open('r',encoding='utf-8',errors='ignore') as f:
        for line in f:
            s=line.strip().lower().rstrip('.')
            if s and not s.startswith('#'):
                yield s

def check_sorted_domain_file(path):
    prev=None
    for i,s in enumerate(domains(path),1):
        if not DOMAIN.match(s):
            errors.append(f'{path.relative_to(ROOT)}: ungültige Domain: {s}')
            if len(errors)>100: return
        if prev is not None and s <= prev:
            errors.append(f'{path.relative_to(ROOT)}: nicht strikt sortiert/dupliziert: {s}')
            if len(errors)>100: return
        prev=s

def is_subset(a,b):
    ia=iter(domains(a)); ib=iter(domains(b))
    try: x=next(ia)
    except StopIteration: return True
    try: y=next(ib)
    except StopIteration: return False
    while True:
        if x==y:
            try: x=next(ia)
            except StopIteration: return True
            try: y=next(ib)
            except StopIteration: return False
        elif x>y:
            try: y=next(ib)
            except StopIteration: return False
        else:
            return False

for p in ROOT.rglob('*.txt'):
    if p.name=='approved-sites.txt' or '_base' in p.parts: continue
    check_sorted_domain_file(p)
    if len(errors)>100: break

for p in ROOT.rglob('*'):
    if p.is_file() and re.search(r'(?:^|[-_])part[-_]?\d+',p.name,re.I):
        errors.append(f'Part-Datei verboten: {p.relative_to(ROOT)}')

levels=['light','normal','pro','pro-plus','ultimate']
for main in ROOT.rglob('main'):
    if main.is_dir() and all((main/f'{x}.txt').exists() for x in levels):
        for n1,n2 in zip(levels,levels[1:]):
            if not is_subset(main/f'{n1}.txt',main/f'{n2}.txt'):
                errors.append(f'Nicht kumulativ: {main.relative_to(ROOT)}/{n1} !⊂ {n2}')

pdir=ROOT/'profiles'
for n1,n2 in zip(levels,levels[1:]):
    if not is_subset(pdir/f'{n1}.txt',pdir/f'{n2}.txt'):
        errors.append(f'Globale Profile nicht kumulativ: {n1} !⊂ {n2}')

if errors:
    print('\n'.join(errors[:200])); print(f'FEHLER: {len(errors)}'); sys.exit(1)
print('OK: Domainformat, Sortierung/Duplikate, keine Part-Dateien und kumulative Profile geprüft.')

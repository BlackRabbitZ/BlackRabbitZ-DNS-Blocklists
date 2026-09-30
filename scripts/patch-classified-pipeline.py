#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPDATER = ROOT / 'scripts' / 'update-upstreams.py'
BUILDER = ROOT / 'scripts' / 'build-categories.py'
WORKFLOW = ROOT / '.github' / 'workflows' / 'daily-upstream-update.yml'


def fail(msg: str) -> int:
    print(f'ERROR: {msg}')
    return 2


def main() -> int:
    for p in (UPDATER, BUILDER, WORKFLOW):
        if not p.exists():
            return fail(f'missing required file: {p.relative_to(ROOT)}')

    updater = UPDATER.read_text(encoding='utf-8')
    original = updater

    # update-upstreams.py must only refresh raw per-source caches. Public lists are
    # built AFTER classification by the workflow.
    call_variants = [
        '''    if not args.dry_run:\n        subprocess.run([sys.executable, str(ROOT / "scripts" / "build-categories.py")], check=True)\n\n''',
        '''    if not args.dry_run:\n        subprocess.run([sys.executable, str(ROOT / 'scripts' / 'build-categories.py')], check=True)\n\n''',
    ]
    removed = False
    for block in call_variants:
        if block in updater:
            updater = updater.replace(block, '', 1)
            removed = True
            break

    # Remove subprocess import only if it is no longer used.
    if 'subprocess.' not in updater:
        updater = updater.replace('import subprocess\n', '')

    # Keep the updater documentation truthful.
    updater = updater.replace(
        '- lists/categories/*.txt are deterministic generated unions of manual + caches.',
        '- updater writes only raw per-source caches; public lists are built later from manual + classified data.',
    )

    if 'build-categories.py' in updater and 'subprocess.run' in updater:
        return fail('update-upstreams.py still invokes build-categories.py; refusing partial patch')

    if updater != original:
        UPDATER.write_text(updater, encoding='utf-8', newline='\n')
        print('PATCHED: scripts/update-upstreams.py now refreshes raw caches only.')
    elif removed:
        print('OK: updater call removed.')
    else:
        print('OK: no premature public-list build found in updater.')

    builder = BUILDER.read_text(encoding='utf-8')
    required_builder = ["CLASSIFIED_DIR", "MANUAL_DIR", "folder=CLASSIFIED_DIR/cat"]
    missing = [x for x in required_builder if x not in builder]
    if missing:
        return fail('build-categories.py is not the classified-data builder; missing: ' + ', '.join(missing))
    if "UPSTREAM_DIR" in builder:
        return fail('build-categories.py still references UPSTREAM_DIR; public lists must not consume raw caches directly')

    wf = WORKFLOW.read_text(encoding='utf-8')
    markers = [
        'python3 ./scripts/update-upstreams.py',
        'python3 ./scripts/classify-upstreams.py',
        'python3 ./scripts/validate-classifier.py',
        'python3 ./scripts/build-categories.py',
    ]
    positions = [wf.find(x) for x in markers]
    if any(p < 0 for p in positions):
        return fail('daily workflow is missing one or more required pipeline stages')
    if positions != sorted(positions):
        return fail('daily workflow order is wrong; expected updater -> classifier -> validation -> builder')

    print('OK: classified pipeline contract verified.')
    print('     upstream -> classifier -> sources/classified -> public categories')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

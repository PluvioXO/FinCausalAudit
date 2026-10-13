#!/usr/bin/env python3
"""Check code/data against package checksums."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parents[1]
entries=json.loads((root/'manifest.json').read_text())['files']
bad=[]
for e in entries:
 p=root/e['path']
 if not p.exists():bad.append((e['path'],'MISSING'));continue
 h=hashlib.sha256(p.read_bytes()).hexdigest()
 if h!=e['sha256']:bad.append((e['path'],'SHA256 MISMATCH'))
print(f'Checked {len(entries)} files; issues: {len(bad)}')
for item in bad:print(*item)
sys.exit(1 if bad else 0)

from __future__ import annotations
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
DIRS = ["adapters","config","contracts","core","skills","tools","tests","verification"]
errors = []
for item in REQUIRED:
    if not (ROOT/item).is_file(): errors.append(f"missing file: {item}")
for item in DIRS:
    if not (ROOT/item).is_dir(): errors.append(f"missing directory: {item}")
text = (ROOT/"EXPLAINABILITY.md").read_text(encoding="utf-8") if (ROOT/"EXPLAINABILITY.md").exists() else ""
required = ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]
for heading in required:
    if text.count(heading) != 1: errors.append(f"required heading count != 1: {heading}")
for bad in ["## Inputs","## Decision","## Limits"]:
    if re.search(rf"^{re.escape(bad)}\s*$", text, re.M): errors.append(f"conflicting heading: {bad}")
sections = []
for heading in required:
    start = text.find(heading)
    if start >= 0:
        next_pos = text.find("\n## ", start + len(heading))
        body = text[start + len(heading): next_pos if next_pos >= 0 else len(text)].strip()
        sentences = re.findall(r"[^.!?]+[.!?]", body)
        if len(sentences) < 2: errors.append(f"section has fewer than two sentences: {heading}")
if errors:
    print("READINESS AUDIT: FAIL")
    for e in errors: print(f"- {e}")
    sys.exit(1)
print(f"READINESS AUDIT: PASS\nChecked {len(REQUIRED)} files and {len(DIRS)} directories.")

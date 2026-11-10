# SPDX-License-Identifier: MIT
# Copyright (c) 2026 David Joyner
"""Run every verification script in the repository and report pass/fail."""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SCRIPTS = sorted(p for p in ROOT.rglob("*_check.py"))

failed = []
for script in SCRIPTS:
    print("=" * 70)
    print("Running", script.relative_to(ROOT))
    print("=" * 70)
    result = subprocess.run([sys.executable, script.name], cwd=script.parent)
    if result.returncode != 0:
        failed.append(script)

print()
print("%d script(s) run, %d failed" % (len(SCRIPTS), len(failed)))
sys.exit(1 if failed else 0)

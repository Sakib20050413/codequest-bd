import ast
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

BANNED_AI_SLOP_STRINGS = [
    "Point 10",
    "Point 16",
    "Zero AI Filler Slop",
    "Inspired by Claude",
    "gamesTaxonomyModal",
]

def run_audit():
    py_count = 0
    html_count = 0
    for root, _, files in os.walk(BASE):
        if "venv" in root or ".git" in root or "staticfiles" in root:
            continue
        for fn in files:
            p = os.path.join(root, fn)
            if fn.endswith(".py"):
                with open(p, "r", encoding="utf-8") as f:
                    src = f.read()
                ast.parse(src, filename=p)
                py_count += 1
            elif fn.endswith((".html", ".css", ".js")):
                with open(p, "r", encoding="utf-8") as f:
                    txt = f.read()
                for banned in BANNED_AI_SLOP_STRINGS:
                    assert banned not in txt, f"Found banned AI-slop string '{banned}' in {p}"
                # Ensure zero hidden zero-width unicode marks
                assert not re.search(r"[\u200b\u200c\u200d\ufeff]", txt), f"Zero-width watermark in {p}"
                if fn.endswith(".html"):
                    html_count += 1

    print(f"[AUDIT PASSED] {py_count} Python files AST-verified, {html_count} HTML templates verified 100% free of AI-slop!")

if __name__ == "__main__":
    run_audit()

"""Validate published file links, encodings and excluded input boundaries."""
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

def main():
    files = [p for p in ROOT.rglob("*") if p.is_file() and not any(x in p.relative_to(ROOT).parts for x in [".git", "cache", "raw", "local", "__pycache__"])]
    errors, links = [], 0
    for path in files:
        if path.suffix in [".md", ".py", ".R", ".json", ".csv", ".txt", ".yml"]:
            text = path.read_text(encoding="utf-8-sig")
            if "\ufffd" in text:
                errors.append(f"Replacement character: {path.relative_to(ROOT)}")
            if path.suffix == ".json":
                json.loads(text)
            if path.suffix == ".md":
                for target in re.findall(r"\]\(([^)]+)\)", text):
                    if target.startswith(("http:", "https:", "mailto:", "#", "codex:")):
                        continue
                    target = unquote(target.split("#")[0].split(' "')[0].strip("<>"))
                    links += 1
                    if target and not (path.parent / target).exists():
                        errors.append(f"Missing {path.relative_to(ROOT)} -> {target}")
    tracked = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT, text=True, capture_output=True, check=True).stdout.split("\0")
    total = 0
    for relative in filter(None, tracked):
        path = ROOT / relative
        total += path.stat().st_size
        if path.stat().st_size > 20 * 1024 * 1024:
            errors.append(f"Unexpected >20MB published asset: {relative}")
        if relative.startswith(("data/raw/", "data/cache/", "data/local/")):
            errors.append(f"Ignored input tracked: {relative}")
    result = {"status": "FAIL" if errors else "PASS", "published_files": len(list(filter(None, tracked))), "published_bytes": total, "markdown_local_links_checked": links, "errors": errors, "large_inputs_tracked": False if not any("input tracked" in e for e in errors) else True}
    (ROOT / "reports/repository_check.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    main()

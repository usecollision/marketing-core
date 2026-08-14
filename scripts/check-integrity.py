#!/usr/bin/env python3
"""Marketing OS integrity watchdog.

Clones/reads all 5 domain repos via the GitHub API and checks:
1. Every SKILL.md has valid YAML frontmatter + required keys.
2. Every cross-repo related_skills ref resolves to a real skill.
3. Stale markers: hardcoded years, "as of <date>", and version strings that
   suggest platform-specific facts may have rotted.

Output contract (watchdog pattern):
- Healthy  -> prints nothing, exits 0 (silent).
- Problems -> prints a concise report to stdout, exits 0 so the scheduler
             delivers it (exit 1 = error alert; we only alert on real drift).

Run: python check-integrity.py
"""
import json, subprocess, re, base64, sys, yaml

REPOS = ["marketing-intelligence", "marketing-messaging", "marketing-channels",
         "marketing-paid", "marketing-optimize"]
ORG = "usecollision"

REQUIRED_KEYS = ["name", "category", "description", "triggers", "inputs",
                 "outputs", "related_skills", "required_context", "version"]

# stale markers: things that rot as platforms change
STALE_PATTERNS = [
    r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? 20\d{2}",  # "Aug 14, 2026"
    r"\b20\d{2}\b(?=\s+(?:Q[1-4]|update|release|rebrand|deprecat))",                    # "2026 update"
    r"as of [A-Z][a-z]+ \d{1,2},? \d{4}",                                               # "as of Aug 14, 2026"
    r"(API v[0-9]+(?:\.[0-9]+)+)",                                                       # pinned API versions
]

def gh(args):
    out = subprocess.run(["gh", "api"] + args, capture_output=True, text=True)
    return out.stdout

def main():
    have = set()
    skills = []
    for r in REPOS:
        tree = json.loads(gh([f"repos/{ORG}/{r}/git/trees/HEAD?recursive=1"]))
        for e in tree.get("tree", []):
            p = e["path"]
            if not p.endswith("SKILL.md"):
                continue
            raw = gh([f"repos/{ORG}/{r}/contents/{p}", "--jq", ".content"])
            text = base64.b64decode(raw).decode("utf-8", "replace")
            skills.append((r, p, text))
            have.add((r, p.split("/")[0]))

    problems = []
    for r, p, text in skills:
        fm = re.match(r"^---\n(.*?)\n---", text, re.S)
        if not fm:
            problems.append(f"[yaml] {r}/{p}: no frontmatter")
            continue
        try:
            d = yaml.safe_load(fm.group(1))
            for k in REQUIRED_KEYS:
                if k not in d:
                    problems.append(f"[missing-key] {r}/{p}: {k}")
            if ": " in d.get("description", ""):
                problems.append(f"[desc-colon] {r}/{p}")
        except Exception as ex:
            problems.append(f"[yaml-parse] {r}/{p}: {str(ex)[:50]}")
            continue
        for m in re.finditer(r'^\s+-\s+([a-z0-9-]+/[a-z0-9-]+)\s*$', text, re.M):
            ref = m.group(1)
            if tuple(ref.split("/")) not in have:
                problems.append(f"[dangling-ref] {r}/{p} -> {ref}")
        for pat in STALE_PATTERNS:
            for m in re.finditer(pat, text):
                problems.append(f"[stale] {r}/{p}: {m.group(0)!r}")

    if not problems:
        return  # healthy, stay silent

    print(f"Marketing OS integrity check — {len(problems)} issue(s) across {len(skills)} skills")
    for p in problems:
        print("  " + p)
    return

if __name__ == "__main__":
    main()

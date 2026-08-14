#!/usr/bin/env python3
"""Validate the tool binding: every allowed_tools value in every skill must
resolve to a key in execution/tool-registry.yaml. Prints violations, stays
silent when clean (watchdog-compatible)."""
import os, re, sys, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, "execution", "tool-registry.yaml")
REPOS = ["marketing-intelligence", "marketing-messaging", "marketing-channels",
         "marketing-paid", "marketing-optimize"]

def main():
    reg = yaml.safe_load(open(REGISTRY, encoding="utf-8"))
    known = set(reg["tools"].keys())
    known.add("none")

    violations = []
    operator = 0
    strategist = 0
    for r in REPOS:
        for root, dirs, files in os.walk(os.path.join(ROOT, r)):
            for fn in files:
                if fn != "SKILL.md":
                    continue
                path = os.path.join(root, fn)
                text = open(path, encoding="utf-8").read()
                skill = os.path.basename(root)
                m = re.search(r'^allowed_tools:\n((?:\s+-\s+.+\n)+|\s*\[\]\s*\n)', text, re.M)
                if not m:
                    strategist += 1
                    continue
                items = re.findall(r'-\s*(.+?)\s*$', m.group(1), re.M)
                items = [i.strip() for i in items]
                if not items or items == ["[]"]:
                    strategist += 1
                    continue
                operator += 1
                for it in items:
                    if it == "none":
                        continue
                    if it not in known:
                        violations.append(f"{r}/{skill}: undefined tool '{it}'")

    if violations:
        print(f"Tool binding violations ({len(violations)}):")
        for v in violations:
            print("  " + v)
        return
    # healthy
    return

if __name__ == "__main__":
    main()

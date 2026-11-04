#!/usr/bin/env python3
"""Päivitä TAIDOT.md: listaa .claude/skills/*/SKILL.md nimet ja kuvaukset taulukkoon.

Ajo megabrainin juuressa: python3 _tyokalut/paivita_taidot.py
Lukee jokaisen SKILL.md:n frontmatterista name- ja description-rivit. Ei riippuvuuksia.
"""
import os
import re
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
skills_dir = os.path.join(root, ".claude", "skills")
rows = []
broken = []
if os.path.isdir(skills_dir):
    for name in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, name, "SKILL.md")
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8", errors="replace") as f:
            head = f.read(4000)
        m = re.search(r"^description:\s*(.+?)\s*$", head, re.M)
        desc = m.group(1).strip() if m else ""
        if desc[:1] in ("'", '"') and desc[-1:] == desc[:1]:
            desc = desc[1:-1].replace("''", "'")
        if not desc:
            broken.append(name)
            desc = "⚠️ kuvaus puuttuu"
        desc = desc.replace("|", "\\|")
        if len(desc) > 220:
            desc = desc[:217].rstrip() + "…"
        rows.append(f"| {name} | {desc} |")

out = ["# Taidot", "",
       "Generoidaan komennolla `python3 _tyokalut/paivita_taidot.py`, ei käsin. Listaa `.claude/skills/*/SKILL.md`.",
       "", "| Taito | Mitä tekee ja milloin |", "|---|---|"] + rows
if broken:
    out += ["", "Kuvaus puuttuu tai ei jäsenny (korjaa frontmatter): " + ", ".join(broken)]
with open(os.path.join(root, "TAIDOT.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")
print(f"TAIDOT.md: {len(rows)} taitoa" + (f", {len(broken)} ilman kuvausta" if broken else ""))

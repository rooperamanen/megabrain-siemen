#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Taitomuistutus (Claude Code Stop-hook). Yleistetty megabrain-siemeneen 4.11.2026.

Kun tekoäly on lopettamassa vuoron, tämä skripti katsoo transkriptista, tehtiinkö
viimeisen ihmisviestin jälkeen työtä (tiedostoja kirjoitettiin, Bash muokkasi
jotain tai työkalukutsuja oli paljon) ja koskettiinko taitoihin
(.claude/skills/, TAIDOT.md tai taito `taidoksi`). Jos työtä tehtiin mutta
taitoihin ei koskettu, tekoäly saa kertaalleen muistutuksen arvioida, syntyikö
toistettava työtapa, ja tehdä siitä taito.

Syöte (stdin, JSON): session_id, transcript_path, cwd, hook_event_name,
stop_hook_active. Tuloste: JSON {"decision":"block","reason":...} tai tyhjä.
Virhetilanteissa skripti vaikenee (exit 0): hook ei saa koskaan estää työtä.

Pois päältä: luo tyhjä tiedosto OFF tähän kansioon (touch .claude/hooks/OFF).
Takaisin päälle: poista se. Testi: python3 taito-muistutus.py --testi
"""
import json
import os
import re
import sys

WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
BANK_MARKERS = (".claude/skills/", "TAIDOT.md", "taidoksi")
MIN_TOOL_CALLS = 12  # paljon hakuja/lukemista on myös työtä: tutkimusmenetelmä voi olla skilli
BASH_WRITE_RE = re.compile(
    r"(?<![0-9&<=\-])>>?\s*(?!/dev/null)[^\s|;&]"  # ohjaus tiedostoon, ei 2>/dev/null, ei -> tai =>
    r"|(?:^|[\s;&|(])(?:tee|cp|mv|mkdir|rsync|ln|touch|install|chmod|sed -i|perl -i)\s"
    r"|\bgit\s+(?:commit|push|add|mv|rm)\b"
    r"|\bgh\s+(?:issue|pr)\s+(?:create|edit|close|comment)\b"
    r"|(?:^|[\s;&|(])(?:openscad|ffmpeg|magick|convert|sips|pandoc|osascript)\s"
)

REASON = (
    "Taitotarkistus (Stop-hook .claude/hooks/taito-muistutus.py): "
    "tässä vuorossa tehtiin työtä, mutta taitoihin (.claude/skills/) ei koskettu. "
    "Arvioi nyt: syntyikö toistettava työtapa (menettely, skripti, tarkistuslista, asetukset, polut), "
    "jota omistaja todennäköisesti pyytää uudelleen? "
    "JOS KYLLÄ: lataa taito `taidoksi` (Skill-työkalu) ja luo tai päivitä taito sen ohjeen mukaan, "
    "aja python3 _tyokalut/paivita_taidot.py ja kerro omistajalle yhdellä rivillä, mikä taito syntyi tai päivittyi. "
    "JOS EI (kertaluonteinen asia, pelkkä kysymys tai keskustelu, tai työ on vielä kesken): "
    "lopeta ilman lisäselityksiä; kesken olevan työn taito tehdään, kun työ on valmis. "
    "Tämä muistutus tulee enintään kerran per vuoro."
)


def load_entries(path):
    entries = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except ValueError:
                continue
            if not isinstance(o, dict) or o.get("isSidechain"):
                continue
            if o.get("type") in ("user", "assistant"):
                entries.append(o)
    return entries


def is_human_prompt(o):
    if o.get("type") != "user" or o.get("isMeta"):
        return False
    if o.get("toolUseResult") is not None:
        return False
    c = (o.get("message") or {}).get("content")
    if isinstance(c, list):
        if any(isinstance(b, dict) and b.get("type") == "tool_result" for b in c):
            return False
    return True


def tool_uses_after_last_prompt(entries):
    start = None
    for i in range(len(entries) - 1, -1, -1):
        if is_human_prompt(entries[i]):
            start = i
            break
    if start is None:
        return []
    uses = []
    for o in entries[start + 1:]:
        if o.get("type") != "assistant":
            continue
        for b in (o.get("message") or {}).get("content") or []:
            if isinstance(b, dict) and b.get("type") == "tool_use":
                name = b.get("name") or ""
                inp = b.get("input") or {}
                uses.append((name, json.dumps(inp, ensure_ascii=False)))
    return uses


def decide(uses):
    """Palauta True, jos muistutus on paikallaan."""
    if not uses:
        return False
    if any(any(m in inp for m in BANK_MARKERS) for _, inp in uses):
        return False  # taitoihin koskettiin jo
    wrote = any(n in WRITE_TOOLS for n, _ in uses)
    bash_wrote = False
    for n, inp in uses:
        if n != "Bash":
            continue
        try:
            cmd = json.loads(inp).get("command", "")
        except ValueError:
            cmd = inp
        if BASH_WRITE_RE.search(cmd or ""):
            bash_wrote = True
            break
    substantial = len(uses) >= MIN_TOOL_CALLS
    return wrote or bash_wrote or substantial


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(os.path.join(here, "OFF")):
        return
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return
    if not isinstance(data, dict) or data.get("stop_hook_active"):
        return
    path = data.get("transcript_path")
    if not path or not os.path.isfile(path):
        return
    try:
        uses = tool_uses_after_last_prompt(load_entries(path))
        if decide(uses):
            print(json.dumps({"decision": "block", "reason": REASON}, ensure_ascii=False))
    except Exception:  # hook ei saa kaatua
        return


def _selftest():
    def bash(cmd):
        return ("Bash", json.dumps({"command": cmd}))
    cases = [
        ("tyhjä vuoro", [], False),
        ("vain lukua", [("Read", "{}"), bash("ls -la"), bash("grep -r foo . 2>/dev/null")], False),
        ("Edit tehty", [("Read", "{}"), ("Edit", json.dumps({"file_path": "/x/a.scad"}))], True),
        ("Bash kirjoitti", [bash("openscad -o a.stl a.scad")], True),
        ("Bash ohjaus tiedostoon", [bash("echo hei > loki.md")], True),
        ("Bash 2>/dev/null ei ole kirjoitus", [bash("python3 x.py 2>/dev/null")], False),
        ("python -> ei ole kirjoitus", [bash("python3 -c 'print(1) if 2 > 1 else 0'")], True),  # tunnettu heuristiikan raja
        ("taitoihin koskettu", [("Edit", json.dumps({"file_path": "/x/a.py"})),
                               ("Write", json.dumps({"file_path": "/Users/x/megabrain/.claude/skills/x/SKILL.md"}))], False),
        ("taidoksi ladattu", [("Edit", "{}"), ("Skill", json.dumps({"skill": "taidoksi"}))], False),
        ("paljon hakuja", [("Read", "{}")] * 12, True),
        ("vähän hakuja", [("Read", "{}")] * 5, False),
    ]
    ok = True
    for name, uses, want in cases:
        got = decide(uses)
        flag = "OK " if got == want else "VIRHE"
        ok &= got == want
        print(f"{flag} {name}: {got} (odotettu {want})")
    print("KAIKKI OK" if ok else "TESTEJÄ EPÄONNISTUI")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--testi":
        _selftest()
    else:
        main()

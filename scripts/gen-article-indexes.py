#!/usr/bin/env python3
"""Genererar articles/README.md (översikt över artikelkort) för varje domän och shared-modul.

Läser artikelkortens rubrik och regler. Regler hämtas både från kortets egen regellista
och från regler vars "Rättslig grund" länkar till kortet. Körs om efter ändringar.

Användning:
    python scripts/gen-article-indexes.py
"""
import os
import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"

# Tillämpningsdatum för domänen Återvändande (förordning 2026/2280 art. 50)
RR_DATES = {1: "16 okt 2026", 4: "16 okt 2026", 14: "16 okt 2026", 15: "16 okt 2026", 16: "16 okt 2026",
            34: "16 okt 2026", 35: "16 okt 2026", 41: "16 okt 2026", 43: "16 okt 2026", 47: "16 okt 2026",
            48: "16 okt 2026", 49: "16 okt 2026",
            2: "2.1–2.3: 16 okt 2026; övrigt 17 okt 2027", 3: "3.3: 16 okt 2026; övrigt 17 okt 2027",
            5: "5.13, 5.15: 16 okt 2026; övrigt 17 okt 2027", 50: "Ikraft 16 okt 2026 (anger datumen)"}


def field(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*\n+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def art_number(card_text, stem):
    m = re.search(r"artikel (\d+)", field(card_text, "Artikel"), re.I)
    if m:
        return int(m.group(1))
    m = re.search(r"(\d+)$", stem)
    return int(m.group(1)) if m else 0


def rules_for(card, text, rule_files):
    ids = set()
    sec = re.search(r"^## Härledda regler\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if sec:
        ids.update(re.findall(r"RULE-[A-Z0-9]+(?:-[A-Z0-9]+)+", sec.group(1)))
    for rf in rule_files:
        rt = rf.read_text(encoding="utf-8")
        basis = re.search(r"^## Rättslig grund\s*\n(.*?)(?=^## |^---|\Z)", rt, re.M | re.S)
        if basis and re.search(rf"articles/{re.escape(card.name)}\)", basis.group(1)):
            m = re.search(r"^# (RULE-[A-Z0-9-]+)", rt, re.M)
            if m:
                ids.add(m.group(1))
    return sorted(ids)


def build(module_dir):
    art_dir = module_dir / "articles"
    cards = sorted(p for p in art_dir.glob("*.md") if p.name != "README.md")
    if not cards:
        return None
    readme = module_dir / "README.md"
    title = re.search(r"^# (.+)$", readme.read_text(encoding="utf-8"), re.M).group(1) if readme.exists() else module_dir.name
    rule_files = list((module_dir / "rules").glob("*.md")) if (module_dir / "rules").exists() else []
    is_rr = module_dir.name == "return"

    rows = []
    for c in cards:
        t = c.read_text(encoding="utf-8")
        act_art = field(t, "Artikel")
        act_art = re.sub(r"\s*\(förordning \(EU\) [0-9/]+\)", "", act_art)
        rubrik = field(t, "Rubrik") or "—"
        rids = rules_for(c, t, rule_files)
        links = []
        for r in rids:
            target = None
            for rf in [module_dir / "rules" / f"{r.lower()}.md", *DOCS.glob(f"*/*/rules/{r.lower()}.md")]:
                if rf.exists():
                    target = Path(os.path.relpath(rf, art_dir)).as_posix()
                    break
            links.append(f"[{r}]({target})" if target else r)
        rule_cell = ", ".join(links) if links else "—"
        n = art_number(t, c.stem)
        row = [f"[{act_art}]({c.name})", rubrik.replace("|", "/"), rule_cell]
        if is_rr:
            row.insert(2, RR_DATES.get(n, "17 okt 2027"))
        rows.append((re.sub(r"\d+.*", "", c.stem), n, row))
    rows.sort(key=lambda r: (r[0], r[1]))

    head = ["Artikel", "Rubrik", "Regler"]
    if is_rr:
        head.insert(2, "Tillämpas från")
    short = re.sub(r"^Delat\s*[—-]\s*", "", title)
    kind = "modulens" if module_dir.parent.name == "shared" else "domänens"
    lines = [f"← [{short}](../README.md)", "", f"# Artiklar — {short}", "",
             f"Översikt över {kind} {len(rows)} artikelkort. Genereras av `scripts/gen-article-indexes.py`.", "",
             "| " + " | ".join(head) + " |", "|" + "|".join("-" * (len(h) + 2) for h in head) + "|"]
    lines += ["| " + " | ".join(r[2]) + " |" for r in rows]
    (art_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(rows), sum(1 for r in rows if r[2][-1] != "—")


def main():
    for base in ("domains", "shared"):
        for module_dir in sorted((DOCS / base).iterdir()):
            if (module_dir / "articles").is_dir():
                res = build(module_dir)
                if res:
                    print(f"{base}/{module_dir.name}: {res[0]} artiklar, {res[1]} med regler")


if __name__ == "__main__":
    main()

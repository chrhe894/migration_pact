#!/usr/bin/env python3
"""Genererar en katalog över obestämda tidsangivelser ("så snart som möjligt",
"utan dröjsmål", "omedelbart", "skyndsamt" m.fl.) i de bindande källtexterna.

Läser texterna i references/_text/ (skapas med scripts/mhtml-to-text.py).
Förarbeten (Ds, prop.) ingår inte. Skäl (före artikel 1) och bilagor ingår inte.

Användning:
    python scripts/gen-indeterminate-time.py
"""
import re
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT = ROOT / "references" / "_text"
OUT = ROOT / "docs" / "shared" / "time-limits" / "concepts" / "obestamda-tidsangivelser.md"

# (fil, kortnamn, rubrik, typ)
SOURCES = [
    ("OJ_L_202401356_SV_TXT.txt", "Screening", "Screeningförordningen (EU) 2024/1356", "eu"),
    ("OJ_L_202401358_SV_TXT.txt", "Eurodac", "Eurodacförordningen (EU) 2024/1358", "eu"),
    ("OJ_L_202401348_SV_TXT.txt", "APR", "Asylprocedurförordningen (EU) 2024/1348 (APR)", "eu"),
    ("OJ_L_202401349_SV_TXT.txt", "2024/1349", "Förordning (EU) 2024/1349 om gränsförfarande för återvändande", "eu"),
    ("OJ_L_202401351_SV_TXT.txt", "AMMR", "Asyl- och migrationshanteringsförordningen (EU) 2024/1351 (AMMR)", "eu"),
    ("OJ_L_202502055_SV_TXT.txt", "2025/2055", "Genomförandeförordning (EU) 2025/2055 till AMMR", "eu"),
    ("OJ_L_202401359_SV_TXT.txt", "Kris", "Krisförordningen (EU) 2024/1359", "eu"),
    ("OJ_L_202401346_SV_TXT.txt", "RCD", "Mottagandedirektivet (EU) 2024/1346", "eu"),
    ("OJ_L_2008348_SV_TXT.txt", "2008/115", "Återvändandedirektivet 2008/115/EG (gäller till 17 okt 2027)", "eu"),
    ("OJ_L_202602280_SV_TXT.txt", "RR", "Återvändandeförordningen (EU) 2026/2280 (i huvudsak från 17 okt 2027)", "eu"),
    ("OJ_L_2003321_SV_TXT.txt", "2003/110", "Direktiv 2003/110/EG om transitering för avlägsnande med flyg", "eu"),
    ("OJ_L_2004261_SV_TXT.txt", "2004/573", "Beslut 2004/573/EG om gemensamma flygningar för avlägsnande", "eu"),
    ("OJ_L_2016311_SV_TXT.txt", "2016/1953", "Förordning (EU) 2016/1953 om europeisk resehandling för återvändande", "eu"),
    ("OJ_L_2019295_SV_TXT.txt", "Frontex", "Förordning (EU) 2019/1896 om europeiska gräns- och kustbevakningen", "eu"),
    ("OJ_L_2020198_SV_TXT.txt", "2020/851", "Förordning (EU) 2020/851 om migrationsstatistik", "eu"),
    ("nationella/Utlänningslag (2005_716) - Regeringskansliets rättsdatabaser.txt", "UtlL",
     "Utlänningslagen (2005:716)", "se"),
    ("nationella/mottagandelagen_2026_999.txt", "Mottagandelagen", "Mottagandelagen (2026:999)", "se"),
    ("nationella/RA-FS 2026-1.txt", "RA-FS", "RA-FS 2026:1", "se"),
]

PHRASES = [
    ("så snart som möjligt", r"så snart som möjligt|så snart det är möjligt|så snart det är praktiskt möjligt"),
    ("snarast", r"\bsnarast(?: möjligt)?\b"),
    ("utan onödigt dröjsmål", r"utan onödigt dröjsmål"),
    ("utan dröjsmål", r"(?<!onödigt )\butan dröjsmål\b"),
    ("omedelbart", r"\bomedelbart\b"),
    ("genast", r"\bgenast\b"),
    ("skyndsamt", r"\bskyndsam(?:t|ma|hetskrav)?\b|\bmed tillbörlig skyndsamhet\b"),
    ("rimlig, skälig eller god tid", r"\b(?:inom|i) rimlig tid\b|\bi god tid\b|\bskälig tid(?:sfrist)?\b|\bskälig tidsperiod\b"),
    ("så kort tid som möjligt", r"så kort tid(?:speriod)? som möjligt|så kort tid som är möjligt|kortast möjliga tid|den tid som är strikt nödvändig"),
    ("intervall", r"\bregelbund(?:et|na) (?:intervall|tidsintervall|mellanrum)\b|\blämpliga (?:tids)?intervall\b|\blämpliga mellanrum\b|\bfortlöpande\b|\bså ofta det finns anledning\b"),
]
PHRASE_RE = [(name, re.compile(rx, re.I)) for name, rx in PHRASES]

NUM = r"(?:\d+|en|ett|två|tre|fyra|fem|sex|sju|åtta|nio|tio|elva|tolv|femton|tjugo|trettio)"
UNIT = r"(?:arbets)?(?:dagar|dag|dygn|timmar|timme|veckor|vecka|månader|månad|år)"
OUTER_RE = re.compile(
    rf"\b(?:senast|inom|dock|i alla händelser|högst|före|inte senare än)\b[^.;]*?\b{NUM}\s+{UNIT}\b"
    r"|\bsenast (?:vid|när|i samband med|före|innan|den dag)\b|\bföre utgången av\b|\bi alla händelser (?:före|innan)\b",
    re.I)
# Beskrivande användning som inte är en tidsangivelse för en skyldighet
SKIP_RE = re.compile(r"omedelbart avlägsna|omedelbart verkställ|omedelbar verkställighet|omedelbart omhändert", re.I)
EFFECT_RE = re.compile(r"\b(?:gäller|gälla) omedelbart\b|\bomedelbart gäll", re.I)
INTERVAL_NUM_RE = re.compile(rf"\b(?:minst|åtminstone)\s+(?:var|vart|varje)\s+\w+\s+{UNIT}\b|\bvar\s+(?:tredje|fjärde|sjätte|annan)\s+{UNIT}\b", re.I)
MARKER_RE = re.compile(r"/([^/]{3,80}?)\s*([UI]):(\d{4}-\d{2}-\d{2})/")

TYPES = OrderedDict([
    ("MED_YTTRE_GRÄNS", "Obestämd med yttre gräns"),
    ("OBESTÄMD", "Obestämd utan yttre gräns"),
    ("VARAKTIGHET", "Så kort tid som möjligt"),
    ("INTERVALL", "Återkommande utan fast intervall"),
    ("VERKAN", "Verkan inträder omedelbart"),
])


def classify(phrase, sentence):
    if phrase == "så kort tid som möjligt":
        return "VARAKTIGHET"
    if phrase == "intervall":
        return "MED_YTTRE_GRÄNS" if OUTER_RE.search(sentence) or INTERVAL_NUM_RE.search(sentence) else "INTERVALL"
    if phrase == "omedelbart" and EFFECT_RE.search(sentence):
        return "VERKAN"
    if OUTER_RE.search(sentence):
        return "MED_YTTRE_GRÄNS"
    return "OBESTÄMD"


def blocks_eu(lines):
    """Ger (artikel, punkt, text) för de operativa artiklarna."""
    start = next((i for i, l in enumerate(lines) if l.strip() == "Artikel 1"), None)
    if start is None:
        return
    art, para, buf = None, None, []
    for l in lines[start:]:
        s = l.strip()
        if re.fullmatch(r"BILAGA(?: [IVX]+)?", s):
            break
        m = re.fullmatch(r"Artikel (\d+[a-z]?)", s)
        if m:
            if buf:
                yield art, para, " ".join(buf)
            art, para, buf = m.group(1), None, []
            continue
        m = re.match(r"^(\d{1,2})\.(?:\s+(.*))?$", s)
        if m and art is not None:
            if buf:
                yield art, para, " ".join(buf)
            para, buf = m.group(1), ([m.group(2)] if m.group(2) else [])
            continue
        if s:
            buf.append(s)
    if buf:
        yield art, para, " ".join(buf)


def blocks_se(lines):
    """Ger (kapitel, paragraf, text). Markerar lydelse från 1 dec 2027."""
    chap, sec, buf, version = None, None, [], ""
    for l in lines:
        s = l.strip()
        m = re.match(r"^(\d+ ?[a-z]?) kap\. [A-ZÅÄÖ]", s)
        if m and len(s) < 120 and not s.endswith(","):
            if buf:
                yield chap, sec, version, " ".join(buf)
            chap, sec, buf, version = m.group(1).replace(" ", " "), None, [], ""
            continue
        m = re.match(r"^(\d+ ?[a-z]?) § (.*)$", s)
        if m and chap and re.match(r"[A-ZÅÄÖ/]", m.group(2) or ""):
            if buf:
                yield chap, sec, version, " ".join(buf)
            sec, buf, version = m.group(1), [m.group(2)], ""
            continue
        if "Träder i kraft I:2027-12-01" in s:
            if buf:
                yield chap, sec, version, " ".join(buf)
            buf, version = [], "från 1 dec 2027"
            continue
        if "Upphör att gälla U:2027-12-01" in s:
            if buf:
                yield chap, sec, version, " ".join(buf)
            buf, version = [], "till 1 dec 2027"
            continue
        if s:
            buf.append(s)
    if buf:
        yield chap, sec, version, " ".join(buf)


SENT_SPLIT = re.compile(r"(?<=[.;:])\s+(?=[A-ZÅÄÖ0-9a-z]\)|[A-ZÅÄÖ])")


def excerpt(sentence, match, width=260):
    sentence = re.sub(r"\s+", " ", sentence).strip()
    if len(sentence) <= width:
        return sentence
    a = max(0, match.start() - width // 2)
    b = min(len(sentence), a + width)
    a = max(0, b - width)
    out = sentence[a:b]
    return ("…" if a > 0 else "") + out + ("…" if b < len(sentence) else "")


def slug(t):
    """Samma som standardslugify i Python-Markdown (toc)."""
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode("ascii")
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"[-\s]+", "-", t)


def esc(t):
    return t.replace("|", "\\|")


def rows_from(ref, text, rows, seen):
    for sent in SENT_SPLIT.split(text):
        for name, rx in PHRASE_RE:
            m = rx.search(sent)
            if not m:
                continue
            if name == "omedelbart" and SKIP_RE.search(sent[max(0, m.start() - 5):m.end() + 25]):
                continue
            # "fortlöpande ... inom två månader" är en fast frist, inte en obestämd
            if name == "intervall" and m.group(0).lower() == "fortlöpande" and (OUTER_RE.search(sent) or "inom samma tid" in sent):
                continue
            ex = excerpt(sent, m)
            key = (ref, name, ex)
            if key in seen:
                continue
            seen.add(key)
            rows.append((ref, name, classify(name, sent), ex))


def main():
    results = OrderedDict()
    for fname, short, title, kind in SOURCES:
        path = TEXT / fname
        if not path.exists():
            print(f"saknas: {fname}")
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        rows, seen = [], set()
        if kind == "eu":
            items = ((f"{short} art. {a}" + (f".{p}" if p else ""), t) for a, p, t in blocks_eu(lines))
        else:
            items = ((f"{short} {c}:{s or '–'}" + (f" ({v})" if v else ""), t)
                     for c, s, v, t in blocks_se(lines) if c)
        for ref, text in items:
            # Dela upp vid lydelsemarkeringar så att varje mening får rätt lydelse
            segments, label, pos = [], "", 0
            for m in MARKER_RE.finditer(text):
                segments.append((label, text[pos:m.start()]))
                what, kind_, date = m.group(1).strip(), m.group(2), m.group(3)
                if kind_ == "I":
                    label = f"lydelse från {date}"
                elif what.startswith("Ny beteckning"):
                    label = what.replace("Ny beteckning ", "blir ") + f" från {date}"
                else:
                    label = f"lydelse till {date}"
                pos = m.end()
            segments.append((label, text[pos:]))
            for label, seg in segments:
                seg_ref = f"{ref} ({label})" if label else ref
                seg = re.sub(r"-{3} Sida \d+ -{3}", " ", seg)
                seg = re.sub(r"\s+", " ", seg)
                rows_from(seg_ref, seg, rows, seen)
        results[short] = (title, rows)

    out = []
    out.append("""---
tags:
  - shared
  - tidsfrister
  - koncept
---

# Obestämda tidsangivelser

> Sidan är genererad av `scripts/gen-indeterminate-time.py`. Ändra i skriptet, inte här.

## Syfte

Många skyldigheter har ingen fast frist. Texten säger i stället "så snart som möjligt", "utan dröjsmål", "omedelbart" eller "skyndsamt". Sidan listar alla sådana formuleringar i de bindande texterna i repot, så att en applikation för tidsfrister kan hantera dem. Förarbeten (Ds, prop.), skäl och bilagor ingår inte. Se även [Konsekvens vid överskriden frist](konsekvens-vid-overskriden-frist.md).

## Typer

| Typ | Innebörd | Hur ett system kan hantera den |
|-----|----------|--------------------------------|
| **Obestämd med yttre gräns** | "så snart som möjligt, dock senast 3 dagar". Den fasta gränsen är den rättsliga fristen. Den obestämda delen är ett krav på att inte vänta till sista dagen | Bevaka den fasta gränsen som frist. Mät faktisk tid som kvalitetsmått |
| **Obestämd utan yttre gräns** | "utan dröjsmål", "omedelbart", "skyndsamt" utan siffra | Ingen frist att räkna. Verksamheten behöver ett eget mål (servicenivå), till exempel "inom 1 arbetsdag". Målet är inte en rättslig frist och ska märkas så |
| **Så kort tid som möjligt** | Gäller en varaktighet, till exempel förvar. Kombineras ofta med ett tak | Bevaka taket. Kräv att skälen för fortsatt åtgärd dokumenteras löpande |
| **Återkommande utan fast intervall** | "regelbundet", "lämpliga intervall", "fortlöpande", "så ofta det finns anledning". Anger texten också ett minsta intervall ("dock minst var tredje dag") räknas träffen som *med yttre gräns* | Verksamheten bestämmer intervall. Om lagen anger ett fast intervall någon annanstans gäller det |
| **Verkan inträder omedelbart** | "beslutet gäller omedelbart". Ingen frist, utan en regel om när ett beslut får verkan | Sätt verkansdatum till beslutsdatum |

Typningen är maskinell. En träff får typen *med yttre gräns* om samma mening innehåller "senast", "inom", "dock", "högst", "före" eller "inte senare än" följt av ett antal timmar, dagar, veckor, månader eller år. Den får också typen om gränsen är en händelse, till exempel "senast vid registreringen" eller "före utgången av tidsfristen". "Fortlöpande inom två månader" är en fast frist och står i stället på sidan om konsekvenser. "Omedelbart avlägsnas" och "omedelbar verkställighet" är beskrivningar, inte tidsangivelser, och är inte med. Kontrollera alltid mot texten innan en regel byggs.

## Översikt
""")
    types = list(TYPES)
    out.append("| Akt | " + " | ".join(TYPES[t] for t in types) + " | Totalt |")
    out.append("|-----|" + "|".join(":---:" for _ in types) + "|:---:|")
    tot = Counter()
    for short, (title, rows) in results.items():
        c = Counter(r[2] for r in rows)
        tot.update(c)
        anchor = slug(title)
        out.append(f"| [{short}](#{anchor}) | " + " | ".join(str(c.get(t, 0)) for t in types) + f" | {len(rows)} |")
    out.append("| **Totalt** | " + " | ".join(f"**{tot.get(t, 0)}**" for t in types) + f" | **{sum(tot.values())}** |")
    out.append("")
    for short, (title, rows) in results.items():
        out.append(f"## {title}")
        out.append("")
        if not rows:
            out.append("Inga träffar.")
            out.append("")
            continue
        out.append("| Bestämmelse | Formulering | Typ | Utdrag |")
        out.append("|-------------|-------------|-----|--------|")
        for ref, name, typ, ex in rows:
            out.append(f"| {esc(ref)} | {name} | {TYPES[typ]} | {esc(ex)} |")
        out.append("")
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)}: {sum(tot.values())} träffar")
    for t in types:
        print(f"  {TYPES[t]}: {tot.get(t, 0)}")


if __name__ == "__main__":
    main()

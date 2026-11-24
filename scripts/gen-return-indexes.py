#!/usr/bin/env python3
"""Genererar capability-kort samt index för regler och krav i domänen Återvändande (docs/domains/return).

Läser regel-ID och korta titlar från artikelkortens "Härledda regler" och kravens
"Krav"-, "Härledd från"- och "Stöds av"-sektioner. Körs om efter ändringar.
"""
import re
import tempfile
from pathlib import Path

DOMAIN = Path(__file__).resolve().parent.parent / "docs" / "domains" / "return"

CAPS = [
    ("001", "Issue Return Decision", "Avgöra om förordningen är tillämplig, utfärda beslut om återvändande, fastställa tidsfrist för avresa och utfärda inreseförbud.", [2, 4, 5, 6, 8, 9],
     ["Beslut om återvändande (europeisk återvändandeorder)", "Tidsfrist för avresa eller krav på omedelbar avresa", "Inreseförbud"],
     ["Beslut om att avsluta eller neka laglig vistelse", "Uppgifter om identitet och återvändandeland"]),
    ("002", "Recognise and Enforce Return Decisions of Other Member States", "Erkänna och verkställa beslut om återvändande från en annan medlemsstat.", [7],
     ["Verkställighet av annan medlemsstats beslut", "Eget beslut när erkännande inte sker"],
     ["Europeisk återvändandeorder via SIS", "Uppgifter från den utfärdande medlemsstaten"]),
    ("003", "Carry Out Removal", "Avlägsna personen, skjuta upp avlägsnandet när det krävs och hantera säkerhetsrisker och avtal med tredjeland.", [10, 11, 12, 13, 14],
     ["Beslut om avlägsnande", "Verkställt avlägsnande", "Skriftlig bekräftelse av uppskjutande"],
     ["Beslut om återvändande", "Bedömning av non-refoulement", "Resehandlingar"]),
    ("004", "Safeguard Minors in Return", "Beakta barnets bästa, genomföra åldersbedömning och säkerställa mottagande av ensamkommande barn.", [15, 16, 17],
     ["Bedömning av barnets bästa", "Åldersbedömning", "Försäkran om mottagande"],
     ["Uppgifter om ålder och familj", "Företrädare för ensamkommande barn"]),
    ("005", "Manage Cooperation and Risk of Absconding", "Hantera skyldigheten att samarbeta, bedöma risk för avvikande och besluta om tillgänglighetsåtgärder och alternativ till förvar.", [18, 19, 20, 21, 22, 23],
     ["Bedömning av risk för avvikande", "Beslut om tillgänglighetsåtgärder och alternativ till förvar", "Konsekvenser vid bristande samarbete"],
     ["Uppgifter från personen", "Uppgifter om tidigare avvikande"]),
    ("006", "Handle Information, Legal Aid and Appeals", "Informera personen, ge rättsligt bistånd och hantera överklaganden och uppskjutande i domstol.", [24, 25, 26, 27, 28],
     ["Information till personen", "Beslut om rättsligt bistånd", "Överklagande och eventuellt uppskjutande av avlägsnande"],
     ["Beslut om återvändande, avlägsnande och inreseförbud", "Datum för underrättelse"]),
    ("007", "Manage Return Detention", "Besluta om förvar, bevaka förvarstidens tak och genomföra återkommande prövningar.", [29, 30, 31, 32, 33],
     ["Beslut om förvar", "Prövning av förvaret", "Frigivning"],
     ["Bedömning av risk för avvikande", "Säkerhetsbedömning", "Uppgifter om ålder och sårbarhet"]),
    ("008", "Readmission and Third-Country Cooperation", "Inleda återtagande och utbyta uppgifter med medlemsstater och tredjeländer.", [34, 35, 36, 37, 38, 39],
     ["Framställan om återtagande", "Utbytta uppgifter", "Resehandling"],
     ["Beslut om återvändande", "Identitets- och hälsouppgifter"]),
    ("009", "Operate the Common Return System", "Utse behöriga myndigheter, samarbeta, använda Frontex-stöd, ge återvändandestöd, hantera kris och rapportera.", [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
     ["Återvändande- och återintegreringsstöd", "Statistik och rapporter", "Underrättelse om krisåtgärder"],
     ["Uppgifter från alla förmågor"]),
]


# Regler från andra rättsakter och delprocesser per förmåga
EXTRA_RULES = {
    "003": [("RULE-JRF-004-001", "Gemensam flygning: organiserande medlemsstat"),
            ("RULE-JRF-005-001", "Gemensam flygning: deltagande medlemsstat"),
            ("RULE-JRF-006-001", "Gemensam flygning: handlingar, viseringar och beskickningar"),
            ("RULE-JRF-007-001", "Riktlinjer för säkerhet vid återsändande med flyg"),
            ("RULE-FRX-050-001", "Frontex återvändandeinsatser"),
            ("RULE-FRX-053-001", "Frontex återvändandeinterventioner (fem arbetsdagar)"),
            ("RULE-UTL-12-014-001", "Verkställande myndighet (UtlL 12:14)"),
            ("RULE-UTL-12-015-001", "När beslutet ska verkställas (UtlL 12:15)"),
            ("RULE-UTL-12-021-001", "Verkställt när personen lämnat landet (UtlL 12:21)")],
    "008": [("RULE-ETD-003-001", "Europeisk resehandling för återvändande"),
            ("RULE-ETD-005-001", "Resehandlingen är kostnadsfri"),
            ("RULE-FRX-048-001", "Frontex stöd, konsulärt samarbete utan att röja asylansökan"),
            ("RULE-APR-007-001", "Tystnadsplikt mot påstådda förföljare (APR 7)")],
    "009": [("RULE-UTL-12-014C-001", "Förlänga eller upphäva tidsfrist för frivillig avresa (UtlL 12:14 b–c)")],
}
EXTRA_PROCS = {
    "003": ["[PROC-RTN-005 Återvändandesamordning – resa](../processes/return-coordination-travel.md)"],
    "005": ["[PROC-RTN-004 Återvändandesamordning – ambassad](../processes/return-coordination-embassy.md)"],
    "008": ["[PROC-RTN-004 Återvändandesamordning – ambassad](../processes/return-coordination-embassy.md)"],
    "009": ["[PROC-RTN-006 Frivilligt återvändande med stöd](../processes/assisted-voluntary-return.md)"],
}


def rule_link(rid):
    if rid.startswith("RULE-APR-"):
        return f"../../asylum-procedure/rules/{rid.lower()}.md"
    return f"../rules/{rid.lower()}.md"


def rule_titles():
    titles = {}
    for card in sorted((DOMAIN / "articles").glob("rr-*.md")):
        for m in re.finditer(r"^- \[(RULE-RR-\d{3}-\d{3})\]\([^)]*\) — (.+)$", card.read_text(encoding="utf-8"), re.M):
            titles[m.group(1)] = m.group(2).strip()
    return titles


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return ""
    return "\n".join(l for l in m.group(1).strip().splitlines() if l.strip() and l.strip() != "---").strip()


def main():
    titles = rule_titles()
    caps_dir = DOMAIN / "capabilities"
    caps_dir.mkdir(exist_ok=True)

    cap_rows = []
    for num, name, purpose, arts, produces, consumes in CAPS:
        rules = [r for r in sorted(titles) if int(r.split("-")[2]) in arts]
        art_links = ", ".join(f"[{a}](../articles/rr-{a:03d}.md)" for a in arts)
        body = [
            "---", "tags:", "  - återvändande", "  - förmåga", "---", "",
            "← [Återvändande](../README.md)", "", f"# CAP-RTN-{num}", "",
            "## Verksamhetsförmåga", "", name, "", "---", "", "## Syfte", "", purpose, "", "---", "",
            "## Artiklar", "", f"Återvändandeförordningen art. {art_links}", "", "---", "",
            "## Implementerar", "",
        ]
        body += [f"- [{r}](../rules/{r.lower()}.md) — {titles[r]}" for r in rules] or ["- —"]
        extra = EXTRA_RULES.get(num, [])
        if extra:
            body += ["", "Från andra rättsakter:", ""]
            body += [f"- [{r}]({rule_link(r)}) — {t}" for r, t in extra]
        body += ["", "---", "", "## Stöds av", "",
                 "- [PROC-RTN-001 Återvändandeförfarande](../processes/return-procedure.md)"]
        body += [f"- {p}" for p in EXTRA_PROCS.get(num, [])]
        if num == "007":
            body.append("- [PROC-RTN-002 Förvar inför avlägsnande](../processes/return-detention.md)")
        if num == "002":
            body.append("- [PROC-RTN-003 Erkännande av annan medlemsstats beslut](../processes/recognition-of-return-decision.md)")
        body += ["", "---", "", "## Producerar", ""] + [f"- {p}" for p in produces]
        body += ["", "---", "", "## Konsumerar", ""] + [f"- {c}" for c in consumes]
        body += ["", "---", "", "## Status", "", "Complete", ""]
        (caps_dir / f"cap-rtn-{num}.md").write_text("\n".join(body), encoding="utf-8")
        cap_rows.append(f"| [CAP-RTN-{num}](cap-rtn-{num}.md) | {name} | Art. {', '.join(map(str, arts))} | {len(rules) + len(extra)} |")

    (caps_dir / "README.md").write_text("\n".join([
        "← [Återvändande](../README.md)", "", "# Verksamhetsförmågor — Återvändande", "",
        "| ID | Förmåga | Artiklar | Antal regler |", "|----|---------|----------|--------------|", *cap_rows, ""]), encoding="utf-8")

    req_rows = []
    for req in sorted((DOMAIN / "requirements").glob("req-rr-*.md")):
        t = req.read_text(encoding="utf-8")
        rid = req.stem.upper()
        krav = " ".join(section(t, "Krav").split())
        if len(krav) > 160:
            krav = krav[:157].rsplit(" ", 1)[0] + " …"
        krav = krav.replace("|", "/")
        src = ", ".join(re.findall(r"RULE-RR-\d{3}-\d{3}", section(t, "Härledd från"))) or "—"
        cap = ", ".join(sorted(set(re.findall(r"CAP-RTN-\d{3}", section(t, "Stöds av"))))) or "—"
        req_rows.append(f"| [{rid}]({req.name}) | {krav} | {src} | {cap} |")
    (DOMAIN / "requirements" / "README.md").write_text("\n".join([
        "← [Återvändande](../README.md)", "", "# Krav — Återvändande", "",
        "| ID | Krav | Härledd från | Förmåga |", "|----|------|--------------|---------|", *req_rows, ""]), encoding="utf-8")

    rule_rows = [f"| [{r}](rules/{r.lower()}.md) | {titles[r]} |" for r in sorted(titles)]
    # Tabellrader för regeltabellen i domänens README (klistras in manuellt)
    out = Path(tempfile.gettempdir()) / "return-rules-table.md.txt"
    out.write_text("\n".join(rule_rows), encoding="utf-8")
    print(f"Regeltabell: {out}")
    print(f"{len(CAPS)} förmågor, {len(req_rows)} krav, {len(rule_rows)} regler")


if __name__ == "__main__":
    main()

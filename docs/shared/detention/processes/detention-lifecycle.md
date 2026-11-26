---
tags:
  - förvar
  - process
---

← [Förvar](../README.md)

# PROC-DET-001

# Förvar — huvudprocess

## Trigger

Det finns ett behov av att frihetsberöva en utlänning för att säkra ett förfarande: identifiering, asylutredning, gränsförfarandet, ansvarsförfarandet eller verkställighet.

---

## Resultat

Ett beslut om förvar eller uppsikt med angiven grund och beslutsfattare, eller ett konstaterande att förutsättningar saknas. Under förvaret bevakas klockorna och händelser från andra processer tills förvaret upphör ([PROC-DET-004](release.md)).

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/detention-lifecycle.svg" width="100%"></object>

Källa: [`detention-lifecycle.pu`](../diagrams/detention-lifecycle.pu)

---

## Steg

| # | Steg | Regel |
|---|------|-------|
| 1 | Vid brådska: Polismyndighetens **interimistiska beslut** (FG-12). Anmäls skyndsamt och prövas omedelbart av behörig myndighet | [RULE-UTL-10-020-001](../rules/rule-utl-10-020-001.md) |
| 2 | Bestäm **beslutsfattare**: Polis (avvisningsärende, verkställighet), Säpo (verkställighet i säkerhetsärende), annars Migrationsverket | [RULE-UTL-10-020-001](../rules/rule-utl-10-020-001.md) |
| 3 | Bestäm **status**: sökande (har rätt att vistas här som sökande) eller inte, vuxen eller barn | [RULE-UTL-10-003-001](../rules/rule-utl-10-003-001.md), [RULE-UTL-10-005-001](../rules/rule-utl-10-005-001.md) |
| 4 | Pröva om **uppsikt räcker**. Förvar bara om syftet inte kan nås med uppsikt | [RULE-UTL-10-002-001](../rules/rule-utl-10-002-001.md) |
| 5 | Välj **förvarsgrund** (FG). Grunden styr tak, prövning och domstolsfrist | [Beslutskatalog](../decision-catalogue.md#1-forvarsgrunder-fg) |
| 6 | Skriftligt, motiverat **beslut om förvar** (BH-03) | [RULE-RD-015-001](../rules/rule-rd-015-001.md), [RULE-AMMR-044-001](../../../domains/responsibility/rules/rule-ammr-044-001.md) |
| 7 | **Verkställ** och starta klockorna: K1 grundtak, K2 ny prövning, K5 total tid, och vid ansvarsförfarande K4 | [Beslutskatalog, klockor](../decision-catalogue.md#2-klockor-k) |
| 8 | **Bevaka**: händelser från andra processer hanteras i [PROC-DET-002](change-of-ground.md). Ny prövning i [PROC-DET-003](review-and-court.md) | — |
| 9 | **Upphörande** när skälen faller bort, ett tak nås, en frist passeras eller personen överförs eller avlägsnas | [PROC-DET-004](release.md) |

---

## Alternativa flöden

**Uppsikt i stället för förvar.** Om syftet kan nås med anmälningsplikt, inlämnat pass, boende på viss plats eller vistelse inom visst område beslutas uppsikt (UP-01). Från 1 december 2027 kan uppsikt inom ett område förenas med elektronisk övervakning (förstärkt uppsikt, UP-02). Ny prövning inom 6 månader, vid förstärkt uppsikt 3 månader och för barn 1 månad ([RULE-UTL-10-015-001](../rules/rule-utl-10-015-001.md)).

**Barn.** Förvar bara på de snävare grunderna i 10:4 och 10:6, inte om barnet skiljs från vårdnadshavare, och för barn utan vårdnadshavare bara vid synnerliga skäl. Högst **72 timmar**, vid synnerliga skäl ytterligare 72. I säkerhetsärenden högst 3 (6) månader **sammanlagt**, med ny prövning varje månad ([RULE-UTL-10-013-001](../rules/rule-utl-10-013-001.md), [RULE-UTL-10-017-001](../rules/rule-utl-10-017-001.md)).

**Gränsförfarandet för asyl.** FG-04, högst 12 veckor. Om ansökan avslås och rätten att stanna kvar upphör går förvaret över i återvändandegränsförfarandet (FG-10) med ett **nytt beslut** ([PROC-DET-002, scenario B](change-of-ground.md#scenario-b-gransforfarande-till-atervandande)).

**Ansvarsförfarandet (Dublin).** FG-07. Framställan inom 2 veckor (1 vecka om förvaret sker senare), svar inom 1 vecka, beslut om överföring inom 2 veckor och överföring inom 5 veckor. Missas en frist ska personen friges ([RULE-AMMR-045-001](../../../domains/responsibility/rules/rule-ammr-045-001.md)).

**Säkerhetsärende.** Säpo beslutar vid verkställighet. FG-09 får pågå 12 + 12 månader ([RULE-UTL-10-012-001](../rules/rule-utl-10-012-001.md)).

**Annan lag inskränker rörelsefriheten** (t.ex. LVU, psykiatrisk tvångsvård, smittskydd). Beslut om förvar får fattas men verkställs först när förutsättningarna är uppfyllda (10:9). Den ansvariga nämnden eller läkaren underrättar när omhändertagandet upphör (10:10).

**Från 17 oktober 2027** gäller förordning 2026/2280 för förvar inför återvändande: tak 12 + 12 + 6 månader och prövning minst var sjätte månad ([PROC-RTN-002](../../../domains/return/processes/return-detention.md)). Utlänningslagen har ännu inte anpassats.

---

## Juridiska milstolpar

- Beslut om förvar (eller interimistiskt beslut) med grund
- Verkställighet påbörjad (start för K2)
- Överklagande inkommet (start för K3 för sökande)
- Varje ny prövning
- Upphävande eller upphörande

---
tags:
  - förvar
  - process
  - prövning
  - tidsfrister
---

← [Förvar](../README.md)

# PROC-DET-003

# Ny prövning och domstolsprövning

## Trigger

Ett förvars- eller uppsiktsbeslut gäller, och fristen för ny prövning närmar sig (K2, K6), eller beslutet överklagas (K3).

---

## Resultat

Förvaret eller uppsikten består efter ny prövning, eller upphävs. Vid överklagande: domstolens slutliga avgörande.

---

## Ny prövning hos myndigheten

| Beslut | Frist | Räknas från | Regel |
|--------|-------|-------------|-------|
| Förvar enligt FG-03–07, FG-09, FG-10 och 10:9 | **Inom 2 månader** | Den dag **verkställigheten påbörjades** (eller verkställigheten av ett interimistiskt beslut). Därefter från **senaste förvarsbeslutet** | [RULE-UTL-10-016-001](../rules/rule-utl-10-016-001.md) |
| Barn i säkerhetsärende eller barn som utvisats på grund av brott | **Inom 1 månad** | Som ovan | [RULE-UTL-10-017-001](../rules/rule-utl-10-017-001.md) |
| Uppsikt | **Inom 6 månader** | Beslutsdagen, därefter senaste prövningen | [RULE-UTL-10-015-001](../rules/rule-utl-10-015-001.md) |
| Förstärkt uppsikt (från 1 dec 2027) | **Inom 3 månader**, barn **1 månad** | Som ovan | [RULE-UTL-10-015-001](../rules/rule-utl-10-015-001.md) |
| FG-01, FG-02, FG-08 | Ingen tvåmånadersprövning | Tak 4 veckor | [RULE-UTL-10-011-001](../rules/rule-utl-10-011-001.md) |

| # | Steg | Regel |
|---|------|-------|
| 1 | Bevaka fristen. Varna i god tid | — |
| 2 | Kalla till **muntlig förhandling** (för förvar alltid, för uppsikt om den inte uppenbart saknar betydelse) | [RULE-UTL-10-018-001](../rules/rule-utl-10-018-001.md) |
| 3 | Pröva om skälen och grunden består, om uppsikt räcker, och om taket tillåter fortsatt förvar | [RULE-UTL-10-002-001](../rules/rule-utl-10-002-001.md), [RULE-UTL-10-014-001](../rules/rule-utl-10-014-001.md) |
| 4 | Nytt beslut (BH-05). Ny tvåmånadersfrist räknas från detta beslut | [RULE-UTL-10-016-001](../rules/rule-utl-10-016-001.md) |
| 5 | **Om fristen passeras utan prövning upphör beslutet** (BH-44) → frigivning | [RULE-UTL-10-019-001](../rules/rule-utl-10-019-001.md) |

---

## Domstolsprövning

| Förvar | Frist för domstolen | Följd | Regel |
|--------|---------------------|-------|-------|
| Asylsökande (10 kap. 3–4 §§) | Slutligt avgörande **inom 15 dagar**, särskilda skäl **21 dagar**, från att överklagandet kom in | Efter 21 dagar **upphör beslutet** (BH-45) | [RULE-UTL-16-004-001](../rules/rule-utl-16-004-001.md) |
| Övriga (10 kap. 5–6 §§) | Skyndsam handläggning, ingen dagsfrist | — | Utlänningslagen 16 kap. 4 § första st. |

EU-rätten kräver snabb rättslig prövning när en administrativ myndighet fattat beslutet: för sökande mottagandedirektivet art. 11.3 (15 dagar, i undantagsfall 21, annars omedelbar frigivning; [RULE-RCD-011-001](../rules/rule-rcd-011-001.md)), AMMR art. 44.5, direktiv 2008/115/EG art. 15.2 och, från 17 oktober 2027, förordning 2026/2280 art. 31.3.

Mottagandedirektivet art. 11.5 kräver dessutom att en rättslig myndighet omprövar förvaret av en sökande med lämpliga intervall, och förvar av **ensamkommande barn** på eget initiativ med regelbundna intervall. I Sverige sker den nya prövningen efter 2 månader (10:16) hos den myndighet som fattat beslutet. Den kan överklagas till domstol.

---

## Alternativa flöden

- **Interimistiskt beslut:** behörig myndighet ska pröva omedelbart. Tvåmånadersfristen räknas från verkställigheten av det interimistiska beslutet ([RULE-UTL-10-020-001](../rules/rule-utl-10-020-001.md)).
- **Kris (från 17 oktober 2027):** medlemsstaten får tillämpa längre tidsfrister för rättslig prövning av förvar ([RULE-RR-045-001](../../../domains/return/rules/rule-rr-045-001.md)).

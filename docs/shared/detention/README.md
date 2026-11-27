---
tags:
  - shared
  - förvar
  - uppsikt
  - tidsfrister
---

# Delat — Förvar

## Syfte

Modulen samlar förvar och uppsikt över alla förfaranden: asylprövning, gränsförfarandet, ansvarsförfarandet, återvändandegränsförfarandet och återvändande. Den beskriver förvarsgrunder, tidsfrister, prövning och upphörande, och hur beslut i **andra** processer påverkar ett pågående förvar.

Förvar är en egen process som **lyssnar på händelser** från de andra processerna. Ett beslut om avslag, överföring eller uppehållstillstånd kan göra att förvarsgrunden ändras eller faller bort. Se [Beslutskatalog och händelsematris](decision-catalogue.md).

---

## Primära rättskällor

- [Utlänningslagen 10 kap.](../../references/legislation/utlanningslagen.md) — Uppsikt och förvar (grunder, längsta tid, ny prövning, beslutsfattare)
- [Utlänningslagen 16 kap. 4 §](rules/rule-utl-16-004-001.md) — Domstolsprövning av förvar av asylsökande inom 15 (21) dagar
- [AMMR artikel 44](../../domains/responsibility/articles/ammr-044.md) och [45](../../domains/responsibility/articles/ammr-045.md) — Förvar i ansvarsförfarandet
- [Förordning 2024/1349 artikel 5](../../domains/return-border-procedure/articles/return-005.md) — Förvar i återvändandegränsförfarandet
- [Direktiv 2008/115/EG artikel 15](../../references/legislation/return-directive.md) — Förvar inför återvändande (till 17 oktober 2027)
- [Förordning 2026/2280 artikel 29–33](../../domains/return/articles/rr-029.md) — Förvar inför återvändande (från 17 oktober 2027)

- [Mottagandedirektivet (EU) 2024/1346 artikel 10–13](../../references/legislation/reception-directive.md) — EU-ramen för förvar av sökande: grunder (10.4 a–g), garantier och domstolsprövning (11), förhållanden (12) och sökande med särskilda behov samt barn (13). Genomförs i utlänningslagen 10 kap. 3–4 §§ och 16 kap. 4 §

!!! note "Ändrat innehåll"
    Mottagandedirektivet finns nu i repot. Tidigare stod här att det saknades.

---

## Processer

| Process | Beskrivning |
|---------|-------------|
| [PROC-DET-001 Förvar — huvudprocess](processes/detention-lifecycle.md) | Från frihetsberövande till frigivning: beslut, verkställighet, bevakning |
| [PROC-DET-002 Händelsehantering och byte av förvarsgrund](processes/change-of-ground.md) | Vad som händer med förvaret när ett beslut fattas i en annan process |
| [PROC-DET-003 Ny prövning och domstolsprövning](processes/review-and-court.md) | Tvåmånadersprövning, muntlig förhandling, domstolsfrist |
| [PROC-DET-004 Upphörande och frigivning](processes/release.md) | Alla vägar ut ur förvaret |

---

## Översikt: förvarsgrunder och tidsfrister

| Förfarande | Grund | Längsta tid | Ny prövning | Domstol | Gäller |
|------------|-------|-------------|-------------|---------|--------|
| Asylprövning | Identitet, utreda grunder (FG-01–02) | 4 veckor | — | 15 (21) dagar | Nu |
| Asylprövning | Boendebeslut, försena verkställighet, säkerhet (FG-03, 05, 06) | 12 månader | 2 månader | 15 (21) dagar | Nu |
| Gränsförfarandet för asyl | FG-04 | 12 veckor (+6 vid kris) | 2 månader | 15 (21) dagar | Nu |
| Ansvarsförfarandet | FG-07 (AMMR art. 44) | Överföring inom 5 veckor efter godtagande | 2 månader | 15 (21) dagar | Nu |
| Återvändandegränsförfarandet | FG-10 | Tolvveckorsperioden (+6 vid kris) | 2 månader | Skyndsamt | Nu |
| Verkställighet | FG-09 | 6 + 12 månader (säkerhet 12 + 12; EES 6/12) | 2 månader | Skyndsamt | Nu; EU-ram ändras 17 okt 2027 |
| Barn | FG-11 | 72 + 72 timmar; säkerhet 3 (6) mån | Säkerhet 1 månad | 15 (21) om sökande | Nu |
| Uppsikt | UP-01 | — | 6 månader | — | Nu |
| Förstärkt uppsikt | UP-02 | Barn 3 (6) mån; säkerhet 12 (18) | 3 mån; barn 1 mån | — | 1 dec 2027 |

Fullständig tabell med lagrum och beslutsfattare: [Beslutskatalog](decision-catalogue.md#1-forvarsgrunder-fg).

---

## Regler

| Regel | Innehåll |
|-------|----------|
| [RULE-UTL-10-002-001](rules/rule-utl-10-002-001.md) | Förvar endast om uppsikt inte räcker |
| [RULE-UTL-10-003-001](rules/rule-utl-10-003-001.md) | Förvarsgrunder för vuxna sökande |
| [RULE-UTL-10-004-001](rules/rule-utl-10-004-001.md) | Förvarsgrunder för barn som söker skydd |
| [RULE-UTL-10-005-001](rules/rule-utl-10-005-001.md) | Förvarsgrunder för vuxna som inte är sökande |
| [RULE-UTL-10-006-001](rules/rule-utl-10-006-001.md) | Barn som inte är sökande; barn skiljs inte från vårdnadshavare |
| [RULE-UTL-10-011-001](rules/rule-utl-10-011-001.md) | Längsta tid: 4 veckor, 12 veckor, 12 månader |
| [RULE-UTL-10-012-001](rules/rule-utl-10-012-001.md) | Längsta tid inför verkställighet: 6 + 12 månader m.m. |
| [RULE-UTL-10-013-001](rules/rule-utl-10-013-001.md) | Barn: 72 + 72 timmar; säkerhetsärende 3 (6) månader |
| [RULE-UTL-10-014-001](rules/rule-utl-10-014-001.md) | Omedelbart upphävande när skälen faller bort |
| [RULE-UTL-10-015-001](rules/rule-utl-10-015-001.md) | Ny prövning av uppsikt: 6 mån (förstärkt 3, barn 1) |
| [RULE-UTL-10-016-001](rules/rule-utl-10-016-001.md) | Ny prövning av förvar inom 2 månader |
| [RULE-UTL-10-017-001](rules/rule-utl-10-017-001.md) | Barn i säkerhetsärende: ny prövning inom 1 månad |
| [RULE-UTL-10-018-001](rules/rule-utl-10-018-001.md) | Muntlig förhandling vid ny prövning |
| [RULE-UTL-10-019-001](rules/rule-utl-10-019-001.md) | Beslutet upphör om ny prövning inte sker i tid |
| [RULE-UTL-10-020-001](rules/rule-utl-10-020-001.md) | Beslutande myndighet och interimistiskt beslut |
| [RULE-UTL-10-023-001](rules/rule-utl-10-023-001.md) | Upphävande vid uppehållstillstånd eller skydd; inhibition |
| [RULE-UTL-16-004-001](rules/rule-utl-16-004-001.md) | Domstolens avgörande inom 15 (21) dagar |
| [RULE-RCD-010-001](rules/rule-rcd-010-001.md) | Mottagandedirektivet art. 10: förvarsgrunder för sökande (10.4 a–g), individuell bedömning |
| [RULE-RCD-011-001](rules/rule-rcd-011-001.md) | Mottagandedirektivet art. 11: skriftligt beslut, domstolsprövning inom 15 (21) dagar, omprövning |
| [RULE-RD-015-001](rules/rule-rd-015-001.md) | Direktiv 2008/115/EG art. 15: 6 + 12 månader, frigivning utan utsikter |

Regler i andra domäner: [RULE-AMMR-044-001](../../domains/responsibility/rules/rule-ammr-044-001.md), [RULE-AMMR-045-001](../../domains/responsibility/rules/rule-ammr-045-001.md), [RULE-AMMR-045-002](../../domains/responsibility/rules/rule-ammr-045-002.md), [RULE-RET-005-001](../../domains/return-border-procedure/rules/rule-ret-005-001.md), [RULE-RR-029-001](../../domains/return/rules/rule-rr-029-001.md) – [RULE-RR-033-001](../../domains/return/rules/rule-rr-033-001.md).

---

## Paragrafnummer från 1 december 2027

Utlänningslagen 10 kap. får ny numrering genom SFS 2026:1427, och förstärkt uppsikt införs. Reglerna i modulen använder nuvarande nummer och anger det nya.

| Nu | Från 1 dec 2027 | Innehåll |
|----|-----------------|----------|
| 1 § | 1 § | Uppsikt |
| — | 2–3 §§ | Förstärkt uppsikt (elektronisk övervakning) och positionsuppgifter |
| 2 § | 4 § | Förvar bara om uppsikt inte räcker |
| 3–4 §§ | 5–6 §§ | Grunder för sökande (vuxna, barn) |
| 5–6 §§ | 7–8 §§ | Grunder för övriga (vuxna, barn) |
| 7–9 §§ | 9–11 §§ | Barn och vårdnadshavare; inskränkt rörelsefrihet |
| — | 13 § | Längsta tid för förstärkt uppsikt av barn |
| 11–13 §§ | 14–16 §§ | Längsta tid för förvar |
| 14–19 §§ | 17–22 §§ | Upphävande, ny prövning, muntlig förhandling, upphörande |
| 20–24 §§ | 23–27 §§ | Beslutande myndigheter, interimistiskt beslut |

---

## Öppna frågor

- [Sammanräkning av förvarstid och start av klockor](open_questions/aggregation-of-detention-time.md)

---

## Används av

- [PROC-RES-001 Ansvarig medlemsstat och överföring](../../domains/responsibility/processes/determine-responsible-member-state.md)
- [PROC-BRD-001 Gränsförfarande för asyl](../../domains/border-procedure/processes/asylum-border-procedure.md)
- [PROC-RET-001 Gränsförfarande för återvändande](../../domains/return-border-procedure/processes/return-border-procedure.md)
- [PROC-RTN-002 Förvar inför avlägsnande](../../domains/return/processes/return-detention.md) (från 17 oktober 2027)
- [Uppsikt](../time-limits/concepts/uppsikt.md)

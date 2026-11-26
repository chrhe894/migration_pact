---
tags:
  - förvar
  - process
  - upphörande
---

← [Förvar](../README.md)

# PROC-DET-004

# Upphörande och frigivning

## Trigger

Någon av händelserna nedan inträffar.

---

## Resultat

Personen är frigiven, eller förvaret har avslutats genom överföring eller avlägsnande. Förvarsperioden (K5) avslutas och dokumenteras.

---

## Vägar ut ur förvaret

| Orsak | BH | Typ | Avslutskod | Regel |
|-------|----|-----|------------|-------|
| Skälen för förvaret finns inte längre | — | Upphävande, **omedelbart** | UPPH | [RULE-UTL-10-014-001](../rules/rule-utl-10-014-001.md) |
| Uppehållstillstånd eller internationellt skydd beviljas | BH-15 | Upphävande i samma beslut | UPPH | [RULE-UTL-10-023-001](../rules/rule-utl-10-023-001.md) |
| Uppsikt räcker | BH-04 | Ersätts av uppsikt | UPPH | [RULE-UTL-10-002-001](../rules/rule-utl-10-002-001.md) |
| Statusbyte utan ny grund | BH-14, BH-16 | Upphävande | UPPH | [PROC-DET-002](change-of-ground.md) |
| Ny prövning sker inte i tid | BH-44 | **Beslutet upphör** automatiskt | FÖRFALLER | [RULE-UTL-10-019-001](../rules/rule-utl-10-019-001.md) |
| Domstolen avgör inte inom 21 dagar (sökande) | BH-45 | **Beslutet upphör** automatiskt | FÖRFALLER | [RULE-UTL-16-004-001](../rules/rule-utl-16-004-001.md) |
| Domstolen bifaller överklagandet | BH-07 | Upphävande | UPPH | [RULE-UTL-16-004-001](../rules/rule-utl-16-004-001.md) |
| Grundtaket nås och förlängning är inte tillåten | BH-43 | Frigivning | UPPH ⚠ | [RULE-UTL-10-011-001](../rules/rule-utl-10-011-001.md), [012](../rules/rule-utl-10-012-001.md), [013](../rules/rule-utl-10-013-001.md) |
| AMMR-frist missad | BH-25 | Frigivning. Ansvarsförfarandet fortsätter | UPPH | [RULE-AMMR-045-001](../../../domains/responsibility/rules/rule-ammr-045-001.md) |
| Rimliga utsikter till avlägsnande saknas | BH-33 | Frigivning | UPPH | [RULE-RD-015-001](../rules/rule-rd-015-001.md) |
| Tolvveckorsperioden i återvändandegränsförfarandet slut | K7 | FG-10 upphör. Nytt beslut FG-09 eller frigivning | UPPH, eller nytt beslut UTL / VERK | [RULE-RET-005-001](../../../domains/return-border-procedure/rules/rule-ret-005-001.md) |
| Personen överförs till ansvarig medlemsstat | BH-26 | Avslutat | UPPH ⚠ | — |
| Personen avlägsnas | BH-34 | Avslutat, beslutet verkställt | UPPH ⚠ | [RULE-UTL-12-021-001](../../../domains/return/rules/rule-utl-12-021-001.md) |

---

Avslutskoder: **UPPH** = upphävande genom beslut, **FÖRFALLER** = beslutet upphör att gälla enligt lag. ⚠ = förslag, se [avslutskoder](../decision-catalogue.md#avslutskoder).

---

## Steg

| # | Steg |
|---|------|
| 1 | Registrera orsak och tidpunkt |
| 2 | Vid upphävande: fatta beslut. Vid automatiskt upphörande: konstatera och frige utan dröjsmål |
| 3 | Pröva om uppsikt eller tillgänglighetsåtgärder behövs efter frigivningen. Från 17 oktober 2027 får åtgärder enligt förordning 2026/2280 art. 20 och 23 tillämpas även när förvarstaken löpt ut (art. 30.5) |
| 4 | Avsluta förvarsperioden (K5) och spara total tid. Den behövs om personen tas i förvar igen |
| 5 | Underrätta berörda processer (asyl, ansvar, återvändande) och mottagandet |

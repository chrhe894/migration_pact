---
tags:
  - screening-vid-yttre-grans
  - screening
  - process
---


# PROC-SCR-001

# Screening vid yttre gräns

## Trigger

En tredjelandsmedborgare omhändertas vid otillåten gränspassage, landsätts efter sök- och räddningsinsats, eller gör en asylansökan vid ett gränsövergångsställe utan att uppfylla inresevillkoren.

---

## Resultat

Personen har genomgått screening och hänvisats till rätt förfarande med screeningformuläret som underlag.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/screening-at-external-border.svg" width="100%"></object>

Källa: [`screening-at-external-border.pu`](../diagrams/screening-at-external-border.pu)

---

## Alternativt flöde — massinflöde/förkortad period

Om personen befunnit sig vid yttre gränsen i mer än 72 timmar förkortas screeningperioden till fyra dagar ([RULE-SCR-008-001](../rules/rule-scr-008-001.md)).

---

## Alternativt flöde — tidsfrist löper ut

Om inte alla kontroller slutförts inom sju dagar ska screeningen ändå avslutas och personen hänvisas till lämpligt förfarande.

---

## Alternativt flöde — inresevillkor uppfylls

Om det under screeningen framkommer att personen uppfyller inresevillkoren ska screeningen avslutas.

---

## Juridiska milstolpar

- Screening inledd
- Screening avslutad
- Hänvisning till förfarande

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Person omhändertagen, ej identifierad | Screening genomförs | Identifierad, screenad, hänvisad till förfarande |

---

## Tidsfrister

| Tidsfrist | Källa | Kommentar |
|-----------|-------|-----------|
| **Ordinarie** — 7 dagar | [Screening art. 8](../articles/screening-008.md) | Maximal screeningperiod vid yttre gräns |
| **Förkortad** — 4 dagar | [Screening art. 8](../articles/screening-008.md) | Om personen befunnits >72h vid gränsen |

### Koppling till statistik

| Datapunkt | Betydelse | Källa |
|-----------|-----------|-------|
| Genomsnittlig screeningtid | Tidseffektivitet mot 7-dagarskravet | Nationell statistik |
| Andel hänvisade till asylförfarande vs återvändande | Flödesfördelning efter screening | Nationell statistik |

---

## Regler

- [RULE-SCR-005-001](../rules/rule-scr-005-001.md) — Screening obligatorisk vid gränspassage
- [RULE-SCR-005-002](../rules/rule-scr-005-002.md) — Screening av asylsökande vid gränsövergångsställen
- [RULE-SCR-008-001](../rules/rule-scr-008-001.md) — Tidsfrist sju dagar
- [RULE-SCR-008-003](../rules/rule-scr-008-003.md) — Obligatoriska delar
- [RULE-SCR-014-001](../rules/rule-scr-014-001.md) — Identifiering
- [RULE-SCR-015-001](../rules/rule-scr-015-001.md) — Säkerhetskontroll
- [RULE-SCR-017-001](../rules/rule-scr-017-001.md) — Screeningformulär
- [RULE-SCR-018-001](../rules/rule-scr-018-001.md) — Hänvisning

---

## Delade aktiviteter

- [Verifiera identitet](../../../shared/identity/activities/verify-identity.md)
- [Fastställ tolkbehov](../../../shared/interpreters/activities/determine-interpreter-needs.md)
- [Samla in och överföra biometriska uppgifter](../../eurodac/processes/collect-and-transmit-biometric-data.md)

---

## Diagram

Se huvudflöde ovan.

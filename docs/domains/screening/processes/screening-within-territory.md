---
tags:
  - screening
  - process
---


# PROC-SCR-002

# Screening inom territoriet

## Trigger

En tredjelandsmedborgare som vistas olagligt inom territoriet omhändertas och har passerat en yttre gräns på otillåtet sätt utan att tidigare ha genomgått screening.

---

## Resultat

Personen har genomgått screening och hänvisats till rätt förfarande.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/screening-within-territory.svg" width="100%"></object>

Källa: [`screening-within-territory.pu`](../diagrams/screening-within-territory.pu)

---

## Alternativt flöde — bilateral överföring

Om personen omedelbart skickas tillbaka till en annan medlemsstat enligt bilateralt avtal ansvarar den mottagande medlemsstaten för screeningen.

---

## Juridiska milstolpar

- Screening inledd
- Screening avslutad
- Hänvisning till förfarande

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Person som vistas olagligt, ej screenad | Screening genomförs | Person screenad, hänvisad till förfarande |

---

## Regler

- [RULE-SCR-008-002](../rules/rule-scr-008-002.md) — Tidsfrist tre dagar
- [RULE-SCR-007-001](../rules/rule-scr-007-001.md) — Screening inom territoriet
- [RULE-SCR-008-003](../rules/rule-scr-008-003.md) — Obligatoriska delar
- [RULE-SCR-014-001](../rules/rule-scr-014-001.md) — Identifiering
- [RULE-SCR-015-001](../rules/rule-scr-015-001.md) — Säkerhetskontroll
- [RULE-SCR-017-001](../rules/rule-scr-017-001.md) — Screeningformulär
- [RULE-SCR-018-001](../rules/rule-scr-018-001.md) — Hänvisning

---

## Shared Activities

- [Verify identity](../../../shared/identity/activities/verify-identity.md)
- [Samla in och överföra biometriska uppgifter](../../eurodac/processes/collect-and-transmit-biometric-data.md)

---

## Diagram

Se huvudflöde ovan.

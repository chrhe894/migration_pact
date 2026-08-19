---
tags:
  - återvändande-vid-gräns
  - återvändande
  - process
---


# PROC-RET-001

# Återvändande vid gräns

## Trigger

En ansökan om internationellt skydd har avslagits eller avvisats i asylgränsförfarandet och personen har inte rätt att stanna kvar.

---

## Resultat

Personen har återvänt (frivilligt eller genom avlägsnande) eller tidsfrist löpt ut och inresa tillåtits.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/return-border-procedure.svg" width="100%"></object>

Källa: [`return-border-procedure.pu`](../diagrams/return-border-procedure.pu)

---

## Alternativt flöde — överklagande

Personen överklagar och beviljas suspensiv verkan. Tidsfristerna fryser till dess domstolsprövningen avslutats.

---

## Juridiska milstolpar

- Rejection in border procedure
- Return decision issued
- Voluntary departure period (max 15 days)
- Removal executed / Entry permitted (12 weeks)

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Person med avslag i gränsförfarande | Återvändandebeslut + 12 veckor | Person har lämnat EU / Tidsfrist löpt ut → inresa |

---

## Tidsfrister

| Tidsfrist | Källa | Kommentar |
|-----------|-------|-----------|
| **Maximal varaktighet** — 12 veckor | [Återvändandeförordningen art. 5](../articles/return-005.md) | Från återvändandebeslut till verkställighet |
| **Frivillig avresa** — 15 dagar | [Återvändandeförordningen art. 5](../articles/return-005.md) | Maximal period för frivillig avresa |

### Koppling till statistik

| Datapunkt | Betydelse | Källa |
|-----------|-----------|-------|
| Andel frivilliga avresor | Andel som reser frivilligt inom 15 dagar | Nationell statistik |
| Andel verkställda avlägsnanden | Effektivitetsmått för återvändande | Nationell statistik |
| Genomsnittlig handläggningstid | Tidseffektivitet mot 12-veckorskravet | Nationell statistik |

---

## Regler

- [RULE-RET-004-001](../rules/rule-ret-004-001.md) — Tillämpning efter avslag
- [RULE-RET-005-001](../rules/rule-ret-005-001.md) — Maximal varaktighet 12 veckor

---

## Diagram

Se huvudflöde ovan.

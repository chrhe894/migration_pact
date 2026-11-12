---
tags:
  - återvändande-vid-gräns
  - återvändande
  - process
---


# PROC-RET-001

# Gränsförfarande för återvändande

## Trigger

En ansökan om internationellt skydd har **avslagits** i gränsförfarandet för asyl, och personen har inte längre rätt att stanna kvar och tillåts inte stanna kvar.

---

## Resultat

Personen har återvänt, frivilligt eller genom avlägsnande. Alternativt har tolvveckorsperioden löpt ut och återvändandet fortsätter enligt återvändandedirektivet 2008/115/EG.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/return-border-procedure.svg" width="100%"></object>

Källa: [`return-border-procedure.pu`](../diagrams/return-border-procedure.pu)

---

## Alternativt flöde — överklagande med rätt att stanna kvar

Har personen rätt att stanna kvar under överklagandet, eller tillåter en domstol det ([APR art. 68](../../asylum-procedure/articles/apr-068.md)), har tolvveckorsperioden **inte börjat**. Perioden börjar den dag rätten att stanna kvar upphör ([art. 4.2](../articles/return-004.md)). Det är ingen frysning av en löpande frist. Tolvveckorsperioden får en senare startpunkt.

---

## Alternativt flöde — återvändandet hinns inte verkställas

Kan beslutet om återvändande inte verkställas inom tolvveckorsperioden fortsätter återvändandeförfarandet enligt återvändandedirektivet ([art. 4.4](../articles/return-004.md)). Förordningen ger **ingen** rätt till inresa. Förvar enligt direktivet räknas in i direktivets maximala förvarsperioder ([art. 5.4](../articles/return-005.md)).

---

## Alternativt flöde — kris

I en krissituation får tolvveckorsperioden och förvarsperioden förlängas med högst sex veckor ([art. 6](../articles/return-006.md)), efter en begäran enligt [art. 7](../articles/return-007.md). De berörda ska informeras om åtgärderna och deras varaktighet ([art. 8](../articles/return-008.md)).

---

## Juridiska milstolpar

- Avslag i gränsförfarandet för asyl
- Rätten att stanna kvar upphör (tolvveckorsperioden börjar)
- Eventuell tidsfrist för frivillig avresa (på begäran, högst 15 dagar)
- Återvändande verkställt, eller återvändandet fortsätter enligt direktiv 2008/115/EG

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Person med avslag i gränsförfarandet för asyl | Gränsförfarande för återvändande | Har återvänt, eller återvändandet fortsätter enligt återvändandedirektivet |

---

## Tidsfrister

| Tidsfrist | Startar | Källa | Kommentar |
|-----------|---------|-------|-----------|
| **Gränsförfarandet för återvändande** — högst 12 veckor | Den dag personen inte längre har rätt att stanna kvar och inte tillåts stanna kvar | [RULE-RET-004-002](../rules/rule-ret-004-002.md) ([art. 4.2](../articles/return-004.md)) | Fryses inte. Ett överklagande med rätt att stanna kvar skjuter upp starten |
| **Vid kris** — +högst 6 veckor (max 18) | Som ovan | [RULE-RET-006-001](../rules/rule-ret-006-001.md) ([art. 6.1 a](../articles/return-006.md)) | Kräver rådets genomförandebeslut |
| **Förvar** — högst lika länge som perioden ovan | — | [RULE-RET-005-001](../rules/rule-ret-005-001.md) ([art. 5.4](../articles/return-005.md)) | Sista utväg |
| **Frivillig avresa** — högst 15 dagar | Beviljas på begäran | [RULE-RET-004-003](../rules/rule-ret-004-003.md) ([art. 4.5](../articles/return-004.md)) | Ger ingen rätt till inresa |

Fristerna beräknas enligt förordningens egen regel i [art. 11](../articles/return-011.md) ([RULE-RET-011-001](../rules/rule-ret-011-001.md)). Startdagen räknas inte in och helgdagar räknas in. En frist som slutar på en helgdag flyttas till nästa arbetsdag. Något krav på minst två arbetsdagar finns inte.

### Koppling till statistik

| Datapunkt | Betydelse | Källa |
|-----------|-----------|-------|
| Andel frivilliga avresor | Andel som reser frivilligt inom beviljad tidsfrist | Nationell statistik |
| Andel verkställda återvändanden inom 12 veckor | Effektivitetsmått | Nationell statistik |
| Andel som går vidare till återvändandedirektivet | Ärenden som inte hunnit verkställas | Nationell statistik |

---

## Regler

- [RULE-RET-004-001](../rules/rule-ret-004-001.md) — Ingen inresa efter avslag
- [RULE-RET-004-002](../rules/rule-ret-004-002.md) — Tolvveckorsperioden
- [RULE-RET-004-003](../rules/rule-ret-004-003.md) — Frivillig avresa
- [RULE-RET-005-001](../rules/rule-ret-005-001.md) — Förvar
- [RULE-RET-006-001](../rules/rule-ret-006-001.md) — Förlängning vid kris
- [RULE-RET-011-001](../rules/rule-ret-011-001.md) — Fristberäkning

---

## Kommentar

> **Rättelse:** processidan angav tidigare art. 5 som grund för tolvveckorsperioden och frivillig avresa. Den angav också att fristerna "fryser" vid överklagande och att inresa tillåts efter tolv veckor. Inget av detta stämmer mot förordningstexten.

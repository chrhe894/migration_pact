---
tags:
  - registrering-av-ansökan
  - registrering
  - process
---


# PROC-REG-001

# Registrering av en ansökan

## Trigger

En person uttrycker en önskan att ansöka om internationellt skydd.

---

## Resultat

Ansökan är registrerad, sökanden har tillhandahållits registreringshandling och ärendet kan gå vidare till inlämnande.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/registration-of-an-application.svg" width="100%"></object>

Källa: [`registration-of-an-application.pu`](../diagrams/registration-of-an-application.pu)

---

## Alternativt flöde — ansökan görs till fel myndighet

Om ansökan görs till en myndighet som inte är registreringsbehörig underrättar den myndigheten registreringsmyndigheten inom tre arbetsdagar ([RULE-APR-027-003](../rules/rule-apr-027-003.md)). Registreringsmyndigheten registrerar ansökan senast fem dagar efter att den tagit emot informationen.

---

## Alternativt flöde — massinflöde

Om ett oproportionellt stort antal ansökningar görs inom samma period kan registreringen ske senast 15 dagar efter att ansökan gjordes ([RULE-APR-027-004](../rules/rule-apr-027-004.md)).

---

## Alternativt flöde — sökanden har genomgått screening

Om sökanden har genomgått screening enligt Screeningförordningen artikel 5.1 ska registreringen ske efter att screeningen avslutats ([RULE-APR-027-005](../rules/rule-apr-027-005.md)).

---

## Juridiska milstolpar

- Application made
- Application registered

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Person uttryckt önskan om skydd | Ansökan registreras | Registrerad ansökan, registreringshandling utfärdad |

---

## Tidsfrister

| Tidsfrist | Källa | Kommentar |
|-----------|-------|-----------|
| **Ordinarie** — 5 dagar | [APR art. 27](../articles/apr-027.md) | Från ansökan gjord till registrering |
| **Massinflöde** — 15 dagar | [APR art. 27](../articles/apr-027.md) | Vid oproportionellt stort antal ansökningar |
| **Vid kris** — 4 veckor | [Krishanteringsförordningen art. 10](../../crisis/articles/crisis-010.md) | Förlängd tidsfrist vid kris |

### Koppling till statistik

| Datapunkt | Betydelse | Källa |
|-----------|-----------|-------|
| Antal registrerade per dag | Volym- och kapacitetsuppföljning | Nationell statistik |
| Andel registrerade inom tidsfrist | Efterlevnadsmått mot 5-dagarskravet | Nationell statistik |

---

## Regler

- [RULE-APR-027-001](../rules/rule-apr-027-001.md) — Skyldighet att registrera
- [RULE-APR-027-002](../rules/rule-apr-027-002.md) — Uppgifter som ska registreras
- [RULE-APR-027-003](../rules/rule-apr-027-003.md) — Anmälan vid fel myndighet
- [RULE-APR-027-004](../rules/rule-apr-027-004.md) — Tidsfrist vid massinflöde
- [RULE-APR-027-005](../rules/rule-apr-027-005.md) — Tillämpning efter screening
- [RULE-APR-029-001](../rules/rule-apr-029-001.md) — Registreringshandling

---

## Delade aktiviteter

- [Verifiera identitet](../../../shared/identity/activities/verify-identity.md)
- [Fastställ tolkbehov](../../../shared/interpreters/activities/determine-interpreter-needs.md)

---

## Diagram

Se huvudflöde ovan.
---
tags:
  - fastställ-ansvarig-medlemsstat
  - ansvar
  - process
---


# PROC-RES-001

# Fastställ ansvarig medlemsstat

## Trigger

En ansökan om internationellt skydd har registrerats och ansvarig medlemsstat ska fastställas.

---

## Resultat

Ansvarig medlemsstat har fastställts och sökanden kan hänvisas till rätt stat för prövning.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/determine-responsible-member-state.svg" width="100%"></object>

Källa: [`determine-responsible-member-state.pu`](../diagrams/determine-responsible-member-state.pu)

---

## Alternativt flöde — diskretionär bedömning

Medlemsstaten får besluta att överta prövningsansvaret av humanitära skäl oavsett kriterierna ([RULE-AMMR-035-001](../rules/rule-ammr-035-001.md)).

---

## Alternativt flöde — ansvarets upphörande

Om tidsfristerna i artikel 33 har löpt ut (20 resp. 12 månader) kan inresestaten inte längre hållas ansvarig ([RULE-AMMR-033-002](../rules/rule-ammr-033-002.md)).

---

## Juridiska milstolpar

- Application registered (referenspunkt)
- Responsible Member State determined
- Take charge request sent (om annan stat)
- Transfer decision (om annan stat)

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Ansökan registrerad, ansvarig stat okänd | Kriterier tillämpas | Ansvarig stat fastställd |
| Ansvarig stat ≠ nuvarande stat | Framställan om övertagande | Överföringsbeslut fattat |

---

## Tidsfrister

| Tidsfrist | Källa | Kommentar |
|-----------|-------|-----------|
| **Framställan om övertagande** — 2 månader | [AMMR art. 39](../articles/ammr-039.md) | Från registrering |
| **Framställan vid Eurodac-träff** — 1 månad | [AMMR art. 39](../articles/ammr-039.md) | Förkortad vid Eurodac-bevis |
| **Svar på framställan** — 1 månad | [AMMR art. 40](../articles/ammr-040.md) | Ordinarie svarsfrist |
| **Svar vid Eurodac-träff** — 2 veckor | [AMMR art. 40](../articles/ammr-040.md) | Förkortad svarsfrist |
| **Överföring** — 6 månader | [AMMR art. 46](../articles/ammr-046.md) | Från godkännande till verkställighet |
| **Överföring vid avvikande** — 18 månader | [AMMR art. 46](../articles/ammr-046.md) | Förlängd vid avvikande |

### Koppling till statistik

| Datapunkt | Betydelse | Källa |
|-----------|-----------|-------|
| Antal framställningar | Volymuppföljning av övertagandeförfaranden | Nationell statistik |
| Acceptansgrad | Andel godkända framställningar | Nationell statistik |
| Andel verkställda överföringar | Effektivitetsmått | Nationell statistik |
| Genomsnittlig överföringstid | Tidseffektivitet mot 6-månaderskravet | Nationell statistik |

---

## Regler

- [RULE-AMMR-024-001](../rules/rule-ammr-024-001.md) — Kriterierna i angiven ordning
- [RULE-AMMR-024-002](../rules/rule-ammr-024-002.md) — Situationen vid första registrering
- [RULE-AMMR-025-001](../rules/rule-ammr-025-001.md) — Ensamkommande barn
- [RULE-AMMR-029-001](../rules/rule-ammr-029-001.md) — Uppehållshandling eller visering
- [RULE-AMMR-033-001](../rules/rule-ammr-033-001.md) — Första irreguljära inresa
- [RULE-AMMR-033-002](../rules/rule-ammr-033-002.md) — Tidsbegränsning
- [RULE-AMMR-035-001](../rules/rule-ammr-035-001.md) — Diskretionär bedömning

---

## Delade aktiviteter

- [Verifiera identitet](../../../shared/identity/activities/verify-identity.md)

---

## Diagram

Se huvudflöde ovan.

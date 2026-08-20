---
tags:
  - utfärda-sökandehandlingar
  - registrering
  - process
---


# PROC-REG-003

# Utfärda sökandehandlingar

## Trigger

En ansökan om internationellt skydd har registrerats eller lämnats in.

---

## Resultat

Sökanden har tillhandahållits de handlingar som krävs enligt [APR artikel 29](../articles/apr-029.md).

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/issue-applicant-documents.svg" width="100%"></object>

Källa: [`issue-applicant-documents.pu`](../diagrams/issue-applicant-documents.pu)

---

## Alternativt flöde — direkt utfärdande

Om sökandehandlingen kan utfärdas direkt vid registreringen ska registreringshandlingen inte utfärdas ([APR artikel 29.2](../articles/apr-029.md), se [RULE-APR-029-001](../rules/rule-apr-029-001.md)).

---

## Alternativt flöde — förvar eller fängelsestraff

Om sökanden är i förvar eller avtjänar fängelsestraff behöver handlingarna inte utfärdas. När sökanden friges ska handlingen tillhandahållas ([APR artikel 29.5](../articles/apr-029.md), se [RULE-APR-029-001](../rules/rule-apr-029-001.md)).

---

## Alternativt flöde — medföljande barn

För medföljande barn kan handlingar som utfärdas till förälder eller ansvarig vuxen i tillämpliga fall även omfatta barnet ([APR artikel 29.6](../articles/apr-029.md)).

---

## Juridiska milstolpar

- Application registered — registreringshandling utfärdas
- Application lodged — sökandehandling utfärdas

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Ansökan registrerad, inga handlingar | Registreringshandling utfärdas | Sökande med registreringshandling |
| Ansökan inlämnad | Sökandehandling utfärdas | Sökande med sökandehandling |

---

## Tidsfrister

| Tidsfrist | Källa | Kommentar |
|-----------|-------|-----------|
| **Registreringshandling** — vid registrering | [APR art. 29](../articles/apr-029.md) | Utfärdas omedelbart vid registrering |
| **Sökandehandling** — vid inlämnande | [APR art. 29](../articles/apr-029.md) | Utfärdas senast vid inlämnande |
| **Giltighetstid** — 12 månader | [APR art. 29](../articles/apr-029.md) | Förnyas automatiskt |

### Koppling till statistik

| Datapunkt | Betydelse | Källa |
|-----------|-----------|-------|
| Antal utfärdade handlingar | Volymuppföljning | Nationell statistik |
| Förnyelsefrekvens | Andel handlingar som förnyats | Nationell statistik |

---

## Regler

- [RULE-APR-029-001](../rules/rule-apr-029-001.md) — Registreringshandling
- [RULE-APR-029-002](../rules/rule-apr-029-002.md) — Sökandehandling efter inlämnande
- [RULE-APR-029-003](../rules/rule-apr-029-003.md) — Giltighetstid för sökandehandling

---

## Delade aktiviteter

- (se shared/documents)

---

## Diagram

Se huvudflöde ovan.
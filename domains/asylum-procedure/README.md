<div align="right">← <a href="../../README.md">Kunskapsbasen</a></div>

# Asylum Procedure

## Syfte

Domänen beskriver det reguljära förfarandet för prövning av ansökningar om internationellt skydd enligt Asylum Procedure Regulation (APR).

Förfarandet inleds efter att ansökan har registrerats och lämnats in, och avslutas med ett beslut om ansökan.

---

## Plats i livscykeln

| | |
|---|---|
| **Föregående** | [Responsibility](../responsibility/README.md) (ansvarig stat fastställd) |
| **Nästa** | Beslut: uppehållstillstånd eller återvändande |
| **Inträde** | Ansökan inlämnad i den ansvariga staten |
| **Utträde** | Beslut fattat (beviljande, avslag eller återkallande) |

---

## Primära rättskällor

- [APR artikel 34](articles/apr-034.md) — Prövning av ansökningar
- [APR artikel 35](articles/apr-035.md) — Prövningsförfarandets varaktighet
- [APR artikel 36](articles/apr-036.md) — Beslut om ansökningar
- [APR artikel 37](articles/apr-037.md) — Avslag och beslut om återvändande
- [APR artikel 38](articles/apr-038.md) — Beslut om upptagande till prövning
- [APR artikel 39](articles/apr-039.md) — Beslut efter prövning i sak
- [APR artikel 40](articles/apr-040.md) — Uttryckligt återkallande
- [APR artikel 41](articles/apr-041.md) — Implicit återkallande
- [APR artikel 42](articles/apr-042.md) — Påskyndat prövningsförfarande

---

## Processer

| Process | Beskrivning |
|---------|-------------|
| [PROC-ASY-001 Examine an application](processes/examine-an-application.md) | Från inlämnad ansökan till beslut |
| [PROC-ASY-002 Subsequent application](processes/subsequent-application.md) | Hantering av efterföljande ansökan |

---

## Juridiska milstolpar

```text
Application lodged
        │
        ▼
Examination begins
        │
        ├── Admissibility check (art. 38)
        │       ├── Inadmissible → Rejection
        │       └── Admissible → Examination on the merits
        │
        ├── Personal interview (art. 11–14)
        │
        ▼
Decision on the merits (art. 39)
        │
        ├── Granted (refugee status or subsidiary protection)
        ├── Rejected → Return decision (art. 37)
        └── Withdrawn (explicit art. 40 / implicit art. 41)
```

---

## Begrepp

| ID | Begrepp |
|----|---------|
| [CON-ASY-001](concepts/determining-authority.md) | Determining authority |
| [CON-ASY-002](concepts/admissibility.md) | Admissibility |
| [CON-ASY-003](concepts/examination-on-the-merits.md) | Examination on the merits |
| [CON-ASY-004](concepts/accelerated-procedure.md) | Accelerated procedure |
| [CON-ASY-005](concepts/subsequent-application.md) | Subsequent application |

---

## Regler

### APR artikel 34 — Prövning

| Regel | Beskrivning |
|-------|-------------|
| [RULE-APR-034-001](rules/rule-apr-034-001.md) | Skyldighet att pröva ansökan individuellt, objektivt och opartiskt |
| [RULE-APR-034-002](rules/rule-apr-034-002.md) | Prövning mot både flyktingstatus och subsidiärt skydd |

### APR artikel 35 — Tidsfrister

| Regel | Beskrivning |
|-------|-------------|
| [RULE-APR-035-001](rules/rule-apr-035-001.md) | Prövningstidsfrist — sex månader |
| [RULE-APR-035-002](rules/rule-apr-035-002.md) | Förlängning vid komplexa ärenden — upp till 15 månader |

### APR artikel 38 — Upptagande till prövning

| Regel | Beskrivning |
|-------|-------------|
| [RULE-APR-038-001](rules/rule-apr-038-001.md) | Grunder för att avvisa en ansökan |

### APR artikel 42 — Påskyndat förfarande

| Regel | Beskrivning |
|-------|-------------|
| [RULE-APR-042-001](rules/rule-apr-042-001.md) | Grunder för påskyndat prövningsförfarande |
| [RULE-APR-042-002](rules/rule-apr-042-002.md) | Tidsfrist vid påskyndat — tre månader |

---

## Tolkningar

| Fil | Frågeställning |
|-----|----------------|
| [admissibility-vs-merits](interpretations/admissibility-vs-merits.md) | Skillnaden mellan upptagandeprövning och prövning i sak |

---

## Öppna frågor

| Fil | Fråga |
|-----|-------|
| [implicit-withdrawal-consequences](open_questions/implicit-withdrawal-consequences.md) | Vad händer vid implicit återkallande? |

---

## Shared capabilities

| Modul | Länk |
|-------|------|
| Interpreters | [shared/interpreters](../../shared/interpreters/README.md) |
| Identity | [shared/identity](../../shared/identity/README.md) |
| Time limits | [shared/time-limits](../../shared/time-limits/README.md) |
| Children | [shared/children](../../shared/children/README.md) |
| Vulnerable persons | [shared/vulnerable-persons](../../shared/vulnerable-persons/README.md) |
| Interviews | [shared/interviews](../../shared/interviews/) |

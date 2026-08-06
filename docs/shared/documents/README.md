# Delat — Dokument

## Syfte

Denna shared-modul dokumenterar handlingar som utfärdas till sökande under förfarandet för internationellt skydd.

Handlingarna fyller flera funktioner: de bekräftar att en person befinner sig i ett pågående förfarande, ger rätt att stanna på territoriet och möjliggör tillgång till mottagandevillkor.

---

## Primära rättskällor

- [APR artikel 29](../../domains/registration/articles/apr-029.md) — Handlingar som tillhandahålls sökanden
- [APR artikel 29.1](../../domains/registration/articles/apr-029.md) — Registreringshandling (utfärdas vid registrering)
- [APR artikel 29.2–5](../../domains/registration/articles/apr-029.md) — Sökandehandling (utfärdas vid inlämnande)
- [APR artikel 29.6](../../domains/registration/articles/apr-029.md) — Handlingar för medföljande barn

---

## Begrepp

| Begrepp | ID | Beskrivning |
|---------|-----|-------------|
| Registreringshandling | [CON-REG-006](../../domains/registration/concepts/registration-certificate.md) | Handling som bekräftar att ansökan registrerats; utfärdas i sökandens namn |
| Sökandehandling | [CON-REG-007](../../domains/registration/concepts/applicant-document.md) | Handling som styrker sökandens rätt att stanna; giltig 12 månader |

---

## Regler

| Regel | Beskrivning |
|-------|-------------|
| [RULE-APR-029-001](../../domains/registration/rules/rule-apr-029-001.md) | Skyldighet att tillhandahålla registreringshandling |
| [RULE-APR-029-002](../../domains/registration/rules/rule-apr-029-002.md) | Skyldighet att utfärda sökandehandling |
| [RULE-APR-029-003](../../domains/registration/rules/rule-apr-029-003.md) | Giltighetstid för sökandehandling (12 månader, förlängningsbar) |

---

## Handlingarnas livscykel

```text
Ansökan registreras
        │
        ▼
Registreringshandling utfärdas (art. 29.1)
        │  Bekräftar registrering
        │  Anger registreringsmyndighet och datum
        │
        ▼
Ansökan lämnas in
        │
        ▼
Sökandehandling utfärdas (art. 29.2)
        │  Styrker rätten att stanna
        │  Giltig 12 månader
        │  Förnyas vid behov
        │
        ▼
Beslut fattas
        │
        ├── Beviljat → uppehållstillstånd ersätter handlingen
        └── Avslag → handlingen upphör att gälla
```

---

## Innehåll i handlingarna

### Registreringshandling (art. 29.1)

- Sökandens namn och fotografi
- Datum och plats för registrering
- Registreringsmyndighetens namn
- Uppgift om att ansökan registrerats

### Sökandehandling (art. 29.2–5)

- Sökandens namn, födelsedatum, nationalitet och fotografi
- Utfärdandedatum och giltighetstid
- Uppgift om att sökanden har rätt att stanna
- Uppgift om vilken medlemsstat som prövar ansökan
- Uppgift om tillgång till arbetsmarknaden (om tillämpligt)

### Medföljande barn (art. 29.6)

- Barn ska namnges i förälderns handlingar
- Separata handlingar kan utfärdas om barnet separeras

---

## Koppling till andra moduler

- [Identitet](../identity/README.md) — Handlingarna styrker identitet
- [Tidsfrister](../time-limits/README.md) — Sökandehandlingens giltighetstid (12 mån)
- [Barn](../children/README.md) — Särskilda bestämmelser för barns handlingar

---

## Används av

- [PROC-REG-001 Registrering av en ansökan](../../domains/registration/processes/registration-of-an-application.md)
- [PROC-REG-002 Ingivande av en ansökan](../../domains/registration/processes/lodging-an-application.md)
- [PROC-REG-003 Utfärda sökandehandlingar](../../domains/registration/processes/issue-applicant-documents.md)

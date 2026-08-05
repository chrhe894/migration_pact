
# Eurodac

## Syfte

Domänen beskriver Eurodacförordningen (EU) 2024/1358, med fokus på insamling, överföring, registrering och lagring av biometriska uppgifter som är relevanta för screening, registrering av asylansökan och personer som vistas olagligt inom territoriet.

Eurodac är ett informationssystem för jämförelse av biometriska uppgifter och andra personuppgifter. Systemet används bland annat för att stödja tillämpningen av asyl- och migrationshanteringsreglerna.

---

## Plats i livscykeln

| | |
|---|---|
| **Föregående** | [Screening](../screening/README.md) / [Registration](../registration/README.md) |
| **Nästa** | [Responsibility](../responsibility/README.md) (Eurodac-träff kan utlösa ansvarsförfarande) |
| **Inträde** | Biometriska uppgifter ska tas (screening eller registrering) |
| **Utträde** | Dataset registrerat i Eurodac, tillgängligt för jämförelse |

---

## Primära rättskällor

- [Eurodac artikel 1](articles/eur-001.md) — Syfte och tillämpningsområde
- [Eurodac artikel 2](articles/eur-002.md) — Definitioner
- [Eurodac artikel 13](articles/eur-013.md) — Skyldighet att ta biometriska uppgifter
- [Eurodac artikel 14](articles/eur-014.md) — Särskilda bestämmelser rörande underåriga
- [Eurodac artikel 15](articles/eur-015.md) — Insamling och överföring för asylsökande
- [Eurodac artikel 17](articles/eur-017.md) — Registrering av uppgifter
- [Eurodac artikel 18](articles/eur-018.md) — Sök- och räddningsinsatser
- [Eurodac artikel 19](articles/eur-019.md) — Omplacerade personer
- [Eurodac artikel 20](articles/eur-020.md) — Vidarebosatta personer
- [Eurodac artikel 21](articles/eur-021.md) — Irreguljär gränspassage
- [Eurodac artikel 22](articles/eur-022.md) — Återkallat uppehållstillstånd
- [Eurodac artikel 23](articles/eur-023.md) — Olaglig vistelse
- [Eurodac artikel 24](articles/eur-024.md) — Märkning vid skyddsbeslut
- [Eurodac artikel 25](articles/eur-025.md) — Avmärkning
- [Eurodac artikel 26](articles/eur-026.md) — Statusuppgifter
- [Eurodac artikel 29](articles/eur-029.md) — Lagring av uppgifter
- [Eurodac artikel 30](articles/eur-030.md) — Radering i förtid
- [Eurodac artikel 31](articles/eur-031.md) — Jämförelse
- [Eurodac artikel 32](articles/eur-032.md) — Brottsbekämpande åtkomst
- [Eurodac artikel 33](articles/eur-033.md) — Europols åtkomst
- [Eurodac artikel 34](articles/eur-034.md) — Kommunikation
- [Eurodac artikel 35](articles/eur-035.md) — Loggning
- [Eurodac artikel 36](articles/eur-036.md) — Ansvar för uppgiftsbehandling
- [Eurodac artikel 37](articles/eur-037.md) — Överföring till tredjeland
- [Eurodac artikel 38](articles/eur-038.md) — Uppgiftskvalitet
- [Eurodac artikel 39](articles/eur-039.md) — Datasäkerhet
- [Eurodac artikel 40](articles/eur-040.md) — Förbud mot obehörig behandling
- [Eurodac artikel 41](articles/eur-041.md) — Skadeståndsansvar
- [Eurodac artikel 42](articles/eur-042.md) — Information till registrerade

---

## Processer

| Process | Beskrivning |
|---------|-------------|
| [PROC-EUR-001 Collect and transmit biometric data](processes/collect-and-transmit-biometric-data.md) | Från att biometriska uppgifter ska tas till att dataset överförs till Eurodac |

---

## Juridiska milstolpar

```text
Person omfattas av Eurodac-kategori
        │
        ▼
Biometriska uppgifter tas
        │
        ▼
Dataset överförs till Eurodac
        │
        ▼
Uppgifter registreras
        │
        ▼
Uppgifter lagras enligt tillämplig kategori
```

---

## Begrepp

| ID | Begrepp |
|----|---------|
| [CON-EUR-001](concepts/eurodac.md) | Eurodac |
| [CON-EUR-002](concepts/biometric-data.md) | Biometric data |
| [CON-EUR-003](concepts/fingerprint-data.md) | Fingerprint data |
| [CON-EUR-004](concepts/facial-image-data.md) | Facial image data |
| [CON-EUR-005](concepts/dataset.md) | Dataset |
| [CON-EUR-006](concepts/originating-member-state.md) | Originating Member State |

---

## Regler

### Eurodac artikel 13 — Skyldighet att ta biometriska uppgifter

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-013-001](rules/rule-eur-013-001.md) | Skyldighet att ta och lämna biometriska uppgifter |
| [RULE-EUR-013-002](rules/rule-eur-013-002.md) | Respekt för värdighet och fysisk integritet |

### Eurodac artikel 14 — Underåriga

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-014-001](rules/rule-eur-014-001.md) | Biometriska uppgifter för underåriga från sex års ålder |

### Eurodac artikel 15 — Personer som ansöker om internationellt skydd

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-015-001](rules/rule-eur-015-001.md) | Insamling och överföring för asylsökande |

### Eurodac artikel 18 — Sök- och räddningsinsatser

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-018-001](rules/rule-eur-018-001.md) | Tidsfrist för biometrisk insamling vid landsättning (72 timmar) |

### Eurodac artikel 19 — Omplacerade personer

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-019-001](rules/rule-eur-019-001.md) | Biometrisk registrering vid omplacering |

### Eurodac artikel 20 — Vidarebosatta eller mottagna personer

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-020-001](rules/rule-eur-020-001.md) | Biometrisk registrering vid vidarebosättning |

### Eurodac artikel 21 — Irreguljär gränspassage

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-021-001](rules/rule-eur-021-001.md) | Biometrisk registrering vid irreguljär gränspassage |

### Eurodac artikel 22 — Återkallat uppehållstillstånd

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-022-001](rules/rule-eur-022-001.md) | Biometrisk registrering vid återkallat uppehållstillstånd |

### Eurodac artikel 23 — Personer som vistas olagligt

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-023-001](rules/rule-eur-023-001.md) | Insamling och överföring för personer som vistas olagligt |

### Eurodac artikel 24 — Märkning vid skyddsbeslut

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-024-001](rules/rule-eur-024-001.md) | Skyldighet att märka uppgifter vid skyddsbeslut |

### Eurodac artikel 25 — Avmärkning

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-025-001](rules/rule-eur-025-001.md) | Skyldighet att avmärka vid återkallat skydd |

### Eurodac artikel 26 — Statusuppgifter

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-026-001](rules/rule-eur-026-001.md) | Skyldighet att registrera statusuppgifter |

### Eurodac artikel 29 — Lagring

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-029-001](rules/rule-eur-029-001.md) | Lagringstid för asylsökande |
| [RULE-EUR-029-002](rules/rule-eur-029-002.md) | Lagringstid för personer som vistas olagligt |

### Eurodac artikel 30 — Radering i förtid

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-030-001](rules/rule-eur-030-001.md) | Radering vid medborgarskap eller uppehållstillstånd |
| [RULE-EUR-030-002](rules/rule-eur-030-002.md) | Ursprungsmedlemsstatens raderingsskyldighet |

### Eurodac artikel 31 — Jämförelse

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-031-001](rules/rule-eur-031-001.md) | Automatisk jämförelse vid överföring |

### Eurodac artikel 32 — Brottsbekämpande åtkomst

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-032-001](rules/rule-eur-032-001.md) | Villkor för brottsbekämpande åtkomst |
| [RULE-EUR-032-002](rules/rule-eur-032-002.md) | Subsidiaritetskrav (nationella databaser först) |

### Eurodac artikel 33 — Europols åtkomst

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-033-001](rules/rule-eur-033-001.md) | Europols villkor för åtkomst |

### Eurodac artikel 34 — Kommunikation

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-034-001](rules/rule-eur-034-001.md) | Nationella åtkomstpunkter som enda kanal |

### Eurodac artikel 35 — Loggning

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-035-001](rules/rule-eur-035-001.md) | Loggningsskyldighet för all åtkomst |
| [RULE-EUR-035-002](rules/rule-eur-035-002.md) | Lagringstid för loggar (minst fem år) |

### Eurodac artikel 36 — Ansvar för uppgiftsbehandling

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-036-001](rules/rule-eur-036-001.md) | Ansvarsfördelning personuppgiftsansvarig/biträde |

### Eurodac artikel 37 — Överföring till tredjeland

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-037-001](rules/rule-eur-037-001.md) | Förbud mot överföring till tredjeland |

### Eurodac artikel 38 — Uppgiftskvalitet

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-038-001](rules/rule-eur-038-001.md) | Kvalitetskrav för biometriska uppgifter |
| [RULE-EUR-038-002](rules/rule-eur-038-002.md) | Skyldighet att åtgärda avvisade dataset |

### Eurodac artikel 39 — Datasäkerhet

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-039-001](rules/rule-eur-039-001.md) | Krav på tekniska och organisatoriska säkerhetsåtgärder |

### Eurodac artikel 40 — Förbud mot obehörig behandling

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-040-001](rules/rule-eur-040-001.md) | Ändamålsbegränsning |

### Eurodac artikel 41 — Skadeståndsansvar

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-041-001](rules/rule-eur-041-001.md) | Rätt till ersättning vid olaglig behandling |

### Eurodac artikel 42 — Information till registrerade

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-042-001](rules/rule-eur-042-001.md) | Informationsplikt gentemot registrerade |
| [RULE-EUR-042-002](rules/rule-eur-042-002.md) | Information ska ges på begripligt språk |

---

## Tolkningar

| Fil | Frågeställning |
|-----|----------------|
| [eurodac-in-screening-and-registration](interpretations/eurodac-in-screening-and-registration.md) | Hur förhåller sig Eurodac till screening och registrering? |

---

## Öppna frågor

| Fil | Fråga |
|-----|-------|
| [scope-of-next-eurodac-slice](open_questions/scope-of-next-eurodac-slice.md) | Vilken Eurodac-kategori bör dokumenteras efter screening- och registreringsspåret? |

---

## Delade moduler

| Modul | Länk |
|-------|------|
| Biometrics | [shared/biometrics](../../shared/biometrics/README.md) |
| Identity | [shared/identity](../../shared/identity/README.md) |
| Children | [shared/children](../../shared/children/README.md) |

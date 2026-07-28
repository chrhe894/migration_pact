<div align="right">← <a href="../../README.md">Kunskapsbasen</a></div>

# Eurodac

## Syfte

Domänen beskriver Eurodacförordningen (EU) 2024/1358, med fokus på insamling, överföring, registrering och lagring av biometriska uppgifter som är relevanta för screening, registrering av asylansökan och personer som vistas olagligt inom territoriet.

Eurodac är ett informationssystem för jämförelse av biometriska uppgifter och andra personuppgifter. Systemet används bland annat för att stödja tillämpningen av asyl- och migrationshanteringsreglerna.

---

## Primära rättskällor

- [Eurodac artikel 13](articles/eur-013.md) — Skyldighet att ta biometriska uppgifter
- [Eurodac artikel 14](articles/eur-014.md) — Särskilda bestämmelser rörande underåriga
- [Eurodac artikel 15](articles/eur-015.md) — Insamling och överföring av biometriska uppgifter för personer som ansöker om internationellt skydd
- [Eurodac artikel 17](articles/eur-017.md) — Registrering av uppgifter
- [Eurodac artikel 23](articles/eur-023.md) — Insamling och överföring av biometriska uppgifter för personer som vistas olagligt
- [Eurodac artikel 29](articles/eur-029.md) — Lagring av uppgifter

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

### Eurodac artikel 23 — Personer som vistas olagligt

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-023-001](rules/rule-eur-023-001.md) | Insamling och överföring för personer som vistas olagligt |

### Eurodac artikel 29 — Lagring

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-029-001](rules/rule-eur-029-001.md) | Lagringstid för asylsökande |
| [RULE-EUR-029-002](rules/rule-eur-029-002.md) | Lagringstid för personer som vistas olagligt |

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

## Shared capabilities

| Modul | Länk |
|-------|------|
| Biometrics | [shared/biometrics](../../shared/biometrics/README.md) |
| Identity | [shared/identity](../../shared/identity/README.md) |
| Children | [shared/children](../../shared/children/README.md) |

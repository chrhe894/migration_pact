
# Eurodac

## Syfte

Domänen beskriver Eurodacförordningen (EU) 2024/1358, med fokus på insamling, överföring, registrering och lagring av biometriska uppgifter som är relevanta för screening, registrering av asylansökan och personer som vistas olagligt inom territoriet.

Eurodac är ett informationssystem för jämförelse av biometriska uppgifter och andra personuppgifter. Systemet används bland annat för att stödja tillämpningen av asyl- och migrationshanteringsreglerna.

---

## Plats i livscykeln

| | |
|---|---|
| **Föregående** | [Screening](../screening/README.md) / [Registrering](../registration/README.md) |
| **Nästa** | [Ansvar](../responsibility/README.md) (Eurodac-träff kan utlösa ansvarsförfarande) |
| **Inträde** | Biometriska uppgifter ska tas (screening eller registrering) |
| **Utträde** | Dataset registrerat i Eurodac, tillgängligt för jämförelse |

---

## Primära rättskällor

| Artikel | Rubrik | Kapitel |
|---------|--------|---------|
| [1](articles/eur-001.md) | Syftet med Eurodac | I Allmänna bestämmelser |
| [2](articles/eur-002.md) | Definitioner | I |
| [13](articles/eur-013.md) | Skyldighet att ta biometriska uppgifter | I |
| [14](articles/eur-014.md) | Särskilda bestämmelser rörande underåriga | I |
| [15](articles/eur-015.md) | Insamling och överföring — sökande av internationellt skydd | II |
| [16](articles/eur-016.md) | Information om den registrerades status (ansvarig MS, ankomst, utresa) | II |
| [17](articles/eur-017.md) | Registrering av uppgifter — sökande (inkl. säkerhetsflaggning 17.2 i) | II |
| [18](articles/eur-018.md) | Insamling och överföring — inreseförfarande enligt unionsramen för vidarebosättning | III avsnitt 1 |
| [19](articles/eur-019.md) | Registrering av uppgifter — unionsramen | III avsnitt 1 |
| [20](articles/eur-020.md) | Insamling och överföring — nationellt vidarebosättningsprogram | III avsnitt 2 |
| [21](articles/eur-021.md) | Registrering av uppgifter — nationellt program | III avsnitt 2 |
| [22](articles/eur-022.md) | Insamling och överföring — irreguljär passage av yttre gräns | IV |
| [23](articles/eur-023.md) | Insamling och överföring — olaglig vistelse | V |
| [24](articles/eur-024.md) | Insamling och överföring — landsättning efter sök och räddning | VI |
| [25](articles/eur-025.md) | Information om omfördelningsstatus | VII |
| [26](articles/eur-026.md) | Insamling och överföring — tillfälligt skydd | VIII |
| [27](articles/eur-027.md) | Jämförelse av biometriska uppgifter | IX |
| [28](articles/eur-028.md) | Jämförelse av uppgifter om ansiktsbild | IX |
| [29](articles/eur-029.md) | Lagring av uppgifter | X |
| [30](articles/eur-030.md) | Radering av uppgifter i förtid (medborgarskap) | X |
| [31](articles/eur-031.md) | Markering av uppgifter (skydd, uppehållstillstånd) | X |
| [32](articles/eur-032.md) | Förfarande för jämförelse — brottsbekämpning | XI |
| [33](articles/eur-033.md) | Villkor för utsedda myndigheters åtkomst | XI |
| [34](articles/eur-034.md) | Villkor för Europols åtkomst | XI |
| [35](articles/eur-035.md) | Kommunikation inom brottsbekämpande förfarande | XI |
| [36](articles/eur-036.md) | Ansvar i frågor som rör uppgiftsbehandling | XII |
| [37](articles/eur-037.md) | Överföring (dataformat, referensnummer) | XII |
| [38](articles/eur-038.md) | Genomförande av jämförelser och överföring av resultat | XII |
| [39](articles/eur-039.md) | Kommunikation mellan medlemsstaterna och Eurodac | XII |
| [40](articles/eur-040.md) | Åtkomst till och rättelse eller radering av uppgifter | XII |
| [41](articles/eur-041.md) | Register | XII |
| [42](articles/eur-042.md) | Rätt till information | XII |

Artiklar utan eget kort (3–12, 43–63, bland annat datasäkerhet art. 48, tredjeland art. 49–50 och skadestånd art. 52) finns i [referenskortet för Eurodacförordningen](../../references/legislation/eurodac.md).

> **Rättelse (granskning 2026-09):** flera artikelkort och regler i domänen var numrerade fel och beskrev en annan artikel än filnamnet. Ett par innehöll också uppgifter som inte står i förordningen. Alla kort och regler är nu kontrollerade mot förordningstexten. Där innehållet ändrats finns en rättelsenot på respektive sida.

---

## Processer

| Process | Beskrivning |
|---------|-------------|
| [PROC-EUR-001 Samla in och överföra biometriska uppgifter](processes/collect-and-transmit-biometric-data.md) | Från att biometriska uppgifter ska tas till att dataset överförs till Eurodac |

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
| [CON-EUR-002](concepts/biometric-data.md) | Biometriska uppgifter |
| [CON-EUR-003](concepts/fingerprint-data.md) | Fingeravtryck |
| [CON-EUR-004](concepts/facial-image-data.md) | Ansiktsbild |
| [CON-EUR-005](concepts/dataset.md) | Dataset |
| [CON-EUR-006](concepts/originating-member-state.md) | Originating Member State |

---

## Regler

| Artikel | Regel | Beskrivning |
|---------|-------|-------------|
| 13 | [RULE-EUR-013-001](rules/rule-eur-013-001.md) | Skyldighet att ta och lämna biometriska uppgifter |
| 13 | [RULE-EUR-013-002](rules/rule-eur-013-002.md) | Respekt för värdighet och fysisk integritet |
| 14 | [RULE-EUR-014-001](rules/rule-eur-014-001.md) | Biometriska uppgifter för underåriga från sex års ålder |
| 15 | [RULE-EUR-015-001](rules/rule-eur-015-001.md) | Insamling och överföring för sökande (72 timmar) |
| 16 | [RULE-EUR-016-001](rules/rule-eur-016-001.md) | Uppdatering av ansvarig medlemsstat, ankomst och utresa |
| 18 | [RULE-EUR-018-001](rules/rule-eur-018-001.md) | Biometri vid inreseförfarande enligt unionsramen |
| 19 | [RULE-EUR-019-001](rules/rule-eur-019-001.md) | Registrerade uppgifter — unionsramen |
| 20 | [RULE-EUR-020-001](rules/rule-eur-020-001.md) | Biometri vid nationellt vidarebosättningsprogram (72 timmar) |
| 21 | [RULE-EUR-021-001](rules/rule-eur-021-001.md) | Registrerade uppgifter — nationellt program |
| 22 | [RULE-EUR-022-001](rules/rule-eur-022-001.md) | Biometri vid irreguljär gränspassage (72 timmar) |
| 23 | [RULE-EUR-023-001](rules/rule-eur-023-001.md) | Biometri vid olaglig vistelse (72 timmar) |
| 24 | [RULE-EUR-024-001](rules/rule-eur-024-001.md) | Biometri vid landsättning efter sök och räddning (72 timmar) |
| 25 | [RULE-EUR-025-001](rules/rule-eur-025-001.md) | Uppdatering av dataset vid omfördelning |
| 26 | [RULE-EUR-026-001](rules/rule-eur-026-001.md) | Biometri vid tillfälligt skydd (tio dagar) |
| 27 | [RULE-EUR-027-001](rules/rule-eur-027-001.md) | Automatisk jämförelse och överföring av resultat |
| 29 | [RULE-EUR-029-001](rules/rule-eur-029-001.md) | Lagringstid för sökande (tio år) |
| 29 | [RULE-EUR-029-002](rules/rule-eur-029-002.md) | Lagringstid vid olaglig vistelse (fem år) |
| 30 | [RULE-EUR-030-001](rules/rule-eur-030-001.md) | Radering i förtid vid medborgarskap |
| 30 | [RULE-EUR-030-002](rules/rule-eur-030-002.md) | Underrättelse inom 72 timmar efter radering |
| 31 | [RULE-EUR-031-001](rules/rule-eur-031-001.md) | Markering vid internationellt skydd och avmarkering vid återkallelse |
| 31 | [RULE-EUR-031-002](rules/rule-eur-031-002.md) | Markering vid uppehållstillstånd |
| 32 | [RULE-EUR-032-001](rules/rule-eur-032-001.md) | Kontrollmyndighetens förhandskontroll av framställan |
| 32 | [RULE-EUR-032-002](rules/rule-eur-032-002.md) | Brådskande undantagsfall och efterhandskontroll |
| 33 | [RULE-EUR-033-001](rules/rule-eur-033-001.md) | Kumulativa villkor för utsedda myndigheters åtkomst |
| 34 | [RULE-EUR-034-001](rules/rule-eur-034-001.md) | Villkor för Europols åtkomst och ursprungsmedlemsstatens tillstånd |
| 35 | [RULE-EUR-035-001](rules/rule-eur-035-001.md) | Säkrad elektronisk kommunikation |
| 35 | [RULE-EUR-035-002](rules/rule-eur-035-002.md) | Digital behandling i fastställt dataformat |
| 36 | [RULE-EUR-036-001](rules/rule-eur-036-001.md) | Ursprungsmedlemsstatens och eu-LISA:s ansvar |
| 37 | [RULE-EUR-037-001](rules/rule-eur-037-001.md) | Elektronisk överföring och entydigt referensnummer |
| 38 | [RULE-EUR-038-001](rules/rule-eur-038-001.md) | Adekvat kvalitet och ny överföring |
| 38 | [RULE-EUR-038-002](rules/rule-eur-038-002.md) | Behandlingstid (24 h / 1 h) och kontroll av träffar |
| 39 | [RULE-EUR-039-001](rules/rule-eur-039-001.md) | Användning av kommunikationsinfrastrukturen |
| 40 | [RULE-EUR-040-001](rules/rule-eur-040-001.md) | Endast ursprungsmedlemsstaten får ändra eller radera |
| 41 | [RULE-EUR-041-001](rules/rule-eur-041-001.md) | Register över uppgiftsbehandling och dess lagringstid |
| 42 | [RULE-EUR-042-001](rules/rule-eur-042-001.md) | Informationsplikt gentemot registrerade |
| 42 | [RULE-EUR-042-002](rules/rule-eur-042-002.md) | Information på begripligt språk |

> **Ändrade regel-ID:** flera regler har fått nytt innehåll så att numret följer den verkliga artikeln. 72-timmarsregeln för sök och räddning är nu **RULE-EUR-024-001** (tidigare 018-001). Märkning och avmärkning vid skydd är nu **RULE-EUR-031-001** (tidigare 024-001 och 025-001). Varje berörd regel har en not om vad den tidigare avsåg.

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

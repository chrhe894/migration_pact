# Kunskapsbas för EU:s migrations- och asylpakt

## Om projektet

Detta repository innehåller en kunskapsbas för EU:s migrations- och asylpakt.

Syftet är att strukturera och dokumentera innehållet i EU:s rättsakter på ett sätt som är spårbart, konsekvent och lätt att underhålla.

Projektet bygger på principen att varje uppgift ska kunna härledas till sin rättsliga källa eller tydligt identifieras som en tolkning eller en öppen fråga.

Projektet är under aktiv utveckling och byggs stegvis.

---

## Syfte

Projektet har följande mål:

- beskriva EU:s migrations- och asylpakt på ett strukturerat sätt,
- säkerställa att varje regel kan spåras till sin rättsliga källa,
- skilja mellan lagtext, tolkningar och öppna frågor,
- dokumentera processer och samband mellan regler,
- skapa en långsiktigt hållbar kunskapsbas.

---

## Omfattning

Projektet omfattar främst:

- EU-förordningar,
- EU-direktiv när de är relevanta,
- bilagor,
- skäl (recitals),
- officiell vägledning från EU:s institutioner när den kompletterar lagstiftningen.

Projektet omfattar inte:

- nationell lagstiftning,
- nationell tillämpning,
- myndigheters interna rutiner,
- juridisk rådgivning.

---

## Grundprinciper

### EU-rätten är den primära källan

Alla påståenden ska kunna härledas till en rättslig källa eller tydligt anges som en tolkning.

### Spårbarhet

Varje regel ska kunna följas tillbaka till relevant artikel, skäl, bilaga eller annan rättskälla.

### En regel dokumenteras en gång

En rättsregel dokumenteras endast en gång och återanvänds därefter genom referenser.

### Diagram beskriver struktur

PlantUML används för att visualisera processer, flöden och relationer.

Diagram innehåller inte den rättsliga innebörden utan fungerar som ett komplement till dokumentationen.

### Modulär dokumentation

Repositoryt består av många mindre dokument istället för ett fåtal stora dokument. Det gör innehållet enklare att underhålla, granska och återanvända.

---

## Repositorystruktur

| Mapp          | Innehåll                               |
| ---------------| ----------------------------------------|
| `domains/`    | Domäner per förordning och förfarande  |
| `shared/`     | Delade begrepp, regler och aktiviteter |
| `references/` | Lagstiftningsreferenser och källtexter |
| `templates/`  | Mallar för projektets dokument         |
| `diagrams/`   | Övergripande diagram                   |

**Nyläsare?** Börja med [CASE_LIFECYCLE.md](CASE_LIFECYCLE.md) för en överblick av hela förfarandekedjan.

Se även:
- [FAQ — Vanliga frågor](FAQ.md)
- [Ordlista (Glossary)](GLOSSARY.md)
- [Scenarios — konkreta exempel](scenarios/README.md)
- [Dublin III vs AMMR — vad har ändrats?](DUBLIN_VS_AMMR.md)

---

## Domäner

| Domän                                                                | Förordning                 | Status |
| ----------------------------------------------------------------------| ----------------------------| --------|
| [Registrering](domains/registration/README.md)                       | APR                        | Klar   |
| [Asylförfarande](domains/asylum-procedure/README.md)                 | APR                        | Klar   |
| [Gränsförfarande](domains/border-procedure/README.md)                | APR                        | Klar   |
| [Screening](domains/screening/README.md)                             | Screeningförordningen      | Klar   |
| [Eurodac](domains/eurodac/README.md)                                 | Eurodacförordningen        | Klar   |
| [Ansvar](domains/responsibility/README.md)                           | AMMR                       | Klar   |
| [Solidaritet](domains/solidarity/README.md)                          | AMMR                       | Klar   |
| [Kris](domains/crisis/README.md)                                     | Krishanteringsförordningen | Klar   |
| [Återvändande vid gräns](domains/return-border-procedure/README.md)  | Återvändandeförordningen   | Klar   |

---

## Delade moduler

| Modul | Innehåll |
|-------|----------|
| [Identitet](shared/identity/README.md) | Identitetsfastställande |
| [Tolkar](shared/interpreters/README.md) | Tolktjänster |
| [Dokument](shared/documents/README.md) | Handlingar till sökanden |
| [Tidsfrister](shared/time-limits/README.md) | Tidsfrister |
| [Barn](shared/children/) | Särskilda garantier för barn |
| [Sårbara personer](shared/vulnerable-persons/README.md) | Sårbara personer |
| [Biometri](shared/biometrics/) | Biometriska uppgifter |
| [Säkerhetskontroller](shared/security-checks/) | Säkerhetskontroller |
| [Intervjuer](shared/interviews/README.md) | Personliga intervjuer |
| [Statistik](shared/statistics/README.md) | Datapunkter och beräkningar |

---

## Språk

Repositoryts tekniska struktur använder engelska.

Det gäller exempelvis:

- katalognamn,
- filnamn,
- mallar.

Projektets innehåll skrivs på svenska.

Det gäller bland annat:

- dokumentation,
- analyser,
- kommentarer,
- diagram.

---

## Arbetssätt

Projektet utvecklas stegvis.

Varje område färdigställs innan nästa påbörjas.

För varje område eftersträvas:

- identifierade begrepp,
- dokumenterade regler,
- processbeskrivningar,
- diagram,
- tolkningar,
- öppna frågor,
- full spårbarhet till rättskällorna.

---

## Status

Projektet är under aktiv utveckling.

Repositoryts struktur och innehåll kommer att utvecklas över tid, men de grundläggande principerna om spårbarhet, modularitet och tydliga källhänvisningar ska bestå.

---

## Ansvarsfriskrivning

Detta är ett fristående kunskapsprojekt.

Projektet är inte en officiell publikation från Europeiska unionen eller någon nationell myndighet och ska inte betraktas som juridisk rådgivning eller ett rättsligt bindande dokument.

Den officiella lagstiftningen finns alltid i Europeiska unionens officiella tidning (EUT).

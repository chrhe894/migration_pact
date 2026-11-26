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

Kunskapsbasen utgår från EU-rätten och kompletteras med den svenska rätt som behövs för att förstå hur pakten genomförs och vad den kräver av ett systemstöd.

**EU-rätt (primär källa)**

- paktens förordningar: artiklar, skäl och bilagor,
- genomförandeförordningar och allmänna EU-regler som förordningarna bygger på, till exempel reglerna för beräkning av frister,
- EU-direktiv när de behövs för sammanhanget, till exempel mottagandedirektivet och återvändandedirektivet.

**Svensk rätt och förarbeten**

- nationell lagstiftning som genomför eller kompletterar pakten, till exempel mottagandelagen,
- nationell lagstiftning som styr hur uppgifter får lagras och gallras: arkivlagen, tryckfrihetsförordningen, utlänningsdataförordningen och Riksarkivets föreskrifter,
- förarbeten (departementsskrivelser och propositioner) som beskriver de nationella valen i genomförandet. Förslag som ännu inte är antagna markeras som förslag.

**Systemperspektiv**

- processer, regler, krav och förmågor som härleds ur rättskällorna,
- tvärgående frågor som tidsfrister, flaggor och markeringar, statistik samt gallring och radering,
- tolkningar och öppna frågor, tydligt skilda från lagtexten.

**Omfattas inte**

- myndigheters interna rutiner och handböcker,
- rättspraxis, utom när den uttryckligen anges som källa,
- juridisk rådgivning.

Källorna listas i [Källor](#kallor).

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
| [Återvändande vid gräns](domains/return-border-procedure/README.md)  | Förordning (EU) 2024/1349  | Klar   |
| [Återvändande](domains/return/README.md)                             | Förordning (EU) 2026/2280  | Ny (2026-11). Tillämpas i huvudsak från 17 okt 2027 |

---

## Delade moduler

| Modul | Innehåll |
|-------|----------|
| [Identitet](shared/identity/README.md) | Identitetsfastställande |
| [Tolkar](shared/interpreters/README.md) | Tolktjänster |
| [Dokument](shared/documents/README.md) | Handlingar till sökanden |
| [Tidsfrister](shared/time-limits/README.md) | Tidsfrister |
| [Barn](shared/children/README.md) | Särskilda garantier för barn |
| [Sårbara personer](shared/vulnerable-persons/README.md) | Sårbara personer |
| [Prioritet](shared/priority/README.md) | Vilka ärenden som ska eller får behandlas före andra |
| [Förvar](shared/detention/README.md) | Förvarsgrunder, tidsfrister, prövning och händelsestyrd hantering av beslut |
| [Biometri](shared/biometrics/README.md) | Biometriska uppgifter |
| [Säkerhetskontroller](shared/security-checks/README.md) | Säkerhetskontroller |
| [Personliga intervjuer](shared/interviews/README.md) | Personliga intervjuer och övriga intervjuer |
| [Statistik](shared/statistics/README.md) | Datapunkter och beräkningar |
| [Flaggor och markeringar](shared/flags/README.md) | Villkorsutlösta flaggor, markeringar och varningar |
| [Gallring och radering](shared/data-retention/README.md) | Lagringstider, radering och medborgarskapsundantag |

---

## Källor

Uppgifterna är hämtade ur källtexterna i `references/` och kontrollerade där. Textversionerna för sökning finns i `references/_text/`.

### EU-förordningar

| Förkortning | Rättsakt | Nummer | Antagen | Publicerad (EUT L) | Tillämpas från | Referenskort |
|-------------|----------|--------|---------|--------------------|----------------|--------------|
| APR | Förordning om ett gemensamt förfarande för internationellt skydd i unionen | (EU) 2024/1348 | 14 maj 2024 | 22 maj 2024 | 12 juni 2026 | [APR](references/legislation/apr.md) |
| AMMR | Förordning om asyl- och migrationshantering | (EU) 2024/1351 | 14 maj 2024 | 22 maj 2024 | 1 juli 2026. Vissa artiklar, bl.a. art. 7–15, från 11 juni 2024 (art. 85) | [AMMR](references/legislation/ammr.md) |
| Screening | Förordning om screening av tredjelandsmedborgare vid de yttre gränserna | (EU) 2024/1356 | 14 maj 2024 | 22 maj 2024 | 12 juni 2026 | [Screening](references/legislation/screening.md) |
| Eurodac | Förordning om inrättande av Eurodac | (EU) 2024/1358 | 14 maj 2024 | 22 maj 2024 | 12 juni 2026. Art. 26 (tillfälligt skydd) från 12 juni 2029 | [Eurodac](references/legislation/eurodac.md) |
| Kris | Förordning om krissituationer och force majeure-situationer | (EU) 2024/1359 | 14 maj 2024 | 22 maj 2024 | 1 juli 2026 | [Kris](references/legislation/crisis.md) |
| Return | Förordning om ett gränsförfarande för återvändande | (EU) 2024/1349 | 14 maj 2024 | 22 maj 2024 | 12 juni 2026 | [Return](references/legislation/return-border-procedure.md) |
| Återvändandedirektivet | Direktiv om gemensamma normer och förfaranden för återvändande av tredjelandsmedborgare som vistas olagligt | 2008/115/EG | 16 december 2008 | 24 december 2008 | Gäller till 17 oktober 2027 (förordning 2026/2280 art. 49) | [2008/115](references/legislation/return-directive.md) |
| ETD | Förordning om en europeisk resehandling för återvändande | (EU) 2016/1953 | 26 oktober 2016 | 17 november 2016 | 8 april 2017 (art. 9) | [ETD](references/legislation/european-travel-document.md) |
| 862/2007 | Förordning om gemenskapsstatistik över migration och internationellt skydd, ändrad genom (EU) 2020/851 | (EG) nr 862/2007; ändring (EU) 2020/851 | 11 juli 2007; ändring 18 juni 2020 | — | Asylstatistik enligt ändringen från januari 2021 (art. 4.1) | [Statistikförordningen](references/legislation/eurostat-migration-statistics.md) (endast ändringsförordningen i repot) |
| TRA | Rådets direktiv om bistånd vid transitering i samband med återsändande med flyg | 2003/110/EG | 25 november 2003 | 6 december 2003 | Samma dag som offentliggörandet (art. 12) | [TRA](references/legislation/transit-by-air.md) |
| JRF | Rådets beslut om gemensamma flygningar för återsändande | 2004/573/EG | 29 april 2004 | 6 augusti 2004 | Dagen efter offentliggörandet (art. 8) | [JRF](references/legislation/joint-return-flights.md) |
| Frontex | Förordning om den europeiska gräns- och kustbevakningen | (EU) 2019/1896 | 13 november 2019 | 14 november 2019 | Gäller (grundtexten; senare ändringar ej kontrollerade) | [Frontex](references/legislation/frontex.md) |
| RR | Förordning om ett gemensamt system för återvändande av tredjelandsmedborgare vars vistelse är olaglig | (EU) 2026/2280 | 7 oktober 2026 | 15 oktober 2026 | Delvis 16 oktober 2026; i övrigt 17 oktober 2027 (art. 50). Ersätter direktiv 2008/115/EG från 17 oktober 2027 (art. 49) | [RR](references/legislation/return-regulation.md) |
| AMMR-IMPL | Kommissionens genomförandeförordning om tillämpningsföreskrifter för AMMR | (EU) 2025/2055 | 2 oktober 2025 | 12 november 2025 | 12 juni 2026 | [AMMR-IMPL](references/legislation/ammr-implementing.md) |
| 1182/71 | Rådets förordning om regler för bestämning av perioder, datum och frister | (EEG, Euratom) nr 1182/71 | 3 juni 1971 | — | Gäller | [1182/71](references/legislation/time-limits-regulation.md) (källtexten finns inte i repot) |

### Svensk lagstiftning och föreskrifter

| Författning | Nummer | Utfärdad / beslutad | Ikraft | Lydelse i repot | Referenskort |
|-------------|--------|---------------------|--------|-----------------|--------------|
| Mottagandelag | SFS 2026:999 | 4 juni 2026 | 1 oktober 2026 (paktanpassning SFS 2026:1168: 2 oktober 2026) | t.o.m. SFS 2026:1630 | [Mottagandelagen](references/legislation/mottagandelagen.md) |
| Utlänningslag | SFS 2005:716 | — | — | t.o.m. SFS 2026:1752 | [Utlänningslagen](references/legislation/utlanningslagen.md) |
| Utlänningsdataförordning | SFS 2016:30 | 4 februari 2016 | 12 februari 2016 | t.o.m. SFS 2026:1362 | [Utlänningsdataförordningen](references/legislation/utlanningsdataforordningen.md) |
| Arkivlag | SFS 1990:782 | 7 juni 1990 | 1 juli 1991 | t.o.m. SFS 2026:715 | [Arkivlagstiftning](references/legislation/arkivlagstiftning.md) |
| Tryckfrihetsförordning | SFS 1949:105 | — | — | t.o.m. SFS 2022:1524 | [Arkivlagstiftning](references/legislation/arkivlagstiftning.md) |
| Lag om svenskt medborgarskap | SFS 2001:82 | — | — | t.o.m. SFS 2026:1689 | [Medborgarskapslagen](references/legislation/medborgarskapslagen.md) |
| Riksarkivets föreskrifter om gallring av handlingar och uppgifter inom informationsutbyten mellan myndigheter | RA-FS 2026:1 | Beslutad 31 augusti 2026 | Utkom 18 september 2026 | — | [Arkivlagstiftning](references/legislation/arkivlagstiftning.md) |

"—" betyder att uppgiften inte framgår av källfilen i repot.

### Förarbeten

| Dokument | Nummer | Datum | Status | Sida |
|----------|--------|-------|--------|------|
| Migrations- och asylpakten (volym 1 och 2) | Ds 2025:30 | 2025 | Departementsskrivelse med förslag. Delvis ersatt av antagen lag | [Ds 2025:30](shared/time-limits/national/ds-2025-30.md) |
| Skärpta regler om uppsikt och förvar | Prop. 2025/26:265 | 30 april 2026 | Proposition. Föreslaget ikraftträdande 21 juli 2026, vissa delar 1 oktober 2026 och 1 december 2027 | [Prop. 2025/26:265](shared/time-limits/national/prop-2025-26-265.md) |

### Rättsakter som refereras men inte finns i repot

Uppgifter som bygger på dessa är inte kontrollerade mot källtexten.

| Rättsakt | Nummer | Används för |
|----------|--------|-------------|
| Mottagandedirektivet | (EU) 2024/1346 | Genomförs genom mottagandelagen |
| Skyddsgrundsförordningen | (EU) 2024/1347 | Skyddsgrunder, flyktingbegreppet |
| Direktivet om tillfälligt skydd | 2001/55/EG | Tillfälligt skydd i Eurodac |
| Mottagandeutredningen | SOU 2024:68 | Bakgrund till mottagandelagen |

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

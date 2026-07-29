# Knowledge Base for the EU Migration and Asylum Pact

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

| Mapp | Innehåll |
|------|----------|
| `domains/` | Domäner per förordning och förfarande |
| `shared/` | Delade begrepp, regler och aktiviteter |
| `references/` | Lagstiftningsreferenser och källtexter |
| `templates/` | Mallar för projektets dokument |
| `diagrams/` | Övergripande diagram |

**Nyläsare?** Börja med [CASE_LIFECYCLE.md](CASE_LIFECYCLE.md) för en överblick av hela förfarandekedjan.

---

## Domäner

| Domän | Förordning | Status |
|-------|------------|--------|
| [Registration](domains/registration/README.md) | APR | Pågår |
| [Asylum procedure](domains/asylum-procedure/README.md) | APR | Pågår |
| [Border procedure](domains/border-procedure/README.md) | APR | Pågår |
| [Screening](domains/screening/README.md) | Screeningförordningen | Pågår |
| [Eurodac](domains/eurodac/README.md) | Eurodacförordningen | Pågår |
| [Responsibility](domains/responsibility/README.md) | AMMR | Pågår |
| [Solidarity](domains/solidarity/README.md) | AMMR | Pågår |
| [Crisis](domains/crisis/README.md) | Krishanteringsförordningen | Pågår |
| [Return border procedure](domains/return-border-procedure/README.md) | Return Border Procedure | Pågår |

---

## Shared capabilities

| Modul | Innehåll |
|-------|----------|
| [Identity](shared/identity/README.md) | Identitetsfastställande |
| [Interpreters](shared/interpreters/README.md) | Tolktjänster |
| [Documents](shared/documents/README.md) | Handlingar till sökanden |
| [Time limits](shared/time-limits/README.md) | Tidsfrister |
| [Children](shared/children/) | Särskilda garantier för barn |
| [Vulnerable persons](shared/vulnerable-persons/README.md) | Sårbara personer |
| [Biometrics](shared/biometrics/) | Biometriska uppgifter |
| [Security checks](shared/security-checks/) | Säkerhetskontroller |
| [Interviews](shared/interviews/README.md) | Personliga intervjuer |
| [Statistics](shared/statistics/README.md) | Datapunkter och beräkningar |

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

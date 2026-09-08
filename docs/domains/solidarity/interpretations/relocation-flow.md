---
tags:
  - solidaritet
  - omfördelning
  - tolkning
---


# Tolkning

## Frågeställning

Hur ser hela omfördelningsflödet ut — från att en sökande identifieras i en utsatt stat till att ansvaret övergått till mottagande stat — och hur hänger de olika stegen, tidsfristerna och undantagen ihop?

---

## Analys

Omfördelning (relocation) är den primära formen av solidaritet i AMMR (se [solidarity-types](solidarity-types.md)). Den finns dokumenterad i flera artefakter i den här domänen — koncept, process, regel och artiklarna 67/68 — men de beskriver var sitt fragment. Den här sidan knyter ihop hela kedjan.

<object type="image/svg+xml" data="../diagrams/relocation-flow.svg" width="100%"></object>

Källa: [`relocation-flow.pu`](../diagrams/relocation-flow.pu)

### Steg 1–4: Förfarande inför omfördelning ([art. 67](../articles/ammr-067.md))

Den utsatta staten (förmånsstaten) identifierar sökande som kan omfördelas och meddelar den bidragande staten (omfördelningsmedlemsstaten). Mottagarstaten ska bekräfta mottagande. **Överföringen ska ske inom fyra veckor efter bekräftelsen** ([RULE-AMMR-067-001](../rules/rule-ammr-067-001.md)).

Fyraveckorsfristen är den enda tidsfristen i själva omfördelningsförfarandet och listas i [shared/time-limits](../../shared/time-limits/README.md).

### Säkerhetsundantag

Mottagarstaten kan vägra omfördelning av en specifik person om det finns rimliga skäl att anta att personen utgör en fara för nationell säkerhet eller allmän ordning. Detta är ett undantag för *enskilda personer* — inte ett sätt att undvika sitt solidaritetsbidrag som helhet (se öppen fråga nedan).

### Steg 5: Ansvarsövergång ([art. 68](../articles/ammr-068.md))

När omfördelningen genomförts blir den mottagande staten **ansvarig stat** för prövningen. Lämnar sökanden senare in en efterföljande ansökan i en annan stat är det fortfarande omfördelningsstaten som ansvarar — detta hindrar att omfördelning kringgås genom vidareförflyttning.

### Steg 6–7: Registrering i mottagande stat

Vid omfördelning ska den mottagande staten ta biometriska uppgifter och överföra dem till Eurodac snarast ([RULE-EUR-019-001](../../eurodac/rules/rule-eur-019-001.md), Eurodac art. 19). Därefter sker registreringen av ansökan i mottagande stat — vilket är domänens angivna utträdespunkt mot [Registrering](../../registration/README.md).

### Koppling till gränsförfarande

En sökande som omfördelats kan därefter hänvisas till gränsförfarande i mottagarstaten ([APR art. 43.1 d](../../border-procedure/articles/apr-043.md), [APR art. 52](../../border-procedure/articles/apr-052.md)). Omfördelning är alltså inte nödvändigtvis förfarandets slutpunkt.

---

## Vad händer om en stat inte omfördelar?

Omfördelning är den primära men inte den enda formen av solidaritet. En stat som inte omfördelar sin kvot tvingas kompensera enligt hierarkin (se [solidarity-types](solidarity-types.md)):

| Om staten inte omfördelar | Konsekvens | Rättslig grund |
|---------------------------|------------|----------------|
| Ansvarskompensation | Staten övertar prövningsansvar för motsvarande antal ansökningar | [RULE-AMMR-063-001](../rules/rule-ammr-063-001.md) (art. 63) |
| Ekonomiskt bidrag | Minst 20 000 euro per person som inte omfördelas | [art. 64](../articles/ammr-064.md) |
| Alternativa åtgärder | Kapacitetsstöd, personal, tekniskt bistånd | [art. 65](../articles/ammr-065.md) |

Systemet är designat så att ingen stat kan undvika solidaritet helt. Frågan om en stat *systematiskt* kan undvika fysisk omfördelning är dock inte helt löst — se [refusal-to-relocate](../open_questions/refusal-to-relocate.md).

---

## Sammanfattning av de sammanlänkade artefakterna

| Steg / aspekt | Artefakt |
|---------------|----------|
| Begrepp | [CON-SOL-002 Omfördelning](../concepts/relocation.md) |
| Process (helhet) | [PROC-SOL-001 Omfördelning](../processes/relocation.md) |
| Förfarande inför | [art. 67](../articles/ammr-067.md) / [RULE-AMMR-067-001](../rules/rule-ammr-067-001.md) |
| Tidsfrist (4 veckor) | [shared/time-limits](../../shared/time-limits/README.md) |
| Förfarande efter / ansvarsövergång | [art. 68](../articles/ammr-068.md) |
| Biometri i mottagande stat | [RULE-EUR-019-001](../../eurodac/rules/rule-eur-019-001.md) |
| Gränsförfarande efter omfördelning | [APR art. 43](../../border-procedure/articles/apr-043.md), [APR art. 52](../../border-procedure/articles/apr-052.md) |
| Vid utebliven omfördelning | [solidarity-types](solidarity-types.md), [refusal-to-relocate](../open_questions/refusal-to-relocate.md) |

---

## Rättslig grund

- [AMMR artikel 67](../articles/ammr-067.md) — Förfarande inför omfördelning
- [AMMR artikel 68](../articles/ammr-068.md) — Förfarande efter omfördelning
- [AMMR artikel 63](../articles/ammr-063.md) — Ansvarskompensationer
- [AMMR artikel 57](../articles/ammr-057.md) — Solidaritetspoolen

---

## Status

Complete

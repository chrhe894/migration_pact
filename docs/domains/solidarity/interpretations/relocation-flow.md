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

Den utsatta staten (gynnad medlemsstat, i repot även förmånsstat) identifierar personer som kan omfördelas och översänder uppgifter till den bidragande staten (omfördelningsmedlemsstaten). Mottagarstaten ska inom en vecka bekräfta mottagande (undantagsvis högst två veckor, tystnad = bekräftelse). Den gynnade staten beslutar om överföring inom en vecka från bekräftelsen och **överföringen ska ske inom fyra veckor efter bekräftelsen** ([RULE-AMMR-067-001](../rules/rule-ammr-067-001.md)).

Fristerna ligger hos olika stater och är samlade i [Omfördelning (översikt)](../processes/relocation.md). Rollerna har egna flöden: [Omfördelning UT](../processes/relocation-out.md) och [Omfördelning IN](../processes/relocation-in.md). Fristerna listas även i [shared/time-limits](../../../shared/time-limits/README.md).

### Säkerhetsundantag

Båda staterna kontrollerar om det finns rimliga skäl att anse att personen utgör ett **hot mot den inre säkerheten**: den gynnade staten före och under förfarandet (art. 67.2), omfördelningsmedlemsstaten vid sin granskning (art. 67.8–67.9). Bekräftas hotet omfördelas personen inte. Detta är ett undantag för *enskilda personer* — inte ett sätt att undvika sitt solidaritetsbidrag som helhet (se öppen fråga nedan). Art. 67 kopplar inte säkerhetsvägran till ansvarskompensation; det är ett separat spår (se nedan).

### Steg 5: Ansvarsövergång ([art. 68](../articles/ammr-068.md))

När omfördelningen genomförts blir den mottagande staten **ansvarig stat** för prövningen. Lämnar sökanden senare in en efterföljande ansökan i en annan stat är det fortfarande omfördelningsstaten som ansvarar — detta hindrar att omfördelning kringgås genom vidareförflyttning.

### Steg 6–7: Registrering i mottagande stat

Eurodac hanterar omfördelning i kapitel VII ([Eurodac art. 25](../../eurodac/articles/eur-025.md)): den gynnade staten uppdaterar sitt dataset med uppgift om omfördelningsmedlemsstaten så snart den är skyldig att ta emot personen (25.1), och omfördelningsmedlemsstaten översänder personens dataset med ankomstdatum när personen anlänt (25.2). Ansvaret anges i Eurodac enligt art. 16.1 och 16.3, och för personer med skydd registrerar sig omfördelningsmedlemsstaten som ansvarig med den gynnade statens markering (art. 31.6). Därefter sker registreringen av ansökan i mottagande stat — vilket är domänens angivna utträdespunkt mot [Registrering](../../registration/README.md).

> **Rättelse:** tidigare angavs Eurodac art. 19 som regel för biometri vid omfördelning. Art. 19 gäller registrering av vidarebosatta personer, inte omfördelning.

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
| Tidsfrist (4 veckor) | [shared/time-limits](../../../shared/time-limits/README.md) |
| Förfarande efter / ansvarsövergång | [art. 68](../articles/ammr-068.md) |
| Eurodac vid omfördelning | [Eurodac art. 25, 16, 31.6](../../eurodac/articles/eur-025.md) |
| Flöde UT (gynnad stat) | [PROC-SOL-002](../processes/relocation-out.md) |
| Flöde IN (omfördelningsmedlemsstat) | [PROC-SOL-003](../processes/relocation-in.md) |
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

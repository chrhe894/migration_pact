# Datapunkter: omfördelning

## Källgrund

- Ny reglering: Förordning (EU) 2024/1351, särskilt artikel 12, 13, 15, 56-69, 70-72 och bilaga I.
- Lokal ny källa: `ref_material/OJ_L_202401351_SV_TXT.pdf`.
- Officiell referens:
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1351>

## Datapunkter att modellera

| Datapunkt | Exempel på värde | Källa i ny reglering | Möjlig systemkälla |
| --- | --- | --- | --- |
| Solidaritetsår | 2027 | Artiklarna 12, 57 | Styrning/rapportering |
| Genomförandeakt | Rådsbeslut för årlig pool | Artiklarna 57, 61, 62 | Juridik/styrning |
| Medlemsstatsroll | Bidragande, gynnad, omfördelningsmedlemsstat | Artiklarna 56-69 | Ärendehantering/styrning |
| Solidaritetstyp | Omfördelning, ekonomiskt bidrag, alternativ åtgärd | Artikel 56.2 | Styrning/ekonomi |
| Utfästelse | Antal personer eller belopp | Artiklarna 13, 57 | Styrning/rapportering |
| Referensandel | Procent/antal enligt referensnyckel | Artikel 66 och bilaga I | BI/styrning |
| Folkmängdsunderlag | Eurostatvärde | Artikel 66 | BI/extern data |
| BNP-underlag | Eurostatvärde | Artikel 66 | BI/extern data |
| Personkategori | Sökande, person med internationellt skydd | Artiklarna 56.2 a, 67, 68 | Ärendehantering |
| Omfördelningsbarhet | Ja/nej, skälskod | Artikel 67 | Ärendehantering |
| Säkerhetshinder | Rimliga skäl finns/finns inte | Artikel 67.2, 67.8-9 | Screening/säkerhet |
| Meningsfull koppling | Familj, kultur, språk, annan relevant koppling | Artikel 67.3-4 | Ärendehantering |
| Familjesammanhållning | Familjegrupp-id | Artikel 67.6 | Person-/familjerelationer |
| Samtycke skyddsstatus | Skriftligt samtycke ja/nej | Artikel 67.4 | Dokument/kommunikation |
| Informationsgivning | Datum, kanal, språk | Artikel 67.5 | Kommunikation |
| Standardformulär | Skickat/mottaget, version | Artikel 67.7, 67.14 | Integration/dokument |
| Relevant handling | Identitet, ärendeunderlag, skyddsskäl, beslutsskäl | Artikel 67.7, 67.13 | Dokument/arkiv |
| Bekräftelsefrist | En vecka, två veckor vid undantag | Artikel 67.9 | Fristmotor |
| Bekräftelsestatus | Bekräftad, avslag på grund av säkerhet, uteblivet svar | Artikel 67.9 | Ärendehantering |
| Överföringsbeslut | Datum, mottagande medlemsstat | Artikel 67.10 | Beslut/kommunikation |
| Underrättelsefrist | Senast två dagar före överföring för sökande, en vecka för skyddsstatus | Artikel 67.10 | Fristmotor/kommunikation |
| Överföringsfrist | Inom fyra veckor | Artikel 67.11 | Fristmotor/logistik |
| Ankomststatus | Ankommen, ej infunnit sig | Artikel 68.1 | Mottagning/integration |
| Ansvarsövergång | Ansvarig medlemsstat efter omfördelning | Artikel 68.2-3 | Ansvarsmodul/Eurodac |
| Eurodacansvar | Angivet enligt 2024/1358 artikel 16.1 eller 16.3 | Artikel 68.2-3 | Eurodac/integration |
| Efterföljande ansökan | Ansvar följer omfördelningsmedlemsstat | Artikel 68.3 | Ärendehistorik |
| Skyddsstatus efter omfördelning | Automatisk motsvarande status | Artikel 68.4 | Beslut/mottagning |
| Ansvarskompensation | Antal ansökningar som tas över | Artikel 69 | Ansvarsmodul |
| Rapportering av genomförande | Status, hinder, genomförda åtgärder | Artikel 70 | Rapportering |
| Ekonomiskt stöd efter omfördelning | AMIF-stöd enligt 2021/1147 | Artikel 71 | Ekonomi/styrning |

## Centrala tidsfrister

| Moment | Tidsfrist | Kommentar |
| --- | --- | --- |
| Kommissionens årliga förslag | Senast 15 oktober | Artikel 12.6. |
| Rådets årliga solidaritetspool | Före utgången av varje kalenderår | Artikel 57.1. |
| Omfördelningsmedlemsstatens svar | Inom en vecka | Artikel 67.9. |
| Uppskjutet svar vid komplicerad granskning | Senast inom två veckor | Artikel 67.9. |
| Överföringsbeslut efter bekräftelse | Inom en vecka | Artikel 67.10. |
| Underrättelse till sökande | Senast två dagar före överföring | Artikel 67.10. |
| Underrättelse till person med skyddsstatus | Senast en vecka före överföring | Artikel 67.10. |
| Fysisk överföring | Inom fyra veckor efter bekräftelse eller slutligt beslut vid suspensiv verkan | Artikel 67.11. |
| Svar vid ansvarskompensation | Inom 30 dagar | Artikel 69.2. |

## Datakvalitetsregler att följa upp

- Omfördelningsärende ska ha koppling till ett giltigt solidaritetsår och relevant genomförandeakt.
- Personer med rimliga säkerhetshinder ska inte ligga kvar som omfördelningsbara.
- Familjemedlemmar ska inte splittras mellan olika omfördelningsmedlemsstater.
- Uppgift om meningsfull koppling ska vara dokumenterad men inte presenteras som valfri medlemsstatsval.
- Uteblivet svar inom frist ska kunna hanteras som bekräftelse när artikel 67.9 är tillämplig.
- Ansvarsövergång efter omfördelning ska stämma mellan ärendesystem och Eurodac.
- Omfördelning, ansvarskompensation och ekonomiska/alternativa solidaritetsåtgärder ska kunna hållas isär i rapportering.

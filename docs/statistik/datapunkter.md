# Datapunkter: statistik

## Källgrund

- Ny reglering: Förordning (EU) 2024/1358, särskilt artikel 12, 17, 19, 21-24, 26, 31, 57 och 63.
- Gammal reglering: Förordning (EU) nr 603/2013, särskilt artikel 8.
- Lokal ny källa: `ref_material/OJ_L_202401358_SV_TXT.pdf`.
- Officiella referenser:
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1358>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32013R0603>

## Datapunkter att modellera

| Datapunkt | Exempel på värde | Källa i ny reglering | Möjlig systemkälla |
| --- | --- | --- | --- |
| Statistikperiod | Månad, år | Artikel 12.2 | Statistik/BI |
| Medlemsstat | Sverige, Danmark, Tyskland | Artikel 12.2 | Eurodac/integration |
| Eurodac-kategori | Sökande, irreguljär gränspassage, olaglig vistelse, SAR, vidarebosättning, tillfälligt skydd | Artikel 12.1 och artiklar 15, 18, 20, 22, 23, 24, 26 | Ärendehantering/Eurodac |
| Första ansökan | Ja/nej | Artikel 12.1 b | Ärendehistorik/Eurodac |
| Rejected applicant utan rätt att stanna | Ja/nej, datum | Artikel 12.1 c och artikel 17.2 j | Beslut/Återvändande |
| Minderårig | Ja/nej | Artikel 12.1 f | Person-/ärendehantering |
| Födelseår | ÅÅÅÅ | Artikel 12.2 | Person-/ärendehantering |
| Kön | Registrerat kön | Artikel 12.2 och datalistorna i artiklarna 17, 19, 21-24, 26 | Person-/ärendehantering |
| Biometrisk sändning | Datum/tid skickad | Artiklarna 15, 18, 20, 22, 23, 24, 26 | Eurodac/integration |
| Biometrisk kvalitet | Godkänd, begärd igen | Artikel 12.1 q | Eurodac/integration |
| Träff | Träff/ingen träff | Artikel 12.1 k-p | Eurodac/integration |
| Träffkategori | Träff mot sökande, olaglig vistelse, SAR, skyddsstatus etc. | Artikel 12.1 k-p | Eurodac/integration/BI |
| Ansvarig medlemsstat | Medlemsstat | Artikel 16 och artikel 12 indirekt | Ansvarsfördelning/Eurodac |
| Skyddsstatus beviljad | Ja/nej, datum | Artikel 12.1 e, artikel 31 | Beslut/Eurodac |
| Markering/avmarkering | Markerad, avmarkerad | Artikel 12.1 r-s och artikel 31 | Eurodac/integration |
| Vidarebosättningsspår | EU-ram eller nationell ordning | Artikel 12.1 g-h och artiklar 18-21 | Vidarebosättning |
| Admission outcome | Beviljad, vägrad, avbruten | Artikel 12.1 k-l och artikel 19 | Vidarebosättning |
| SAR-landstigning | Ja/nej, plats, datum | Artikel 24 och artikel 12.1 | Gräns/Eurodac |
| Tillfälligt skydd | Registrerad förmånstagare | Artikel 26 och artikel 63.2 | Mottagning/Eurodac |
| AVRR | Beviljad frivillig återvändandehjälp | Artiklarna 22-24 | Återvändande |
| Avresa/avlägsnande | Datum | Artiklarna 16, 22-24 | Återvändande |
| Relocation | Medlemsstat för relocation | Artiklarna 22-25 | Ansvar/solidaritet |
| Säkerhetsflagga | Ja/nej, borttagen | Artiklarna 17, 22-24 och skäl 7-8 | Screening/Eurodac |
| Brottsbekämpande begäran | Antal begäranden, träffar, syfte | Artikel 57.8 | Särskild åtkomstkedja |
| Statistikbehörighet | Utsedd myndighet/användare | Artikel 12.6 | Behörighet/IAM |

## Frekvens och åtkomst

| Rapporttyp | Frekvens | Mottagare/åtkomst | Kommentar |
| --- | --- | --- | --- |
| Eurodac månadsstatistik | Månatlig | Publiceras av eu-LISA; tillgänglig för relevanta aktörer enligt artikel 12 | Artikel 12.2. |
| Eurodac årsstatistik | Årlig | Publiceras av eu-LISA | Artikel 12.2. |
| Cross-system-statistik | Månatlig | Medlemsstater, Europaparlamentet, kommissionen, EUAA, Frontex och Europol | Artikel 12.3; innehåll specificeras i genomförandeakter. |
| Särskild statistik på kommissionens begäran | Vid begäran | Kommissionen och vid begäran andra angivna aktörer | Artikel 12.4. |
| Underlag till årsrapport | Årlig | eu-LISA och kommissionen | Artikel 57.6. |
| Övergripande utvärdering | Vart fjärde år från 12 juni 2029 | Kommissionen | Artikel 57.5 och 57.7. |
| Brottsbekämpande åtkomst | Vartannat år | Kommissionen, sedan Europaparlamentet, rådet och EDPS | Artikel 57.8-57.9. |

## Datakvalitetsregler att följa upp

- Poster utan Eurodac-kategori bör inte kunna ingå i statistik utan avvikelsemarkering.
- Sena överföringar bör kunna följas per kategori, plats och tidsfrist.
- Dubbletter bör hanteras genom Eurodac-länkning av dataset och nationell ärendehistorik.
- Korrigeringar efter överföring bör kunna spåras utan att historiska rapporter blir obegripliga.
- Små tal och kombinationer av födelseår, kön, medlemsstat och kategori bör kontrolleras mot risk för indirekt identifiering.
- Artikel 26 om tillfälligt skydd bör hållas separat i rapportlogiken eftersom den tillämpas från 12 juni 2029.

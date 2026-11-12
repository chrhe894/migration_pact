---
search:
  exclude: true
---

# Förlängning och frysning per domän (arbetssida)

> **Tillfällig arbetssida.** Sidan finns inte i menyn och är utesluten från sökningen. Den nås bara via direktlänk.
> Kolumner markerade med * är förifyllda. Övriga kolumner är tomma för ifyllnad.
> Underlag och detaljer: [Frysning och förlängning av tidsfrister](concepts/frysning-och-forlangning.md).

**Så är kolumnerna ifyllda**

- **Processlista start / stopp:** den domän där händelsen som startar fristen sker, och den domän där fristen ska vara uppfylld. Exempel: Eurodac-fristen startar vid registreringen (Registrering) och uppfylls vid överföringen till Eurodac (Eurodac).
- **Kortnamn** innehåller rättslig grund inom parentes.
- **Tidsfrist:** ordinarie frist → frist efter förlängning, eller den nya startpunkten vid frysning.
- **Frysning** betyder att en ny frist räknas från en ny startpunkt. Fristen pausas inte. Vid hälsohinder i Eurodac (rad 6, 11 och 23) är den nya fristen kortare (48 h) än den ordinarie.
- **Ordning:** raderna följer [livscykeln](../../CASE_LIFECYCLE.md) och sorteras efter när fristen startar i ärendets förlopp.
- **Egna tabeller:** [Solidaritet](#solidaritet-omfordelning) (S1–S2) och [Krisläge](#krislage) (K1–K9) är parallella spår som inte varje ärende passerar.

## Ordinarie läge

| Rader | Livscykelsteg |
|-------|---------------|
| 1–6 | 1. Screening (biometri som tas i samband med gripande, landsättning eller ansökan vid gränsen) |
| 7–9 | 2. Registrering |
| 10–11 | 3. Biometri (Eurodac) för sökande |
| 12 | 4. Inlämnande |
| 13–18 | 5. Ansvar |
| 19–20 | 6a. Asylförfarande |
| 21 | 6b. Gränsförfarande |
| 22–24 | Utanför asylärendets livscykel (tillfälligt skydd och vidarebosättning i Eurodac) |

| # | Status | Processlista - start * | Processlista stopp * | Kortnamn * | Tidsfrist * (dag/veckor/månad) | Aktivitet - start | Aktivitet - stopp | Flöde - start | Händelse - start | Flöde - stopp | Händelse - stopp | Typ * (Förlängning/Frysning) |
|---|--------|------------------------|----------------------|------------|-------------------------------|-------------------|-------------------|---------------|------------------|---------------|------------------|------------------------------|
| 1 | | Screening | Eurodac | Sök och räddning, tekniska problem (Eurodac 24.5) | 72 timmar → +48 timmar | | | | | | | Förlängning |
| 2 | | Screening | Eurodac | Sök och räddning, plötslig tillströmning (Eurodac 24.6) | 72 timmar → +48 timmar (under högst 1 månad) | | | | | | | Förlängning |
| 3 | | Screening | Eurodac | Irreguljär gränspassage, tekniska problem (Eurodac 22.6) | 72 timmar → +48 timmar | | | | | | | Förlängning |
| 4 | | Screening | Eurodac | Biometri sökande vid gränsövergång, tekniska problem (Eurodac 15.1 b, 15.2) | 72 timmar → +48 timmar | | | | | | | Förlängning |
| 5 | | Screening | Eurodac | Olaglig vistelse, tekniska problem (Eurodac 23.5) | 72 timmar → +48 timmar | | | | | | | Förlängning |
| 6 | | Screening | Eurodac | Hälsohinder, irreguljär gränspassage, olaglig vistelse, sök och räddning (Eurodac 22.6, 23.5, 24.5) | 72 timmar → 48 timmar efter att hindren undanröjts | | | | | | | Frysning |
| 7 | | Registrering | Registrering | Registrering vid massinflöde (APR 27) | 5 dagar → 15 dagar | | | | | | | Förlängning |
| 8 | | Registrering | Registrering | Företrädare för ensamkommande barn (APR 23.3) | 15 arbetsdagar → +10 arbetsdagar | | | | | | | Förlängning |
| 9 | | Registrering | Asylförfarande | Sökandehandlingens giltighet (APR 29.9) | Upp till 12 månader → hela perioden med rätt att stanna kvar | | | | | | | Förlängning |
| 10 | | Registrering | Eurodac | Biometri sökande, tekniska problem (Eurodac 15.1 a, 15.2) | 72 timmar → +48 timmar | | | | | | | Förlängning |
| 11 | | Registrering | Eurodac | Hälsohinder, sökande (Eurodac 15.2) | 72 timmar → 48 timmar efter att hindren undanröjts | | | | | | | Frysning |
| 12 | | Registrering | Registrering | Bokad tid för inlämnande vid massinflöde (APR 28.5) | 21 dagar → 2 månader från registreringen | | | | | | | Förlängning |
| 13 | | Ansvar | Ansvar | Företrädare för ensamkommande barn (AMMR 23.2 b) | 15 arbetsdagar → +10 arbetsdagar | | | | | | | Förlängning |
| 14 | | Registrering | Ansvar | Framställan om övertagande, undanhållna uppgifter (AMMR 51.5) | 2 månader (1 månad efter träff) → + lika lång tid som svaret försenats | | | | | | | Förlängning |
| 15 | | Ansvar | Ansvar | Överföring, frihetsberövad (AMMR 46.2) | 6 månader → högst 1 år | | | | | | | Förlängning |
| 16 | | Ansvar | Ansvar | Överföring, avvikande / motstånd / medicinska krav (AMMR 46.2) | 6 månader → högst 3 år | | | | | | | Förlängning |
| 17 | | Ansvar | Ansvar | Överföring, suspensiv verkan (AMMR 46.1) | 6 månader → ny full frist från slutligt beslut om överklagandet | | | | | | | Frysning |
| 18 | | Ansvar | Ansvar | Överföring vid förvar, suspensiv verkan (AMMR 45.3 b) | 5 veckor → ny full frist från den dag suspensiv verkan upphör | | | | | | | Frysning |
| 19 | | Registrering | Asylförfarande | Upptagandeprövning (APR 35.2) | 2 månader → +högst 2 månader (max 4) | | | | | | | Förlängning |
| 20 | | Registrering | Asylförfarande | Prövning i sak (APR 35.5) | 6 månader → +högst 6 månader (max 12) | | | | | | | Förlängning |
| 21 | | Registrering | Gränsförfarande | Gränsförfarande efter omfördelning (APR 51.2) | 12 veckor → 16 veckor (inte i kombination med K8) | | | | | | | Förlängning |
| 22 | | Eurodac | Eurodac | Tillfälligt skydd, tekniska problem (Eurodac 26.4) | 10 dagar → +48 timmar | | | | | | | Förlängning |
| 23 | | Eurodac | Eurodac | Hälsohinder, nationell vidarebosättning och tillfälligt skydd (Eurodac 20.3, 26.4) | 72 timmar / 10 dagar → 48 timmar efter att hindren undanröjts | | | | | | | Frysning |
| 24 | | Eurodac | Eurodac | Lagring tillfälligt skydd (Eurodac 29.9) | 1 år → förlängs varje år så länge skyddet varar | | | | | | | Förlängning |

> Rad 21 utlöses av en omfördelning (S2). Den står här eftersom fristen löper i gränsförfarandet.

## Solidaritet (omfördelning)

Omfördelningen startar när en person identifieras för omfördelning från solidaritetspoolen ([AMMR art. 67](../../domains/solidarity/articles/ammr-067.md)). Spåret går parallellt med livscykeln, ungefär i höjd med steg 5 (Ansvar).

| # | Status | Processlista - start * | Processlista stopp * | Kortnamn * | Tidsfrist * (dag/veckor/månad) | Aktivitet - start | Aktivitet - stopp | Flöde - start | Händelse - start | Flöde - stopp | Händelse - stopp | Typ * (Förlängning/Frysning) |
|---|--------|------------------------|----------------------|------------|-------------------------------|-------------------|-------------------|---------------|------------------|---------------|------------------|------------------------------|
| S1 | | Solidaritet | Solidaritet | Besked från omfördelningsmedlemsstaten (AMMR 67.9) | 1 vecka → högst 2 veckor | | | | | | | Förlängning |
| S2 | | Solidaritet | Solidaritet | Överföring vid omfördelning, suspensiv verkan (AMMR 67.11) | 4 veckor → ny full frist från slutligt beslut om överklagandet | | | | | | | Frysning |

> Beslutsfristen (1 vecka) har ingen förlängning eller frysning och är därför inte med.

## Krisläge

Gäller bara när rådet genom ett genomförandebeslut har godkänt undantagen för medlemsstaten (krisförordningen 2024/1359, art. 4). Registrering, ansvar och gränsförfarande för asyl gäller vid kris eller force majeure. Gränsförfarandet för återvändande gäller bara vid kris (Return art. 6).

| # | Status | Processlista - start * | Processlista stopp * | Kortnamn * | Tidsfrist * (dag/veckor/månad) | Aktivitet - start | Aktivitet - stopp | Flöde - start | Händelse - start | Flöde - stopp | Händelse - stopp | Typ * (Förlängning/Frysning) |
|---|--------|------------------------|----------------------|------------|-------------------------------|-------------------|-------------------|---------------|------------------|---------------|------------------|------------------------------|
| K1 | | Registrering | Registrering | Registrering vid kris (Kris 10.1) | 5 dagar → 4 veckor | | | | | | | Förlängning |
| K2 | | Registrering | Ansvar | Framställan om övertagande vid kris (Kris 12.2 a) | 2 månader → 4 månader från registreringen | | | | | | | Förlängning |
| K3 | | Ansvar | Ansvar | Svar på framställan vid kris (Kris 12.2 b) | 1 månad → 2 månader | | | | | | | Förlängning |
| K4 | | Eurodac | Ansvar | Avisering om återtagande vid kris (Kris 12.2 c) | 2 veckor från Eurodac-träffen → 1 månad | | | | | | | Förlängning |
| K5 | | Ansvar | Ansvar | Bekräftelse av återtagande vid kris (Kris 12.2 c) | 2 veckor → 1 månad | | | | | | | Förlängning |
| K6 | | Ansvar | Ansvar | Överföring vid kris (Kris 12.2 d) | 6 månader → 1 år | | | | | | | Förlängning |
| K7 | | Ansvar | Ansvar | Överföring vid kris, suspensiv verkan (Kris 12.2 d) | 1 år → ny full frist från slutligt beslut om överklagandet | | | | | | | Frysning |
| K8 | | Registrering | Gränsförfarande | Gränsförfarande vid kris (Kris 11.1) | 12 veckor → högst 18 veckor (inte i kombination med rad 21) | | | | | | | Förlängning |
| K9 | | Gränsförfarande | Återvändande vid gräns | Återvändande vid gräns vid kris (Return 6.1) | 12 veckor → högst 18 veckor | | | | | | | Förlängning |

> Rad 2 (plötslig tillströmning vid sök och räddning) bygger på Eurodacförordningen och kräver inget krisbeslut. Den står därför i den ordinarie tabellen.

## Domäner utan förlängning eller frysning

| Domän | Varför |
|-------|--------|
| Screening (egna frister) | 7 dagar vid yttre gräns och 3 dagar inom territoriet kan inte förlängas. Sjudagarsfristen kan i stället förkortas till 4 dagar (Screening art. 8.3) |
| Asylförfarande, efterföljande ansökan | Inga egna förlängningar. Samma som rad 19–20 när ansökan tas upp |
| Asylförfarande, påskyndat förfarande och art. 38.1 e | 3 månader respektive 10 arbetsdagar har ingen förlängningsgrund (APR art. 35) |
| Återvändande vid gräns (ordinarie läge) | 12 veckor och frivillig avresa högst 15 dagar har ingen förlängning utanför kris (K9) |
| Kris | Har inga egna frister. Förlänger frister i andra domäner (K1–K9) |

## Avgränsning (inte med i tabellerna)

- **Uppskjutanden och spärrar** är varken förlängning eller frysning: uppskjutande vid osäkra förhållanden (APR 35.7, max 21 månader), uppskjutande innan implicit återkallande (APR 41.4), spärr för överföring till krisstat (Kris 12.4) och domstolens beslut om uppskov (AMMR 43.3).
- **Gränsförfarandet för återvändande** startar när rätten att stanna kvar upphört (Return 4.2). Det är en senare startpunkt, inte en frysning.
- **Prövning i sak efter AMMR-överföring** räknas från inlämnandet i den ansvariga medlemsstaten (APR 35.6). Det anger var fristen startar, inte en ny startpunkt för en frist som redan löper.
- **Förhandstillämpning vid kris** (Kris 10.6, högst 10 dagar) avser när krisregeln får börja tillämpas, inte en frist som förlängs.

---
search:
  exclude: true
---

# Förlängning, frysning och förkortning per domän (arbetssida)

> **Tillfällig arbetssida.** Sidan finns inte i menyn och är utesluten från sökningen. Den nås bara via direktlänk.
> Kolumner markerade med * är förifyllda. Övriga kolumner är tomma för ifyllnad.
> Underlag och detaljer: [Frysning och förlängning av tidsfrister](concepts/frysning-och-forlangning.md).

**Så är kolumnerna ifyllda**

- **Processlista start / stopp:** den domän där händelsen som startar fristen sker, och den domän där fristen ska vara uppfylld. Exempel: Eurodac-fristen startar vid registreringen (Registrering) och uppfylls vid överföringen till Eurodac (Eurodac).
- **Kortnamn** innehåller rättslig grund inom parentes.
- **Villkor** anger vad som måste vara uppfyllt och vem som avgör. "Gäller direkt" betyder att förordningen säger "ska" och att inget särskilt beslut krävs. "Får" betyder att myndigheten beslutar.
- **Tidsfrist:** ordinarie frist → frist efter förlängning eller förkortning, eller den nya startpunkten vid frysning.
- **Frysning** betyder att en ny frist räknas från en ny startpunkt. Fristen pausas inte. Vid hälsohinder i Eurodac (rad 6, 11 och 23) är den nya fristen kortare (48 h) än den ordinarie.
- **Oproportionellt stort antal ansökningar** (rad 7, 8, 12, 13, 19, 20) är inte kris och kräver inget EU-beslut. Myndigheten bedömer själv om det blivit omöjligt att hålla fristen. Kris (massankomst enligt krisförordningen art. 1.4 a) kräver beslut av kommissionen och rådet, se [Krisläge](#krislage).
- **Ordning:** raderna följer [livscykeln](../../CASE_LIFECYCLE.md) och sorteras efter när fristen startar i ärendets förlopp.
- **Egna tabeller:** [Solidaritet](#solidaritet-omfordelning) (S1–S2), [Krisläge](#krislage) (K1–K9) och [Förkortningar](#forkortningar) (FK1–FK14).

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

| # | Status | Processlista - start * | Processlista stopp * | Kortnamn * | Villkor * | Tidsfrist * (dag/veckor/månad) | Aktivitet - start | Aktivitet - stopp | Flöde - start | Händelse - start | Flöde - stopp | Händelse - stopp | Typ * (Förlängning/Frysning) |
|---|--------|------------------------|----------------------|------------|-----------|-------------------------------|-------------------|-------------------|---------------|------------------|---------------|------------------|------------------------------|
| 1 | | Screening | Eurodac | Sök och räddning, tekniska problem (Eurodac 24.5) | Allvarliga tekniska problem. Förlängningen används för att genomföra nationella kontinuitetsplaner. Medlemsstaten får förlänga | 72 timmar → +48 timmar | | | | | | | Förlängning |
| 2 | | Screening | Eurodac | Sök och räddning, plötslig tillströmning (Eurodac 24.6) | Plötslig tillströmning. Medlemsstaten får förlänga. Gäller från den dag den anmäls till kommissionen och övriga medlemsstater, under den period som anges i anmälan. Inget krisbeslut krävs | 72 timmar → +48 timmar (under högst 1 månad) | | | | | | | Förlängning |
| 3 | | Screening | Eurodac | Irreguljär gränspassage, tekniska problem (Eurodac 22.6) | Allvarliga tekniska problem, kontinuitetsplaner. Medlemsstaten får förlänga | 72 timmar → +48 timmar | | | | | | | Förlängning |
| 4 | | Screening | Eurodac | Biometri sökande vid gränsövergång, tekniska problem (Eurodac 15.1 b, 15.2) | Ansökan görs vid gränsövergångsställe eller i transitzon av person som inte uppfyller inresevillkoren. Allvarliga tekniska problem, kontinuitetsplaner | 72 timmar från att biometrin togs → +48 timmar | | | | | | | Förlängning |
| 5 | | Screening | Eurodac | Olaglig vistelse, tekniska problem (Eurodac 23.5) | Allvarliga tekniska problem, kontinuitetsplaner. Medlemsstaten får förlänga | 72 timmar → +48 timmar | | | | | | | Förlängning |
| 6 | | Screening | Eurodac | Hälsohinder, irreguljär gränspassage, olaglig vistelse, sök och räddning (Eurodac 22.6, 23.5, 24.5) | Biometrin kan inte tas på grund av åtgärder för att skydda personens hälsa eller folkhälsan. Gäller direkt | 72 timmar → 48 timmar efter att hindren undanröjts | | | | | | | Frysning |
| 7 | | Registrering | Registrering | Registrering vid oproportionellt stort antal ansökningar (APR 27.5) | Oproportionellt stort antal ansökningar inom samma tidsperiod gör det omöjligt att registrera inom 5 dagar. Gäller direkt | 5 dagar → 15 dagar från att ansökan gjordes | | | | | | | Förlängning |
| 8 | | Registrering | Registrering | Företrädare för ensamkommande barn (APR 23.3) | Oproportionellt stort antal ansökningar från ensamkommande barn, eller andra exceptionella situationer. Myndigheten får förlänga | 15 arbetsdagar → +10 arbetsdagar | | | | | | | Förlängning |
| 9 | | Registrering | Asylförfarande | Sökandehandlingens giltighet (APR 29.9) | Handlingen utfärdas av den ansvariga medlemsstaten | Upp till 12 månader → hela perioden med rätt att stanna kvar | | | | | | | Förlängning |
| 10 | | Registrering | Eurodac | Biometri sökande, tekniska problem (Eurodac 15.1 a, 15.2) | Allvarliga tekniska problem, kontinuitetsplaner. Medlemsstaten får förlänga | 72 timmar från registreringen → +48 timmar | | | | | | | Förlängning |
| 11 | | Registrering | Eurodac | Hälsohinder, sökande (Eurodac 15.2) | Biometrin kan inte tas på grund av åtgärder för att skydda personens hälsa eller folkhälsan. Gäller direkt | 72 timmar → 48 timmar efter att hindren undanröjts | | | | | | | Frysning |
| 12 | | Registrering | Registrering | Bokad tid för inlämnande vid oproportionellt stort antal ansökningar (APR 28.5) | Oproportionellt stort antal ansökningar gör det omöjligt att ge varje sökande en bokad tid inom 21 dagar. Gäller direkt | 21 dagar → 2 månader från registreringen | | | | | | | Förlängning |
| 13 | | Ansvar | Ansvar | Företrädare för ensamkommande barn (AMMR 23.2 b) | Oproportionellt stort antal ansökningar från ensamkommande barn, eller andra exceptionella situationer. Myndigheten får förlänga | 15 arbetsdagar → +10 arbetsdagar | | | | | | | Förlängning |
| 14 | | Registrering | Ansvar | Framställan om övertagande, undanhållna uppgifter (AMMR 51.5) | Den anmodade staten har vid informationsutbyte undanhållit uppgifter som visar att den är ansvarig. Gäller direkt | 2 månader (1 månad efter träff) → + lika lång tid som svaret försenats | | | | | | | Förlängning |
| 15 | | Ansvar | Ansvar | Överföring, frihetsberövad (AMMR 46.2) | Överföringen har inte kunnat verkställas därför att personen varit frihetsberövad | 6 månader → högst 1 år | | | | | | | Förlängning |
| 16 | | Ansvar | Ansvar | Överföring, avvikande / motstånd / medicinska krav (AMMR 46.2) | Personen eller medföljande familjemedlem har avvikit, motsätter sig fysiskt, ser avsiktligt till att tillståndet inte medger överföring, eller uppfyller inte de medicinska kraven. Den överförande staten underrättar den ansvariga | 6 månader → högst 3 år från underrättelsen | | | | | | | Förlängning |
| 17 | | Ansvar | Ansvar | Överföring, suspensiv verkan (AMMR 46.1) | Överklagande eller omprövning med suspensiv verkan (AMMR 43.3) | 6 månader → ny full frist från slutligt beslut om överklagandet | | | | | | | Frysning |
| 18 | | Ansvar | Ansvar | Överföring vid förvar, suspensiv verkan (AMMR 45.3 b) | Personen hålls i förvar och överklagandet har haft suspensiv verkan. Passeras fristen ska personen friges, men art. 46 gäller fortsatt (45.4) | 5 veckor → ny full frist från den dag suspensiv verkan upphör | | | | | | | Frysning |
| 19 | | Registrering | Asylförfarande | Upptagandeprövning (APR 35.2) | Oproportionellt stort antal ansökningar, komplexa faktiska eller rättsliga omständigheter, eller försening som enbart beror på sökandens underlåtenhet (art. 9). Beslutande myndighet får förlänga | 2 månader → +högst 2 månader (max 4) | | | | | | | Förlängning |
| 20 | | Registrering | Asylförfarande | Prövning i sak (APR 35.5) | Samma tre grunder som rad 19. Beslutande myndighet får förlänga | 6 månader → +högst 6 månader (max 12) | | | | | | | Förlängning |
| 21 | | Registrering | Gränsförfarande | Gränsförfarande efter omfördelning (APR 51.2) | Den medlemsstat som personen överförts till enligt AMMR 67.11 tillämpar gränsförfarandet. Inte i kombination med K8 | 12 veckor → 16 veckor | | | | | | | Förlängning |
| 22 | | Eurodac | Eurodac | Tillfälligt skydd, tekniska problem (Eurodac 26.4) | Allvarliga tekniska problem. Medlemsstaten får förlänga | 10 dagar → +48 timmar | | | | | | | Förlängning |
| 23 | | Eurodac | Eurodac | Hälsohinder, nationell vidarebosättning och tillfälligt skydd (Eurodac 20.3, 26.4) | Biometrin kan inte tas på grund av åtgärder för att skydda personens hälsa eller folkhälsan. Gäller direkt | 72 timmar / 10 dagar → 48 timmar efter att hindren undanröjts | | | | | | | Frysning |
| 24 | | Eurodac | Eurodac | Lagring tillfälligt skydd (Eurodac 29.9) | Det tillfälliga skyddet består. Gäller direkt | 1 år → förlängs varje år så länge skyddet varar | | | | | | | Förlängning |

> Rad 21 utlöses av en omfördelning (S2). Den står här eftersom fristen löper i gränsförfarandet.

## Solidaritet (omfördelning)

Omfördelningen startar när en person identifieras för omfördelning från solidaritetspoolen ([AMMR art. 67](../../domains/solidarity/articles/ammr-067.md)). Spåret går parallellt med livscykeln, ungefär i höjd med steg 5 (Ansvar).

| # | Status | Processlista - start * | Processlista stopp * | Kortnamn * | Villkor * | Tidsfrist * (dag/veckor/månad) | Aktivitet - start | Aktivitet - stopp | Flöde - start | Händelse - start | Flöde - stopp | Händelse - stopp | Typ * (Förlängning/Frysning) |
|---|--------|------------------------|----------------------|------------|-----------|-------------------------------|-------------------|-------------------|---------------|------------------|---------------|------------------|------------------------------|
| S1 | | Solidaritet | Solidaritet | Besked från omfördelningsmedlemsstaten (AMMR 67.9) | Särskilt komplicerad granskning, eller ett stort antal ärenden samtidigt. Omfördelningsstaten meddelar uppskjutandet inom den första veckan | 1 vecka → högst 2 veckor | | | | | | | Förlängning |
| S2 | | Solidaritet | Solidaritet | Överföring vid omfördelning, suspensiv verkan (AMMR 67.11) | Överklagande eller omprövning med suspensiv verkan | 4 veckor → ny full frist från slutligt beslut om överklagandet | | | | | | | Frysning |

> Beslutsfristen (1 vecka) har ingen förlängning eller frysning och är därför inte med.

## Krisläge

Gäller bara när rådet genom ett genomförandebeslut har godkänt undantagen för medlemsstaten (krisförordningen 2024/1359, art. 4). Registrering, ansvar och gränsförfarande för asyl gäller vid kris eller force majeure. Gränsförfarandet för återvändande gäller bara vid kris (Return art. 6).

| # | Status | Processlista - start * | Processlista stopp * | Kortnamn * | Villkor * | Tidsfrist * (dag/veckor/månad) | Aktivitet - start | Aktivitet - stopp | Flöde - start | Händelse - start | Flöde - stopp | Händelse - stopp | Typ * (Förlängning/Frysning) |
|---|--------|------------------------|----------------------|------------|-----------|-------------------------------|-------------------|-------------------|---------------|------------------|---------------|------------------|------------------------------|
| K1 | | Registrering | Registrering | Registrering vid kris (Kris 10.1) | Rådets beslut godkänner art. 10. Vid kris enligt art. 1.4 a gäller den bara under perioden i det ursprungliga beslutet, inte under förlängningar (10.4) | 5 dagar → 4 veckor från att ansökan gjordes | | | | | | | Förlängning |
| K2 | | Registrering | Ansvar | Framställan om övertagande vid kris (Kris 12.2 a) | Rådets beslut godkänner art. 12. Missas fristen blir krisstaten ansvarig (12.3) | 2 månader → 4 månader från registreringen | | | | | | | Förlängning |
| K3 | | Ansvar | Ansvar | Svar på framställan vid kris (Kris 12.2 b) | Rådets beslut godkänner art. 12. Missas fristen blir krisstaten ansvarig (12.3) | 1 månad → 2 månader | | | | | | | Förlängning |
| K4 | | Eurodac | Ansvar | Avisering om återtagande vid kris (Kris 12.2 c) | Rådets beslut godkänner art. 12 | 2 veckor från Eurodac-träffen → 1 månad | | | | | | | Förlängning |
| K5 | | Ansvar | Ansvar | Bekräftelse av återtagande vid kris (Kris 12.2 c) | Rådets beslut godkänner art. 12 | 2 veckor → 1 månad | | | | | | | Förlängning |
| K6 | | Ansvar | Ansvar | Överföring vid kris (Kris 12.2 d) | Rådets beslut godkänner art. 12. Missas fristen blir krisstaten ansvarig (12.3) | 6 månader → 1 år | | | | | | | Förlängning |
| K7 | | Ansvar | Ansvar | Överföring vid kris, suspensiv verkan (Kris 12.2 d) | Som K6, och överklagandet har suspensiv verkan | 1 år → ny full frist från slutligt beslut om överklagandet | | | | | | | Frysning |
| K8 | | Registrering | Gränsförfarande | Gränsförfarande vid kris (Kris 11.1) | Rådets beslut godkänner art. 11. Inte i kombination med rad 21 | 12 veckor → högst 18 veckor | | | | | | | Förlängning |
| K9 | | Gränsförfarande | Återvändande vid gräns | Återvändande vid gräns vid kris (Return 6.1) | Krissituation (inte force majeure) och rådets beslut efter begäran från medlemsstaten | 12 veckor → högst 18 veckor | | | | | | | Förlängning |

> Rad 2 (plötslig tillströmning vid sök och räddning) bygger på Eurodacförordningen och kräver inget krisbeslut. Den står därför i den ordinarie tabellen.

## Förkortningar

Frister som blir **kortare** än den ordinarie fristen när ett villkor är uppfyllt. Sorterade efter livscykeln. Krisförordningen innehåller inga förkortningar.

| # | Status | Processlista - start * | Processlista stopp * | Kortnamn * | Villkor * | Tidsfrist * (dag/veckor/månad) | Aktivitet - start | Aktivitet - stopp | Flöde - start | Händelse - start | Flöde - stopp | Händelse - stopp | Typ * |
|---|--------|------------------------|----------------------|------------|-----------|-------------------------------|-------------------|-------------------|---------------|------------------|---------------|------------------|-------|
| FK1 | | Screening | Screening | Screening efter mer än 72 timmar vid gränsen (Screening 8.3) | Person som omhändertagits vid irreguljär gränspassage (art. 5.1 a) och som fysiskt uppehållit sig vid den yttre gränsen i mer än 72 timmar. Screeningen genomförs därefter. Gäller direkt | 7 dagar → 4 dagar | | | | | | | Förkortning |
| FK2 | | Registrering | Registrering | Inlämnande i gränsförfarandet (APR 51.1) | Ansökan prövas i gränsförfarandet och sökanden ges en faktisk möjlighet att lämna in. Missad frist hindrar inte gränsförfarandet | 21 dagar → 5 dagar från första registreringen (efter omfördelning: från ankomsten till omfördelningsstaten) | | | | | | | Förkortning |
| FK3 | | Eurodac | Ansvar | Framställan om övertagande efter träff (AMMR 39.1 andra st.) | Träff i Eurodac på uppgifter enligt Eurodac art. 22 eller 24, eller träff i VIS. Missas fristen blir den registrerande staten ansvarig | 2 månader från registreringen → 1 månad från träffen | | | | | | | Förkortning |
| FK4 | | Ansvar | Ansvar | Svar på framställan efter träff (AMMR 40.2) | Framställan grundas på träff i Eurodac (art. 22 eller 24) eller VIS | 1 månad → 2 veckor | | | | | | | Förkortning |
| FK5 | | Registrering | Ansvar | Framställan / avisering vid förvar (AMMR 45.1 första st.) | Personen tas i förvar enligt art. 44 | 2 månader (övertagande) / 2 veckor (återtagande) → 2 veckor från registreringen, eller från Eurodac-träffen om ingen ny ansökan registrerats | | | | | | | Förkortning |
| FK6 | | Ansvar | Ansvar | Framställan / avisering vid senare förvar (AMMR 45.1 andra st.) | Personen tas i förvar senare än vid registreringen | → 1 vecka från dagen för förvarstagandet | | | | | | | Förkortning |
| FK7 | | Ansvar | Ansvar | Svar på framställan vid förvar (AMMR 45.2) | Personen hålls i förvar. Uteblivet svar inom en vecka räknas som godtagande | 1 månad → 1 vecka | | | | | | | Förkortning |
| FK8 | | Ansvar | Ansvar | Överföring vid förvar (AMMR 45.3 a) | Personen hålls i förvar. Passeras fristen ska personen friges, men art. 46 gäller fortsatt (45.4) | 6 månader → 5 veckor från godtagandet eller bekräftelsen | | | | | | | Förkortning |
| FK9 | | Ansvar | Ansvar | Bilateral överenskommelse (AMMR 53.1 b) | Medlemsstaterna har ingått en bilateral administrativ överenskommelse som förkortar fristerna för att översända och granska framställningar och aviseringar | Enligt överenskommelsen | | | | | | | Förkortning |
| FK10 | | Registrering | Asylförfarande | Upptagandeprövning, sen ansökan efter återvändandebeslut (APR 35.1 andra st., 38.1 e) | Sökanden har ett beslut om återvändande och ansökte först efter sju arbetsdagar från att beslutet mottogs, var informerad om konsekvenserna, och inga nya relevanta faktorer har framkommit | 2 månader → 10 arbetsdagar (startpunkt anges inte uttryckligen) | | | | | | | Förkortning |
| FK11 | | Registrering | Asylförfarande | Påskyndat prövningsförfarande (APR 35.3) | Någon av grunderna i art. 42.1 eller 42.3 är tillämplig | 6 månader → 3 månader från inlämnandet | | | | | | | Förkortning |
| FK12 | | Registrering | Gränsförfarande | Gränsförfarande, hela förfarandet (APR 51.2) | Ansökan prövas i gränsförfarandet. Prövning, begäran om att stanna kvar och överklagande ska rymmas inom perioden | 6 månader (prövning) → 12 veckor från registreringen, inklusive överklagande | | | | | | | Förkortning |
| FK13 | | Asylförfarande | Asylförfarande | Kortare överklagandefrist (APR 67.7 a) | Beslut att neka prövning, eller avslag som implicit återkallad, ogrundad eller uppenbart ogrundad när någon omständighet i art. 42.1 eller 42.3 gällde. Längden fastställs i nationell rätt | 2 veckor–1 månad → 5–10 dagar | | | | | | | Förkortning |
| FK14 | | Återvändande vid gräns | Återvändande vid gräns | Frivillig avresa (Return 4.5) | Beviljas bara på begäran, och inte vid risk för avvikande, avslag som uppenbart ogrundad i gränsförfarandet eller risk för allmän ordning eller säkerhet. Ger ingen rätt till inresa | Högst 15 dagar (återvändandedirektivet art. 7.1: 7–30 dagar) | | | | | | | Förkortning |

> FK11 och FK12 är egna förfaranden med egna frister snarare än förkortningar av en löpande frist. De står med eftersom fristen blir kortare än vid ordinarie prövning.
> FK14 jämför med återvändandedirektivet 2008/115/EG, som inte finns i `references/`. Uppgiften 7–30 dagar är inte kontrollerad mot direktivtexten.

## Domäner utan förlängning, frysning eller förkortning

| Domän | Varför |
|-------|--------|
| Screening inom territoriet | 3 dagar (Screening 8.4). Ingen förlängning eller förkortning |
| Asylförfarande, efterföljande ansökan | Inga egna förlängningar. Samma som rad 19–20 när ansökan tas upp |
| Asylförfarande, påskyndat förfarande och art. 38.1 e | 3 månader respektive 10 arbetsdagar (FK10, FK11) har ingen förlängningsgrund (APR art. 35) |
| Återvändande vid gräns (ordinarie läge) | 12 veckor har ingen förlängning utanför kris (K9) |
| Kris | Har inga egna frister. Förlänger frister i andra domäner (K1–K9) |

## Avgränsning (inte med i tabellerna)

- **Uppskjutanden och spärrar** är varken förlängning eller frysning: uppskjutande vid osäkra förhållanden (APR 35.7, max 21 månader), uppskjutande innan implicit återkallande (APR 41.4), spärr för överföring till krisstat (Kris 12.4) och domstolens beslut om uppskov (AMMR 43.3).
- **Gränsförfarandet för återvändande** startar när rätten att stanna kvar upphört (Return 4.2). Det är en senare startpunkt, inte en frysning.
- **Prövning i sak efter AMMR-överföring** räknas från inlämnandet i den ansvariga medlemsstaten (APR 35.6). Det anger var fristen startar, inte en ny startpunkt för en frist som redan löper.
- **Förhandstillämpning vid kris** (Kris 10.6, högst 10 dagar) avser när krisregeln får börja tillämpas, inte en frist som förlängs.

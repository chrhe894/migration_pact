---
tags:
  - förvar
  - beslutskoder
  - händelser
  - systemstöd
---

← [Förvar](README.md)

# Beslutskatalog och händelsematris

Sidan är underlaget för en **händelsestyrd** systemlösning. Varje beslut eller faktisk händelse i ett ärende är en **beslutshändelse (BH)**. Förvarsprocessen lyssnar på händelserna och avgör vad som händer med förvaret: om en grund startar, upphör eller byts, om en klocka startar, fryses eller nollställs, eller om personen ska friges.

Kolumnen **Kod** är till för verksamhetens egna beslutskoder och fylls i internt. En kod kan motsvara flera BH, och en BH kan ha flera koder.

---

## 1. Förvarsgrunder (FG)

Varje förvarsbeslut har **en** grund. Grunden bestämmer längsta tid, prövningsintervall och domstolsfrist. Där andra sidor skriver FG-09 avses både FG-09a och FG-09b.

| FG | Grund | Lagrum (nuvarande / från 1 dec 2027) | Vem | Längsta tid | Ny prövning | Domstol | Beslutar | Kod |
|----|-------|---------------------------------------|-----|-------------|-------------|---------|----------|-----|
| FG-01 | Sökande: bestämma eller bekräfta identitet/nationalitet | 10:3 1 st. 1 / 10:5 | Vuxen sökande | **4 veckor** | — | **15 dagar** (21) | MV | **ID** |
| FG-02 | Sökande: utreda grunderna för ansökan | 10:3 1 st. 2 / 10:5 | Vuxen sökande | **4 veckor** | — | 15 (21) | MV | **UTANS** |
| FG-03 | Sökande: inte följt boendebeslut + risk för avvikande | 10:3 1 st. 3 / 10:5 | Vuxen sökande | **12 månader** | **2 mån** | 15 (21) | MV | **BOSKYL** |
| FG-04 | Gränsförfarandet för asyl (APR art. 43) | 10:3 1 st. 4 / 10:5 | Vuxen sökande | **12 veckor** (+6 v vid kris) | 2 mån | 15 (21) | MV | **ASYLGR** |
| FG-05 | Ansökan i förvar för att försena verkställighet | 10:3 1 st. 5 / 10:5 | Vuxen sökande, redan i förvar enligt FG-09 | **12 månader** | 2 mån | 15 (21) | MV | **FHVERK** |
| FG-06 | Sökande: nationell säkerhet eller allmän ordning | 10:3 1 st. 6 / 10:5 | Vuxen sökande | **12 månader** | 2 mån | 15 (21) | MV | **SÄKORD** |
| FG-07 | Ansvarsförfarandet (AMMR art. 44) | 10:3 1 st. 7 / 10:5 | Sökande | AMMR art. 45: framställan 2 v (1 v), svar 1 v, beslut 2 v, **överföring 5 v** | 2 mån | 15 (21) | MV | **AMMR** |
| FG-08 | Ej sökande: utreda identitet eller rätt att resa in/stanna | 10:5 1 st. 1 / 10:7 | Vuxen | **4 veckor** | — | Skyndsamt | Polis/MV | **UTRED** |
| FG-09a | Avvisning eller utvisning **kan antas** + risk (prognosförvar) | 10:5 1 st. 2 / 10:7 | Vuxen | **6 mån + 12 mån**. EES-stat 6/12. Säkerhetsärende 12 + 12. Brottsutvisad: inget tak | 2 mån | Skyndsamt | Polis/Säpo/MV | **AVLÄGS** ⚠ |
| FG-09b | Beslut om avvisning eller utvisning **ska verkställas** + risk | 10:5 1 st. 2 / 10:7 | Vuxen | **6 mån + 12 mån**. EES-stat 6/12. Säkerhetsärende 12 + 12. Brottsutvisad: inget tak | 2 mån | Skyndsamt | Polis/Säpo/MV | **VERK** |
| FG-10 | Återvändandegränsförfarandet (förordning 2024/1349 art. 5) | 10:5 2 st. / 10:7 | Vuxen | Högst **tolvveckorsperioden** (+6 v vid kris). Räknas in i FG-09:s tak vid direkt följande förvar | 2 mån | Skyndsamt | Polis/MV | **ÅVGR** |
| FG-11 | Barn (sökande 10:4 eller övriga 10:6) | 10:4, 10:6 / 10:6, 10:8 | Barn | **72 h + 72 h**. Säkerhetsärende **3 mån** (6) sammanlagt | Säkerhet: **1 mån** | 15 (21) om sökande | Som ovan | Typ **INS-BARN** eller **UTL-BARN** + grundkod; **SANN** ⚠ är ren barngrund (10:6 1 st. 1) |
| FG-12 | Interimistiskt beslut av Polismyndigheten | 10:24 / 10:27 | Alla | Tills behörig myndighet beslutat (prövas omedelbart) | Räknas in i 2 mån | — | Polis | — (ingen grundkod) |
| UP-01 | Uppsikt (alternativ till förvar) | 10:1 / 10:1 | Alla | Ingen | **6 mån** | — | Som förvar | — (ej angiven) |
| UP-02 | Förstärkt uppsikt med elektronisk övervakning (från 1 dec 2027) | — / 10:2–3 | Alla | Barn 3 mån (6), säkerhet 12 (18) | **3 mån**, barn **1 mån** | — | Som förvar | — (ej angiven) |

### Beslutskoder för förvarsgrund

Verksamhetens koder anger **grunden** i ett förvarsbeslut (BH-03). ⚠ = tolkning av förkortningen, behöver bekräftas. Kolumnen RCD anger motsvarande led i [mottagandedirektivet (EU) 2024/1346](../../references/legislation/reception-directive.md) artikel 10.4 ([RULE-RCD-010-001](rules/rule-rcd-010-001.md)). Direktivet gäller bara sökande, så UTL-koderna och SANN saknar motsvarighet. Sökande barn (INS-BARN) får enligt artikel 13.2 tas i förvar bara undantagsvis, som en sista utväg.

!!! note "Ändrat innehåll"
    UTANS och FHVERK är nu markerade som säkra. 10:3 1 st. 1–7 motsvarar artikel 10.4 a–g i mottagandedirektivet, och övriga sex INS-koder täcker de andra punkterna.

| Kod | FG | Lagrum (nu) | RCD | Lagtextens formulering | Säkerhet |
|-----|----|-------------|-----|------------------------|----------|
| ID | FG-01 | 10:3 1 st. 1 | 10.4 a | "bestämma eller bekräfta utlänningens identitet eller nationalitet" | Säker |
| UTANS | FG-02 | 10:3 1 st. 2 | 10.4 b | "utreda de omständigheter som ansökan om internationellt skydd grundas på" | Säker. Enda INS-koden som återstår för 1 st. 2; motsvarar RCD 10.4 b |
| BOSKYL | FG-03 | 10:3 1 st. 3 | 10.4 c | Inte följt beslut om **boende** på bestämd plats + risk för avvikande | Säker (boendeskyldighet) |
| ASYLGR | FG-04 | 10:3 1 st. 4 | 10.4 d | Led i ett **gränsförfarande** enligt APR art. 43 | Säker |
| FHVERK | FG-05 | 10:3 1 st. 5 | 10.4 e | Ansökan gjord i förvar för att "**försena eller hindra verkställigheten**" | Säker. Samma ord i RCD 10.4 e (F + H + VERK) |
| SÄKORD | FG-06 | 10:3 1 st. 6 | 10.4 f | "nationella **säkerheten** eller för att upprätthålla allmän **ordning**" | Säker |
| AMMR | FG-07 | 10:3 1 st. 7 | 10.4 g | "i enlighet med artikel 44 i asyl- och migrationshanteringsförordningen" | Säker |
| UTRED | FG-08 | 10:5 1 st. 1 | — | "en **utredning** av utlänningens identitet eller rätt att resa in i eller stanna i Sverige" | Säker |
| AVLÄGS | FG-09a | 10:5 1 st. 2, första ledet | — | "det **kan antas** att utlänningen kommer att avvisas eller utvisas" | ⚠ Tolkat som prognosförvar inför **avlägsnande** |
| VERK | FG-09b | 10:5 1 st. 2, andra ledet | — | "det är fråga om att **verkställa** ett beslut om avvisning eller utvisning" | Säker |
| ÅVGR | FG-10 | 10:5 2 st. | — | Förvar enligt art. 5 i förordningen om **återvändandegränsförfarande** | Säker |
| SANN | FG-11 | 10:6 1 st. 1 (barn) | — | "det är **sannolikt** att barnet kommer att avvisas av Polismyndigheten eller avvisas med omedelbar verkställighet av Migrationsverket" | ⚠ Ordet "sannolikt" finns bara i barnparagrafen |

**FG-09a och FG-09b** har samma lagrum, tak (6 + 12 månader, 10:12) och prövning (2 månader), men olika utlösande händelser. AVLÄGS används **innan** ett verkställbart beslut finns, VERK **när** det finns. När beslutet blir verkställbart (BH-14) bör koden bytas från AVLÄGS till VERK.

### Beslutstyper

Beslutstypen anger **vilken paragraf** i 10 kap. som är tillämplig: personens status (sökande eller inte) och ålder. Grundkoden anger **vilken punkt** i paragrafen.

| Typ | Betydelse | Lagrum (nu / från 1 dec 2027) | Rubrik i lagen |
|-----|-----------|-------------------------------|----------------|
| INS | Sökande av **internationellt skydd**, vuxen | 10:3 / 10:5 | Uppsikt över och förvar av en utlänning som är sökande av internationellt skydd |
| INS-BARN | Sökande av internationellt skydd, barn | 10:4 / 10:6 | Samma |
| UTL | **Utlänning** som inte är sökande, vuxen | 10:5 / 10:7 | Uppsikt över och förvar av en utlänning som inte är sökande av internationellt skydd |
| UTL-BARN | Utlänning som inte är sökande, barn | 10:6 / 10:8 | Samma |

Typen styr också tak och domstolsfrist: barntyperna har 72 + 72 timmar (10:13), och INS-typerna har domstolens 15 (21) dagar (16:4).

### Tillåtna kombinationer av typ och kod

Systemet kan validera att koden finns i den paragraf som typen anger.

| Kod | INS (10:3) | INS-BARN (10:4) | UTL (10:5) | UTL-BARN (10:6) |
|-----|:----------:|:---------------:|:----------:|:---------------:|
| ID | 1 st. 1 | — | — | — |
| UTANS | 1 st. 2 | — | — | — |
| BOSKYL | 1 st. 3 | p. 1 (**uppenbar** risk) | — | — |
| ASYLGR | 1 st. 4 | — | — | — |
| FHVERK | 1 st. 5 | — | — | — |
| SÄKORD | 1 st. 6 | p. 4 | — | — |
| AMMR | 1 st. 7 | p. 5 | — | — |
| UTRED | — | — | 1 st. 1 | — |
| AVLÄGS | — | — | 1 st. 2 (kan antas) | — |
| SANN | — | — | — | 1 st. 1 (sannolikt avvisning) |
| VERK | — | — | 1 st. 2 (verkställa) | 1 st. 2 (**uppenbar** risk) |
| ÅVGR | — | — | 2 st. | 2 st. |

Punkterna i 10:4 är numrerade 1, 4 och 5 i rättsdatabasernas text. Se [RULE-UTL-10-004-001](rules/rule-utl-10-004-001.md).

För barntyperna gäller dessutom att barnet inte får skiljas från vårdnadshavare (10:7) och att barn utan vårdnadshavare här får tas i förvar bara vid synnerliga skäl (10:8). Det tidigare förslaget att barn skulle markeras med ett eget attribut för ålder behövs inte: barntyperna gör det.

### Avslutskoder

| Kod | Betydelse | Lagrum | Händelser |
|-----|-----------|--------|-----------|
| UPPH | Beslutet **upphävs** genom ett aktivt beslut av myndighet eller domstol | 10:14 (skälen finns inte längre), 10:23 (uppehållstillstånd eller skydd beviljas), domstolens bifall | BH-04 (ersätts av uppsikt), BH-07 (bifall), BH-15, BH-25, BH-33, statusbyte utan ny grund (BH-14, BH-16) |
| FÖRFALLER | Beslutet **upphör att gälla** utan nytt beslut, direkt enligt lag | 10:19 (ny prövning inte i tid), 16:4 (domstolen avgör inte inom 21 dagar), 10:24 (interimistiskt beslut när behörig myndighet beslutat) | BH-44, BH-45, BH-03 efter interimistiskt beslut |

**Placeringsbeslut** (var personen placeras, t.ex. i kriminalvårdsanstalt) har en egen frist: ny prövning inom **en månad**, annars upphör beslutet att gälla (10 a kap. 16 §). Det är också ett FÖRFALLER-fall, men för placeringen, inte för förvaret. 10 a kap. är inte kartlagt ännu.

Tolkning: lagen använder just skillnaden mellan "upphäva" och "upphör att gälla", och koderna verkar följa den. Två fall är oklara och behöver bekräftas:

- **Taket nås (BH-43).** Lagen säger att utlänningen "får inte hållas i förvar längre tid än". Den säger inte att beslutet upphör att gälla. Förslag: **UPPH**, med ett beslut senast när taket nås.
- **Överföring eller avlägsnande genomförd (BH-26, BH-34).** Förvaret avslutas eftersom syftet är uppnått. Lagen har ingen uttrycklig regel. Förslag: **UPPH**, eller en egen kod om verksamheten har en.


**Grunder utan kod:** interimistiskt beslut (FG-12) har ingen egen grundkod. Det fattas på samma grunder och bör få typ och grundkod som ett vanligt beslut. Uppsikt (UP-01, UP-02) beslutas på samma grunder som förvar (10:3–6) och kan därför använda samma typer och koder; det som skiljer är **åtgärden** (uppsikt eller förvar), inte grunden.

**Koder och händelser.** Grundkoderna gäller förvarsbeslutet (BH-03, BH-05). Kolumnen *Kod* i händelsetabellen nedan avser **andra** beslut (avslag, överföring, uppehållstillstånd m.fl.) och är fortfarande tom.

Källor: [regler](README.md#regler). Från **17 oktober 2027** ersätts EU-ramen för FG-09 av förordning 2026/2280 art. 29–33 ([PROC-RTN-002](../../domains/return/processes/return-detention.md)).

---

## 2. Klockor (K)

En person i förvar kan ha flera klockor som löper samtidigt. Systemet behöver bevaka alla.

| K | Klocka | Startar | Stoppas / nollställs | Följd vid utgång | Regel |
|---|--------|---------|----------------------|------------------|-------|
| K1 | **Grundtak** (längsta tid per FG) | När förvaret med den grunden verkställs | Ny grund startar ny K1. Se [öppen fråga](open_questions/aggregation-of-detention-time.md) | Frigivning, eller förlängningsbeslut (FG-09: 6 → +12 mån) | [RULE-UTL-10-011-001](rules/rule-utl-10-011-001.md), [012](rules/rule-utl-10-012-001.md), [013](rules/rule-utl-10-013-001.md) |
| K2 | **Ny prövning** (2 mån; barn i säkerhetsärende 1 mån) | Verkställighet av förvarsbeslutet, eller av interimistiskt beslut | Ny prövning: räknas från senaste förvarsbeslutet | **Beslutet upphör** (10:19) | [RULE-UTL-10-016-001](rules/rule-utl-10-016-001.md), [017](rules/rule-utl-10-017-001.md), [019](rules/rule-utl-10-019-001.md) |
| K3 | **Domstolsfrist** (15 dagar, särskilda skäl 21) | Överklagandet kommer in till migrationsdomstolen (FG-01–07, FG-11 sökande) | Slutligt avgörande | Efter 21 dagar **upphör beslutet** | [RULE-UTL-16-004-001](rules/rule-utl-16-004-001.md) |
| K4 | **AMMR-klockor** (framställan 2 v/1 v, svar 1 v, beslut 2 v, överföring 5 v) | Registrering/Eurodac-träff/förvarstagande; mottagande; godtagande | Överföringsklockan **får ny startpunkt** när suspensiv verkan upphör | **Frigivning**; AMMR art. 39, 41, 46 fortsätter | [RULE-AMMR-045-001](../../domains/responsibility/rules/rule-ammr-045-001.md), [045-002](../../domains/responsibility/rules/rule-ammr-045-002.md) |
| K5 | **Total tid i förvar** (sammanhängande) | Första frihetsberövandet | Frigivning | Underlag för sammanräkning (barn i säkerhetsärende; 2024/1349 art. 5.4) | [RULE-UTL-10-013-001](rules/rule-utl-10-013-001.md), [RULE-RD-015-001](rules/rule-rd-015-001.md) |
| K6 | **Uppsikt** (6 mån; förstärkt 3 mån; barn förstärkt 1 mån) | Beslutsdagen | Ny prövning | **Beslutet upphör** | [RULE-UTL-10-015-001](rules/rule-utl-10-015-001.md) |
| K7 | **Tolvveckorsperioden** (2024/1349) | Rätten att stanna kvar upphör | — | Förvaret enligt FG-10 upphör; ev. nytt förvar enligt FG-09 | [RULE-RET-004-002](../../domains/return-border-procedure/rules/rule-ret-004-002.md), [RULE-RET-005-001](../../domains/return-border-procedure/rules/rule-ret-005-001.md) |

---

## 3. Beslutshändelser (BH) och deras effekt på förvaret

**Källprocess** anger var beslutet fattas. **Effekt** anger vad förvarsprocessen ska göra när händelsen kommer in. Händelsehanteringen beskrivs i [PROC-DET-002](processes/change-of-ground.md).

### Förvaret självt

| BH | Beslut / händelse | Kod | Källprocess | Effekt på förvar | Klockor | Regel |
|----|-------------------|-----|-------------|------------------|---------|-------|
| BH-01 | Omhändertagande enligt 11 § polislagen | *(fylls i)* | Polis | Inget förvar ännu; beslut om förvar ska fattas | — | [RULE-UTL-10-020-001](rules/rule-utl-10-020-001.md) |
| BH-02 | Interimistiskt beslut om förvar | *(fylls i)* | Polis | FG-12. Anmäls skyndsamt till behörig myndighet | K2 startar vid verkställighet; K5 startar | [RULE-UTL-10-020-001](rules/rule-utl-10-020-001.md) |
| BH-03 | Beslut om förvar (med FG) | *(fylls i)* | MV/Polis/Säpo | Sätter grund. Ersätter interimistiskt beslut | K1 (ny grund), K2; K5 om ej startad | [RULE-UTL-10-002-001](rules/rule-utl-10-002-001.md) |
| BH-04 | Beslut om uppsikt eller förstärkt uppsikt | *(fylls i)* | MV/Polis/Säpo | Alternativ till förvar (UP-01/UP-02). Ersätter förvar om det räcker | K6 | [RULE-UTL-10-015-001](rules/rule-utl-10-015-001.md) |
| BH-05 | Ny prövning av förvar (efter muntlig förhandling) | *(fylls i)* | MV/Polis/Säpo | Förvaret fortsätter eller upphävs | K2 räknas från detta beslut | [RULE-UTL-10-016-001](rules/rule-utl-10-016-001.md), [018](rules/rule-utl-10-018-001.md) |
| BH-06 | Överklagande av förvarsbeslut kommer in | *(fylls i)* | Domstol | — | K3 startar (sökande) | [RULE-UTL-16-004-001](rules/rule-utl-16-004-001.md) |
| BH-07 | Domstolens avgörande i förvarsmål | *(fylls i)* | Domstol | Bifall: frigivning. Avslag: fortsatt förvar | K3 stoppas | [RULE-UTL-16-004-001](rules/rule-utl-16-004-001.md) |
| BH-08 | Förlängning av FG-09 (bristande samarbete eller handlingar) | *(fylls i)* | Polis/MV | FG-09 fortsätter efter 6 mån, högst +12 | K1 förlängs | [RULE-UTL-10-012-001](rules/rule-utl-10-012-001.md) |

### Asylärendet

| BH | Beslut / händelse | Kod | Källprocess | Effekt på förvar | Klockor | Regel |
|----|-------------------|-----|-------------|------------------|---------|-------|
| BH-10 | Ansökan om internationellt skydd görs/registreras | *(fylls i)* | Registrering | Personen blir **sökande**: grunderna i 10:3 gäller. Är personen i förvar enligt FG-09 krävs nytt beslut (t.ex. FG-05) eller frigivning | Ny K1; K3 gäller | [RULE-UTL-10-003-001](rules/rule-utl-10-003-001.md) |
| BH-11 | Beslut att pröva i gränsförfarandet | *(fylls i)* | Gränsförfarande | FG-04 möjlig | K1 = 12 veckor | [RULE-UTL-10-011-001](rules/rule-utl-10-011-001.md) |
| BH-12 | Avslag med rätt att stanna kvar under överklagande (APR art. 68) | *(fylls i)* | Asylförfarande | Personen är **fortfarande sökande**. Grunden består | Oförändrade | [APR art. 68](../../domains/asylum-procedure/articles/apr-068.md) |
| BH-13 | Rätten att stanna kvar upphör efter avslag i gränsförfarandet | *(fylls i)* | Gränsförfarande | FG-04 upphör. Fortsatt förvar enligt **FG-10** (2024/1349 art. 5.2–5.3) kräver nytt beslut | K7 startar; ny K1 | [RULE-RET-005-001](../../domains/return-border-procedure/rules/rule-ret-005-001.md) |
| BH-14 | Avslag som får verkställas (laga kraft eller omedelbar verkställighet) | *(fylls i)* | Asylförfarande | Personen är **inte längre sökande**: 10:3-grunderna upphör. **Nytt beslut enligt FG-09** eller frigivning | Ny K1; K3 gäller inte längre | [RULE-UTL-10-005-001](rules/rule-utl-10-005-001.md), [RULE-UTL-10-014-001](rules/rule-utl-10-014-001.md) |
| BH-15 | Beviljat uppehållstillstånd eller internationellt skydd | *(fylls i)* | Asylförfarande / domstol | **Upphäv förvaret** i samma beslut | Alla stoppas | [RULE-UTL-10-023-001](rules/rule-utl-10-023-001.md) |
| BH-16 | Ansökan återkallas (uttryckligt eller implicit) | *(fylls i)* | Asylförfarande | Personen är inte längre sökande: som BH-14 | Ny K1 | [RULE-UTL-10-005-001](rules/rule-utl-10-005-001.md) |
| BH-17 | Efterföljande ansökan görs | *(fylls i)* | Asylförfarande | Rätt att stanna kvar kan saknas (APR art. 56). Har personen rätt att vistas som sökande: som BH-10 (ofta FG-05). Annars består FG-09 | Beroende på utfall | [RULE-APR-056-001](../../domains/asylum-procedure/rules/rule-apr-056-001.md) |

### Ansvarsförfarandet (AMMR)

| BH | Beslut / händelse | Kod | Källprocess | Effekt på förvar | Klockor | Regel |
|----|-------------------|-----|-------------|------------------|---------|-------|
| BH-20 | Eurodac-träff / beslut att inleda ansvarsförfarande | *(fylls i)* | Ansvar | FG-07 möjlig | K4: framställan inom 2 v (1 v om förvaret sker senare) | [RULE-AMMR-044-001](../../domains/responsibility/rules/rule-ammr-044-001.md) |
| BH-21 | Framställan om övertagande / avisering om återtagande skickad | *(fylls i)* | Ansvar | — | K4: svar inom 1 vecka | [RULE-AMMR-045-001](../../domains/responsibility/rules/rule-ammr-045-001.md) |
| BH-22 | Godtagande eller bekräftelse (även tyst) | *(fylls i)* | Ansvar | — | K4: beslut om överföring inom 2 v; **överföring inom 5 v** | [RULE-AMMR-045-001](../../domains/responsibility/rules/rule-ammr-045-001.md) |
| BH-23 | Beslut om överföring | *(fylls i)* | Ansvar | Grunden består (FG-07). Räknas som avlägsnandebeslut i mottagandelagen | — | [AMMR art. 42](../../domains/responsibility/articles/ammr-042.md) |
| BH-24 | Suspensiv verkan beviljad vid överklagande | *(fylls i)* | Domstol | Förvaret kan bestå | K4 överföring: **ny startpunkt** när suspensiv verkan upphör | [RULE-AMMR-045-002](../../domains/responsibility/rules/rule-ammr-045-002.md) |
| BH-25 | AMMR-frist missad (framställan, beslut eller överföring) | *(fylls i)* | Ansvar | **Frigivning** (AMMR 45.4). Ansvarsförfarandet fortsätter | Alla förvarsklockor stoppas | [RULE-AMMR-045-001](../../domains/responsibility/rules/rule-ammr-045-001.md) |
| BH-26 | Överföring genomförd | *(fylls i)* | Ansvar | Förvaret avslutas | Alla stoppas | — |

### Verkställighet och återvändande

| BH | Beslut / händelse | Kod | Källprocess | Effekt på förvar | Klockor | Regel |
|----|-------------------|-----|-------------|------------------|---------|-------|
| BH-30 | Ärendet lämnas över till Polismyndigheten för verkställighet | *(fylls i)* | Återvändande | **Beslutsfattare** för förvaret byts till Polis (10:20) | Oförändrade | [RULE-UTL-10-020-001](rules/rule-utl-10-020-001.md), [RULE-UTL-12-014-001](../../domains/return/rules/rule-utl-12-014-001.md) |
| BH-31 | Verkställighetshinder åberopas (12:19 b) | *(fylls i)* | Återvändande | Polis behåller behörighet tills MV beslutat om prövning. MV får besluta om **inhibition** av förvaret | — | [RULE-UTL-10-023-001](rules/rule-utl-10-023-001.md) |
| BH-32 | Inhibition av verkställigheten | *(fylls i)* | MV / domstol | Pröva om FG-09 fortfarande har skäl (10:14) | — | [RULE-UTL-10-014-001](rules/rule-utl-10-014-001.md) |
| BH-33 | Rimliga utsikter till avlägsnande saknas | *(fylls i)* | Återvändande | **Frigivning** (direktiv 2008/115/EG art. 15.4) | Alla stoppas | [RULE-RD-015-001](rules/rule-rd-015-001.md) |
| BH-34 | Avlägsnande genomfört (personen har lämnat landet) | *(fylls i)* | Återvändande | Förvaret avslutas. Beslutet verkställt (12:21) | Alla stoppas | [RULE-UTL-12-021-001](../../domains/return/rules/rule-utl-12-021-001.md) |
| BH-35 | Uppskjutande av avlägsnande (från 17 okt 2027) | *(fylls i)* | Återvändande | Åtgärder enligt art. 18, 23 och 29 får tillämpas om villkoren är uppfyllda | — | [RULE-RR-011-003](../../domains/return/rules/rule-rr-011-003.md) |

### Övriga händelser

| BH | Beslut / händelse | Kod | Källprocess | Effekt på förvar | Klockor | Regel |
|----|-------------------|-----|-------------|------------------|---------|-------|
| BH-40 | Personen fyller 18 år, eller åldersbedömning visar vuxen/barn | *(fylls i)* | Alla | Barnregler (FG-11) börjar eller upphör att gälla. Nytt beslut | Ny K1 | [RULE-UTL-10-013-001](rules/rule-utl-10-013-001.md) |
| BH-41 | Rörelsefriheten inskränks enligt annan lag (t.ex. LVU, smittskydd) | *(fylls i)* | Annan myndighet | Beslut får fattas men verkställs när förutsättningarna är uppfyllda (10:9) | — | Utlänningslagen 10 kap. 9–10 §§ |
| BH-42 | Rådets genomförandebeslut om kris | *(fylls i)* | EU | FG-04 och FG-10: tak +6 veckor (kris art. 11.1, 2024/1349 art. 6) | K1/K7 förlängs | [RULE-RET-006-001](../../domains/return-border-procedure/rules/rule-ret-006-001.md) |
| BH-43 | Grundtak (K1) nås | *(fylls i)* | Systemet | Frigivning, eller förlängning (BH-08) om tillåtet | — | [RULE-UTL-10-011-001](rules/rule-utl-10-011-001.md) |
| BH-44 | Frist för ny prövning (K2) passeras | *(fylls i)* | Systemet | **Beslutet upphör** (10:19) | — | [RULE-UTL-10-019-001](rules/rule-utl-10-019-001.md) |
| BH-45 | Domstolsfrist 21 dagar (K3) passeras | *(fylls i)* | Systemet | **Beslutet upphör** (16:4) | — | [RULE-UTL-16-004-001](rules/rule-utl-16-004-001.md) |

---

## Principer för systemlösningen

1. **Förvarsperiod och förvarsbeslut är olika saker.** En sammanhängande förvarsperiod (K5) kan bestå av flera beslut med olika grunder. Lagra dem separat.
2. **Varje beslut i ett annat ärende är en händelse.** Händelsen skickas till förvarsprocessen, som avgör om grunden fortfarande gäller (10:14). Händelser utan effekt loggas ändå.
3. **Statusbyte kräver nytt beslut.** När personen slutar vara sökande (BH-14, BH-16) upphör 10:3-grunderna. Förvaret får inte fortsätta på den gamla grunden.
4. **Klockor räknas per beslut och per grund.** Systemet ska varna i god tid före K1, K2, K3 och K4, eftersom flera av dem har automatisk rättsföljd (beslutet upphör eller personen ska friges).
5. **Beslutsfattaren följer ärendet.** När ärendet byter myndighet (BH-30) byter också förvaret beslutsfattare.
6. **Datum för tillämplighet.** Varje FG och regel anger från när den gäller. Från 1 december 2027 ändras paragrafnumren. Från 17 oktober 2027 gäller förordning 2026/2280 för återvändandeförvar.

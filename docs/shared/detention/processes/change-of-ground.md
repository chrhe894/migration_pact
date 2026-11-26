---
tags:
  - förvar
  - process
  - händelser
  - systemstöd
---

← [Förvar](../README.md)

# PROC-DET-002

# Händelsehantering och byte av förvarsgrund

## Trigger

En **beslutshändelse** (BH) kommer in från en annan process medan personen är i förvar eller under uppsikt. Exempel: avslag, överföringsbeslut, godtagande från annan medlemsstat, suspensiv verkan, beviljat uppehållstillstånd, överlämnande till Polismyndigheten.

---

## Resultat

Förvaret är oförändrat, har fått ny grund genom ett nytt beslut, har fått nya klockor, har fått ny beslutsfattare, eller har upphävts.

---

## Varför processen behövs

Förvarsgrunderna i utlänningslagen hänger på personens **status**. 10:3 gäller bara "under den tid som utlänningen har rätt att vistas i Sverige i egenskap av sökande av internationellt skydd". När statusen ändras genom ett beslut i ett annat ärende kan förvaret inte fortsätta på den gamla grunden. Det måste upphävas omedelbart (10:14) eller ersättas av ett nytt beslut med en annan grund.

---

## Flöde

<object type="image/svg+xml" data="../diagrams/detention-event-handling.svg" width="100%"></object>

Källa: [`detention-event-handling.pu`](../diagrams/detention-event-handling.pu)

Tillstånd och övergångar:

<object type="image/svg+xml" data="../diagrams/detention-states.svg" width="100%"></object>

Källa: [`detention-states.pu`](../diagrams/detention-states.pu)

---

## Steg

| # | Steg | Regel |
|---|------|-------|
| 1 | Ta emot händelsen med beslutskod och mappa den till BH | [Beslutskatalog](../decision-catalogue.md#3-beslutshandelser-bh-och-deras-effekt-pa-forvaret) |
| 2 | Hämta pågående förvar: förvarsperiod, aktuellt beslut, FG, beslutsfattare och klockor | — |
| 3 | **Upphävandehändelse?** Beviljat tillstånd eller skydd, missad AMMR-frist, inga utsikter till avlägsnande, bifall i domstol: upphäv omedelbart och gå till [PROC-DET-004](release.md) | [RULE-UTL-10-014-001](../rules/rule-utl-10-014-001.md), [RULE-UTL-10-023-001](../rules/rule-utl-10-023-001.md) |
| 4 | **Statusbyte?** Pröva om skäl finns enligt en ny grund. Fatta i så fall nytt beslut och starta ny K1 och K2. Annars frigivning eller uppsikt | [RULE-UTL-10-003-001](../rules/rule-utl-10-003-001.md), [RULE-UTL-10-005-001](../rules/rule-utl-10-005-001.md) |
| 5 | **Klockhändelse?** Starta, förläng eller ge ny startpunkt | [Klockor](../decision-catalogue.md#2-klockor-k) |
| 6 | **Myndighetsbyte?** Ny beslutsfattare för förvaret | [RULE-UTL-10-020-001](../rules/rule-utl-10-020-001.md) |
| 7 | Uppdatera bevakning och logga händelsen | — |

---

## Kodbyten vid händelser

När en händelse ändrar grunden ska förvarsbeslutet få en ny grundkod ([beslutskoder](../decision-catalogue.md#beslutskoder-for-forvarsgrund)). Varje byte kräver ett nytt beslut.

| Från typ / kod | Händelse | Till typ / kod | Kommentar |
|----------------|----------|----------------|-----------|
| UTL / AVLÄGS | BH-14 avslaget får verkställas | UTL / VERK | Samma lagrum och tak (10:5 1 st. 2, 10:12) |
| UTL / VERK | BH-10 ansökan om skydd i förvar, syfte att försena | INS / FHVERK | Personen blir sökande. Domstolsfristen 15 (21) dagar gäller |
| UTL / UTRED | BH-10 ansökan om skydd | INS / ID, UTANS m.fl. | Personen blir sökande |
| UTL / UTRED | Beslut om avvisning | UTL / AVLÄGS eller VERK | — |
| INS / alla koder | BH-14, BH-16 personen är inte längre sökande | UTL / VERK (eller AVLÄGS) | 10:3-grunderna upphör |
| INS / ASYLGR | BH-13 rätten att stanna kvar upphör | UTL / ÅVGR | Förordning 2024/1349 art. 5.2–5.3 |
| UTL / ÅVGR | Tolvveckorsperioden slut (K7) | UTL / VERK | Tiden i ÅVGR räknas in i takets 6 + 12 mån (2024/1349 art. 5.4) |
| INS / AMMR | BH-25 AMMR-frist missad | — / **UPPH** | Frigivning |
| INS-BARN / BOSKYL, SÄKORD, AMMR | BH-14, BH-16 barnet är inte längre sökande | UTL-BARN / VERK eller SANN | Barnreglerna fortsätter |
| INS-BARN, UTL-BARN / valfri | BH-40 barnet fyller 18 | INS eller UTL / motsvarande kod | Barnreglerna upphör. Pröva att koden finns i vuxenparagrafen |
| Valfri | Ny prövning sker inte i tid (BH-44) | — / **FÖRFALLER** | Beslutet upphör att gälla (10:19) |
| INS, INS-BARN / valfri | Domstolen avgör inte inom 21 dagar (BH-45) | — / **FÖRFALLER** | 16:4 |
| Valfri | Skälen faller bort, tillstånd beviljas, domstolen bifaller | — / **UPPH** | 10:14, 10:23 |

Varje byte av typ eller grundkod kräver ett **nytt beslut**. Kontrollera kombinationen mot [tillåtna kombinationer](../decision-catalogue.md#tillatna-kombinationer-av-typ-och-kod).

---

## Scenarier

### Scenario A: ansvarsförfarandet (Dublin)

| Dag | Händelse | Effekt |
|-----|----------|--------|
| 0 | BH-10 ansökan, BH-20 Eurodac-träff, BH-03 förvar FG-07 | K4: framställan inom **2 veckor**. K2 ny prövning inom 2 mån. K3 om överklagande |
| 10 | BH-21 framställan skickad | K4: svar inom **1 vecka**, annars tyst godtagande |
| 17 | BH-22 godtagande (tyst) | K4: beslut om överföring inom **2 veckor**, överföring inom **5 veckor** |
| 20 | BH-23 beslut om överföring | Grunden består |
| 25 | BH-24 suspensiv verkan beviljad | K4 överföring: räknas från dagen då suspensiv verkan upphör |
| 50 | BH-07 domstolen avslår överklagandet | Ny 5-veckorsfrist för överföring startar |
| 70 | BH-26 överförd | Förvaret avslutas |

Missas någon K4-frist: BH-25 och **frigivning**. Ansvarsförfarandet fortsätter med ordinarie frister.

### Scenario B: gränsförfarande till återvändande

| Händelse | Effekt |
|----------|--------|
| BH-11 + BH-03 förvar FG-04 | K1: högst **12 veckor** |
| Avslag med rätt att stanna kvar under överklagande (BH-12) | Ingen ändring, personen är fortfarande sökande |
| BH-13 rätten att stanna kvar upphör | FG-04 upphör. **Nytt beslut** FG-10 enligt 2024/1349 art. 5.2 (person som hölls i förvar under gränsförfarandet). K7: tolvveckorsperioden startar |
| Tolvveckorsperioden slut utan avlägsnande | FG-10 upphör. Fortsatt förvar kräver nytt beslut FG-09. **Tiden i FG-10 räknas in** i takets 6 + 12 månader (2024/1349 art. 5.4) |

### Scenario C: ansökan om skydd i förvar inför verkställighet

| Händelse | Effekt |
|----------|--------|
| BH-03 förvar FG-09 inför verkställighet | K1: 6 månader. K2: 2 mån |
| BH-10 personen ansöker om skydd | Personen blir sökande. Förvar på FG-09 kan inte fortsätta. **Nytt beslut** FG-05 om syftet antas vara att försena verkställigheten, annars annan grund eller frigivning. K3: domstol 15 (21) dagar gäller nu |
| BH-14 avslag som får verkställas | Personen är inte längre sökande. **Nytt beslut** FG-09 eller frigivning |
| BH-30 ärendet lämnas till Polismyndigheten | Polisen blir beslutsfattare för förvaret |
| BH-34 avlägsnad | Förvaret avslutas |

### Scenario D: beviljat tillstånd

| Händelse | Effekt |
|----------|--------|
| BH-15 uppehållstillstånd eller skydd beviljas | Migrationsverket (eller domstolen) **upphäver förvaret i samma beslut** (10:23). Alla klockor stoppas |

---

## Öppet

Om ett nytt beslut med ny grund startar en **ny** tvåmånadersperiod för ny prövning, och om tiden med olika grunder ska **räknas samman** mot taken, framgår inte entydigt av lagen. Se [öppen fråga](../open_questions/aggregation-of-detention-time.md).

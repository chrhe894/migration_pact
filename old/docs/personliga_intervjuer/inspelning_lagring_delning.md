# Inspelning, lagring och delning

## Källgrund

- Förordning (EU) 2024/1348, särskilt artikel 14.
- Direktiv 2013/32/EU, särskilt artikel 17.
- Lokal ny källa: `ref_material/OJ_L_202401348_SV_TXT.pdf`.
- Kompletterande vägledning: EUAA, `Practical Guide on the Audio Recording of Personal Interviews`, oktober 2025.

## Livscykel för ljudfilen

| Steg | Vad behöver hända? | Systemfrågor |
| --- | --- | --- |
| 1. Planering | Systemet avgör att intervjun omfattas av krav på ljudinspelning. | Är intervjutypen rätt klassad? Finns undantag? Finns särskilda processuella garantier? |
| 2. Förhandsinformation | Sökanden informeras om att intervjun spelas in och varför. | Var dokumenteras att information har lämnats? På vilket språk? Med tolk? |
| 3. Start av inspelning | Ljudinspelning startas och kopplas till rätt ärende, person och intervjutillfälle. | Hur förhindras felkoppling till fel ärende? Finns teknisk kontroll före intervjun? |
| 4. Genomförande | Intervjun genomförs med ljudupptagning under sekretess. | Hur hanteras paus, avbrott, tolkbyte, tekniskt fel eller flera ljudspår? |
| 5. Avslut | Inspelningen stoppas, sparas och låses mot otillåten ändring. | Finns checksummor, tidsstämpel och metadata? |
| 6. Aktföring | Inspelningen inkluderas i sökandens akt tillsammans med rapport eller transkript. | Hur visas relationen mellan ljudfil, rapport/transkript och beslut? |
| 7. Kommentar/förtydligande | Sökanden får möjlighet att kommentera eller förtydliga fel i rapport eller transkript. | Hur hanteras tidsfrist, inkomna kommentarer och beslut om korrigering? |
| 8. Åtkomst före beslut | Rapport eller transkript görs tillgängligt så snart som möjligt och i tid före beslut. | Vilka roller får läsa? Hur loggas åtkomst? |
| 9. Överklagande | Inspelningen görs tillgänglig i överklagandeförfarandet. | Hur delas ljudfilen säkert med domstol, ombud eller annan behörig aktör? |
| 10. Bevarande/gallring | Ljudfilen bevaras eller gallras enligt tillämpliga arkiv- och dataskyddsregler. | Vilken gallringsfrist gäller? Vad händer vid överklagande, återförvisning eller nytt ärende? |

## Kravområden

### Metadata

Ljudfilen bör minst kunna kopplas till:

- ärende-id
- person-id eller motsvarande aktkoppling
- intervjutyp
- datum och tid
- intervjuare
- tolk
- språk
- plats eller distansformat
- teknisk status
- version eller kompletterande fil om inspelningen avbryts och återupptas

### Integritet och säkerhet

Ljudfilen innehåller mycket känsliga personuppgifter. Systemstödet behöver därför hantera:

- behörighetsstyrning
- åtkomstloggning
- kryptering vid lagring och överföring
- skydd mot ändring eller radering utan stöd i regelverk
- säker delning med behöriga mottagare
- incidenthantering vid felaktig åtkomst eller förlorad inspelning

### Kvalitet och robusthet

Eftersom ljudinspelningen kan få företräde vid tvivel om vad sökanden sagt behöver systemet stödja:

- kontroll av mikrofon och ljudnivå före start
- markering av tekniska avbrott
- möjlighet att hantera flera filer för samma intervju
- tydlig status: inspelad, delvis inspelad, misslyckad, ersatt, delad
- manuell avvikelsehantering när inspelning inte kunnat göras

### Delning

Delning bör skilja mellan minst tre situationer:

| Situation | Primärt objekt | Kommentar |
| --- | --- | --- |
| Före beslut | Rapport eller transkript | Ska ges så snart som möjligt efter intervjun och i tid före beslut. |
| Kommentar/förtydligande | Rapport, transkript eller transkript av inspelning | Sökanden ska kunna påtala fel eller missförstånd. |
| Överklagande | Ljudinspelning | Åtkomst till inspelningen ska ges i överklagandeförfarandet. |

## Tillfällig fysisk överföring via USB och post

Om tillfälliga tekniska svårigheter gör att ljudfilen inte kan skickas via säkra digitala kanaler och verksamheten i stället måste använda USB-minne och postgång, bör det hanteras som ett undantagsförfarande med förhöjd risk. Det är inte bara ett annat leveranssätt, utan en ny behandling och transportkedja för mycket känsligt material.

### Huvudsakliga implikationer

| Område | Implikation | Rekommenderad kontroll |
| --- | --- | --- |
| Konfidentialitet | USB-minnet kan tappas bort, stjälas, skickas fel eller öppnas av obehörig. | Kryptera filen eller hela USB-minnet innan det lämnar myndighetens kontroll. |
| Spårbarhet | Digital kanal kan normalt ge tydligare loggar än fysisk post. | Registrera vem som skapat kopian, tidpunkt, mottagare, försändelse-id och kvittens. |
| Integritet | Det måste gå att visa att ljudfilen inte ändrats under transport. | Skapa checksumma eller annan integritetskontroll före utskick och kontrollera vid mottagande. |
| Tillgänglighet | Postgång kan fördröjas, och förlorad försändelse kan påverka tidsfrister i beslut eller överklagande. | Använd spårbar försändelse, bevaka tidsfrist och ha rutin för förlorad eller försenad försändelse. |
| Dataminimering | USB-minnet kan råka innehålla mer än den aktuella ljudfilen. | Använd tomt dedikerat USB-minne och lägg endast de filer som ska lämnas ut. |
| Behörighet | Fel mottagare kan få fysisk tillgång till materialet. | Kontrollera mottagaridentitet och adress före utskick. Kräv kvittens vid mottagande. |
| Incidentrisk | Förlorad okrypterad USB med känsliga personuppgifter kan vara personuppgiftsincident. | Ha färdig incidentrutin och bedöm anmälan till IMY inom 72 timmar vid förlust eller obehörig åtkomst. |
| Gallring/destruktion | Extra kopior kan bli kvar på USB-minne eller i temporära arbetsytor. | Kräv återlämning eller säker destruktion och dokumentera när kopian raderats. |

### Kan man kryptera en USB-sticka?

Ja. För den här typen av material bör USB-minnet inte skickas okrypterat. Det finns två huvudsakliga sätt:

1. Kryptera hela USB-minnet, till exempel med en godkänd lösning för flyttbar media eller hårdvarukrypterad USB.
2. Kryptera själva ljudfilen eller lägga den i en krypterad behållare innan den kopieras till USB-minnet.

Förfarandet bör minst uppfylla detta:

- använd stark, etablerad kryptering
- lösenord eller nyckel ska skickas i separat kanal, aldrig i samma brev som USB-minnet
- lösenordet ska vara tillräckligt långt och unikt för försändelsen
- mottagaren ska ha instruktioner för hur filen öppnas
- försändelsen ska vara spårbar
- utlämnandet ska dokumenteras i ärendet
- mottagaren ska kvittera mottagande och åtkomst
- USB-minnet ska återlämnas eller förstöras enligt dokumenterad rutin

### Miniminivå för ett undantagsförfarande

| Steg | Krav |
| --- | --- |
| Beslut om undantag | Dokumentera varför säker digital kanal inte kan användas och vem som godkänt undantaget. |
| Förbered USB | Använd dedikerad tom media, kopiera endast aktuell ljudfil och kryptera innan utskick. |
| Nyckelhantering | Skicka lösenord/nyckel separat, exempelvis via telefon till verifierad mottagare eller annan godkänd kanal. |
| Transport | Använd spårbar post eller kurir med kvittens. |
| Mottagning | Mottagaren verifierar försändelsen, kontrollerar att filen går att öppna och bekräftar mottagande. |
| Efterarbete | Dokumentera utlämnande, kvittens, eventuell återlämning/destruktion och radering av temporära kopior. |
| Incident | Vid förlust, fel mottagare, trasig media eller misstänkt åtkomst: hantera som möjlig personuppgiftsincident. |

### Bedömning

Fysisk USB-överföring kan vara möjlig som tillfälligt reservförfarande, men bör inte beskrivas som en normal säker kanal. Den bör vara tidsbegränsad, beslutad, dokumenterad och krypterad. Okrypterad USB med ljud från asylintervjuer bör betraktas som olämpligt eftersom ljudfilen kan innehålla känsliga personuppgifter, skyddsskäl, uppgifter om tredje person och uppgifter som kan påverka sökandens säkerhet.

## Om USB-minnet försvinner på vägen

Om ett USB-minne med ljudinspelning försvinner under postgång eller transport är det en säkerhetsincident. Om USB-minnet innehåller personuppgifter innebär förlusten normalt att organisationen måste bedöma om det också är en personuppgiftsincident enligt GDPR.

En personuppgiftsincident kan bestå av förlust, obehörigt röjande eller obehörig åtkomst till personuppgifter. En försvunnen USB-sticka med asylintervju är därför allvarlig även om man inte vet att någon faktiskt har öppnat filen.

### Skillnad mellan krypterad och okrypterad USB

| Situation | Trolig bedömning | Praktisk innebörd |
| --- | --- | --- |
| Okrypterad USB försvinner | Mycket sannolikt personuppgiftsincident med risk eller hög risk för den registrerade. | Snabb intern eskalering, dokumentation, riskbedömning, sannolikt anmälan till IMY inom 72 timmar och eventuell information till berörda personer. |
| Krypterad USB försvinner, stark kryptering och separat nyckel | Fortfarande säkerhetsincident och ska dokumenteras, men risken för obehörig åtkomst kan vara låg om nyckeln inte röjts. | Riskbedömning krävs. IMY-anmälan kan eventuellt bedömas inte behövas, men beslutet måste kunna motiveras och dokumenteras. |
| Krypterad USB försvinner tillsammans med lösenord eller nyckel | Bör behandlas nära okrypterad förlust. | Sannolik anmälningspliktig personuppgiftsincident och eventuell information till registrerade. |
| Oklart om USB var krypterad eller vad den innehöll | Osäkerhet ökar risken. | Utred skyndsamt, utgå försiktigt tills motsatsen är visad och dokumentera bedömningen. |

### Vad innebär det för Migrationsverket?

Om Migrationsverket är den myndighet som skapat USB-kopian och skickat ljudfilen innebär en förlust typiskt att Migrationsverket behöver:

- aktivera intern incidentrutin och dataskyddsombud
- fastställa vilket ärende, vilka personer och vilka uppgifter som berörs
- kontrollera om USB-minnet var krypterat och om nyckeln skickats separat
- försöka spåra försändelsen och begränsa skadan
- dokumentera händelsen, tidslinjen, riskbedömningen och vidtagna åtgärder
- bedöma om incidenten ska anmälas till IMY inom 72 timmar från vetskap
- bedöma om den registrerade ska informeras utan onödigt dröjsmål
- informera domstolen om ljudfilen behövs i ett pågående mål och leveransen inte kan anses ha skett
- skapa en ny säker leverans om utlämnandet fortfarande behövs
- utreda om rutinen med USB och post behöver stoppas eller ändras

För Migrationsverket kan incidenten också få processuell betydelse. Om ljudfilen behövs i ett överklagande kan förlusten påverka tidsfrister, partsinsyn, domstolens handläggning och möjligheten att kontrollera vad som sagts vid intervjun.

### Vad innebär det för domstolen?

Domstolens roll beror på var i kedjan förlusten sker.

| Scenario | Möjlig konsekvens för domstolen |
| --- | --- |
| USB försvinner innan domstolen tagit emot den | Domstolen är främst mottagare som inte fått materialet. Domstolen behöver normalt registrera att material saknas och begära ny säker leverans, men incidentansvaret ligger typiskt hos avsändaren. |
| USB försvinner efter att domstolen tagit emot den | Domstolen behöver hantera incidenten inom sin egen organisation, inklusive dokumentation, riskbedömning och eventuell anmälan enligt tillämpliga dataskyddsregler. |
| Det är oklart var förlusten skett | Båda myndigheterna behöver samordna faktainsamling: avsändningsdatum, spårningsnummer, kvittenser, mottagningsrutiner och vem som senast hade kontroll över försändelsen. |

Domstolen kan också behöva bedöma processuella följder:

- om målet behöver anstå i väntan på ny ljudfil
- om parten eller ombudet har fått tillräcklig insyn
- om domstolen kan avgöra målet utan ljudfilen
- om en ny kopia behöver begäras från Migrationsverket
- om sekretess eller säkerhet kräver särskild hantering av den fortsatta kommunikationen

### Vem anmäler till IMY?

Utgångspunkten är att den personuppgiftsansvariga organisationen bedömer och anmäler sina egna personuppgiftsincidenter. Om Migrationsverket tappar kontrollen över USB-minnet före mottagande ligger bedömningen normalt hos Migrationsverket. Om domstolen tappar bort ett mottaget USB-minne ligger bedömningen normalt hos domstolen.

Om båda myndigheterna behandlar uppgifter i kedjan behöver de ändå samordna faktaunderlaget. Det viktiga är att incidenten inte faller mellan stolarna. Det bör finnas en utsedd ansvarig för att:

- fastställa när organisationen fick vetskap om incidenten
- starta 72-timmarsbedömningen
- avgöra om IMY-anmälan krävs
- avgöra om registrerade ska informeras
- dokumentera beslut även om anmälan inte görs

### Information till den registrerade

Om förlusten sannolikt innebär hög risk för den registrerades rättigheter och friheter ska den registrerade som utgångspunkt informeras utan onödigt dröjsmål. För en asylintervju kan hög risk vara särskilt relevant eftersom ljudfilen kan innehålla:

- skyddsskäl
- uppgifter om hälsa, religion, politisk uppfattning eller sexuell läggning
- uppgifter om familj eller andra tredje personer
- uppgifter som kan innebära risk vid röjande till ursprungsland, nätverk eller obehöriga
- röstidentifiering och andra indirekta identifierare

Om USB-minnet var starkt krypterat och nyckeln inte förlorats kan risken för faktisk obehörig åtkomst vara betydligt lägre. Även då behöver organisationen dokumentera varför den bedömer att information till registrerade inte krävs.

## Öppna frågor

- Ska sökanden kunna lyssna på ljudfilen via e-tjänst, på myndighetens plats eller via ombud?
- Ska ljudfilen exporteras, strömmas eller bara göras tillgänglig i ett säkert visnings-/lyssningsläge?
- Hur hanteras sekretess om intervjun innehåller uppgifter om familjemedlemmar eller tredje person?
- Ska transkribering vara obligatorisk i vissa situationer eller bara ett alternativ till rapport?
- Hur hanteras ljudinspelning vid tolkning på distans?
- Vilka nationella arkiv- och gallringsregler styr ljudfilens livslängd?
- Vilken teknisk lösning är godkänd för kryptering av flyttbar media?
- Vem får godkänna undantag från säker digital delning?
- Vem har personuppgiftsansvar under transporten mellan Migrationsverket och domstol?
- Vilken myndighet ska informera registrerade om USB-minnet försvinner?

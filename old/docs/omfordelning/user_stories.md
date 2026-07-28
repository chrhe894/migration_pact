# User stories: omfördelning

## Källgrund

- Ny reglering: Förordning (EU) 2024/1351, särskilt artikel 12, 13, 15, 56-69, 70-72 och bilaga I.
- Gammal reglering: Förordning (EU) nr 604/2013, Dublin III.
- Lokal ny källa: `ref_material/OJ_L_202401351_SV_TXT.pdf`.
- Officiella referenser:
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1351>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32013R0604>

## Kort slutsats

Den nya ordningen gör omfördelning till en del av en permanent solidaritetsmekanism. Det nya är inte bara att personer kan flyttas mellan medlemsstater, utan att detta kopplas till en årlig solidaritetspool, nationella utfästelseförfaranden, EU-solidaritetssamordnaren, tekniskt forum, tidsfriststyrda mellanstatliga kontroller, ansvarsövergång och Eurodacuppdatering.

Kravmässigt bör omfördelning delas upp i strategisk styrning, urval och matchning, säkerhetskontroll, informationsutbyte, tidsfrister, överföring, efterföljande ansvar, ansvarskompensation samt uppföljning/rapportering.

## User stories

| nr | Feature | Användarberättelse | System | Kommentar |
| --- | --- | --- | --- | --- |
| 1 | Visa solidaritetsroll | Som processägare vill jag se om Sverige i ett visst år är bidragande medlemsstat, gynnad medlemsstat eller båda, så att rätt process och rapportering aktiveras. | Styrning/rapportering | Artiklarna 56-57 och 70. |
| 2 | Hantera årlig solidaritetspool | Som styrningsansvarig vill jag kunna registrera den årliga solidaritetspoolen och Sveriges utfästelse, så att nationella åtaganden kan följas upp. | Styrning | Artiklarna 12, 13 och 57. |
| 3 | Välja solidaritetstyp | Som beslutsfattare vill jag kunna ange om Sveriges bidrag består av omfördelning, ekonomiskt bidrag, alternativ solidaritetsåtgärd eller kombination, så att åtagandet redovisas korrekt. | Styrning/ekonomi | Artikel 56.2 och 57. |
| 4 | Beräkna rättvis andel | Som analytiker vill jag kunna se Sveriges referensandel baserad på folkmängd och BNP, så att utfästelse kan jämföras med referensnyckeln. | BI/styrning | Artikel 66 och bilaga I. |
| 5 | Skapa omfördelningsärende | Som handläggare vill jag kunna skapa ett omfördelningsärende kopplat till solidaritetspoolen, så att individflödet kan spåras från urval till ankomst. | Ärendehantering | Artikel 67. |
| 6 | Identifiera omfördelningsbara personer | Som handläggare i gynnad medlemsstat vill jag kunna filtrera personer som kan bli aktuella för omfördelning, så att urvalet följer förordningen. | Ärendehantering | Artikel 67.3. |
| 7 | Utesluta vid säkerhetshot | Som säkerhetshandläggare vill jag kunna markera rimliga skäl att anse att personen utgör hot mot inre säkerhet, så att personen inte omfördelas. | Screening/säkerhet | Artikel 67.2 och 67.8-9. |
| 8 | Dokumentera meningsfull koppling | Som handläggare vill jag kunna registrera familje-, kultur- eller annan relevant koppling till medlemsstat, så att matchning kan beakta meningsfulla kopplingar. | Ärendehantering/matchning | Artikel 67.3-4. |
| 9 | Tydliggöra inget val av land | Som handläggare vill jag att systemet visar att uppgifter om kopplingar inte ger rätt att välja medlemsstat, så att kommunikationen till personen blir korrekt. | Kommunikation | Artikel 67.3. |
| 10 | Hålla ihop familj | Som handläggare vill jag att familjemedlemmar kopplas till samma omfördelningsmedlemsstat, så att familjer inte splittras i omfördelningsprocessen. | Person-/familjerelationer | Artikel 67.6. |
| 11 | Hantera samtycke för skyddsstatus | Som handläggare vill jag registrera skriftligt samtycke när en person med internationellt skydd ska omfördelas, så att omfördelning inte sker utan krävt samtycke. | Dokument/kommunikation | Artikel 67.4. |
| 12 | Informera berörd person | Som handläggare vill jag kunna dokumentera att personen informerats om omfördelningsförfarandet och relevanta skyldigheter, så att informationskravet kan visas i efterhand. | Kommunikation | Artikel 67.5. |
| 13 | Skicka standardformulär | Som handläggare vill jag kunna skapa och skicka standardformulär med relevanta uppgifter och handlingar till omfördelningsmedlemsstaten, så att kontrollen kan göras inom frist. | Integration/dokument | Artikel 67.7 och 67.14. |
| 14 | Granska inkommet ärende | Som handläggare i omfördelningsmedlemsstat vill jag kunna granska mottagna uppgifter och handlingar, så att Sverige kan bekräfta eller stoppa omfördelning enligt reglerna. | Ärendehantering | Artikel 67.8-9. |
| 15 | Boka säkerhetsintervju | Som handläggare vill jag kunna boka personlig intervju när Sverige vill kontrollera säkerhetsinformation, så att intervjun ryms inom svarstidsfristen. | Bokning/säkerhet | Artikel 67.8. |
| 16 | Bevaka svarfrist | Som handläggare vill jag att systemet bevakar enveckasfristen och möjlig två veckors förlängning, så att passivitet inte leder till oavsiktlig skyldighet att omfördela. | Fristmotor | Artikel 67.9. |
| 17 | Hantera tyst bekräftelse | Som processägare vill jag att systemet varnar när uteblivet svar kan anses som bekräftelse, så att ansvariga agerar innan fristen löper ut. | Fristmotor/eskalering | Artikel 67.9. |
| 18 | Fatta överföringsbeslut | Som handläggare i gynnad medlemsstat vill jag kunna fatta överföringsbeslut inom en vecka efter bekräftelse, så att överföringen kan ske inom förordningens tidsram. | Beslut/kommunikation | Artikel 67.10. |
| 19 | Underrätta före överföring | Som handläggare vill jag att systemet visar rätt underrättelsefrist för sökande respektive person med skyddsstatus, så att personen informeras i tid. | Kommunikation/fristmotor | Artikel 67.10. |
| 20 | Planera fysisk överföring | Som logistiksamordnare vill jag kunna planera överföring inom fyra veckor, så att omfördelningen genomförs i tid. | Logistik/mottagning | Artikel 67.11. |
| 21 | Registrera ankomst | Som mottagningshandläggare vill jag registrera om personen kommit fram eller inte infunnit sig, så att gynnad medlemsstat, asylbyrån och EU-solidaritetssamordnaren kan underrättas. | Mottagning/rapportering | Artikel 68.1. |
| 22 | Uppdatera ansvar efter omfördelning | Som ansvarshandläggare vill jag att systemet uppdaterar ansvarig medlemsstat efter omfördelning, så att fortsatt asylprövning sker i rätt medlemsstat. | Ansvarsmodul/Eurodac | Artikel 68.2-3 och 2024/1358 artikel 16. |
| 23 | Hantera efterföljande ansökan efter omfördelning | Som handläggare vill jag att systemet visar att ansvar för ytterligare framställningar och efterföljande ansökningar följer omfördelningsmedlemsstaten, så att fel medlemsstat inte handlägger ärendet. | Ärendehistorik | Artikel 68.3 och 2024/1348 artiklarna 55-56. |
| 24 | Bevilja motsvarande skyddsstatus | Som beslutsfattare vill jag att systemet stödjer automatisk motsvarande skyddsstatus när en person med internationellt skydd omfördelats, så att statusen inte omprövas felaktigt. | Beslut/mottagning | Artikel 68.4. |
| 25 | Hantera ansvarskompensation | Som ansvarig för solidaritetsbidrag vill jag kunna registrera att Sverige tar över ansvar för ett antal ansökningar i stället för omfördelningar, så att ansvarskompensation hålls isär från fysisk omfördelning. | Ansvarsmodul/styrning | Artikel 69. |
| 26 | Rapportera genomförande | Som rapporteringsansvarig vill jag kunna sammanställa genomförda, pågående och avbrutna solidaritetsåtgärder, så att Sverige kan underrätta kommissionen och EU-solidaritetssamordnaren. | Rapportering | Artikel 70. |
| 27 | Skydda känsliga uppgifter | Som dataskyddsansvarig vill jag att omfördelningsärenden har rollstyrd åtkomst och auditlogg, så att säkerhetsuppgifter, familjeuppgifter och skyddsskäl behandlas korrekt. | Behörighet/dataskydd | Artiklarna 72-73. |
| 28 | Följa ekonomiskt stöd | Som ekonomiansvarig vill jag kunna koppla omfördelning till relevant unionsfinansiering, så att ersättning och kostnader kan följas upp. | Ekonomi/styrning | Artikel 71 och förordning (EU) 2021/1147. |

## Frågor för fortsatt analys

- Vilka svenska verksamhetsdelar skulle äga styrning, individärende, mottagning, säkerhetskontroll och rapportering vid omfördelning?
- Behövs en separat ärendetyp för omfördelning, eller ska den modelleras som ett tillägg till asyl-/mottagningsärendet?
- Hur ska Sverige hantera inkommande omfördelningsärenden där svar uteblir och tyst bekräftelse kan uppstå?
- Vilka standardformulär och tekniska format kommer kommissionens genomförandeakter att fastställa?
- Hur ska Eurodacuppdatering kontrolleras när ansvar övergår efter omfördelning eller ansvarskompensation?
- Hur ska statistik skilja mellan omfördelning av sökande, omfördelning av personer med skyddsstatus och ansvarskompensation?

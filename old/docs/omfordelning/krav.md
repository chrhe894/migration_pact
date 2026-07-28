# Krav: omfördelning

## Källgrund

- Ny reglering: Förordning (EU) 2024/1351, särskilt artikel 12, 13, 15, 56-69, 70-72 och bilaga I.
- Kopplad reglering: Förordning (EU) 2024/1358, särskilt artikel 16 om ansvarig medlemsstat i Eurodac.
- Lokal ny källa: `ref_material/OJ_L_202401351_SV_TXT.pdf`.
- Officiell referens:
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1351>

## Läsanvisning

Detta är ett kravanalytiskt underlag, inte en slutlig rättsutredning. Kraven är härledda från de artikelhänvisningar som redan finns i `jamforelse.md`, `datapunkter.md` och `user_stories.md`. Varje krav bör kontrolleras mot den svenska EUT-texten och senare genomförandeakter innan det används som beslutsunderlag.

`Ska` används när kravet följer av en uttrycklig skyldighet, en rättsverkan eller en nödvändig systemförmåga för att kunna uppfylla förordningen. `Bör` används när funktionen inte nödvändigtvis är uttryckligen reglerad, men behövs för styrning, kvalitet, spårbarhet eller robust handläggning.

## Ska-krav

| ID | Krav | Rättslig grund | Område | Koppling till user stories |
| --- | --- | --- | --- | --- |
| OMF-SKA-001 | Systemet ska kunna hantera ett solidaritetsår och koppla omfördelningsåtgärder till relevant årlig solidaritetspool eller genomförandeakt. | Artiklarna 12, 57, 61-62 | Styrning | 1, 2, 5 |
| OMF-SKA-002 | Systemet ska kunna registrera medlemsstatens roll i processen: bidragande medlemsstat, gynnad medlemsstat och omfördelningsmedlemsstat. | Artiklarna 56-69 | Styrning/ärende | 1 |
| OMF-SKA-003 | Systemet ska kunna skilja omfördelning från ekonomiska bidrag, alternativa solidaritetsåtgärder och ansvarskompensation. | Artiklarna 56.2, 57, 69 | Styrning/rapportering | 3, 25, 26 |
| OMF-SKA-004 | Systemet ska kunna registrera Sveriges utfästelse eller mottagna solidaritetsstöd med antal, typ, år och status. | Artiklarna 13, 57, 70 | Styrning/rapportering | 2, 3, 26 |
| OMF-SKA-005 | Systemet ska kunna lagra eller visa referensandel enligt referensnyckeln, inklusive koppling till folkmängd och BNP. | Artikel 66 och bilaga I | BI/styrning | 4 |
| OMF-SKA-006 | Systemet ska kunna skapa ett individuellt omfördelningsärende kopplat till person, personkategori, solidaritetsår och berörda medlemsstater. | Artiklarna 56.2 a, 67 | Ärendehantering | 5 |
| OMF-SKA-007 | Systemet ska kunna ange om personen är sökande eller person som beviljats internationellt skydd, eftersom villkor och följder skiljer sig åt. | Artiklarna 56.2 a, 67, 68 | Ärendehantering | 6, 11, 19, 24 |
| OMF-SKA-008 | Systemet ska stödja bedömning av om en person kan bli aktuell för omfördelning enligt förordningens personkrets och urvalsregler. | Artikel 67 | Ärendeurval | 6 |
| OMF-SKA-009 | Systemet ska kunna dokumentera rimliga skäl att anse att personen utgör hot mot inre säkerhet och hindra att personen hanteras som omfördelningsbar när sådana skäl finns. | Artiklarna 67.2, 67.8-9 | Säkerhet | 7, 14 |
| OMF-SKA-010 | Systemet ska kunna registrera meningsfulla kopplingar, exempelvis familje-, kultur- eller andra relevanta kopplingar, utan att behandla detta som en rätt för personen att välja medlemsstat. | Artiklarna 67.3-4 | Matchning/kommunikation | 8, 9 |
| OMF-SKA-011 | Systemet ska kunna koppla familjemedlemmar så att de omfördelas till samma omfördelningsmedlemsstat när artikel 67.6 är tillämplig. | Artikel 67.6 | Personrelationer | 10 |
| OMF-SKA-012 | Systemet ska kunna registrera skriftligt samtycke innan en person med internationellt skydd omfördelas när sådant samtycke krävs. | Artikel 67.4 | Dokument/kommunikation | 11 |
| OMF-SKA-013 | Systemet ska kunna dokumentera att berörd person informerats om omfördelningsförfarandet och relevanta skyldigheter. | Artikel 67.5 | Kommunikation | 12 |
| OMF-SKA-014 | Systemet ska kunna skapa, ta emot och spåra standardformulär och relevanta handlingar mellan berörda medlemsstater. | Artiklarna 67.7, 67.13-14 | Integration/dokument | 13, 14 |
| OMF-SKA-015 | Systemet ska kunna stödja omfördelningsmedlemsstatens granskning av inkomna uppgifter och handlingar. | Artiklarna 67.8-9 | Ärendehantering | 14 |
| OMF-SKA-016 | Systemet ska kunna registrera och bevaka om omfördelningsmedlemsstaten begär ytterligare kontroll, inklusive personlig intervju där sådan används. | Artikel 67.8 | Säkerhet/bokning | 15 |
| OMF-SKA-017 | Systemet ska bevaka svarfrist för omfördelningsmedlemsstatens bekräftelse, inklusive huvudfrist om en vecka och möjlig förlängning till två veckor. | Artikel 67.9 | Fristmotor | 16 |
| OMF-SKA-018 | Systemet ska kunna hantera rättsverkan av uteblivet svar där tyst bekräftelse är tillämplig enligt artikel 67.9. | Artikel 67.9 | Fristmotor/ärende | 17 |
| OMF-SKA-019 | Systemet ska stödja beslut om överföring inom en vecka efter bekräftelse. | Artikel 67.10 | Beslut | 18 |
| OMF-SKA-020 | Systemet ska skilja underrättelsefrist för sökande från underrättelsefrist för person med internationellt skydd. | Artikel 67.10 | Kommunikation/frist | 19 |
| OMF-SKA-021 | Systemet ska kunna planera och bevaka fysisk överföring inom fyra veckor från bekräftelse eller från slutligt beslut när suspensiv verkan påverkar tidslinjen. | Artikel 67.11 | Logistik/frist | 20 |
| OMF-SKA-022 | Systemet ska kunna registrera om personen ankommit eller inte infunnit sig efter överföring. | Artikel 68.1 | Mottagning | 21 |
| OMF-SKA-023 | Systemet ska kunna skapa underrättelse om ankomst eller utebliven ankomst till berörda aktörer, inklusive gynnad medlemsstat, asylbyrån och EU-solidaritetssamordnaren där detta krävs. | Artikel 68.1 | Rapportering/integration | 21 |
| OMF-SKA-024 | Systemet ska kunna uppdatera ansvarig medlemsstat efter genomförd omfördelning när ansvaret övergår. | Artiklarna 68.2-3 | Ansvar | 22, 23 |
| OMF-SKA-025 | Systemet ska kunna samordna ansvarsövergång efter omfördelning med Eurodacuppgift om ansvarig medlemsstat. | Artiklarna 68.2-3 och förordning (EU) 2024/1358 artikel 16 | Eurodac/integration | 22 |
| OMF-SKA-026 | Systemet ska kunna visa att ansvar för ytterligare framställningar och efterföljande ansökningar följer omfördelningsmedlemsstaten när artikel 68.3 är tillämplig. | Artikel 68.3 | Ärendehistorik/ansvar | 23 |
| OMF-SKA-027 | Systemet ska stödja att en omfördelad person med internationellt skydd får motsvarande skyddsstatus i omfördelningsmedlemsstaten utan felaktig omprövning av statusgrunden. | Artikel 68.4 | Beslut/mottagning | 24 |
| OMF-SKA-028 | Systemet ska kunna hantera ansvarskompensation som ett eget solidaritetsspår, skilt från fysisk omfördelning. | Artikel 69 | Ansvar/styrning | 25 |
| OMF-SKA-029 | Systemet ska bevaka 30-dagarsfrist vid ansvarskompensation där sådan svarstid gäller. | Artikel 69.2 | Fristmotor | 25 |
| OMF-SKA-030 | Systemet ska kunna sammanställa status för genomförda, pågående och avbrutna solidaritetsåtgärder för underrättelse till kommissionen och EU-solidaritetssamordnaren. | Artikel 70 | Rapportering | 26 |
| OMF-SKA-031 | Systemet ska skydda personuppgifter, säkerhetsuppgifter, familjeuppgifter och skyddsrelaterad information genom behörighetsstyrning och spårbar åtkomst. | Artiklarna 72-73 | Dataskydd/sekretess | 27 |
| OMF-SKA-032 | Systemet ska kunna koppla omfördelning till relevant unionsfinansiering eller ekonomiskt stöd där sådant stöd ska följas upp. | Artikel 71 och förordning (EU) 2021/1147 | Ekonomi/styrning | 28 |

## Bör-krav

| ID | Krav | Motivering | Område | Koppling till user stories |
| --- | --- | --- | --- | --- |
| OMF-BOR-001 | Systemet bör visa en samlad översikt per solidaritetsår med utfästelser, utnyttjade bidrag, kvarstående kapacitet och öppna frister. | Underlättar styrning av den årliga solidaritetspoolen och rapportering enligt artikel 70. | Styrning/rapportering | 1, 2, 26 |
| OMF-BOR-002 | Systemet bör kunna versionshantera uppgifter om genomförandeakt, nationell utfästelse och ändrade solidaritetsbidrag. | Pool och nationella åtaganden kan behöva följas historiskt. | Styrning | 2, 3 |
| OMF-BOR-003 | Systemet bör kunna visa hur referensandel beräknats och vilket dataunderlag som använts. | Gör folkmängds- och BNP-baserad jämförelse granskningsbar. | BI/styrning | 4 |
| OMF-BOR-004 | Systemet bör kunna ange om ett ärende avser inkommande eller utgående omfördelning ur svensk synvinkel. | Sverige kan vara både bidragande och gynnad medlemsstat i olika lägen. | Ärendehantering | 1, 5 |
| OMF-BOR-005 | Systemet bör ge handläggaren strukturerade skälskoder för omfördelningsbarhet och hinder. | Ökar datakvalitet och gör rapportering jämförbar. | Ärendeurval | 6, 7 |
| OMF-BOR-006 | Systemet bör visa varning om familjegrupp riskerar att splittras mellan olika omfördelningsmedlemsstater. | Minskar risken för avsteg från familjesammanhållning. | Personrelationer | 10 |
| OMF-BOR-007 | Systemet bör ha tydlig textmall eller kommunikationsstöd som förklarar att meningsfull koppling beaktas men inte innebär valfrihet. | Minskar risken för missförstånd i informationen till personen. | Kommunikation | 9, 12 |
| OMF-BOR-008 | Systemet bör kunna markera sekretessnivå för säkerhetsuppgifter och begränsa synlighet i omfördelningsvyer. | Säkerhetsbedömningar kan vara känsliga och bör inte spridas brett. | Säkerhet/dataskydd | 7, 14, 27 |
| OMF-BOR-009 | Systemet bör ha arbetsköer för inkomna standardformulär, väntande säkerhetsgranskning, väntande bekräftelse och förestående överföring. | De korta tidsfristerna gör arbetsstyrning viktig. | Ärendehantering/frist | 13-20 |
| OMF-BOR-010 | Systemet bör eskalera ärenden där tyst bekräftelse kan uppstå inom kort. | Minskar risken för oavsiktlig processverkan vid passivitet. | Fristmotor | 16, 17 |
| OMF-BOR-011 | Systemet bör visa en tidslinje med alla centrala händelser: urval, formulär, granskning, bekräftelse, beslut, underrättelse, överföring och ankomst. | Gör ärendet begripligt och granskningsbart. | Ärendehantering | 5, 13-22 |
| OMF-BOR-012 | Systemet bör kunna lagra kvittenser och tekniska statusar för skickade och mottagna meddelanden. | Stödjer bevisning om informationsutbyte och friststart. | Integration | 13, 14, 23 |
| OMF-BOR-013 | Systemet bör kontrollera att överföringsbeslut inte fattas utan dokumenterad bekräftelse eller tillämplig tyst bekräftelse. | Minskar risken för felaktig överföring. | Beslut/frist | 17, 18 |
| OMF-BOR-014 | Systemet bör kunna särskilja utebliven ankomst från avbruten, uppskjuten eller ännu inte genomförd överföring. | Krävs för korrekt uppföljning och operativ åtgärd. | Mottagning/rapportering | 20, 21 |
| OMF-BOR-015 | Systemet bör ha avstämningsrapport mellan omfördelningsärenden, ansvarsfält och Eurodacstatus. | Fångar datakvalitetsfel efter ansvarsövergång. | Eurodac/ansvar | 22, 23 |
| OMF-BOR-016 | Systemet bör kunna separera statistik för omfördelning av sökande, omfördelning av personer med internationellt skydd och ansvarskompensation. | De tre spåren har olika rättslig och operativ innebörd. | Statistik/BI | 23-26 |
| OMF-BOR-017 | Systemet bör kunna markera beroenden till kommande standardformulär och tekniska format från genomförandeakter. | Delar av informationsutbytet kan preciseras senare. | Integration/förvaltning | 13 |
| OMF-BOR-018 | Systemet bör kunna registrera vilken svensk funktion som äger ärendet i varje fas: styrning, urval, säkerhet, mottagning, ansvar och rapportering. | Nationell ansvarsfördelning behöver kunna operationaliseras. | Organisation/workflow | 1, 5, 14, 21, 26 |
| OMF-BOR-019 | Systemet bör stödja rapportuttag för både operativ uppföljning och extern underrättelse. | Samma data behöver kunna användas för intern styrning och artikel 70-rapportering. | Rapportering | 26 |
| OMF-BOR-020 | Systemet bör ha auditlogg för ändringar av solidaritetsåtagande, säkerhetshinder, ansvarsövergång och ankomststatus. | Dessa uppgifter påverkar rättsliga följder och bör kunna granskas i efterhand. | Audit/dataskydd | 2, 7, 21, 22, 25, 27 |

## Luckor och verifieringspunkter

- Exakt innehåll i standardformulär, tekniska format och informationskanaler behöver verifieras mot kommande eller befintliga genomförandeakter.
- Svensk nationell rollfördelning behöver fastställas: vem äger styrning, säkerhetskontroll, mottagning, ansvar och rapportering?
- Kopplingen till Eurodac bör kontrolleras mer detaljerat mot förordning (EU) 2024/1358, särskilt vilka uppdateringar som kan automatiseras och vilka som kräver manuell kontroll.
- Krav på gallring, loggning, sekretess och dataskydd behöver kompletteras med nationell informationsklassning och dataskyddsanalys.
- Om kris- eller force majeure-förordningen används kan tidsfrister eller processförutsättningar påverkas och bör analyseras separat.

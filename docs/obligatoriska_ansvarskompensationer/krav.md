# Krav: obligatoriska ansvarskompensationer

## Källgrund

- Ny reglering: Förordning (EU) 2024/1351, särskilt artiklarna 12, 13, 56, 57, 58-63, 66, 69, 70, 72-73 och 85.
- Kopplad reglering: Förordning (EU) 2024/1358 artikel 16.3, förordning (EU) 2024/1348 artiklarna 55-56 och förordning (EU) 2024/1359.
- Lokal källa: `ref_material/OJ_L_202401351_SV_TXT.pdf`.
- Officiella referenser:
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1351>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1358>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1348>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1359>

## Läsanvisning

Detta är ett kravanalytiskt underlag, inte en slutlig rättsutredning. `Ska` används när kravet följer av en uttrycklig skyldighet, en rättsverkan eller en nödvändig systemförmåga för att kunna tillämpa ansvarskompensation enligt förordningen. `Bör` används när funktionen inte nödvändigtvis är uttryckligen reglerad, men behövs för styrning, kvalitet, spårbarhet eller robust handläggning.

Analysen avser främst ansvarskompensationer som solidaritetsåtgärd, med tonvikt på de obligatoriska fallen enligt artikel 63.3-5. Artikel 69 tas med eftersom den styr begäran och svar när ansvarskompensation används enligt artikel 63.1-2, men obligatoriska ansvarskompensationer behöver även modelleras som en egen avräknings- och ansvarsövergångsprocess.

## Kort slutsats

Obligatorisk ansvarskompensation är inte en fysisk omfördelning av en person. Det är en ansvarsförflyttning där en bidragande medlemsstat tar över prövningsansvar för identifierade ansökningar som en gynnad medlemsstat annars ansvarar för. Systempåverkan ligger därför främst i styrning, kvotberäkning, avräkning, identifiering av ansökningar, Eurodacuppdatering, rapportering och ärendehistorik.

## Ska-krav

| ID | Krav | Rättslig grund | Område | Motivering |
| --- | --- | --- | --- | --- |
| OAK-SKA-001 | Systemet ska kunna registrera ansvarskompensation som en egen solidaritetstyp, skild från omfördelning, ekonomiska bidrag och alternativa solidaritetsåtgärder. | Artiklarna 56.2, 63 | Styrning/rapportering | Ansvarskompensation har annan operativ och rättslig effekt än fysisk omfördelning. |
| OAK-SKA-002 | Systemet ska kunna koppla ansvarskompensation till solidaritetsår, årlig solidaritetspool och relevant genomförandeakt från rådet. | Artiklarna 12, 57, 63 | Styrning | Obligatoriska ansvarskompensationer beror på nivåerna i den årliga solidaritetspoolen. |
| OAK-SKA-003 | Systemet ska kunna registrera om Sverige agerar bidragande medlemsstat eller gynnad medlemsstat i ansvarskompensationsprocessen. | Artiklarna 56-63 | Roll/ärende | Samma process får olika uppgifter beroende på svensk roll. |
| OAK-SKA-004 | Systemet ska kunna lagra det antal omfördelningar som utlovats, accepterats, genomförts och återstår per medlemsstat och solidaritetsår. | Artiklarna 57, 63.5 | Avräkning | Obligatorisk kompensation kan utlösas när utlovade omfördelningar inte genomförts eller accepterats. |
| OAK-SKA-005 | Systemet ska kunna beräkna eller registrera medlemsstatens obligatoriska rättvisa andel enligt referensnyckeln. | Artiklarna 63.7, 66 och bilaga I | Beräkning | Artikel 63.7 begränsar skyldigheten till medlemsstatens rättvisa andel. |
| OAK-SKA-006 | Systemet ska kunna jämföra totala omfördelningsutfästelser med tröskeln 30 000 och med 60 procent av referensnumret för omfördelning. | Artiklarna 12.2 a, 63.3 | Tröskelstyrning | Artikel 63.3 anger när ansvarskompensation ska användas upp till det högre av dessa tal. |
| OAK-SKA-007 | Systemet ska kunna identifiera om artikel 63.4 blir tillämplig när utfästelser som ska genomföras under året faller under tröskeln på grund av avdrag eller undantag. | Artiklarna 58.1, 59.4, 61, 62, 63.4 | Tröskelstyrning | Skyldigheten kan uppstå även efter att poolen först fastställts. |
| OAK-SKA-008 | Systemet ska kunna registrera begäran från gynnad medlemsstat om att en bidragande medlemsstat tar över ansvar efter årets slut när omfördelningslöften inte genomförts. | Artikel 63.5 | Begäran/avräkning | Denna situation är ett centralt obligatoriskt ansvarskompensationsfall. |
| OAK-SKA-009 | Systemet ska kunna bevaka att ansvar tas över så snart som möjligt efter årets slut när artikel 63.5 är tillämplig. | Artikel 63.5 | Frist/uppföljning | Förordningen anger ingen fast dagfrist men kräver skyndsamhet. |
| OAK-SKA-010 | Systemet ska kunna hantera begäran enligt artikel 69 när ansvarskompensation används enligt artikel 63.1-2. | Artiklarna 63.1-2, 69.1 | Begäran | Begäran ska innehålla antal ansökningar som ansvar ska tas för i stället för omfördelning. |
| OAK-SKA-011 | Systemet ska kunna bevaka 30-dagarsfrist för svar på begäran enligt artikel 69. | Artikel 69.2 | Fristmotor | Bidragande medlemsstat ska svara inom 30 dagar. |
| OAK-SKA-012 | Systemet ska kunna registrera att bidragande medlemsstat accepterar ett lägre antal ansökningar än begärt när artikel 69.2 är tillämplig. | Artikel 69.2 | Beslut/avräkning | Delaccept påverkar avräkning, kvarstående behov och rapportering. |
| OAK-SKA-013 | Systemet ska kunna identifiera individuella ansökningar som omfattas av ansvarskompensation. | Artiklarna 63.6, 69.3 | Ärendeidentifiering | Ansvar övergår för identifierade ansökningar, inte enbart för en totalsiffra. |
| OAK-SKA-014 | Systemet ska kunna informera den gynnade medlemsstaten om identifierade ansökningar via relevant elektroniskt kommunikationsnät. | Artikel 63.6 | Integration/kommunikation | Artikel 63.6 hänvisar till nätet enligt artikel 18 i förordning (EG) nr 1560/2003. |
| OAK-SKA-015 | Systemet ska kunna uppdatera ansvarig medlemsstat i ärendet när bidragande medlemsstat blir ansvarig för identifierad ansökan. | Artikel 63.6 | Ansvar | Rättsverkan är att den bidragande medlemsstaten blir ansvarig medlemsstat. |
| OAK-SKA-016 | Systemet ska kunna initiera eller kontrollera Eurodacangivelse av ansvar enligt artikel 16.3 i förordning (EU) 2024/1358. | Artikel 63.6 och 69.3 i 2024/1351; artikel 16.3 i 2024/1358 | Eurodac | Ansvarsövertagandet ska avspeglas i Eurodac. |
| OAK-SKA-017 | Systemet ska hindra ansvarskompensation enligt artikel 63 för ensamkommande barn. | Artikel 63.8 a | Behörighetskontroll | Personkretsen är uttryckligen begränsad. |
| OAK-SKA-018 | Systemet ska kontrollera att den gynnade medlemsstatens ansvar grundas på kriterierna i artiklarna 29-33 innan artikel 63 tillämpas. | Artikel 63.8 b | Behörighetskontroll | Ansvarskompensation får bara användas i angiven ansvarssituation. |
| OAK-SKA-019 | Systemet ska kontrollera att överföringsfristen enligt artikel 39.1 inte har löpt ut. | Artikel 63.8 c | Frist/behörighet | Utgången överföringsfrist hindrar tillämpning av artikel 63. |
| OAK-SKA-020 | Systemet ska kontrollera att sökanden inte har avvikit från den bidragande medlemsstaten. | Artikel 63.8 d | Behörighetskontroll | Avvikande är uttryckligen undantagna från artikelns tillämpning. |
| OAK-SKA-021 | Systemet ska hindra ansvarskompensation enligt artikel 63 för personer som redan är personer med internationellt skydd. | Artikel 63.8 e | Behörighetskontroll | Ansvarskompensation avser prövningsansvar, inte statusöverföring. |
| OAK-SKA-022 | Systemet ska hindra ansvarskompensation enligt artikel 63 för antagna personer. | Artikel 63.8 f | Behörighetskontroll | Antagna personer är uttryckligen undantagna. |
| OAK-SKA-023 | Systemet ska kunna markera när artikel 63.9 används för tredjelandsmedborgare eller statslösa personer vars ansökningar slutligt avslagits i den gynnade medlemsstaten. | Artikel 63.9 och förordning (EU) 2024/1348 artiklarna 55-56 | Särfall | Detta är en särskild tillämpning med koppling till efterföljande ansökningar. |
| OAK-SKA-024 | Systemet ska kunna redovisa ansvarskompensationer som del av medlemsstatens obligatoriska rättvisa andel. | Skäl 33, artiklarna 63, 66 | Rapportering/avräkning | Kompensationerna räknas som solidaritetsbidrag. |
| OAK-SKA-025 | Systemet ska kunna hantera att en bidragande medlemsstat inte är skyldig att tillämpa ansvarskompensation gentemot en gynnad medlemsstat där kommissionen identifierat systembrister enligt förordningen. | Artikel 57.3 | Undantag/styrning | Systembrister kan påverka skyldigheten att bidra till just den medlemsstaten. |
| OAK-SKA-026 | Systemet ska kunna sammanställa status för planerade, begärda, accepterade, identifierade och genomförda ansvarskompensationer. | Artiklarna 63, 69, 70 | Rapportering | Kommissionen och EU-solidaritetssamordnaren behöver kunna följa genomförandet. |
| OAK-SKA-027 | Systemet ska skydda personuppgifter, ärendeuppgifter och uppgifter om ansvar enligt behörighetsstyrning, loggning och spårbar åtkomst. | Artiklarna 72-73 | Dataskydd/sekretess | Ansvarskompensation innebär behandling av person- och ärendedata mellan medlemsstater. |

## Bör-krav

| ID | Krav | Motivering | Område |
| --- | --- | --- | --- |
| OAK-BOR-001 | Systemet bör visa en samlad vy per solidaritetsår över utfästelser, genomförda omfördelningar, kvarstående åtagande och möjlig ansvarskompensation. | Ger styrning innan obligatorisk kompensation aktualiseras. | Dashboard/styrning |
| OAK-BOR-002 | Systemet bör varna när omfördelningsutfästelser riskerar att hamna under relevanta trösklar enligt artikel 63.3-4. | Tidig varning minskar risken för överraskande ansvarseffekt. | Tröskelstyrning |
| OAK-BOR-003 | Systemet bör kunna visa hur 30 000-tröskeln, 60-procentströskeln och rättvis andel har beräknats eller registrerats. | Gör beräkningen granskningsbar. | BI/beräkning |
| OAK-BOR-004 | Systemet bör ha skälskoder för varför ansvarskompensation initierats: tröskelbrist, avdrag/undantag, uteblivet genomförande eller frivillig överenskommelse. | Underlättar statistik och intern uppföljning. | Datakvalitet |
| OAK-BOR-005 | Systemet bör kunna särskilja obligatorisk ansvarskompensation från frivillig ansvarskompensation enligt artikel 63.1-2. | De två fallen har olika processlogik och olika styrningsrisk. | Klassificering |
| OAK-BOR-006 | Systemet bör visa en tidslinje för varje ansvarskompensationsärende: begäran, svar, identifiering, underrättelse, ansvarsövergång och Eurodacstatus. | Gör ansvarsövergången begriplig och granskningsbar. | Ärendehistorik |
| OAK-BOR-007 | Systemet bör ha arbetsköer för väntande 30-dagarssvar, väntande identifiering av ansökningar och väntande Eurodacbekräftelse. | Ansvarskompensation riskerar annars att fastna mellan styrning och individärende. | Workflow |
| OAK-BOR-008 | Systemet bör kunna jämföra ansvarskompensationer mot fysisk omfördelning i rapporter utan att slå ihop dem till samma händelsetyp. | Båda räknas som solidaritet men har olika faktisk innebörd. | Statistik/BI |
| OAK-BOR-009 | Systemet bör ha kontrollrapport mellan ansvarskompensationsregistret, ärendeansvar och Eurodacstatus. | Fångar fel där ansvar tagits över i ett system men inte i ett annat. | Avstämning |
| OAK-BOR-010 | Systemet bör kunna registrera kommunikationskvittenser och teknisk leveransstatus för meddelanden mellan medlemsstater. | Stödjer bevisning om när begäran, svar och identifiering skett. | Integration/audit |
| OAK-BOR-011 | Systemet bör kunna simulera effekten av olika genomförandegrad av omfördelningslöften på kommande ansvarskompensationer. | Hjälper planering av kapacitet och resursbehov. | Planering |
| OAK-BOR-012 | Systemet bör kunna markera om ansvarskompensation påverkas av kris- eller force majeure-regler. | Förordning (EU) 2024/1359 kan ändra förutsättningar och rättvis andel. | Undantag |
| OAK-BOR-013 | Systemet bör kunna ange nationell ägare per fas: EU-styrning, avräkning, juridisk kontroll, ärendeidentifiering, Eurodac och rapportering. | Ansvarskompensation går över flera organisatoriska gränser. | Organisation |
| OAK-BOR-014 | Systemet bör ha auditlogg för ändringar av antal, tröskelbedömning, personurval, ansvarsstatus och Eurodacstatus. | Dessa uppgifter påverkar rättsliga följder och bör kunna granskas. | Audit |
| OAK-BOR-015 | Systemet bör kunna exportera ett underlag för extern rapportering med aggregerade tal och ett separat internt underlag med individkopplingar. | Minskar risken för onödig spridning av personuppgifter. | Rapportering/dataskydd |

## Luckor och verifieringspunkter

- Exakt nationell rollfördelning behöver fastställas: vem äger beräkning, begäran, accept, ärendeidentifiering och Eurodackontroll?
- Tillämpningen av artikel 63.3-5 bör verifieras mot kommande årliga genomförandeakter och praktiska instruktioner från EU-solidaritetssamordnaren.
- Det behöver klargöras hur artikel 69-förfarandet ska användas i relation till obligatoriska fall enligt artikel 63.3-5, eftersom artikel 69 uttryckligen hänvisar till artikel 63.1-2.
- Kopplingen till Eurodac bör kontrolleras mer detaljerat mot tekniska specifikationer för artikel 16.3 i förordning (EU) 2024/1358.
- Krav på gallring, sekretess, loggning och informationsklassning behöver kompletteras med nationell dataskyddsanalys.
- Om kris- eller force majeure-förordningen används kan trösklar, andelar eller avräkning påverkas och bör analyseras separat.

# Krav: efterföljande ansökningar

## Källgrund

- Ny reglering: Förordning (EU) 2024/1348, särskilt artikel 3.19, 38.2, 55, 56 och 68.
- Kopplad reglering: Förordning (EU) 2024/1351 om ansvarig medlemsstat och förordning (EU) 2024/1358 om Eurodac.
- Gammal reglering: Direktiv 2013/32/EU, särskilt artikel 2 q, 33.2 d och 40-42.
- Lokal ny källa: `ref_material/OJ_L_202401348_SV_TXT.pdf`.
- Officiella referenser:
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1348>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1351>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1358>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32013L0032>

## Läsanvisning

Detta är ett kravanalytiskt underlag, inte en slutlig rättsutredning. `Ska` används när kravet följer av en uttrycklig skyldighet, en rättsverkan eller en nödvändig systemförmåga för att kunna tillämpa reglerna om efterföljande ansökningar. `Bör` används när funktionen inte nödvändigtvis är uttryckligen reglerad, men behövs för styrning, kvalitet, spårbarhet eller robust handläggning.

Kraven refererar inte till användarberättelser. De är skrivna som fristående system- och verksamhetskrav.

## Kort slutsats

Den nya förordningen behåller huvudlogiken att en efterföljande ansökan först ska förhandsprövas och kan avvisas om det saknas nya relevanta omständigheter. Systempåverkan ligger främst i att korrekt identifiera tidigare slutliga beslut, skilja efterföljande ansökan från ytterligare framställning i ett öppet ärende, stödja en strukturerad förhandsprövning och hantera rätt att stanna, överklagande och verkställighet utan att tappa non-refoulement-kontrollen.

## Ska-krav

| ID | Krav | Rättslig grund | Område | Motivering |
| --- | --- | --- | --- | --- |
| EFA-SKA-001 | Systemet ska kunna markera en ansökan som efterföljande när den görs efter ett slutligt beslut om en tidigare ansökan. | Artikel 3.19, 55.2 i 2024/1348 | Ärendeidentifiering | Klassificeringen styr om förhandsprövning enligt artikel 55 ska användas. |
| EFA-SKA-002 | Systemet ska kunna beakta tidigare slutliga beslut oavsett i vilken medlemsstat den tidigare ansökan gjordes, när uppgiften finns tillgänglig. | Artikel 3.19, 55.2 i 2024/1348 | Ärendehistorik/EU-koppling | Definitionen omfattar efterföljande ansökan efter tidigare beslut i vilken medlemsstat som helst. |
| EFA-SKA-003 | Systemet ska kunna skilja en efterföljande ansökan från en ytterligare framställning innan slutligt beslut har fattats i ett pågående ärende. | Artikel 55.1 i 2024/1348 | Ärendehantering | Nya uppgifter före slutligt beslut ska hanteras inom det pågående förfarandet. |
| EFA-SKA-004 | Systemet ska kunna visa om tidigare ansökan fortfarande är administrativt öppen, överklagad eller slutligt avgjord. | Artikel 55.1-2 i 2024/1348 | Status/ärendehistorik | Rätt process beror på om det finns ett slutligt beslut. |
| EFA-SKA-005 | Systemet ska kunna ange ansvarig medlemsstat för prövningen av den efterföljande ansökan. | Artikel 55 i 2024/1348 och 2024/1351 | Ansvar | Ansökan ska hanteras av ansvarig medlemsstat enligt ansvarsförordningen. |
| EFA-SKA-006 | Systemet ska stödja förhandsprövning av om det finns nya omständigheter eller uppgifter som väsentligt ökar sannolikheten för att sökanden har rätt till internationellt skydd. | Artikel 55.3 a i 2024/1348 | Prövningsstöd | Detta är kärnprövningen för om ansökan ska gå vidare till sakprövning. |
| EFA-SKA-007 | Systemet ska stödja förhandsprövning av om nya omständigheter eller uppgifter rör en tidigare använd avvisningsgrund. | Artikel 55.3 b i 2024/1348 | Prövningsstöd | Förordningen gör detta till ett eget relevant spår. |
| EFA-SKA-008 | Systemet ska kunna dokumentera vilka uppgifter som åberopas som nya och när de blev tillgängliga. | Artikel 55.3, 55.5 i 2024/1348 | Bevisning | Nyhetsbedömningen kräver spårbarhet om uppgifternas innehåll och tidpunkt. |
| EFA-SKA-009 | Systemet ska kunna dokumentera om sökanden kunde ha lagt fram uppgifterna i det tidigare förfarandet. | Artikel 55.5 i 2024/1348 | Prövningsstöd | Förhandsprövningen påverkas av om uppgiften borde ha åberopats tidigare. |
| EFA-SKA-010 | Systemet ska kunna markera när en uppgift ändå ska beaktas trots att den kunde ha lagts fram tidigare, om den väsentligt påverkar skyddsbedömningen eller tidigare avvisningsbedömning. | Artikel 55.5 i 2024/1348 | Rättssäkerhetskontroll | Förordningen anger undantag från en strikt nyhetsbedömning. |
| EFA-SKA-011 | Systemet ska kunna markera om den tidigare ansökan avslutades som implicit återkallad utan sakprövning. | Artikel 55.5 i 2024/1348 | Ärendehistorik | Detta kan påverka om nya uppgifter ska beaktas. |
| EFA-SKA-012 | Systemet ska kunna registrera om förhandsprövningen görs skriftligt eller med personlig intervju. | Artikel 55.4 i 2024/1348 | Intervju/prövning | Förordningen tillåter båda formerna och valet behöver vara spårbart. |
| EFA-SKA-013 | Systemet ska kunna dokumentera skäl för att avstå personlig intervju vid förhandsprövningen. | Artikel 55.4 i 2024/1348 | Intervju/rättssäkerhet | Avstående bör kunna granskas, särskilt när beslut fattas på skriftligt underlag. |
| EFA-SKA-014 | Systemet ska kunna föra ärendet vidare till full sakprövning när förhandsprövningen visar att relevanta nya omständigheter finns. | Artikel 55.6 i 2024/1348 | Workflow | En efterföljande ansökan ska prövas i sak när tröskeln är uppfylld, om ingen annan avvisningsgrund gäller. |
| EFA-SKA-015 | Systemet ska kunna hantera beslut om avvisning som otillåtlig när förhandsprövningen visar att relevanta nya omständigheter saknas. | Artikel 55.7 och 38.2 i 2024/1348 | Beslut | Beslutsgrunden skiljer sig från sakprövning och behöver egen klassificering. |
| EFA-SKA-016 | Systemet ska kunna skilja beslut som bygger på avsaknad av nya skyddsskäl från beslut som bygger på att tidigare avvisningsgrund fortfarande består. | Artikel 55.3, 55.7 och 38.2 i 2024/1348 | Beslutsgrund | De två prövningsspåren bör inte blandas i beslut, statistik eller uppföljning. |
| EFA-SKA-017 | Systemet ska kunna räkna om ansökan är första, andra eller ytterligare efterföljande ansökan. | Artikel 56 i 2024/1348 | Ärendehistorik | Antalet påverkar rätten att stanna och verkställighetsbedömningen. |
| EFA-SKA-018 | Systemet ska kunna koppla en efterföljande ansökan till återvändandebeslut och planerad eller nära förestående verkställighet. | Artikel 56 a i 2024/1348 | Återvändande/verkställighet | Rätt att stanna kan bedömas annorlunda om ansökan endast syftar till att försena avlägsnande. |
| EFA-SKA-019 | Systemet ska kunna markera när första efterföljande ansökan bedöms ha lämnats in enbart för att försena eller hindra ett nära förestående avlägsnande. | Artikel 56 a i 2024/1348 | Verkställighet/rätt att stanna | Detta är en särskild förutsättning för undantag från rätt att stanna. |
| EFA-SKA-020 | Systemet ska kunna markera när ansökan är en andra eller följande efterföljande ansökan efter tidigare avslag eller avvisning. | Artikel 56 b i 2024/1348 | Verkställighet/rätt att stanna | Detta kan påverka om sökanden har rätt att stanna under prövningen. |
| EFA-SKA-021 | Systemet ska kunna visa om sökanden har rätt att stanna under förhandsprövning, beslut och överklagande. | Artiklarna 56 och 68 i 2024/1348 | Rätt att stanna | Verkställighet får inte ske om rätt att stanna gäller. |
| EFA-SKA-022 | Systemet ska stödja kontroll av suspensiv effekt vid överklagande av beslut i efterföljande ansökan. | Artikel 68 i 2024/1348 | Överklagande/verkställighet | Handläggare behöver veta om överklagandet stoppar verkställighet automatiskt eller kräver särskilt beslut. |
| EFA-SKA-023 | Systemet ska kräva dokumenterad non-refoulement-kontroll innan undantag från rätt att stanna används. | Artiklarna 56 och 68 i 2024/1348 | Rättssäkerhetskontroll | Verkställighet får inte ske i strid med non-refoulement. |
| EFA-SKA-024 | Systemet ska kunna spåra relationen mellan tidigare ansökan, efterföljande ansökan, beslut, överklagande och verkställighetsstatus. | Artiklarna 55, 56 och 68 i 2024/1348 | Ärendehistorik/audit | Efterföljande ansökningar kräver tydlig kedja mellan gammalt och nytt ärende. |
| EFA-SKA-025 | Systemet ska kunna behörighetsstyra och logga åtkomst till skyddsskäl, tidigare beslut, avvisningsgrunder och verkställighetsuppgifter. | 2024/1348 samt dataskyddsregler | Dataskydd/sekretess | Uppgifterna kan vara känsliga och påverka rätt till skydd och verkställighet. |
| EFA-SKA-026 | Systemet ska kunna separera efterföljande ansökningar i rapportering från första ansökningar, ytterligare framställningar och överklaganden. | Artiklarna 3.19 och 55 i 2024/1348 | Statistik/rapportering | Begreppen har olika rättslig innebörd och olika processkonsekvenser. |

## Bör-krav

| ID | Krav | Motivering | Område |
| --- | --- | --- | --- |
| EFA-BOR-001 | Systemet bör visa en samlad översikt över tidigare ansökningar, beslut, överklaganden, återkallanden och verkställighetsstatus. | Handläggaren behöver snabbt förstå om ansökan är efterföljande och vilket flöde som gäller. | Ärendeöversikt |
| EFA-BOR-002 | Systemet bör varna när användaren försöker skapa ny ansökan trots att tidigare ärende inte är slutligt avgjort. | Minskar risken att en ytterligare framställning felaktigt hanteras som efterföljande ansökan. | Ärendehantering |
| EFA-BOR-003 | Systemet bör ha strukturerade skälskoder för nya skyddsskäl, nya uppgifter om tidigare avvisningsgrund, ej nya uppgifter och uppgifter som kunde ha lagts fram tidigare. | Ger bättre beslutsstöd och jämförbar statistik. | Prövningsstöd |
| EFA-BOR-004 | Systemet bör kunna visa beslutsstöd som tydligt skiljer förhandsprövning från full sakprövning. | Minskar risken att förhandsprövningen blir antingen för summarisk eller felaktigt fullständig. | Workflow |
| EFA-BOR-005 | Systemet bör kunna koppla bevisning och bilagor till specifika nya omständigheter. | Gör det lättare att granska varför ansökan gick vidare eller avvisades. | Dokument/bevisning |
| EFA-BOR-006 | Systemet bör kunna visa en tidslinje för när nya uppgifter uppkom, åberopades och bedömdes. | Stödjer nyhetsbedömningen och frågan om uppgifterna kunde ha lagts fram tidigare. | Ärendehistorik |
| EFA-BOR-007 | Systemet bör ha mallstöd för beslut om att gå vidare till sakprövning respektive avvisa som otillåtlig. | Beslutsgrunderna behöver formuleras konsekvent enligt den nya förordningen. | Beslut |
| EFA-BOR-008 | Systemet bör ha mallstöd för beslut eller notering om att personlig intervju inte behövs i förhandsprövningen. | Gör avståendet från intervju spårbart och enhetligt. | Intervju |
| EFA-BOR-009 | Systemet bör kunna visa om tidigare ansökan avvisades på processuell grund, avslogs i sak eller avslutades efter implicit återkallelse. | Olika tidigare utfall påverkar prövningen av den nya ansökan. | Ärendehistorik |
| EFA-BOR-010 | Systemet bör kunna hämta eller presentera relevanta uppgifter från EU-system eller medlemsstatskommunikation när tidigare ansökan finns i annan medlemsstat. | Definitionen omfattar tidigare beslut i vilken medlemsstat som helst, men uppgifterna kan behöva verifieras. | Integration |
| EFA-BOR-011 | Systemet bör ha arbetsköer för efterföljande ansökningar med nära förestående verkställighet. | Dessa ärenden har hög rättssäkerhetsrisk och kan kräva snabb bedömning. | Workflow/verkställighet |
| EFA-BOR-012 | Systemet bör varna om verkställighet planeras medan rätt att stanna eller suspensiv effekt är oklar. | Minskar risken för felaktig verkställighet. | Återvändande |
| EFA-BOR-013 | Systemet bör visa en särskild kontrollpunkt för non-refoulement innan ärendet lämnas till verkställighet. | Rättssäkerhetsspärret bör vara synligt och obligatoriskt i risklägen. | Rättssäkerhet |
| EFA-BOR-014 | Systemet bör kunna separera statistik för första efterföljande ansökan och andra eller följande efterföljande ansökan. | Rätt att stanna och processrisk skiljer sig mellan kategorierna. | Statistik |
| EFA-BOR-015 | Systemet bör kunna separera statistik för ansökningar som avvisas efter förhandsprövning och ansökningar som går vidare till sakprövning. | Visar hur artikel 55 används i praktiken. | Statistik |
| EFA-BOR-016 | Systemet bör kunna markera om en efterföljande ansökan har koppling till omfördelning eller ansvarskompensation där ansvarig medlemsstat ändrats. | Ansvarsförändringar enligt solidaritetsmekanismen kan påverka vilken medlemsstat som ska hantera ansökan. | Ansvar/EU-koppling |
| EFA-BOR-017 | Systemet bör ha auditlogg för ändringar av klassificering, nyhetsbedömning, intervjubedömning, rätt att stanna och verkställighetsstatus. | Dessa ändringar påverkar centrala rättsföljder. | Audit |
| EFA-BOR-018 | Systemet bör kunna generera intern kvalitetsrapport över vanliga skäl till avvisning eller fortsatt sakprövning. | Stödjer enhetlig tillämpning och utbildningsbehov. | Uppföljning |

## Luckor och verifieringspunkter

- Begreppet `slutligt beslut` behöver mappas mot svenska beslutstyper, överklagandestadier och verkställbarhet.
- Det behöver klargöras vilka system eller informationsutbyten som praktiskt kan visa tidigare ansökningar och slutliga beslut i andra medlemsstater.
- Artikel 68 behöver analyseras mer detaljerat mot svenskt överklagande- och verkställighetsflöde.
- Beslutsmallar behöver kontrolleras mot nationella processregler och terminologi för avvisning som otillåtlig.
- Kopplingar till Eurodac, ansvarsförordningen och solidaritetsmekanismen bör fördjupas där ansvarig medlemsstat har ändrats efter omfördelning eller ansvarskompensation.
- Krav på gallring, sekretess, loggning och informationsklassning behöver kompletteras med nationell dataskyddsanalys.

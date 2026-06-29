# User stories: statistik

## Källgrund

- Ny reglering: Förordning (EU) 2024/1358, särskilt artikel 12, 57 och 63.
- Gammal reglering: Förordning (EU) nr 603/2013, särskilt artikel 8 och 40.
- Lokal ny källa: `ref_material/OJ_L_202401358_SV_TXT.pdf`.
- Officiella referenser:
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1358>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32013R0603>

## Kort slutsats

Statistikspåret ändras från relativt begränsad Eurodacstatistik om fingeravtryck, transaktioner och träffar till ett bredare rapporteringsunderlag för asyl- och migrationshantering. Den nya Eurodacförordningen kräver månadsstatistik, årsstatistik, flera personkategorier, statusmarkeringar, kvalitetsmått, statistik över träffar mellan kategorier, samt åtkomst till den centrala databasen för rapportering och statistik enligt interoperabilitetsramen.

## User stories

| nr | Feature | Användarberättelse | System | Kommentar |
| --- | --- | --- | --- | --- |
| 1 | Identifiera statistikgap | Som analytiker vill jag se vilka statistikuppgifter som är nya jämfört med tidigare ordning, så att systempåverkan kan prioriteras. | Statistik/rapportering | Bygger på jämförelse mellan 603/2013 artikel 8 och 2024/1358 artikel 12. |
| 2 | Eurodac-kategori | Som handläggare vill jag att systemet anger vilken Eurodac-kategori en person hör till, så att uppgifter registreras och sammanställs i rätt statistikgrupp. | Ärendehantering/Eurodac | Nya artikel 12 utgår från flera kategorier: sökande, irreguljär gränspassage, olaglig vistelse, SAR, skyddsstatus, vidarebosättning och tillfälligt skydd. |
| 3 | Månadsstatistik | Som rapporteringsansvarig vill jag att Eurodacrelaterad statistik kan tas fram per månad, så att rapporteringen motsvarar artikel 12.2. | Statistik/rapportering | Ny ordning anger publicering av månatliga statistiska uppgifter. |
| 4 | Årsstatistik | Som rapporteringsansvarig vill jag kunna låsa och granska årsstatistik, så att årsutfall kan jämföras över tid och mot eu-LISA:s publicering. | Statistik/rapportering | Artikel 12.2 anger även årlig statistik. |
| 5 | Uppdelning per medlemsstat | Som analytiker vill jag kunna bryta ned statistiken per medlemsstat, så att svenska siffror kan jämföras med övriga medlemsstater. | Statistik/BI | Artikel 12.2 anger uppdelning per medlemsstat. |
| 6 | Uppdelning efter födelseår och kön | Som analytiker vill jag kunna visa relevanta statistikmått efter födelseår och kön när det är möjligt, så att kravet på mer granulär statistik kan uppfyllas utan att identifiera individer. | Statistik/BI | Gäller särskilt datapunkter enligt artikel 12.1 i, där artikel 12.2 anger uppdelning när möjligt. |
| 7 | Förstagångsansökningar | Som analytiker vill jag kunna särskilja första ansökningar från andra ansökningar, så att statistik om asylinflöde inte dubbelräknar samma person. | Ärendehistorik/Eurodac | Artikel 12.1 b tar upp antal personer som ansökt för första gången. |
| 8 | Avslagna ansökningar utan rätt att stanna | Som besluts- eller återvändandeansvarig vill jag att systemet kan markera när ansökan avslagits och personen saknar rätt att stanna, så att Eurodac- och återvändandestatistik blir korrekt. | Beslut/Återvändande/Eurodac | Kopplas till nya statusuppgifter i Eurodac, bland annat artikel 17.2 j och statistik enligt artikel 12. |
| 9 | Minderåriga | Som analytiker vill jag kunna följa antal registrerade minderåriga, så att rapportering och kapacitetsplanering kan skilja barn från vuxna. | Ärendehantering/Statistik | Artikel 12.1 f anger antal personer registrerade som minderåriga. |
| 10 | Biometrisk upptagning från sex år | Som systemförvaltare vill jag kunna följa om biometriska uppgifter tas för personer från sex års ålder där förordningen kräver det, så att processen följer nya Eurodacregler. | Eurodac/Datakvalitet | Nya kategorier använder sex år som tröskel i flera artiklar, bland annat 15, 22, 23, 24 och 26. |
| 11 | Datatransmission inom tidsfrist | Som systemförvaltare vill jag följa om data skickas till Eurodac inom 72 timmar eller annan relevant tidsfrist, så att brister kan upptäckas och åtgärdas. | Eurodac/integration | Flera kategorier har 72-timmarsfrist; vissa undantag har annan kompletterande frist. |
| 12 | Biometrisk datakvalitet | Som systemförvaltare vill jag se hur ofta Eurodac begär nya biometriska uppgifter på grund av otillräcklig kvalitet, så att utrustning och arbetssätt kan förbättras. | Eurodac/integration | Artikel 12.1 q anger antal biometriska uppgifter som måste begäras mer än en gång. |
| 13 | Träffmatris mellan kategorier | Som analytiker vill jag kunna visa träffar mellan olika Eurodac-kategorier, så att sekundära rörelser och tidigare registreringar kan analyseras korrekt. | Statistik/BI/Eurodac | Artikel 12.1 k-p beskriver träffar för flera kategori-kombinationer. |
| 14 | Sök- och räddningskategori | Som rapporteringsansvarig vill jag kunna särskilja personer som landsatts efter sök- och räddningsinsats, så att statistiken speglar den nya Eurodac-kategorin. | Gräns/Eurodac/Statistik | Ny uttrycklig kategori i 2024/1358, artikel 24 och artikel 12. |
| 15 | Tillfälligt skydd | Som rapporteringsansvarig vill jag kunna hantera statistik om personer registrerade som förmånstagare av tillfälligt skydd när artikel 26 börjar tillämpas, så att systemet är redo från rätt datum. | Mottagning/Eurodac/Statistik | Artikel 26 tillämpas först från 12 juni 2029 enligt artikel 63.2. |
| 16 | Vidarebosättning och humanitärt mottagande | Som analytiker vill jag kunna följa personer i antagningsförfarande och nationell vidarebosättning, så att Eurodacstatistik även omfattar dessa nya spår. | Vidarebosättning/Eurodac/Statistik | Artikel 12.1 g-h och relaterade artiklar 18-21. |
| 17 | Markeringar och avmarkeringar | Som systemförvaltare vill jag följa antal markerade och avmarkerade dataset, så att skyddsstatus och uppehållsrelaterade markeringar hålls korrekta. | Eurodac/Datakvalitet | Artikel 12.1 r hänvisar till markering enligt artikel 31. |
| 18 | Central rapporteringsåtkomst | Som statistikbehörig vill jag kunna få kontrollerad åtkomst till den centrala databasen för rapportering och statistik, så att behöriga rapporter kan tas fram utan individidentifiering. | Statistik/Behörighet | Artikel 12.5-12.6 hänvisar till central repository for reporting and statistics enligt interoperabilitetsramen. |
| 19 | Anpassade statistikbeställningar | Som analytiker vill jag kunna svara på särskilda statistikbeställningar från kommissionen eller nationella mottagare, så att särskilda aspekter av Eurodactillämpningen kan redovisas. | Statistik/BI | Artikel 12.4 anger att eu-LISA på kommissionens begäran ska lämna statistik om särskilda aspekter. |
| 20 | Anonymiseringskontroll | Som dataskyddsansvarig vill jag att statistikrapporter kontrolleras så att de inte identifierar enskilda, så att rapportering följer artikel 12 och dataskyddskraven. | Statistik/Dataskydd | Artikel 12.2, 12.3 och 12.5 betonar att statistiken inte ska identifiera individer. |
| 21 | Underlag till eu-LISA:s årsrapport | Som rapporteringsansvarig vill jag kunna lämna den information som eu-LISA och kommissionen behöver för årsrapporten, så att medlemsstatens bidrag blir komplett. | Statistik/Eurodacförvaltning | Artikel 57.6 anger att medlemsstaterna ska lämna information för årsrapporten. |
| 22 | Underlag till kommissionens utvärdering | Som processägare vill jag kunna ta fram uppgifter till kommissionens fyraåriga Eurodacutvärdering, så att Sverige kan redovisa effekt, dataskydd och operativa konsekvenser. | Statistik/Styrning | Artikel 57.5 och 57.7. |
| 23 | Brottsbekämpande åtkomst | Som behörig rapporteringsansvarig vill jag kunna ta fram tvåårsrapporter om brottsbekämpande jämförelser mot Eurodac, så att Sverige uppfyller artikel 57.8. | Brottsbekämpande åtkomst/Statistik | Separat känsligt spår med uppgifter om syfte, misstankegrund, antal begäranden och träffar. |
| 24 | Kvalitetssäkring före publicering | Som rapporteringsansvarig vill jag kunna granska avvikelser, sena överföringar och oklassade poster före statistikpublicering, så att rapporteringen inte bygger på ofullständiga data. | Statistik/Datakvalitet | Praktiskt kontrollkrav som följer av fler datapunkter och tidsfrister i 2024/1358. |
| 25 | Övergångsdatum | Som systemförvaltare vill jag att rapporteringen skiljer på regler före och efter 12 juni 2026, och artikel 26 från 12 juni 2029, så att statistik inte blandar gamla och nya rättsliga grunder. | Statistik/Regelstyrning | Artikel 63 anger tillämpningsdatum och upphävande av 603/2013. |

## Frågor för fortsatt analys

- Vilken svensk myndighet eller organisatorisk funktion ska utses eller ges åtkomst enligt artikel 12.6 och artikel 40.2?
- Vilka nationella system äger fälten för beslut, rätt att stanna, återvändande, AVRR, SAR, vidarebosättning och tillfälligt skydd?
- Vilka statistikmått ska Migrationsverket ta fram nationellt, och vilka genereras främst av eu-LISA från Eurodac?
- Hur ska små tal och kombinationer av födelseår, kön, medlemsstat och kategori hanteras för att undvika indirekt identifiering?
- Behövs särskilda migrerings- eller jämförelseregler för statistik över perioder som passerar 12 juni 2026?

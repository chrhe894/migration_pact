# Eurodac och statistik

## Källgrund

- Ny reglering: Förordning (EU) 2024/1358.
- Gammal reglering: Förordning (EU) nr 603/2013.
- Lokal ny källa: `ref_material/OJ_L_202401358_SV_TXT.pdf`.
- Äldre källa online: <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32013R0603>.
- Ny källa online: <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1358>.

## Varför Eurodac hör till statistikspåret

Den nya Eurodacförordningen anger uttryckligen att Eurodac ska stödja evidensbaserat beslutsfattande genom framställning av statistik. Det gör rättsakten relevant både som egen systemfråga och som underlag för uppgiften om ny statistik jämfört med gammal ordning.

## Första jämförelseområden

| Område | Gammal ordning, 603/2013 | Ny ordning, 2024/1358 | Möjlig systempåverkan |
| --- | --- | --- | --- |
| Syfte | Eurodac stödde främst fingeravtrycksjämförelse för Dublinansvar och vissa brottsbekämpande sökningar. | Eurodac stödjer bredare asyl- och migrationshantering, vidarebosättning/humanitärt mottagande, identifiering av olaglig vistelse, VIS/ETIAS-kopplingar och statistik. | Fler processer och fler verksamhetsområden kan behöva konsumera eller producera Eurodacrelaterade uppgifter. |
| Datatyper | Fokus på fingeravtrycksuppgifter och begränsade ärendeuppgifter. | Omfattar biometriska uppgifter, inklusive fingeravtryck och ansiktsbild, samt fler person- och processuppgifter. | Datamodeller, behörigheter, lagring och kvalitetskontroller behöver analyseras. |
| Personkategorier | Sökande, personer som passerat yttre gräns olagligt och personer som vistas olagligt. | Fler kategorier, bland annat kopplade till vidarebosättning/humanitärt mottagande, tillfälligt skydd och personer som landsatts efter sök- och räddningsinsats. | Statistik och rapportering behöver kunna särskilja fler kategorier. |
| Ålder för upptagning | Kräver artikelverifiering mot gammal rättsakt. | Nya regler anger upptagning av biometriska uppgifter från personer som är minst sex år i flera kategorier. | Processer för barn, samtycke/information, utrustning och dataskydd behöver särskild analys. |
| Statistik | Äldre ordning hade rapportering och årlig uppföljning av centralsystemets verksamhet. | Ny ordning gör statistik till ett uttryckligt syfte och har bredare databasunderlag. | Kravanalysen bör identifiera vilka statistikmått som är nya, ändrade eller mer granulära. |

## User story-kandidater

| nr | Feature | Användarberättelse | System | Kommentar |
| --- | --- | --- | --- | --- |
| 1 | Eurodacstatistik | Som analytiker vill jag kunna ta fram statistik baserad på de nya Eurodac-kategorierna, så att rapportering och uppföljning motsvarar förordning (EU) 2024/1358. | Statistik/rapportering | Vidareutvecklad i `user_stories.md` och `datapunkter.md`. |
| 2 | Datakategori | Som handläggare vill jag att systemet anger vilken Eurodac-kategori en person tillhör, så att uppgifter kan skickas och sammanställas korrekt. | Ärendehantering/Eurodac | Behöver jämföras mot gamla kategorier i förordning (EU) nr 603/2013. |
| 3 | Biometrisk datakvalitet | Som systemförvaltare vill jag följa upp om biometriska uppgifter har skickats inom rätt tid och med rätt kvalitet, så att Eurodacrapporteringen blir tillförlitlig. | Eurodac/integration | Kopplas till tidsfrister och tekniska krav i 2024/1358. |

## Frågor för fortsatt analys

- Vilka nationella system behöver ändras för att leverera de datapunkter som identifieras i `datapunkter.md`?
- Vilka statistikmått ska Migrationsverket själv kvalitetssäkra, och vilka genereras främst centralt av eu-LISA?
- Vilka uppgifter ska kunna aggregeras utan att skapa otillåten personuppgiftsbehandling?
- Vilka system behöver lämna underlag till Eurodacstatistik: asyl, mottagning, återvändande, gräns, vidarebosättning eller brottsbekämpande åtkomst?

#!/usr/bin/env python3
"""Skapar regler för återvändandesamordning (ambassad och resa) från förordning 2016/1953,
beslut 2004/573/EG, förordning 2019/1896, APR art. 7 och utlänningslagen 12 kap.

Innehållet är kontrollerat mot texterna i references/_text/. Körs en gång; ändra sedan filerna direkt.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "docs" / "domains"
RET = "../../../references/legislation"

RULES = [
    # (domän, ID, rättslig grund (markdown), regeltyp, regel, syfte, utlösare, rättsverkan[list], tillämpas, relaterade[list], taggar[list])
    ("asylum-procedure", "RULE-APR-007-001",
     f"[APR artikel 7](../articles/apr-007.md), punkt 1–2 ([APR]({RET}/apr.md))",
     "Förbud",
     "Myndigheterna är bundna av tystnadsplikt för alla personuppgifter de inhämtar, inbegripet utbyte mellan medlemsstaterna (7.1). Under förfarandet för internationellt skydd **och efter ett slutligt beslut** får myndigheterna inte **a)** röja uppgifter om en enskild ansökan eller **det faktum att en ansökan har gjorts** till de aktörer som påstås utöva förföljelse eller tillfoga allvarlig skada, eller **b)** inhämta uppgifter från dessa aktörer på ett sätt som ger dem information om att personen har ansökt (7.2).",
     "Skyddar sökanden och anhöriga mot repressalier från dem som sökanden flytt från.",
     "Myndigheten kontaktar ursprungslandets myndigheter, till exempel en ambassad, för identifiering eller resehandling, eller inhämtar uppgifter från dem.",
     ["Gäller även efter avslag och under återvändandet (\"efter det att ett slutligt beslut om ansökan har fattats\").",
      "När staten eller dess företrädare påstås vara förföljaren får ambassaden inte få veta att personen har sökt asyl.",
      "Frontex har motsvarande begränsning vid konsulärt samarbete ([RULE-FRX-048-001](../../return/rules/rule-frx-048-001.md)).",
      "Förordning 2026/2280 art. 37 tillåter överföring av vissa uppgifter till tredjeland, men innehåller inget eget förbud av detta slag. Se [PROC-RTN-004](../../return/processes/return-coordination-embassy.md)."],
     "12 juni 2026 (APR)",
     ["[RULE-RR-037-001](../../return/rules/rule-rr-037-001.md) — Överföring av uppgifter till tredjeländer"],
     ["asylförfarande", "regel", "tystnadsplikt", "återvändande"]),

    ("return", "RULE-ETD-003-001",
     f"[Förordning (EU) 2016/1953 artikel 3]({RET}/european-travel-document.md)",
     "Obligation",
     "Den europeiska resehandlingen för återvändande ska följa mallen i bilagan och innehålla personens namn, födelsedatum, kön, medborgarskap, särskilda kännetecken och känd adress i mottagande tredjeland, ett fotografi, utfärdande myndighet, datum och plats för utfärdande och giltighetstid samt information om avresa och ankomst (3.1). Den utfärdas på den utfärdande medlemsstatens officiella språk och vid behov även på engelska och franska (3.2). Den är giltig för **en enda resa** fram till ankomsten till det mottagande tredjelandet (3.3). Ytterligare handlingar får bifogas (3.4).",
     "Ger en enhetlig resehandling när personen saknar giltigt pass och tredjelandet godtar handlingen.",
     "Personen saknar giltig resehandling och återtagandeinstrumentet medger europeisk resehandling ([art. 34.1](../articles/rr-034.md)).",
     ["Ny handling krävs för varje resa.",
      "Handlingen är utan kostnad för personen ([RULE-ETD-005-001](rule-etd-005-001.md)).",
      "Om tredjelandet godtar handlingen styrs av återtagandeavtalet eller överenskommelsen."],
     "8 april 2017 (gäller nu)",
     ["[RULE-RR-034-001](rule-rr-034-001.md) — Inledande av återtagande"],
     ["återvändande", "regel", "resehandling"]),

    ("return", "RULE-ETD-005-001",
     f"[Förordning (EU) 2016/1953 artikel 5]({RET}/european-travel-document.md)",
     "Rättighet",
     "Den europeiska resehandlingen för återvändande ska utfärdas **utan kostnad** för tredjelandsmedborgaren.",
     "Hindrar att kostnaden för handlingen läggs på personen.",
     "En europeisk resehandling utfärdas.",
     ["Ingen avgift får tas ut för handlingen."],
     "8 april 2017 (gäller nu)",
     ["[RULE-ETD-003-001](rule-etd-003-001.md)"],
     ["återvändande", "regel", "resehandling"]),

    ("return", "RULE-JRF-004-001",
     f"[Rådets beslut 2004/573/EG artikel 4]({RET}/joint-return-flights.md)",
     "Obligation",
     "En medlemsstat som organiserar en gemensam flygning öppen för andra medlemsstater ska informera deras nationella myndigheter (4.1). Den organiserande statens myndighet ska bland annat **a)** välja lufttrafikföretag, fastställa kostnader och ingå avtal, **b)** begära och ta emot de tillstånd som krävs från **transit- och destinationsländerna**, **c)** samordna med de deltagande staterna, **d)** fastställa operativa former och, i samförstånd med de deltagande staterna, **antalet ledsagare** i förhållande till antalet återvändande, och **e)** ingå finansiella överenskommelser (4.2).",
     "Fördelar ansvaret när flera medlemsstater återsänder på samma flygning.",
     "Sverige organiserar en gemensam flygning för återsändande.",
     ["Tillstånd från transit- och destinationsländer måste finnas innan flygningen genomförs.",
      "Antalet ledsagare bestäms per insats, se riktlinjerna ([RULE-JRF-007-001](rule-jrf-007-001.md))."],
     "Gäller nu",
     ["[RULE-JRF-005-001](rule-jrf-005-001.md)", "[RULE-JRF-006-001](rule-jrf-006-001.md)"],
     ["återvändande", "regel", "gemensam-flygning"]),

    ("return", "RULE-JRF-005-001",
     f"[Rådets beslut 2004/573/EG artikel 5]({RET}/joint-return-flights.md)",
     "Obligation",
     "En medlemsstat som deltar i en gemensam flygning ska **a)** informera den organiserande statens myndighet om sin avsikt och om **antalet** återvändande, och **b)** tillhandahålla ett tillräckligt antal ledsagare. Om bara den organiserande staten tillhandahåller ledsagare ska varje deltagande stat ha **minst två företrädare** ombord, som ansvarar för att de egna återvändande överlämnas till destinationslandets myndigheter.",
     "Säkerställer att varje stat ansvarar för sina egna återvändande hela vägen.",
     "Sverige deltar i en gemensam flygning som en annan medlemsstat organiserar.",
     ["Minst två svenska företrädare ombord när den organiserande staten står för ledsagarna.",
      "Används privata ledsagare ska minst en officiell företrädare finnas ombord (bilagan 1.2.3)."],
     "Gäller nu",
     ["[RULE-JRF-004-001](rule-jrf-004-001.md)"],
     ["återvändande", "regel", "gemensam-flygning"]),

    ("return", "RULE-JRF-006-001",
     f"[Rådets beslut 2004/573/EG artikel 6]({RET}/joint-return-flights.md)",
     "Obligation",
     "Den organiserande och varje deltagande medlemsstat ska **a)** se till att varje återvändande och ledsagare har **giltiga resehandlingar** och andra nödvändiga handlingar, till exempel inrese- eller transitviseringar, intyg eller registreringar, och **b)** så snart som möjligt informera sina **diplomatiska och konsulära beskickningar** i transit- och destinationsländerna om flygningen för att få den hjälp som behövs.",
     "Säkerställer att resan inte stoppas av saknade handlingar och att beskickningarna kan bistå.",
     "En gemensam flygning planeras.",
     ["Resehandlingar och viseringar kontrolleras före flygningen.",
      "Egna beskickningar i transit- och destinationsland informeras i förväg."],
     "Gäller nu",
     ["[RULE-JRF-007-001](rule-jrf-007-001.md)"],
     ["återvändande", "regel", "gemensam-flygning", "resehandling"]),

    ("return", "RULE-JRF-007-001",
     f"[Rådets beslut 2004/573/EG artikel 7 och bilagan]({RET}/joint-return-flights.md)",
     "Obligation",
     "Vid gemensamma flygningar ska medlemsstaterna beakta de gemensamma riktlinjerna för säkerhetsbestämmelser i bilagan. Förordning 2026/2280 art. 10.10 kräver att riktlinjerna beaktas vid **alla avlägsnanden med flyg**.",
     "Ger gemensamma minimiregler för säkerhet, värdighet och vård under återsändande med flyg.",
     "Avlägsnande med flyg, särskilt gemensam flygning.",
     ["**Före:** den rättsliga ställningen ska tillåta återsändande. Hälsotillståndet ska medge säker flygning, och sjukjournaler ska finnas vid kända hälsoproblem (1.1.1–1.1.2). Resehandlingar och kompletterande handlingar ska finnas och behållas av en bemyndigad person fram till ankomsten (1.1.3). Flygbolag, transitländer och destinationsland ska underrättas **i god tid** (1.1.4).",
      "**Ledsagare:** utbildade, obeväpnade och tydligt identifierade. Antalet bestäms efter riskanalys och bör i de flesta fall **minst motsvara antalet återvändande**, med en reservenhet vid behov (1.2).",
      "**Flygplats:** ledsagare och återvändande anländer **minst tre timmar före avgång**. Säker zon och noggrann säkerhetskontroll (2.1–2.2).",
      "**Tvång:** rimligt och proportionerligt, får inte hindra andningen, och **lugnande medel är förbjudna** (utom nödåtgärder för flygsäkerheten). Förteckning över tillåtna metoder ska fastställas i förväg. I tveksamma fall avbryts insatsen (3.2).",
      "**Vård och tolk:** **minst en läkare** ombord vid gemensam flygning. Bara läkaren får ge medicin. Personen ska kunna tala med läkare eller ledsagare via tolk (3.3).",
      "**Ankomst:** överlämnande till destinationslandets myndigheter **utan handbojor eller andra tvångsmedel**, utanför flygplanet. Konsulatpersonal eller sambandsmän får underlätta överlämnandet (5).",
      "**Misslyckad insats:** varje deltagande stat ansvarar för och bekostar återresan för sina återvändande (6).",
      "Transitering i en medlemsstat följer direktiv 2003/110/EG (4), som inte finns i repot."],
     "Gäller nu. Hänvisningen i förordning 2026/2280 art. 10.10 gäller från 17 oktober 2027",
     ["[RULE-RR-010-004](rule-rr-010-004.md) — Tvångsåtgärder vid avlägsnande", "[RULE-RR-012-001](rule-rr-012-001.md) — Övervakning"],
     ["återvändande", "regel", "gemensam-flygning", "tidsfrister"]),

    ("return", "RULE-FRX-048-001",
     f"[Förordning (EU) 2019/1896 artikel 48]({RET}/frontex.md)",
     "Befogenhet",
     "Frontex ska, utan att pröva besluten om återvändande i sak, ge medlemsstaterna tekniskt och operativt stöd, bland annat vid **i)** insamling av uppgifter och identifiering, **ii)** **anskaffande av resehandlingar, inbegripet genom konsulärt samarbete, utan att lämna ut information om att en ansökan om internationellt skydd gjorts** eller annan information som inte krävs för återvändandet, **iii)** organisation och samordning av återvändandeinsatser och bistånd vid frivilliga återvändanden, och **iv)** bistånd till den som återvänder frivilligt, före, under och efter resan (48.1 a). Stödet omfattar också tolktjänster, information om tredjeländer, rådgivning och utrustning (48.2).",
     "Ger medlemsstaterna gemensamma resurser för identifiering, resehandlingar och resor.",
     "Medlemsstaten begär stöd från Frontex ([RR art. 43](../articles/rr-043.md)).",
     ["Besluten om återvändande förblir medlemsstatens ansvar.",
      "Vid konsulärt samarbete får det inte avslöjas att personen ansökt om internationellt skydd. Jämför [RULE-APR-007-001](../../asylum-procedure/rules/rule-apr-007-001.md)."],
     "Gäller nu",
     ["[RULE-RR-043-001](rule-rr-043-001.md) — Begära stöd från Frontex", "[RULE-FRX-050-001](rule-frx-050-001.md)"],
     ["återvändande", "regel", "frontex"]),

    ("return", "RULE-FRX-050-001",
     f"[Förordning (EU) 2019/1896 artikel 50]({RET}/frontex.md)",
     "Obligation",
     "Frontex ska samordna eller organisera återvändandeinsatser, bland annat genom att **chartra flygplan** och organisera återvändande på **reguljära flygningar** eller med andra transportmedel (50.1). Medlemsstaterna ska via plattformen lämna operativa data och underrätta Frontex om sin **preliminära planering** (antal personer och mottagande tredjeländer) (50.2). Utplacerade enheter ska **före återvändandet konsultera SIS** för att kontrollera om beslutet om återvändande upphävts tillfälligt eller verkställigheten skjutits upp (50.2). Insatser med tvång ska **övervakas** från förberedelserna inför avresan till överlämnandet (50.5).",
     "Samordnar flygningar mellan medlemsstater och säkerställer kontroll och övervakning.",
     "Sverige deltar i en återvändandeinsats som Frontex organiserar eller samordnar.",
     ["SIS-kontroll av uppskjutet eller upphävt beslut omedelbart före återvändandet.",
      "Övervakare av återvändande med tvång från reserven i art. 51 kan ställas till förfogande.",
      "Frontex rapporterar om insatserna **var sjätte månad** (50.7)."],
     "Gäller nu",
     ["[RULE-FRX-048-001](rule-frx-048-001.md)", "[RULE-RR-012-001](rule-rr-012-001.md) — Oberoende övervakning"],
     ["återvändande", "regel", "frontex"]),

    ("return", "RULE-FRX-053-001",
     f"[Förordning (EU) 2019/1896 artikel 53]({RET}/frontex.md)",
     "Tidsfrist",
     "Om en medlemsstat ställs inför en belastning när den ska återsända personer får Frontex, på eget initiativ med samtycke eller på begäran, ge stöd genom en **återvändandeintervention** (53.1). Vid specifika och oproportionella utmaningar ges en **snabb återvändandeintervention** (53.2). Den verkställande direktören utarbetar utan dröjsmål en operativ plan (53.3) och beslutar om den snarast möjligt, vid snabb intervention **inom fem arbetsdagar** (53.4).",
     "Ger förstärkning när ett lands återvändandesystem är hårt belastat.",
     "Sverige begär en återvändandeintervention.",
     ["Beslut om operativ plan vid snabb intervention: **högst fem arbetsdagar** från begäran (startpunkt anges inte uttryckligen).",
      "Beslutet meddelas omedelbart skriftligen."],
     "Gäller nu",
     ["[RULE-FRX-050-001](rule-frx-050-001.md)"],
     ["återvändande", "regel", "frontex", "tidsfrister"]),

    ("return", "RULE-UTL-12-014-001",
     f"[Utlänningslagen 12 kap. 14 och 14 a §§]({RET}/utlanningslagen.md)",
     "Obligation",
     "**Migrationsverket** verkställer beslut om avvisning eller utvisning, om inte annat följer av paragrafen. **Säkerhetspolisen** verkställer i säkerhetsärenden. **Polismyndigheten** verkställer sina egna avvisningsbeslut, allmän domstols utvisning på grund av brott och beslut som ska verkställas på nytt (14 §). Migrationsverket får lämna över ärendet till Polismyndigheten om personen **håller sig undan** eller om det kan antas att **tvång** behövs (14 a §).",
     "Anger vilken myndighet som ansvarar för ambassadkontakter och resa i det enskilda ärendet.",
     "Ett beslut om avvisning eller utvisning ska verkställas.",
     ["Ansvarig myndighet styr vem som sköter identifiering, resehandling och resa.",
      "Överlämnande till Polismyndigheten vid avvikande eller behov av tvång."],
     "Gällande rätt (lydelse t.o.m. SFS 2026:1752)",
     ["[RULE-UTL-12-015-001](rule-utl-12-015-001.md)"],
     ["återvändande", "regel", "nationell", "verkställighet"]),

    ("return", "RULE-UTL-12-014C-001",
     f"[Utlänningslagen 12 kap. 14 b och 14 c §§]({RET}/utlanningslagen.md)",
     "Befogenhet",
     "Den verkställande myndigheten får **upphäva** en tidsfrist för frivillig avresa om det under fristen uppstår risk för avvikande eller risk för allmän ordning eller säkerhet. Beslutet gäller omedelbart och förenas som huvudregel med återreseförbud på **högst fem år** (14 b §). Om det av **särskilda skäl** behövs en längre tidsfrist får Migrationsverket eller Polismyndigheten **förlänga** fristen eller bestämma en **ny frist** efter att den löpt ut (14 c §).",
     "Gör det möjligt att anpassa avresefristen efter hur resan kan ordnas.",
     "Resan kan inte ordnas inom fristen, eller risk för avvikande uppstår.",
     ["Förlängning eller ny frist vid särskilda skäl, till exempel när resehandling inte hunnit utfärdas.",
      "Upphävande av fristen leder till verkställighet snarast möjligt (15 §)."],
     "Gällande rätt (lydelse t.o.m. SFS 2026:1752)",
     ["[RULE-RR-005-004](rule-rr-005-004.md) — Förlängning enligt förordning 2026/2280 (från 17 okt 2027)"],
     ["återvändande", "regel", "nationell", "tidsfrister"]),

    ("return", "RULE-UTL-12-015-001",
     f"[Utlänningslagen 12 kap. 15 och 15 a §§]({RET}/utlanningslagen.md)",
     "Tidsfrist",
     "Ett beslut **utan** tidsfrist för frivillig avresa ska verkställas **snarast möjligt**. Om beslutet har en tidsfrist ska personen lämna landet senast när fristen löper ut. Har personen inte lämnat landet då, eller har fristen upphävts, ska beslutet verkställas **snarast möjligt därefter** (15 §). Har personen inte lämnat landet när fristen löpt ut ska myndigheten meddela **återreseförbud** på högst fem år, utom vid inhibition, ansökan om uppehållstillstånd eller ny prövning, eller särskilda skäl (15 a §).",
     "Bestämmer när verkställigheten, och därmed resan, ska ske.",
     "Tidsfristen för frivillig avresa löper ut, eller beslutet saknar tidsfrist.",
     ["Planering av resa ska ske så att verkställighet sker snarast möjligt efter fristens utgång.",
      "EES-medborgare: tidigast fyra veckor efter delgivning, om inte synnerliga skäl finns (15 § tredje st.)."],
     "Gällande rätt (lydelse t.o.m. SFS 2026:1752)",
     ["[RULE-RR-010-001](rule-rr-010-001.md) — Skyldighet att avlägsna (från 17 okt 2027)"],
     ["återvändande", "regel", "nationell", "tidsfrister"]),

    ("return", "RULE-UTL-12-021-001",
     f"[Utlänningslagen 12 kap. 21 och 22 §§]({RET}/utlanningslagen.md)",
     "Villkor",
     "Ett beslut om avvisning eller utvisning ska anses **verkställt** om utlänningen har **lämnat landet**, med undantag för vissa straffrättsliga överföringar (21 §). Ett beslut som inte meddelats av allmän domstol **upphör att gälla fem år** från det att personen lämnat landet i enlighet med beslutet, eller senare om ett återreseförbud då fortfarande löper (22 §).",
     "Anger när resan avslutar ärendet och hur länge beslutet gäller därefter.",
     "Personen lämnar landet.",
     ["Avresedatum ska registreras: det avgör att beslutet är verkställt och när femårsfristen och ett eventuellt inreseförbud börjar löpa ([RULE-RR-008-007](rule-rr-008-007.md))."],
     "Gällande rätt (lydelse t.o.m. SFS 2026:1752)",
     ["[RULE-RR-008-007](rule-rr-008-007.md) — Inreseförbudets startpunkt"],
     ["återvändande", "regel", "nationell", "tidsfrister"]),
]


def write(rule):
    domain, rid, basis, rtype, text, purpose, trigger, effects, applies, related, tags = rule
    lines = ["---", "tags:"] + [f"  - {t}" for t in tags] + ["---", "", f"# {rid}", "",
             "## Rättslig grund", "", basis, "", "---", "", "## Regeltyp", "", rtype, "", "---", "",
             "## Regel", "", text, "", "---", "", "## Syfte", "", purpose, "", "---", "",
             "## Utlösare", "", trigger, "", "---", "", "## Rättsverkan", ""]
    lines += [f"- {e}" for e in effects]
    lines += ["", "---", "", "## Tillämpas från", "", applies, "", "---", "", "## Relaterade regler", ""]
    lines += [f"- {r}" for r in related]
    lines += ["", "---", "", "## Status", "", "Complete (kontrollerad mot källtexten)", ""]
    out = ROOT / domain / "rules" / f"{rid.lower()}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


if __name__ == "__main__":
    for r in RULES:
        print(write(r).relative_to(ROOT))

#!/usr/bin/env python3
"""Skapar regler för modulen Förvar (docs/shared/detention/rules) från utlänningslagen 10 kap.,
16 kap. 4 § och återvändandedirektivet 2008/115/EG art. 15.

Innehållet är kontrollerat mot references/_text/nationella/Utlänningslag ... .txt (lydelse t.o.m.
SFS 2026:1752) och references/_text/OJ_L_2008348_SV_TXT.txt. Paragrafnummer avser nuvarande lydelse.
Från 1 december 2027 får 10 kap. nya paragrafnummer (anges i varje regel).
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "docs" / "shared" / "detention" / "rules"
UTL = "../../../references/legislation/utlanningslagen.md"
RD = "../../../references/legislation/return-directive.md"
NOW = "Gällande lydelse (t.o.m. SFS 2026:1752)"


def utl(par, new):
    return f"{NOW}. Från 1 december 2027: 10 kap. {new} § (ny numrering, SFS 2026:1427)"


RULES = [
    ("RULE-UTL-10-002-001", f"[Utlänningslagen 10 kap. 2 §]({UTL})", "Villkor",
     "En utlänning får tas i förvar **endast om syftet inte kan uppnås genom uppsikt**.",
     "Förvar är sista utväg. Uppsikt ska prövas först.",
     "Varje beslut om förvar.",
     ["Beslutet ska visa varför uppsikt inte räcker.",
      "Motsvarar kraven på mindre ingripande alternativ i AMMR art. 44.2, direktiv 2008/115/EG art. 15.1, förordning 2024/1349 art. 5.1 och förordning 2026/2280 art. 23 och 29."],
     utl(2, 4), ["[RULE-UTL-10-014-001](rule-utl-10-014-001.md)"], ["villkor"]),

    ("RULE-UTL-10-003-001", f"[Utlänningslagen 10 kap. 3 §]({UTL})", "Villkor",
     "En utlänning som fyllt 18 år får ställas under uppsikt eller tas i förvar **under den tid utlänningen har rätt att vistas i Sverige som sökande av internationellt skydd**, om det är nödvändigt **1)** för att bestämma eller bekräfta identitet eller nationalitet, **2)** för att utreda omständigheterna som ansökan grundas på, **3)** om utlänningen inte följt ett beslut om boende på bestämd plats (mottagandelagen 3 kap. 3 § första st.) och det finns risk för avvikande, **4)** som led i ett **gränsförfarande** enligt APR art. 43 för att avgöra rätten att resa in, **5)** om utlänningen redan hålls i förvar enligt 5 § första st. 2 när ansökan görs och det finns anledning att anta att syftet är att försena eller hindra verkställigheten, **6)** med hänsyn till nationell säkerhet eller allmän ordning, eller **7)** i enlighet med **AMMR art. 44**. Den som av allmän domstol utvisats på grund av brott omfattas i stället av 5 §.",
     "Anger förvarsgrunderna för asylsökande.",
     "Utlänningen är sökande av internationellt skydd och har rätt att vistas här.",
     ["Grunderna upphör när rätten att vistas som sökande upphör, t.ex. när avslaget får verkställas. Då krävs ett nytt beslut enligt 5 § eller frigivning ([PROC-DET-002](../processes/change-of-ground.md)).",
      "Varje grund har en egen längsta tid ([RULE-UTL-10-011-001](rule-utl-10-011-001.md)).",
      "Punkt 7 hänvisar till AMMR; tidsgränserna följer då av AMMR art. 45 ([RULE-AMMR-045-001](../../../domains/responsibility/rules/rule-ammr-045-001.md))."],
     utl(3, 5), ["[RULE-UTL-10-011-001](rule-utl-10-011-001.md)", "[RULE-UTL-10-004-001](rule-utl-10-004-001.md)"], ["villkor", "förvarsgrund"]),

    ("RULE-UTL-10-004-001", f"[Utlänningslagen 10 kap. 4 §]({UTL})", "Villkor",
     "Ett **barn** som är sökande får ställas under uppsikt eller tas i förvar om barnet inte följt ett beslut om boende på bestämd plats och det finns en **uppenbar** risk för avvikande, med hänsyn till nationell säkerhet eller allmän ordning, eller i enlighet med AMMR art. 44.",
     "Snävare förvarsgrunder för barn som söker skydd.",
     "Ett barn som är sökande av internationellt skydd.",
     ["Barn får inte skiljas från vårdnadshavare genom förvar, och barn utan vårdnadshavare här får tas i förvar bara vid synnerliga skäl (7–8 §§).",
      "Tidsgräns 72 timmar + 72 timmar ([RULE-UTL-10-013-001](rule-utl-10-013-001.md)).",
      "Punkterna är numrerade 1, 4 och 5 i källtexten (rättsdatabaserna, lydelse SFS 2026:1426). Hänvisningen \"första stycket 1, 3 och 4\" i andra stycket stämmer inte med numreringen. Kontrollera mot SFS-trycket."],
     utl(4, 6), ["[RULE-UTL-10-013-001](rule-utl-10-013-001.md)"], ["villkor", "förvarsgrund", "barn"]),

    ("RULE-UTL-10-005-001", f"[Utlänningslagen 10 kap. 5 §]({UTL})", "Villkor",
     "I andra fall än 3 § får en utlänning som fyllt 18 år ställas under uppsikt eller tas i förvar **1)** om det är nödvändigt för en utredning av identitet eller rätt att resa in eller stanna i Sverige, eller **2)** om det kan antas att utlänningen kommer att avvisas eller utvisas, eller ett sådant beslut ska verkställas, och det finns risk för brottslig verksamhet, avvikande, att utlänningen håller sig undan eller på annat sätt försvårar verkställigheten. Artikel 5 i förordning 2024/1349 (återvändandegränsförfarandet) ger **ytterligare** möjlighet till förvar (andra stycket).",
     "Anger förvarsgrunderna för den som inte är sökande, främst inför och under verkställighet.",
     "Utlänningen är inte, eller inte längre, sökande av internationellt skydd.",
     ["Punkt 1: högst 4 veckor ([RULE-UTL-10-011-001](rule-utl-10-011-001.md)).",
      "Punkt 2: 6 + 12 månader m.m. ([RULE-UTL-10-012-001](rule-utl-10-012-001.md)).",
      "Andra stycket: förvar under återvändandegränsförfarandet, högst lika länge som tolvveckorsperioden ([RULE-RET-005-001](../../../domains/return-border-procedure/rules/rule-ret-005-001.md))."],
     utl(5, 7), ["[RULE-UTL-10-012-001](rule-utl-10-012-001.md)"], ["villkor", "förvarsgrund"]),

    ("RULE-UTL-10-006-001", f"[Utlänningslagen 10 kap. 6–8 §§]({UTL})", "Villkor",
     "I andra fall än 4 § får ett **barn** ställas under uppsikt eller tas i förvar om det är sannolikt att barnet avvisas av Polismyndigheten eller med omedelbar verkställighet av Migrationsverket, eller om ett beslut om avvisning eller utvisning ska verkställas, och det annars finns en **uppenbar** risk för brott, avvikande eller att verkställigheten försvåras (6 §). Barn eller vårdnadshavare får inte tas i förvar om barnet då skiljs från vårdnadshavaren (7 §). Ett barn utan vårdnadshavare i Sverige får tas i förvar bara om det finns **synnerliga skäl** (8 §).",
     "Skyddar barn mot förvar och mot att skiljas från vårdnadshavare.",
     "Ett barn som inte är sökande, eller vars vårdnadshavare övervägs tas i förvar.",
     ["Tidsgräns 72 timmar + 72 timmar ([RULE-UTL-10-013-001](rule-utl-10-013-001.md))."],
     f"{NOW}. Från 1 december 2027: 10 kap. 8–10 §§", ["[RULE-UTL-10-004-001](rule-utl-10-004-001.md)"], ["villkor", "förvarsgrund", "barn"]),

    ("RULE-UTL-10-011-001", f"[Utlänningslagen 10 kap. 11 §]({UTL})", "Tidsfrist",
     "En utlänning får inte hållas i förvar längre än **1) fyra veckor** med stöd av 3 § första st. 1 eller 2 (identitet, utreda grunder) eller 5 § första st. 1 (utredning av rätt att resa in eller stanna), **2) tolv veckor** med stöd av 3 § första st. 4 (gränsförfarandet), och **3) tolv månader** med stöd av 3 § första st. 3, 5 eller 6 (boendebeslut och avvikanderisk, ansökan för att försena verkställighet, säkerhet eller allmän ordning).",
     "Sätter tak per förvarsgrund för asylsökande och vid utredning.",
     "Förvar med stöd av någon av de angivna grunderna.",
     ["Taket gäller per grund. Lagen säger inte uttryckligen om tid med olika grunder ska räknas samman för vuxna ([öppen fråga](../open_questions/aggregation-of-detention-time.md)).",
      "3 § första st. 7 (AMMR art. 44) har inget tak här. Tidsgränserna följer av AMMR art. 45: överföring inom 5 veckor, annars frigivning.",
      "Barn: [RULE-UTL-10-013-001](rule-utl-10-013-001.md)."],
     utl(11, 14), ["[RULE-UTL-10-012-001](rule-utl-10-012-001.md)", "[RULE-AMMR-045-001](../../../domains/responsibility/rules/rule-ammr-045-001.md)"], ["tidsfrister"]),

    ("RULE-UTL-10-012-001", f"[Utlänningslagen 10 kap. 12 §]({UTL})", "Tidsfrist",
     "Förvar med stöd av 5 § första st. 2 (inför och under verkställighet) får inte pågå längre än **sex månader**. Om bristande samarbete eller tid för att skaffa handlingar gör att verkställigheten sannolikt dröjer längre, får förvaret pågå **ytterligare högst tolv månader**. Gränserna gäller **inte** den som av allmän domstol utvisats på grund av brott (första st.). Inför avvisning eller utvisning till en **EES-stat**: högst sex månader, vid särskilda skäl tolv månader (andra st.). I ett **säkerhetsärende**: högst tolv månader, och vid bristande samarbete, tid för handlingar eller annat väsentligt verkställighetsskäl ytterligare högst tolv månader (tredje st.).",
     "Sätter tak för förvar inför verkställighet, i linje med direktiv 2008/115/EG art. 15.5–15.6.",
     "Förvar med stöd av 5 § första st. 2.",
     ["Ordinarie: 6 månader, högst 18 månader totalt.",
      "EES-stat: 6, högst 12 månader.",
      "Säkerhetsärende: 12, högst 24 månader.",
      "Brottsutvisad av allmän domstol: inget tak i lagen.",
      "Från 17 oktober 2027 gäller förordning 2026/2280 art. 30 (12 + 12 + 6 månader). Den svenska gränsen 18 månader ligger inom förordningens tak."],
     utl(12, 15), ["[RULE-RD-015-001](rule-rd-015-001.md)", "[RULE-RR-030-002](../../../domains/return/rules/rule-rr-030-002.md)"], ["tidsfrister"]),

    ("RULE-UTL-10-013-001", f"[Utlänningslagen 10 kap. 13 §]({UTL})", "Tidsfrist",
     "Ett **barn** får inte hållas i förvar längre än **72 timmar**, eller vid synnerliga skäl **ytterligare 72 timmar**. I ett **säkerhetsärende** får ett barn inte hållas i förvar med stöd av 4 § första st. 1, 3 eller 4 eller 6 § längre **sammanlagd** tid än **tre månader**, eller vid synnerliga skäl **sex månader**. Gränserna gäller även barn som utvisats på grund av brott.",
     "Begränsar förvar av barn till kortast möjliga tid.",
     "Ett barn hålls i förvar.",
     ["Säkerhetsärenden: tiden räknas **sammanlagt**, även över flera beslut.",
      "Ny prövning i säkerhetsärende varje månad ([RULE-UTL-10-017-001](rule-utl-10-017-001.md))."],
     utl(13, 16), ["[RULE-UTL-10-004-001](rule-utl-10-004-001.md)", "[RULE-UTL-10-006-001](rule-utl-10-006-001.md)"], ["tidsfrister", "barn"]),

    ("RULE-UTL-10-014-001", f"[Utlänningslagen 10 kap. 14 §]({UTL})", "Obligation",
     "Ett beslut om uppsikt eller förvar ska **omedelbart upphävas** om det inte längre finns skäl för beslutet. Ett beslut om uppsikt kan upphävas helt eller delvis.",
     "Förvar får aldrig pågå längre än skälet består, oavsett tak och prövningsintervall.",
     "Skälet för förvaret faller bort, till exempel genom ett beslut i ett annat ärende.",
     ["Varje händelse som påverkar grunden ska leda till en kontroll ([PROC-DET-002](../processes/change-of-ground.md))."],
     utl(14, 17), ["[RULE-UTL-10-023-001](rule-utl-10-023-001.md)"], ["upphörande"]),

    ("RULE-UTL-10-015-001", f"[Utlänningslagen 10 kap. 15 §]({UTL})", "Tidsfrist",
     "Så länge en utlänning står under **uppsikt** ska beslutet prövas på nytt **inom sex månader** från beslutsdagen och därefter fortlöpande inom sex månader från senaste prövningen. **Från 1 december 2027:** vid **förstärkt uppsikt** (elektronisk övervakning) inom **tre månader**, och för ett **barn** under förstärkt uppsikt inom **en månad**.",
     "Säkerställer att uppsikt inte pågår utan regelbunden prövning.",
     "Ett beslut om uppsikt gäller.",
     ["Utebliven prövning: beslutet upphör ([RULE-UTL-10-019-001](rule-utl-10-019-001.md)).",
      "Förstärkt uppsikt av barn: högst 3 månader, synnerliga skäl 6. Säkerhetsärende 12, synnerliga skäl 18 (10 kap. 13 § från 1 december 2027)."],
     utl(15, 18), ["[RULE-UTL-10-016-001](rule-utl-10-016-001.md)"], ["tidsfrister", "uppsikt"]),

    ("RULE-UTL-10-016-001", f"[Utlänningslagen 10 kap. 16 §]({UTL})", "Tidsfrist",
     "Ett beslut om förvar enligt 3 § första st. 3–7, 5 § första st. 2 eller andra st. eller 9 § ska prövas på nytt **inom två månader** från den dag då **verkställigheten påbörjades**. Om beslutet föregicks av ett **interimistiskt** beslut (24 §) räknas fristen från den dag det interimistiska beslutet verkställdes. Därefter görs ny prövning fortlöpande **inom två månader från det senaste förvarsbeslutet**.",
     "Garanterar regelbunden prövning av längre förvar.",
     "Förvar med stöd av de angivna grunderna.",
     ["Gäller inte förvar enligt 3 § första st. 1–2 eller 5 § första st. 1, som har tak på fyra veckor.",
      "Varje ny prövning föregås av muntlig förhandling ([RULE-UTL-10-018-001](rule-utl-10-018-001.md)).",
      "Utebliven prövning: beslutet upphör ([RULE-UTL-10-019-001](rule-utl-10-019-001.md)).",
      "Om ett nytt förvarsbeslut med ny grund startar en ny tvåmånadersperiod från verkställigheten (första st.) eller räknas från det senaste förvarsbeslutet (andra st.) framgår inte entydigt ([PROC-DET-002](../processes/change-of-ground.md))."],
     utl(16, 19), ["[RULE-UTL-10-017-001](rule-utl-10-017-001.md)", "[RULE-UTL-10-019-001](rule-utl-10-019-001.md)"], ["tidsfrister", "prövning"]),

    ("RULE-UTL-10-017-001", f"[Utlänningslagen 10 kap. 17 §]({UTL})", "Tidsfrist",
     "Förvar av ett **barn i ett säkerhetsärende**, eller av ett barn som av allmän domstol utvisats på grund av brott, ska prövas på nytt **inom en månad** från verkställighetens början (eller från verkställigheten av ett interimistiskt beslut), och därefter fortlöpande inom en månad från senaste förvarsbeslutet.",
     "Tätare prövning för barn i långvarigt förvar.",
     "Förvar av barn i säkerhetsärende eller efter brottsutvisning.",
     ["Utebliven prövning: beslutet upphör ([RULE-UTL-10-019-001](rule-utl-10-019-001.md))."],
     utl(17, 20), ["[RULE-UTL-10-013-001](rule-utl-10-013-001.md)"], ["tidsfrister", "prövning", "barn"]),

    ("RULE-UTL-10-018-001", f"[Utlänningslagen 10 kap. 18 §]({UTL})", "Obligation",
     "Varje **ny prövning** av ett beslut om förvar ska föregås av **muntlig förhandling**. Detsamma gäller ny prövning av uppsikt, om det inte är uppenbart att förhandlingen saknar betydelse. Bestämmelser om förhandlingen finns i 13 kap. 2–8 §§.",
     "Säkerställer att personen hörs vid varje prövning.",
     "Ny prövning enligt 15–17 §§.",
     ["Förhandlingen måste planeras in i god tid före fristens utgång."],
     utl(18, 21), ["[RULE-UTL-10-016-001](rule-utl-10-016-001.md)"], ["prövning"]),

    ("RULE-UTL-10-019-001", f"[Utlänningslagen 10 kap. 19 §]({UTL})", "Obligation",
     "Om ett beslut om uppsikt eller förvar **inte prövas på nytt inom föreskriven tid upphör beslutet att gälla**.",
     "Gör prövningsfristerna till hårda frister med automatisk rättsföljd.",
     "Fristen för ny prövning enligt 15–17 §§ passeras utan prövning.",
     ["Personen ska friges. Fristen är kritisk för bevakning i systemet."],
     utl(19, 22), ["[RULE-UTL-10-016-001](rule-utl-10-016-001.md)"], ["tidsfrister", "upphörande"]),

    ("RULE-UTL-10-020-001", f"[Utlänningslagen 10 kap. 20–22 och 24 §§]({UTL})", "Befogenhet",
     "**Polismyndigheten** beslutar om uppsikt och förvar när den handlägger ett avvisningsärende eller ska verkställa ett beslut om avvisning eller utvisning, och behåller behörigheten när verkställighetshinder åberopats tills Migrationsverket beslutat om prövning ska beviljas (20 §). **Säkerhetspolisen** beslutar när den ska verkställa (21 §). I övrigt beslutar **Migrationsverket** (22 §). Polismyndigheten får fatta ett **interimistiskt** beslut om det inte finns tid att avvakta behörig myndighet. Beslutet ska skyndsamt anmälas och prövas omedelbart, och upphör när behörig myndighet beslutat. En polisman får omhänderta enligt 11 § polislagen i avvaktan på beslut (24 §).",
     "Anger vem som fattar förvarsbeslut i varje skede.",
     "Förvar beslutas eller ärendet byter ansvarig myndighet (t.ex. överlämnas till Polismyndigheten för verkställighet).",
     ["När ansvaret för ärendet byter myndighet kan också beslutsfattaren för förvaret bytas.",
      "Interimistiskt beslut: tvåmånadersfristen räknas från dess verkställighet (16 §)."],
     f"{NOW}. Från 1 december 2027: 10 kap. 23–25 och 27 §§", ["[RULE-UTL-12-014-001](../../../domains/return/rules/rule-utl-12-014-001.md)"], ["beslutsfattare"]),

    ("RULE-UTL-10-023-001", f"[Utlänningslagen 10 kap. 23 §]({UTL})", "Obligation",
     "Migrationsverket ska **upphäva** ett beslut om uppsikt eller förvar om verket **beviljar uppehållstillstånd eller internationellt skydd**. När verket prövar en sådan fråga får det besluta om **inhibition** av förvarsbeslutet. Om en domstol beslutar i frågan gäller detsamma domstolen.",
     "Kopplar förvaret direkt till utgången i tillstånds- och skyddsärendet.",
     "Beslut om uppehållstillstånd eller internationellt skydd, eller pågående prövning av sådan fråga.",
     ["Beviljat tillstånd eller skydd: förvaret ska upphävas i samma beslut.",
      "Inhibition: förvaret verkställs inte under prövningen."],
     utl(23, 26), ["[RULE-UTL-10-014-001](rule-utl-10-014-001.md)"], ["upphörande"]),

    ("RULE-UTL-16-004-001", f"[Utlänningslagen 16 kap. 4 §]({UTL})", "Tidsfrist",
     "Mål om förvar ska handläggas skyndsamt. En migrationsdomstol ska meddela slutligt avgörande i ett mål om förvar enligt **10 kap. 3 eller 4 §** (asylsökande) **inom 15 dagar**, eller vid särskilda skäl **21 dagar**, från den dag överklagandet kom in. Om avgörandet inte meddelas inom 21 dagar **upphör det överklagade beslutet att gälla**.",
     "Snabb domstolsprövning av förvar av asylsökande.",
     "Ett beslut om förvar av en asylsökande överklagas till migrationsdomstol.",
     ["Fristen löper från överklagandets ankomst till domstolen.",
      "Gäller inte förvar enligt 10 kap. 5–6 § (där krävs skyndsam handläggning men ingen dagsfrist).",
      "Från 1 december 2027 hänvisar paragrafen till 10 kap. 5 eller 6 § (ny numrering), samma grunder."],
     f"{NOW}", ["[RULE-UTL-10-003-001](rule-utl-10-003-001.md)"], ["tidsfrister", "domstol"]),

    ("RULE-RD-015-001", f"[Direktiv 2008/115/EG artikel 15]({RD})", "Tidsfrist",
     "Förvar för återvändande får bara användas om mindre ingripande åtgärder inte räcker, särskilt vid risk för avvikande eller om personen håller sig undan eller hindrar förberedelserna (15.1). Beslut ska vara skriftligt och motiverat, och vid administrativt beslut ska snabb rättslig prövning ske (15.2). Förvaret ska prövas med rimliga intervall (15.3). När **rimliga utsikter till avlägsnande saknas** ska personen **omedelbart friges** (15.4). Varje medlemsstat ska fastställa en förvarsperiod på **högst sex månader** (15.5), som får förlängas med **högst tolv månader** vid bristande samarbete eller dröjsmål med handlingar från tredjeland (15.6).",
     "EU-ramen för förvar inför återvändande som gäller fram till 17 oktober 2027.",
     "Förvar inför återvändande.",
     ["Genomförs genom utlänningslagen 10 kap. 5 § första st. 2 och 12 §.",
      "Förvar under återvändandegränsförfarandet räknas in i maxperioderna i 15.5–15.6 om ett påföljande förvar beslutas direkt efter (förordning 2024/1349 art. 5.4).",
      "Ersätts 17 oktober 2027 av förordning 2026/2280 art. 29–33."],
     "Gäller till 17 oktober 2027 (förordning 2026/2280 art. 49)",
     ["[RULE-UTL-10-012-001](rule-utl-10-012-001.md)", "[RULE-RET-005-001](../../../domains/return-border-procedure/rules/rule-ret-005-001.md)"], ["tidsfrister"]),
]


def write(r):
    rid, basis, rtype, text, purpose, trigger, effects, applies, related, extra_tags = r
    tags = ["förvar", "regel"] + extra_tags
    lines = ["---", "tags:"] + [f"  - {t}" for t in tags] + ["---", "",
             "← [Förvar](../README.md)", "", f"# {rid}", "",
             "## Rättslig grund", "", basis, "", "---", "", "## Regeltyp", "", rtype, "", "---", "",
             "## Regel", "", text, "", "---", "", "## Syfte", "", purpose, "", "---", "",
             "## Utlösare", "", trigger, "", "---", "", "## Rättsverkan", ""]
    lines += [f"- {e}" for e in effects]
    lines += ["", "---", "", "## Tillämpas från", "", applies, "", "---", "", "## Relaterade regler", ""]
    lines += [f"- {x}" for x in related]
    lines += ["", "---", "", "## Status", "", "Complete (kontrollerad mot källtexten)", ""]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{rid.lower()}.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    for r in RULES:
        write(r)
    print(f"{len(RULES)} regler i {OUT}")

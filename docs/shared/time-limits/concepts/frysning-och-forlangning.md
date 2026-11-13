---
tags:
  - shared
  - tidsfrister
  - koncept
  - suspensiv-verkan
  - förlängning
  - frysning
---

# Frysning och förlängning av tidsfrister

## Översikt

Migrationspaktens tidsfrister är som utgångspunkt absoluta. De löper och vid överskridande inträder rättsliga följder, till exempel ansvarsövergång, frigivning eller att förfarandet avslutas. Förordningarna innehåller tre sorters mekanismer som påverkar en frist:

```text
TIDSFRISTER
│
├── FRYSNING (ny startpunkt)
│       Ett överklagande med suspensiv verkan gör att fristen räknas från
│       det slutliga beslutet om överklagandet. En NY FULL frist börjar löpa.
│
├── FÖRLÄNGNING
│       Fristen ersätts av en längre frist, alltid med ett tak.
│       Grunder: massinflöde, komplexitet, sökandens försummelse,
│       frihetsberövande, avvikande, tekniska problem, kris m.fl.
│
├── UPPSKJUTANDE / SPÄRR
│       Förfarandet eller verkställigheten skjuts upp utan en ny fast
│       frist, eller med en yttersta gräns (t.ex. 21 månader).
│
└── FÖRKORTNING
        Fristen ersätts av en kortare frist när ett villkor är uppfyllt.
        Grunder: förvar, träff i Eurodac eller VIS, gränsförfarande,
        påskyndat förfarande, bilateral överenskommelse m.fl.
```

Sidan listar **alla** frister i förordningarna som kan frysas, förlängas, skjutas upp eller förkortas. Först kommer en översikt per process, sedan detaljerna per mekanism och förordning. Den är kontrollerad mot förordningstexten i `references/_text/` (APR 2024/1348, AMMR 2024/1351, Eurodac 2024/1358, kris 2024/1359, genomförandeförordning 2025/2055) screeningförordningen 2024/1356 och förordning 2024/1349 om gränsförfarandet för återvändande.

---

## Översikt per process

Alla processer i kunskapsbasen. "—" betyder att förordningen inte innehåller någon sådan mekanism för processens frister.

| Process | Frist | Frysning | Förlängning | Uppskjutande / spärr | Avsnitt |
|---------|-------|----------|-------------|----------------------|---------|
| [PROC-SCR-001](../../../domains/screening/processes/screening-at-external-border.md) Screening vid yttre gräns | 7 dagar | — | — (kan **förkortas** till 4 dagar efter 72 h vid gränsen) | — | [4](#4-frister-som-uttryckligen-inte-forlangs-eller-paverkas) |
| [PROC-SCR-002](../../../domains/screening/processes/screening-within-territory.md) Screening inom territoriet | 3 dagar | — | — | — | [4](#4-frister-som-uttryckligen-inte-forlangs-eller-paverkas) |
| [PROC-EUR-001](../../../domains/eurodac/processes/collect-and-transmit-biometric-data.md) Biometri till Eurodac | 72 h (10 dagar vid tillfälligt skydd) | — (ny startpunkt 48 h efter hälsohinder) | +48 h vid tekniska problem, +48 h vid plötslig tillströmning (sök och räddning) | — | [2](#eurodac-insamling-och-overforing) |
| [PROC-REG-001](../../../domains/registration/processes/registration-of-an-application.md) Registrering | 5 dagar | — | 15 dagar (massinflöde), 4 veckor (kris) | — | [2](#registrering-och-inlamnande-apr), [2](#registrering-vid-kris-kris-art-10) |
| [PROC-REG-002](../../../domains/registration/processes/lodging-an-application.md) Inlämnande | 21 dagar (5 dagar vid gräns) | — | Bokad tid inom 2 månader (massinflöde) | — | [2](#registrering-och-inlamnande-apr) |
| [PROC-REG-003](../../../domains/registration/processes/issue-applicant-documents.md) Sökandens handlingar | Giltighet upp till 12 mån | — | Hela perioden med rätt att stanna kvar (ansvarig stat) | — | [2](#registrering-och-inlamnande-apr) |
| [PROC-RES-001](../../../domains/responsibility/processes/determine-responsible-member-state.md) Ansvarig medlemsstat och överföring | Framställan 2 mån, svar 1 mån, återtagande 2 v, överföring 6 mån (5 v vid förvar) | **Ja**: överföringsfristen får ny startpunkt vid suspensiv verkan | Överföring 1 år (frihetsberövad) / 3 år (avvikande m.m.). Framställan förlängs vid undanhållna uppgifter. Företrädare +10 arbetsdagar. Kris: 4 mån / 2 mån / 1 mån / 1 år | Domstolens beslut om uppskov inom 1 mån. Kris: överföringar till krisstat skjuts upp | [1](#1-frysning-ny-startpunkt-vid-suspensiv-verkan), [2](#ansvar-och-overforing-ammr), [2](#ansvar-vid-kris-kris-art-12), [3](#3-uppskjutande-och-sparrar) |
| [PROC-ASY-001](../../../domains/asylum-procedure/processes/examine-an-application.md) Prövning | Upptagande 2 mån, sak 6 mån, påskyndat 3 mån | — | +2 mån (upptagande), +6 mån (sak) | Uppskjutande vid osäkra förhållanden i ursprungslandet (max 21 mån). Uppskjutande innan implicit återkallande | [2](#provning-apr), [3](#3-uppskjutande-och-sparrar) |
| [PROC-ASY-002](../../../domains/asylum-procedure/processes/subsequent-application.md) Efterföljande ansökan | Samma som PROC-ASY-001 | — | Samma som PROC-ASY-001 (inga egna) | Samma som PROC-ASY-001 | [4](#4-frister-som-uttryckligen-inte-forlangs-eller-paverkas) |
| [PROC-BRD-001](../../../domains/border-procedure/processes/asylum-border-procedure.md) Gränsförfarande för asyl | 12 veckor | — | 16 veckor (efter omfördelning) **eller** 18 veckor (kris), inte båda | — | [2](#gransforfarande-apr-och-kris) |
| [PROC-RET-001](../../../domains/return-border-procedure/processes/return-border-procedure.md) Gränsförfarande för återvändande | 12 veckor, frivillig avresa högst 15 dagar | — (startar först när rätten att stanna kvar upphört) | +6 veckor vid kris | — | [1](#1-frysning-ny-startpunkt-vid-suspensiv-verkan), [2](#gransforfarande-for-atervandande-forordning-20241349) |
| [PROC-SOL-001](../../../domains/solidarity/processes/relocation.md) Omfördelning (översikt) | Besked 1 v, beslut 1 v, överföring 4 v | **Ja**: överföringen | Besked högst 2 v | — | Se PROC-SOL-002/003 |
| [PROC-SOL-002](../../../domains/solidarity/processes/relocation-out.md) Omfördelning UT | Beslut 1 v, överföring 4 v | **Ja**: överföringen | — | — | [1](#1-frysning-ny-startpunkt-vid-suspensiv-verkan) |
| [PROC-SOL-003](../../../domains/solidarity/processes/relocation-in.md) Omfördelning IN | Besked 1 v | — | Högst 2 v (komplicerad granskning eller många ärenden) | — | [2](#omfordelning-ammr-art-67) |
| [PROC-CRI-001](../../../domains/crisis/processes/activate-crisis-measures.md) Krisåtgärder | (förlänger andra processers frister) | Överföring vid kris: **ja** | Registrering, gränsförfarande, ansvar, återvändande vid gräns | Spärr för överföringar till krisstat | [2](#ansvar-vid-kris-kris-art-12), [3](#3-uppskjutande-och-sparrar) |

---

## 1. Frysning — ny startpunkt vid suspensiv verkan

### Mekanism

När ett överföringsbeslut överklagas och domstolen beviljar **suspensiv verkan** ([AMMR art. 43.3](../../../domains/responsibility/articles/ammr-043.md)) löper överföringsfristen inte. Fristen räknas i stället från det **slutliga beslutet** om överklagandet, eller vid förvar från **den dag den suspensiva verkan upphör**.

```text
Accept → (frist börjar) → Överklagande + suspensiv verkan → … → Slutligt beslut → NY FULL FRIST börjar
```

- Fristen **pausas inte** och fortsätter inte där den var. En ny, full frist börjar löpa från den nya startpunkten.
- Domstolen ska besluta om suspensiv verkan inom en månad från begäran, och ska sträva efter att avgöra överklagandet i sak inom en månad från beslutet att bevilja suspensiv verkan (art. 43.3).
- Om personen inte begärt suspensiv verkan avbryter överklagandet inte verkställigheten (art. 43.3).

### Frister som fryses

| Domän | Frist | Ny startpunkt | Fristtyp | Rättslig grund | Regel / process |
|-------|-------|---------------|----------|----------------|-----------------|
| Ansvar | Överföring **6 månader** | Det slutliga beslutet om överklagandet | [ATÖ](fristtyp-accept-till-overforing.md) | [AMMR art. 46.1](../../../domains/responsibility/articles/ammr-046.md) | [RULE-AMMR-046-001](../../../domains/responsibility/rules/rule-ammr-046-001.md), [PROC-RES-001](../../../domains/responsibility/processes/determine-responsible-member-state.md) |
| Ansvar | Överföring vid förvar **5 veckor** | Den dag överklagandet inte längre har suspensiv verkan | ATÖ (förvar) | [AMMR art. 45.3 b](../../../domains/responsibility/articles/ammr-045.md) | [RULE-AMMR-045-002](../../../domains/responsibility/rules/rule-ammr-045-002.md) |
| Solidaritet | Överföring vid omfördelning **4 veckor** | Det slutliga beslutet om överklagandet | ATÖ (omfördelning) | [AMMR art. 67.11](../../../domains/solidarity/articles/ammr-067.md) | [RULE-AMMR-067-001](../../../domains/solidarity/rules/rule-ammr-067-001.md), [PROC-SOL-002](../../../domains/solidarity/processes/relocation-out.md) |
| Kris | Överföring vid kris **1 år** | Det slutliga beslutet om överklagandet | ATÖ (kris) | [Kris art. 12.2 d](../../../domains/crisis/articles/crisis-012.md) | [RULE-CRI-012-001](../../../domains/crisis/rules/rule-cri-012-001.md) |

> **Gränsförfarandet för återvändande fryses inte.** Tolvveckorsperioden börjar först den dag personen inte längre har rätt att stanna kvar ([Return art. 4.2](../../../domains/return-border-procedure/articles/return-004.md)). Ett överklagande med rätt att stanna kvar ([APR art. 68](../../../domains/asylum-procedure/articles/apr-068.md)) skjuter alltså upp starten. Det pausar inte en löpande frist.

> **Beslutsfristen fryses inte.** Fristen för överföringsbeslut ([ATB](fristtyp-accept-till-beslut.md), AMMR art. 42.1) löper innan något överklagande kan göras. Det är verkställigheten (ATÖ) som får ny startpunkt.

> **Asylbeslut:** att ett **beslut om återvändande** automatiskt upphävs medan sökanden har rätt att stanna kvar ([APR art. 68.1](../../../domains/asylum-procedure/articles/apr-068.md)) är en frysning av beslutets verkan, inte av en tidsfrist.

---

## 2. Förlängning — samlad lista

Varje förlängning har en **utlösande grund** och ett **tak**. Kolumnen *Vem* anger vem som beslutar eller tillämpar förlängningen.

### Registrering och inlämnande (APR)

| Frist | Ordinarie | Förlängd till | Grund | Vem | Rättslig grund | Regel / process |
|-------|-----------|---------------|-------|-----|----------------|-----------------|
| Registrering av ansökan | 5 dagar | **15 dagar** | Oproportionerligt många ansökningar inom samma tid | Registreringsmyndigheten | [APR art. 27](../../../domains/registration/articles/apr-027.md) | [RULE-TL-REG-002](../rules/rule-tl-reg-002.md), [PROC-REG-001](../../../domains/registration/processes/registration-of-an-application.md) |
| Bokad tid för inlämnande | 21 dagar | **2 månader** från registreringen | Oproportionerligt många ansökningar, så att bokad tid inom 21 dagar inte kan ges | Behörig myndighet | [APR art. 28.5](../../../domains/registration/articles/apr-028.md) | [RULE-TL-LOD-002](../rules/rule-tl-lod-002.md), [PROC-REG-002](../../../domains/registration/processes/lodging-an-application.md) |
| Företrädare för ensamkommande barn | 15 arbetsdagar från ansökan görs | **+10 arbetsdagar** | Oproportionerligt många ansökningar från ensamkommande barn, eller andra exceptionella situationer | Behörig myndighet | [APR art. 23.3](../../../references/legislation/apr.md) | — |
| Giltighet för sökandehandlingen | Upp till 12 månader, eller till överföring | **Den period sökanden har rätt att stanna kvar** | Handlingen utfärdas av den ansvariga medlemsstaten | Utfärdande myndighet | [APR art. 29.9](../../../domains/registration/articles/apr-029.md) | [PROC-REG-003](../../../domains/registration/processes/issue-applicant-documents.md) |

### Prövning (APR)

| Frist | Ordinarie | Förlängd till | Grund | Vem | Rättslig grund | Regel / process |
|-------|-----------|---------------|-------|-----|----------------|-----------------|
| Upptagandeprövning (art. 38.1 a–d och 38.2) | 2 månader | **+2 månader** (max 4) | Oproportionerligt många ansökningar, komplexa sak- eller rättsfrågor, eller försening som enbart beror på sökandens underlåtenhet enligt art. 9 | Beslutande myndighet | [APR art. 35.2](../../../domains/asylum-procedure/articles/apr-035.md) | [RULE-APR-035-003](../../../domains/asylum-procedure/rules/rule-apr-035-003.md), [PROC-ASY-001](../../../domains/asylum-procedure/processes/examine-an-application.md), [PROC-ASY-002](../../../domains/asylum-procedure/processes/subsequent-application.md) |
| Prövning i sak | 6 månader | **+6 månader** (max 12) | Samma tre grunder som ovan | Beslutande myndighet | [APR art. 35.5](../../../domains/asylum-procedure/articles/apr-035.md) | [RULE-APR-035-002](../../../domains/asylum-procedure/rules/rule-apr-035-002.md), [PROC-ASY-001](../../../domains/asylum-procedure/processes/examine-an-application.md) |

Fristen i art. 38.1 e (tio arbetsdagar) och påskyndat förfarande (tre månader) har **ingen** förlängningsgrund i art. 35. Påskyndat förfarande kan dock övergå till ordinarie prövning i sak om ärendet är för komplext ([APR art. 42.2](../../../domains/asylum-procedure/articles/apr-042.md)).

### Gränsförfarande (APR och kris)

| Frist | Ordinarie | Förlängd till | Grund | Vem | Rättslig grund | Regel / process |
|-------|-----------|---------------|-------|-----|----------------|-----------------|
| Gränsförfarandets längd | 12 veckor | **16 veckor** | Den medlemsstat som personen omfördelats till (art. 67.11) tillämpar gränsförfarandet | Omfördelningsmedlemsstaten | [APR art. 51.2](../../../domains/border-procedure/articles/apr-051.md) | [RULE-APR-051-002](../../../domains/border-procedure/rules/rule-apr-051-002.md), [PROC-BRD-001](../../../domains/border-procedure/processes/asylum-border-procedure.md) |
| Gränsförfarandets längd vid kris | 12 veckor | **+högst 6 veckor** (max 18) | Kris- eller force majeure-situation | Medlemsstaten, efter rådets genomförandebeslut | [Kris art. 11.1](../../../domains/crisis/articles/crisis-011.md) | [RULE-CRI-011-001](../../../domains/crisis/rules/rule-cri-011-001.md), [PROC-CRI-001](../../../domains/crisis/processes/activate-crisis-measures.md) |

> De två förlängningarna kan **inte kombineras**: krisförlängningen får inte användas utöver 16-veckorsförlängningen i art. 51.2 (Kris art. 11.1).

### Ansvar och överföring (AMMR)

| Frist | Ordinarie | Förlängd till | Grund | Vem | Rättslig grund | Regel / process |
|-------|-----------|---------------|-------|-----|----------------|-----------------|
| Överföring | 6 månader | **högst 1 år** | Överföringen har inte kunnat verkställas därför att personen varit **frihetsberövad** | Överförande stat | [AMMR art. 46.2](../../../domains/responsibility/articles/ammr-046.md) | [RULE-AMMR-046-001](../../../domains/responsibility/rules/rule-ammr-046-001.md), [PROC-RES-001](../../../domains/responsibility/processes/determine-responsible-member-state.md) |
| Överföring | 6 månader | **högst 3 år** från underrättelsen till ansvarig stat | Personen eller en medföljande familjemedlem har **avvikit**, **fysiskt motsätter sig** överföringen, **avsiktligt** ser till att tillståndet inte medger överföring, eller **inte uppfyller de medicinska kraven** | Överförande stat (underrättar ansvarig stat) | [AMMR art. 46.2](../../../domains/responsibility/articles/ammr-046.md) | [RULE-AMMR-046-001](../../../domains/responsibility/rules/rule-ammr-046-001.md) |
| Framställan om övertagande (art. 39) | 2 månader (1 månad efter Eurodac- eller VIS-träff) | Förlängs med **lika lång tid som svaret är försenat** | Den anmodade staten har undanhållit uppgifter som visar att den är ansvarig, vid informationsutbyte (svarsfrist tre veckor) | — (följer direkt av förordningen) | [AMMR art. 51.5](../../../domains/responsibility/articles/ammr-051.md) | — |
| Företrädare för ensamkommande barn | 15 arbetsdagar från inlämnande | **+10 arbetsdagar** | Oproportionerligt många ansökningar från ensamkommande barn, eller andra exceptionella situationer | Behörig myndighet | [AMMR art. 23.2 b](../../../references/legislation/ammr.md) | — |

### Ansvar vid kris (kris art. 12)

Gäller i en krissituation enligt art. 1.4 a eller force majeure, när medlemsstaten inte kan hålla fristerna i AMMR art. 39, 40, 41 och 46. Undantagen tillämpas samtidigt.

| Frist | Ordinarie (AMMR) | Vid kris | Rättslig grund |
|-------|------------------|----------|----------------|
| Framställan om övertagande | 2 månader (art. 39) | **4 månader** från registreringen | [Kris art. 12.2 a](../../../domains/crisis/articles/crisis-012.md) |
| Svar på framställan | 1 månad (art. 40) | **2 månader** från mottagandet | Kris art. 12.2 b |
| Avisering om återtagande | 2 veckor från Eurodac-träffen (art. 41) | **1 månad** | Kris art. 12.2 c |
| Bekräftelse av återtagande | 2 veckor (art. 41) | **1 månad** | Kris art. 12.2 c |
| Överföring | 6 månader (art. 46) | **1 år** | Kris art. 12.2 d |

Missar krisstaten fristerna i 12.2 a, b eller d ligger ansvaret hos, eller övergår till, den staten (12.3). Regel: [RULE-CRI-012-001](../../../domains/crisis/rules/rule-cri-012-001.md). Process: [PROC-CRI-001](../../../domains/crisis/processes/activate-crisis-measures.md).

### Omfördelning (AMMR art. 67)

| Frist | Ordinarie | Förlängd till | Grund | Vem | Rättslig grund | Regel / process |
|-------|-----------|---------------|-------|-----|----------------|-----------------|
| Besked från omfördelningsmedlemsstaten | 1 vecka från mottagandet | **högst 2 veckor** | Särskilt komplicerad granskning, eller ett stort antal ärenden samtidigt. Uppskjutandet ska meddelas inom den första veckan | Omfördelningsmedlemsstaten | [AMMR art. 67.9](../../../domains/solidarity/articles/ammr-067.md), [genomförandeförordning 2025/2055 art. 19](../../../references/legislation/ammr-implementing.md) | [RULE-AMMR-067-001](../../../domains/solidarity/rules/rule-ammr-067-001.md), [PROC-SOL-003](../../../domains/solidarity/processes/relocation-in.md) |

Beslutsfristen (1 vecka) och överföringsfristen (4 veckor) har ingen egen förlängningsgrund. Överföringsfristen kan dock frysas (avsnitt 1).

### Registrering vid kris (kris art. 10)

| Frist | Ordinarie | Vid kris | Villkor | Rättslig grund | Regel / process |
|-------|-----------|----------|---------|----------------|-----------------|
| Registrering av ansökan | 5 dagar (15 vid massinflöde) | **4 veckor** efter att ansökan gjordes | Kris eller force majeure. Vid kris enligt art. 1.4 a endast under perioden i det **ursprungliga** genomförandebeslutet, inte under förlängningar av det (10.4) | [Kris art. 10.1](../../../domains/crisis/articles/crisis-010.md) | [RULE-CRI-010-001](../../../domains/crisis/rules/rule-cri-010-001.md) |
| Förhandstillämpning | — | Högst **10 dagar** innan rådet beslutat | Motiverad begäran enligt art. 2.1 och underrättelse till kommissionen | Kris art. 10.6 | — |

Krisförlängningen påverkar inte Eurodac-fristen i art. 15.1 b (Kris art. 10.7). Personer med särskilda behov, underåriga och deras familjer ska prioriteras (10.2).

### Gränsförfarande för återvändande (förordning 2024/1349)

| Frist | Ordinarie | Förlängd till | Grund | Vem | Rättslig grund | Regel / process |
|-------|-----------|---------------|-------|-----|----------------|-----------------|
| Vistelse vid gränsen (och förvar) | 12 veckor från att rätten att stanna kvar upphört | **+högst 6 veckor** (max 18) | Krissituation enligt krisförordningen art. 1.4, efter begäran (art. 7) | Medlemsstaten, efter rådets genomförandebeslut | [Return art. 6.1](../../../domains/return-border-procedure/articles/return-006.md) | [RULE-RET-006-001](../../../domains/return-border-procedure/rules/rule-ret-006-001.md), [PROC-RET-001](../../../domains/return-border-procedure/processes/return-border-procedure.md) |

Tidsfristen för frivillig avresa (högst 15 dagar, art. 4.5) har ingen förlängningsgrund. Hinns återvändandet inte med inom perioden fortsätter det enligt återvändandedirektivet 2008/115/EG (art. 4.4). Förordningen beräknar frister enligt egna regler ([art. 11](../../../domains/return-border-procedure/articles/return-011.md)).

### Eurodac (insamling och överföring)

| Frist | Ordinarie | Förlängd till | Grund | Rättslig grund |
|-------|-----------|---------------|-------|----------------|
| Överföring: sökande, irreguljär gränspassage, olaglig vistelse, sök och räddning | 72 timmar | **+högst 48 timmar** | Allvarliga tekniska problem, för att genomföra nationella kontinuitetsplaner | [Eurodac art. 15.2](../../../domains/eurodac/articles/eur-015.md), [22.6](../../../domains/eurodac/articles/eur-022.md), [23.5](../../../domains/eurodac/articles/eur-023.md), [24.5](../../../domains/eurodac/articles/eur-024.md) |
| Överföring: sök och räddning | 72 timmar | **+högst 48 timmar** | Plötslig tillströmning. Anmäls till kommissionen och medlemsstaterna, och gäller under angiven period, dock **högst en månad** | [Eurodac art. 24.6](../../../domains/eurodac/articles/eur-024.md) |
| Överföring: tillfälligt skydd | 10 dagar | **+högst 48 timmar** | Allvarliga tekniska problem | [Eurodac art. 26.4](../../../domains/eurodac/articles/eur-026.md) |
| Lagring: tillfälligt skydd | 1 år | **Förlängs varje år** | Så länge det tillfälliga skyddet varar | [Eurodac art. 29.9](../../../domains/eurodac/articles/eur-029.md) |

**Ny startpunkt vid hälsohinder:** om biometrin inte kan tas på grund av åtgärder för att skydda personens hälsa eller folkhälsan, ska den tas och överföras senast **48 timmar efter att hindren undanröjts** (art. 15.2, 20.3, 22.6, 23.5, 24.5, 26.4). För unionsramen gäller "så snart som möjligt" (art. 18.3). Att en Eurodac-frist inte hålls befriar aldrig från skyldigheten att ta och överföra uppgifterna.

Process: [PROC-EUR-001](../../../domains/eurodac/processes/collect-and-transmit-biometric-data.md).

---

## 3. Uppskjutande och spärrar

| Mekanism | Vad som skjuts upp | Gräns | Rättslig grund |
|----------|--------------------|-------|----------------|
| Uppskjutande av prövningen pga osäkra förhållanden i ursprungslandet | Avslutandet av prövningen i sak, när förhållandena förväntas vara tillfälliga | Översyn av situationen minst var **fjärde månad**. Kommissionen och asylbyrån informeras. Prövningen ska alltid avslutas inom **21 månader** från inlämnandet | [APR art. 35.7](../../../domains/asylum-procedure/articles/apr-035.md) |
| Uppskjutande innan implicit återkallande | Förfarandet, för att ge sökanden möjlighet att motivera eller rätta | Ingen frist angiven | [APR art. 41.4](../../../domains/asylum-procedure/articles/apr-041.md) |
| Spärr för överföringar till en stat i kris | Överföringar till den ansvariga staten verkställs inte förrän krisen upphört, om inte staten samtycker | Sker inte överföringen inom **1 år** befrias krisstaten och ansvaret övergår till den överförande staten | [Kris art. 12.4](../../../domains/crisis/articles/crisis-012.md) |
| Beslut om uppskov med verkställighet | Domstolen avgör om överföringen ska avbrytas i väntan på överklagandet | Beslut inom **1 månad** från begäran. Överföring får inte verkställas innan beslutet | [AMMR art. 43.3](../../../domains/responsibility/articles/ammr-043.md) |

---

## 4. Frister som uttryckligen inte förlängs eller påverkas

| Frist | Varför den inte förlängs | Rättslig grund |
|-------|--------------------------|----------------|
| Screening (7 dagar vid yttre gräns, 3 dagar inom territoriet) | Ingen förlängningsgrund. Fristen kan i stället **förkortas** till fyra dagar för personer som uppehållit sig vid den yttre gränsen i mer än 72 timmar (art. 8.3). Om kontrollerna inte är klara när fristen löper ut avslutas screeningen ändå, och personen hänvisas vidare | [Screening art. 8.3–8.4](../../../domains/screening/articles/scr-008.md) |
| Svar på framställan om övertagande (AMMR art. 40.1 och 40.7) | En omprövningsbegäran efter avslag förlänger inte svarsfristerna | [Genomförandeförordning 2025/2055 art. 9](../../../references/legislation/ammr-implementing.md) |
| Upptagandeprövningen (APR art. 35.1) | Om fristen löper ut utan beslut blir ansökan inte automatiskt upptagbar | [APR art. 35.1](../../../domains/asylum-procedure/articles/apr-035.md) |
| Eurodac art. 15.1 b vid kris | Krisförlängningen av registreringen påverkar inte Eurodac-fristen | [Kris art. 10.7](../../../domains/crisis/articles/crisis-010.md) |
| Efterföljande ansökan | Inga egna förlängningar. Förhandsprövningen saknar egen dagsfrist och ryms i upptagandefristen. En upptagen ansökan prövas med samma frister och förlängningar som en ordinarie | [APR art. 55](../../../domains/asylum-procedure/articles/apr-055.md), [PROC-ASY-002](../../../domains/asylum-procedure/processes/subsequent-application.md) |

---

## 5. Förkortning

En frist ersätts av en **kortare** frist när ett villkor är uppfyllt. Krisförordningen innehåller inga förkortningar.

| Frist | Ordinarie | Förkortad till | Villkor | Rättslig grund |
|-------|-----------|----------------|---------|----------------|
| Screening vid yttre gräns | 7 dagar | **4 dagar** | Person som omhändertagits vid irreguljär gränspassage (art. 5.1 a) och som fysiskt uppehållit sig vid den yttre gränsen i mer än 72 timmar. Screeningen genomförs därefter | [Screening art. 8.3](../../../domains/screening/articles/scr-008.md) |
| Inlämnande av ansökan | 21 dagar | **5 dagar** från första registreringen (efter omfördelning: från ankomsten till omfördelningsstaten) | Ansökan prövas i gränsförfarandet och sökanden ges en faktisk möjlighet. Missad frist hindrar inte gränsförfarandet | [APR art. 51.1](../../../domains/border-procedure/articles/apr-051.md) |
| Framställan om övertagande | 2 månader från registreringen | **1 månad** från träffen | Träff i Eurodac på uppgifter enligt Eurodac art. 22 eller 24, eller träff i VIS | [AMMR art. 39.1 andra st.](../../../domains/responsibility/articles/ammr-039.md) |
| Svar på framställan om övertagande | 1 månad | **2 veckor** | Framställan grundas på en sådan träff i Eurodac eller VIS | [AMMR art. 40.2](../../../domains/responsibility/articles/ammr-040.md) |
| Framställan om övertagande eller avisering om återtagande | 2 månader / 2 veckor | **2 veckor** från registreringen (eller från Eurodac-träffen om ingen ny ansökan registrerats). **1 vecka** från förvarstagandet om förvaret sker senare | Personen tas i förvar enligt art. 44 | [AMMR art. 45.1](../../../domains/responsibility/articles/ammr-045.md) |
| Svar på framställan om övertagande | 1 månad | **1 vecka**. Uteblivet svar räknas som godtagande | Personen hålls i förvar | [AMMR art. 45.2](../../../domains/responsibility/articles/ammr-045.md) |
| Överföring | 6 månader | **5 veckor** från godtagandet eller bekräftelsen | Personen hålls i förvar. Passeras fristen ska personen friges, men art. 46 gäller fortsatt (45.4) | [AMMR art. 45.3 a](../../../domains/responsibility/articles/ammr-045.md) |
| Översändande och granskning av framställningar och aviseringar | Enligt AMMR | **Enligt överenskommelsen** | Medlemsstaterna har ingått en bilateral administrativ överenskommelse som förkortar fristerna | [AMMR art. 53.1 b](../../../domains/responsibility/articles/ammr-053.md) |
| Upptagandeprövning | 2 månader | **10 arbetsdagar** | Sökanden har ett beslut om återvändande och ansökte först efter sju arbetsdagar från att beslutet mottogs, var informerad om konsekvenserna, och inga nya relevanta faktorer har framkommit (art. 38.1 e) | [APR art. 35.1 andra st.](../../../domains/asylum-procedure/articles/apr-035.md), [38.1 e](../../../domains/asylum-procedure/articles/apr-038.md) |
| Prövning i sak | 6 månader | **3 månader** från inlämnandet | Påskyndat prövningsförfarande: någon grund i art. 42.1 eller 42.3 | [APR art. 35.3](../../../domains/asylum-procedure/articles/apr-035.md), [42](../../../domains/asylum-procedure/articles/apr-042.md) |
| Hela förfarandet | 6 månader (prövning) | **12 veckor** från registreringen, inklusive begäran om att stanna kvar och överklagande | Ansökan prövas i gränsförfarandet | [APR art. 51.2](../../../domains/border-procedure/articles/apr-051.md) |
| Överklagandefrist | 2 veckor–1 månad | **5–10 dagar** (fastställs i nationell rätt) | Beslut att neka prövning, eller avslag som implicit återkallad, ogrundad eller uppenbart ogrundad när någon omständighet i art. 42.1 eller 42.3 gällde | [APR art. 67.7](../../../domains/asylum-procedure/articles/apr-067.md) |
| Frivillig avresa | 7–30 dagar enligt återvändandedirektivet art. 7.1 (ej kontrollerat, direktivet finns inte i repot) | **Högst 15 dagar** | Beviljas bara på begäran, och inte vid risk för avvikande, avslag som uppenbart ogrundad i gränsförfarandet eller risk för allmän ordning eller säkerhet. Ger ingen rätt till inresa | [Return art. 4.5](../../../domains/return-border-procedure/articles/return-004.md) |

> Påskyndat förfarande och gränsförfarande är egna förfaranden med egna frister, inte förkortningar av en frist som redan löper. De står med eftersom fristen blir kortare än vid ordinarie prövning.

---

## Avgränsning: frysning, förlängning, uppskjutande och förkortning

| | Frysning | Förlängning | Uppskjutande | Förkortning |
|--|----------|-------------|--------------|-------------|
| **Effekt** | Ny startpunkt, ny full frist | Fristen ersätts av en längre frist | Förfarandet eller verkställigheten står still | Fristen ersätts av en kortare frist |
| **Grund** | Suspensiv verkan vid överklagande | Massinflöde, komplexitet, försummelse, frihetsberövande, avvikande, tekniska problem, kris | Osäkra förhållanden i ursprungslandet, kris i mottagarstaten, möjlighet att rätta | Förvar, träff i Eurodac eller VIS, gränsförfarande, påskyndat förfarande, bilateral överenskommelse |
| **Vem utlöser** | Domstol (beviljar suspensiv verkan) | Myndighet eller stat (konstaterar grund), rådet vid kris | Beslutande myndighet eller förordningen | Förordningen (villkoret är uppfyllt), medlemsstaterna vid bilateral överenskommelse |
| **Tak** | Hela fristen löper på nytt | Alltid ett angivet tak | Yttersta gräns (21 månader, 1 år) eller ingen angiven | Den kortare fristen är bindande |

---

## Viktig princip

Tidsfristerna kan **aldrig** förlängas obegränsat. Varje förlängningsgrund har ett angivet tak, och flera förlängningar staplas inte om förordningen inte säger det. Om varken frysning, förlängning eller uppskjutande är tillämpligt löper fristen ut, med rättsliga följder.

> **Rättelser (2026-09):**
> - Sidan angav tidigare att suspensiv verkan *pausar* fristen så att den fortsätter "från samma punkt". Enligt AMMR art. 45.3 b, 46.1 och 67.11 räknas en ny, full frist från det slutliga beslutet.
> - Överföringsfristen vid avvikande angavs som 18 månader (Dublin III). I AMMR är den högst tre år, och dessutom högst ett år vid frihetsberövande.
> - Förlängningen av sakprövningen angavs som 15 månader. Den är 12 (6+6).
> - Återvändande vid gräns angavs ha en frysning vid suspensiv verkan ("Return art. 5"). Tolvveckorsperioden i art. 4.2 har en senare startpunkt men fryses inte, och art. 5 gäller förvar.
> - Listan var ofullständig. Uppgifterna om upptagandeprövning, gränsförfarande vid omfördelning, företrädare för ensamkommande barn, omfördelning, Eurodac, återtagande vid kris och uppskjutanden saknades.

---

## Se även

- [Tidsfrister — översikt](../README.md)
- [Fristtyp ATÖ](fristtyp-accept-till-overforing.md) — Överföringsfristen och dess förlängningar
- [Fristtyp ATB](fristtyp-accept-till-beslut.md) — Beslutsfristen, som inte fryses
- [Uppsikt](uppsikt.md) — Tidsfrister kopplade till uppsikt

---

## Status

Complete

# Delat — Flaggor, markeringar och varningar

## Syfte

Denna shared-modul samlar ett **tvärgående systemmönster** i migrationspakten: punkter där ett villkor inträffar som ska **flagga, markera, varna eller sätta en status** som styr efterföljande handläggning, åtgärd eller sanktion. Flaggan riktar sig ofta till en handläggare, men kan också vara ett rent systemtillstånd (t.ex. en märkning i ett register).

Mönstret är genomgående detsamma:

```text
Villkor inträffar  →  Flagga/markering/status sätts  →  Åtgärd eller konsekvens följer
```

Flaggorna ligger idag utspridda i enskilda regelkort (via sektionerna `## Utlösare` → `## Rättsverkan`, se [STYLE_GUIDE](../../STYLE_GUIDE.md)) och i nationella implementeringsfiler. Den här sidan samlar dem på ett ställe.

---

## Flaggtyper

Flaggorna grupperas i sex kategorier efter vad de uttrycker.

### 1. Säkerhetsflaggor

| Flagga | Utlöses av | Konsekvens | Källa |
|--------|------------|------------|-------|
| Säkerhetsträff (screening) | Träff vid sökning i SIS, EES, ETIAS, VIS, Ecris-TCN, Europol, Interpol | Noteras i screeningformuläret; påverkar hänvisning till förfarande | [RULE-SCR-015-001](../../domains/screening/rules/rule-scr-015-001.md) |
| Maskering av säkerhetsträff | Säkerhetsträff finns | Träffen döljs i den sökandes **egen** version av formuläret (synlig endast för myndigheten) | [REQ-SCR-017-002](../../domains/screening/requirements/req-scr-017-002.md) |
| SIS/SIRENE-notifiering | Träff i SIS vid identifiering | SIRENE-kontoret underrättas omedelbart och vidtar åtgärd enligt registreringen | [eur-016](../../domains/eurodac/articles/eur-016.md) |

### 2. Status- och registermärkningar (Eurodac m.fl.)

| Flagga | Utlöses av | Konsekvens | Källa |
|--------|------------|------------|-------|
| Eurodac-träff (hit/no-hit) | Automatisk jämförelse av biometri | Hit/no-hit till ursprungsstaten; kan utlösa ansvarsförfarande och korta frister | [RULE-EUR-031-001](../../domains/eurodac/rules/rule-eur-031-001.md) |
| Märkning vid beviljat skydd | Slutligt beslut om flykting-/subsidiärt skydd | Uppgifter märks i centralsystemet; ger ej längre träff vid ansvarsbestämning | [eur-024](../../domains/eurodac/articles/eur-024.md) |
| Avmärkning | Skydd upphör/ändras | Märkning tas bort; uppgifter åter sökbara för ansvarsbestämning | [RULE-EUR-025-001](../../domains/eurodac/rules/rule-eur-025-001.md) |
| **Efterföljande-ansökan-markering** | Träff på tidigare ansökan (i Sverige eller via Eurodac i annan MS) | Ärendet markeras som efterföljande ansökan → förhandsprövning (art. 55); nivåräkning styr rätten att stanna (art. 56) | [RULE-APR-055-003](../../domains/asylum-procedure/rules/rule-apr-055-003.md), [RULE-APR-056-002](../../domains/asylum-procedure/rules/rule-apr-056-002.md) |

### 3. Risk- och tvångsåtgärdsflaggor

| Flagga | Utlöses av | Konsekvens | Källa |
|--------|------------|------------|-------|
| Avvikanderisk / säkerhetshot | Individuell bedömning av risk för avvikande eller hot | Förvar får ske (sista utväg) efter proportionalitetsbedömning | [RULE-AMMR-044-001](../../domains/responsibility/rules/rule-ammr-044-001.md) |
| Avvikande (absconding) | Person ej tillgänglig för överföring | Överföringsfristen förlängs från 6 till 18 månader | [RULE-AMMR-046-001](../../domains/responsibility/rules/rule-ammr-046-001.md) |
| Tillgänglighetskrav (screening) | Risk för avvikande, inre säkerhet eller folkhälsa | Nationellt kvarhållande/uppsikt under screening | [scr-006](../../domains/screening/articles/scr-006.md) |

### 4. Sårbarhets- och statuspresumtioner

| Flagga | Utlöses av | Konsekvens | Källa |
|--------|------------|------------|-------|
| Sårbarhetsindikering | Preliminär kontroll identifierar särskilda behov | Anpassat förfarande; specialistmyndighet kopplas in vid barnmisshandel/människohandel | [scr-012](../../domains/screening/articles/scr-012.md) |
| "Behandla som underårig" | Tvivel om ålder | Behandlas som underårig tills annat fastställts; prioriterad handläggning | [apr-021](../vulnerable-persons/articles/apr-021.md) |

### 5. Tidsfrist- och gränsvärdesflaggor

| Flagga | Utlöses av | Konsekvens | Källa |
|--------|------------|------------|-------|
| Bindande tidsfrist | Frist börjar löpa | Vid överskridande: automatisk rättsföljd (ansvar övergår, frigivning, avslutat förfarande) | [time-limits](../time-limits/README.md), [frysning-och-forlangning](../time-limits/concepts/frysning-och-forlangning.md) |
| Bifallsandel under tröskel | EU-genomsnittlig bifallsandel < 20 % (< 50 % vid kris) | Obligatoriskt gränsförfarande / påskyndat (säkert ursprungsland) | [statistics](../statistics/README.md) |
| Kapacitetstak uppnått | Statens gränsförfarandekapacitet full | Vissa grunder för gränsförfarande "stängs av" (säkerhetshot gäller dock alltid) | [adequate-capacity](../../domains/border-procedure/concepts/adequate-capacity.md) |

### 6. Statusberoende spärrar och sanktioner (främst nationell nivå)

| Flagga | Utlöses av | Konsekvens | Källa |
|--------|------------|------------|-------|
| Påskyndat-förfarande-spärr | Ansökan klassas enligt art. 42.1 a–f | Kortare prövningsfrist (3 mån) + spärr mot arbetsmarknadstillträde (AT-UND) | [ds-2025-30-mottagande](../time-limits/national/ds-2025-30-mottagande.md) |
| "Fel medlemsstat"-status | Sökande i annan MS efter delgivet överföringsbeslut | Indragning av mottagningsvillkor (ingen dagersättning, inget AT-UND) | [ds-2025-30-mottagande](../time-limits/national/ds-2025-30-mottagande.md) |
| **Närvarokontroll-räknare** | Upprepade missade kontroller / överträdd anmälningsskyldighet ("per tillfälle") | Nedsättning av dagersättning som ackumuleras per tillfälle (t.ex. 2 veckor per missad anmälan) | [ds-2025-30-mottagande](../time-limits/national/ds-2025-30-mottagande.md) |

---

## Räknare och trösklar

Flera flaggor är inte binära utan **ackumuleras eller mäts mot en tröskel** innan konsekvensen inträder. Dessa är särskilt relevanta för ett systemstöd eftersom de kräver att något räknas eller jämförs över tid:

| Mekanism | Vad som räknas/mäts | Tröskel/effekt | Källa |
|----------|---------------------|----------------|-------|
| Nedsättning dagersättning "per tillfälle" | Antal missade närvarokontroller / överträdelser av anmälningsskyldighet | Varje tillfälle ger ny nedsättningsperiod (ackumulerande) | [ds-2025-30-mottagande](../time-limits/national/ds-2025-30-mottagande.md) |
| Efterföljande-ansökan-nivå | Antal tidigare ansökningar (första vs. andra/följande) | Styr rätten att stanna (art. 56) | [RULE-APR-056-002](../../domains/asylum-procedure/rules/rule-apr-056-002.md) |
| Bifallsandel | EU-genomsnittlig bifallsandel per ursprungsland | < 20 % (< 50 % vid kris) utlöser gränsförfarande/påskyndat | [statistics](../statistics/README.md) |
| Gränsförfarandekapacitet | Antal pågående gränsförfaranden mot statens tak | Tak uppnått stänger av vissa grunder | [adequate-capacity](../../domains/border-procedure/concepts/adequate-capacity.md) |
| Omprövningsintervall (uppsikt) | Tid sedan senaste omprövning | Utebliven omprövning → beslutet upphör | [uppsikt](../time-limits/concepts/uppsikt.md) |

---

## Egenskaper hos en flagga (teknisk modell)

Det här avsnittet är ett underlag för en **återanvändbar teknisk flaggmodell**. Det beskriver vilka egenskaper en flagga kan ha, härlett från de faktiska flaggorna i katalogen ovan. Alla egenskaper behövs inte för alla flaggor — tabellerna markerar vad som är **kärna** (behövs nästan alltid) respektive **valfritt** (används vid behov). Plocka det som passar.

### Identitet och presentation

| Egenskap | Kärna/valfri | Beskrivning | Exempel ur katalogen |
|----------|--------------|-------------|----------------------|
| `id` | Kärna | Stabil, oföränderlig nyckel (inte namnet) | `FLAG_SEC_HIT` |
| `namn` | Kärna | Läsbar etikett | "Säkerhetsträff" |
| `beskrivning` | Kärna | Vad flaggan betyder | — |
| `kategori` | Kärna | En av de sex kategorierna ovan | Säkerhet, Status, Risk … |
| `severity` | Kärna | Allvarlighetsgrad (t.ex. info / varning / kritisk) | Säkerhetsträff = kritisk; sårbarhetsindikering = info |
| `färg` | Valfri | Härleds oftast ur severity | — |
| `ikon` | Valfri | Följer ofta severity | — |

> Färg är i praktiken en *presentation* av severity. Modellera severity som egen egenskap och låt färg/ikon härledas — då slipper du dubbellagra.

### Värde och typ

En flagga är inte alltid på/av. Katalogen visar fyra värdetyper, så flaggan behöver en **typ** och ett **värde**.

| Egenskap | Kärna/valfri | Beskrivning | Exempel ur katalogen |
|----------|--------------|-------------|----------------------|
| `värdetyp` | Kärna | `boolean` \| `räknare` \| `tröskel` \| `enum` | — |
| `värde` | Kärna | Aktuellt värde enligt typen | — |
| `tröskel` | Valfri (krävs för räknare/tröskel) | Gräns då konsekvensen inträder | Bifallsandel < 20 %; räknare "vid 3" |
| `operator` | Valfri (krävs för tröskel) | Jämförelse: `<`, `≥` … | Bifallsandel `<` 20 % |
| `per-steg-effekt` | Valfri | Om varje ökning ger konsekvens (inte bara tröskeln) | Nedsättning dagersättning "per tillfälle" |

Värdetyperna i katalogen:
- **boolean** — säkerhetsträff (finns/finns inte)
- **räknare (0–?)** — närvarokontroll-räknaren, efterföljande-ansökan-nivå
- **tröskel/mätvärde** — bifallsandel, gränsförfarandekapacitet
- **enum (uppräknad status)** — hit/no-hit, "behandla som underårig", "fel medlemsstat"

### Livscykel

Hur flaggan sätts, ändras och tas bort. Det här är ofta det som glöms i en första modell.

| Egenskap | Kärna/valfri | Beskrivning | Exempel ur katalogen |
|----------|--------------|-------------|----------------------|
| `trigger` | Kärna | Villkoret som sätter flaggan | "Utlöses av"-kolumnen ovan |
| `källa` | Kärna | Hur den sattes: automatiskt system / handläggarbeslut / extern notifiering | Eurodac-jämförelse (auto); avvikanderisk (beslut); SIS/SIRENE (extern) |
| `satt_tidsstämpel` | Kärna | När den sattes | — |
| `upphörandetyp` | Kärna | `permanent` \| `manuell avklarning` \| `auto/tidsstyrd` | Avmärkning (manuell/händelse); uppsikt (tidsstyrd) |
| `status` | Kärna | Livscykeltillstånd: aktiv / löst / upphävd | — |
| `giltighetstid` | Valfri | Inbyggd livslängd om sådan finns | — |
| `ändrad_tidsstämpel` | Valfri | Senaste ändring | — |

### Beteende och styrning

| Egenskap | Kärna/valfri | Beskrivning | Exempel ur katalogen |
|----------|--------------|-------------|----------------------|
| `blockerande` | Kärna | Spärrar flaggan något, eller bara upplyser? | Påskyndat-spärr (blockerande) vs. sårbarhetsindikering (informativ) |
| `konsekvens` | Kärna | Vad flaggan utlöser (regel/workflow) | "Konsekvens"-kolumnen ovan |
| `synlighet` | Kärna | Vem får se flaggan (målgrupp/behörighet) | Säkerhetsträff **maskeras för sökanden**, syns för myndigheten |
| `rättslig_grund` | Kärna | Länk till artikel/regel | Hela katalogen bygger på detta |
| `överklagbar` | Valfri | Om konsekvensen kan överklagas | Indragning av mottagningsvillkor; AT-UND-spärr |

### Kontext och relationer

| Egenskap | Kärna/valfri | Beskrivning | Exempel ur katalogen |
|----------|--------------|-------------|----------------------|
| `entitet` | Kärna | Vad flaggan sitter på: person / ärende / grupp / medlemsstat | Kapacitetstak sitter på **staten**, inte individen |
| `domän` | Valfri | Var flaggan hör hemma | Screening, Ansvar … |
| `relaterade_flaggor` | Valfri | Flaggor som utesluter eller förutsätter varandra | Non-refoulement blockerar undantag från rätt att stanna |
| `historik` | Valfri (ofta krav i myndighetsbruk) | Vem satte/ändrade/avklarade och när (audit) | — |

### Minimimodell (kort checklista)

```text
id, namn, beskrivning, kategori, severity
värdetyp (boolean|räknare|tröskel|enum) [+ tröskel, operator vid behov]
trigger, källa, satt_tidsstämpel, upphörandetyp, status
blockerande, konsekvens, synlighet, rättslig_grund
entitet
```

Tre egenskaper som är lätta att missa men som katalogen visar är nödvändiga:
1. **synlighet/maskering** — säkerhetsträffen är dold för den sökande.
2. **upphörandetyp** — Eurodac-märkning tas bort vid avmärkning; uppsikt upphör tidsstyrt.
3. **blockerande vs. informativ** — avgör om flaggan stoppar ett flöde eller bara upplyser.

---

## Bruttolista — kandidatflaggor (för utsållning)

Detta är ett **arbetsunderlag**, inte en formaliserad del av katalogen. Posterna är villkor i dokumentationen som *skulle kunna* modelleras som flaggor men ännu inte är beslutade som sådana. De är grupperade per domän. Sålla och lyft upp till de belagda kategorierna ovan vid behov.

### Screening

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Screening-frist utlöper | Person | tröskel (tid) | 7 dagar (4 om >72h vid gräns) → screening avslutas, hänvisning även om kontroller ej klara | [RULE-SCR-008-001](../../domains/screening/rules/rule-scr-008-001.md), [RULE-SCR-018-001](../../domains/screening/rules/rule-scr-018-001.md) |
| Hänvisningsutfall (kanalisering) | Person | enum | Screening klar/frist ute → status styr nästa spår (asyl / återvändande / omfördelning) | [RULE-SCR-018-001](../../domains/screening/rules/rule-scr-018-001.md) |
| Barnets bästa-markering | Barn | boolean | Person < 18 → barnets bästa ska vägas in och dokumenteras; överklagbart | [RULE-SCR-013-001](../../domains/screening/rules/rule-scr-013-001.md) |

### Eurodac

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Registrering vid återkallat uppehållstillstånd | Person | boolean/märkning | Tillstånd återkallas + ingen rätt att stanna → biometri tas, dataset märks | [RULE-EUR-022-001](../../domains/eurodac/rules/rule-eur-022-001.md) |
| Biometri vid sök-och-räddning (72h) | Person | tröskel (tid) | SAR-landsättning → biometri inom 72h | [RULE-EUR-018-001](../../domains/eurodac/rules/rule-eur-018-001.md) |
| Omfördelningsmärkning | Person | märkning | Omfördelning → dataset märks med ursprungs- och mottagande-MS | [RULE-EUR-019-001](../../domains/eurodac/rules/rule-eur-019-001.md) |

### Registrering

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Implicit återkallande (missad inlämning) | Ärende | tröskel (tid) | Registrerad men ej inlämnad inom 21 dagar → implicit återkallande kan inträda | [RULE-APR-028-001](../../domains/registration/rules/rule-apr-028-001.md) |
| Sökandehandlingens giltighet/upphörande | Person | enum/tid | Max 12 mån; upphör vid överföring; förlängs auto om ansvarig stat utfärdar | [RULE-APR-029-003](../../domains/registration/rules/rule-apr-029-003.md) |
| Registreringshandling återkallas | Person | boolean | Sökandehandling utfärdas → registreringshandling återkallas | [REQ-APR-029-003](../../domains/registration/requirements/req-apr-029-003.md) |

### Gränsförfarande

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Inrese-fiktion / inreseförbud | Person | boolean | Gränsförfarande → inresa nekas tills beslut eller 12 v | [RULE-APR-043-002](../../domains/border-procedure/rules/rule-apr-043-002.md) |
| Förkortad inlämningsfrist (5 d) | Ärende | tröskel (tid) | Registrering i gränsförfarande → inlämning inom 5 d | [RULE-APR-051-001](../../domains/border-procedure/rules/rule-apr-051-001.md) |
| Undantag vid sårbarhet/UAM/medicinskt behov | Person | boolean | Särskilda behov/UAM → gränsförfarande avbryts, inresa beviljas, över till reguljärt | [RULE-APR-053-001](../../domains/border-procedure/rules/rule-apr-053-001.md) |

### Återvändandegränsförfarande

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Automatiskt inlett förfarande + inreseförbud | Ärende | boolean | Avslag i asylgränsförfarande → återvändandeförfarande inleds auto, inresa nekas | [RULE-RET-004-001](../../domains/return-border-procedure/rules/rule-ret-004-001.md) |
| Absolut 12-veckorsfrist → rätt till inresa | Person | tröskel (tid) | 12 v utan verkställt avlägsnande → förfarandet avslutas, inresa tillåts | [RULE-RET-005-001](../../domains/return-border-procedure/rules/rule-ret-005-001.md) |

### Ansvar (AMMR)

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Tyst godkännande (övertagande) | Medlemsstat | presumtion | Inget svar inom frist (1 mån/2 v/1 v) → framställan anses godtagen | [RULE-AMMR-040-001](../../domains/responsibility/rules/rule-ammr-040-001.md) |
| Tyst bekräftelse (återtagande) | Medlemsstat | presumtion | Inget svar inom 2 v → avisering anses bekräftad | [RULE-AMMR-041-001](../../domains/responsibility/rules/rule-ammr-041-001.md) |
| Tyst godkännande vid förvar | Medlemsstat | presumtion | Inget svar inom 1 v (förvar) → godtagande | [RULE-AMMR-045-001](../../domains/responsibility/rules/rule-ammr-045-001.md) |
| Obligatorisk frigivning | Person | tröskel (tid) | Förvarsfrist överskrids → personen ska friges (ansvar består) | [RULE-AMMR-045-001](../../domains/responsibility/rules/rule-ammr-045-001.md) |
| Suspensiv verkan fryser frist | Ärende | boolean | Suspensiv verkan → överföringsfrist pausas | [RULE-AMMR-045-002](../../domains/responsibility/rules/rule-ammr-045-002.md) |
| Automatiskt ansvar (flygplatstransit) | Medlemsstat | boolean | Ansökan i flygplatstransit → MS ansvarar automatiskt | [RULE-AMMR-032-001](../../domains/responsibility/rules/rule-ammr-032-001.md) |
| Familjekriterium upphör | Ärende | tröskel (händelse) | Första beslut i sak fattas → familjekriteriet upphör | [RULE-AMMR-027-001](../../domains/responsibility/rules/rule-ammr-027-001.md) |
| Utgången handling grundar ändå ansvar | Medlemsstat | tröskel (tid) | Handling/visering utgången men inom 3 år / 18 mån → kan grunda ansvar | [REQ-AMMR-029-002](../../domains/responsibility/requirements/req-ammr-029-002.md) |
| Cessation-trösklar | Medlemsstat | tröskel (tid) | 20 mån irreguljär passage / 12 mån SAR / 9 mån frånvaro / 15 mån efter gränsförfarandebeslut → ansvar upphör | [RULE-AMMR-033-002](../../domains/responsibility/rules/rule-ammr-033-002.md), [RULE-AMMR-037-001](../../domains/responsibility/rules/rule-ammr-037-001.md) |

### Solidaritet

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Säkerhetsundantag från omfördelning | Person/MS | boolean | Fara för säkerhet/ordning → personen får inte omfördelas | [RULE-AMMR-067-001](../../domains/solidarity/rules/rule-ammr-067-001.md) |
| Referensnyckel-bidragsandel | Medlemsstat | tröskel/kvot | Poolberäkning → bindande andel per MS (50 % BNP / 50 % befolkning) | [RULE-AMMR-066-001](../../domains/solidarity/rules/rule-ammr-066-001.md) |

### Kris

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Fristförlängning — registrering | MS/ärende | enum (vid kris) | Kris fastställd → registreringsfrist → 4 v | [RULE-CRI-010-001](../../domains/crisis/rules/rule-cri-010-001.md) |
| Fristförlängning — AMMR | Medlemsstat | enum (vid kris) | Kris → framställan 4 mån / svar 2 mån / överföring 1 år | [RULE-CRI-012-001](../../domains/crisis/rules/rule-cri-012-001.md) |
| Fristförlängning — gränsförfarande | MS/person | enum (vid kris) | Kris → gränsförfarande 18 v, personkrets utökas | [RULE-CRI-011-001](../../domains/crisis/rules/rule-cri-011-001.md) |

### Asylförfarande

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Påskyndat-förfarande-utlösare (art. 42) | Ärende | enum | Någon art. 42-grund föreligger → påskyndat, beslut inom 3 mån | [RULE-APR-042-001](../../domains/asylum-procedure/rules/rule-apr-042-001.md) |

### Uppsikt (tidsstyrda tillstånd)

| Kandidat | Entitet | Typ | Utlösare → konsekvens | Källa |
|----------|---------|-----|------------------------|-------|
| Uppsikt upphör vid utebliven omprövning | Person | tröskel (tid) | Omprövningsintervall passeras (6/3/1 mån) utan omprövning → beslutet upphör | [uppsikt](../time-limits/concepts/uppsikt.md) |
| Längsta uppsiktstid barn | Barn | tröskel (tid) | Förstärkt uppsikt barn → max 3 mån (+3 vid synnerliga skäl) | [uppsikt](../time-limits/concepts/uppsikt.md) |

---

## Typningslista — mönster tvärs domäner

Samma kandidater, sorterade efter **mönstertyp** i stället för domän. Den här vyn är tänkt som ingång för en teknisk lösning: varje mönster motsvarar ett beteende som kan återanvändas, och kolumnerna pekar på var det förekommer.

| Mönstertyp | Beteende | Förekommer i (domän → artikel/regel) |
|------------|----------|---------------------------------------|
| **Tyst godkännande / presumtion** | Passivitet inom frist = ja | Ansvar: övertagande ([art. 40](../../domains/responsibility/rules/rule-ammr-040-001.md)), återtagande ([art. 41](../../domains/responsibility/rules/rule-ammr-041-001.md)), förvar ([art. 45](../../domains/responsibility/rules/rule-ammr-045-001.md)); Ansvar/impl: TGÖ ([IMPL-024](../../domains/responsibility/rules/rule-ammr-impl-024-001.md)) |
| **Cessation (tid → ansvar upphör)** | Tidsfrist passeras → tillstånd upphör | Ansvar: [art. 33](../../domains/responsibility/rules/rule-ammr-033-002.md), [art. 37](../../domains/responsibility/rules/rule-ammr-037-001.md) |
| **Frist → rättsföljd (hård deadline)** | Deadline missas → automatisk följd | Ansvar: överföring ([art. 46](../../domains/responsibility/rules/rule-ammr-046-001.md)), frigivning ([art. 45](../../domains/responsibility/rules/rule-ammr-045-001.md)); Återvändandegräns: [art. 5](../../domains/return-border-procedure/rules/rule-ret-005-001.md); Screening: [art. 8/18](../../domains/screening/rules/rule-scr-008-001.md) |
| **Numerisk tröskel / kvot / tak** | Mätvärde mot gräns | Statistik: [bifallsandel](../statistics/README.md); Gränsförfarande: [kapacitet](../../domains/border-procedure/concepts/adequate-capacity.md); Solidaritet: [referensnyckel](../../domains/solidarity/rules/rule-ammr-066-001.md) |
| **Räknare (ackumulerande)** | Antal händelser mot gräns | Mottagande: närvarokontroll ([ds-2025-30](../time-limits/national/ds-2025-30-mottagande.md)); Asyl: efterföljande-nivå ([art. 56](../../domains/asylum-procedure/rules/rule-apr-056-002.md)) |
| **Register-/formulärmärkning** | Status sätts i system/formulär | Eurodac: [art. 24](../../domains/eurodac/articles/eur-024.md), [art. 19](../../domains/eurodac/rules/rule-eur-019-001.md), [art. 22](../../domains/eurodac/rules/rule-eur-022-001.md); Screening: säkerhetsträff ([art. 15](../../domains/screening/rules/rule-scr-015-001.md)) |
| **Spärr / uteslutning** | Rättighet/flöde blockeras | Asyl/mottagande: påskyndat-spärr ([ds-2025-30](../time-limits/national/ds-2025-30-mottagande.md)); Gränsförfarande: inrese-fiktion ([art. 43.2](../../domains/border-procedure/rules/rule-apr-043-002.md)); Solidaritet: säkerhetsundantag ([art. 67](../../domains/solidarity/rules/rule-ammr-067-001.md)) |
| **Säkerhets-/ordningsbedömning** | Hot identifieras → åtgärd | Screening: [art. 15](../../domains/screening/rules/rule-scr-015-001.md); Ansvar: förvar ([art. 44](../../domains/responsibility/rules/rule-ammr-044-001.md)); Solidaritet: [art. 67](../../domains/solidarity/rules/rule-ammr-067-001.md) |
| **Sårbarhet / barn** | Särskilda behov → anpassning/undantag | Screening: [art. 12](../../domains/screening/articles/scr-012.md), [art. 13](../../domains/screening/rules/rule-scr-013-001.md); Vulnerable: [art. 21](../vulnerable-persons/articles/apr-021.md); Gränsförfarande: [art. 53](../../domains/border-procedure/rules/rule-apr-053-001.md) |
| **Systemomfattande masterläge** | Ett tillstånd ändrar många frister | Kris: [art. 10](../../domains/crisis/rules/rule-cri-010-001.md), [art. 11](../../domains/crisis/rules/rule-cri-011-001.md), [art. 12](../../domains/crisis/rules/rule-cri-012-001.md) |

---

## Ej formaliserade flaggor (upptäckta luckor)

Dessa flaggor är kända från praktiken men är **ännu inte dokumenterade som egna regler/krav** i kunskapsbasen. De listas här så att de blir spårbara inför systemarbetet.

| Flagga | Beskrivning | Varför den saknas | Relaterat |
|--------|-------------|-------------------|-----------|
| Non-refoulement-markering | En markering att en person inte får återsändas | Mönstret finns sannolikt implicit i prövningen men dokumenteras inte som en namngiven flagga | — |
| Deadline-varning "X dagar innan" | En operativ varning innan en frist löper ut | EU-rätten anger bindande rättsföljd men ingen kodad förvarning; endast nationell fristbevakning nämns | [time-limits](../time-limits/README.md) |

---

## Relaterade moduler

- [Tidsfrister](../time-limits/README.md) — fristflaggor, frysning/förlängning, uppsikt
- [Statistik](../statistics/README.md) — bifallsandel och kapacitet som tröskelvärden
- [Sårbara personer](../vulnerable-persons/README.md) — sårbarhets- och åldersstatus
- [STYLE_GUIDE](../../STYLE_GUIDE.md) — regelkortens `Utlösare`/`Rättsverkan`-struktur

---

## Status

Arbetsutkast — katalogen samlar belagda flaggor i kunskapsbasen samt kända luckor. Nya flaggor förs in vid behov.

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

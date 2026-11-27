# Backlog — Övergripande

## Nuläge (2025-07-31)

### Vad som finns

| Kunskapsobjekt | Antal | Kommentar |
|----------------|-------|-----------|
| Artikelfiler | ~120 | 9 domäner + shared |
| Regler (RULE) | ~105 | Med Syfte, Utlösare, Rättsverkan |
| Koncept (CON) | 43 | Med Syfte, Skapas av |
| Krav (REQ) | ~225 | 9 domäner + shared/interpreters |
| Förmågor (CAP) | 41 | 9 domäner |
| Processer (PROC) | 13 | Med Tillståndsförändringar |
| Diagram (PlantUML) | 25+ | Med ID-länkkonvention |
| Informationsflödesdiagram | 4 | Registration, Screening, Responsibility, Asylum Procedure |

### Spårbarhetskedja (implementerad)

```
Article → Rule → Requirement → Förmåga → Process → Diagram
```

---

## Kvar att göra

### KRITISKT — Stubs som saknar innehåll

Dessa artikelfiler existerar men saknar substantiellt innehåll.
En användare som navigerar hit möter en tom sida:

- [ ] `shared/interpreters/articles/apr-030.md` — Personlig intervju, tolkningskrav
- [x] `shared/vulnerable-persons/articles/apr-020.md` — Bedömning av behovet av särskilda förfarandegarantier (omskriven 2026-09)
- [x] `shared/vulnerable-persons/articles/apr-021.md` — Sökande i behov av särskilda förfarandegarantier (omskriven 2026-09; tidigare fel artikel)
- [ ] `shared/statistics/articles/ammr-009.md` — Årlig rapport om asyl och migration
- [ ] `shared/statistics/articles/ammr-010.md` — Bedömning av migrationssituationen
- [x] `domains/eurodac/articles/eur-001.md` — Syftet med Eurodac
- [x] `domains/eurodac/articles/eur-002.md` — Definitioner
- [x] `domains/eurodac/articles/eur-016.md` — Information om den registrerades status

### Shared-moduler som saknar krav och capabilities

- [ ] shared/vulnerable-persons — krav och förmågor finns (granskade 2026-09), men inga regler (RULE)
- [ ] shared/priority — ny modul 2026-09; saknar regler, krav och förmågor
- [ ] shared/children — Inga regler, krav eller capabilities
- [ ] shared/identity — Har aktivitet men inga formella krav
- [ ] shared/biometrics — Enbart README
- [ ] shared/security-checks — Enbart README
- [ ] shared/interviews — Artiklarna 11–14 finns i asylum-procedure men shared-modulen är tom
- [ ] shared/statistics — Stubs utan substans
- [ ] shared/documents — Enbart README

### Domäninnehåll — kvarvarande luckor

- [ ] Registration: artikel 4 (behöriga myndigheter) — fil skapad men regler ej formaliserade
- [ ] Screening: artiklarna 9 (samarbetsskyldigheter) — regel saknas
- [x] Eurodac: artiklarna 1–2 och 13–42 — samtliga kort och regler granskade och omskrivna mot förordningstexten (2026-09), se [Eurodac BACKLOG](domains/eurodac/BACKLOG.md)
- [ ] Eurodac: artiklarna 3–12 och 43–63 saknar egna kort (bland annat art. 43 rätt till tillgång, 48 datasäkerhet, 49–50 tredjeland, 52 skadestånd)
- [ ] Eurodac: krav (REQ) och förmågor (CAP) saknas för art. 16, 18–22, 24–28 och 30–42
- [ ] Asylum Procedure: artiklarna 8–14 (garantier, intervju) — delvis i shared men ej komplett

### KRITISKT — Kvalitetsgranskning mot förordningstext

Vid granskningen av Eurodac (2026-09) var ungefär två tredjedelar av artikelkorten numrerade fel, och flera innehöll uppgifter som inte står i förordningen. Felen var systematiska, så de andra domänerna kan ha samma problem. Ett enda felaktigt kort gör hela sajten misstänkt.

Metod per domän: jämför varje artikelkorts rubrik och innehåll med förordningstexten i `references/_text/`, och kontrollera att varje regel hör till rätt artikel. Rätta, lägg in en rättelsenot och uppdatera alla hänvisningar.

- [x] Eurodac (förordning 2024/1358) — art. 1–2, 13–42 och 36 regler
- [ ] Screening (förordning 2024/1356) — obs: textfilen är nu konverterad (`references/_text/OJ_L_202401356_SV_TXT.txt`, med `scripts/mhtml-to-text.py`). Misstänkt fel: flera diagram och sidor hänvisar till ART-SCR-006 för sjudagarsfristen, men texten har fristerna i art. 8.3–8.4 (art. 6 gäller tillstånd att resa in). Kortet för scr-016 bör kontrolleras mot art. 16 (åtgärder för identifiering och säkerhetskontroller)
- [x] Återvändande vid gräns (förordning 2024/1349) — granskad 2026-09. Kort för art. 1–8 och 11, regler, krav, process och diagram är omskrivna. Fel som rättades: artikelnumreringen, "inresa tillåts efter 12 veckor" (rätt: fortsättning enligt direktiv 2008/115/EG, art. 4.4) och "frysning vid suspensiv verkan" (rätt: perioden börjar när rätten att stanna kvar upphör, art. 4.2)
- [ ] Registrering (APR art. 26–33)
- [ ] Asylförfarande (APR)
- [ ] Gränsförfarande (APR art. 43–54)
- [ ] Ansvar (AMMR)
- [ ] Solidaritet (AMMR del IV) — art. 67–68 är redan kontrollerade
- [ ] Kris (förordning 2024/1359)
- [ ] Shared-moduler (statistics, interpreters, time-limits)
- [x] Shared: vulnerable-persons — granskad 2026-09. Korten för art. 20 och 21 hade fel innehåll: art. 21 beskrev ensamkommande barn (art. 22, 23, 25) och påstod att deras ansökningar *ska* prioriteras, och art. 20 saknade 30-dagarsfristen. Kraven har fått nya ID:n (REQ-APR-021-001–005 → 022-001, 023-001/002, 025-001/002; 021-006 borttaget), se [kravlistan](shared/vulnerable-persons/requirements/README.md)
- [ ] **Tidsfrister:** för in 30 dagar för bedömningen av särskilda förfarandegarantier (APR 20.3) på tidsfristsidan
- [ ] **Ändrade krav-ID:** REQ-APR-021-001 och 002 betyder nu annat (art. 21). Kontrollera externa system som använder de gamla betydelserna

### Följdarbete efter Eurodac-granskningen

- [x] **Frysning och förlängning:** [samlad lista](shared/time-limits/concepts/frysning-och-forlangning.md) kontrollerad mot förordningstexten (2026-09). Fel rättade i hela repot: överföringsfristen vid avvikande (18 mån enligt Dublin III → högst 3 år enligt AMMR art. 46.2, samt 1 år vid frihetsberövande), ingen fyraveckorsfrist vid förvar (det är 5 veckor enligt art. 45.3) och frysning som ny startpunkt (inte paus)
- [ ] **Ändrade regel-ID:** kontrollera externa system och dokument som använder de gamla betydelserna. RULE-EUR-018-001 avsåg tidigare sök och räddning (nu 024-001). RULE-EUR-024-001 och RULE-EUR-025-001 avsåg tidigare märkning och avmärkning (nu 031-001). RULE-EUR-031-001 avsåg tidigare Eurodac-träff (nu 027-001)
- [ ] **Tidsfrister:** för in Eurodacs övriga frister på [tidsfristsidan](shared/time-limits/README.md). Där finns i dag bara art. 15. Saknas gör 72 timmar för art. 18, 20, 22, 23 och 24, +48 timmar vid plötslig tillströmning (24.6), tio dagar för tillfälligt skydd (26.2), 24 timmar och en timme för jämförelse (38.2), tre arbetsdagar (38.6, omfattas av regeln om minst två arbetsdagar?) samt 72 timmar för underrättelser (16.4, 30.2, 31.1)
- [ ] **Data-retention:** komplettera Eurodac-raden med samtliga lagringstider i art. 29 (3 år och 1 år saknas), och överväg att markering (art. 31) ska synas i diagrammet
- [ ] **Flaggkatalogen:** överväg Eurodacs säkerhetsflagga (art. 17.2 i och 17.4) i egenskapsmodellen. Den sätts och tas bort av ursprungsmedlemsstaten och sprids via Eurodac inom 72 timmar
- [x] **Mottagandelag (2026:999):** [ny sida](shared/time-limits/national/mottagandelag-2026-999.md) kontrollerad mot lagtexten. Ds-sidan om mottagande hade fel sanktionstider, fel överklagandeinstans, fel paragraf för gränsförfarandeboendet och saknade anmälningsplikten för avlägsnandebeslut (4:6). Rättat i flaggkatalogen och gränsförfarandesidan
- [ ] **Mottagande, rester:** information inom 3 dagar, resehandlingar och skolgång bygger fortfarande bara på Ds 2025:30 (regleras inte i mottagandelagen; skolgång troligen i skollagen). Lydelsen 1 okt 2026 för paragrafer ändrade genom SFS 2026:1168 (ikraft 2 okt) saknas i repo-kopian
- [x] **Förvar:** ny modul [shared/detention](shared/detention/README.md) (2026-11) med förvarsgrunder FG-01–12, klockor K1–K7, beslutshändelser BH-01–45, processer PROC-DET-001–004 och 18 regler från utlänningslagen 10 kap., 16 kap. 4 § och direktiv 2008/115/EG art. 15. Rättat på uppsiktssidan: tvåmånadersprövningen följer av utlänningslagen 10:16, inte AMMR art. 45
- [x] **Förvar, beslutskoder:** beslutstyper (INS, INS-BARN, UTL, UTL-BARN), grundkoder (12 st.) och avslutskoder (UPPH, FÖRFALLER) mappade i [beslutskatalogen](shared/detention/decision-catalogue.md) (2026-11). Att bekräfta: AVLÄGS, SANN, samt avslutskod när taket nås och vid överföring/avlägsnande
- [ ] **Förvar, händelsekoder:** koder för övriga beslut (avslag, överföring, uppehållstillstånd m.fl.) i händelsetabellen
- [ ] **Förvar, placering:** utlänningslagen 10 a kap. (verkställighet och placering, ny prövning inom en månad) är inte kartlagt
- [ ] **Förvar, sammanräkning:** ta ställning till [öppen fråga](shared/detention/open_questions/aggregation-of-detention-time.md) om tid med olika grunder och start av ny prövning, med stöd av förarbeten
- [x] **Förvar, källor:** mottagandedirektivet (EU) 2024/1346 tillagt (2026-09). RULE-RCD-010-001 och RULE-RCD-011-001; UTANS och FHVERK bekräftade mot art. 10.4 b och e
- [ ] **Förvar, källor:** utlänningslagen 10 kap. 4 § har punkterna 1, 4 och 5 i rättsdatabasernas text — kontrollera mot SFS 2026:1426
- [ ] **Mottagande:** egna artikelkort och regler för mottagandedirektivet art. 5 (information), 16 (skolgång), 17 (arbetsmarknad), 23 (nedsättning), 24–28 (särskilda behov, barn) och 32 (beredskapsplanering)
- [ ] **Mottagande:** mottagandelagen 5:5 upphäver arbetsmarknadstillträde vid påskyndad prövning. Kontrollera hur det samspelar med direktivet art. 17.9 (inget upphävande under överklagande med rätt att stanna)
- [ ] **Förvar, krav och förmågor:** modulen har inga krav (REQ) eller förmågor (CAP) ännu
- [ ] **Biometri:** shared/biometrics saknar fortfarande egna krav och förmågor (se nedan)

### MkDocs / HTML-sajt

- [x] MkDocs uppsatt och fungerande
- [x] SVG-diagram med klickbara länkar
- [x] Komplett navigation med alla domäner + regler + tolkningar + öppna frågor + capabilities + krav
- [x] GitHub Pages action
- [x] Responsiva SVG-diagram
- [ ] Testa breadcrumbs / navigation.path (kräver Insiders?)
- [ ] Anpassa CSS (storlek på SVG:er, mobilvy?)

### Diagram — ID-konvention

- [x] Alla 25+ diagram uppgraderade till ID-konvention
- [x] Alla diagram har skinparams och notes med RULE/ART-ID
- [x] Informationsflödesdiagram för 4 domäner
- [x] Bredd-höjd-förhållande max 2:1

### Övrigt

- [ ] Ta bort `old/`-mappen när allt verifierats
- [ ] Verifiera att GitHub Action för SVG-generering fungerar
- [ ] Korsdomännoter (CROSS_DOMAIN_NOTES.md) bör konsolideras till en gemensam lista

---

## Korsdomännoter (samlat)

Följande spill identifierades vid skapande av capabilities/requirements:

### Shared (högsta prioritet)

| Förslag | Motivering |
|---------|------------|
| CAP-ID-001 Verify Identity | Används av screening + registration |
| CAP-INT-001 Provide Interpreter | Används av registration + screening + asylum procedure |
| CAP-BIO-001 Collect Biometric Data | Används av screening + eurodac |
| CAP-CHI-001 Safeguard Minors | Används av screening + eurodac + responsibility |
| REQ-INT-001–003 | Skapade — klart |

### Kopplingar mellan domäner

| Från | Till | Koppling |
|------|------|----------|
| Registration (REQ-APR-027-009) | Screening | Uppgifter från screeningformulär |
| Responsibility (REQ-AMMR-024-002) | Registration | Fryspunkt = registreringsdatum |
| Asylum Procedure (REQ-APR-035-001) | Registration | Prövningsfrist börjar vid inlämnande |
| Eurodac (REQ-EUR-015-001) | Registration | 72h-frist triggas av registrering |
| Border Procedure (REQ-APR-051-001) | Registration | 5-dagars inlämnande |
| Responsibility (REQ-AMMR-039-002) | Eurodac | Eurodac-träff förkortar framställansfrist |

---

## Prioriteringsordning

1. **Kvalitetsgranskning mot förordningstext** — domän för domän, se ovan. Korrekthet går före utökning
2. **Berika stubs** (5 st kvar) — tar bort döda sidor
3. **Shared-modulerna** — identity, children, biometrics behöver formella krav
4. **Eurodac** — krav och förmågor för art. 16–42, kort för art. 3–12 och 43–63
5. **Asylum Procedure artiklarna 8–14** — intervjugarantier
6. **Konsolidera korsdomännoter** till en gemensam underhållslista

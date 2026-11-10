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
- [ ] `shared/vulnerable-persons/articles/apr-020.md` — Garantier vid särskilda behov
- [ ] `shared/vulnerable-persons/articles/apr-021.md` — Garantier för ensamkommande barn
- [ ] `shared/statistics/articles/ammr-009.md` — Årlig rapport om asyl och migration
- [ ] `shared/statistics/articles/ammr-010.md` — Bedömning av migrationssituationen
- [x] `domains/eurodac/articles/eur-001.md` — Syftet med Eurodac
- [x] `domains/eurodac/articles/eur-002.md` — Definitioner
- [x] `domains/eurodac/articles/eur-016.md` — Information om den registrerades status

### Shared-moduler som saknar krav och capabilities

- [ ] shared/vulnerable-persons — Inga regler, krav eller capabilities
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
- [ ] Screening (förordning 2024/1356) — obs: textfilen saknas i `references/_text/` och måste först konverteras från mhtml
- [ ] Registrering (APR art. 26–33)
- [ ] Asylförfarande (APR)
- [ ] Gränsförfarande (APR art. 43–54)
- [ ] Ansvar (AMMR)
- [ ] Solidaritet (AMMR del IV) — art. 67–68 är redan kontrollerade
- [ ] Kris (förordning 2024/1359)
- [ ] Återvändande vid gräns (förordning 2024/1349)
- [ ] Shared-moduler (statistics, interpreters, vulnerable-persons, time-limits)

### Följdarbete efter Eurodac-granskningen

- [ ] **Ändrade regel-ID:** kontrollera externa system och dokument som använder de gamla betydelserna. RULE-EUR-018-001 avsåg tidigare sök och räddning (nu 024-001). RULE-EUR-024-001 och RULE-EUR-025-001 avsåg tidigare märkning och avmärkning (nu 031-001). RULE-EUR-031-001 avsåg tidigare Eurodac-träff (nu 027-001)
- [ ] **Tidsfrister:** för in Eurodacs övriga frister på [tidsfristsidan](shared/time-limits/README.md). Där finns i dag bara art. 15. Saknas gör 72 timmar för art. 18, 20, 22, 23 och 24, +48 timmar vid plötslig tillströmning (24.6), tio dagar för tillfälligt skydd (26.2), 24 timmar och en timme för jämförelse (38.2), tre arbetsdagar (38.6, omfattas av regeln om minst två arbetsdagar?) samt 72 timmar för underrättelser (16.4, 30.2, 31.1)
- [ ] **Data-retention:** komplettera Eurodac-raden med samtliga lagringstider i art. 29 (3 år och 1 år saknas), och överväg att markering (art. 31) ska synas i diagrammet
- [ ] **Flaggkatalogen:** överväg Eurodacs säkerhetsflagga (art. 17.2 i och 17.4) i egenskapsmodellen. Den sätts och tas bort av ursprungsmedlemsstaten och sprids via Eurodac inom 72 timmar
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

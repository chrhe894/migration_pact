# Backlog — Övergripande

## Nuläge (2025-07-31)

### Vad som finns

| Kunskapsobjekt | Antal | Kommentar |
|----------------|-------|-----------|
| Artikelfiler | ~120 | 9 domäner + shared |
| Regler (RULE) | ~105 | Med Syfte, Utlösare, Rättsverkan |
| Koncept (CON) | 43 | Med Syfte, Skapas av |
| Krav (REQ) | ~225 | 9 domäner + shared/interpreters |
| Capabilities (CAP) | 41 | 9 domäner |
| Processer (PROC) | 13 | Med Tillståndsförändringar |
| Diagram (PlantUML) | 25+ | Med ID-länkkonvention |
| Informationsflödesdiagram | 4 | Registration, Screening, Responsibility, Asylum Procedure |

### Spårbarhetskedja (implementerad)

```
Article → Rule → Requirement → Capability → Process → Diagram
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
- [ ] `domains/eurodac/articles/eur-001.md` — Syfte och tillämpningsområde
- [ ] `domains/eurodac/articles/eur-002.md` — Definitioner
- [ ] `domains/eurodac/articles/eur-016.md` — Åtgärder för identifiering

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
- [ ] Eurodac: artiklarna 1–2, 16–22, 24–28, 30–42 (övriga kategorier, brottsbekämpning) — de flesta saknas
- [ ] Asylum Procedure: artiklarna 8–14 (garantier, intervju) — delvis i shared men ej komplett

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

1. **Berika stubs** (8 st) — tar bort döda sidor
2. **Shared-modulerna** — identity, children, biometrics behöver formella krav
3. **Eurodac utökning** — de flesta artiklar saknas fortfarande
4. **Asylum Procedure artiklarna 8–14** — intervjugarantier
5. **Konsolidera korsdomännoter** till en gemensam underhållslista

# Nuläge — 2026-08-03 (uppdaterad)

## Vad som gjorts denna session

### Diagram

- Alla 25+ PlantUML-diagram uppdaterade med ID-länkkonvention (RULE-ID, ART-ID)
- Notes berikade med förklarande text och klickbara länkar
- 4 informationsflödesdiagram skapade (Registration, Screening, Responsibility, Asylum Procedure)
- Bredd-höjd-regel införd (max 2:1) — `determine-responsible-member-state.pu` och `responsibility-lifecycle.pu` omstrukturerade
- SVG:er görs responsiva via build-script

### Rule Cards (90 st)

- Alla berikade med Syfte, Utlösare, Rättsverkan
- Ny regel: RULE-APR-026-001 (ansökan görs)
- Ny regel: RULE-INT-002 (tolkningskostnader)

### Koncept (43 st)

- Alla berikade med Syfte, Skapas av

### Requirements (247+ st)

- Registration: 41 krav (100% av art. 26–29)
- Screening: 40 krav (100% av art. 5–18)
- Eurodac: 18 krav (100% av art. 13–29)
- Responsibility: 46 krav (100% av art. 24–46)
- Asylum Procedure: 32 krav (100% av art. 34–42, 55–56)
- Border Procedure: 22 krav (100% av art. 43–54)
- Solidarity: 9 krav (art. 57, 63, 66–67)
- Crisis: 9 krav (art. 2–4, 10–12)
- Return Border: 5 krav (art. 4–5)
- Shared/interpreters: 8 krav (art. 8, 30)
- Shared/vulnerable-persons: 10 krav (art. 20–21)
- Shared/statistics: 6 krav (AMMR art. 9–10)

### Capabilities (47 st)

- Registration: 6 | Screening: 8 | Eurodac: 5
- Responsibility: 8 | Asylum Procedure: 6 | Border Procedure: 3
- Solidarity: 3 | Crisis: 1 | Return Border: 1
- Shared/vulnerable-persons: 2 | Shared/statistics: 2

### Processer (13 st)

- Alla berikade med Tillståndsförändringar (Before → Action → After)

### Artiklar

- 8 stubs berikade med fullständigt innehåll (0 döda sidor kvar)
- 2 nya artiklar: APR art. 4, APR art. 26
- 11 saknade artikelreferenser åtgärdade

### Infrastruktur

- GitHub Pages workflow (deploy-pages.yml)
- build.sh med PlantUML → MkDocs → fix-svg-links → make-svg-responsive
- Navigation uppdaterad med Regler, Tolkningar, Öppna frågor, Capabilities, Krav per domän
- Tags-plugin aktiverat (pilot: Registration, 35 filer taggade)
- STYLE_GUIDE uppdaterad med mallar för Rule Cards, Koncept, Requirements, Capabilities, diagramkonventioner

### Fixar

- Trasiga länkar åtgärdade (apr-010, references/legislation/*)
- `navigation.expand` borttagen (kollapsad meny som standard)
- SVG-dimensioner responsiva via post-processing

---

## Nästa session

1. ~~**Täckningsgenomgång**~~ ✅ Klar
2. ~~**Status-uppdatering**~~ ✅ 398 filer Draft → Complete
3. ~~**Tags utrullning**~~ ✅ 603 filer taggade (alla domäner + shared)
4. ~~**Broken links**~~ ✅ 7 trasiga `../../shared/identity`-länkar fixade till `../../../shared/identity`
5. **Scenarios** — skapa ett scenario (t.ex. Ceuta 2026) som visar kunskapsbasens tillämpning
6. **Informationsmodell** — pilot för Registration (entiteter, attribut, relationer)

---

## Uppdatering 2026-08-03 (session 2)

### Status-uppdatering

- 398 filer uppdaterade från Draft → Complete (alla 9 domäner + shared)
- 0 Draft-filer kvar i docs/

### Eurodac-gap fyllt

- **21 nya artiklar** (art. 18–22, 24–26, 30–42) — alla personkategorier, märkning, radering, jämförelse, brottsbekämpning, dataskydd, informationsplikt
- **25 nya regler** (RULE-EUR-018 till RULE-EUR-042)
- Eurodac BACKLOG uppdaterad — primära artiklarna 1–42 nu dokumenterade
- README uppdaterad med alla nya artiklar och regler

# Backlog — Övergripande

## Kvar att göra

### Diagram — uppgradera till ID-konvention

Följande diagram saknar RULE-/ART-ID i notes (konventionen enligt STYLE_GUIDE):

- [x] `diagrams/end-to-end-overview.pu`
- [x] `domains/border-procedure/diagrams/border-vs-regular-comparison.pu`
- [x] `domains/registration/diagrams/applicant-status-and-documents.pu`
- [x] `domains/registration/diagrams/made-vs-registered-vs-lodged.pu`
- [x] `domains/responsibility/diagrams/responsibility-lifecycle.pu`
- [x] `domains/responsibility/diagrams/responsibility-overview.pu`
- [x] `domains/screening/diagrams/screening-to-registration-handoff.pu`
- [x] `domains/solidarity/diagrams/solidarity-concept-flow.pu`
- [x] `shared/time-limits/diagrams/time_limits.puml`

### MkDocs / HTML-sajt

- [x] MkDocs uppsatt och fungerande
- [x] SVG-diagram med klickbara länkar (via `<object>` + fix-svg-links.py)
- [x] Komplett navigation med alla domäner
- [ ] GitHub Pages action
- [ ] Testa breadcrumbs / navigation.path (kräver Insiders?)
- [ ] Anpassa CSS (storlek på SVG:er, mobilvy?)

### Domäninnehåll — kvarvarande luckor

- [ ] Registration: regler APR art. 4 (behöriga myndigheter)
- [ ] Screening: regler från art. 9 (samarbetsskyldigheter)
- [ ] Return border: artiklarna 8–12 (garantier, barn, hälsa)
- [ ] Eurodac: artiklarna 18–26, 30–42 (övriga kategorier, brottsbekämpning)

### Shared

- [ ] Interviews: artikelfilerna 11–14 behöver berikade notes och ID-konvention
- [ ] Vulnerable persons: regler under uppbyggnad
- [ ] Children: regler under uppbyggnad

### Övrigt

- [ ] Uppdatera STYLE_GUIDE med diagrammall (skinparams + konvention)
- [ ] Ta bort `old/`-mappen när allt verifierats
- [ ] Ta bort `shared/plantuml/` (tom mapp) och `shared/vulnerary-persons/` (tom efter flytt)
- [ ] Verifiera att GitHub Action för SVG-generering fungerar efter docs/-flytten

# ROADMAP

## Syfte

Detta dokument beskriver projektets övergripande utvecklingsplan.

Målet är att bygga kunskapsbasen stegvis. Varje fas ska vara så komplett som möjligt innan nästa påbörjas.

---

## Fas 0 – Repository Foundation

### Mål

Etablera projektets struktur och gemensamma arbetssätt.

### Leverabler

- Repositorystruktur
- README
- ROADMAP
- STYLE_GUIDE
- CONTRIBUTING
- DECISIONS
- Dokumentmallar

**Status:** ✅ Klar

---

## Fas 1 – Registrering

### Mål

Dokumentera processen för registrering av en ansökan om internationellt skydd.

### Leverabler

- Begrepp (7 st)
- Regler (14 st)
- Krav (41 st)
- Förmågor (6 st)
- Processbeskrivningar (3 st)
- PlantUML-diagram (6 st)
- Tolkningar (3 st)
- Öppna frågor (2 st)

**Status:** ✅ Klar

---

## Fas 2 – Screening

### Mål

Dokumentera screeningförfarandet.

### Leverabler

- Artiklar (14 st), Regler (14 st), Krav (43 st), Förmågor (8 st)
- Processer (2 st), Diagram (4 st), Koncept (5 st)

**Status:** ✅ Klar

---

## Fas 3 – Eurodac

### Mål

Dokumentera registrering och behandling enligt Eurodacförordningen.

### Leverabler

- Artiklar (30 st – art. 1–2, 13–42), Regler (33 st), Krav (18 st), Förmågor (5 st)
- Processer (1 st), Koncept (6 st)

**Status:** ✅ Klar (art. 1–42 dokumenterade; art. 3–12 arkitektur och art. 43–50 slutbestämmelser prioriteras ej)

---

## Fas 4 – Ansvarsfördelning

### Mål

Dokumentera reglerna om ansvarig medlemsstat.

### Leverabler

- Artiklar (24 st), Regler (26 st), Krav (46 st), Förmågor (8 st)
- Processer (1 st), Koncept (6 st), Diagram (6 st)

**Status:** ✅ Klar

---

## Fas 5 – Övriga rättsakter

### Mål

Dokumentera återstående delar av migrations- och asylpakten.

### Leverabler

| Domän | Artiklar | Regler | Krav | Förmågor |
|-------|----------|--------|------|----------|
| Asylförfarande | 16 | 10 | 33 | 6 |
| Gränsförfarande | 12 | 6 | 22 | 3 |
| Solidaritet | 13 | 4 | 9 | 3 |
| Kris | 12 | 3 | 9 | 1 |
| Återvändande vid gräns | 7 | 2 | 5 | 1 |

**Status:** ✅ Klar

---

## Fas 6 – Statisk webbsajt (MkDocs)

### Mål

Generera en klickbar HTML-sajt från kunskapsbasen, där:
- alla markdown-filer renderas som webbsidor,
- SVG-diagram visas inline med fungerande klickbara länkar,
- navigation och sökfunktion finns.

### Leverabler

- MkDocs Material-tema med svensk navigation
- GitHub Pages-deploy (deploy-pages.yml)
- PlantUML → SVG build-pipeline
- Tags-plugin med 219 ämnestaggar
- Responsiva SVG:er via post-processing
- Sökfunktion

**Status:** ✅ Klar

---

## Fas 7 – Delade moduler

### Mål

Dokumentera tvärgående begrepp som delas av flera domäner.

### Leverabler

| Modul | Filer | Status |
|-------|-------|--------|
| Tolkar | 16 | Klar |
| Sårbara personer | 17 | Klar |
| Statistik | 13 | Klar |
| Tidsfrister | 5 | Klar |
| Identitet | 4 | Klar |
| Biometri | 1 (README, fullt innehåll) | Klar |
| Barn | 1 (README, fullt innehåll) | Klar |
| Dokument | 1 (README, fullt innehåll) | Klar |
| Intervjuer | 1 (README, fullt innehåll) | Klar |
| Säkerhetskontroller | 1 (README, fullt innehåll) | Klar |

**Status:** ✅ Klar

---

## Fas 8 – Försvenskning och navigation

### Mål

Hela kunskapsbasens synliga yta ska vara på svenska. Taggar ska göra innehållet sökbart.

### Leverabler

- Alla navigationsrubriker på svenska
- Alla processnamn, begreppsnamn, domännamn på svenska
- Alla tillbaka-länkar (← [...]) på svenska
- Ämnestaggar (219 st) med åäö
- Livscykeldiagram (PlantUML med klickbara domänlänkar)

**Status:** ✅ Klar

---

## Fas 9 – Scenarios (planerad)

### Mål

Skapa konkreta tillämpningsexempel som visar hur kunskapsbasen kan användas i praktiken.

### Idéer

- **Ceuta 2026** — massankomst vid yttre gräns, screening under tidspress, gränsförfarande med kapacitetstak
- **Solidaritetsomfördelning från Grekland** — omfördelningsbeslut, överföring, ansvarets övergång
- **Efterföljande ansökan i Sverige** — ny ansökan efter avslag, upptagandeprövning, tidsfrister
- **Instrumentalisering vid östgräns** — krisförklaring, förlängda tidsfrister, undantag från gränsförfarande

### Format per scenario

- Bakgrund (vem, var, vad)
- Tidslinje som visar vilka domäner/regler som aktiveras
- Länkade regler (RULE-*), krav (REQ-*), processer (PROC-*)
- Slutresultat och alternativa utfall

**Status:** ~10 % (README finns, inget scenario skrivet)

---

## Fas 10 – Informationsmodell (planerad)

### Mål

Dokumentera entiteter, attribut och relationer för att möjliggöra framtida databasmodellering eller API-design.

### Idéer

- **Pilot: Registration** — entiteter som Person, Ansökan, Registreringshandling, Sökandehandling, Myndighet
- **ER-diagram** (PlantUML class diagram) per domän
- **Attributlista** per entitet (datatyp, källa i lagtext, kardinalitet)
- **Relationer** (en ansökan har en sökande, en registrering görs av en myndighet)
- **Gemensamma entiteter** (Person, Medlemsstat, Tidsfrist) i shared/

### Format

- En `information-model/` mapp per domän (eller i shared/)
- PlantUML class-diagram
- Markdown-fil per entitet med attribut och relationer

**Status:** 0 % (ej påbörjad)

---

## Långsiktiga mål

När kunskapsbasen är komplett bör den kunna användas för att:

- förstå sambandet mellan olika rättsakter,
- följa en regel tillbaka till dess rättsliga källa,
- visualisera processer och beslutsflöden,
- identifiera beroenden mellan regler,
- ge en samlad överblick över migrations- och asylpakten,
- stödja kravställning och systemdesign för migrationsmyndigheter,
- utbilda handläggare och jurister i det nya regelverket.

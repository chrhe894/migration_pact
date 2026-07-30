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

**Status:** Pågår

---

## Fas 1 – Registration of an Application

### Mål

Dokumentera processen för registrering av en ansökan om internationellt skydd.

### Leverabler

- Begrepp
- Regler
- Processbeskrivning
- PlantUML-diagram
- Tolkningar
- Öppna frågor

**Status:** Pågår

---

## Fas 2 – Screening

### Mål

Dokumentera screeningförfarandet.

**Status:** Pågår

---

## Fas 3 – Eurodac

### Mål

Dokumentera registrering och behandling enligt Eurodacförordningen.

**Status:** Pågår

---

## Fas 4 – Ansvarsfördelning

### Mål

Dokumentera reglerna om ansvarig medlemsstat.

**Status:** Planerad

---

## Fas 5 – Övriga rättsakter

Dokumentera återstående delar av migrations- och asylpakten.

**Status:** Planerad

---

## Långsiktiga mål

När kunskapsbasen är komplett bör den kunna användas för att:

- förstå sambandet mellan olika rättsakter,
- följa en regel tillbaka till dess rättsliga källa,
- visualisera processer och beslutsflöden,
- identifiera beroenden mellan regler,
- ge en samlad överblick över migrations- och asylpakten.

---

## Fas 6 – Statisk webbsajt (MkDocs)

### Mål

Generera en klickbar HTML-sajt från kunskapsbasen, där:
- alla markdown-filer renderas som webbsidor,
- SVG-diagram visas inline med fungerande klickbara länkar,
- navigation och sökfunktion finns.

### Motivering

Relativa länkar i SVG-diagram fungerar korrekt i en statisk sajt men inte på GitHub. En genererad sajt gör kunskapsbasen tillgänglig för jurister och handläggare utan behov av kodeditor.

### Verktyg

MkDocs med Material-tema (eller liknande).

**Status:** Planerad

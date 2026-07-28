# STYLE GUIDE

## Syfte

Denna guide beskriver hur dokumentation i projektet ska utformas.

Målet är att skapa ett repository som är:

- konsekvent,
- lätt att läsa,
- lätt att underhålla,
- enkelt att granska,
- enkelt att återanvända.

---

# Grundprinciper

## Skriv för att förklara

Dokumentationen ska hjälpa läsaren att förstå lagstiftningen.

Undvik att efterlikna lagtextens språk när det inte behövs.

Skriv hellre:

> Ansökan registreras.

än:

> Registrering av ansökan företas.

---

## Beskriv – tolka inte

Beskriv vad rättsakten anger.

Om något är en tolkning ska det tydligt framgå.

---

## En uppgift på ett ställe

Information ska inte dupliceras.

Om samma regel används på flera ställen ska den refereras, inte kopieras.

---

# Språk

## Repository

Repositoryts tekniska struktur använder engelska.

Exempel:

- katalognamn
- filnamn
- mallar

## Innehåll

Projektets innehåll skrivs på svenska.

Det gäller:

- dokumentation
- kommentarer
- analyser
- diagram

---

# Markdown

Använd standardiserad GitHub Markdown.

Rubriker ska följa en logisk struktur.

Exempel:

```text
# Dokument

## Avsnitt

### Underavsnitt
```

Undvik onödigt djupa rubriknivåer.

---

# Rubriker

Rubriker skrivs med normal svensk rubriksättning.

Exempel:

```
Registrering av en ansökan
```

Inte:

```
Registrering Av En Ansökan
```

---

# Listor

Använd punktlistor när information inte behöver numreras.

Använd numrerade listor endast när ordningen är viktig.

---

# Referenser

Hänvisa alltid till rättskällan.

Exempel:

- Artikel 29
- Skäl 36
- Bilaga II

---

# Filnamn

Filnamn skrivs:

- med små bokstäver,
- med engelska namn,
- utan mellanslag.

Exempel:

```
registration.md

screening.md

take_back.md
```

---

# PlantUML

PlantUML används för att beskriva:

- processer,
- beslut,
- sekvensdiagram,
- relationer.

Diagram ska vara enkla.

Undvik:

- färger,
- avancerad styling,
- manuella placeringar,
- onödig dekor.

Diagrammet ska beskriva struktur.

Den rättsliga innebörden dokumenteras i Markdown.

---

# Dokumentstorlek

Föredra många små dokument framför få stora.

Om ett dokument blir omfattande bör innehållet delas upp.

---

# Källhänvisningar

Alla rättsliga påståenden ska kunna spåras till en källa.

Om något är:

- en tolkning,
- ett antagande,
- en slutsats,

ska det framgå tydligt.

---

# Länkar

## Regelreferenser ska vara klickbara

Referenser till regler i processbeskrivningar ska vara relativa Markdown-länkar.

Exempel:

```markdown
- [RULE-APR-027-001](../rules/rule-apr-027-001.md) — Skyldighet att registrera
```

## Länka i flödessteg

Om ett steg i ett processhuvudflöde eller alternativt flöde styrs av en regel ska regeln länkas i steget.

Exempel:

```markdown
3. Uppgifter samlas in ([RULE-APR-027-002](../rules/rule-apr-027-002.md)).
```

## Diagram länkar till regler

Aktiviteter i PlantUML-diagram länkas till rule.md, inte direkt till artikel-filer.

Navigationskedjan är: **diagram → process → regel → artikel**.

Exempel:

```plantuml
:[[../rules/rule-apr-027-001.md Registrera ansökan]];
```

## Delade aktiviteter länkas

Shared Activities i processbeskrivningar ska länkas till aktivitetsfilen under `shared/`.

Exempel:

```markdown
- [Verify identity](../../../shared/identity/activities/verify-identity.md)
```

---

# Back-länkar

Varje `.md`-fil i en domän ska ha en back-länk längst upp som pekar till domänens README.

Exempel:

```markdown
← [Registration](../README.md)
```

Varje domäns README ska ha en back-länk till kunskapsbasens top-nivå README.

Exempel:

```markdown
← [Kunskapsbasen](../../README.md)
```

Placering: första raden i filen, före dokumentets rubrik.

Exempel:

```html
<div align="right">← <a href="../README.md">Registration</a></div>
```

För domän-README:

```html
<div align="right">← <a href="../../README.md">Kunskapsbasen</a></div>
```

---

# Status

Dokument kan använda följande status:

- Draft
- Review
- Approved

---

# Versionshantering

Repositoryt utvecklas stegvis.

Varje commit ska utgöra en logisk förändring.

Undvik stora commits med många orelaterade ändringar.

---

# Konsistens

När flera alternativ är möjliga ska projektets befintliga struktur följas.

Konsekvens är viktigare än personliga preferenser.
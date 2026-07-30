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

- färger (utom notes i svagt gult),
- avancerad styling,
- manuella placeringar,
- onödig dekor.

Diagrammet ska beskriva struktur.

Den rättsliga innebörden dokumenteras i Markdown.

---

# Diagramkonventioner

## Aktiviteter ska länkas till regler

Varje processaktivitet som styrs av en regel ska länkas:

```plantuml
:[[../rules/rule-apr-027-001.md Registrera ansökan]];
```

## Notes ska innehålla ID-länk och förklaring

Varje aktivitet som har en tidsfrist, ett undantag eller en konsekvens ska ha en note.

I en note ska varje länk använda **dokumentets rubrik-ID** som synlig länktext.
ID:t är exakt det som står som `# RUBRIK` i den länkade filen.

Konventioner:
- Regler: `[[path RULE-XXX-YYY-NNN]]` — t.ex. `RULE-APR-027-004`
- Artiklar: `[[path ART-XXX-YYY]]` — t.ex. `ART-APR-027`
- Koncept: `[[path CON-XXX-YYY]]`
- Processer: `[[path PROC-XXX-NNN]]`

Länktexten ska **aldrig** vara en fri beskrivning — den ska alltid vara det formella ID:t.

Exempel — note med regel-ID:

```plantuml
:[[../rules/rule-apr-027-001.md Registrera ansökan]];
note right
  == Tidsfrist ==
  **5 dagar** från ansökan gjord
  ---
  Vid massinflöde: **15 dagar**
  ([[../rules/rule-apr-027-004.md RULE-APR-027-004]])
  ---
  Vid kris: **4 veckor**
end note
```

Exempel — note med artikel-ID:

```plantuml
note right
  [[../articles/apr-027.md ART-APR-027]], punkt 7 — registrering
  sker först **efter** avslutad screening
end note
```

Exempel — note med regel-ID och förklarande text (utan rubrik):

```plantuml
:[[../../../shared/interpreters/activities/determine-interpreter-needs.md Bedöm tolkbehov]];
note right
  [[../../../shared/interpreters/rules/rule-int-001.md RULE-INT-001]]
  Tolk ska tillhandahållas om
  ändamålsenlig kommunikation
  inte kan säkerställas
end note
```

## Juridiska milstolpar i notes

Viktiga rättsliga tillstånd markeras med en note:

```plantuml
note right
  == Juridisk milstolpe ==
  **Application registered**
  - Sökandens rättigheter aktiveras
  - Eurodac-frist börjar (72h)
end note
```

## If-satser och partition-namn förblir plain-text

Länka inte i if-villkor eller partition-rubriker — det försämrar läsbarheten.

## Undvik djup horisontell nesting

PlantUML lägger nästlade `if/else`-grenar horisontellt. Djup nesting gör diagrammet extremt brett och oläsligt.

**Gräns:** Bredd-höjd-förhållande ska inte överstiga 2:1.

**Lösning vid djup nesting:** Använd separata `if ... stop endif`-block i sekvens istället för nästlade `if/else/if/else`:

```plantuml
' ❌ FEL — genererar brett diagram
if (A?) then (Ja)
  :...;
else (Nej)
  if (B?) then (Ja)
    :...;
  else (Nej)
    if (C?) then (Ja)
      :...;
    else (Nej)
      :...;
    endif
  endif
endif

' ✅ RÄTT — vertikalt vattenfallsmönster
if (A?) then (Ja)
  :...;
  stop
endif

if (B?) then (Ja)
  :...;
  stop
endif

if (C?) then (Ja)
  :...;
  stop
endif

:Residualfall;
```

Alternativt: om varje gren representerar ett möjligt *utfall* snarare än ett *beslut*, samla dem i en note med numrerade vägar.

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

# Begrepp

## Relaterade begrepp ska länkas

Refererade begrepp i CON-filer ska uttryckas som relativa Markdown-länkar.

Exempel:

```markdown
## Relaterade begrepp

- [CON-REG-001 Application for international protection](application-for-international-protection.md)
- [CON-REG-003 Registration](registration.md)
```

## Används i ska länkas

Artiklar och processer som använder ett begrepp ska länkas i sektionen "Används i".

Exempel:

```markdown
## Används i

- [ART-APR-027](../articles/apr-027.md)
- [PROC-REG-001 Registration of an application](../processes/registration-of-an-application.md)
```

## Begrepp länkar till begrepp, artiklar och processer

Konceptfiler (`CON-*.md`) ska använda relativa Markdown-länkar i följande avsnitt:

- `Rättslig grund` ska länka till relevant artikel-fil när artikeln finns i kunskapsbasen.
- `Relaterade begrepp` ska länka till andra `CON-*.md`-filer.
- `Används i` ska länka till relevanta `ART-*.md`, `PROC-*.md` eller shared activity-filer.

Exempel:

```markdown
## Relaterade begrepp

- [CON-REG-003 Registration](registration.md)
- [CON-SCR-001 Screening](../../screening/concepts/screening.md)

## Används i

- [ART-APR-027](../articles/apr-027.md)
- [PROC-REG-001 Registration of an application](../processes/registration-of-an-application.md)
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
```

För domän-README:

```html
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

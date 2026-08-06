# Förslag på förbättringar

## Scenarios

### Vad

Konkreta tillämpningsexempel som demonstrerar kunskapsbasens användning i verkliga eller verklighetsnära situationer.

### Varför

- Gör abstrakta regler gripbara
- Visar hur domäner samverkar i praktiken
- Fungerar som "guided tour" för nya användare
- Validerar att regler, tidsfrister och processer hänger ihop

### Förslag på scenarios

| Scenario | Domäner | Poäng |
|----------|---------|-------|
| **Ceuta 2026 — massankomst** | Screening → Registration → Gränsförfarande → Kris | Visar krismekanismen, kapacitetstak, förlängda tidsfrister |
| **Omfördelning från Grekland** | Ansvar → Solidaritet → Registration (mottagande stat) | Visar hela solidaritetsflödet från tryck till genomförd omplacering |
| **Efterföljande ansökan i Sverige** | Registration → Asylförfarande (efterföljande) | Visar upptagandeprövning, nya omständigheter, tidsfrister |
| **Instrumentalisering vid östgräns** | Screening → Kris → Gränsförfarande | Krisförklaring, undantag, säkerhetskontroll |
| **Familj med barn vid gräns** | Screening → Registration → Ansvar (art. 25–28) | Barn-garantier, familjeförfarande, ensamkommande |

### Format per scenario

```markdown
# Scenario: [Namn]

## Bakgrund
Kort beskrivning av situationen (vem, var, när).

## Tidslinje

| Dag | Händelse | Domän | Regel |
|-----|----------|-------|-------|
| 0 | Person omhändertas | Screening | RULE-SCR-008-001 |
| 1 | Identifiering | Screening | RULE-SCR-014-001 |
| ... | ... | ... | ... |

## Aktiverade regler
- [RULE-...](länk)

## Slutresultat
Vad som händer och alternativa utfall.

## Lärdomar
Vilka domänsamband som illustreras.
```

---

## Informationsmodell

### Vad

En formell beskrivning av entiteter (objekt), attribut och relationer som finns implicit i kunskapsbasen.

### Varför

- Möjliggör databasmodellering för IT-system
- Gör det tydligt vilka dataobjekt som passerar mellan domäner
- Stödjer API-design och systemintegration
- Identifierar gemensamma entiteter som delas mellan domäner

### Förslag på pilot: Registrering

**Entiteter:**

| Entitet | Källa | Beskrivning |
|---------|-------|-------------|
| Person | APR art. 27 | Tredjelandsmedborgare eller statslös |
| Ansökan | APR art. 27 | Ansökan om internationellt skydd |
| Registreringshandling | APR art. 29.1 | Handling som bekräftar registrering |
| Sökandehandling | APR art. 29.2 | Handling som utfärdas vid inlämnande |
| Myndighet | APR art. 4 | Registreringsmyndighet eller behörig myndighet |
| EurodacDataset | Eurodac art. 15 | Biometriskt dataset i centralsystemet |

**Relationer:**

```
Person ──1:N──▸ Ansökan
Ansökan ──1:1──▸ Registreringshandling
Ansökan ──1:1──▸ Sökandehandling
Ansökan ──N:1──▸ Myndighet (registrerar)
Person ──1:N──▸ EurodacDataset
```

**Format:**
- PlantUML class-diagram per domän
- Markdown per entitet (attribut, datatyp, källa, kardinalitet)
- Gemensamma entiteter (Person, Medlemsstat) i `shared/information-model/`

---

## Övriga förbättringsidéer

### Kort sikt

- [ ] **Shared-stubs** — fylla biometri, barn, dokument-modulerna med regler/krav
- [ ] **Sökoptimering** — lägga till `description`-fält i frontmatter för bättre sökresultat
- [ ] **Diagram-rebuild** — regenerera alla SVG:er (nya .pu-filer från denna session saknar SVG)

### Medellång sikt

- [ ] **Täckningsmätare** — automatisk rapport som visar % artiklar med regler/krav per domän
- [ ] **Korsreferensindex** — automatgenererad sida som visar vilka regler som refereras av vilka krav
- [ ] **Versionshistorik per artikel** — visa ändringar sedan förordningen publicerades
- [ ] **Flerspråkig ordlista** — EN/SV/FR för centrala begrepp (stöd för EU-kontext)

### Lång sikt

- [ ] **API-dokumentation** — OpenAPI-spec baserad på informationsmodellen
- [ ] **Interaktivt scenario-verktyg** — användaren väljer parametrar, systemet visar tillämpliga regler
- [ ] **Regelmotor-export** — exportera regler i maskinläsbart format (JSON/YAML) för regelmotor

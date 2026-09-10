---
tags:
  - shared
  - tidsfrister
  - koncept
  - suspensiv-verkan
  - förlängning
  - frysning
---

# Frysning och förlängning av tidsfrister

## Översikt

Migrationspaktens tidsfrister är som utgångspunkt absoluta — de löper obönhörligen och vid överskridande inträder rättsliga konsekvenser (ansvarsövergång, frigivning, förfarandets avslutande). Det finns dock två mekanismer som påverkar tidsfristernas gång:

```text
TIDSFRISTER
│
├── FRYSNING (stopp + start)
│       Fristen pausas och börjar löpa igen vid en specifik händelse.
│       Enda grund: suspensiv verkan vid överklagande.
│
└── FÖRLÄNGNING
        Fristen ersätts av en längre frist.
        Grunder: massinflöde, komplexitet, kris, avvikande.
```

---

## 1. Frysning av tidsfrister (suspensiv verkan)

### Mekanism

När en person överklagar ett beslut och beviljas **suspensiv verkan** pausas den löpande tidsfristen. Fristen börjar löpa igen den dag den suspensiva verkan upphör.

### Tillämpningsområde

| Frist som fryses | Rättslig grund | Regel |
|------------------|----------------|-------|
| 5-veckorsfristen för överföring vid förvar | [AMMR art. 45.3 b](../../../domains/responsibility/articles/ammr-045.md) | [RULE-AMMR-045-002](../../../domains/responsibility/rules/rule-ammr-045-002.md) |
| 6-månadersfristen för överföring (normalt förfarande) | [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) | [RULE-AMMR-046-001](../../../domains/responsibility/rules/rule-ammr-046-001.md) |
| 12-veckorsfristen för återvändande vid gräns | [Return art. 5](../../../domains/return-border-procedure/articles/return-005.md) | [REQ-RET-005-004](../../../domains/return-border-procedure/requirements/req-ret-005-004.md) |

### Princip

```text
Frist börjar löpa → Överklagande + suspensiv verkan beviljas → PAUS → Suspensiv verkan upphör → Frist börjar löpa igen
```

- Fristen pausas — den stannar där den var.
- Fristen börjar löpa igen från samma punkt (inte från noll).
- Det finns **ingen** annan dokumenterad grund för att frysa en tidsfrist (t.ex. administrativa skäl räcker inte).

### Konsekvens

Utan frysningsmekanism skulle beviljad suspensiv verkan i praktiken kunna leda till att en tidsfrist löper ut under pågående domstolsprocess, med oavsiktlig ansvarsövergång eller frigivning som följd.

---

## 2. Förlängning av tidsfrister

### 2.1 Vid oproportionellt inflöde (massinflöde)

| Frist | Ordinarie | Förlängd | Rättslig grund | Regel |
|-------|-----------|----------|----------------|-------|
| Registrering av ansökan | 5 dagar | 15 dagar | [APR art. 27.5](../../../domains/registration/articles/apr-027.md) | [RULE-TL-REG-002](../rules/rule-tl-reg-002.md) |
| Inlämnande av ansökan | 21 dagar | 2 månader | [APR art. 28.5](../../../domains/registration/articles/apr-028.md) | [RULE-TL-LOD-002](../rules/rule-tl-lod-002.md) |

**Utlösare:** Ett oproportionellt stort antal ansökningar görs inom samma tidsperiod och det blir omöjligt att hålla ordinarie frister.

### 2.2 Vid ärendets komplexitet

| Frist | Ordinarie | Förlängd | Rättslig grund | Regel |
|-------|-----------|----------|----------------|-------|
| Prövning i sak | 6 månader | 15 månader | [APR art. 35](../../../domains/asylum-procedure/articles/apr-035.md) | [RULE-APR-035-002](../../../domains/asylum-procedure/rules/rule-apr-035-002.md) |

**Utlösare:** Den beslutande myndigheten bedömer att ärendet innefattar komplexa sak- eller rättsfrågor som kräver längre utredningstid. Förlängningen ska vara motiverad.

### 2.3 Vid kris (Krishanteringsförordningen 2024/1359)

| Frist | Ordinarie | Vid kris | Rättslig grund | Regel |
|-------|-----------|----------|----------------|-------|
| Registrering | 5/15 dagar | 4 veckor | [Kris art. 10](../../../domains/crisis/articles/crisis-010.md) | [RULE-CRI-010-001](../../../domains/crisis/rules/rule-cri-010-001.md) |
| Gränsförfarande varaktighet | 12 veckor | 18 veckor | [Kris art. 11](../../../domains/crisis/articles/crisis-011.md) | [RULE-CRI-011-001](../../../domains/crisis/rules/rule-cri-011-001.md) |
| Framställan om övertagande | 2 månader | 4 månader | [Kris art. 12](../../../domains/crisis/articles/crisis-012.md) | [RULE-CRI-012-001](../../../domains/crisis/rules/rule-cri-012-001.md) |
| Svar på framställan | 1 månad | 2 månader | [Kris art. 12](../../../domains/crisis/articles/crisis-012.md) | [RULE-CRI-012-001](../../../domains/crisis/rules/rule-cri-012-001.md) |
| Överföring | 6 månader | 1 år | [Kris art. 12](../../../domains/crisis/articles/crisis-012.md) | [RULE-CRI-012-001](../../../domains/crisis/rules/rule-cri-012-001.md) |

**Utlösare:** Rådet fastställer att en kris- eller force majeure-situation föreligger i en medlemsstat.

### 2.4 Vid avvikande (specifik för överföring)

| Frist | Ordinarie | Vid avvikande | Rättslig grund | Regel |
|-------|-----------|---------------|----------------|-------|
| Överföring | 6 månader | 18 månader | [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) | [RULE-AMMR-046-001](../../../domains/responsibility/rules/rule-ammr-046-001.md) |

**Utlösare:** Personen avviker (absconds) och är inte tillgänglig för överföring.

---

## Samlad kravtabell per domän

Tabellen samlar frysnings- och förlängningsfristerna, vilken process fristen hamnar i, och länkar till domänens krav (REQ) där sådana finns.

Kolumnerna **Startar i** och **Stoppar i** anger den rättsliga start- respektive stopphändelsen enligt förordningen (den händelse då klockan börjar respektive slutar löpa).

### Frysning (suspensiv verkan)

Vid beviljad suspensiv verkan pausas fristen; den återupptas när den suspensiva verkan upphör (se avsnitt 1).

| Domän | Frist | Mekanism | Process | Krav (REQ) | Startar i | Stoppar i |
|-------|-------|----------|---------|------------|-----------|-----------|
| Ansvar | 5 v — överföring vid förvar (art. 45.3 b) | Frysning | [PROC-RES-001](../../../domains/responsibility/processes/determine-responsible-member-state.md) | [REQ-AMMR-045-005](../../../domains/responsibility/requirements/req-ammr-045-005.md) | Godtagande/bekräftelse, eller dagen suspensiv verkan upphör | Överföringen verkställs |
| Ansvar | 6 mån — överföring (art. 46) | Frysning | [PROC-RES-001](../../../domains/responsibility/processes/determine-responsible-member-state.md) | [REQ-AMMR-046-001](../../../domains/responsibility/requirements/req-ammr-046-001.md) | Godtagande/bekräftelse, eller dagen rättsmedlet upphör ha suspensiv verkan | Överföringen verkställs |
| Återvändande vid gräns | 12 v — återvändandeförfarande (Return art. 5) | Frysning | [PROC-RET-001](../../../domains/return-border-procedure/processes/return-border-procedure.md) | [REQ-RET-005-004](../../../domains/return-border-procedure/requirements/req-ret-005-004.md) | Återvändandeförfarandet inleds (efter avslag i gränsförfarande) | Återvändandet verkställs, eller 12 v löper ut (inresa tillåts) |

### Förlängning

Kris-fristerna (art. 10–12) har samma start- och stopphändelser som sina ordinarie motsvarigheter — det är bara det maximala fristmåttet som förlängs.

| Domän | Frist | Mekanism | Process | Krav (REQ) | Startar i | Stoppar i |
|-------|-------|----------|---------|------------|-----------|-----------|
| Registrering | 5 → 15 dagar vid massinflöde (art. 27.5) | Förlängning | [PROC-REG-001](../../../domains/registration/processes/registration-of-an-application.md) | [REQ-APR-027-005](../../../domains/registration/requirements/req-apr-027-005.md) | Ansökan görs (application made) | Ansökan registreras |
| Registrering | 21 dagar → 2 mån vid massinflöde (art. 28.5) | Förlängning | [PROC-REG-002](../../../domains/registration/processes/lodging-an-application.md) | [REQ-APR-028-005](../../../domains/registration/requirements/req-apr-028-005.md) | Ansökan registreras | Bokad tid för inlämnande ges / ansökan lämnas in |
| Asylförfarande | 6 → 15 mån vid komplexitet (art. 35) | Förlängning | [PROC-ASY-001](../../../domains/asylum-procedure/processes/examine-an-application.md) | [REQ-APR-035-002](../../../domains/asylum-procedure/requirements/req-apr-035-002.md) | Ansökan lämnas in (lodging) | Beslut i sak fattas |
| Ansvar | 6 → 18 mån vid avvikande (art. 46) | Förlängning | [PROC-RES-001](../../../domains/responsibility/processes/determine-responsible-member-state.md) | [REQ-AMMR-046-002](../../../domains/responsibility/requirements/req-ammr-046-002.md) | Godtagande/bekräftelse | Överföringen verkställs, eller 18 mån löper ut (ansvar övergår) |
| Kris | Registrering → 4 v (kris art. 10) | Förlängning | [PROC-CRI-001](../../../domains/crisis/processes/activate-crisis-measures.md) | [REQ-CRI-010-001](../../../domains/crisis/requirements/req-cri-010-001.md) | Ansökan görs (application made) | Ansökan registreras |
| Kris | Gränsförfarande → 18 v (kris art. 11) | Förlängning | [PROC-CRI-001](../../../domains/crisis/processes/activate-crisis-measures.md) | [REQ-CRI-011-002](../../../domains/crisis/requirements/req-cri-011-002.md) | Gränsförfarandet inleds | Gränsförfarandet avslutas, eller 18 v löper ut |
| Kris | Framställan → 4 mån (kris art. 12) | Förlängning | [PROC-CRI-001](../../../domains/crisis/processes/activate-crisis-measures.md) | [REQ-CRI-012-001](../../../domains/crisis/requirements/req-cri-012-001.md) | Ansökan registreras | Framställan om övertagande skickas |
| Kris | Svar → 2 mån (kris art. 12) | Förlängning | [PROC-CRI-001](../../../domains/crisis/processes/activate-crisis-measures.md) | [REQ-CRI-012-002](../../../domains/crisis/requirements/req-cri-012-002.md) | Framställan tas emot | Svar lämnas (eller tyst godkännande inträder) |
| Kris | Överföring → 1 år (kris art. 12) | Förlängning | [PROC-CRI-001](../../../domains/crisis/processes/activate-crisis-measures.md) | [REQ-CRI-012-003](../../../domains/crisis/requirements/req-cri-012-003.md) | Godtagande/bekräftelse | Överföringen verkställs |

---

## Avgränsning: frysning vs. förlängning

| | Frysning | Förlängning |
|--|----------|-------------|
| **Effekt** | Fristen pausas och återupptas | Fristen ersätts av en längre frist |
| **Grund** | Suspensiv verkan (rättsmedel) | Massinflöde, komplexitet, kris, avvikande |
| **Vem utlöser** | Domstol (beviljar suspensiv verkan) | Myndighet/rådet (konstaterar grund) |
| **Varaktighet** | Så länge rättsmedlet har suspensiv verkan | Permanent ny frist (med tak) |
| **Begränsning** | Fristens totala längd ökar med pausperioden | Aldrig obegränsad — alltid ett maxtak |

---

## Viktig princip

Tidsfristerna kan **aldrig** förlängas obegränsat. Varje förlängningsgrund har ett definierat tak. Om varken frysning eller förlängning är tillämplig löper fristen obönhörligen — med rättsliga konsekvenser vid överskridande.

---

## Se även

- [Tidsfrister — översikt](../README.md)
- [Uppsikt](uppsikt.md) — Tidsfrister kopplade till uppsikt
- [RULE-AMMR-045-002](../../../domains/responsibility/rules/rule-ammr-045-002.md) — Suspensiv verkan fryser 5-veckorsfristen
- [RULE-AMMR-046-001](../../../domains/responsibility/rules/rule-ammr-046-001.md) — Överföringsfrist 6 månader / 18 månader
- [RULE-APR-035-002](../../../domains/asylum-procedure/rules/rule-apr-035-002.md) — Förlängning vid komplexitet
- [RULE-CRI-012-001](../../../domains/crisis/rules/rule-cri-012-001.md) — Förlängda frister vid kris

---

## Status

Complete

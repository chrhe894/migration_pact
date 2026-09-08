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

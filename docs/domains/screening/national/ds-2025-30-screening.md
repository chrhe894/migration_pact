---
tags:
  - screening
  - nationell-implementering
  - ds-2025-30
---

# Nationell implementering — Screening

> ⚠️ Baseras på Ds 2025:30 (departementsskrivelse, ej antagen lag). Kan ändras.

## Källa

Ds 2025:30, kapitel 7 (volym 1, avsnitt 7.1–7.13)

---

## Övergripande

EU:s screeningförordning (2024/1356) är direkt tillämplig. Sverige gör inga undantag från förordningens tidsfrister eller kontrollmoment. De nationella kompletteringarna rör **vem som gör vad** och **befogenheter**.

---

## Myndighetstilldelning

| Moment i screeningprocessen | Ansvarig myndighet | Konsekvens för IT |
|----------------------------|-------------------|-------------------|
| Screeningprocessen (huvudansvar) | **Polismyndigheten** | Polis äger arbetsflödet |
| Identifiering / verifiering av identitet | Polismyndigheten + Migrationsverket (gemensamt) | Uppgiftsutbyte mellan myndigheter |
| Säkerhetskontroll (art. 15–16) | Polismyndigheten (ensam) | Databassökningar SIS, VIS, Eurodac, Ecris-TCN, Etias, Europol, Interpol |
| Sårbarhetskontroll (art. 12.3) | Specialiserad personal vid Polismyndigheten + Migrationsverket | Gemensam bedömning |
| Hälsokontroll (art. 12.1) | **Regionerna** (kvalificerad medicinsk personal) | Separat system; rapporterar resultat till screeningmyndighet |
| Biometrisk registrering (art. 8.5 d) | Polismyndigheten + Migrationsverket | Eurodac-överföring |
| Screeningformulär + avslutning | Polismyndigheten + Migrationsverket | Formulär överlämnas till registreringsmyndighet |
| Bistånd vid screening | Tullverket, Kustbevakningen | Samma befogenheter som polis vid kroppsvisitering |

---

## Nya befogenheter (nationell komplettering)

### Kvarhållande vid screening

| Parameter | Värde |
|-----------|-------|
| Rättslig grund | Ny bestämmelse i 9 kap. 11 a § UtlL |
| Max tid | **12 timmar** |
| Förlängning | + 12 timmar vid särskilda skäl (t.ex. lång transport till screeningplats, plötsligt ökat inflöde) |
| Vem beslutar | Polisman, passkontrollant, tulltjänsteman, kustbevakningstjänsteman |
| Undantag | Gäller inte den som redan ansökt om internationellt skydd (då gäller mottagandedirektivets regler) |
| **Systemkonsekvens** | Kräver tidsstämpellogik — registrering av start/slut för kvarhållande |

### Kroppsvisitering

| Parameter | Värde |
|-----------|-------|
| Rättslig grund | Ny bestämmelse i 9 kap. UtlL |
| Syfte | Fastställa identitet under screening |
| Vem får utföra | Polisman, passkontrollant, tulltjänsteman, kustbevakningstjänsteman |
| Begränsning | Hänsynsprincipen; utförs av person av samma kön |
| **Systemkonsekvens** | Loggning av åtgärd i screeningformulär |

### Uppsikt och förvar — ny grund

| Parameter | Värde |
|-----------|-------|
| Kategori | Tredjelandsmedborgare som ska genomgå screening men **inte sökt asyl** |
| Förutsättning | Risk för avvikande |
| Vem beslutar | Polismyndigheten |
| **Systemkonsekvens** | Ny förvarskategori; koppling till screeningformulär |

---

## Uppgiftsskyldighet

| Från | Till | Syfte |
|------|------|-------|
| Migrationsverket | Polismyndigheten | Uppgifter som behövs för identifiering/verifiering |
| Regionerna | Screeningmyndigheterna | Resultat av hälsokontroll |
| Polismyndigheten | Migrationsverket | Screeningformulär vid avslutad screening |

---

## Tidsfrister (oförändrade vs EU)

| Moment | Tidsfrist | Källa |
|--------|-----------|-------|
| Screening vid yttre gräns | Max **7 dagar** | Art. 8.3 screeningförordningen |
| Screening inom territoriet | Max **3 dagar** | Art. 8.4 screeningförordningen |
| Kvarhållande (SE-tillägg) | Max **12 + 12 timmar** | Ds 2025:30 |

Ingen svensk avvikelse från EU:s 7-dagars-/3-dagarsfrister.

---

## Oberoende övervakningsmekanism

Sverige bedömer att befintliga organ (JO, JK, Institutet för mänskliga rättigheter) uppfyller kraven i art. 10 screeningförordningen. Ingen ny myndighet föreslås.

---

## Koppling till kunskapsbasen

- [Screening — processer](../processes/screening-at-external-border.md)
- [Screening — CAP-SCR-003 Verify Identity](../capabilities/cap-scr-003.md)
- [Screening — CAP-SCR-004 Security Check](../capabilities/cap-scr-004.md)
- [Ds 2025:30 — översikt](../../../shared/time-limits/national/ds-2025-30.md)

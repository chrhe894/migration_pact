---
tags:
  - shared
  - tidsfrister
  - koncept
  - fristtyp
  - accept-till-beslut
---

# Fristtyp: Accept till beslut (ATB)

## Vad är en fristtyp?

En **fristtyp** är en återanvändbar mall för en tidsfrist, definierad av sin **startpunkt** och sin **karaktär** — inte av en enskild artikel. Samma fristtyp kan *instansieras* i flera processer, med olika slutpunkt och längd. Detta speglar hur tidsfrister definieras systemmässigt i verksamheten.

Se även fristtypen [Nekad begäran till omprövning](../../../domains/responsibility/interpretations/take-charge-take-back-timelimits.md) (mellanstatlig omprövning).

---

## Definition — ATB

**Accept till beslut (ATB)** är en fristtyp där klockan börjar ticka vid **accept** — dvs. när en framställan/avisering godtas eller bekräftas, **antingen uttryckligen eller genom tyst godkännande** — och löper fram till en definierad slutpunkt (ett beslut eller en verkställd åtgärd).

```text
ACCEPT (uttrycklig eller tyst)  ──►  [ X tid ]  ──►  SLUTPUNKT
```

Det gemensamma för alla ATB-instanser är alltså **startpunkten: accept**. Slutpunkt och längd varierar per instans.

---

## Instanser i AMMR (ansvarsförfarandet)

ATB förekommer i **överföringsförfarandet** — och gäller den stat som **skickat** framställan/avisering och fått accept (UT-riktningen), oavsett om det rör övertagande eller återtagande.

| Instans | Process | Slutpunkt | Längd | Rättslig grund |
|---------|---------|-----------|-------|----------------|
| ATB — beslut | [Övertagande UT](../../../domains/responsibility/interpretations/take-charge-out.md) | Överföringsbeslut fattas och meddelas | **2 veckor** | [AMMR art. 42](../../../domains/responsibility/articles/ammr-042.md) |
| ATB — verkställighet | [Övertagande UT](../../../domains/responsibility/interpretations/take-charge-out.md) | Överföringen verkställd | **6 månader** | [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) |
| ATB — beslut | [Återtagande UT](../../../domains/responsibility/interpretations/take-back-out.md) | Överföringsbeslut fattas och meddelas | **2 veckor** | [AMMR art. 42](../../../domains/responsibility/articles/ammr-042.md) |
| ATB — verkställighet | [Återtagande UT](../../../domains/responsibility/interpretations/take-back-out.md) | Överföringen verkställd | **6 månader** | [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) |

De två instanserna löper i **sekvens**: först 2 veckor från accept till beslut, därefter 6 månader från accept till verkställd överföring (fristerna räknas båda från accept, inte staplade efter varandra).

---

## Avgränsningar (vanliga missförstånd)

- **Gäller UT-riktningen, inte IN.** Både beslut (art. 42) och verkställighet (art. 46) är den överförande/anmodande statens uppgift. Den mottagande staten (IN) *ger* accepten men bär inte ATB-fristerna.
- **Gäller övertagande OCH återtagande** — inte bara övertagande. Startpunkten "accept" finns i båda (godtagande resp. bekräftelse).
- **Inte i ansvarskompensation.** Vid ansvarskompensation (solidaritet, [AMMR art. 63](../../../domains/solidarity/articles/ammr-063.md)) sker ingen fysisk överföring — därför är art. 42/46-fristerna inte tillämpliga.
- **Inte i återvändandeförfarandet.** ATB hör hemma i ansvar/överföring ([PROC-RES-001](../../../domains/responsibility/processes/determine-responsible-member-state.md)), inte i återvändande vid gräns.

---

## Koppling till frysning

6-månadersinstansen (art. 46) kan **frysas**: om personen överklagar och beviljas suspensiv verkan pausas fristen tills verkan upphör (art. 43.3). Se [Frysning och förlängning](frysning-och-forlangning.md). Startpunkten räknas då om till "den dag rättsmedlet inte längre har suspensiv verkan".

---

## Se även

- [Tidsfrister — översikt](../README.md)
- [Övertagande/återtagande — tidsfrister per riktning](../../../domains/responsibility/interpretations/take-charge-take-back-timelimits.md)
- [Frysning och förlängning](frysning-och-forlangning.md)
- [AMMR art. 42](../../../domains/responsibility/articles/ammr-042.md) · [art. 46](../../../domains/responsibility/articles/ammr-046.md)

---

## Status

Complete

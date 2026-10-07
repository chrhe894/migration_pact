---
tags:
  - shared
  - tidsfrister
  - koncept
  - fristtyp
  - ATB
  - accept-till-beslut
---

# Fristtyp: Accept till beslut (ATB)

## Vad är en fristtyp?

En **fristtyp** är en återanvändbar mall för en tidsfrist, definierad av sin **startpunkt** och sin **karaktär** — inte av en enskild artikel. Samma fristtyp kan *instansieras* i flera processer, med olika slutpunkt och längd. Detta speglar hur tidsfrister definieras systemmässigt i verksamheten.

Se även fristtypen [Nekad begäran till omprövning (TNO)](fristtyp-nekad-begaran-till-omprovning.md) (mellanstatlig omprövning).

---

## Definition — ATB

**Accept till beslut (ATB)** är en fristtyp där klockan börjar ticka vid **accept** — dvs. när en framställan/avisering godtas eller bekräftas, **antingen uttryckligen eller genom tyst godkännande** — och löper fram till en definierad slutpunkt (ett beslut eller en verkställd åtgärd).

```text
ACCEPT (uttrycklig eller tyst)  ──►  [ X tid ]  ──►  SLUTPUNKT
```

Det gemensamma för alla ATB-instanser är alltså **startpunkten: accept**. Slutpunkt och längd varierar per instans.

---

## Instanser i AMMR (ansvarsförfarandet)

ATB förekommer i **överföringsförfarandet** — och gäller den stat som **skickat** framställan/avisering och fått accept (UT-riktningen), oavsett om det rör övertagande eller återtagande. Slutpunkten för ATB är alltid **överföringsbeslutet** (art. 42).

| Instans | Process | Slutpunkt | Längd | Rättslig grund |
|---------|---------|-----------|-------|----------------|
| ATB — beslut | [Övertagande UT](../../../domains/responsibility/interpretations/take-charge-out.md) | Överföringsbeslut fattas och meddelas | **2 veckor** | [AMMR art. 42](../../../domains/responsibility/articles/ammr-042.md) |
| ATB — beslut | [Återtagande UT](../../../domains/responsibility/interpretations/take-back-out.md) | Överföringsbeslut fattas och meddelas | **2 veckor** | [AMMR art. 42](../../../domains/responsibility/articles/ammr-042.md) |

> **Verkställigheten är en egen fristtyp.** Själva överföringen (6 mån / 18 mån vid avvikande / 4 v vid förvar, art. 46) hör till fristtypen [Accept till överföring (ATÖ)](fristtyp-accept-till-overforing.md), inte till ATB. Båda startar vid accept och löper **parallellt** — ATB fram till beslutet, ATÖ fram till den verkställda överföringen.

---

## Avgränsningar (vanliga missförstånd)

- **Gäller UT-riktningen, inte IN.** Både beslut (art. 42) och verkställighet (art. 46) är den överförande/anmodande statens uppgift. Den mottagande staten (IN) *ger* accepten men bär inte ATB-fristerna.
- **Gäller övertagande OCH återtagande** — inte bara övertagande. Startpunkten "accept" finns i båda (godtagande resp. bekräftelse).
- **Inte i ansvarskompensation.** Vid ansvarskompensation (solidaritet, [AMMR art. 63](../../../domains/solidarity/articles/ammr-063.md)) sker ingen fysisk överföring — därför är art. 42-fristen inte tillämplig.
- **Inte i återvändandeförfarandet.** ATB hör hemma i ansvar/överföring ([PROC-RES-001](../../../domains/responsibility/processes/determine-responsible-member-state.md)), inte i återvändande vid gräns.
- **Beslut, inte verkställighet.** ATB löper till överföringsbeslutet (art. 42). Själva verkställigheten (art. 46) är fristtypen [ATÖ](fristtyp-accept-till-overforing.md).

---

## Frysning och förlängning

ATB-fristen **varken fryses eller förlängs**. [AMMR art. 42.1](../../../domains/responsibility/articles/ammr-042.md) sätter en fast tvåveckorsfrist för själva beslutet utan någon frysnings- eller förlängningsmekanism, och ingen av de dokumenterade grunderna (suspensiv verkan, massinflöde, komplexitet, kris, avvikande) är kopplad till art. 42.

Orsaken är sekvensen: beslutet fattas **först**, och det är först därefter som personen kan överklaga och begära suspensiv verkan. Den suspensiva verkan pausar då **verkställigheten** — alltså den parallella [ATÖ](fristtyp-accept-till-overforing.md)-fristen (art. 46), vars startpunkt räknas om till "den dag rättsmedlet inte längre har suspensiv verkan" ([AMMR art. 43.3](../../../domains/responsibility/articles/ammr-043.md)) — inte beslutsfristen.

Se [Frysning och förlängning](frysning-och-forlangning.md) för helheten och [ATÖ](fristtyp-accept-till-overforing.md) för den rörliga fristen.

---

## Se även

- [Tidsfrister — översikt](../README.md)
- [Fristtyp: Accept till överföring (ATÖ)](fristtyp-accept-till-overforing.md)
- [Övertagande/återtagande — tidsfrister per riktning](../../../domains/responsibility/interpretations/take-charge-take-back-timelimits.md)
- [Frysning och förlängning](frysning-och-forlangning.md)
- [AMMR art. 42](../../../domains/responsibility/articles/ammr-042.md)

---

## Status

Complete

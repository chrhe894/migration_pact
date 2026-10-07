---
tags:
  - shared
  - tidsfrister
  - koncept
  - fristtyp
  - ATÖ
  - accept-till-overforing
  - överföringsfrist
---

# Fristtyp: Accept till överföring (ATÖ)

## Vad är en fristtyp?

En **fristtyp** är en återanvändbar mall för en tidsfrist, definierad av sin **startpunkt** och sin **karaktär** — inte av en enskild artikel. Samma fristtyp kan *instansieras* i flera processer, med olika slutpunkt och längd. Detta speglar hur tidsfrister definieras systemmässigt i verksamheten.

Se även fristtyperna [Accept till beslut (ATB)](fristtyp-accept-till-beslut.md) och [Nekad begäran till omprövning (TNO)](fristtyp-nekad-begaran-till-omprovning.md).

---

## Definition — ATÖ

**Accept till överföring (ATÖ)**, även kallad **överföringsfrist**, är en fristtyp där klockan börjar ticka vid **accept** — dvs. när en framställan/avisering godtas eller bekräftas — och löper fram till att **överföringen är verkställd**.

```text
ACCEPT (uttrycklig eller tyst)  ──►  [ X tid ]  ──►  ÖVERFÖRING VERKSTÄLLD
```

Det gemensamma för alla ATÖ-instanser är **startpunkten: accept** och **slutpunkten: verkställd överföring**. Längden varierar beroende på personens situation (normalfall, avvikande, förvar).

---

## Karaktär — återkommande drag oavsett instans

Dessa egenskaper följer med fristtypen i varje process där den instansieras:

- **Startpunkt:** accept (godtagande eller bekräftelse), eller — om rättsmedel haft suspensiv verkan — den dag verkan upphör.
- **Slutpunkt:** överföringen är fysiskt verkställd.
- **Sanktion vid överskridande:** om överföringen inte verkställs i tid **övergår ansvaret** till den överförande staten. Detta är systemets yttersta kontrollmekanism.
- **Kan frysas:** vid överklagande med suspensiv verkan pausas fristen (se [Frysning och förlängning](frysning-och-forlangning.md)).
- **Kan förlängas:** vid avvikande ersätts normalfristen av en längre frist.
- **Bärs av den överförande staten (UT-riktningen):** det är den stat som skickat framställan/avisering och fått accept som bär ATÖ-fristen.

Att **missad frist = ansvarsövergång** är ATÖ:s signum och skiljer den från [ATB](fristtyp-accept-till-beslut.md) (där slutpunkten är ett *beslut*, inte en verkställd åtgärd).

---

## Instanser i AMMR (ansvarsförfarandet)

ATÖ instansieras i **överföringsförfarandet** och gäller den stat som skickat framställan/avisering och fått accept (UT-riktningen) — oavsett om det rör övertagande eller återtagande.

| Instans | Situation | Längd | Startpunkt | Rättslig grund |
|---------|-----------|-------|------------|----------------|
| ATÖ — normal | Ordinarie överföring | **6 månader** | Accept (godtagande/bekräftelse) | [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) |
| ATÖ — avvikande | Personen avviker (absconding) | **18 månader** | Accept | [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) |
| ATÖ — förvar | Personen är i förvar | **4 veckor** | Accept | [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) |

Alla tre räknas från accept (inte staplade). Vid överskridande övergår ansvaret till den överförande staten ([RULE-AMMR-046-001](../../../domains/responsibility/rules/rule-ammr-046-001.md)).

> **Angränsande förvarsfrist (ej samma instans):** [AMMR art. 45.3](../../../domains/responsibility/articles/ammr-045.md) anger en överföringsfrist om **5 veckor** inom förvarsregimen (se [RULE-AMMR-045-001](../../../domains/responsibility/rules/rule-ammr-045-001.md)). Den ligger i art. 45:s förvarskontext, medan ATÖ-instansen "förvar" ovan är art. 46:s fyraveckorsfrist. De ska inte sammanblandas; vid frihetsberövande är de kortare art. 45-fristerna styrande och fristöverskridande leder till **frigivning**, inte enbart ansvarsövergång.

---

## Riktningsperspektiv (IN vs. UT)

| Perspektiv | Sveriges roll | Bär ATÖ-fristen? |
|------------|---------------|------------------|
| [Övertagande UT](../../../domains/responsibility/interpretations/take-charge-out.md) | Anmodande stat (fått godtagande) | Ja — ska verkställa överföringen |
| [Övertagande IN](../../../domains/responsibility/interpretations/take-charge-in.md) | Anmodad stat (gav godtagande) | Nej — tar emot personen |
| [Återtagande UT](../../../domains/responsibility/interpretations/take-back-out.md) | Aviserande stat (fått bekräftelse) | Ja — ska verkställa överföringen |
| [Återtagande IN](../../../domains/responsibility/interpretations/take-back-in.md) | Mottagande stat (bekräftade) | Nej — tar emot personen |

---

## Förhållande till ATB

ATÖ och [ATB](fristtyp-accept-till-beslut.md) har **samma startpunkt (accept)** men olika slutpunkt, och löper parallellt i överföringsförfarandet:

```text
ACCEPT ──┬── ATB: 2 veckor ──► Överföringsbeslut (art. 42)
         │
         └── ATÖ: 6 mån / 18 mån / 4 v ──► Överföring verkställd (art. 46)
```

Båda räknas från accept — de staplas inte. ATB leder fram till *beslutet*, ATÖ till den *verkställda överföringen*.

---

## Avgränsningar (vanliga missförstånd)

- **Gäller UT-riktningen, inte IN.** Verkställigheten är den överförande/anmodande statens uppgift. Den mottagande staten ger accepten men bär inte ATÖ-fristen.
- **Gäller övertagande OCH återtagande** — startpunkten "accept" finns i båda (godtagande resp. bekräftelse).
- **Inte i ansvarskompensation.** Vid ansvarskompensation (solidaritet, [AMMR art. 63](../../../domains/solidarity/articles/ammr-063.md)) sker ingen fysisk överföring — art. 46-fristen är inte tillämplig.
- **Förvar: skilj art. 45 från art. 46.** Se noten ovan.

---

## Se även

- [Tidsfrister — översikt](../README.md)
- [Fristtyp: Accept till beslut (ATB)](fristtyp-accept-till-beslut.md)
- [Fristtyp: Nekad begäran till omprövning (TNO)](fristtyp-nekad-begaran-till-omprovning.md)
- [Frysning och förlängning](frysning-och-forlangning.md)
- [Övertagande/återtagande — tidsfrister per riktning](../../../domains/responsibility/interpretations/take-charge-take-back-timelimits.md)
- [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) · [art. 45](../../../domains/responsibility/articles/ammr-045.md)

---

## Status

Complete

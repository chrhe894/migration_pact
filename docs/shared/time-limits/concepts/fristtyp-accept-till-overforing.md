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
- **Ny startpunkt vid suspensiv verkan:** om överklagandet har suspensiv verkan räknas fristen från det slutliga beslutet om överklagandet (art. 46.1), respektive från den dag den suspensiva verkan upphör (art. 45.3 b). Fristen pausas alltså inte, utan börjar om från noll (se [Frysning och förlängning](frysning-och-forlangning.md)).
- **Kan förlängas:** till högst ett år vid frihetsberövande och till högst tre år vid avvikande med mera (art. 46.2).
- **Bärs av den överförande staten (UT-riktningen):** det är den stat som skickat framställan/avisering och fått accept som bär ATÖ-fristen.

Att **missad frist = ansvarsövergång** är ATÖ:s signum och skiljer den från [ATB](fristtyp-accept-till-beslut.md) (där slutpunkten är ett *beslut*, inte en verkställd åtgärd).

---

## Instanser — överföringsförfarandet (ansvar, art. 46)

ATÖ instansieras i **överföringsförfarandet** och gäller den stat som skickat framställan/avisering och fått accept (UT-riktningen) — oavsett om det rör övertagande eller återtagande.

| Instans | Situation | Längd | Startpunkt | Rättslig grund |
|---------|-----------|-------|------------|----------------|
| ATÖ — normal | Ordinarie överföring | **6 månader** | Accept (godtagande/bekräftelse) | [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) |
| ATÖ — frihetsberövad | Överföringen har inte kunnat verkställas därför att personen varit frihetsberövad | Högst **1 år** | Accept | [AMMR art. 46.2](../../../domains/responsibility/articles/ammr-046.md) |
| ATÖ — avvikande m.m. | Personen eller medföljande familjemedlem avviker, fysiskt motsätter sig, avsiktligt förhindrar eller uppfyller inte medicinska krav | Högst **3 år** | Underrättelsen till ansvarig stat | [AMMR art. 46.2](../../../domains/responsibility/articles/ammr-046.md) |
| ATÖ — förvar | Personen är i förvar | **5 veckor** | Accept, eller dagen suspensiv verkan upphör | [AMMR art. 45.3](../../../domains/responsibility/articles/ammr-045.md) |

Förlängningarna ersätter normalfristen och staplas inte. Ett-årsfristen räknas från accept, tre-årsfristen från underrättelsen till den ansvariga staten. Fem-veckorsfristen vid förvar gäller i stället för art. 46. Vid överskridande övergår ansvaret till den överförande staten ([RULE-AMMR-046-001](../../../domains/responsibility/rules/rule-ammr-046-001.md)).

---

## Instans — omfördelning (solidaritet, art. 67.11)

Samma fristtyp dyker upp i **omfördelningsförfarandet**. Här sker en faktisk fysisk överföring av personen från den gynnade staten till omfördelningsmedlemsstaten, så ATÖ-karaktären gäller — men med egen frist och egen startpunkt (omfördelningsmedlemsstatens bekräftelse).

| Instans | Situation | Längd | Startpunkt | Rättslig grund |
|---------|-----------|-------|------------|----------------|
| ATÖ — omfördelning | Verkställd omfördelning | **4 veckor** | Omfördelningsmedlemsstatens bekräftelse (art. 67.9) | [AMMR art. 67.11](../../../domains/solidarity/articles/ammr-067.md) → [RULE-AMMR-067-001](../../../domains/solidarity/rules/rule-ammr-067-001.md) |

Fristen räknas från bekräftelsen, eller — vid överklagande med suspensiv verkan — från det slutliga beslutet (art. 67.11 hänvisar uttryckligen till art. 43.3). Omfördelningens överföringsbeslut fattas separat inom **1 vecka** från bekräftelsen (art. 67.10); det är omfördelningens motsvarighet till [ATB](fristtyp-accept-till-beslut.md), fast kortare.

> **Angränsande förvarsfrist (ej samma instans):** [AMMR art. 45.3](../../../domains/responsibility/articles/ammr-045.md) anger en överföringsfrist om **5 veckor** inom förvarsregimen (se [RULE-AMMR-045-001](../../../domains/responsibility/rules/rule-ammr-045-001.md)). Den gäller i stället för art. 46 när personen hålls i förvar. Fristöverskridande leder då till **frigivning** ur förvar (art. 45.4), medan art. 39, 41 och 46 fortsätter att gälla.

> **Rättelse:** sidan angav tidigare en fyraveckorsfrist vid förvar i art. 46 och "18 månader" vid avvikande. Art. 46 innehåller ingen förvarsfrist, och förlängningen är högst tre år (art. 46.2).

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
         └── ATÖ: 6 mån / 1 år / 3 år / 5 v ──► Överföring verkställd (art. 46)
```

Båda räknas från accept — de staplas inte. ATB leder fram till *beslutet*, ATÖ till den *verkställda överföringen*.

---

## Frysning och förlängning

ATÖ är den fristtyp i överföringsförfarandet som faktiskt påverkas av både frysning och förlängning. Se [Frysning och förlängning](frysning-och-forlangning.md) för helheten.

- **Frysning (suspensiv verkan):** Om personen överklagar överföringsbeslutet och beviljas suspensiv verkan ([AMMR art. 43.3](../../../domains/responsibility/articles/ammr-043.md)), räknas ATÖ-fristen från det slutliga beslutet om överklagandet (art. 46.1), och vid förvar från den dag den suspensiva verkan upphör (art. 45.3 b). En **ny full frist** börjar då löpa. Detsamma gäller omfördelningsinstansen — art. 67.11 hänvisar uttryckligen till art. 43.3.
- **Förlängning (art. 46.2):** 6-månadersinstansen får förlängas till högst **ett år** om personen varit frihetsberövad, och till högst **tre år** om personen eller en medföljande familjemedlem avviker, fysiskt motsätter sig, avsiktligt förhindrar överföringen eller inte uppfyller de medicinska kraven. Detta är ATÖ:s egna förlängningsgrunder.
- **Förlängning vid kris:** Vid aktiverad krissituation kan överföringsfristen förlängas till **1 år** ([Kris art. 12](../../../domains/crisis/articles/crisis-012.md)).

> Till skillnad från ATB (som varken fryses eller förlängs) är ATÖ alltså den rörliga fristen — den kan både pausas och ersättas av en längre frist.

---

## Avgränsningar (vanliga missförstånd)

- **Gäller UT-riktningen, inte IN.** Verkställigheten är den överförande/anmodande statens uppgift. Den mottagande staten ger accepten men bär inte ATÖ-fristen.
- **Gäller övertagande OCH återtagande** — startpunkten "accept" finns i båda (godtagande resp. bekräftelse).
- **Solidaritet: skilj ansvarskompensation från omfördelning.**
  - **Ansvarskompensation** ([AMMR art. 63](../../../domains/solidarity/articles/ammr-063.md)) innebär att en stat *övertar prövningsansvaret* — ingen fysisk överföring av personen sker, så ingen ATÖ-frist gäller.
  - **Omfördelning** ([AMMR art. 67](../../../domains/solidarity/articles/ammr-067.md)) innebär en *fysisk överföring* av personen — därför gäller ATÖ-karaktären, med fyraveckorsfristen i art. 67.11 (se instanstabellen ovan).
- **Förvar: skilj art. 45 från art. 46.** Se noten ovan.

---

## Se även

- [Tidsfrister — översikt](../README.md)
- [Fristtyp: Transfer — genomförande av överföring (TGÖ)](fristtyp-transfer-genomforande-overforing.md) — de inre koordineringsfristerna inom ATÖ-ramen
- [Fristtyp: Accept till beslut (ATB)](fristtyp-accept-till-beslut.md)
- [Fristtyp: Nekad begäran till omprövning (TNO)](fristtyp-nekad-begaran-till-omprovning.md)
- [Frysning och förlängning](frysning-och-forlangning.md)
- [Övertagande/återtagande — tidsfrister per riktning](../../../domains/responsibility/interpretations/take-charge-take-back-timelimits.md)
- [AMMR art. 46](../../../domains/responsibility/articles/ammr-046.md) · [art. 45](../../../domains/responsibility/articles/ammr-045.md)

---

## Status

Complete

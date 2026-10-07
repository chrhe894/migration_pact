---
tags:
  - shared
  - tidsfrister
  - koncept
  - fristtyp
  - nekad-begaran-till-omprovning
  - omprövning
---

# Fristtyp: Nekad begäran till omprövning (TNO)

## Vad är en fristtyp?

En **fristtyp** är en återanvändbar mall för en tidsfrist, definierad av sin **startpunkt** och sin **karaktär** — inte av en enskild artikel. Samma fristtyp kan *instansieras* i flera processer, med olika slutpunkt och längd. Detta speglar hur tidsfrister definieras systemmässigt i verksamheten.

Se även fristtypen [Accept till beslut (ATB)](fristtyp-accept-till-beslut.md).

---

## Definition — TNO

**Nekad begäran till omprövning (TNO)** är en fristtyp där klockan börjar ticka vid ett **nekande** — dvs. när en mellanstatlig begäran avslås eller inte bekräftas — och ger den begärande staten en kort frist att **begära omprövning**, följt av en frist för motparten att **svara**.

```text
NEKANDE (avslag / icke-bekräftelse)  ──►  [ begär omprövning inom X ]  ──►  [ svar inom Y ]  ──►  förfarandet avslutas
```

Det gemensamma för alla TNO-instanser är alltså **startpunkten: ett nekande** och **karaktären: ett snabbt mellanstatligt korrektiv** utan domstol. Begärandefristen och svarsfristen varierar per instans.

TNO är **rent mellanstatlig** och ska inte förväxlas med individens rättsmedel mot ett överföringsbeslut ([AMMR art. 43](../../../domains/responsibility/articles/ammr-043.md)).

---

## Karaktär — återkommande drag oavsett instans

Dessa egenskaper följer med fristtypen i varje process där den instansieras:

- **Startpunkt:** ett nekande (avslag på framställan, eller icke-bekräftelse av avisering).
- **Tvåstegsstruktur:** först en frist att *begära* omprövning, sedan en frist att *svara*.
- **Hård avslutning:** när svarsfristen löper ut **avslutas** förfarandet, oavsett om svar lämnats.
- **Tystnad ≠ medgivande:** uteblivet svar innebär **inte** bekräftelse — tvärtemot grundförfarandets tysta godkännande ([RULE-AMMR-040-001](../../../domains/responsibility/rules/rule-ammr-040-001.md), [RULE-AMMR-041-001](../../../domains/responsibility/rules/rule-ammr-041-001.md)).
- **Förlänger inte ordinarie frister:** omprövningen påverkar inte de ordinarie svarsfristerna i grundförfarandet.
- **Rättslig grund:** genomförandeförordning (EU) 2025/2055 (tillämpningsföreskrift till AMMR).

Just det att **tystnad inte är medgivande** och att **förfarandet avslutas hårt vid fristens slut** skiljer TNO:s karaktär från accept-startade fristtyper (ATB/ATÖ), där tyst godkännande och ansvarsövergång är huvudregeln.

---

## Instanser i AMMR (ansvarsförfarandet)

TNO förekommer i **två riktningar** i det mellanstatliga ansvarsförfarandet. Karaktären är densamma; startpunkten och begärandefristen skiljer sig.

| Instans | Process | Startpunkt (nekande) | Begär omprövning inom | Svar inom | Rättslig grund |
|---------|---------|----------------------|------------------------|-----------|----------------|
| TNO — övertagande | [Övertagande UT](../../../domains/responsibility/interpretations/take-charge-out.md) | Framställan om övertagande **avslås** (AMMR art. 40) | **3 veckor** från avslaget | **2 veckor** | [2025/2055 art. 9.2](../../../references/legislation/ammr-implementing.md) → [RULE-AMMR-IMPL-009-001](../../../domains/responsibility/rules/rule-ammr-impl-009-001.md) |
| TNO — återtagande | [Återtagande UT](../../../domains/responsibility/interpretations/take-back-out.md) | Avisering om återtagande **inte bekräftas** (ansvaret sägs ha upphört, AMMR art. 37) | **2 veckor** efter icke-bekräftelsen | **2 veckor** | [2025/2055 art. 15.3–15.4](../../../references/legislation/ammr-implementing.md) → [RULE-AMMR-IMPL-015-001](../../../domains/responsibility/rules/rule-ammr-impl-015-001.md) |

Begärandefristen är alltså **3 veckor vid övertagande** men **2 veckor vid återtagande**; svarsfristen är **2 veckor i båda**.

---

## Riktningsperspektiv (IN vs. UT)

Vem som bär vilken frist beror på Sveriges roll:

| Perspektiv | Sveriges roll | TNO-frist som gäller Sverige |
|------------|---------------|------------------------------|
| [Övertagande UT](../../../domains/responsibility/interpretations/take-charge-out.md) | Anmodande stat (fått avslag) | *Begär* omprövning inom 3 veckor |
| [Övertagande IN](../../../domains/responsibility/interpretations/take-charge-in.md) | Anmodad stat (gav avslag) | *Svarar* inom 2 veckor |
| [Återtagande UT](../../../domains/responsibility/interpretations/take-back-out.md) | Aviserande/meddelande stat (fått icke-bekräftelse) | *Begär* omprövning inom 2 veckor |
| [Återtagande IN](../../../domains/responsibility/interpretations/take-back-in.md) | Mottagande stat (icke-bekräftade) | *Svarar* inom 2 veckor |

---

## Avgränsningar (vanliga missförstånd)

- **Enbart mellanstatlig.** TNO rör förhandlingen mellan två medlemsstater om vem som är ansvarig stat. Den förekommer **inte** i övriga domäner — där "omprövning" nämns (asyl-, gränsförfarande) avses individens rättsmedel. Se [Två slags omprövning](../../../domains/responsibility/interpretations/take-charge-take-back-timelimits.md#tva-slags-omprovning-blanda-inte-ihop).
- **Avslag/nekande som angränsar men INTE är TNO:** t.ex. ett *avslag i gränsförfarandet* startar återvändandegränsförfarandet ([RULE-RET-004-001](../../../domains/return-border-procedure/rules/rule-ret-004-001.md)). Det är ett annat mönster — avslaget startar ett *nytt förfarande*, inte en begäran om mellanstatlig omprövning.
- **Förlänger inte grundfristerna.** De ordinarie svarsfristerna i AMMR art. 40/41 påverkas inte av att omprövning begärs.

---

## Se även

- [Tidsfrister — översikt](../README.md)
- [Fristtyp: Accept till beslut (ATB)](fristtyp-accept-till-beslut.md)
- [Övertagande/återtagande — tidsfrister per riktning](../../../domains/responsibility/interpretations/take-charge-take-back-timelimits.md)
- [RULE-AMMR-IMPL-009-001](../../../domains/responsibility/rules/rule-ammr-impl-009-001.md) · [RULE-AMMR-IMPL-015-001](../../../domains/responsibility/rules/rule-ammr-impl-015-001.md)
- [Genomförandeförordning (EU) 2025/2055](../../../references/legislation/ammr-implementing.md)

---

## Status

Complete

# Delat — Personliga intervjuer

## Syfte

Denna shared-modul dokumenterar den **personliga intervjun** som en gemensam förmåga i asyl- och ansvarsförfarandena. Intervjun är den viktigaste källan till direkt information från sökanden och återanvänds av flera förfaranden med gemensamma krav och rutiner.

En central egenskap är att personliga intervjuer **ska spelas in** (eller dokumenteras i rapport) och att varje intervjutyp är kopplad till en rutin för vad intervjun ska behandla.

---

## Personliga intervjuer som gemensam förmåga

<object type="image/svg+xml" data="diagrams/personal-interview-capability.svg" width="100%"></object>

Källa: [`personal-interview-capability.pu`](diagrams/personal-interview-capability.pu)

---

## Primära rättskällor

- [APR artikel 8.3](../interpreters/articles/apr-008.md) — Rätt till tolkning vid registrering, inlämnande och personlig intervju
- [APR artikel 11](../../domains/asylum-procedure/articles/apr-011.md) — Intervju för ansvarsbestämning
- [APR artikel 12](../../domains/asylum-procedure/articles/apr-012.md) — Intervju om grunderna för ansökan
- [APR artikel 13](../../domains/asylum-procedure/articles/apr-013.md) — Krav på de personliga intervjuerna
- [APR artikel 14](../../domains/asylum-procedure/articles/apr-014.md) — Rapportering och inspelning

---

## Typer av personliga intervjuer

Varje typ har en egen rutin för vad intervjun ska behandla.

| Typ | Rutin — vad intervjun behandlar | Artikel |
|-----|--------------------------------|---------|
| Ansvarsintervju | Familjemedlemmar, uppehållstillstånd, resvägar och andra omständigheter som avgör ansvarig stat (AMMR-kriterier) | [APR art. 11](../../domains/asylum-procedure/articles/apr-011.md) |
| Upptagandeintervju | Om ansökan kan avvisas (t.ex. första asylland, säkert tredjeland) — genomförs innan avvisningsbeslut | [APR art. 38](../../domains/asylum-procedure/articles/apr-038.md) |
| Sakintervju | Grunderna för internationellt skydd — sökanden ges tillfälle att fullständigt redogöra för sina skäl | [APR art. 12](../../domains/asylum-procedure/articles/apr-012.md) |

---

## Krav på intervjuerna (art. 13)

- Ska genomföras av kvalificerad personal vid den beslutande myndigheten.
- Sökanden ska ges tillfälle att fullständigt redogöra för sin ansökan.
- Tolk ska tillhandahållas om ändamålsenlig kommunikation inte kan säkerställas (se [shared/interpreters](../interpreters/README.md)).
- Intervjun ska vara individuell (utan familjemedlemmars närvaro) om det inte anses nödvändigt.
- Förhållandena ska vara förtroliga och möjliggöra att sökanden redogör för sina skäl.
- Intervjuaren ska ha kunskap om sökandens personliga situation och kulturella bakgrund.
- Sökanden får begära intervjuare och tolk av samma kön.

---

## Rapportering och inspelning (art. 14)

Inspelningen är en obligatorisk del av varje personlig intervju:

- Intervjun ska dokumenteras i en rapport **eller** genom ljud-/videoinspelning.
- Sökanden ska ges möjlighet att korrigera felaktigheter.
- Rapporten eller inspelningen ska ingå i akten och följer ärendet genom förfarandet.

---

## Undantag från personlig intervju

Intervju om grunderna behöver inte genomföras om:
- myndigheten kan fatta positivt beslut baserat på tillgängliga bevis,
- sökanden inte kan intervjuas av allvarliga medicinska skäl (temporärt — intervju ska genomföras när det åter är möjligt).

---

## Koppling till shared/interpreters

Tolkbehovet vid intervjun hanteras av [shared/interpreters](../interpreters/README.md). [APR artikel 13.3 b](../../domains/asylum-procedure/articles/apr-013.md) anger att om ändamålsenlig kommunikation inte kan säkerställas ska en kvalificerad tolk tillhandahållas. Rätten till tolk vid själva intervjun följer även av [APR artikel 8.3](../interpreters/articles/apr-008.md).

---

## Övriga intervjuer

Utöver de personliga intervjuerna enligt APR förekommer andra samtal och utfrågningar i systemet. Dessa är **inte** personliga intervjuer i APR:s mening och omfattas inte nödvändigtvis av kraven i art. 13–14 (t.ex. inspelningskravet).

| Intervju/samtal | Sammanhang | Källa |
|-----------------|------------|-------|
| Förhandsprövning av efterföljande ansökan | Kan ske skriftligt eller med samtal; filtrerar ansökningar utan nytt underlag | [RULE-APR-055-001](../../domains/asylum-procedure/rules/rule-apr-055-001.md) |
| Frågor under screening | Identifiering och registrering av uppgifter före förfarandet (ej skyddsintervju) | [Screening](../../domains/screening/README.md) |

> Om en av dessa senare formaliseras som en personlig intervju gäller kraven i art. 13–14, inklusive inspelning.

---

## Används av

- [PROC-ASY-001 Pröva en ansökan](../../domains/asylum-procedure/processes/examine-an-application.md)
- [PROC-RES-001 Fastställ ansvarig medlemsstat](../../domains/responsibility/processes/determine-responsible-member-state.md)
- [PROC-BRD-001 Asylgränsförfarande](../../domains/border-procedure/processes/asylum-border-procedure.md)

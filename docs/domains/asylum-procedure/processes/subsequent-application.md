---
tags:
  - efterföljande-ansökan
  - asylförfarande
  - process
---


# PROC-ASY-002

# Efterföljande ansökan

## Trigger

En person lämnar in en ny ansökan om internationellt skydd efter att ett slutligt beslut har fattats om en tidigare ansökan.

---

## Resultat

Ansökan har antingen avvisats som otillåtlig eller tagits upp till prövning i sak.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/subsequent-application.svg" width="100%"></object>

Källa: [`subsequent-application.pu`](../diagrams/subsequent-application.pu)

---

## Alternativt flöde — rätt att stanna

- Vid **första** efterföljande ansökan: sökanden har rätt att stanna.
- Vid **andra eller följande**: undantag kan gälla ([RULE-APR-056-001](../rules/rule-apr-056-001.md)).
- Undantag kräver non-refoulement-kontroll.

---

## Tidsfrister

Alla frister löper **från den dag ansökan lämnades in** (lodged, [art. 28.2](../../registration/articles/apr-028.md)) och stoppas när beslut fattas. Förhandsprövningen har ingen egen dagsfrist — den ryms inom upptagandefristen. Se scenariomatrisen i [konceptet för efterföljande ansökan](../concepts/subsequent-application.md) för hela bilden.

| Tidsfrist | Källa | Kommentar |
|-----------|-------|-----------|
| **Avvisning som ej upptagbar** — 2 månader | [APR art. 35.1 första st.](../articles/apr-035.md) | Vanligaste utfallet: efterföljande ansökan utan nya faktorer nekas enligt art. 38.2 |
| **Återvändandebeslut + sen ansökan (art. 38.1 e)** — 10 arbetsdagar | [APR art. 35.1 andra st.](../articles/apr-035.md) | Kortare specialfrist |
| **Förhandsprövning** — ingen explicit dagsfrist | [APR art. 55.3–4](../articles/apr-055.md) | Ska ske snarast; ryms inom tvåmånadersfristen ovan |
| **Prövning i sak (om nya faktorer)** — 6 månader | [APR art. 35.4](../articles/apr-035.md) | Samma frist som ordinarie ansökningar |
| **Påskyndat förfarande** — 3 månader | [APR art. 35.3 / 42](../articles/apr-042.md) | Om ansökan bedöms uppenbart ogrundad |
| **Gränsförfarande** — 12 veckor | [APR art. 51](../../border-procedure/articles/apr-051.md) | Efterföljande ansökan med enbart fördröjningssyfte kan prövas i gränsförfarande ([art. 43.1 c](../../border-procedure/articles/apr-043.md)) |
| **Förlängning** | [APR art. 35.2 / 35.5](../articles/apr-035.md) | +2 mån (upptagande) / +6 mån (sak) vid massinflöde, komplexitet eller sökandens försummelse |

### Koppling till statistik

| Datapunkt | Betydelse | Källa |
|-----------|-----------|-------|
| Bifallsandel efterföljande ansökningar | Om <20 % → påskyndat förfarande kan tillämpas | EUAA kvartalsdata |
| Andel avvisade som otillåtliga | Mått på hur ofta nya omständigheter saknas | Nationell statistik |
| Tid från inlämning till förhandsprövningsbeslut | Effektivitetsmått | Nationell statistik |

---

## Alternativt flöde — ingen tidigare slutlig dom

Om det inte finns ett slutligt beslut om den tidigare ansökan (ärendet pågår eller är överklagat) ska de nya uppgifterna hanteras inom det pågående förfarandet — inte som en efterföljande ansökan.

---

## Juridiska milstolpar

- Efterföljande ansökan registrerad
- Förhandsprövning genomförd
- Upptagandebeslut (otillåtlig / upptagbar)
- Om upptagbar: prövning i sak → beslut (6 mån / 3 mån påskyndat)

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Person med tidigare slutligt beslut | Förhandsprövning | Nya omständigheter: sakprövning / Inga: avvisas |

---

## Regler

- [RULE-APR-055-001](../rules/rule-apr-055-001.md) — Förhandsprövning
- [RULE-APR-055-002](../rules/rule-apr-055-002.md) — Avvisning vid avsaknad av nya omständigheter
- [RULE-APR-056-001](../rules/rule-apr-056-001.md) — Undantag från rätt att stanna

---

## Delade aktiviteter

- [Fastställ tolkbehov](../../../shared/interpreters/activities/determine-interpreter-needs.md)

---

## Diagram

Se huvudflöde ovan.

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

| Tidsfrist | Källa | Kommentar |
|-----------|-------|-----------|
| **Förhandsprövning** — ingen explicit tidsfrist | APR art. 55 | Ska genomföras "snarast"; underförstått innan prövningstidsfristerna börjar löpa |
| **Prövning i sak (om upptagbar)** — 6 månader | APR art. 35 | Samma tidsfrist som för ordinarie ansökningar |
| **Påskyndat förfarande** — 3 månader | APR art. 42 | Kan tillämpas om ansökan bedöms som uppenbart ogrundad |
| **Gränsförfarande** — 12 veckor | APR art. 51 | Efterföljande ansökan som enbart syftar till att fördröja kan prövas i gränsförfarande (art. 43.1 c) |

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

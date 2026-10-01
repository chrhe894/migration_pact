---
tags:
  - asylförfarande
  - regel
  - flagga
---


# RULE-APR-056-002

## Rättslig grund

[APR artikel 56](../articles/apr-056.md)

---

## Regeltyp

Obligation

---

## Regel

Det ska hållas reda på hur många efterföljande ansökningar en sökande har lämnat in. Nivån — första efterföljande ansökan respektive andra eller följande — avgör om undantag från rätten att stanna kvar kan tillämpas.

---

## Syfte

Säkerställa att rätten att stanna kvar bedöms korrekt, eftersom undantag enligt artikel 56 endast kan gälla vid andra eller följande efterföljande ansökan.

---

## Utlösare

En efterföljande ansökan har markerats ([RULE-APR-055-003](rule-apr-055-003.md)) och nivån ska fastställas.

---

## Rättsverkan

- Vid **första** efterföljande ansökan har sökanden rätt att stanna kvar i avvaktan på beslut.
- Vid **andra eller följande** efterföljande ansökan kan undantag från rätten att stanna gälla ([RULE-APR-056-001](rule-apr-056-001.md)).
- Undantag kan aldrig tillämpas om det finns risk för kränkning av principen om non-refoulement.

---

## Kommentar

Nivåräkningen är en räknarbaserad flagga: antalet tidigare efterföljande ansökningar mäts mot tröskeln "första vs. andra/följande". Den förutsätter att markeringen enligt [RULE-APR-055-003](rule-apr-055-003.md) upprätthålls över tid. Se [shared/flags](../../../shared/flags/README.md).

---

## Relaterade regler

- [RULE-APR-056-001](rule-apr-056-001.md) — Undantag från rätt att stanna
- [RULE-APR-055-003](rule-apr-055-003.md) — Markering som efterföljande ansökan

---

## Status

Complete

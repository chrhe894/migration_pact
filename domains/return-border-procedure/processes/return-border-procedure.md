<div align="right">← <a href="../README.md">Return Border Procedure</a></div>

# PROC-RET-001

# Return border procedure

## Trigger

En ansökan om internationellt skydd har avslagits eller avvisats i asylgränsförfarandet och personen har inte rätt att stanna kvar.

---

## Resultat

Personen har återvänt (frivilligt eller genom avlägsnande) eller tidsfrist löpt ut och inresa tillåtits.

---

## Huvudflöde

1. Avslag i asylgränsförfarande meddelas ([RULE-RET-004-001](../rules/rule-ret-004-001.md)).
2. Återvändandebeslut utfärdas.
3. Tidsfrist för frivillig avresa beviljas (max 15 dagar).
4. Om frivillig avresa inte sker: avlägsnande verkställs.
5. Om avlägsnande inte verkställs inom 12 veckor: personen tillåts resa in ([RULE-RET-005-001](../rules/rule-ret-005-001.md)).

---

## Alternativt flöde — överklagande

Personen överklagar och beviljas suspensiv verkan. Tidsfristerna fryser till dess domstolsprövningen avslutats.

---

## Juridiska milstolpar

- Rejection in border procedure
- Return decision issued
- Voluntary departure period (max 15 days)
- Removal executed / Entry permitted (12 weeks)

---

## Regler

- [RULE-RET-004-001](../rules/rule-ret-004-001.md) — Tillämpning efter avslag
- [RULE-RET-005-001](../rules/rule-ret-005-001.md) — Maximal varaktighet 12 veckor

---

## Diagram

Se `../diagrams/return-border-procedure.pu`

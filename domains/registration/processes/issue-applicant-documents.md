<div align="right">← <a href="../README.md">Registration</a></div>

# PROC-REG-003

# Issue applicant documents

## Trigger

En ansökan om internationellt skydd har registrerats eller lämnats in.

---

## Resultat

Sökanden har tillhandahållits de handlingar som krävs enligt APR artikel 29.

---

## Huvudflöde

1. I samband med registreringen tillhandahålls sökanden en registreringshandling ([RULE-APR-029-001](../rules/rule-apr-029-001.md)).
2. När ansökan lämnas in utfärdas sökandehandlingen ([RULE-APR-029-002](../rules/rule-apr-029-002.md)).
3. Registreringshandlingen återkallas.
4. Sökandehandlingen tillhandahålls sökanden.

---

## Alternativt flöde — direkt utfärdande

Om sökandehandlingen kan utfärdas direkt vid registreringen ska registreringshandlingen inte utfärdas (APR artikel 29.2, se [RULE-APR-029-001](../rules/rule-apr-029-001.md)).

---

## Alternativt flöde — förvar eller fängelsestraff

Om sökanden är i förvar eller avtjänar fängelsestraff behöver handlingarna inte utfärdas. När sökanden friges ska handlingen tillhandahållas (APR artikel 29.5, se [RULE-APR-029-001](../rules/rule-apr-029-001.md)).

---

## Alternativt flöde — medföljande barn

För medföljande barn kan handlingar som utfärdas till förälder eller ansvarig vuxen i tillämpliga fall även omfatta barnet (APR artikel 29.6).

---

## Juridiska milstolpar

- Application registered — registreringshandling utfärdas
- Application lodged — sökandehandling utfärdas

---

## Regler

- [RULE-APR-029-001](../rules/rule-apr-029-001.md) — Registreringshandling
- [RULE-APR-029-002](../rules/rule-apr-029-002.md) — Sökandehandling efter inlämnande
- [RULE-APR-029-003](../rules/rule-apr-029-003.md) — Giltighetstid för sökandehandling

---

## Shared Activities

- (se shared/documents)

---

## Diagram

Se `../diagrams/issue-applicant-documents.pu`
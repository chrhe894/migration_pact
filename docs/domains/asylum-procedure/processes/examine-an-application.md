---
tags:
  - asylförfarande
  - process
---


# PROC-ASY-001

# Pröva en ansökan

## Trigger

En ansökan om internationellt skydd har lämnats in och den ansvariga medlemsstaten ska pröva den.

---

## Resultat

Ett beslut har fattats om ansökan — beviljande av skydd, avslag eller konstaterat återkallande.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/examine-an-application.svg" width="100%"></object>

Källa: [`examine-an-application.pu`](../diagrams/examine-an-application.pu)

---

## Alternativt flöde — påskyndat förfarande

Om grunder enligt artikel 42 föreligger ska förfarandet påskyndas ([RULE-APR-042-001](../rules/rule-apr-042-001.md)). Beslut ska fattas inom tre månader ([RULE-APR-042-002](../rules/rule-apr-042-002.md)).

---

## Alternativt flöde — uttryckligt återkallande

Om sökanden uttryckligen återkallar sin ansökan avbryts prövningen och ett beslut fattas om att ansökan är uttryckligen återkallad.

---

## Alternativt flöde — implicit återkallande

Om sökanden avviker, inte samarbetar eller inte inställer sig till intervju utan giltigt skäl, kan ansökan betraktas som implicit återkallad efter rimliga ansträngningar att kontakta sökanden.

---

## Juridiska milstolpar

- Application lodged (startpunkt)
- Admissibility decision
- Personal interview conducted
- Decision on the merits

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Ansökan inlämnad | Admissibility-prövning | Ansökan tillåtlig eller otillåtlig |
| Ansökan tillåtlig | Prövning i sak | Beslut (beviljat/avslag) |

---

## Regler

- [RULE-APR-034-001](../rules/rule-apr-034-001.md) — Individuell, objektiv, opartisk prövning
- [RULE-APR-034-002](../rules/rule-apr-034-002.md) — Prövning mot flyktingstatus och subsidiärt skydd
- [RULE-APR-035-001](../rules/rule-apr-035-001.md) — Tidsfrist sex månader
- [RULE-APR-035-002](../rules/rule-apr-035-002.md) — Förlängning till 15 månader
- [RULE-APR-038-001](../rules/rule-apr-038-001.md) — Grunder för avvisning
- [RULE-APR-042-001](../rules/rule-apr-042-001.md) — Grunder för påskyndat förfarande
- [RULE-APR-042-002](../rules/rule-apr-042-002.md) — Tidsfrist tre månader (påskyndat)

---

## Shared Activities

- [Verify identity](../../../shared/identity/activities/verify-identity.md)
- [Determine interpreter needs](../../../shared/interpreters/activities/determine-interpreter-needs.md)

---

## Diagram

Se huvudflöde ovan.

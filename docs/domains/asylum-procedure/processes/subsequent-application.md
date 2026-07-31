
# PROC-ASY-002

# Subsequent application

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

## Alternativt flöde — ingen tidigare slutlig dom

Om det inte finns ett slutligt beslut om den tidigare ansökan (ärendet pågår eller är överklagat) ska de nya uppgifterna hanteras inom det pågående förfarandet — inte som en efterföljande ansökan.

---

## Juridiska milstolpar

- Subsequent application registered
- Preliminary examination completed
- Admissibility decision (inadmissible / admissible)
- If admissible: examination on the merits → decision

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

## Shared Activities

- [Determine interpreter needs](../../../shared/interpreters/activities/determine-interpreter-needs.md)

---

## Diagram

Se huvudflöde ovan.

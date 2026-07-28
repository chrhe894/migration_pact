<div align="right">← <a href="../README.md">Responsibility</a></div>

# PROC-RES-001

# Determine responsible Member State

## Trigger

En ansökan om internationellt skydd har registrerats och ansvarig medlemsstat ska fastställas.

---

## Resultat

Ansvarig medlemsstat har fastställts och sökanden kan hänvisas till rätt stat för prövning.

---

## Huvudflöde

1. Ansökan registreras ([RULE-APR-027-001](../../registration/rules/rule-apr-027-001.md)).
2. Situationen vid registreringstidpunkten fastställs ([RULE-AMMR-024-002](../rules/rule-ammr-024-002.md)).
3. Kriterierna tillämpas i angiven ordning ([RULE-AMMR-024-001](../rules/rule-ammr-024-001.md)):
   - a) Ensamkommande barn? → [RULE-AMMR-025-001](../rules/rule-ammr-025-001.md)
   - b) Familjemedlem lagligen bosatt? → AMMR art. 26
   - c) Familjemedlem med pågående ansökan? → AMMR art. 27
   - d) Familjeförfarande? → AMMR art. 28
   - e) Uppehållshandling eller visering? → [RULE-AMMR-029-001](../rules/rule-ammr-029-001.md)
   - f) Examensbevis? → AMMR art. 30
   - g) Viseringsfri inresa? → AMMR art. 31
   - h) Transitzon på flygplats? → AMMR art. 32
   - i) Irreguljär inresa? → [RULE-AMMR-033-001](../rules/rule-ammr-033-001.md)
4. Om inget kriterium ger en ansvarig stat: den stat där ansökan först registrerades.
5. Ansvarig stat fastställs.
6. Om ansvarsstaten är en annan stat: framställan om övertagande (take charge request) skickas.

---

## Alternativt flöde — diskretionär bedömning

Medlemsstaten får besluta att överta prövningsansvaret av humanitära skäl oavsett kriterierna ([RULE-AMMR-035-001](../rules/rule-ammr-035-001.md)).

---

## Alternativt flöde — ansvarets upphörande

Om tidsfristerna i artikel 33 har löpt ut (20 resp. 12 månader) kan inresestaten inte längre hållas ansvarig ([RULE-AMMR-033-002](../rules/rule-ammr-033-002.md)).

---

## Juridiska milstolpar

- Application registered (referenspunkt)
- Responsible Member State determined
- Take charge request sent (om annan stat)
- Transfer decision (om annan stat)

---

## Regler

- [RULE-AMMR-024-001](../rules/rule-ammr-024-001.md) — Kriterierna i angiven ordning
- [RULE-AMMR-024-002](../rules/rule-ammr-024-002.md) — Situationen vid första registrering
- [RULE-AMMR-025-001](../rules/rule-ammr-025-001.md) — Ensamkommande barn
- [RULE-AMMR-029-001](../rules/rule-ammr-029-001.md) — Uppehållshandling eller visering
- [RULE-AMMR-033-001](../rules/rule-ammr-033-001.md) — Första irreguljära inresa
- [RULE-AMMR-033-002](../rules/rule-ammr-033-002.md) — Tidsbegränsning
- [RULE-AMMR-035-001](../rules/rule-ammr-035-001.md) — Diskretionär bedömning

---

## Shared Activities

- [Verify identity](../../../shared/identity/activities/verify-identity.md)

---

## Diagram

Se `../diagrams/determine-responsible-member-state.pu`

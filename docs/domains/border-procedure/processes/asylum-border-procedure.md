
# PROC-BRD-001

# Asylum border procedure

## Trigger

Screening avslutad och sökanden uppfyller villkoren för gränsförfarande (artikel 43) eller gränsförfarandet är obligatoriskt (artikel 45).

---

## Resultat

Beslut fattat — beviljande, avslag eller undantag med inresa.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/asylum-border-procedure.svg" width="100%"></object>

Källa: [`asylum-border-procedure.pu`](../diagrams/asylum-border-procedure.pu)

---

## Alternativt flöde — undantag (art. 53)

Om sökanden har särskilda behov som inte kan tillgodoses, är ensamkommande barn (ej säkerhetshot), eller behöver medicinsk vård: gränsförfarandet avbryts, sökanden tillåts resa in, reguljärt förfarande tar vid ([RULE-APR-053-001](../rules/rule-apr-053-001.md)).

---

## Alternativt flöde — kapacitet uppnådd

Om statens kapacitet uppnåtts: obligatorisk tillämpning av vissa grunder upphör, reguljärt förfarande tar vid.

---

## Alternativt flöde — 12 veckor passerar utan beslut

Sökanden tillåts resa in. Ärendet övergår till reguljärt förfarande.

---

## Juridiska milstolpar

- Application registered
- Border procedure initiated (ingen inresa)
- Application lodged (5 dagar)
- Decision (inom 12 veckor)
- Entry permitted / Return border procedure initiated

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Sökande efter screening, vid gränsen | Gränsförfarande (12 veckor) | Beviljat: inresa / Avslag: return border procedure |

---

## Regler

- [RULE-APR-043-001](../rules/rule-apr-043-001.md) — Villkor för tillämpning
- [RULE-APR-043-002](../rules/rule-apr-043-002.md) — Inresa nekas
- [RULE-APR-045-001](../rules/rule-apr-045-001.md) — Obligatorisk tillämpning
- [RULE-APR-051-001](../rules/rule-apr-051-001.md) — Inlämnande inom 5 dagar
- [RULE-APR-051-002](../rules/rule-apr-051-002.md) — Maximal varaktighet 12 veckor
- [RULE-APR-053-001](../rules/rule-apr-053-001.md) — Undantag för sårbara

---

## Shared Activities

- [Verify identity](../../../shared/identity/activities/verify-identity.md)
- [Determine interpreter needs](../../../shared/interpreters/activities/determine-interpreter-needs.md)

---

## Diagram

Se huvudflöde ovan.

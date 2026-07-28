<div align="right">← <a href="../README.md">Eurodac</a></div>

# PROC-EUR-001

# Collect and transmit biometric data

## Trigger

En person omfattas av en Eurodac-kategori där biometriska uppgifter ska tas, exempelvis:

- en person som ansöker om internationellt skydd,
- en person som vistas olagligt inom en medlemsstats territorium.

---

## Resultat

Biometriska uppgifter och tillhörande dataset har tagits, överförts till Eurodac och omfattas av tillämplig lagringsperiod.

---

## Huvudflöde

1. Behörig myndighet konstaterar att personen omfattas av en Eurodac-kategori.
2. Personen informeras om skyldigheten att lämna biometriska uppgifter ([RULE-EUR-013-001](../rules/rule-eur-013-001.md)).
3. Biometriska uppgifter tas med respekt för personens värdighet och fysiska integritet ([RULE-EUR-013-002](../rules/rule-eur-013-002.md)).
4. Om personen är underårig tillämpas särskilda garantier ([RULE-EUR-014-001](../rules/rule-eur-014-001.md)).
5. Dataset sammanställs med biometriska och relevanta alfanumeriska uppgifter.
6. Dataset överförs till Eurodac inom tillämplig tidsfrist:
   - asylsökande: [RULE-EUR-015-001](../rules/rule-eur-015-001.md),
   - person som vistas olagligt: [RULE-EUR-023-001](../rules/rule-eur-023-001.md).
7. Dataset lagras enligt tillämplig lagringsregel:
   - asylsökande: [RULE-EUR-029-001](../rules/rule-eur-029-001.md),
   - person som vistas olagligt: [RULE-EUR-029-002](../rules/rule-eur-029-002.md).

---

## Alternativt flöde — hälsorelaterat hinder

Om biometriska uppgifter för en asylsökande inte kan tas på grund av hälsorelaterade hinder ska uppgifterna tas och överföras så snart som möjligt och senast 48 timmar efter att hindren undanröjts.

---

## Alternativt flöde — tekniskt problem

Vid allvarliga tekniska problem får 72-timmarsfristen för asylsökande förlängas med högst 48 timmar.

---

## Juridiska milstolpar

- Biometriska uppgifter tas
- Dataset överförs till Eurodac
- Dataset registreras
- Dataset lagras

---

## Regler

- [RULE-EUR-013-001](../rules/rule-eur-013-001.md) — Skyldighet att ta och lämna biometriska uppgifter
- [RULE-EUR-013-002](../rules/rule-eur-013-002.md) — Respekt för värdighet och fysisk integritet
- [RULE-EUR-014-001](../rules/rule-eur-014-001.md) — Underåriga
- [RULE-EUR-015-001](../rules/rule-eur-015-001.md) — Asylsökande
- [RULE-EUR-023-001](../rules/rule-eur-023-001.md) — Personer som vistas olagligt
- [RULE-EUR-029-001](../rules/rule-eur-029-001.md) — Lagringstid för asylsökande
- [RULE-EUR-029-002](../rules/rule-eur-029-002.md) — Lagringstid för personer som vistas olagligt

---

## Shared Activities

- [Verify identity](../../../shared/identity/activities/verify-identity.md)

---

## Diagram

Se `../diagrams/collect-and-transmit-biometric-data.pu`

<div align="right">← <a href="../README.md">Screening</a></div>

# PROC-SCR-001

# Screening vid yttre gräns

## Trigger

En tredjelandsmedborgare omhändertas vid otillåten gränspassage, landsätts efter sök- och räddningsinsats, eller gör en asylansökan vid ett gränsövergångsställe utan att uppfylla inresevillkoren.

---

## Resultat

Personen har genomgått screening och hänvisats till rätt förfarande med screeningformuläret som underlag.

---

## Huvudflöde

1. Person omhändertas, landsätts eller ansöker om asyl vid yttre gräns ([RULE-SCR-005-001](../rules/rule-scr-005-001.md), [RULE-SCR-005-002](../rules/rule-scr-005-002.md)).
2. Inresa nekas under pågående screening.
3. Preliminär hälsokontroll genomförs av medicinsk personal.
4. Preliminär sårbarhetskontroll genomförs av specialiserad personal.
5. Identitet fastställs eller verifieras ([RULE-SCR-014-001](../rules/rule-scr-014-001.md)).
6. Biometriska uppgifter registreras i Eurodac om ej redan skett.
7. Säkerhetskontroll genomförs mot EU-databaser ([RULE-SCR-015-001](../rules/rule-scr-015-001.md)).
8. Screeningformulär fylls i ([RULE-SCR-017-001](../rules/rule-scr-017-001.md)).
9. Screening avslutas och personen hänvisas till rätt förfarande ([RULE-SCR-018-001](../rules/rule-scr-018-001.md)).

---

## Alternativt flöde — massinflöde/förkortad period

Om personen befunnit sig vid yttre gränsen i mer än 72 timmar förkortas screeningperioden till fyra dagar ([RULE-SCR-008-001](../rules/rule-scr-008-001.md)).

---

## Alternativt flöde — tidsfrist löper ut

Om inte alla kontroller slutförts inom sju dagar ska screeningen ändå avslutas och personen hänvisas till lämpligt förfarande.

---

## Alternativt flöde — inresevillkor uppfylls

Om det under screeningen framkommer att personen uppfyller inresevillkoren ska screeningen avslutas.

---

## Juridiska milstolpar

- Screening inledd
- Screening avslutad
- Hänvisning till förfarande

---

## Regler

- [RULE-SCR-005-001](../rules/rule-scr-005-001.md) — Screening obligatorisk vid gränspassage
- [RULE-SCR-005-002](../rules/rule-scr-005-002.md) — Screening av asylsökande vid gränsövergångsställen
- [RULE-SCR-008-001](../rules/rule-scr-008-001.md) — Tidsfrist sju dagar
- [RULE-SCR-008-003](../rules/rule-scr-008-003.md) — Obligatoriska delar
- [RULE-SCR-014-001](../rules/rule-scr-014-001.md) — Identifiering
- [RULE-SCR-015-001](../rules/rule-scr-015-001.md) — Säkerhetskontroll
- [RULE-SCR-017-001](../rules/rule-scr-017-001.md) — Screeningformulär
- [RULE-SCR-018-001](../rules/rule-scr-018-001.md) — Hänvisning

---

## Shared Activities

- [Verify identity](../../../shared/identity/activities/verify-identity.md)
- [Determine interpreter needs](../../../shared/interpreters/activities/determine-interpreter-needs.md)

---

## Diagram

Se `../diagrams/screening-at-external-border.pu`

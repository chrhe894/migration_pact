# Delat — Biometri

## Syfte

Denna shared-modul dokumenterar regler och begrepp kring insamling, lagring och användning av biometriska uppgifter (fingeravtryck och ansiktsbild) som är gemensamma för flera domäner.

Biometriska uppgifter är centrala för hela systemet — de möjliggör identifiering, ansvarsbestämning och säkerhetskontroller.

---

## Primära rättskällor

- [Eurodacförordningen artikel 13](../../domains/eurodac/articles/eur-013.md) — Skyldighet att ta biometriska uppgifter
- [Eurodacförordningen artikel 14](../../domains/eurodac/articles/eur-014.md) — Särskilda bestämmelser för underåriga
- [Eurodacförordningen artikel 15](../../domains/eurodac/articles/eur-015.md) — Insamling och överföring för asylsökande
- [Eurodacförordningen artikel 18](../../domains/eurodac/articles/eur-018.md) — Sök- och räddningsinsatser
- [Eurodacförordningen artikel 21](../../domains/eurodac/articles/eur-021.md) — Irreguljär gränspassage
- [Screeningförordningen artikel 14](../../domains/screening/articles/scr-014.md) — Identifiering med biometriska uppgifter
- [Screeningförordningen artikel 8](../../domains/screening/articles/scr-008.md), punkt 5 d — Registrering av biometriska uppgifter som del av screening

---

## Begrepp

- [Biometriska uppgifter (CON-EUR-002)](../../domains/eurodac/concepts/biometric-data.md) — Samlingsbegrepp: fingeravtryck + ansiktsbild
- [Fingeravtryck (CON-EUR-003)](../../domains/eurodac/concepts/fingerprint-data.md) — Tio fingeravtryck (platta avtryck)
- [Ansiktsbild (CON-EUR-004)](../../domains/eurodac/concepts/facial-image-data.md) — Ansiktsbild av tillräcklig kvalitet

---

## Regler

| Regel | Beskrivning |
|-------|-------------|
| [RULE-EUR-013-001](../../domains/eurodac/rules/rule-eur-013-001.md) | Skyldighet att ta biometriska uppgifter |
| [RULE-EUR-013-002](../../domains/eurodac/rules/rule-eur-013-002.md) | Respekt för värdighet och fysisk integritet |
| [RULE-EUR-014-001](../../domains/eurodac/rules/rule-eur-014-001.md) | Biometriska uppgifter för underåriga från sex år |
| [RULE-EUR-015-001](../../domains/eurodac/rules/rule-eur-015-001.md) | Insamling och överföring för asylsökande (72h) |
| [RULE-EUR-018-001](../../domains/eurodac/rules/rule-eur-018-001.md) | Tidsfrist vid landsättning (72h) |
| [RULE-EUR-021-001](../../domains/eurodac/rules/rule-eur-021-001.md) | Registrering vid irreguljär gränspassage |
| [RULE-EUR-038-001](../../domains/eurodac/rules/rule-eur-038-001.md) | Kvalitetskrav för biometriska uppgifter |
| [RULE-SCR-014-001](../../domains/screening/rules/rule-scr-014-001.md) | Identifiering med biometriska uppgifter under screening |

---

## Personkategorier

Biometriska uppgifter ska tas för följande kategorier (från 6 års ålder):

| Kategori | Artikel | Tidsfrist |
|----------|---------|-----------|
| Asylsökande | Eurodac art. 15 | 72 timmar |
| Sök- och räddning | Eurodac art. 18 | 72 timmar |
| Omplacerade | Eurodac art. 19 | Snarast efter omplacering |
| Vidarebosatta | Eurodac art. 20 | 72 timmar |
| Irreguljär gränspassage | Eurodac art. 21 | 72 timmar |
| Återkallat uppehållstillstånd | Eurodac art. 22 | Tillämplig tidsfrist |
| Olaglig vistelse | Eurodac art. 23 | Snarast möjligt |

---

## Koppling till ansvarsbestämning

Biometrisk registrering i Eurodac kan utlösa ansvarsförfarande:
- En träff mot ett redan registrerat dataset kan identifiera vilken stat som är ansvarig (AMMR art. 33 — irreguljär inresa).
- Brottsbekämpande jämförelse är möjlig under strikta villkor (Eurodac art. 32).

---

## Används av

- [PROC-SCR-001 Screening vid yttre gräns](../../domains/screening/processes/screening-at-external-border.md)
- [PROC-SCR-002 Screening inom territoriet](../../domains/screening/processes/screening-within-territory.md)
- [PROC-EUR-001 Samla in och överföra biometriska uppgifter](../../domains/eurodac/processes/collect-and-transmit-biometric-data.md)
- [PROC-REG-001 Registrering av en ansökan](../../domains/registration/processes/registration-of-an-application.md)
- [PROC-RES-001 Fastställ ansvarig medlemsstat](../../domains/responsibility/processes/determine-responsible-member-state.md)

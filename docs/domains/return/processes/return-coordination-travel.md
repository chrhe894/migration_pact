---
tags:
  - återvändande
  - återvändandesamordning
  - resa
  - återvändandeinsats
  - process
---

# PROC-RTN-005

# Återvändandesamordning – resa

Delprocess till [PROC-RTN-001 Återvändandeförfarande](return-procedure.md), steg 10. Gäller **avlägsnande** (verkställighet med eller utan tvång). Frivilligt återvändande med stöd beskrivs i [PROC-RTN-006](assisted-voluntary-return.md).

## Trigger

Beslutet om återvändande är verkställbart, personen har en giltig resehandling ([PROC-RTN-004](return-coordination-embassy.md)), och tidsfristen för frivillig avresa har löpt ut eller saknas.

---

## Resultat

Personen har överlämnats till myndigheterna i destinationslandet och avresedatumet är registrerat. Alternativt har insatsen avbrutits eller misslyckats och ett nytt försök planeras.

---

## Ansvar

Den verkställande myndigheten enligt [RULE-UTL-12-014-001](../rules/rule-utl-12-014-001.md). Vid gemensamma flygningar: den nationella myndighet som utsetts enligt beslut 2004/573/EG art. 3.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/return-coordination-travel.svg" width="100%"></object>

Källa: [`return-coordination-travel.pu`](../diagrams/return-coordination-travel.pu)

---

## Steg

| # | Steg | Regler | Gäller |
|---|------|--------|--------|
| 1 | Verkställ **snarast möjligt** efter att tidsfristen löpt ut, eller direkt om beslutet saknar tidsfrist | [RULE-UTL-12-015-001](../rules/rule-utl-12-015-001.md) | Nu |
| 2 | Kontrollera hinder: uppskjutande, inhibition, non-refoulement. Kontrollera SIS före återvändandet | [RULE-RR-011-001](../rules/rule-rr-011-001.md), [RULE-RR-010-003](../rules/rule-rr-010-003.md), [RULE-FRX-050-001](../rules/rule-frx-050-001.md) | RR: 17 okt 2027; Frontex: nu |
| 3 | Ensamkommande barn: försäkra dig om att barnet tas emot i återvändandelandet | [RULE-RR-017-002](../rules/rule-rr-017-002.md) | 17 okt 2027 |
| 4 | Hälsa: flygduglighet, sjukjournal vid kända hälsoproblem, uppgifter om medicinskt stöd | [RULE-JRF-007-001](../rules/rule-jrf-007-001.md), [RULE-RR-039-001](../rules/rule-rr-039-001.md) | Riktlinjer: nu; RR: 17 okt 2027 |
| 5 | Välj transport: **reguljärt flyg**, **nationell charter**, **gemensam flygning** (organisera eller delta) eller **Frontex-insats** | [RULE-JRF-004-001](../rules/rule-jrf-004-001.md), [RULE-JRF-005-001](../rules/rule-jrf-005-001.md), [RULE-FRX-050-001](../rules/rule-frx-050-001.md) | Nu |
| 6 | Handlingar och viseringar för den återvändande och ledsagarna. Tillstånd från transit- och destinationsländer. Informera egna beskickningar | [RULE-JRF-006-001](../rules/rule-jrf-006-001.md), [RULE-JRF-004-001](../rules/rule-jrf-004-001.md) | Nu |
| 7 | Underrätta flygbolag, transitländer och destinationsland **i god tid**. Överför nödvändiga uppgifter till flygbolag | [RULE-JRF-007-001](../rules/rule-jrf-007-001.md), [RULE-RR-037-001](../rules/rule-rr-037-001.md) | Riktlinjer: nu; RR: 17 okt 2027 |
| 8 | Transit via annan medlemsstat | [RULE-RR-042-001](../rules/rule-rr-042-001.md) (direktiv 2003/110/EG, finns inte i repot) | 17 okt 2027 |
| 9 | **Ledsagare:** antal efter riskanalys, bör minst motsvara antalet återvändande. Minst två företrädare vid deltagande i annan stats flygning | [RULE-JRF-007-001](../rules/rule-jrf-007-001.md), [RULE-JRF-005-001](../rules/rule-jrf-005-001.md) | Nu |
| 10 | Förvar fram till avresan om det behövs | [PROC-RTN-002](return-detention.md), [RULE-RR-030-004](../rules/rule-rr-030-004.md) | 17 okt 2027 |
| 11 | **Avresedag:** på flygplatsen minst tre timmar före avgång, säkerhetskontroll, proportionerligt tvång, inga lugnande medel, läkare vid gemensam flygning, övervakning | [RULE-JRF-007-001](../rules/rule-jrf-007-001.md), [RULE-RR-010-004](../rules/rule-rr-010-004.md), [RULE-RR-012-001](../rules/rule-rr-012-001.md) | Riktlinjer: nu; RR: 17 okt 2027 |
| 12 | **Ankomst:** överlämnande utan handbojor eller andra tvångsmedel | [RULE-JRF-007-001](../rules/rule-jrf-007-001.md) | Nu |
| 13 | **Registrera avresedatum:** beslutet är verkställt, inreseförbudet börjar löpa | [RULE-UTL-12-021-001](../rules/rule-utl-12-021-001.md), [RULE-RR-008-007](../rules/rule-rr-008-007.md) | UtlL: nu; RR: 17 okt 2027 |
| 14 | **Misslyckad insats:** varje stat ansvarar för återresan för sina återvändande. Nytt försök planeras | [RULE-JRF-007-001](../rules/rule-jrf-007-001.md) | Nu |

---

## Tidsfrister och tidsgränser

| Vad | Längd eller tidpunkt | Regel |
|-----|----------------------|-------|
| Verkställighet | Snarast möjligt efter att avresefristen löpt ut | [RULE-UTL-12-015-001](../rules/rule-utl-12-015-001.md) |
| Verkställighet mot EES-medborgare | Tidigast fyra veckor efter delgivning, om inte synnerliga skäl finns | [RULE-UTL-12-015-001](../rules/rule-utl-12-015-001.md) |
| Ankomst till flygplatsen | Minst tre timmar före avgång (gemensam flygning, riktlinjerna 2.1 a) | [RULE-JRF-007-001](../rules/rule-jrf-007-001.md) |
| Underrättelse till flygbolag, transit- och destinationsland | I god tid (ingen siffra) | [RULE-JRF-007-001](../rules/rule-jrf-007-001.md) |
| Frontex beslut om operativ plan vid snabb återvändandeintervention | Inom fem arbetsdagar | [RULE-FRX-053-001](../rules/rule-frx-053-001.md) |
| Beslutets giltighet efter avresa | Upphör fem år efter att personen lämnat landet, eller när ett pågående återreseförbud löper ut | [RULE-UTL-12-021-001](../rules/rule-utl-12-021-001.md) |
| Inreseförbud | Löper från avresedagen | [RULE-RR-008-007](../rules/rule-rr-008-007.md) |

---

## Att observera

- Riktlinjerna i beslut 2004/573/EG är skrivna för **gemensamma flygningar**. Förordning 2026/2280 art. 10.10 gör att de ska beaktas vid **alla avlägsnanden med flyg** från 17 oktober 2027.
- Repo-kopian av Frontexförordningen är grundtexten från 2019. Senare ändringar är inte kontrollerade.

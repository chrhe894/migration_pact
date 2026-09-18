# Del 2 – Genomförande

> Status: arbetsutkast  
> Syfte med dokumentet: krav- och utvecklingsunderlag för genomförandet av redan bokade intervjuer.

## AI-instruktioner

Du arbetar med **Del 2 – Genomförande**.

1. Utgå från genomförandepaketet från Del 1.
2. Del 2 ska inte återskapa bokningslogik.
3. Del 2 ska inte behöva känna till hur tider, resurser, personal, stödpersoner eller tolk hittades.
4. Gruppnummer, ärendetyp och intervjutyp ska följa med genom hela genomförandet.
5. Användaren ska uppleva flödet som en sammanhållen process även om flera separata Zoom-möten används bakom kulisserna.
6. Varje intervju kan ha ett eget Zoom Meeting ID.
7. När användaren går vidare från en intervju ska den aktuella Zoom-mötesinstansen avslutas enligt definierad process och nästa intervju aktiveras.
8. Exakta Zoom-API-anrop ska kapslas bakom en tydlig integrationsyta.
9. Ändringar i kontraktet mot Del 1 ska dokumenteras.
10. Del 2 ska kunna utvecklas och testas med ett simulerat genomförandepaket utan att Del 1 behöver vara aktivt.

## Krav

| ID | Krav | Prioritet | Status | Kommentar |
|---|---|---|---|---|
| G-001 | Applikationen ska kunna läsa ett genomförandepaket. | MUST | Öppet | |
| G-002 | Gruppnummer ska visas i genomförandevyn. | MUST | Öppet | |
| G-003 | Ärendetyp ska visas i genomförandevyn. | MUST | Öppet | Exempelvärde FS. |
| G-004 | Intervjutyp ska visas i genomförandevyn. | MUST | Öppet | Exempel Sakintervju. |
| G-005 | Aktuell individ ska visas tydligt. | MUST | Öppet | |
| G-006 | Eventuell stödperson ska visas när relevant. | MUST | Öppet | |
| G-007 | Eventuell tolk ska visas när relevant. | MUST | Öppet | |
| G-008 | Applikationen ska visa vilken intervju i ordningen som pågår. | MUST | Öppet | Exempel 3 av 4. |
| G-009 | Applikationen ska kunna öppna eller ansluta till rätt Zoom-möte. | MUST | Öppet | Exakt UX fastställs. |
| G-010 | Inspelningsstatus ska kunna visas. | MUST | Öppet | |
| G-011 | Användaren ska kunna avsluta aktuell intervju och gå vidare. | MUST | Öppet | Primär användaråtgärd. |
| G-012 | Aktuellt Zoom-möte ska avslutas enligt definierad process. | MUST | Öppet | |
| G-013 | Nästa intervju ska kunna laddas utan att användaren behöver hantera Meeting ID manuellt. | MUST | Öppet | |
| G-014 | Varje intervju ska kopplas till rätt Zoom Meeting ID. | MUST | Öppet | |
| G-015 | Intervjuernas ordning ska vara spårbar. | MUST | Öppet | |
| G-016 | Fel i Zoom-integrationen ska visas begripligt för användaren. | MUST | Öppet | |
| G-017 | Del 2 ska kunna återuppta ett avbrutet genomförande. | SHOULD | Öppet | Verksamhetsregel behöver definieras. |
| G-018 | Del 2 ska logga viktiga händelser. | SHOULD | Öppet | |

## Föreslaget användargränssnitt

```text
┌─────────────────────────────────────────────┐
│ Gruppnummer: 20260012                       │
│ Ärendetyp: FS       Intervjutyp: Sakintervju│
├─────────────────────────────────────────────┤
│                                             │
│ Intervju 3 av 4                             │
│                                             │
│ Lisa Andersson                              │
│ 11 år · Barn                                │
│ Vårdnadshavare: Anna Andersson              │
│                                             │
│ Zoom-möte: AKTIVT                           │
│ Inspelning: AKTIV                           │
│                                             │
│           [ Avsluta och gå till nästa ]     │
└─────────────────────────────────────────────┘
```

Målet är inte att återskapa Zooms hela användargränssnitt.

## Tillståndsmodell

Preliminärt:

```text
PLANNED
   ↓
READY
   ↓
ACTIVE
   ↓
ENDING
   ↓
RECORDING_PROCESSING
   ↓
COMPLETED
```

Fel kan inträffa i flera steg:

```text
ACTIVE
  ↓
ERROR
```

Tillståndsmodellen ska förfinas när Zooms faktiska händelser och API-beteende verifierats.

## Gränssnitt mot Del 1

Del 2 förväntar sig minst:

- kontraktsversion,
- gruppnummer,
- ärendetyp,
- intervjutyp,
- lista över intervjuer,
- ordning,
- personidentifierare,
- visningsinformation,
- stödpersoner där relevant,
- tolk där relevant,
- planerad tid,
- lokal där relevant,
- intervjuare,
- Zoom Meeting ID,
- Zoom Join URL eller motsvarande anslutningsinformation.

## Krav på gränssnittet mot Del 3

| ID | Krav | Prioritet |
|---|---|---|
| G-020 | Inspelningen ska kunna kopplas till gruppnummer. | MUST |
| G-021 | Inspelningen ska kunna kopplas till intervju/individ. | MUST |
| G-022 | Zoom Meeting ID ska kunna kopplas till inspelningen. | MUST |
| G-023 | Tidsinformation ska kunna användas för spårbarhet. | SHOULD |
| G-024 | Del 3 ska kunna hitta rätt metadata utan att tolka hela användargränssnittet. | MUST |

## Öppna frågor

| ID | Fråga | Status | Kommentar |
|---|---|---|---|
| G-Q01 | Ska användaren klicka `Starta` först och sedan `Nästa`, eller räcker ett aktivt genomförandeflöde? | Öppen | |
| G-Q02 | Ska Zoom-klienten öppnas separat eller bäddas in? | Öppen | |
| G-Q03 | Vad händer om användaren av misstag stänger Zoom? | Öppen | |
| G-Q04 | Vad händer om inspelningen inte startat? | Öppen | |
| G-Q05 | Vad händer om användaren trycker `Nästa` innan inspelningen är klar? | Öppen | |
| G-Q06 | Ska nästa intervju kunna startas innan föregående inspelning är färdigbehandlad? | Öppen | |
| G-Q07 | Ska användaren kunna gå tillbaka? | Öppen | |
| G-Q08 | Vad händer om en intervju måste göras om? | Öppen | |
| G-Q09 | Hur hanteras frånvaro? | Öppen | |
| G-Q10 | Hur hanteras en grupp där bara vissa individer ska intervjuas? | Öppen | |
| G-Q11 | Hur hanteras stödperson/tolk som deltar i flera intervjuer? | Öppen | |

## Acceptanskriterier – första version

| ID | Acceptanskriterium | Status |
|---|---|---|
| G-A01 | Del 2 kan startas med ett statiskt testpaket. | Öppet |
| G-A02 | Rätt gruppinformation visas. | Öppet |
| G-A03 | Rätt individ och intervjuordning visas. | Öppet |
| G-A04 | Rätt Zoom-möte används. | Öppet |
| G-A05 | Användaren behöver inte själv hantera Meeting ID. | Öppet |
| G-A06 | `Nästa`/avslut avslutar aktuell intervju enligt definierad process. | Öppet |
| G-A07 | Nästa intervju kan aktiveras. | Öppet |
| G-A08 | Händelser loggas så att varje intervju kan följas. | Öppet |
| G-A09 | Ett tydligt underlag finns för Del 3. | Öppet |

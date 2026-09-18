# Del 3 – Efterarbete

> Status: arbetsutkast  
> Syfte med dokumentet: minimal första integrationsyta för inspelningar och framtida koppling till verksamhetssystem.

## AI-instruktioner

Du arbetar med **Del 3 – Efterarbete**.

1. Håll första versionen minimal.
2. Utgå från metadata och identifierare som producerats i Del 1 och Del 2.
3. Försök inte lösa hela integrationen mot verksamhetssystemet i första versionen.
4. Separera mottagning av Zoom-inspelning från framtida verksamhetsintegration.
5. Varje inspelning ska kunna kopplas till rätt intervju och individ.
6. Använd händelsebaserad kommunikation där det är lämpligt.
7. Fel och återförsök ska vara spårbara.
8. Externa system ska kapslas bakom tydliga integrationsgränser.
9. Gör inte antaganden om verksamhetssystemets API innan det är specificerat.
10. Dokumentera öppna frågor istället för att fylla dem med antaganden.

## Krav

| ID | Krav | Prioritet | Status | Kommentar |
|---|---|---|---|---|
| E-001 | Del 3 ska kunna ta emot information om att en Zoom-inspelning är färdig. | MUST | Öppet | Exakt Zoom-händelse ska verifieras. |
| E-002 | Del 3 ska kunna identifiera rätt Zoom-möte. | MUST | Öppet | |
| E-003 | Del 3 ska kunna koppla inspelningen till rätt intervju. | MUST | Öppet | |
| E-004 | Del 3 ska kunna hämta relevant ljudfil. | MUST | Öppet | |
| E-005 | Del 3 ska kunna visa status för inspelningen. | MUST | Öppet | |
| E-006 | Del 3 ska kunna rapportera fel. | MUST | Öppet | |
| E-007 | Del 3 ska ha stöd för återförsök vid tillfälliga integrationsfel. | SHOULD | Öppet | |
| E-008 | Del 3 ska kunna lämna ett definierat integrationsunderlag till verksamhetssystemet. | SHOULD | Öppet | Första versionen kan vara en mock/stub. |
| E-009 | Viktiga händelser ska loggas. | SHOULD | Öppet | |
| E-010 | Processen ska vara idempotent så att samma inspelning inte importeras flera gånger av misstag. | SHOULD | Öppet | |

## Minimal process

```text
Zoom
  |
  | recording completed
  v
Efterarbete
  |
  | hämta metadata
  v
Identifiera intervju
  |
  | hämta ljud
  v
Ljudfil + metadata
  |
  v
[ framtida verksamhetssystem ]
```

Första versionen behöver inte automatisera hela sista steget.

## Data som bör följa med

| ID | Data | Prioritet | Kommentar |
|---|---|---|---|
| E-D01 | Gruppnummer | MUST | |
| E-D02 | Ärendetyp | MUST | Exempelvärde FS. |
| E-D03 | Intervjutyp | MUST | Exempelvärde Sakintervju. |
| E-D04 | Intervjuidentifierare | MUST | |
| E-D05 | Individidentifierare | MUST | |
| E-D06 | Zoom Meeting ID | MUST | |
| E-D07 | Tidsinformation | SHOULD | |
| E-D08 | Inspelningsidentifierare | MUST | |
| E-D09 | Filtyp | SHOULD | |
| E-D10 | Filstorlek | SHOULD | |
| E-D11 | Status | MUST | |
| E-D12 | Felinformation | SHOULD | |

## Statusmodell

Preliminärt:

```text
EXPECTED
   ↓
RECORDING_AVAILABLE
   ↓
DOWNLOADING
   ↓
IDENTIFIED
   ↓
READY_FOR_IMPORT
   ↓
IMPORTED
```

Fel:

```text
ANY STATE
   ↓
ERROR
   ↓
RETRY / MANUAL_ACTION
```

Den slutliga statusmodellen ska tas fram tillsammans med verksamheten.

## Framtida verksamhetsintegration

Verksamhetssystemet ska betraktas som en separat integrationspart.

Preliminär arkitektur:

```text
Zoom
  |
  v
Efterarbete
  |
  v
Integrationsadapter
  |
  v
Verksamhetssystem
```

Detta gör att framtida utveckling kan göras utan att ändra den grundläggande logiken för mottagning och identifiering av Zoom-inspelningar.

## Öppna frågor

| ID | Fråga | Status | Kommentar |
|---|---|---|---|
| E-Q01 | Vilken Zoom-händelse ska vara startpunkt? | Öppen | |
| E-Q02 | Vilka inspelningsformat ska stödjas? | Öppen | |
| E-Q03 | Ska bara ljud hämtas eller även video? | Öppen | |
| E-Q04 | Var ska temporära filer lagras? | Öppen | |
| E-Q05 | Hur länge ska filer finnas kvar? | Öppen | |
| E-Q06 | Hur identifieras rätt individ/intervju? | Öppen | |
| E-Q07 | Vilken metadata kräver verksamhetssystemet? | Öppen | |
| E-Q08 | Finns ett API mot verksamhetssystemet? | Öppen | |
| E-Q09 | Ska importen vara automatisk eller kräva användarbekräftelse? | Öppen | |
| E-Q10 | Hur ska dubbletter hanteras? | Öppen | |
| E-Q11 | Hur ska felaktiga inspelningar hanteras? | Öppen | |
| E-Q12 | Vilka behörigheter krävs? | Öppen | |
| E-Q13 | Vilken loggning/audit krävs? | Öppen | |
| E-Q14 | Finns krav på kryptering under transport och lagring? | Öppen | |

## Acceptanskriterier – första version

| ID | Acceptanskriterium | Status |
|---|---|---|
| E-A01 | En testinspelning kan identifieras. | Öppet |
| E-A02 | Inspelningen kan kopplas till rätt intervju. | Öppet |
| E-A03 | Ljudfil kan hämtas. | Öppet |
| E-A04 | Status kan visas. | Öppet |
| E-A05 | Fel kan registreras. | Öppet |
| E-A06 | Samma inspelning kan inte importeras två gånger av misstag. | Öppet |
| E-A07 | Ett tydligt gränssnitt finns mot framtida verksamhetssystem. | Öppet |
| E-A08 | Verksamhetssystemets detaljer är inte hårdkodade i kärnlogiken. | Öppet |

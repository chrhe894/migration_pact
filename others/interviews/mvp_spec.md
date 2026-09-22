# MVP-specifikation – Outlook → verksamhetssystem → Zoom

## Instruktion till AI i IDE

Bygg en liten, tydligt avgränsad MVP som orkestrerar ett redan bokat Outlook-möte.

MVP:n ska:
1. Hämta information från ett valt/bokat Outlook-möte via Microsoft Graph.
2. Använda relevant information från mötet, framför allt gruppnummer/ärendeidentifierare, för att hämta individer från ett verksamhetssystem.
3. Visa individerna i applikationen.
4. Skapa ett separat Zoom-möte med unikt Meeting ID för varje individ via Zoom API.
5. Spara resultatet per individ.
6. Skriva tillbaka en tabell med resultatet till Outlook-mötets body.
7. Inte implementera den fullständiga bokningsmotorn, själva intervjugenomförandet eller efterarbetet ännu.

Prioritera enkelhet, tydliga gränssnitt mellan integrationerna och testbar kod. Undvik att bygga framtida funktionalitet innan MVP:n fungerar.

---

## 1. Målbild

```text
Outlook-möte
    │
    ▼
Microsoft Graph
    │
    ▼
MVP-applikation
    │
    ├──► Verksamhetssystem → individer
    │
    └──► Zoom API → ett separat möte per individ
    │
    ▼
Resultattabell
    │
    ▼
Microsoft Graph
    │
    ▼
Samma Outlook-möte uppdateras
```

Applikationen är orkestrator. Outlook, verksamhetssystemet och Zoom är externa system.

---

## 2. Avgränsning för MVP

### Ska ingå

| ID | Krav | Prioritet |
|---|---|---|
| MVP-001 | Läsa ett befintligt Outlook-möte via Microsoft Graph. | Must |
| MVP-002 | Visa mötets relevanta information i applikationen. | Must |
| MVP-003 | Hämta gruppnummer/ärendeidentifierare från mötet. | Must |
| MVP-004 | Anropa verksamhetssystemet och hämta individer i gruppen. | Must |
| MVP-005 | Visa individernas namn och individnummer. | Must |
| MVP-006 | Skapa ett separat Zoom-möte per individ. | Must |
| MVP-007 | Varje individ ska få ett eget unikt Zoom Meeting ID. | Must |
| MVP-008 | Spara Zoom URL och Meeting ID tillsammans med rätt individ. | Must |
| MVP-009 | Visa resultatet i en tabell i applikationen. | Must |
| MVP-010 | Uppdatera det ursprungliga Outlook-mötets body med resultattabellen. | Must |
| MVP-011 | Hantera fel per individ utan att hela körningen behöver avbrytas. | Should |
| MVP-012 | Logga vad applikationen gör och resultatet från varje integration. | Must |

### Ska inte ingå ännu

- Automatisk sökning efter bästa mötestid.
- Bokning av Outlook-möten.
- Automatisk hantering av personal, rum, utrustning eller tolk.
- Själva intervjugenomförandet.
- Start/stopp av Zoom under intervjun.
- Byte av Zoom-möte under intervjun.
- Hämtning av inspelningar.
- Efterbearbetning av ljud.
- Integration med efterföljande verksamhetssystem.
- Outlook-plugin/add-in.
- Avancerad användaradministration.
- Fullständig databaslösning om den inte behövs för MVP:n.

---

## 3. Outlook / Microsoft Graph

Använd Microsoft Graph som integration mot Microsoft 365.

Applikationen behöver kunna:
1. Hämta ett specifikt kalenderobjekt.
2. Läsa Event ID, subject, start, end, location, body och vid behov attendees.
3. Uppdatera body på samma event.

Använd inte Outlooks UI-automation. Kommunicera med Outlook via Microsoft Graph API.

### Val av möte

Första MVP-versionen kan ha en enkel lösning där användaren väljer ett möte i en lista eller anger/klistrar in ett Event ID.

Välj den enklaste lösningen som är rimlig för utvecklingsmiljön.

---

## 4. Gruppnummer / ärendeinformation

Utgångspunkt:

```text
Outlook-möte
      │
      ▼
Gruppnummer
      │
      ▼
Verksamhetssystem
      │
      ▼
Lista med individer
```

Hur gruppnumret ligger i Outlook-mötet ska isoleras bakom en tydlig funktion:

```text
extract_group_number(event)
```

Anta inte i onödan att gruppnumret alltid finns på exakt samma plats i body/subject innan detta är verifierat.

---

## 5. Verksamhetssystem

Skapa ett separat integrationslager.

Exempel:

```text
BusinessSystemService

get_group(group_number)
    -> Group

get_individuals(group_number)
    -> list[Individual]
```

Intern datamodell:

```json
{
  "individualNumber": "12345",
  "name": "Anna Andersson"
}
```

Om riktiga API:t ännu inte är tillgängligt ska integrationen kunna mockas.

---

## 6. Zoom

Använd Zoom API.

För varje individ ska applikationen skapa ett separat Zoom-möte.

Minst följande ska sparas:

```text
Zoom URL
Zoom Meeting ID
```

Eventuellt även passcode, start time, duration och meeting type om det behövs.

Exakta Zoom-inställningar ska ligga i konfiguration och inte hårdkodas på flera ställen.

Viktigt: Applikationen ska inte själv generera Meeting ID. Zoom ska skapa mötet och returnera Meeting ID.

---

## 7. Tidsinformation

Outlook-mötet innehåller en tidsperiod.

Första MVP:n ska inte implementera avancerad tidsfördelning mellan individer om det inte uttryckligen behövs.

Hur tiderna ska fördelas är en separat verksamhetsfråga.

---

## 8. Intern datamodell

Skapa en intern modell för hela körningen.

Exempel:

```json
{
  "outlookEventId": "...",
  "groupNumber": "20260012",
  "subject": "Familjeintervju",
  "start": "2026-10-05T09:00:00",
  "end": "2026-10-05T12:00:00",
  "location": "Rum 3",
  "individuals": [
    {
      "individualNumber": "12345",
      "name": "Anna Andersson",
      "meetingType": "Sakintervju",
      "zoomUrl": "...",
      "zoomMeetingId": "123456789",
      "status": "created"
    }
  ]
}
```

Använd riktiga datamodeller/klasser i koden snarare än lösa dictionaries överallt.

---

## 9. Resultattabell

Applikationen ska visa minst:

| Kolumn | Beskrivning |
|---|---|
| Namn | Individens namn |
| Individnummer | Individens identifierare |
| Mötestyp | Exempelvis Sakintervju |
| Zoom URL | URL för Zoom-mötet |
| Meeting ID | Zooms Meeting ID |
| Status | Exempelvis Skapad / Fel |

---

## 10. Uppdatering av Outlook

När Zoom-mötena är skapade ska applikationen uppdatera det ursprungliga Outlook-mötet och lägga till resultattabellen i body.

Var försiktig så att befintligt innehåll inte oavsiktligt skrivs över.

Strategin ska vara:

```text
existing body
       +
MVP-generated section
       =
updated body
```

Det ska också vara möjligt att köra processen igen utan att skapa duplicerade resultatsektioner.

---

## 11. Idempotens / körning flera gånger

MVP:n ska ta hänsyn till att användaren kan köra processen två gånger.

Minimikrav:
- Identifiera om Outlook-eventet redan innehåller en tidigare genererad resultatsektion.
- Informera användaren.
- Låt användaren välja om befintligt resultat ska användas/uppdateras eller om en ny körning ska göras.

Undvik en komplex databaslösning enbart för detta om det kan lösas enklare i MVP:n.

---

## 12. Felhantering

Ett fel för en individ ska inte automatiskt stoppa alla andra.

Exempel:

```text
Anna Andersson   → Zoom skapad
Erik Andersson   → Zoom skapad
Sara Andersson   → FEL
Karin Andersson  → Zoom skapad
```

Resultatet ska visa exempelvis:

```text
3 skapade
1 fel
```

---

## 13. GUI

GUI:t ska vara enkelt och behöver i princip tre steg.

### Steg 1 – Outlook-möte

```text
Välj Outlook-möte

[ Familjeintervju – 2026-10-05 09:00 ]

Gruppnummer: 20260012
Tid:          09:00–12:00
Plats:        Rum 3

[ Hämta grupp ]
```

### Steg 2 – Individer

```text
Grupp: 20260012

| Namn | Individnummer | Mötestyp |
|------|---------------|----------|
| Anna | 12345         | Sakintervju |
| Erik | 12346         | Sakintervju |
| Sara | 12347         | Sakintervju |

[ Skapa Zoom-möten ]
```

### Steg 3 – Resultat

```text
Zoom-möten

| Namn | Individnummer | Mötestyp | Zoom URL | Meeting ID | Status |
|------|---------------|----------|----------|------------|--------|
| Anna | 12345 | Sakintervju | ... | ... | Skapad |
| Erik | 12346 | Sakintervju | ... | ... | Skapad |

[ Uppdatera Outlook ]

Status: 2 av 2 skapade
```

GUI:t ska inte försöka efterlikna Outlook.

---

## 14. Teknisk arkitektur

Föreslagen struktur:

```text
app/
├── main
├── ui/
├── models/
├── services/
│   ├── outlook/
│   ├── business_system/
│   └── zoom/
├── orchestration/
├── config/
└── tests/
```

Princip:

```text
UI
 │
 ▼
Orchestrator
 │
 ├── OutlookService
 ├── BusinessSystemService
 └── ZoomService
```

UI:t ska inte anropa Graph eller Zoom direkt.

Orchestratorn ska inte innehålla HTTP-detaljer för externa API:er.

---

## 15. Konfiguration och hemligheter

Lägg inte client secrets, API-nycklar, Zoom credentials eller lösenord direkt i källkoden.

Använd organisationens godkända metod för miljövariabler/secret storage.

Exempel:

```text
MICROSOFT_TENANT_ID
MICROSOFT_CLIENT_ID
ZOOM_CLIENT_ID
ZOOM_CLIENT_SECRET
BUSINESS_SYSTEM_BASE_URL
```

Exakta värden ska komma från miljön. Hitta inte på produktionsvärden.

---

## 16. Autentisering

För Microsoft Graph ska organisationens godkända Microsoft Entra ID-flöde användas.

För Zoom ska organisationens godkända OAuth-/server-till-server-modell användas.

AI:t ska inte hitta på credentials, scopes eller tenant-specifika värden.

Om något saknas:

```text
TODO – kräver miljöspecifik konfiguration
```

---

## 17. Testning

Skapa tester för:
1. Parsing av gruppnummer.
2. Mappning från individ till Zoom-resultat.
3. Lyckad Zoom-skapning.
4. Zoom-fel för en individ.
5. Generering av Outlook-tabell.
6. Uppdatering av body utan att förstöra befintligt innehåll.
7. Körning två gånger/idempotens.
8. Mockad verksamhetssystemsintegration.
9. Mockad Zoom-integration.
10. Mockad Microsoft Graph-integration.

Integrationstester mot riktiga system ska kunna köras separat.

---

## 18. Loggning

Logga minst:

```text
Start av körning
Outlook event identifierat
Gruppnummer identifierat
Antal individer hämtade
Zoom-möte skapat per individ
Zoom-möte misslyckades per individ
Outlook uppdaterat
Körning klar
```

Loggar får inte innehålla tokens eller andra hemligheter.

Personuppgifter ska hanteras enligt organisationens säkerhets- och dataskyddskrav.

---

## 19. Öppna frågor – ska inte gissas

| ID | Fråga |
|---|---|
| Q-001 | Exakt var i Outlook-mötet finns gruppnumret? |
| Q-002 | Vilket API/endpoint används för verksamhetssystemet? |
| Q-003 | Vilka fält returnerar verksamhetssystemet för individen? |
| Q-004 | Vilken autentisering krävs mot verksamhetssystemet? |
| Q-005 | Vilket Zoom-konto ska skapa mötena? |
| Q-006 | Vilka Zoom-inställningar ska gälla? |
| Q-007 | Ska Zoom-mötena ha samma start/sluttid som Outlook-mötet eller annan tidslogik? |
| Q-008 | Ska mötestypen alltid vara "Sakintervju" i MVP eller hämtas från annat system? |
| Q-009 | Ska Zoom URL/Meeting ID skrivas i body eller annan del av Outlook-eventet? |
| Q-010 | Hur ska en omkörning hanteras verksamhetsmässigt? |
| Q-011 | Vilka Microsoft Graph permissions får applikationen använda? |
| Q-012 | Vilka Zoom API permissions får applikationen använda? |

AI:t ska stanna och fråga efter information när en fråga är blockerande. Hitta inte på verksamhetsregler.

---

## 20. Definition of Done för MVP

- [ ] Användaren kan välja ett befintligt Outlook-möte.
- [ ] Applikationen hämtar mötets information via Microsoft Graph.
- [ ] Gruppnumret kan identifieras.
- [ ] Gruppen kan hämtas från verksamhetssystemet, alternativt via mock.
- [ ] Individerna visas i GUI:t.
- [ ] Ett separat Zoom-möte skapas för varje individ.
- [ ] Varje Zoom-möte har ett eget Meeting ID.
- [ ] Zoom URL och Meeting ID kopplas till rätt individ.
- [ ] Resultatet visas i en tabell.
- [ ] Tabellen skrivs tillbaka till samma Outlook-möte.
- [ ] Befintligt Outlook-innehåll bevaras.
- [ ] Omkörning hanteras kontrollerat.
- [ ] Ett fel för en individ påverkar inte automatiskt övriga individer.
- [ ] Loggning finns.
- [ ] Tester finns för central logik.
- [ ] Inga hemligheter är hårdkodade.

---

## 21. Framtida utbyggnad

MVP:n ska senare kunna utvecklas mot:

```text
MVP
 │
 ├── Del 1: Bokning
 │
 ├── Del 2: Genomförande
 │
 └── Del 3: Efterarbete
```

Använd därför redan nu ett internt resultatobjekt som senare kan utvecklas till ett formellt "Genomförandepaket".

Bygg dock inte de tre delarna nu.

Fokusera på:

```text
Outlook
   ↓
Grupp
   ↓
Individer
   ↓
Zoom-möten
   ↓
Resultattabell
   ↓
Outlook
```

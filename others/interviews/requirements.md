# Requirements Document

## Introduction

Detta dokument formaliserar MVP-specifikationen i `mvp_spec.md` till strukturerade, avbockningsbara krav enligt EARS-mönster och INCOSE-kvalitetsregler.

MVP:n är en orkestrerande applikation som utgår från ett redan bokat Outlook-möte, hämtar en grupp av individer från ett verksamhetssystem, skapar ett separat Zoom-möte per individ och skriver tillbaka en resultattabell i det ursprungliga Outlook-mötets body. Applikationen är orkestratorn; Outlook, verksamhetssystemet och Zoom är externa system som nås via tydligt avgränsade integrationslager.

Kärnflödet är: Outlook-möte → gruppnummer → individer → ett Zoom-möte per individ → resultattabell → tillbaka till Outlook-mötet.

Dokumentet täcker MVP-kraven MVP-001–MVP-012, Definition of Done (spec avsnitt 20), samt registrerar de öppna frågorna Q-001–Q-012 (spec avsnitt 19) som kända osäkerheter/antaganden. Framtida funktionalitet (bokningsmotor, intervjugenomförande, efterarbete, inspelningar) är uttryckligen utanför scope.

## Glossary

- **System**: Hela MVP-applikationen som orkestrerar flödet.
- **Orchestrator**: Komponent som binder ihop flödet och anropar tjänstelagren. Innehåller inga HTTP-detaljer för externa API:er.
- **UI**: Användargränssnittet. Anropar Orchestrator, aldrig externa API:er direkt.
- **OutlookService**: Gemensamt tjänstegränssnitt mot kalender/mötesdata. Håller flera bakomliggande implementationer öppna (on-prem Exchange via EWS, Exchange Online via Microsoft Graph, annan källa via CalDAV).
- **BusinessSystemService**: Tjänstegränssnitt mot verksamhetssystemet med operationerna `get_group` och `get_individuals`.
- **ZoomService**: Tjänstegränssnitt mot Zoom API för att skapa möten.
- **Outlook_Event**: Ett kalenderobjekt/möte med fälten Event ID, subject, start, end, location och body.
- **Event_ID**: Unik identifierare för ett Outlook_Event.
- **Group_Number**: Gruppnummer/ärendeidentifierare kopplat till ett Outlook_Event.
- **Individual**: En person i gruppen, med individnummer, namn och valfri roll (barn/förälder/okänd).
- **Individual_Number**: Individens identifierare.
- **Zoom_Meeting**: Ett Zoom-möte skapat via Zoom API.
- **Meeting_ID**: Zooms egen unika identifierare för ett Zoom_Meeting, genererad av Zoom.
- **Zoom_URL**: URL för ett Zoom_Meeting.
- **Result_Table**: Tabell med kolumnerna Namn, Individnummer, Mötestyp, Zoom URL, Meeting ID och Status.
- **Result_Section**: Den avgränsade sektion i Outlook_Event-body som System skriver Result_Table i.
- **Run_Result**: Sammanhållet internt resultatobjekt för en körning.
- **Mock_Mode**: Läge (styrt av flaggan `USE_MOCKS`) där alla tre integrationerna körs mot mockade implementationer utan riktiga credentials.

## Requirements

### Requirement 1: Läsa Outlook-möte (MVP-001, MVP-002)

**User Story:** Som användare vill jag läsa in ett befintligt Outlook-möte, så att jag kan utgå från det bokade mötet i det vidare flödet.

#### Acceptance Criteria

1. WHEN användaren väljer eller anger ett Event_ID, THE OutlookService SHALL hämta motsvarande Outlook_Event.
2. WHEN ett Outlook_Event hämtas, THE OutlookService SHALL läsa fälten Event_ID, subject, start, end, location och body.
3. WHEN ett Outlook_Event har hämtats, THE UI SHALL visa mötets subject, start, end och location.
4. IF ett Outlook_Event med angivet Event_ID inte kan hämtas, THEN THE System SHALL visa ett felmeddelande och avbryta körningen.
5. THE System SHALL läsa och uppdatera kalenderdata enbart via OutlookService och SHALL undvika UI-automation av Outlook-klienten.

### Requirement 2: OutlookService-abstraktion med flera bakomliggande källor

**User Story:** Som utvecklare vill jag att kalenderintegrationen ligger bakom ett gemensamt gränssnitt, så att den bakomliggande källan kan bytas utan att övrig kod påverkas.

#### Acceptance Criteria

1. THE OutlookService SHALL exponera ett gemensamt gränssnitt för att hämta ett Outlook_Event och uppdatera dess body.
2. THE OutlookService SHALL stödja att en av flera bakomliggande implementationer väljs: on-prem Exchange via EWS, Exchange Online via Microsoft Graph, eller annan källa via CalDAV.
3. THE System SHALL fungera med OutlookService-gränssnittet utan att binda sig till en enda konkret bakomliggande implementation.
4. WHERE en konkret bakomliggande implementation kräver miljöspecifik konfiguration, THE System SHALL markera den saknade konfigurationen som TODO i stället för att använda påhittade värden.

### Requirement 3: Extrahera gruppnummer (MVP-003)

**User Story:** Som användare vill jag att gruppnumret hämtas från mötet, så att rätt grupp kan slås upp i verksamhetssystemet.

#### Acceptance Criteria

1. WHEN ett Outlook_Event har hämtats, THE System SHALL extrahera Group_Number via en isolerad funktion `extract_group_number(event)`.
2. THE System SHALL isolera logiken för var Group_Number finns i Outlook_Event bakom `extract_group_number(event)` och SHALL inte anta en exakt placering i body eller subject utöver vad som är verifierat (Q-001).
3. IF Group_Number inte kan extraheras ur Outlook_Event, THEN THE System SHALL visa ett felmeddelande och avbryta körningen.
4. WHEN Group_Number har extraherats, THE UI SHALL visa Group_Number.

### Requirement 4: Hämta individer från verksamhetssystemet (MVP-004, MVP-005)

**User Story:** Som användare vill jag hämta individerna i gruppen, så att jag ser vilka personer som ska få ett Zoom-möte.

#### Acceptance Criteria

1. WHEN Group_Number har extraherats, THE BusinessSystemService SHALL hämta gruppen via operationen `get_group`.
2. WHEN Group_Number har extraherats, THE BusinessSystemService SHALL hämta gruppens individer via operationen `get_individuals`.
3. THE Individual SHALL innehålla Individual_Number, namn och en valfri roll med värdena barn, förälder eller okänd.
4. WHEN individerna har hämtats, THE UI SHALL visa varje individs namn och Individual_Number.
5. IF anropet till BusinessSystemService misslyckas, THEN THE System SHALL visa ett felmeddelande och avbryta körningen.

### Requirement 5: Skapa Zoom-möte per individ (MVP-006, MVP-007, MVP-008)

**User Story:** Som användare vill jag att ett separat Zoom-möte skapas för varje individ, så att varje person får en egen unik möteslänk.

#### Acceptance Criteria

1. WHEN användaren startar skapandet av Zoom-möten, THE ZoomService SHALL skapa ett separat Zoom_Meeting för varje Individual.
2. WHEN ett Zoom_Meeting skapas, THE ZoomService SHALL använda det Meeting_ID som Zoom API returnerar och THE System SHALL inte själv generera Meeting_ID.
3. WHEN ett Zoom_Meeting har skapats för en Individual, THE System SHALL spara Zoom_URL och Meeting_ID kopplade till den Individual.
4. THE System SHALL hämta Zoom-inställningar från konfiguration och SHALL inte hårdkoda dem på flera ställen.

### Requirement 6: Felhantering per individ (MVP-011)

**User Story:** Som användare vill jag att ett fel för en individ inte stoppar övriga, så att resten av gruppen ändå får sina Zoom-möten.

#### Acceptance Criteria

1. IF skapandet av ett Zoom_Meeting för en Individual misslyckas, THEN THE System SHALL fortsätta bearbeta återstående individer.
2. IF skapandet av ett Zoom_Meeting för en Individual misslyckas, THEN THE System SHALL sätta statusen för den Individual till fel.
3. WHEN alla individer har bearbetats, THE System SHALL visa antalet skapade Zoom-möten och antalet fel.

### Requirement 7: Visa resultattabell (MVP-009)

**User Story:** Som användare vill jag se resultatet i en tabell, så att jag kan verifiera vilka möten som skapats.

#### Acceptance Criteria

1. WHEN alla individer har bearbetats, THE UI SHALL visa en Result_Table med kolumnerna Namn, Individnummer, Mötestyp, Zoom URL, Meeting ID och Status.
2. THE UI SHALL visa en rad i Result_Table för varje Individual i körningen.
3. THE UI SHALL visa statusen för varje Individual som skapad eller fel.

### Requirement 8: Uppdatera Outlook-mötets body idempotent (MVP-010)

**User Story:** Som användare vill jag skriva tillbaka resultattabellen i det ursprungliga mötet, så att informationen finns samlad i Outlook utan att befintligt innehåll skadas.

#### Acceptance Criteria

1. WHEN användaren väljer att uppdatera Outlook, THE OutlookService SHALL skriva en Result_Section som innehåller Result_Table i det ursprungliga Outlook_Event-body.
2. WHEN Outlook_Event-body uppdateras, THE System SHALL bevara det befintliga innehållet i body.
3. WHEN Outlook_Event-body redan innehåller en tidigare Result_Section, THE System SHALL uppdatera den befintliga Result_Section i stället för att lägga till en ny.
4. WHEN processen körs flera gånger på samma Outlook_Event, THE System SHALL undvika duplicerade Result_Section i body.

### Requirement 9: Kontrollerad omkörning (MVP-010, idempotens)

**User Story:** Som användare vill jag att en omkörning hanteras kontrollerat, så att jag medvetet väljer om ett tidigare resultat ska behållas eller ersättas.

#### Acceptance Criteria

1. WHEN ett Outlook_Event redan innehåller en tidigare Result_Section, THE System SHALL informera användaren om att ett tidigare resultat finns.
2. WHEN ett tidigare resultat finns och användaren startar en körning, THE System SHALL låta användaren välja mellan att använda/uppdatera det befintliga resultatet eller göra en ny körning.
3. WHERE den verksamhetsmässiga hanteringen av en omkörning ännu inte är fastställd, THE System SHALL behandla frågan som en känd öppen fråga (Q-010).

### Requirement 10: Loggning (MVP-012)

**User Story:** Som utvecklare vill jag att applikationen loggar sina steg, så att jag kan följa och felsöka en körning.

#### Acceptance Criteria

1. WHEN en körning startar, THE System SHALL logga att körningen startat.
2. WHEN ett Outlook_Event har identifierats, THE System SHALL logga att eventet identifierats.
3. WHEN Group_Number har identifierats, THE System SHALL logga att gruppnumret identifierats.
4. WHEN individerna har hämtats, THE System SHALL logga antalet hämtade individer.
5. WHEN ett Zoom_Meeting har skapats för en Individual, THE System SHALL logga att mötet skapats.
6. IF ett Zoom_Meeting för en Individual misslyckas, THEN THE System SHALL logga att mötet misslyckats.
7. WHEN Outlook_Event har uppdaterats, THE System SHALL logga att Outlook uppdaterats.
8. WHEN körningen är klar, THE System SHALL logga att körningen är klar.
9. THE System SHALL utelämna tokens och andra hemligheter ur loggarna.

### Requirement 11: Arkitektur och separation av ansvar

**User Story:** Som utvecklare vill jag ha tydliga gränser mellan UI, orchestrator och tjänstelager, så att koden blir testbar och underhållbar.

#### Acceptance Criteria

1. THE UI SHALL anropa Orchestrator och SHALL inte anropa externa API:er direkt.
2. THE Orchestrator SHALL anropa OutlookService, BusinessSystemService och ZoomService och SHALL inte innehålla HTTP-detaljer för externa API:er.
3. THE System SHALL representera körningen med interna datamodeller/klasser i stället för lösa dictionaries.
4. THE Run_Result SHALL vara utformat så att det senare kan utökas till ett formellt genomförandepaket.

### Requirement 12: Mockat läge för lokal utveckling

**User Story:** Som utvecklare vill jag kunna köra hela flödet mockat utan credentials, så att jag kan utveckla på privat dator innan koden flyttas till en riktig miljö.

#### Acceptance Criteria

1. WHERE Mock_Mode är aktiverat, THE System SHALL köra OutlookService, BusinessSystemService och ZoomService mot mockade implementationer utan riktiga credentials.
2. THE System SHALL styra valet mellan mockade och riktiga implementationer via flaggan `USE_MOCKS`.
3. WHERE Mock_Mode är aktiverat, THE System SHALL kunna genomföra hela kärnflödet från Outlook_Event till uppdaterad body med mockdata.

### Requirement 13: Konfiguration och hemligheter

**User Story:** Som säkerhetsansvarig vill jag att inga hemligheter hårdkodas, så att credentials hanteras enligt organisationens krav.

#### Acceptance Criteria

1. THE System SHALL läsa client secrets, API-nycklar, Zoom-credentials och lösenord från miljön eller godkänd secret storage.
2. THE System SHALL undvika att lagra hemligheter i källkoden.
3. WHERE ett miljöspecifikt värde saknas, THE System SHALL markera det som TODO i stället för att använda ett påhittat värde.

### Requirement 14: Testning av central logik (Definition of Done)

**User Story:** Som utvecklare vill jag ha tester för central logik, så att jag kan verifiera MVP:ns beteende.

#### Acceptance Criteria

1. THE System SHALL innehålla tester för extrahering av Group_Number.
2. THE System SHALL innehålla tester för mappning från Individual till Zoom-resultat.
3. THE System SHALL innehålla tester för lyckat skapande av Zoom_Meeting.
4. THE System SHALL innehålla tester för fel vid skapande av Zoom_Meeting för en enskild Individual.
5. THE System SHALL innehålla tester för generering av Result_Table.
6. THE System SHALL innehålla tester som verifierar att uppdatering av Outlook_Event-body bevarar befintligt innehåll.
7. THE System SHALL innehålla tester för idempotens vid omkörning på samma Outlook_Event.
8. THE System SHALL innehålla tester mot mockad BusinessSystemService, mockad ZoomService och mockad OutlookService.

## Avgränsning (utanför MVP-scope)

Följande funktionalitet är uttryckligen utanför MVP och ska inte byggas nu:

- Automatisk sökning efter bästa mötestid och bokningsmotor.
- Automatisk hantering av personal, rum, utrustning eller tolk.
- Själva intervjugenomförandet samt start/stopp eller byte av Zoom-möte under intervjun.
- Hämtning av inspelningar och efterbearbetning av ljud.
- Integration med efterföljande verksamhetssystem.
- Outlook-plugin/add-in och avancerad användaradministration.
- Fullständig databaslösning om den inte behövs för MVP:n.

## Kända öppna frågor och antaganden

Följande frågor från spec avsnitt 19 är registrerade som kända osäkerheter. System ska inte gissa verksamhetsregler; blockerande frågor ska tas upp med användaren.

| ID | Fråga | Status/antagande i MVP |
|---|---|---|
| Q-001 | Exakt var i Outlook-mötet finns gruppnumret? | Isoleras bakom `extract_group_number(event)`; ingen exakt placering antas (Krav 3). |
| Q-002 | Vilket API/endpoint används för verksamhetssystemet? | Öppen. BusinessSystemService kan mockas (Krav 4, 12). |
| Q-003 | Vilka fält returnerar verksamhetssystemet för individen? | Antagande i MVP: namn + individnummer + valfri roll (Krav 4). |
| Q-004 | Vilken autentisering krävs mot verksamhetssystemet? | Öppen. Konfiguration/TODO (Krav 13). |
| Q-005 | Vilket Zoom-konto ska skapa mötena? | Öppen. Konfiguration/TODO (Krav 13). |
| Q-006 | Vilka Zoom-inställningar ska gälla? | Öppen. Läses från konfiguration (Krav 5). |
| Q-007 | Ska Zoom-mötena ha samma tid som Outlook-mötet eller annan tidslogik? | Öppen verksamhetsfråga; ingen avancerad tidsfördelning i MVP. |
| Q-008 | Ska mötestypen alltid vara "Sakintervju" i MVP eller hämtas från annat system? | Öppen. Standardantagande "Sakintervju". |
| Q-009 | Ska Zoom URL/Meeting ID skrivas i body eller annan del av eventet? | Antagande i MVP: i body (Krav 8). |
| Q-010 | Hur ska en omkörning hanteras verksamhetsmässigt? | Öppen (Krav 9). |
| Q-011 | Vilka Microsoft Graph permissions får applikationen använda? | Öppen. Konfiguration/TODO (Krav 13). |
| Q-012 | Vilka Zoom API permissions får applikationen använda? | Öppen. Konfiguration/TODO (Krav 13). |

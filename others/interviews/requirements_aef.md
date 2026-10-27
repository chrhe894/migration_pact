# Requirements Document – ÄF-integration (Outlook + Zoom-bokning)

## Introduction

Detta dokument beskriver kraven för ny funktionalitet som ska läggas in i det
befintliga systemet **ÄF** (ett äldre Java-system som redan bokar in möten i
Outlook till en handläggare). Syftet är att ÄF, utöver Outlook-bokningen, även
ska kunna skapa Zoom-möten enligt tre olika bokningslägen och sätta Zoom-mötena
i privat läge automatiskt.

Dokumentet innehåller **endast krav** (ingen design eller implementation) och är
avsett som underlag för att estimera tidsåtgång för realisering. Koden skrivs
senare direkt i ÄF, inte i detta repo.

Logiken som avgör vilket bokningsläge som ska användas ligger i ÄF och ligger
**utanför** detta dokument. Kraven behandlar valt bokningsläge, handläggare,
person(er) och mötesdata som given indata från ÄF.

## Antaganden

Dessa antaganden ligger till grund för kraven och bör bekräftas innan estimat
fastställs (se även Öppna frågor):

- **A1**: Zoom-autentisering sker med Server-to-Server OAuth (ÄF agerar som
  tjänst och bokar å handläggarens vägnar). Användarbaserad OAuth är ej vald.
- **A2**: ÄF tillhandahåller nödvändig indata per bokning: bokningsläge,
  handläggare, person(er) med individnummer samt roll (vuxen/barn) där det behövs.
- **A3**: "Privat läge" avser Zoom-mötesinställningar som normalt sätts manuellt
  och som här ska sättas automatiskt per möte (se Krav 5 och Ordlista).
- **A4**: Intervjureglerna för grupp (läge C) är desamma som i den tidigare
  prototypen: en intervju per vuxen samt ett barnfokuserat möte per (barn, vuxen).

## Glossary

- **ÄF**: Det befintliga Java-systemet som bokar Outlook-möten till en handläggare och som ska utökas med Zoom-bokning.
- **Handläggare**: Den person hos verksamheten som mötet bokas till i Outlook.
- **Person**: En individ som ska delta i mötet, identifierad med ett individnummer.
- **Individnummer**: En textsträng som identifierar en person. Behandlas som text.
- **Grupp**: En uppsättning personer (t.ex. vuxna och barn) som en bokning avser.
- **Roll**: En persons roll i en grupp: vuxen eller barn (styr intervjugenereringen i läge C).
- **Bokningsläge**: Ett av tre lägen (A, B, C) som ÄF väljer för en bokning, se nedan.
- **Läge A**: 1 Outlook-möte + 1 Zoom-möte för handläggare och en (1) person.
- **Läge B**: 1 Outlook-möte + flera Zoom-möten för en hel grupp, där Outlook-mötet innehåller en lista med Zoom-URL:er och mötes-id:n.
- **Läge C**: 1 Zoom-möte per person i gruppen enligt intervjureglerna (en intervju per vuxen samt barnfokuserat möte per barn och vuxen).
- **Zoom-möte**: Ett möte skapat via Zoom API. Meeting ID och Join URL genereras av Zoom, aldrig av ÄF.
- **Privat läge**: Zoom-mötesinställningar som gör mötet privat/skyddat, satta automatiskt vid skapandet (se Krav 5).
- **Outlook-möte**: Den kalenderbokning i Outlook som ÄF skapar för handläggaren.

## Requirements

### Krav 1: Zoom-autentisering

**User Story:** Som ÄF-system vill jag autentisera mot Zoom innan möten skapas, så att Zoom-möten kan bokas å handläggarens vägnar utan manuell inloggning.

#### Acceptanskriterier

1. NÄR ÄF behöver skapa ett Zoom-möte, SKALL *ÄF* säkerställa att ett giltigt Zoom-access token finns innan anrop mot Zoom API görs.
2. OM inget giltigt access token finns, DÅ SKALL *ÄF* hämta ett nytt token enligt vald autentiseringsmetod (antagande: Server-to-Server OAuth) innan möten skapas.
3. OM autentiseringen mot Zoom misslyckas, DÅ SKALL *ÄF* avbryta bokningen av Zoom-möten och signalera ett fel utan att skapa några ofullständiga möten.
4. *ÄF* SKALL läsa Zoom-credentials från en säker källa utanför källkoden och SKALL INTE logga credentials eller tokens i klartext.

### Krav 2: Läge A – ett Outlook-möte och ett Zoom-möte

**User Story:** Som handläggare vill jag att ÄF bokar ett Outlook-möte med ett tillhörande Zoom-möte för mig och en person, så att vi kan ha ett enskilt videomöte.

#### Acceptanskriterier

1. NÄR ÄF utför en bokning i läge A, SKALL *ÄF* skapa exakt ett (1) Zoom-möte för handläggaren och den angivna personen.
2. NÄR Zoom-mötet har skapats, SKALL *ÄF* skapa exakt ett (1) Outlook-möte för handläggaren och infoga Zoom-mötets Join URL och Meeting ID i Outlook-mötet.
3. *ÄF* SKALL använda det Meeting ID och den Join URL som Zoom returnerar och SKALL INTE generera dessa själv.
4. OM skapandet av Zoom-mötet misslyckas, DÅ SKALL *ÄF* signalera ett fel och SKALL INTE skapa ett Outlook-möte utan giltig Zoom-länk.

### Krav 3: Läge B – ett Outlook-möte med flera Zoom-möten för en grupp

**User Story:** Som handläggare vill jag att ÄF bokar ett Outlook-möte som samlar flera Zoom-möten för en hel grupp, så att jag har alla länkar på ett ställe.

#### Acceptanskriterier

1. NÄR ÄF utför en bokning i läge B, SKALL *ÄF* skapa ett Zoom-möte per person i gruppen.
2. OM skapandet av ett enskilt Zoom-möte i gruppen misslyckas, DÅ SKALL *ÄF* fortsätta skapa övriga Zoom-möten i gruppen utan avbrott.
3. NÄR gruppens Zoom-möten har bearbetats, SKALL *ÄF* skapa exakt ett (1) Outlook-möte för handläggaren som innehåller en lista med Join URL och Meeting ID för varje skapat Zoom-möte.
4. *ÄF* SKALL i Outlook-mötet tydligt koppla varje Zoom-länk till rätt person i gruppen.
5. OM inget Zoom-möte kunde skapas för gruppen, DÅ SKALL *ÄF* signalera ett fel och SKALL INTE skapa ett tomt Outlook-möte.

### Krav 4: Läge C – ett Zoom-möte per person enligt intervjureglerna

**User Story:** Som handläggare vill jag att ÄF skapar Zoom-möten enligt intervjureglerna för en grupp, så att varje vuxen och varje barnfokuserat möte får en egen länk.

#### Acceptanskriterier

1. NÄR ÄF utför en bokning i läge C, SKALL *ÄF* skapa ett Zoom-möte per vuxen i gruppen (vuxen ensam).
2. NÄR både barn och vuxna finns i gruppen, SKALL *ÄF* skapa ett barnfokuserat Zoom-möte per kombination av (barn, vuxen), dvs varje barn paras med varje vuxen.
3. OM skapandet av ett enskilt Zoom-möte misslyckas, DÅ SKALL *ÄF* fortsätta skapa övriga möten utan avbrott.
4. *ÄF* SKALL använda det Meeting ID och den Join URL som Zoom returnerar för varje möte och SKALL INTE generera dessa själv.
5. *ÄF* SKALL koppla varje skapat Zoom-möte till rätt person(er) så att resultatet kan presenteras eller skrivas tillbaka korrekt.

### Krav 5: Privat läge för Zoom-möten

**User Story:** Som verksamhet vill jag att alla Zoom-möten skapas i privat läge automatiskt, så att möten inte kan nås av obehöriga och inget manuellt steg krävs.

#### Acceptanskriterier

1. NÄR ÄF skapar ett Zoom-möte i något av lägena A, B eller C, SKALL *ÄF* sätta mötet i privat läge automatiskt via Zoom-mötesinställningar vid skapandet.
2. *ÄF* SKALL tillämpa privat läge på samtliga skapade Zoom-möten utan att något manuellt steg krävs.
3. *ÄF* SKALL definiera inställningarna för privat läge på en enda central plats så att de inte upprepas per bokningsläge.

### Krav 6: Felhantering och återkoppling

**User Story:** Som handläggare vill jag få tydlig återkoppling när en bokning inte kan slutföras, så att jag vet vad som behöver åtgärdas.

#### Acceptanskriterier

1. OM ett fel inträffar vid skapandet av ett enskilt Zoom-möte i en grupp (läge B eller C), DÅ SKALL *ÄF* registrera felet per person utan att avbryta övriga i gruppen.
2. NÄR en bokning har bearbetats, SKALL *ÄF* kunna redovisa vilka Zoom-möten som skapades och vilka som misslyckades.
3. NÄR ett fel loggas, SKALL *ÄF* utelämna credentials och tokens ur loggarna.

## Öppna frågor

Dessa behöver utredas och kan påverka estimatet väsentligt:

- **Q1 (Auth)**: Bekräfta att Server-to-Server OAuth gäller. Vilket Zoom-konto/användare äger mötena? Krävs delegering per handläggare?
- **Q2 (Privat läge)**: Exakt vilka Zoom-inställningar utgör "privat läge"? (t.ex. väntrum på, lösenkod, kräver autentisering, ej publikt listad, join-before-host av). Dessa behöver specificeras konkret.
- **Q3 (Lägesval)**: Logiken som väljer läge A/B/C ligger i ÄF. Behöver ÄF-koden ändras för att välja läge, eller är valet redan givet när den nya funktionen anropas?
- **Q4 (Outlook)**: Hur bokar ÄF Outlook-möten idag (Graph, EWS, annat)? Kan Zoom-länkar infogas i den befintliga bokningen, eller krävs en ny väg?
- **Q5 (Grupp/roller)**: Hur levereras gruppens personer och roller (vuxen/barn) till den nya funktionen? Är individnummer alltid tillgängliga?
- **Q6 (Mötesinställningar)**: Ska duration, väntrum, inspelning m.m. sättas centralt (som i prototypens Meeting_Defaults) även här?
- **Q7 (Återskrivning)**: Ska resultatet (länkar/id:n) skrivas tillbaka till ÄF eller endast till Outlook-mötet?

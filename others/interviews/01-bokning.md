# Del 1 – Planering och bokning

> Status: arbetsutkast  
> Syfte med dokumentet: krav- och utvecklingsunderlag för en första implementation.  
> Princip: krav och öppna frågor prioriteras framför detaljerad implementation.

## AI-instruktioner

Du arbetar med **Del 1 – Planering och bokning** i en lösning för att planera och boka intervjuer.

1. Denna del ska kunna utvecklas relativt självständigt från Del 2.
2. Microsoft Graph används som huvudsakligt gränssnitt mot Microsoft 365/Outlook där kalender- och resursinformation behövs.
3. Personuppslag och personalurval ska behandlas som en separat integrationsfråga. Tre alternativ för AD/Entra-hantering ska kunna utvärderas utan att resten av lösningen låses till ett av dem.
4. Bokningen ska kunna avse **en individ eller en grupp av individer**.
5. En bokning kan dessutom innehålla stödpersoner och en tolk. Tolken hämtas från ett annat internt system.
6. Del 1 ansvarar för att skapa ett komplett och entydigt underlag för genomförandet.
7. Del 2 ska inte behöva känna till hur tider, resurser, personal, stödpersoner eller tolk hittades.
8. Ändringar i gränssnittet mellan Del 1 och Del 2 ska dokumenteras och versionshanteras.
9. Gör inte antaganden om verksamhetsregler som inte finns i krav eller öppna frågor.
10. Prioritera spårbarhet, behörighet, felhantering och tydliga integrationer framför teknisk finess.

## Krav

| ID | Krav | Prioritet | Status | Kommentar |
|---|---|---|---|---|
| B-001 | Användaren ska kunna ange gruppnummer. | MUST | Öppet | |
| B-002 | Användaren ska kunna ange ärendetyp. Exempel i mockup: `FS`. | MUST | Öppet | Värden ska fastställas med verksamheten. |
| B-003 | Användaren ska kunna ange intervjutyp. Exempel: `Sakintervju`. | MUST | Öppet | |
| B-004 | Användaren ska kunna välja om bokningen gäller en individ eller en grupp av individer. | MUST | Öppet | Viktig grundskillnad i bokningsflödet. |
| B-005 | Användaren ska kunna lägga till en eller flera individer i en gruppbokning. | MUST | Öppet | |
| B-006 | Användaren ska kunna lägga till stödperson(er). | MUST | Öppet | Verksamheten behöver definiera reglerna. |
| B-007 | Användaren ska kunna lägga till tolk. | MUST | Öppet | Tolk hämtas från separat internt system. |
| B-008 | Applikationen ska kunna hitta tillgängliga tider för relevanta personer och resurser. | MUST | Öppet | Microsoft Graph kan användas för kalender/free-busy. |
| B-009 | Applikationen ska kunna hantera lokal och eventuell utrustning som bokningsresurs. | MUST | Öppet | |
| B-010 | Applikationen ska kunna föreslå ett eller flera bokningsalternativ. | MUST | Öppet | Urvalskriterier fastställs med verksamheten. |
| B-011 | Användaren ska kunna justera ett föreslaget schema innan bokning. | SHOULD | Öppet | |
| B-012 | Vid godkänd bokning ska kalenderhändelser skapas eller uppdateras i Microsoft 365/Outlook. | MUST | Öppet | |
| B-013 | Varje intervju som kräver separat Zoom-möte ska få ett eget Meeting ID. | MUST | Öppet | |
| B-014 | Del 1 ska kunna skapa och registrera kopplingen mellan intervju och Zoom-möte. | MUST | Öppet | |
| B-015 | Del 1 ska producera ett genomförandepaket enligt kontraktet mot Del 2. | MUST | Öppet | |
| B-016 | Del 1 ska kunna rapportera partiella fel utan att hela bokningen förlorar sin status. | SHOULD | Öppet | Exakt beteende behöver definieras. |
| B-017 | Alla relevanta bokningsbeslut ska kunna spåras. | SHOULD | Öppet | Vem, när, vad och resultat. |

## Integrationer

### Microsoft Graph / Outlook

Microsoft Graph ska vara integrationsgränssnittet mot Microsoft 365. Exakt behörighetsmodell fastställs i designfasen.

### Zoom

Del 1 ska kunna:
- skapa Zoom-möten,
- få tillbaka Meeting ID och mötesinformation,
- koppla varje möte till rätt intervju,
- lämna relevant information vidare till Del 2.

Exakta Zoom-API-anrop och autentiseringsmodell fastställs separat.

### Personal / AD / Entra ID

Tre arkitekturalternativ ska utvärderas.

**Alternativ A – Entra ID som katalog för applikationen**

```text
Vår applikation
      |
      v
Microsoft Graph
      |
      v
Microsoft Entra ID
```

**Alternativ B – Graph/Entra + intern kompletteringstjänst**

```text
Vår applikation
      |
      +----> Microsoft Graph / Entra ID
      |
      +----> Intern katalog-/personaltjänst
```

**Alternativ C – Graph för Microsoft 365 + intern AD-tjänst**

```text
Vår applikation
      |
      +----> Microsoft Graph
      |
      +----> Intern AD-/katalogtjänst
                    |
                    v
                   AD
```

Applikationen bör inte behöva prata direkt med lokal AD om en intern tjänst kan kapsla den integrationen.

### Tolksystem

Tolken ska hämtas från ett separat internt system.

```text
Vår applikation
      |
      v
Tolkintegration
      |
      v
Internt tolksystem
```

## Genomförandekontrakt mot Del 2

Del 1 ska lämna över ett maskinläsbart **genomförandepaket**.

JSON rekommenderas som dataformat för kontraktet.

Exempel på preliminär struktur:

```json
{
  "contractVersion": "0.1",
  "groupNumber": "20260012",
  "caseType": "FS",
  "interviewType": "Sakintervju",
  "bookingMode": "group",
  "participants": [
    {
      "sequence": 1,
      "personId": "person-001",
      "name": "Anna Andersson",
      "role": "individual",
      "supportPersons": [],
      "interpreter": null
    }
  ],
  "interviews": [
    {
      "sequence": 1,
      "personId": "person-001",
      "scheduledStart": "2026-09-18T09:00:00",
      "scheduledEnd": "2026-09-18T09:45:00",
      "locationId": "room-03",
      "interviewerId": "user-001",
      "zoom": {
        "meetingId": "123456789",
        "joinUrl": "..."
      }
    }
  ]
}
```

Detta är ett diskussionsunderlag, inte en fastställd datamodell.

### Kontraktskrav

| ID | Krav | Prioritet |
|---|---|---|
| B-020 | Kontraktet ska ha versionsnummer. | MUST |
| B-021 | Varje intervju ska ha en stabil ordnings-/intervjuidentifierare. | MUST |
| B-022 | Gruppnummer, ärendetyp och intervjutyp ska följa med. | MUST |
| B-023 | Person, stödperson(er) och tolk ska kunna representeras. | MUST |
| B-024 | Kalenderinformation ska kunna representeras. | MUST |
| B-025 | Zoom Meeting ID ska kunna kopplas till rätt intervju. | MUST |
| B-026 | Kontraktet ska kunna valideras innan Del 2 startas. | SHOULD |

## Konfiguration kontra kontrakt

**JSON:** använd primärt för data som skickas mellan Del 1 och Del 2.

**YAML/JSON-konfiguration:** använd för teknisk konfiguration, exempelvis miljö, URL:er, feature flags och icke-verksamhetskritiska standardvärden.

Blanda inte dessa två begrepp i implementationen.

## Öppna verksamhetsfrågor

| ID | Fråga | Status | Kommentar |
|---|---|---|---|
| B-Q01 | Vad skiljer en individbokning från en gruppbokning i verksamhetsreglerna? | Öppen | |
| B-Q02 | När ska stödperson automatiskt föreslås eller krävas? | Öppen | |
| B-Q03 | Kan flera stödpersoner kopplas till samma individ? | Öppen | |
| B-Q04 | Hur väljs tolk? | Öppen | |
| B-Q05 | Ska tolkens tillgänglighet ingå i bokningsalgoritmen? | Öppen | |
| B-Q06 | Vilka attribut behövs från personalkatalogen? | Öppen | |
| B-Q07 | Vilka personkategorier får användaren söka efter? | Öppen | |
| B-Q08 | Vilka resurser måste alltid vara med i tillgänglighetskontrollen? | Öppen | |
| B-Q09 | Ska bokning ske som en transaktion eller kunna lämna ett delvis bokat läge? | Öppen | |
| B-Q10 | Vad händer om ett Zoom-möte kan skapas men Outlook-bokningen misslyckas? | Öppen | |
| B-Q11 | Vad händer om Outlook-bokningen lyckas men Zoom-mötet misslyckas? | Öppen | |
| B-Q12 | Vad händer om någon manuellt ändrar en Outlook-bokning efteråt? | Öppen | |
| B-Q13 | Vilken komponent är master för bokningens status? | Öppen | |

## Acceptanskriterier – första version

| ID | Acceptanskriterium | Status |
|---|---|---|
| B-A01 | En användare kan skapa ett bokningsunderlag för en individ. | Öppet |
| B-A02 | En användare kan skapa ett bokningsunderlag för flera individer. | Öppet |
| B-A03 | Stödperson kan representeras. | Öppet |
| B-A04 | Tolk kan representeras och hämtas via definierad integration. | Öppet |
| B-A05 | Tillgänglighet för relevanta personer/resurser kan hämtas. | Öppet |
| B-A06 | Ett föreslaget schema kan presenteras. | Öppet |
| B-A07 | Godkänd bokning skapar kalenderhändelser. | Öppet |
| B-A08 | Relevanta Zoom-möten skapas. | Öppet |
| B-A09 | Ett validerbart genomförandepaket kan lämnas till Del 2. | Öppet |

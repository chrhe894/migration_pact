# Case Lifecycle

## Syfte

Detta dokument beskriver hur ett asylärende fortskrider genom EU:s migrations- och asylpakt — från att en person söker skydd till slutligt utfall.

Det fungerar som primär navigationshjälp för nya läsare.

---

## Översikt

```text
Person söker skydd
        │
        ▼
┌─────────────────────────────────────────┐
│  SCREENING (7 dagar)                    │
│  Identifiering, hälsa, sårbarhet,       │
│  säkerhet, screeningformulär            │
└─────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────┐
│  REGISTRATION (5 dagar)                 │
│  Ansökan registreras formellt           │
│  Registreringshandling utfärdas         │
│  Eurodac-registrering (72h)             │
└─────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────┐
│  INLÄMNANDE (21 dagar / 5 vid gräns)   │
│  Ansökan lämnas in personligen          │
│  Sökandehandling utfärdas               │
└─────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────┐
│  ANSVARSBEDÖMNING                       │
│  Vilken stat prövar ansökan?            │
│  Kriterierna tillämpas i rangordning    │
│  Ev. överföring till annan stat         │
└─────────────────────────────────────────┘
        │
        ├─────────────────────────────┐
        ▼                             ▼
┌──────────────────┐   ┌──────────────────────────┐
│  REGULJÄRT       │   │  GRÄNSFÖRFARANDE         │
│  FÖRFARANDE      │   │  (12 veckor)             │
│  (6 månader)     │   │  Vid gränsen, ingen      │
│  På territoriet  │   │  inresa tillåts          │
└──────────────────┘   └──────────────────────────┘
        │                             │
        ▼                             ▼
┌──────────────────────────────────────────┐
│  BESLUT                                  │
│                                          │
│  ✓ Flyktingstatus                        │
│  ✓ Subsidiärt skydd                      │
│  ✗ Avslag → Återvändande                 │
└──────────────────────────────────────────┘
```

---

## Domäner och deras plats i livscykeln

| Steg | Domän | Förordning | Tidsfrist |
|------|-------|------------|-----------|
| 1. Screening | [Screening](domains/screening/README.md) | Screeningförordningen | 7 dagar (3 inom territoriet) |
| 2. Registrering | [Registration](domains/registration/README.md) | APR art. 27 | 5 dagar (15 vid massinflöde) |
| 3. Biometri | [Eurodac](domains/eurodac/README.md) | Eurodacförordningen | 72 timmar |
| 4. Inlämnande | [Registration](domains/registration/README.md) | APR art. 28 | 21 dagar (5 vid gräns) |
| 5. Ansvarsbedömning | [Responsibility](domains/responsibility/README.md) | AMMR art. 24–46 | 2 mån + 1 mån + 6 mån |
| 6a. Reguljärt förfarande | [Asylum Procedure](domains/asylum-procedure/README.md) | APR art. 34–42 | 6 månader |
| 6b. Gränsförfarande | [Border Procedure](domains/border-procedure/README.md) | APR art. 43–54 | 12 veckor |
| 7. Återvändande vid gräns | [Return Border](domains/return-border-procedure/README.md) | Förordning 2024/1349 | 12 veckor |

---

## Stödsystem

| System | Domän | Funktion |
|--------|-------|----------|
| Solidaritet | [Solidarity](domains/solidarity/README.md) | Omfördelning vid tryck |
| Krishantering | [Crisis](domains/crisis/README.md) | Undantag vid kris |

---

## Diagram

<object type="image/svg+xml" data="diagrams/end-to-end-overview.svg" width="100%"></object>

Källa: [`end-to-end-overview.pu`](diagrams/end-to-end-overview.pu)

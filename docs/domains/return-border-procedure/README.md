
# Återvändande vid gräns

## Syfte

Domänen beskriver förordning (EU) 2024/1349 om **gränsförfarandet för återvändande**. Förfarandet tillämpas efter att en asylansökan avslagits i gränsförfarandet för asyl ([APR art. 43–54](../border-procedure/README.md)).

Förfarandet säkerställer att personer vars ansökan avslagits i gränsförfarandet inte tillåts resa in på territoriet. I stället ska återvändandet genomföras inom högst tolv veckor, och därefter fortsätta enligt återvändandedirektivet 2008/115/EG om det inte hunnits med. Förordningen tillämpas från och med den 12 juni 2026.

---

## Plats i livscykeln

| | |
|---|---|
| **Föregående** | [Gränsförfarande](../border-procedure/README.md) (avslag i gränsförfarandet för asyl) |
| **Nästa** | Verkställt återvändande, eller fortsatt återvändande enligt direktiv 2008/115/EG |
| **Inträde** | Avslag i gränsförfarandet för asyl, och personen har inte längre rätt att stanna kvar |
| **Utträde** | Personen har återvänt, eller tolvveckorsperioden har löpt ut |

---

## Primära rättskällor

| Artikel | Rubrik |
|---------|--------|
| [1](articles/return-001.md) | Innehåll och tillämpningsområde |
| [2](articles/return-002.md) | Hänvisningar till förordning (EU) 2024/1348 |
| [3](articles/return-003.md) | Definitioner |
| [4](articles/return-004.md) | Gränsförfarande för återvändande (12 veckor, frivillig avresa) |
| [5](articles/return-005.md) | Förvar |
| [6](articles/return-006.md) | Åtgärder i krissituation (+6 veckor) |
| [7](articles/return-007.md) | Förfaranderegler |
| [8](articles/return-008.md) | Särskilda bestämmelser och garantier |
| [11](articles/return-011.md) | Beräkning av tidsfrister |

Art. 9 (ändringar av förordning 2021/1148), 10 (överklagande från offentliga myndigheter), 12 (övergångsbestämmelser: nationella genomförandeplaner klara senast den 1 juli 2026), 13 (utvärdering) och 14 (ikraftträdande) har inga egna kort. Förordningstexten finns i `references/_text/OJ_L_202401349_SV_TXT.txt`.

> **Rättelse (granskning 2026-09):** domänens artikelkort var numrerade fel. Bara kortet för art. 3 stämde. Domänen påstod också att personen tillåts resa in om återvändandet inte verkställts inom tolv veckor, och att fristen fryses vid överklagande. Båda påståendena är felaktiga. Kort, regler, krav, process och diagram är nu kontrollerade mot förordningstexten.

---

## Processer

| Process | Beskrivning |
|---------|-------------|
| [PROC-RET-001 Gränsförfarande för återvändande](processes/return-border-procedure.md) | Från avslag i gränsförfarandet för asyl till verkställt återvändande, eller fortsättning enligt återvändandedirektivet |

---

## Juridiska milstolpar

```text
Avslag i gränsförfarandet för asyl
        │
        ▼
Ingen inresa (art. 4.1)
        │
        ├── Rätt att stanna kvar under överklagande? → perioden har inte börjat
        │
        ▼
Rätten att stanna kvar upphör → tolvveckorsperioden börjar (art. 4.2)
        │
        ├── Förvar som sista utväg (art. 5)
        ├── Frivillig avresa på begäran, högst 15 dagar (art. 4.5)
        ├── Kris: +högst 6 veckor (art. 6)
        │
        ▼
Återvändande verkställt
   eller
Fortsatt återvändande enligt direktiv 2008/115/EG (art. 4.4)
```

---

## Begrepp

| ID | Begrepp |
|----|---------|
| [CON-RET-001](concepts/return-border-procedure-concept.md) | Gränsförfarande för återvändande |
| [CON-RET-002](concepts/voluntary-departure.md) | Frivillig avresa |

---

## Regler

| Regel | Beskrivning |
|-------|-------------|
| [RULE-RET-004-001](rules/rule-ret-004-001.md) | Ingen inresa efter avslag i gränsförfarandet för asyl |
| [RULE-RET-004-002](rules/rule-ret-004-002.md) | Tolvveckorsperioden och fortsättning enligt återvändandedirektivet |
| [RULE-RET-004-003](rules/rule-ret-004-003.md) | Frivillig avresa högst 15 dagar |
| [RULE-RET-005-001](rules/rule-ret-005-001.md) | Förvar som sista utväg, högst tolv veckor |
| [RULE-RET-006-001](rules/rule-ret-006-001.md) | Förlängning med högst sex veckor vid kris |
| [RULE-RET-011-001](rules/rule-ret-011-001.md) | Fristberäkning |

> **Ändrat regel-ID:** RULE-RET-005-001 avsåg tidigare tolvveckorsperioden och avser nu förvar. Tolvveckorsperioden finns som RULE-RET-004-002.

---

## Tolkningar

| Fil | Frågeställning |
|-----|----------------|
| [return-vs-regular-return](interpretations/return-vs-regular-return.md) | Skillnaden mot det ordinarie återvändandedirektivet |

---

## Öppna frågor

| Fil | Fråga |
|-----|-------|
| [non-removable-persons](open_questions/non-removable-persons.md) | Vad händer med personer som inte kan avlägsnas inom tolv veckor? |

---

## Delade moduler

| Modul | Länk |
|-------|------|
| Time limits | [shared/time-limits](../../shared/time-limits/README.md) |

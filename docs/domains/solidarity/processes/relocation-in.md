---
tags:
  - omfördelning
  - solidaritet
  - process
  - omfördelning-in
---

← [Omfördelning (översikt)](relocation.md)

# PROC-SOL-003

# Omfördelning IN

## Perspektiv

Sverige är **omfördelningsmedlemsstat**: en bidragande stat som **tar emot** personer från en gynnad medlemsstat. Motsvarande avsändarperspektiv beskrivs i [Omfördelning UT](relocation-out.md).

## Trigger

Den gynnade staten har översänt uppgifter och handlingar om en person som ska omfördelas ([art. 67.7](../articles/ammr-067.md)).

---

## Resultat

Personen har tagits emot och omfördelningsmedlemsstaten har blivit ansvarig stat, eller omfördelningen har avslagits på grund av hot mot den inre säkerheten.

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/relocation-in.svg" width="100%"></object>

Källa: [`relocation-in.pu`](../diagrams/relocation-in.pu)

---

## Steg i den mottagande statens flöde

| Steg | Vad staten gör | Källa |
|------|----------------|-------|
| 1 | Tar emot uppgifter och handlingar. **Klockan på 1 vecka startar** | [art. 67.7, 67.9](../articles/ammr-067.md) |
| 2 | Granskar uppgifterna och kontrollerar att det inte finns rimliga skäl att anse personen som **hot mot den inre säkerheten**. Får göra en personlig intervju inom tidsfristerna | [art. 67.8](../articles/ammr-067.md) |
| 3 | Bekräftar att personen kommer att omfördelas, eller underrättar om hot | [art. 67.9](../articles/ammr-067.md) |
| 4 | Ombesörjer lämpliga ankomstarrangemang | [art. 67.9](../articles/ammr-067.md) |
| 5 | Underrättar den gynnade staten, asylbyrån och EU-solidaritetssamordnaren om ankomst eller utebliven ankomst | [art. 68.1](../articles/ammr-068.md) |
| 6 | Översänder personens Eurodac-dataset med ankomstdatum | [Eurodac art. 25.2](../../eurodac/articles/eur-025.md) |
| 7 | Fastställer ansvar och anger det i Eurodac | [art. 68.2–68.3](../articles/ammr-068.md), [Eurodac art. 16.1, 16.3](../../eurodac/articles/eur-016.md) |
| 8 | Beviljar skyddsstatus automatiskt om personen hade internationellt skydd | [art. 68.4](../articles/ammr-068.md), [Eurodac art. 31.6](../../eurodac/articles/eur-031.md) |

## Alternativa flöden

### Hot mot den inre säkerheten (p. 9)

Bekräftar kontrollerna rimliga skäl att anse personen som hot mot den inre säkerheten, ska omfördelningsmedlemsstaten **inom en vecka** (högst två veckor, se nedan) underrätta den gynnade staten om arten av och de underliggande faktorerna till en registrering i en relevant databas. Personen **omfördelas inte**.

### Särskilt komplicerad granskning (p. 9 tredje st.)

Om granskningen är särskilt komplicerad, eller ett stort antal ärenden behöver kontrolleras samtidigt, får svaret lämnas efter veckan men **inom två veckor**. Beslutet att skjuta upp svaret måste meddelas den gynnade staten **inom den ursprungliga veckan**.

### Tyst bekräftelse (p. 9 fjärde st.)

Underlåtenhet att agera inom en vecka (eller två veckor vid uppskjutande) räknas som **bekräftelse** och medför skyldighet att omfördela personen, inklusive att ombesörja lämpliga ankomstarrangemang.

### Ansvar vid omfördelning (art. 68.2–68.3)

| Läge | Följd |
|------|-------|
| Sökande för vilken ansvarig stat **ännu inte fastställts** | Omfördelningsmedlemsstaten tillämpar förfarandena i del III (utom art. 16.2, 17.1, 17.2, 25.5, 29, 30, 33.1 och 33.2). Kan ingen ansvarig stat fastställas är omfördelningsmedlemsstaten ansvarig för prövningen. Ansvaret anges i Eurodac (art. 16.1) |
| Sökande för vilken den **gynnade staten tidigare fastställts som ansvarig** (av andra skäl än art. 67.5 andra st.) | Ansvaret övergår till omfördelningsmedlemsstaten. Det gäller även ytterligare framställningar och efterföljande ansökan enligt [APR art. 55](../../asylum-procedure/articles/apr-055.md) och [56](../../asylum-procedure/articles/apr-056.md). Ansvaret anges i Eurodac (art. 16.3) |
| Person med **internationellt skydd** | Omfördelningsmedlemsstaten beviljar automatiskt motsvarande skyddsstatus (art. 68.4) |

### Gränsförfarande efter omfördelning

En omfördelad sökande kan hänvisas till gränsförfarande i omfördelningsmedlemsstaten ([APR art. 43.1 d](../../border-procedure/articles/apr-043.md)).

---

## Tidsfrister

| Steg | Frist | Startar | Källa |
|------|-------|---------|-------|
| **Besked** (bekräftelse eller hot) | **1 vecka** | Mottagandet av informationen från den gynnade staten | [art. 67.9](../articles/ammr-067.md) |
| Besked vid särskilt komplicerad granskning | Högst **2 veckor**. Uppskjutandet meddelas inom den första veckan | Mottagandet av informationen | [art. 67.9](../articles/ammr-067.md) |
| Underlåtenhet att agera | Räknas som **bekräftelse** | Fristens utgång | [art. 67.9](../articles/ammr-067.md) |
| Underrättelse om ankomst eller utebliven ankomst | Ingen frist angiven. Avser "den fastställda tidsfristen" | — | [art. 68.1](../articles/ammr-068.md) |

Besked-fristen startar vid **mottagandet av begäran**, inte vid en accept, och är därför inte en instans av ATB, ATÖ, TNO eller TGÖ. De efterföljande stegen (beslut 1 vecka, överföring 4 veckor) ligger hos den gynnade staten, se [Omfördelning UT](relocation-out.md) och [fristtyperna](../../../shared/time-limits/README.md).

### Koppling till statistik

| Datapunkt | Betydelse | Källa |
|-----------|-----------|-------|
| Tid från mottagande till besked | Efterlevnad av 1-veckorsfristen | Nationell statistik |
| Antal bekräftade, avslagna (hot) och tysta bekräftelser | Uppföljning av art. 67.9 | Nationell statistik |
| Bidragsandel per stat | Uppföljning mot referensnyckel och utfästelser | EU-rapporter |
| Antal ankomna och uteblivna | Underlag för underrättelse enligt art. 68.1 | Nationell statistik |

---

## Juridiska milstolpar

- Uppgifter mottagna från den gynnade staten
- Granskning genomförd
- Bekräftelse (uttrycklig eller tyst) eller hotbesked
- Person ankommen, eller utebliven ankomst anmäld
- Ansvar fastställt och angivet i Eurodac

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Person hos den gynnade staten | Bekräftelse + ankomst | Person hos omfördelningsmedlemsstaten, ansvar övergått eller fastställt (art. 68) |

---

## Regler

- [RULE-AMMR-067-001](../rules/rule-ammr-067-001.md) — Förfarande inför omfördelning
- [RULE-AMMR-057-001](../rules/rule-ammr-057-001.md) — Skyldighet att bidra
- [RULE-AMMR-063-001](../rules/rule-ammr-063-001.md) — Ansvarskompensation (separat spår, se översikten)

---

## Öppna frågor

- Art. 68.1 anger inte vad som händer när en person inte infunnit sig inom den fastställda tidsfristen, eller vem som då är ansvarig.

---

## Se även

- [Omfördelning UT](relocation-out.md)
- [Omfördelning (översikt)](relocation.md)

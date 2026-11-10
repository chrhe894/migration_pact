---
tags:
  - omfördelning
  - solidaritet
  - process
  - omfördelning-ut
---

← [Omfördelning (översikt)](relocation.md)

# PROC-SOL-002

# Omfördelning UT

## Perspektiv

Sverige är **gynnad medlemsstat** (i repot även kallad förmånsstat): en stat som är utsatt för migrationstryck och som **skickar** personer vidare till en annan medlemsstat. Motsvarande mottagarperspektiv beskrivs i [Omfördelning IN](relocation-in.md).

## Trigger

Solidaritetspoolen har aktiverats ([RULE-AMMR-057-001](../rules/rule-ammr-057-001.md)) och den gynnade staten ska genomföra omfördelning av personer enligt [art. 56.2 a](../articles/ammr-056.md).

---

## Resultat

Personen har överförts till omfördelningsmedlemsstaten, eller förfarandet har avslutats utan omfördelning (hot mot den inre säkerheten, personen inte berättigad).

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/relocation-out.svg" width="100%"></object>

Källa: [`relocation-out.pu`](../diagrams/relocation-out.pu)

---

## Steg i den gynnade statens flöde

Alla punkter avser [AMMR art. 67](../articles/ammr-067.md) om inget annat anges.

| Steg | Vad staten gör | Punkt |
|------|----------------|-------|
| 1 | Kontrollerar att det inte finns rimliga skäl att anse personen som **hot mot den inre säkerheten**, före och under förfarandet | 2 |
| 2 | Identifierar personer som kan omfördelas (asylbyrån kan stödja identifiering och matchning) | 3 |
| 3 | Beaktar meningsfulla kopplingar (familj, kultur). Personen får lämna information om detta men har **ingen rätt att välja** stat | 3 |
| 4 | Fördelar personer utan koppling rättvist mellan övriga omfördelningsmedlemsstater | 4 |
| 5 | Ser till att **familjemedlemmar** omfördelas till samma stat | 6 |
| 6 | Inhämtar **skriftligt samtycke** om personen har beviljats internationellt skydd | 4 |
| 7 | Informerar personen om förfarandet i art. 67 och 68 | 5 |
| 8 | Översänder uppgifter och handlingar till omfördelningsmedlemsstaten med standardformulär, **så snart som möjligt** | 7 |
| 9 | Uppdaterar Eurodac-datasetet med uppgift om omfördelningsmedlemsstaten när den är skyldig att ta emot personen ([Eurodac art. 25.1](../../eurodac/articles/eur-025.md)) | — |
| 10 | Fattar beslut om överföring | 10 |
| 11 | Underrättar personen skriftligen | 10 |
| 12 | Verkställer överföringen | 11 |

## Alternativa flöden

### Hot mot den inre säkerheten före eller under förfarandet (p. 2)

Den gynnade staten ska inte tillämpa förfarandet, eller avsluta det omedelbart. Personen **utesluts från all framtida omfördelning eller överföring** till en medlemsstat. Om personen ansöker om internationellt skydd är den gynnade staten ansvarig enligt [AMMR art. 16.4](../../../references/legislation/ammr.md).

### Omfördelningsmedlemsstaten meddelar hot (p. 9)

Om omfördelningsmedlemsstatens kontroller bekräftar rimliga skäl att anse personen som hot mot den inre säkerheten, ska personen **inte omfördelas**. Art. 67 anger ingen följd utöver det, och kopplar inte detta till ansvarskompensation.

### Sökande för vilka den gynnade staten är ansvarig (p. 5)

Sökande för vilka den gynnade staten kan fastställas som ansvarig enligt kriterierna i [art. 25](../../responsibility/articles/ammr-025.md)–[28](../../responsibility/articles/ammr-028.md) och [34](../../responsibility/articles/ammr-034.md) (utom art. 25.5) är **inte berättigade** till omfördelning, och informationsskyldigheten i p. 5 gäller inte dem.

### Personer med internationellt skydd (p. 4, 13)

Omfördelning kräver personens skriftliga samtycke. Vid verkställd överföring ska den gynnade staten även översända information enligt [art. 51.2](../../responsibility/articles/ammr-051.md), vad personen åberopat och skälen för tidigare beslut.

### Rättsmedel (p. 13)

[Art. 43](../../responsibility/articles/ammr-043.md) gäller i tillämpliga delar (tillsammans med art. 42.3–42.5, 44, 46.1, 46.3, 47.2, 47.3, 48 och 50). Överklagande med suspensiv verkan flyttar startpunkten för överföringsfristen till det slutliga beslutet (p. 11).

---

## Tidsfrister

| Steg | Frist | Startar | Fristtyp | Källa |
|------|-------|---------|----------|-------|
| Översända uppgifter | Så snart som möjligt | — | — | [art. 67.7](../articles/ammr-067.md) |
| **Beslut om överföring** | **1 vecka** | Omfördelningsmedlemsstatens bekräftelse | Motsvarar [ATB](../../../shared/time-limits/concepts/fristtyp-accept-till-beslut.md) | [art. 67.10](../articles/ammr-067.md) |
| **Underrättelse till personen** | Utan dröjsmål, senast **2 dagar** före överföring (sökande) / **1 vecka** före (skyddade) | Räknas **baklänges** från överföringen | — | [art. 67.10](../articles/ammr-067.md) |
| **Verkställd överföring** | **4 veckor** | Bekräftelsen, eller det slutliga beslutet vid överklagande med suspensiv verkan | [ATÖ](../../../shared/time-limits/concepts/fristtyp-accept-till-overforing.md) | [art. 67.11](../articles/ammr-067.md) |
| Koordinering av genomförandet | Se TGÖ | Efter överföringsbeslutet | [TGÖ](../../../shared/time-limits/concepts/fristtyp-transfer-genomforande-overforing.md) | Genomförandeförordning 2025/2055 |

Underrättelsen om överföringen är en varseltid, inte en frist att utföra något *inom*, och ingår därför inte i den allmänna regeln om minst två arbetsdagar (se [Tidsfrister](../../../shared/time-limits/README.md)).

Art. 67 och 68 anger inte uttryckligen vad som händer om fyraveckorsfristen överskrids. Art. 68.1 behandlar utebliven ankomst, se [Omfördelning IN](relocation-in.md).

### Koppling till statistik

| Datapunkt | Betydelse | Källa |
|-----------|-----------|-------|
| Antal identifierade och överförda | Volymuppföljning mot utfästelser i solidaritetspoolen | Nationell statistik |
| Genomsnittlig överföringstid | Tidseffektivitet mot 4-veckorskravet | Nationell statistik |
| Antal som utesluts på grund av hot (p. 2) | Uppföljning av undantaget | Nationell statistik |

---

## Juridiska milstolpar

- Solidaritetspool aktiverad
- Säkerhetskontroll genomförd
- Person identifierad och informerad
- Uppgifter översända
- Omfördelningsmedlemsstatens bekräftelse mottagen
- Överföringsbeslut fattat
- Överföring verkställd

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Person i den gynnade staten | Överföring verkställd | Person hos omfördelningsmedlemsstaten, ansvar enligt [art. 68](../articles/ammr-068.md) (se [Omfördelning IN](relocation-in.md)) |

---

## Regler

- [RULE-AMMR-057-001](../rules/rule-ammr-057-001.md) — Skyldighet att bidra
- [RULE-AMMR-067-001](../rules/rule-ammr-067-001.md) — Förfarande inför omfördelning

---

## Se även

- [Omfördelning IN](relocation-in.md)
- [Omfördelning (översikt)](relocation.md)
- [Fristtyp ATÖ](../../../shared/time-limits/concepts/fristtyp-accept-till-overforing.md)

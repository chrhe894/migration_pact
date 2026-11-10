---
tags:
  - omfördelning
  - solidaritet
  - process
---


# PROC-SOL-001

# Omfördelning (översikt)

## Trigger

En medlemsstat har konstaterats vara utsatt för migrationstryck och solidaritetspoolen har aktiverats.

---

## Resultat

Sökande eller person med internationellt skydd har omfördelats till en bidragande stat som tar emot personen och blir ansvarig enligt [art. 68](../articles/ammr-068.md).

---

## Två flöden: UT och IN

Omfördelning ser olika ut beroende på om staten **skickar** eller **tar emot**. Rollerna har olika steg, olika frister och olika skyldigheter, och därför finns ett flöde per roll.

| Flöde | Staten är | AMMR-term | Process | Kärnan |
|-------|-----------|-----------|---------|--------|
| **UT** | Utsatt stat som skickar | Gynnad medlemsstat (i repot även förmånsstat) | [PROC-SOL-002 Omfördelning UT](relocation-out.md) | Kontrollera hot, identifiera, översända uppgifter, besluta om och verkställa överföring |
| **IN** | Bidragande stat som tar emot | Omfördelningsmedlemsstat | [PROC-SOL-003 Omfördelning IN](relocation-in.md) | Granska, bekräfta eller meddela hot, ombesörja ankomst, fastställa ansvar |

---

## Samspel

<object type="image/svg+xml" data="../diagrams/relocation.svg" width="100%"></object>

Källa: [`relocation.pu`](../diagrams/relocation.pu)

---

## Tidsfrister i samspel

Fristerna ligger hos olika stater. Kolumnen *Vem* visar vilket flöde som äger fristen.

| Steg | Vem | Frist | Startar | Fristtyp | Källa |
|------|-----|-------|---------|----------|-------|
| Översända uppgifter | UT | Så snart som möjligt | — | — | [art. 67.7](../articles/ammr-067.md) |
| **Besked** (bekräftelse eller hot) | IN | **1 vecka** (undantagsvis högst 2, uppskjutande meddelas inom 1 v). Tystnad = bekräftelse | Mottagandet av informationen | Svarsfrist | [art. 67.9](../articles/ammr-067.md) |
| **Överföringsbeslut** | UT | **1 vecka** | Bekräftelsen | Motsvarar [ATB](../../../shared/time-limits/concepts/fristtyp-accept-till-beslut.md) | [art. 67.10](../articles/ammr-067.md) |
| Underrättelse till personen | UT | Senast **2 dagar** (sökande) / **1 vecka** (skyddade) före överföring | Räknas baklänges | — | [art. 67.10](../articles/ammr-067.md) |
| **Överföring verkställd** | UT | **4 veckor**. Kan frysas vid suspensiv verkan (art. 43.3) | Bekräftelsen (eller slutligt beslut) | [ATÖ](../../../shared/time-limits/concepts/fristtyp-accept-till-overforing.md) | [art. 67.11](../articles/ammr-067.md) |
| Underrätta om ankomst / utebliven ankomst | IN | Ingen frist angiven | — | — | [art. 68.1](../articles/ammr-068.md) |

---

## Alternativt flöde — hot mot den inre säkerheten

Grunden i art. 67 är **hot mot den inre säkerheten**, och den kontrolleras av båda staterna:

- **UT** ska säkerställa att det inte finns rimliga skäl att anse personen som hot innan förfarandet tillämpas (p. 2). Finns det, avslutas förfarandet och personen utesluts från all framtida omfördelning eller överföring.
- **IN** granskar uppgifterna (p. 8). Bekräftas hotet, underrättar IN den gynnade staten inom en vecka och personen omfördelas inte (p. 9).

Art. 67 kopplar inte detta till ansvarskompensation.

---

## Separat spår — ansvarskompensation

Ansvarskompensation ([art. 63](../articles/ammr-063.md)) är ett **eget alternativ** till omfördelning, inte en följd av en säkerhetsvägran. En bidragande stat som inte genomfört sina utfästelser eller godtagit omfördelningar enligt art. 67.9 motsvarande utfästelsen vid årets slut ska, på begäran av den gynnade staten, ta ansvar för motsvarande antal ansökningar ([art. 63.5](../articles/ammr-063.md), [RULE-AMMR-063-001](../rules/rule-ammr-063-001.md)). Någon fysisk överföring sker då inte, och ingen ATÖ-frist gäller.

---

## Juridiska milstolpar

- Migration pressure established
- Solidarity pool activated
- Omfördelning bekräftad
- Transfer completed
- Responsibility transferred

---

## Tillståndsförändringar

| Före | Åtgärd | Efter |
|------|--------|-------|
| Sökande i utsatt stat | Omfördelning | Sökande i bidragande stat, ansvar övergått |

---

## Regler

- [RULE-AMMR-057-001](../rules/rule-ammr-057-001.md) — Skyldighet att bidra
- [RULE-AMMR-063-001](../rules/rule-ammr-063-001.md) — Ansvarskompensation
- [RULE-AMMR-066-001](../rules/rule-ammr-066-001.md) — Referensnyckel
- [RULE-AMMR-067-001](../rules/rule-ammr-067-001.md) — Förfarande inför omfördelning

---

## Se även

- [Tolkning: hela omfördelningsflödet](../interpretations/relocation-flow.md)
- [Omfördelning UT](relocation-out.md)
- [Omfördelning IN](relocation-in.md)

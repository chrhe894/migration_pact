# Delat — Gallring och radering av uppgifter

## Syfte

Denna shared-modul samlar reglerna om **hur länge uppgifter om individer lagras och när de ska raderas** inom migrationspakten. Frågan är tvärgående: samma individ kan ha uppgifter i flera system med **olika lagringsregimer och olika klockor**, och raderingen kan utlösas antingen av att en tidsfrist löper ut eller av en händelse (t.ex. medborgarskap).

Modulen täcker både EU-reglerna (belagt) och de systemkonsekvenser/öppna frågor som uppstår vid nationell tillämpning (resonemang, tydligt märkt).

---

## Två parallella lagringsregimer

En central poäng: det finns **inte en** lagringstid, utan minst två som löper samtidigt för samma person.

| Regim | Vad som lagras | Startpunkt för klockan | Ordinarie lagringstid | Källa |
|-------|----------------|------------------------|------------------------|-------|
| **Asyl-akten** | Handläggningsuppgifter: intervjurapport **och ljud-/videoinspelning** (art. 14), registreringsuppgifter (art. 27), inlämningsuppgifter (art. 28) | Dagen för **slutligt beslut** | **10 år** | [APR art. 72](../../domains/asylum-procedure/articles/apr-072.md) |
| **Eurodac** | Biometriska uppgifter (fingeravtryck, ansiktsbild) | Dagen för **överföring** till Eurodac | **10 år** (asylsökande) / **5 år** (olaglig vistelse) | [Eurodac art. 29](../../domains/eurodac/articles/eur-029.md) |
| **Nationell biometri** (SE) | Migrationsverkets register över fingeravtryck/fotografier | Dagen för **registrering** | **10 år** (eller vid svenskt medborgarskap) | [Utlänningsdataförordningen 3 §](../../references/legislation/utlanningsdataforordningen.md) |

De har alltså **olika startpunkter** (slutligt beslut vs. överföring vs. registrering) och delvis olika längd. En uppgift kan behöva raderas ur det ena systemet men inte det andra vid samma tidpunkt.

---

## Fallen för radering

### Fall 1 — Ordinarie lagringstid löper ut

- **Asyl-akt:** raderas när **10 år** från det slutliga beslutet har löpt ut ([APR art. 72.1](../../domains/asylum-procedure/articles/apr-072.md)).
- **Eurodac:** raderas automatiskt när **10/5 år** från överföringen har löpt ut ([Eurodac art. 29.10](../../domains/eurodac/articles/eur-029.md)).

### Fall 2 — Radering i förtid vid medborgarskap

Detta är det fall som ofta missförstås. Medborgarskap leder till radering **tidigare** än den ordinarie fristen, inte efter den.

- **Asyl-akt:** om personen förvärvar medborgarskap i **en medlemsstat före** tioårsperiodens utgång, ska uppgifterna raderas **så snart medlemsstaten får kännedom** om det ([APR art. 72.1](../../domains/asylum-procedure/articles/apr-072.md)).
- **Eurodac:** uppgifter enligt art. 15 (asylsökande) ska raderas i förtid om personen får medborgarskap i en medlemsstat; ursprungsmedlemsstaten ska begära radering i centralsystemet utan dröjsmål ([Eurodac art. 30](../../domains/eurodac/articles/eur-030.md)).
- **Nationell biometri (SE):** uppgifter i Migrationsverkets fingeravtrycks-/fotoregister ska **alltid gallras senast när den registrerade blir svensk medborgare** ([utlänningsdataförordningen 3 §](../../references/legislation/utlanningsdataforordningen.md)).

> **"En medlemsstat", inte nödvändigtvis den lagrande:** art. 72 talar om medborgarskap i *en* medlemsstat. Medborgarskap i vilken EU-stat som helst kan alltså utlösa raderingsplikten — även om det är en annan stat än den som lagrar uppgiften.

> **Vad "8 år" egentligen är:** åttaårssiffran som ibland nämns i detta sammanhang är **inte** en lagrings-/gallringstid. Det är **huvudregelns hemvistkrav för naturalisering** — åtta års hemvist med styrkt identitet ([medborgarskapslagen 11 § första stycket 3](../../references/legislation/medborgarskapslagen.md)). Vid **oklar identitet** krävs i stället **tio år** (11 c § andra stycket). Kopplingen till gallring är indirekt: hemvisttiden leder till *medborgarskap*, och det är **medborgarskapet** som är raderingstriggern ovan — inte åttaårsgränsen i sig.

### Fall 3 — Eurodac: andra grunder för förtida radering

För vissa kategorier raderas Eurodac-uppgifter även vid **uppehållstillstånd** eller när personen **lämnat medlemsstaternas territorium** ([Eurodac art. 30.2–30.3](../../domains/eurodac/articles/eur-030.md)). Detta gäller inte asyl-aktens art. 72-regim.

---

## Exempel — medborgarskap efter 8 år

Scenariot: en sökande registreras, får avslag, och förvärvar så småningom svenskt medborgarskap efter åtta års hemvist — alltså **före** tioårsfristens utgång. Vad händer med uppgifterna i akten?

| Uppgift i ärendet | Omfattas av | Öde vid medborgarskap |
|-------------------|-------------|------------------------|
| **Ljud-/videoinspelning av intervjun** | [APR art. 14 → art. 72.1](../../domains/asylum-procedure/articles/apr-072.md) | **Raderas** i förtid, så snart medlemsstaten får kännedom om medborgarskapet |
| Registrerings- och inlämningsuppgifter | [APR art. 27/28 → art. 72.1](../../domains/asylum-procedure/articles/apr-072.md) | **Raderas** i förtid |
| Biometri i Migrationsverkets register | [Utlänningsdataförordningen 3 §](../../references/legislation/utlanningsdataforordningen.md) | **Raderas** senast när personen blir svensk medborgare |
| Biometri i Eurodac | [Eurodac art. 30](../../domains/eurodac/articles/eur-030.md) | **Raderas** i förtid |
| **Beslut och centrala ärendehandlingar** | [Arkivlagen 3 §](../../references/legislation/arkivlagstiftning.md) (bevarandehuvudregel) | **Bevaras/arkiveras** — ingen specifik gallringsregel träffar dem |

**Poängen:** två delar av *samma ärende* får motsatt öde. **Ljudinspelningen ska raderas**, medan själva **beslutet kan bevaras** för framtida rättsskipning och forskning. Det är inte "radera hela akten" — det är radera de specifikt reglerade uppgifterna och bevara resten.

> **Notera:** åttaårssiffran styr ingenting här. Det är **medborgarskapshändelsen** som triggar raderingen — hade personen blivit medborgare efter fem år hade inspelningen raderats då i stället. Åtta år är bara hemvistvillkoret för att nå medborgarskap ([medborgarskapslagen 11 §](../../references/legislation/medborgarskapslagen.md)).

Att raderingen faktiskt sker "direkt" förutsätter dock att signalen om medborgarskap når fram till det system där ljudfilen ligger — ofta en **separat medielagring** (se **Problem 4** nedan). Det är där den rättsliga skyldigheten och den tekniska verkligheten glider isär.

---

## Översikt — aktivitetsdiagram

<object type="image/svg+xml" data="diagrams/data-retention.svg" width="100%"></object>

[Öppna diagrammet i egen flik](diagrams/data-retention.svg){target=_blank} (zooma för att se hela) · Källa: [`data-retention.puml`](diagrams/data-retention.puml)

---

## GDPR gäller parallellt

Utöver de specifika lagringstiderna ska all lagring ske i enlighet med **förordning (EU) 2016/679 (GDPR)**, inbegripet principen om **ändamålsbegränsning** och **lagringsminimering** ([APR art. 72.2](../../domains/asylum-procedure/articles/apr-072.md)). GDPR kan alltså skärpa kraven ytterligare — uppgifter får inte behandlas för andra ändamål eller lagras längre än nödvändigt, även inom de tillåtna maxtiderna.

---

## Gallring vs. arkivering — två motsatta logiker

Begreppen blandas ofta ihop men betyder nästan motsatta saker:

| | **Gallring** | **Arkivering / bevarande** |
|---|---|---|
| Innebörd | Uppgifter **förstörs/raderas** | Uppgifter **bevaras** (ofta långsiktigt) |
| Syfte | Skydda individen; data finns inte kvar längre än nödvändigt | Kulturarv, insyn, rättssäkerhet |
| Drivs av | Dataskydd — [APR art. 72](../../domains/asylum-procedure/articles/apr-072.md), Eurodac art. 29–30, GDPR | Svensk arkivrätt — [arkivlagen (1990:782)](../../references/legislation/arkivlagstiftning.md), TF 2 kap. |
| Utgångspunkt | Radera när ändamålet uppfyllts | **Bevara** är huvudregel; gallring kräver stöd |

### Svensk arkivrätt i korthet

- Allmänna handlingar hos en myndighet bildar dess arkiv och **ska bevaras** — de är "en del av det nationella kulturarvet" (arkivlagen **3 §**).
- Gallring är tillåten men ska vara **föreskriven** (arkivlagen **6 § p. 5** och **10 §**); i praktiken enligt Riksarkivets föreskrifter (RA-FS) eller myndighetsspecifika gallringsbeslut.
- **Riksarkivet** är statlig arkivmyndighet och utövar tillsyn (**7–9 §§**).

### Hur konflikten löses rättsligt

EU-förordningen kräver **gallring** (radera efter 10 år / vid medborgarskap), medan svensk arkivrätt utgår från **bevarande**. Kopplingen som löser krocken finns i **arkivlagen 10 § tredje stycket**:

> "Om det finns avvikande bestämmelser om gallring av vissa allmänna handlingar i annan lag eller i förordning gäller dessa bestämmelser."

En EU-förordnings raderingskrav (art. 72, Eurodac art. 29–30) är sådana "avvikande bestämmelser" och **tar därmed över** arkivlagens bevarandehuvudregel för just de uppgifterna. Så rättsligt finns en lösning — men den förutsätter att systemen faktiskt tillämpar EU-fristerna i stället för det normala bevarandet, vilket leder till systemfrågorna nedan.

---

## Systemkonsekvenser och öppna frågor

> Avsnittet nedan är **resonemang om tillämpningen**, inte belagd rättstext. EU-reglerna ovan säger *att* radering ska ske, men inte *hur* informationen om en utlösande händelse ska nå de system som faktiskt lagrar och arkiverar. Numreringen nedan motsvarar problemmarkörerna (**Problem 1–5**) i [aktivitetsdiagrammet](diagrams/data-retention.svg).

1. **Olika klockor för samma person.** En och samma individ har uppgifter i tre regimer med olika startpunkt: asyl-akt (slutligt beslut, art. 72), Eurodac (överföring, art. 29) och nationell biometri (registrering, [utlänningsdataförordningen 3 §](../../references/legislation/utlanningsdataforordningen.md)). Samma handling kan därmed ha olika raderingsdatum, och systemet måste hålla reda på vilken klocka som gäller var.

2. **Triggern för medborgarskap saknar spridningsmekanism.** Art. 72 kräver radering "så snart medlemsstaten får kännedom", men ålägger ingen mekanism för hur den kunskapen ska nå de lagrande/arkiverande systemen. Medborgarskap beslutas i en annan process/myndighet ([medborgarskapslagen](../../references/legislation/medborgarskapslagen.md)) och signalen måste spridas till asyl-akt, Eurodac **och** biometriregistret. Detta är kärnproblemet.

3. **Gränsöverskridande fall är särskilt svårt.** Eftersom medborgarskap i *vilken* MS som helst utlöser plikten, skulle t.ex. ett medborgarskapsbeslut i en annan medlemsstat behöva nå fram till det svenska lagringssystemet — något som inte är reglerat i art. 72.

4. **Ljud-/videoinspelningar i separata system.** Intervjuinspelningar ([art. 14](../../domains/asylum-procedure/articles/apr-014.md)) omfattas av asyl-aktens tioårsregim och medborgarskapsundantaget, men kan ligga i separat medielagring skild från ärendeakten — vilket gör triggerspridningen (problem 2) extra svår.

5. **Gallring vs. bevarande kolliderar.** Svensk arkivrätt utgår från bevarande ([arkivlagen 3 §](../../references/legislation/arkivlagstiftning.md)), medan EU-förordningen kräver radering. Rättsligt löses det via arkivlagen 10 § tredje stycket (avvikande bestämmelser gäller), men systemen måste faktiskt vara konfigurerade att tillämpa EU-fristen i stället för normalt bevarande — och Riksarkivets gallringsföreskrifter (RA-FS) behöver vara i linje med det.

> Dessa punkter är **inte dokumenterade i någon rättskälla** som en konflikt — de är identifierade systemkonsekvenser inför det nationella systemarbetet.

---

## Relaterade sidor

- [APR artikel 72](../../domains/asylum-procedure/articles/apr-072.md) — Lagring av uppgifter (asyl-akt)
- [Eurodac artikel 29](../../domains/eurodac/articles/eur-029.md) — Lagring av uppgifter (biometri)
- [Eurodac artikel 30](../../domains/eurodac/articles/eur-030.md) — Radering i förtid
- [Tidsfrister](../time-limits/README.md) — hur lagringstider beräknas
- [Flaggor och markeringar](../flags/README.md) — radering/avmärkning som statusflaggor
- [Svensk arkivlagstiftning](../../references/legislation/arkivlagstiftning.md) — arkivlagen, TF, RA-FS (nationell motpol till gallringskravet)
- [Utlänningsdataförordningen (2016:30)](../../references/legislation/utlanningsdataforordningen.md) — nationell gallring av biometri (10 år / medborgarskap)
- [Medborgarskapslagen (2001:82)](../../references/legislation/medborgarskapslagen.md) — medborgarskap som raderingstrigger; "8 år"-hemvistregeln förklarad

---

## Status

Arbetsutkast — EU-reglerna är källbelagda; systemkonsekvenserna är resonemang inför nationellt systemarbete.

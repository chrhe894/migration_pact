# Arbetsyta — Fristtyper (övertagande & återtagande)

> **Status: arbetsyta.** Ligger i `others/` och är **inte** en del av MkDocs-bygget eller vänstermenyn. Syftet är att öka förståelsen för hur olika *typer* av tidsfrister kopplar till övertagande/återtagande inom AMMR/Ansvar. Ingenting här publiceras förrän det aktivt flyttas in i `docs/`.

---

## Vad är en fristtyp?

En **fristtyp** är en återanvändbar mall för en tidsfrist, definierad av sin **startpunkt** och **karaktär** — inte av en enskild artikel. Samma typ kan förekomma som flera *instanser* i olika processer, med olika slutpunkt och längd.

Här dokumenteras de typer vi hittills identifierat i övertagande/återtagande. Listan är inte komplett — verksamheten arbetar med ~10–12 typer totalt.

---

## Översikt — fristtyper på tidsaxeln

Var varje typ lägger sig längs det mellanstatliga överföringsflödet (UT = Sverige överför).

<object type="image/svg+xml" data="overview-fristtyper.svg" width="100%"></object>

Källa: [`overview-fristtyper.pu`](overview-fristtyper.pu)

---

## Typ: ATB (Accept till Beslut) och ATÖ (Accept till Överföring)

Båda startar vid **accept** (godtagande/bekräftelse, uttrycklig eller tyst) men har olika slutpunkt och rättsföljd:

- **ATB** — accept → **beslut** (2 v, art. 42). Missad = beslutet är försenat, förfarandet fortsätter.
- **ATÖ** — accept → **överföring verkställd** (6 mån / 18 mån avvikande / 4 v förvar, art. 46). Missad = **ansvaret övergår** till den överförande staten.

Klockorna startar samtidigt (vid accept); ATB är en delsträcka inom ATÖ:s längre fönster. Diagrammet nedan visar båda.

<object type="image/svg+xml" data="atb.svg" width="100%"></object>

Källa: [`atb.pu`](atb.pu)

---

## Typ: TNO (Nekad begäran till omprövning)

Startar vid **avslag** (övertagande) eller **icke-bekräftelse** (återtagande). Mellanstatlig omprövning enligt genomförandeförordning 2025/2055.

<object type="image/svg+xml" data="omprovning.svg" width="100%"></object>

Källa: [`omprovning.pu`](omprovning.pu)

---

## Identifierade typer hittills

| Fristtyp | Startpunkt | Instanser (exempel) | Lagdel (att mappa) | Modifierare |
|----------|-----------|---------------------|--------------------|-------------|
| Framställningsfrist (ordinarie) | Registrering | 2 mån / 1 mån (Eurodac) | AMMR art. 39 | **L** kris (→4 mån) · **K** förvar (→ TAB) |
| TAB (Tidsfrist Ansökan till Begäran) — förvar | Registrering / tidpunkt för förvar | 2 v (1 v om förvar sker senare) | AMMR art. 45.1 | (är den förkortade förvarsvarianten) |
| TBS (Tidsfrist Begäran till Svar) | Begäran/framställan/avisering mottagen | övert.: 1 mån (2 v Eurodac/VIS, 1 v förvar) · återt.: 2 v | AMMR art. 40 / 41 / 45 | **L** kris (svar →2 mån) · **K** förvar (→1 v) |
| TNO (Nekad begäran till omprövning) | Avslag / icke-bekräftelse | begär 3 v (övert.) / 2 v (återt.), svar 2 v | Genomf. 2025/2055 art. 9.2 / 15 | — |
| ATB (Accept till Beslut) | Accept | 2 v | AMMR art. 42 | — |
| ATÖ (Accept till Överföring) | Accept | 6 mån / 18 mån / 4 v | AMMR art. 46 | **F** suspensiv verkan · **L** avvikande (→18 mån), kris (→1 år) · **K** förvar (→4 v / 5 v) |
| ATÖ (ansvarskompensation) | Godtagande (accept/tyst) av kompensationsåtagande | frist tills person överförd | Solidaritet, art. 63 (att verifiera) | (att verifiera) |
| Frysning | Beviljad suspensiv verkan | pausar ATÖ | AMMR art. 43.3 → 46 | (är själva frysmekanismen) |

**Modifierare:** **F** = frysning (pausas, återupptas) · **L** = förlängning (ersätts av längre frist) · **K** = förkortning (kortare frist, t.ex. vid förvar). Se [frysning-och-forlangning](../../docs/shared/time-limits/concepts/frysning-och-forlangning.md) i docs för frysning/förlängning; förkortning vid förvar följer av art. 45.


> **ATB och ATÖ — typen, inte artikeln.** Mönstret är "godtagande av något (accept/tyst) → frist tills åtgärd slutförd". ATB slutar vid beslutet, ATÖ vid den verkställda överföringen; båda startar vid accept och ATB är en delsträcka inom ATÖ:s fönster. Samma typer återanvänds i övertagande UT, återtagande UT och (för ATÖ) ansvarskompensation UT — men instanserna vilar på olika lagrum. Ansvarskompensationens exakta lagrum (troligen solidaritetskapitlet, art. 63 eller angränsande) återstår att verifiera.

> **TBS (Begäran till Svar)** gäller i övertagande **UT och IN** samt återtagande **UT och IN** — fristen ägs av den mottagande staten (IN, som ska svara), medan den avsändande staten (UT) väntar på svaret. Kärnegenskap: **uteblivet svar inom fristen = tyst godkännande/bekräftelse**. Samma typ förekommer sannolikt i andra regelverk än AMMR, men här listas endast AMMR-instanserna.

> **TAB (Ansökan till Begäran)** — här dokumenterad som **förvarsvarianten** (art. 45.1), som gäller **övertagande UT (förvar)** och **återtagande UT (förvar)**: samma artikel täcker både framställan och avisering. Startpunkten är enligt AMMR **registreringen** (eller tidpunkten för förvar) — inte "ansökan" i strikt mening; namnet "ansökan" används löst för ärendets initiering. Den ordinarie (icke-förvar) framställningsfristen ligger i art. 39 (egen rad ovan).

---

## Nästa steg (när/om detta ska in i docs)

- **Mappa mot lagdelarna** — koppla varje fristtyp till exakt artikel/punkt och till motsvarande regelkort (RULE-*). Kan bli en jämförelsetabell "fristtyp ↔ lagrum ↔ regelkort".
- **Bestäm källa (single source of truth)** — regelkorten (RULE-*) håller fristvärdena; fristtyp-sidor och domänöversikter *länkar* dit i stället för att upprepa.
- **Avgör publicering** — om typerna bedöms vara implementationsspecifika (verksamhet/teknik) kan de förbli i `others/`, eller lyftas in som en egen sektion i `docs/shared/time-limits/` med egen menypost.

---

## Referenser

- AMMR (2024/1351) — art. 39, 40, 42, 43, 45, 46
- Genomförandeförordning (EU) 2025/2055 — art. 9.2 (övertagande), art. 15.3–15.4 (återtagande)
- Publicerade motsvarigheter i kunskapsbasen:
  - `docs/domains/responsibility/interpretations/take-charge-out.md` / `take-back-out.md`
  - `docs/shared/time-limits/concepts/fristtyp-accept-till-beslut.md`
  - `docs/shared/time-limits/concepts/frysning-och-forlangning.md`

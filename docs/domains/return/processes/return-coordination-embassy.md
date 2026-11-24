---
tags:
  - återvändande
  - återvändandesamordning
  - ambassad
  - resehandling
  - process
---

# PROC-RTN-004

# Återvändandesamordning – ambassad

Delprocess till [PROC-RTN-001 Återvändandeförfarande](return-procedure.md), steg 10.

## Trigger

Det finns ett beslut om återvändande (avvisning eller utvisning), och personens **identitet eller medborgarskap** är inte fastställt eller personen saknar **giltig resehandling**.

---

## Resultat

Personen har en giltig resehandling (nationellt pass, tillfällig resehandling från tredjelandet eller europeisk resehandling för återvändande) och identiteten är bekräftad. Ärendet går vidare till [PROC-RTN-005 Återvändandesamordning – resa](return-coordination-travel.md). Alternativt finns ett hinder som leder till fortsatta åtgärder eller uppskjutande.

---

## Ansvar

Den myndighet som verkställer beslutet: Migrationsverket, Polismyndigheten (bl.a. när personen håller sig undan eller tvång behövs) eller Säkerhetspolisen i säkerhetsärenden ([RULE-UTL-12-014-001](../rules/rule-utl-12-014-001.md)).

---

## Huvudflöde

<object type="image/svg+xml" data="../diagrams/return-coordination-embassy.svg" width="100%"></object>

Källa: [`return-coordination-embassy.pu`](../diagrams/return-coordination-embassy.pu)

---

## Steg

| # | Steg | Regler | Gäller |
|---|------|--------|--------|
| 1 | Inhämta uppgifter och handlingar från personen: identitet, medborgarskap, varför handlingar saknas, resvägar och transitländer | [RULE-RR-018-002](../rules/rule-rr-018-002.md), [RULE-RR-018-003](../rules/rule-rr-018-003.md) | 17 okt 2027 |
| 2 | Kontrollera med andra medlemsstater om de har uppgifter eller resehandlingar i original | [RULE-RR-036-001](../rules/rule-rr-036-001.md), [RULE-RR-036-002](../rules/rule-rr-036-002.md), [RULE-RR-036-004](../rules/rule-rr-036-004.md) | 17 okt 2027 |
| 3 | **Tystnadsplikt:** lämna bara de uppgifter som behövs. Avslöja **inte** att personen har ansökt om internationellt skydd för de aktörer som påstås förfölja, till exempel ursprungslandets myndigheter | [RULE-APR-007-001](../../asylum-procedure/rules/rule-apr-007-001.md) | Nu (APR) |
| 4 | Överför uppgifter till tredjelandets behöriga myndighet bara om det är nödvändigt. Dokumentera överföringen | [RULE-RR-037-001](../rules/rule-rr-037-001.md) | 17 okt 2027 |
| 5a | **Ambassad eller konsulat:** begär resehandling eller bekräftelse av medborgarskap. Personen ska lämna de uppgifter som krävs och inställa sig personligen eller via video | [RULE-RR-034-001](../rules/rule-rr-034-001.md), [RULE-RR-018-002](../rules/rule-rr-018-002.md) (18.3 l–m) | 34: nu; 18: 17 okt 2027 |
| 5b | **Europeisk resehandling för återvändande**, om återtagandeinstrumentet medger det. Gäller en resa och är kostnadsfri | [RULE-ETD-003-001](../rules/rule-etd-003-001.md), [RULE-ETD-005-001](../rules/rule-etd-005-001.md) | Nu |
| 5c | **Stöd:** Frontex konsulära samarbete, en annan medlemsstat som kontaktar tredjelandet, unionens sambandsmän för återvändande | [RULE-FRX-048-001](../rules/rule-frx-048-001.md), [RULE-RR-042-002](../rules/rule-rr-042-002.md), [RULE-RR-043-001](../rules/rule-rr-043-001.md) | Frontex: nu; RR 42: 17 okt 2027; RR 43: nu |
| 6 | Om personen inte samarbetar: konsekvenser, tillgänglighetsåtgärder eller förvar | [RULE-RR-022-001](../rules/rule-rr-022-001.md), [RULE-RR-029-001](../rules/rule-rr-029-001.md) | 17 okt 2027 |
| 7 | Resehandling erhållen → [PROC-RTN-005](return-coordination-travel.md). Annars fortsatta åtgärder eller uppskjutande | [RULE-RR-011-002](../rules/rule-rr-011-002.md) | 17 okt 2027 |

---

## Tidsfrister och tidsgränser

| Vad | Längd | Regel |
|-----|-------|-------|
| Svar från annan medlemsstat på begäran om uppgifter | Högst **två veckor** | [RULE-RR-036-002](../rules/rule-rr-036-002.md) |
| Förvar när handlingar från tredjeland dröjer | Högst **24 månader** i stället för 12 | [RULE-RR-030-002](../rules/rule-rr-030-002.md) |
| Förvar efter 24 månader när resehandling erhållits eller kan förväntas | Ytterligare högst **6 månader** sammanlagt | [RULE-RR-030-003](../rules/rule-rr-030-003.md) |
| Avresefristen när resehandlingen dröjer | Får förlängas vid särskilda skäl | [RULE-UTL-12-014C-001](../rules/rule-utl-12-014c-001.md) (nu), [RULE-RR-005-004](../rules/rule-rr-005-004.md) (17 okt 2027) |

Varken förordningen eller utlänningslagen anger någon frist för hur snabbt tredjelandet ska svara. Det styrs av återtagandeavtal och överenskommelser, som inte finns i repot.

---

## Att observera

- **Förordning 2026/2280 tillåter överföring av mer än identitetsuppgifter.** Art. 37.1 tillåter överföring av uppgifterna i art. 36.6 a–h, bland annat uppehållsstatus och ansökningar (e) och **skälen till besluten om återvändande** (h). Förordningen har inget eget förbud mot att avslöja en asylansökan. Förbudet följer av APR art. 7.2, som gäller även efter det slutliga beslutet, och av Frontex art. 48.1 a ii för Frontex. Överföringen ska alltså begränsas till det som är nödvändigt och samtidigt förenligt med APR art. 7.2.
- **Fram till 17 oktober 2027** gäller direktiv 2008/115/EG och utlänningslagen för samarbetsskyldigheten och förvaret. Art. 34 (återtagande), förordning 2016/1953, Frontexförordningen och APR art. 7 gäller redan.

---

## Juridiska milstolpar

- Beslut om återvändande verkställbart
- Begäran till tredjelandets myndighet skickad
- Personens inställelse hos ambassad eller konsulat
- Resehandling utfärdad, eller avslag eller uteblivet svar från tredjelandet

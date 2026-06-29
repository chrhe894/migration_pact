# User stories: personliga intervjuer

## Källgrund

- Ny reglering: Förordning (EU) 2024/1348, särskilt artiklarna 11-14.
- Gammal reglering: Direktiv 2013/32/EU, särskilt artiklarna 14-17 och 34.
- Lokal ny källa: `ref_material/OJ_L_202401348_SV_TXT.pdf`.
- Kompletterande vägledning: EUAA, `Practical Guide on the Audio Recording of Personal Interviews`, oktober 2025.

## User stories

| nr | Feature | Användarberättelse | System | Kommentar |
| --- | --- | --- | --- | --- |
| 1 | Identifiera intervjutyp | Som handläggare vill jag kunna ange om intervjun är en tillåtlighetsintervju eller sakintervju, så att rätt regler och dokumentationskrav används. | Intervjustöd/ärendehantering | Ny förordning skiljer tydligt mellan intervju om tillåtlighet och intervju om sakprövning. |
| 2 | Bedöma om intervju krävs | Som handläggare vill jag att systemet visar om personlig intervju ska genomföras, kan kombineras eller kan avstås, så att ärendet hanteras enligt rätt process. | Workflow | Kräver koppling till artiklarna 11-13 i förordning (EU) 2024/1348. |
| 3 | Planera intervju | Som handläggare vill jag kunna boka intervju med rätt intervjuare, tolk, språk och format, så att sökanden får möjlighet att lägga fram sin ansökan korrekt. | Bokning/intervjustöd | Behöver stödja sekretess, tolkning och eventuella önskemål om kön på intervjuare eller tolk där möjligt. |
| 4 | Hantera särskilda processuella garantier | Som handläggare vill jag att systemet visar relevanta stödbehov inför intervjun, så att intervjun kan anpassas utan att känsliga uppgifter exponeras i onödan. | Ärendehantering/intervjustöd | Artikel 14 betonar särskild uppmärksamhet vid ljudinspelning för sökande i behov av särskilda processuella garantier. |
| 5 | Informera om ljudinspelning | Som handläggare vill jag dokumentera att sökanden informerats i förväg om att intervjun spelas in och varför, så att informationskravet kan visas i efterhand. | Intervjustöd | Nytt krav enligt artikel 14.2. |
| 6 | Starta ljudinspelning | Som intervjuare vill jag kunna starta ljudinspelning direkt från intervjutillfället, så att inspelningen kopplas till rätt ärende och intervju. | Ljudinspelning/intervjustöd | Ljudinspelning är obligatorisk enligt nya förordningen. |
| 7 | Kontrollera ljudkvalitet | Som intervjuare vill jag få teknisk bekräftelse på att ljud spelas in med tillräcklig kvalitet, så att intervjun inte genomförs utan användbar inspelning. | Ljudinspelning | Viktigt eftersom ljudinspelningen kan få företräde vid tvivel om vad som sagts. |
| 8 | Hantera avbrott | Som intervjuare vill jag kunna markera paus, avbrott och tekniska problem, så att akten visar varför inspelningen eventuellt består av flera delar eller är ofullständig. | Ljudinspelning/intervjustöd | Behöver avvikelsehantering vid misslyckad eller delvis inspelad intervju. |
| 9 | Spara inspelning i akten | Som handläggare vill jag att ljudinspelningen automatiskt sparas i sökandens akt, så att förordningens krav på aktföring uppfylls. | Dokument-/akthantering | Artikel 14.2 anger att inspelningen ska inkluderas i akten. |
| 10 | Skapa rapport eller transkript | Som handläggare vill jag kunna skapa rapport, transkript av intervjun eller transkript av inspelningen, så att huvuddelarna av intervjun dokumenteras i text. | Dokumentstöd | Artikel 14.1 anger alternativen. |
| 11 | Koppla text och ljud | Som beslutsfattare vill jag se relationen mellan rapport/transkript och ljudinspelning, så att jag kan förstå vilket underlag som hör till vilken intervju. | Akthantering | Särskilt viktigt vid flera intervjuer eller flera ljudfiler. |
| 12 | Ge sökanden möjlighet att kommentera | Som handläggare vill jag kunna skicka rapport eller transkript för kommentar inom rätt tidsfrist, så att sökanden kan påtala fel, missförstånd eller översättningsproblem. | Kommunikation/dokumentstöd | Artikel 14.3. |
| 13 | Registrera bekräftelse eller vägran | Som handläggare vill jag kunna registrera att sökanden bekräftar innehållet eller vägrar bekräfta det med skäl, så att akten blir komplett. | Ärendehantering | Artikel 14.4. |
| 14 | Hantera undantag från kommentar/bekräftelse | Som handläggare vill jag att systemet visar när sökanden inte behöver ombes kommentera eller bekräfta rapport/transkript, så att onödiga processteg undviks. | Workflow | Kräver artikelverifiering och nationell processmappning. |
| 15 | Prioritera ljud vid oklarhet | Som beslutsfattare vill jag enkelt kunna lyssna på relevant del av inspelningen vid tvivel om vad sökanden sagt, så att beslutet bygger på korrekt underlag. | Beslutsstöd/akthantering | Enligt artikel 14.4 ska ljudinspelningen ha företräde vid tvivel om uttalanden. |
| 16 | Åtkomst före beslut | Som sökande eller ombud vill jag få tillgång till rapport eller transkript så snart som möjligt efter intervjun och i tid före beslut, så att jag kan kontrollera underlaget. | E-tjänst/kommunikation | Artikel 14.6 i nya förordningen. |
| 17 | Åtkomst i överklagande | Som ombud vill jag kunna få tillgång till ljudinspelningen i överklagandeförfarandet, så att jag kan granska vad som faktiskt sagts vid intervjun. | Överklagande/aktdelning | Ny förordning anger åtkomst till inspelningen i överklagandeförfarandet. |
| 18 | Behörighetsstyra ljudfil | Som systemförvaltare vill jag kunna styra och logga åtkomst till ljudinspelningar, så att känsliga personuppgifter skyddas. | Behörighet/loggning | Ljudfiler kan innehålla mycket känsliga uppgifter. |
| 19 | Dela ljudfil säkert | Som handläggare vill jag kunna dela ljudinspelningen säkert med behörig mottagare, så att utlämnande inte sker via osäkra kanaler. | Akthantering/kommunikation | Relevant för domstol, ombud och intern granskning. |
| 20 | Bevara och gallra | Som arkivansvarig vill jag kunna styra bevarande och gallring av ljudinspelningar, så att nationella arkiv- och dataskyddskrav följs. | Arkiv/dokumenthantering | Kräver svensk nationell komplettering. |
| 21 | Rapportera avvikelse | Som handläggare vill jag kunna registrera när ljudinspelning saknas, misslyckas eller inte kan användas, så att ärendet kan kvalitetssäkras och följas upp. | Kvalitet/avvikelsehantering | Viktigt eftersom inspelning är obligatorisk. |
| 22 | Följa upp efterlevnad | Som processägare vill jag kunna se statistik över genomförda intervjuer, saknade inspelningar, tekniska avbrott och delningar, så att processen kan styras och förbättras. | Statistik/rapportering | Kopplar personliga intervjuer till statistikspåret. |

## Frågor för fortsatt analys

- Hur ska systemet definiera "personlig intervju" i relation till olika svenska intervju- och utredningsmoment?
- Vilka undantag från personlig intervju ska modelleras som systemregler?
- Hur ska sökanden informeras om ljudinspelningen när tolk används?
- Ska ljudinspelningen kunna delas direkt med sökande eller endast med ombud/domstol?
- Hur ska ljudfilen hanteras när rapport/transkript korrigeras efter sökandens kommentarer?
- Vilka krav ställs på gallring, arkivering och loggning enligt svensk rätt?

# DECISIONS

## Syfte

Detta dokument beskriver de viktigaste arkitekturella och metodmässiga beslut som har fattats för projektet.

Besluten dokumenteras för att skapa en gemensam förståelse och minska risken för att samma diskussion behöver tas flera gånger.

Om ett beslut ändras ska ett nytt beslut dokumenteras. Tidigare beslut behålls som en del av projektets historik.

---

# DEC-001

## Titel

Repositoryts språk

## Status

Accepted

## Beslut

Repositoryts tekniska struktur använder engelska.

Det gäller exempelvis:

- katalognamn,
- filnamn,
- mallar.

Projektets innehåll skrivs på svenska.

Det gäller bland annat:

- dokumentation,
- analyser,
- kommentarer,
- PlantUML-diagram.

## Motiv

Engelska filnamn följer etablerad GitHub-praxis.

Svenskt innehåll gör dokumentationen mer tillgänglig för projektets målgrupp.

---

# DEC-002

## Titel

EU-rätten är projektets primära källa

## Status

Accepted

## Beslut

Projektet beskriver EU:s rättsakter.

Nationell lagstiftning och nationell tillämpning ingår inte som en del av kunskapsbasen.

## Motiv

Projektets syfte är att beskriva den gemensamma unionsrätten.

Det gör dokumentationen tydligare och minskar risken för att nationella särlösningar blandas ihop med EU-rätten.

---

# DEC-003

## Titel

Spårbarhet är en grundprincip

## Status

Accepted

## Beslut

Alla rättsliga påståenden ska kunna spåras tillbaka till en rättslig källa eller tydligt anges som en tolkning.

## Motiv

Spårbarhet ökar kvaliteten, förenklar granskning och gör kunskapsbasen långsiktigt underhållbar.

---

# DEC-004

## Titel

PlantUML används för diagram

## Status

Accepted

## Beslut

Diagram skapas i PlantUML.

PlantUML-filer utgör projektets original.

Genererade bilder betraktas som härledda artefakter.

## Motiv

PlantUML är textbaserat, versionshanteras väl och lämpar sig för både människor och automatiserad bearbetning.

---

# DEC-005

## Titel

Små och modulära dokument

## Status

Accepted

## Beslut

Repositoryt ska bestå av många mindre dokument i stället för ett fåtal stora.

## Motiv

Små dokument är enklare att:

- underhålla,
- granska,
- återanvända,
- referera till.

---

# DEC-006

## Titel

En regel dokumenteras en gång

## Status

Accepted

## Beslut

En rättsregel ska dokumenteras endast en gång.

Övriga dokument ska referera till den istället för att kopiera innehållet.

## Motiv

Det minskar risken för motstridiga beskrivningar och förenklar framtida uppdateringar.

---

# DEC-007

## Titel

Diagram beskriver struktur

## Status

Accepted

## Beslut

Diagram används för att beskriva processer, flöden och relationer.

Den rättsliga innebörden dokumenteras i Markdown.

## Motiv

Det gör diagrammen enkla att förstå och minskar risken för att juridiska regler dupliceras.

---

# DEC-008

## Titel

Regelreferenser ska vara klickbara länkar

## Status

Accepted

## Beslut

Referenser till regler, processer och delade aktiviteter i processbeskrivningar och diagram ska uttryckas som relativa Markdown-länkar, inte som plain-text ID:n.

Exempel i processbeskrivning:

```markdown
- [RULE-APR-027-001](../rules/rule-apr-027-001.md) — Skyldighet att registrera
```

Exempel i flödessteg:

```markdown
3. Uppgifter samlas in ([RULE-APR-027-002](../rules/rule-apr-027-002.md)).
```

Exempel i PlantUML-diagram:

```plantuml
:[[../rules/rule-apr-027-001.md Registrera ansökan]];
```

Exempel i regel:

```markdown
## Rättslig grund

[APR artikel 27](../articles/apr-027.md), punkt 1
```

## Motiv

Plain-text ID:n kräver att läsaren manuellt söker upp regeln. Klickbara länkar gör det möjligt att navigera direkt från process till regel till rättskälla, vilket är kärnan i kunskapsbasens spårbarhetsprincip.

---

# DEC-009

## Titel

Diagram länkar till regler, inte till artiklar

## Status

Accepted

## Beslut

När en aktivitet i ett PlantUML-diagram har en rättslig grund ska länken peka på den relevanta rule.md-filen, inte direkt på artikel-filen.

## Motiv

Regel-filerna sammanfattar vad som gäller på ett tillgängligt sätt. Artikel-filerna innehåller den fullständiga lagtexten och är bättre som ett andra steg i navigationskedjan regel → artikel.

Navigationskedjan ska vara: diagram → process → regel → artikel.

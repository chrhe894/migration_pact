# Delat — Statistik

## Syfte

Denna shared-modul dokumenterar de statistiska datapunkter och beräkningar som används i migrationspaktens förordningar för att styra förfaranden, tröskelvärden och ansvarsbedömningar.

Statistik är inte en rättsakt i sig utan en stödfunktion som påverkar tillämpningen av flera domäner.

---

## Datapunkter som styr förfaranden

### Bifallsandel (recognition rate)

| Användning | Tröskel | Källa |
|-----------|---------|-------|
| Obligatoriskt gränsförfarande | < 20% i EU-genomsnitt | APR art. 45.1 → art. 42.1 c |
| Gränsförfarande vid kris | < 50% i EU-genomsnitt | Krishanteringsförordningen art. 11 |
| Påskyndat förfarande — säkert ursprungsland | < 20% | APR art. 42.1 c |

**Datakälla:** EU:s asylbyrå (EUAA) publicerar kvartals- och årsdata.

---

### Kapacitetsberäkning (gränsförfarande)

| Parameter | Värde/formel | Källa |
|-----------|--------------|-------|
| Unionens totala kapacitet | 30 000 | APR art. 46 |
| Medlemsstats kapacitet | Proportionell andel av 30 000 baserat på 3 års data | APR art. 47.4 |
| Beräkningsgrund | Irreguljära gränspassager + landsättningar + nekade inresor | APR art. 47.4 |
| Årligt högsta antal | 2x (2026), 3x (2027), 4x (2028) av kapaciteten | APR art. 47.1 |

**Datakälla:** Frontex (gränspassager) och Eurostat.

---

### Referensnyckel (solidaritet)

| Parameter | Vikt | Källa |
|-----------|------|-------|
| BNP | 50% | AMMR art. 66 |
| Befolkning | 50% | AMMR art. 66 |

**Datakälla:** Eurostat.

---

### Ansvarets upphörande

| Parameter | Tidsfrist | Källa |
|-----------|-----------|-------|
| Irreguljär gränspassage | 20 månader | AMMR art. 33.1 |
| Landsättning (sök-och-räddning) | 12 månader | AMMR art. 33.2 |
| Frånvaro från EU | 9 månader | AMMR art. 37.4 |
| Efter gränsförfarandebeslut | 15 månader | AMMR art. 37.2 |

**Datakälla:** Eurodac (registrerade uppgifter), in- och utresesystemet (EES).

---

## Informationssystem som levererar data

| System | Vad det mäter | Används av |
|--------|--------------|------------|
| Eurodac | Biometriska registreringar, ansvarig stat | Responsibility, Eurodac |
| EES (in- och utresesystemet) | Gränspassager, in-/utresor | Screening, Responsibility |
| Frontex | Irreguljära passager, landsättningar | Border procedure (kapacitet) |
| EUAA | Asylansökningar, bifallsandelar | Border procedure, Asylum procedure |
| Eurostat | Befolkning, BNP | Solidarity (referensnyckel) |

---

## Rapportering

- **AMMR artikel 9** — Den årliga europeiska asyl- och migrationsrapporten
- **AMMR artikel 10** — Information för att bedöma migrationstryck
- **APR artikel 49** — Medlemsstats underrättelse om kapacitet

---

## Öppna frågor

- Hur ofta uppdateras bifallsandelen — kvartalsvis eller årsvis?
- Vilken period ligger till grund för beräkningen av "säkert ursprungsland"?
- Hur snabbt slår förändringar i migrationsflöden igenom i kapacitetsberäkningen (3-årsdata)?
- Hur hanteras diskrepanser mellan Frontex- och nationell statistik?

---

## Används av

- [Border Procedure](../../domains/border-procedure/README.md) — kapacitetsberäkning och bifallsgräns
- [Asylum Procedure](../../domains/asylum-procedure/README.md) — påskyndat vid säkert ursprungsland
- [Solidarity](../../domains/solidarity/README.md) — referensnyckel
- [Responsibility](../../domains/responsibility/README.md) — ansvarets upphörande (tidsberäkning)
- [Crisis](../../domains/crisis/README.md) — utökad bifallsgräns vid kris

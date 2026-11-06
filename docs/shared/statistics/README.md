# Delat — Statistik

## Syfte

Denna shared-modul dokumenterar de statistiska datapunkter och beräkningar som används i migrationspaktens förordningar för att styra förfaranden, tröskelvärden och ansvarsbedömningar.

Statistik är inte en rättsakt i sig utan en stödfunktion som påverkar tillämpningen av flera domäner.

---

## Datapunkter som styr förfaranden

### Bifallsandel (recognition rate)

| Användning | Tröskel | Källa |
|-----------|---------|-------|
| Obligatoriskt gränsförfarande | < 20% i EU-genomsnitt | [APR art. 45.1](../../domains/border-procedure/articles/apr-045.md) → [art. 42.1 c](../../domains/asylum-procedure/articles/apr-042.md) |
| Gränsförfarande vid kris | < 50% i EU-genomsnitt | [Krishanteringsförordningen art. 11](../../domains/crisis/articles/crisis-011.md) |
| Påskyndat förfarande — säkert ursprungsland | < 20% | [APR art. 42.1 c](../../domains/asylum-procedure/articles/apr-042.md) |

**Datakälla:** EU:s asylbyrå (EUAA) publicerar kvartals- och årsdata.

---

### Kapacitetsberäkning (gränsförfarande)

| Parameter | Värde/formel | Källa |
|-----------|--------------|-------|
| Unionens totala kapacitet | 30 000 | [APR art. 46](../../domains/border-procedure/articles/apr-046.md) |
| Medlemsstats kapacitet | Proportionell andel av 30 000 baserat på 3 års data | [APR art. 47.4](../../domains/border-procedure/articles/apr-047.md) |
| Beräkningsgrund | Irreguljära gränspassager + landsättningar + nekade inresor | [APR art. 47.4](../../domains/border-procedure/articles/apr-047.md) |
| Årligt högsta antal | 2x (2026), 3x (2027), 4x (2028) av kapaciteten | [APR art. 47.1](../../domains/border-procedure/articles/apr-047.md) |

**Datakälla:** Frontex (gränspassager) och Eurostat.

---

### Referensnyckel (solidaritet)

| Parameter | Vikt | Källa |
|-----------|------|-------|
| BNP | 50% | [AMMR art. 66](../../domains/solidarity/articles/ammr-066.md) |
| Befolkning | 50% | [AMMR art. 66](../../domains/solidarity/articles/ammr-066.md) |

**Datakälla:** Eurostat.

---

### Ansvarets upphörande

| Parameter | Tidsfrist | Källa |
|-----------|-----------|-------|
| Irreguljär gränspassage | 20 månader | [AMMR art. 33.1](../../domains/responsibility/articles/ammr-033.md) |
| Landsättning (sök-och-räddning) | 12 månader | [AMMR art. 33.2](../../domains/responsibility/articles/ammr-033.md) |
| Frånvaro från EU | 9 månader | [AMMR art. 37.4](../../domains/responsibility/articles/ammr-037.md) |
| Efter gränsförfarandebeslut | 15 månader | [AMMR art. 37.2](../../domains/responsibility/articles/ammr-037.md) |

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

- [AMMR artikel 9](articles/ammr-009.md) — Den årliga europeiska asyl- och migrationsrapporten
- [AMMR artikel 10](articles/ammr-010.md) — Information för att bedöma migrationstryck
- [APR artikel 49](../../domains/border-procedure/articles/apr-049.md) — Medlemsstats underrättelse om kapacitet

---

## Öppna frågor

- Hur ofta uppdateras bifallsandelen — kvartalsvis eller årsvis?
- Vilken period ligger till grund för beräkningen av "säkert ursprungsland"?
- Hur snabbt slår förändringar i migrationsflöden igenom i kapacitetsberäkningen (3-årsdata)?
- Hur hanteras diskrepanser mellan Frontex- och nationell statistik?

---

## Används av

- [Gränsförfarande](../../domains/border-procedure/README.md) — kapacitetsberäkning och bifallsgräns
- [Asylförfarande](../../domains/asylum-procedure/README.md) — påskyndat vid säkert ursprungsland
- [Solidaritet](../../domains/solidarity/README.md) — referensnyckel
- [Ansvar](../../domains/responsibility/README.md) — ansvarets upphörande (tidsberäkning)
- [Kris](../../domains/crisis/README.md) — utökad bifallsgräns vid kris

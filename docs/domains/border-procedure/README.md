
# Gränsförfarande

## Syfte

Domänen beskriver gränsförfarandet för asyl (border procedure) enligt APR artiklarna 43–54.

Gränsförfarandet är ett särskilt förfarande som genomförs vid eller nära de yttre gränserna för personer som inte tillåtits resa in på territoriet. Det syftar till att snabbt pröva ansökningar som uppfyller vissa kriterier — utan att sökanden ges tillstånd att resa in.

---

## Plats i livscykeln

| | |
|---|---|
| **Föregående** | [Screening](../screening/README.md) → [Registration](../registration/README.md) |
| **Nästa** | Beviljande (inresa tillåts) eller [Återvändande vid gräns](../return-border-procedure/README.md) |
| **Inträde** | Ansökan registrerad, sökanden vid yttre gräns, gränsförfarandevillkor uppfyllda |
| **Utträde** | Beslut fattat inom 12 veckor, eller tidsfrist löpt ut (inresa tillåts) |

---

## Primära rättskällor

- [APR artikel 43](articles/apr-043.md) — Villkor för att tillämpa gränsförfarandet
- [APR artikel 44](articles/apr-044.md) — Beslut inom ramen för gränsförfarandet
- [APR artikel 45](articles/apr-045.md) — Obligatorisk tillämpning
- [APR artikel 46](articles/apr-046.md) — Tillräcklig kapacitet på unionsnivå
- [APR artikel 47](articles/apr-047.md) — En medlemsstats tillräckliga kapacitet
- [APR artikel 51](articles/apr-051.md) — Tidsfrister
- [APR artikel 53](articles/apr-053.md) — Undantag från gränsförfarandet
- [APR artikel 54](articles/apr-054.md) — Platser för genomförande

---

## Processer

| Process | Beskrivning |
|---------|-------------|
| [PROC-BRD-001 Asylgränsförfarande](processes/asylum-border-procedure.md) | Prövning av ansökan inom ramen för gränsförfarande |

---

## Juridiska milstolpar

```text
Screening avslutad (ingen inresa tillåts)
        │
        ▼
Gränsförfarande inleds
        │
        ├── Admissibility check (art. 38 via art. 44)
        ├── Examination on the merits (art. 42 via art. 44)
        │
        ▼
Beslut (inom 12 veckor)
        │
        ├── Beviljat → inresa tillåts
        ├── Avslag → återvändandeförfarande vid gräns (förordning 2024/1349)
        └── Kapacitet uppnådd → reguljärt förfarande
```

---

## Begrepp

| ID | Begrepp |
|----|---------|
| [CON-BRD-001](concepts/border-procedure.md) | Border procedure |
| [CON-BRD-002](concepts/adequate-capacity.md) | Adequate capacity |

---

## Regler

### APR artikel 43 — Villkor

| Regel | Beskrivning |
|-------|-------------|
| [RULE-APR-043-001](rules/rule-apr-043-001.md) | Villkor för tillämpning av gränsförfarandet |
| [RULE-APR-043-002](rules/rule-apr-043-002.md) | Inresa nekas under gränsförfarandet |

### APR artikel 45 — Obligatorisk tillämpning

| Regel | Beskrivning |
|-------|-------------|
| [RULE-APR-045-001](rules/rule-apr-045-001.md) | Obligatorisk tillämpning vid säkerhetshot, vilseledning eller säkert ursprungsland |

### APR artikel 51 — Tidsfrister

| Regel | Beskrivning |
|-------|-------------|
| [RULE-APR-051-001](rules/rule-apr-051-001.md) | Inlämnande inom 5 dagar |
| [RULE-APR-051-002](rules/rule-apr-051-002.md) | Maximal varaktighet — 12 veckor |

### APR artikel 53 — Undantag

| Regel | Beskrivning |
|-------|-------------|
| [RULE-APR-053-001](rules/rule-apr-053-001.md) | Undantag för sårbara sökande |

---

## Tolkningar

| Fil | Frågeställning |
|-----|----------------|
| [border-vs-regular-procedure](interpretations/border-vs-regular-procedure.md) | Skillnaden mellan gränsförfarande och reguljärt förfarande |

---

## Öppna frågor

| Fil | Fråga |
|-----|-------|
| [capacity-mechanism](open_questions/capacity-mechanism.md) | Hur fungerar kapacitetsmekanismen i praktiken? |

---

## Delade moduler

| Modul | Länk |
|-------|------|
| Time limits | [shared/time-limits](../../shared/time-limits/README.md) |
| Children | [shared/children](../../shared/children/README.md) |
| Vulnerable persons | [shared/vulnerable-persons](../../shared/vulnerable-persons/README.md) |
| Interpreters | [shared/interpreters](../../shared/interpreters/README.md) |

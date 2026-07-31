# Screening — spill till andra domäner/shared

Skapandet av capabilities och requirements för Screening visar att följande
bör skapas eller uppdateras i andra domäner:

---

## Shared

| Typ | Förslag | Motivering |
|-----|---------|------------|
| CAP | CAP-ID-001 Verify Identity | CAP-SCR-003 beror på shared/identity. En gemensam capability borde existera. |
| CAP | CAP-INT-001 Provide Interpreter | REQ-SCR-011-003 kräver tolktjänster → shared/interpreters |
| CAP | CAP-BIO-001 Collect Biometric Data | CAP-SCR-003 och CAP-SCR-001 konsumerar biometri → shared/biometrics |
| REQ | REQ-INT-001 | Tolk ska tillhandahållas (redan som regel, men saknas som formellt REQ) |

---

## Eurodac

| Typ | Förslag | Motivering |
|-----|---------|------------|
| REQ | REQ-EUR-014-001 | Biometriska uppgifter tagna under screening ska kunna överföras direkt till Eurodac (REQ-SCR-014-003) |

---

## Registration

| Typ | Förslag | Motivering |
|-----|---------|------------|
| REQ | (komplettering) | REQ-SCR-018-002 innebär att screeningformuläret ska överlämnas → koppla till REQ-APR-027-009 |

---

## Children (shared)

| Typ | Förslag | Motivering |
|-----|---------|------------|
| CAP | CAP-CHI-001 Safeguard Unaccompanied Minors | CAP-SCR-008 berör barn → gemensam capability |
| REQ | REQ-CHI-001 | Företrädare ska utses (max 30 barn/företrädare) |

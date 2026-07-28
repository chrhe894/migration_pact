<div align="right">← <a href="../README.md">Asylum Procedure</a></div>

# PROC-ASY-002

# Subsequent application

## Trigger

En person lämnar in en ny ansökan om internationellt skydd efter att ett slutligt beslut har fattats om en tidigare ansökan.

---

## Resultat

Ansökan har antingen avvisats som otillåtlig eller tagits upp till prövning i sak.

---

## Huvudflöde

1. Person lämnar in ny ansökan (eller nya uppgifter).
2. Ärendehistorik hämtas — tidigare ansökningar, beslut, ansvarig stat.
3. Kontrollera att slutligt beslut finns om tidigare ansökan.
4. Ansökan klassificeras som efterföljande ansökan.
5. Ansvarig medlemsstat fastställs.
6. Förhandsprövning genomförs ([RULE-APR-055-001](../rules/rule-apr-055-001.md)):
   - Nya omständigheter och bevis registreras.
   - Bedöm om uppgifterna kunde ha lagts fram tidigare.
   - Avgör om prövningen ska ske skriftligt eller med intervju.
7. Beslut:
   - **Nya relevanta omständigheter finns** → ansökan tas upp till sakprövning.
   - **Inga nya relevanta omständigheter** → avvisning som otillåtlig ([RULE-APR-055-002](../rules/rule-apr-055-002.md)).

---

## Alternativt flöde — rätt att stanna

- Vid **första** efterföljande ansökan: sökanden har rätt att stanna.
- Vid **andra eller följande**: undantag kan gälla ([RULE-APR-056-001](../rules/rule-apr-056-001.md)).
- Undantag kräver non-refoulement-kontroll.

---

## Alternativt flöde — ingen tidigare slutlig dom

Om det inte finns ett slutligt beslut om den tidigare ansökan (ärendet pågår eller är överklagat) ska de nya uppgifterna hanteras inom det pågående förfarandet — inte som en efterföljande ansökan.

---

## Juridiska milstolpar

- Subsequent application registered
- Preliminary examination completed
- Admissibility decision (inadmissible / admissible)
- If admissible: examination on the merits → decision

---

## Regler

- [RULE-APR-055-001](../rules/rule-apr-055-001.md) — Förhandsprövning
- [RULE-APR-055-002](../rules/rule-apr-055-002.md) — Avvisning vid avsaknad av nya omständigheter
- [RULE-APR-056-001](../rules/rule-apr-056-001.md) — Undantag från rätt att stanna

---

## Shared Activities

- [Determine interpreter needs](../../../shared/interpreters/activities/determine-interpreter-needs.md)

---

## Diagram

Se `../diagrams/subsequent-application.pu`

# User stories: efterföljande ansökningar

## Källgrund

- Ny reglering: Förordning (EU) 2024/1348, särskilt artikel 3.19, 38.2, 55, 56 och 68.
- Gammal reglering: Direktiv 2013/32/EU, särskilt artikel 2 q, 33.2 d och 40-42.
- Lokal ny källa: `ref_material/OJ_L_202401348_SV_TXT.pdf`.
- Officiella referenser:
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32024R1348>
  - <https://eur-lex.europa.eu/legal-content/SV/TXT/?uri=CELEX:32013L0032>

## Kort jämförelse

Den nya regleringen behåller huvudlogiken från det gamla asylprocedurdirektivet: en efterföljande ansökan ska först förhandsprövas och kan avvisas om det saknas nya relevanta omständigheter. De tydligaste förändringarna är att reglerna nu finns i en direkt tillämplig förordning, att ansökan uttryckligen kopplas till "vilken medlemsstat som helst" efter ett slutligt beslut, att prövningen knyts till ansvarig medlemsstat enligt den nya ansvarsförordningen och att kriterierna för nya omständigheter blir mer harmoniserade.

En viktig nyhet är också att nya omständigheter inte bara kan avse skyddsbehovet, utan även en tidigare använd grund för avvisning när den tidigare ansökan avvisades som otillåtlig. Det gör att systemet behöver kunna skilja mellan nya skyddsskäl och nya omständigheter som påverkar en tidigare processuell avvisningsgrund.

## Skillnader att omsätta i krav

| Område | Gammal ordning | Ny ordning | Möjlig systempåverkan |
| --- | --- | --- | --- |
| Rättslig form | Direktiv 2013/32/EU, genomfört i nationell rätt. | Förordning (EU) 2024/1348, direkt tillämplig. | Mindre utrymme för olika nationella processvarianter i kärnflödet. |
| Definition | Efterföljande ansökan efter slutligt beslut på tidigare ansökan. | Efterföljande ansökan efter slutligt beslut på tidigare ansökan, gjord i vilken medlemsstat som helst. | Systemet behöver känna igen tidigare slutliga beslut även när ärendet kopplar till annan medlemsstat. |
| Ansökan före slutligt beslut | Hanteras som ytterligare framställning eller inom pågående prövning/överklagande när det sker i samma medlemsstat. | Ska ses som ytterligare framställning, inte ny ansökan, och prövas i ansvarig medlemsstat inom pågående administrativt förfarande eller överklagande. | Behöver undvika att skapa nytt ärende när tidigare ärende fortfarande är öppet. |
| Förhandsprövning | Nya element eller fakta som rör om sökanden kvalificerar för internationellt skydd. | Nya element som väsentligt ökar sannolikheten för skydd eller som rör en tidigare använd avvisningsgrund. | Förhandsprövningen behöver två spår: skyddsgrund och tidigare avvisningsgrund. |
| "Kunde ha lagts fram tidigare" | Medlemsstater fick föreskriva att ansökan bara går vidare om sökanden utan egen skuld inte kunde lägga fram uppgifterna tidigare. | Nyhetskravet blir mer uttryckligt i förordningen, med undantag när uppgifterna ändå väsentligt påverkar skydds- eller avvisningsbedömningen eller tidigare ärende avslutades som implicit återkallat utan sakprövning. | Systemet behöver dokumentera varför uppgift är ny, varför den inte lades fram tidigare och om undantag ändå gäller. |
| Personlig intervju | Nationella regler kunde tillåta skriftlig förhandsprövning utan intervju, med vissa undantag. | Förhandsprövning kan ske skriftligt eller med personlig intervju; intervju kan särskilt avstås om skriftligt underlag tydligt visar att nya element saknas. | Beslut om intervju/ingen intervju bör loggas med skäl. |
| Avvisning utan nya element | Ansökan betraktades som otillåtlig enligt artikel 33.2 d. | Ansökan ska avvisas som otillåtlig enligt artikel 38.2 när artikel 55.7 är uppfylld. | Beslutsmallar och klassificering behöver uppdateras. |
| Rätt att stanna | Undantag kunde göras vid första efterföljande ansökan som bara syftade till att försena avlägsnande, eller vid ytterligare ansökan i samma medlemsstat efter tidigare slutligt beslut. | Undantag kan göras vid första efterföljande ansökan som syftar till att försena ett nära förestående avlägsnande och inte prövas vidare, eller vid andra/följande efterföljande ansökan i vilken medlemsstat som helst efter tidigare avslag/avvisning. | Systemet behöver flagga första respektive andra/följande efterföljande ansökan och koppla till återvändandebeslut. |
| Överklagande och suspensiv effekt | Reglerades i direktivets överklagandestruktur och nationell rätt. | Förordningen anger mer detaljerat när rätt att stanna och suspensiv effekt finns eller kan begränsas. | Systemet behöver visa om överklagande automatiskt stoppar verkställighet eller kräver särskilt beslut om rätt att stanna. |

## User stories

| nr | Feature | Användarberättelse | System | Kommentar |
| --- | --- | --- | --- | --- |
| 1 | Identifiera efterföljande ansökan | Som handläggare vill jag att systemet markerar en ansökan som efterföljande när det finns ett slutligt beslut på en tidigare ansökan, så att rätt förhandsprövning används. | Ärendehantering | Ny definition i förordning (EU) 2024/1348 artikel 3.19 och 55.2 omfattar ansökan i vilken medlemsstat som helst. |
| 2 | Skilja ytterligare framställning från ny ansökan | Som handläggare vill jag att systemet visar om tidigare ärende fortfarande är öppet, så att nya uppgifter hanteras som ytterligare framställning i stället för ny ansökan. | Ärendehantering | Ny artikel 55.1 uttrycker detta tydligare som "further representation" före slutligt beslut. |
| 3 | Hitta ansvarig medlemsstat | Som handläggare vill jag se vilken medlemsstat som är ansvarig för prövningen, så att efterföljande ansökan hanteras i rätt medlemsstat. | Ansvars-/Dublinersättande modul | Kopplas till förordning (EU) 2024/1351 i stället för Dublin III. Kräver vidare analys mot 2024/1351. |
| 4 | Förhandspröva nya skyddsskäl | Som handläggare vill jag registrera nya omständigheter som kan öka sannolikheten för internationellt skydd, så att systemet stödjer beslut om ansökan ska prövas i sak. | Prövningsstöd | Fortsätter gammal huvudlogik men nu enligt artikel 55.3 a. |
| 5 | Förhandspröva tidigare avvisningsgrund | Som handläggare vill jag kunna registrera nya omständigheter som rör en tidigare avvisningsgrund, så att en tidigare processuell avvisning kan omprövas när det är relevant. | Prövningsstöd | Ny uttrycklig gren i artikel 55.3 b jämfört med äldre huvudformulering om skyddskvalificering. |
| 6 | Bedöma om uppgift är ny | Som handläggare vill jag dokumentera varför en omständighet inte kunde läggas fram tidigare, så att nyhetskravet kan bedömas enligt förordningen. | Prövningsstöd | Artikel 55.5 gör detta mer harmoniserat och bör få eget beslutsstöd. |
| 7 | Hantera undantag från nyhetskravet | Som handläggare vill jag kunna markera att en tidigare möjlig uppgift ändå ska beaktas, så att väsentliga skydds- eller avvisningsfrågor inte tappas bort. | Prövningsstöd | Artikel 55.5 anger undantag, bland annat om uppgiften väsentligt ökar sannolikheten eller om tidigare ansökan var implicit återkallad utan sakprövning. |
| 8 | Besluta om intervju behövs | Som handläggare vill jag att systemet stödjer beslut om förhandsprövningen ska göras skriftligt eller genom personlig intervju, så att skälen blir spårbara. | Ärendehantering | Artikel 55.4 tillåter att intervju avstås när skriftligt underlag tydligt visar att nya element saknas. |
| 9 | Avvisa utan nya element | Som beslutsfattare vill jag kunna fatta beslut om avvisning när inga nya relevanta element finns, så att ansökan inte går till full sakprövning. | Beslutsstöd | Ny hänvisning: artikel 55.7 jämförd med artikel 38.2. |
| 10 | Gå vidare till sakprövning | Som beslutsfattare vill jag att systemet leder ärendet till sakprövning när nya relevanta element finns, så att ansökan behandlas enligt ordinarie materiell prövning. | Workflow | Artikel 55.6, med förbehåll för andra avvisningsgrunder i artikel 38.1. |
| 11 | Flagga försening av verkställighet | Som handläggare vill jag kunna flagga att en första efterföljande ansökan verkar ha lämnats in enbart för att försena ett nära förestående avlägsnande, så att rätt att stanna kan bedömas korrekt. | Återvändande/verkställighet | Artikel 56 a. Kräver tydlig rättssäker dokumentation och non-refoulement-kontroll. |
| 12 | Räkna antal efterföljande ansökningar | Som handläggare vill jag se om ansökan är första, andra eller ytterligare efterföljande ansökan, så att undantag från rätt att stanna kan bedömas korrekt. | Ärendehistorik | Artikel 56 b omfattar andra eller följande efterföljande ansökan i vilken medlemsstat som helst efter tidigare avslag/avvisning. |
| 13 | Visa suspensiv effekt | Som handläggare vill jag se om överklagande automatiskt ger rätt att stanna eller om särskild begäran/beslut krävs, så att verkställighet inte sker i strid med reglerna. | Överklagande/verkställighet | Artikel 68 behöver analyseras närmare mot nationellt processflöde. |
| 14 | Säkerställa non-refoulement-kontroll | Som beslutsfattare vill jag att systemet kräver kontroll av non-refoulement innan undantag från rätt att stanna används, så att verkställighet inte sker i strid med EU-rätt eller internationella åtaganden. | Rättssäkerhetskontroll | Både gamla och nya regler behåller denna spärr, men ny förordning uttrycker den i artikel 56 och 68. |
| 15 | Spåra beslutsgrund | Som jurist vill jag kunna se om beslutet bygger på skyddsskäl, avvisningsgrund, avsaknad av nya element eller rätt att stanna, så att efterföljande ansökningar kan granskas konsekvent. | Rapportering/audit | Viktigt eftersom nya reglerna delar upp fler beslutspunkter än det äldre direktivflödet. |

## Frågor för fortsatt analys

- Hur ska "slutligt beslut" mappas mot svenska beslutstyper och överklagandestadier?
- Vilka register eller EU-system behövs för att identifiera efterföljande ansökningar i annan medlemsstat?
- Hur ska systemet visa att en uppgift rör tidigare avvisningsgrund snarare än nytt skyddsbehov?
- Vilka svenska beslutsmallar påverkas av övergången från direktivets artikel 33.2 d till förordningens artikel 38.2 och 55.7?
- Hur ska rätt att stanna och suspensiv effekt modelleras i gränsfall där överklagande sker samtidigt som verkställighet planeras?

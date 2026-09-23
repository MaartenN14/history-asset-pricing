# Rubriek: cijfer voor de didactische kwaliteit van een lecture (0 tot 10)

Doel: één cijfer per lecture, met per criterium een deelcijfer, wat goed is, wat
mis is (met vindplaats) en wat beter uitgelegd kan worden. De beoordelaar leest de
lecture als een eerstejaars PhD-student die de eerdere lectures heeft gelezen maar
niet paraat heeft. IJkpunt voor een 10: een QuantEcon-lecture zoals
`lucas_model` of `markov_asset` (korte alinea's, motivatie → vergelijking →
interpretatie, één model, leesbare code, directe oefeningen).

## Cijferschaal (geldt per criterium en voor het eindcijfer)

| cijfer | betekenis |
|---|---|
| 9–10 | QuantEcon-niveau. Elke stap is te volgen zonder terug te bladeren; niets hoeft beter. |
| 7–8 | Goed. Alles is te volgen; op enkele plekken kost het moeite of ontbreekt een getal, een naam of een zin. |
| 5–6 | Begrijpelijk met inspanning. De lezer moet zelf gaten vullen of eerdere lectures openen. |
| 3–4 | Grote gaten. Kernstappen zijn niet te volgen, of de lezer leert iets anders dan bedoeld. |
| 0–2 | Niet te volgen. |

## Criteria en gewichten

| nr | criterium | gewicht | wat een 10 is | wat een 5 is |
|---|---|---|---|---|
| 1 | **Helderheid van de uitleg** | 30% | Elk symbool krijgt naam, betekenis en orde van grootte bij de eerste keer. Elk geleend resultaat wordt in één regel herhaald. Bij elke formule waarvan de grootte ertoe doet staat een uitgerekend getal. "Dat" en "dit" verwijzen eenduidig. Abstracte termen krijgen een exemplaar. | Symbolen of resultaten uit eerdere lectures worden aangehaald zonder uitleg; formules zonder getal; de lezer moet raden waar "dat" naar verwijst. |
| 2 | **Opbouw en rode draad** | 20% | Overzicht stelt de vraag en geeft het antwoord. De intuïtie doet een voorspelling die de theorie inlost. Toy, theorie, simulatie en replicatie gebruiken dezelfde getallen. Routekaart vooraan, Samengevat achteraan. Elke sectie begint met haar conclusie. | Secties staan los van elkaar; de intuïtie belooft iets anders dan de theorie levert; de kern is pas na lezen te benoemen. |
| 3 | **Taal** | 15% | Natuurlijk Nederlands, één gedachte per zin, geen vertaald Engels, geen u/je, één naam per begrip, Engelse citaten geparafraseerd of als blokcitaat met inleiding. | Lange stapelzinnen, calques, wisselende namen voor hetzelfde begrip, projectjargon. |
| 4 | **Toy-voorbeeld** | 10% | Met de hand na te rekenen in vijf minuten, één mechanisme, hoogstens één nog niet afgeleide formule, tabel hand/code, één zin wat de lezer nu weet. | Meerdere mechanismen, formules die pas later worden afgeleid, alleen code zonder handstappen. |
| 5 | **Code en figuren** | 10% | Elke cel heeft een zin ervoor en erna. Code leest als de wiskunde: benoemde tussenresultaten, zichtbare lussen waar het proces ertoe doet, geen trucs. Vóór elke figuur staat waarop te letten, erna wat te zien is. | Cellen zonder tekst, compacte trucs, figuren zonder leeswijzer. |
| 6 | **Replicatie en empirie** | 10% | Bron, wat, data, verschil en verwachte afwijking in hoogstens 250 woorden. Tabel origineel/hier. Oordeel begint met Geslaagd / Gedeeltelijk / Niet geslaagd en verwijst naar de verwachte afwijking. Getallen in tabellen, niet in lopende tekst. | Getallenbrij in proza, geen tabel, oordeel ontbreekt of is niet aan de verwachting gekoppeld. |
| 7 | **Oefeningen** | 5% | Instap (variatie op het toy), afleiding, uitbreiding van de replicatie; elke uitwerking eindigt met wat dit leert. | Oefeningen zonder verband met de lecture, uitwerkingen zonder les. |

**Eindcijfer** = gewogen gemiddelde van de zeven deelcijfers, afgerond op één
decimaal. Een lecture met een deelcijfer onder 5 op criterium 1 of 2 krijgt
hoogstens een 6, ongeacht de rest: wat niet te volgen is, is niet didactisch.

## Wat de beoordelaar oplevert: `notes/rating-<slug>.md`

1. **Eindcijfer** en de tabel met de zeven deelcijfers.
2. **Per criterium**, in deze volgorde:
   - *Goed*: twee of drie dingen die werken, met vindplaats (kopje).
   - *Aanmerkingen*: wat mis is, elk met kopje en de zin letterlijk geciteerd.
   - *Beter uitleggen*: welke stap, begrip of formule een lezer niet meekrijgt, en
     wat er nodig is om hem wel mee te krijgen (een getal, een voorbeeld, een
     naam, een zin ervoor). Geen herschrijfvoorstel, wel de aanwijzing.
3. **De drie verbeteringen met het meeste effect op het cijfer**, genummerd, met
   het verwachte nieuwe deelcijfer.
4. **Navertelling in vijf zinnen**: wat de beoordelaar na lezing denkt dat de
   lecture beweert. Wijkt die af van het Overzicht, dan staat dat erbij.

De beoordelaar wijzigt niets aan de lecture en geeft geen stijladvies buiten
criterium 3. Bij twijfel tussen twee cijfers geldt het lagere.

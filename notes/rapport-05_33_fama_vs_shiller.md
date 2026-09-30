STATUS 05_33_fama_vs_shiller F4T words=5839 prose=PASS open=0 cijfer=- min=-

# Rapport 05_33_fama_vs_shiller

**Kern.** Is de variatie in discontovoeten die prijzen en rendementen laten zien een
vergoeding voor risico of een vergissing van beleggers? Koersdata kunnen dat principieel
niet scheiden, omdat prijzen alleen het product van overtuigingen en marginaal nut
vastleggen; enquêtes over verwachtingen kunnen het wel, en die geven het teken van
extrapolatie, al blijft open of de respondenten de prijs zetten.

## F0

`05_33_fama_vs_shiller.md 5729 words, sent_mean 19.6, sent_p90 35, sent_gt40 19, para_mean 72,
semicol 32, motief 5, deel 1, u 1, je 5, calque 14, engquote 23, colon_mid 12.2, tmpl 5
(Waarom zou), connect 19` → FAIL op sent_p90, sent_gt40, para_mean, semicol, motief, deel,
u_form, je_form, calque, engquote, colon_mid, tmpl, connect.

Vijf grootste problemen:

1. Taal overal, vooral Theorie en Replicatie (r. 241–484, 760–959): 19 zinnen boven 40
   woorden, 32 puntkomma's, dubbele punt als lijm, 23 Engelse citaten midden in de zin
   (Overzicht r. 44–58, Theorie r. 266–292, Middenwegen r. 456–465).
2. Structuur: imports-cel aan het eind van Overzicht (r. 75); Overzicht opent met een
   anekdote in plaats van vraag en antwoord; geen routekaart en geen Samengevat in
   Theorie; vijf keer "*Waarom zou dit waar zijn?*".
3. Replicatieblok ≈ 600 woorden (max 250) met getallen en datumdetails (r. 651–704);
   getallenbrij in de lopende tekst na de tabellen (r. 760–778, 884–894, 943–951); geen
   oordeel "Geslaagd / Gedeeltelijk / Niet geslaagd".
4. Projectjargon en aanspreekvorm: "Motief 2/3", drie keer "2%-motief" (r. 50–54, 130,
   634, 881), "deel V" (r. 50), "lecture", "u" (r. 363), vijf keer "je" (o.a. kop Simulatie
   r. 486), werkmelding "de tekst van het artikel konden we niet inzien" (r. 312).
5. Toy en oefeningen: toy-cel eindigt niet met een tabel hand/code; symbool $x$ staat voor
   regressor, vereiste premie en payoff (H7); oefening 1 is geen instap maar een
   afleiding; "Les:" als etiket (r. 1127).

Schraplijst (schraptoets §11.11; eis 2 gecontroleerd met grep op alle labels in
`lectures/`: alleen de paginalabel en `prop-fama-vs-shiller-equivalentie` worden elders
aangehaald, door 06_36; de propositie blijft).

| passage | kopje | woorden | eis niet gehaald | actie |
|---|---|---|---|---|
| Replicatieblok: citaten van tabelgetallen, AAII/Shiller-downloaddetails, stempeldatum | Replicatie | −350 | 1 (details horen in code/rapport) | inkorten tot ≤ 250 |
| Getallenalinea's (1), (2), (3) | Replicatie | −200 | 1 (herhalen de tabellen) | tabel + oordeel |
| Tabel II-getallen en twee Engelse citaten van Cochrane | Theorie, Het feit | −60 | 1 (staan in de replicatietabel) | één zin + blokcitaat |
| Fama 1998-alinea met werkmelding | Theorie, efficiëntie | −60 | 1 | twee zinnen |
| Nobel-anekdote met citaten, motievenalinea | Overzicht | −90 | 1, 3 deels | vraag/antwoord, lijst, één alinea geschiedenis |
| Engelse citaten Martin, Greenwood-Shleifer, Adam-Marcet-Beutel | Theorie | −40 | – | parafraseren |
| Risico of vergissing (230 w), Santa-Clara-slotzin | Wat er brak | −110 | 1 | ≤ 120 woorden |
| Toy: afleidingen (a) en (b) in lopende tekst | Toy | −60 | – | stappen, één regel per stap |
| Warning simulatie | Simulatie | −30 | – | inkorten |

Toevoegingen: routekaart +60, Samengevat +90, instapoefening +160, oordelen +50, zinnen
voor en na cellen +80. Verwachte lengte: 5729 − 1000 + 440 ≈ 5.170 woorden. Geen splitsing
nodig.

## F1

**Eindmeting.** `words 5905, sent_mean 16.8, sent_p90 25, sent_gt40 0, para_mean 54, semicol 3,
motief 0, calque 0, engquote 1, colon_mid 0.2, para_one 1, tmpl 0, connect 31` → PASS op alle
drempels. Lengte 5.905: onder de grens van 6.000, boven het doel van 5.500 (zie open punten).

**Geschrapt of verplaatst** (eerdere agent herschreef alle secties; deze ronde herstelde de rest):
- Engels blokcitaat van Cochrane → Nederlandse parafrase in de lopende tekst (engquote).
- Slotzin Overzicht over "tijdvak van één theorie" → weg, herhaalde de kern.
- Zin over de rationele tegenwerping in Replicatie (2) → weg, staat in "Risico of vergissing?".
- Fama 1998: onderdeel over methodegevoeligheid weg, argument in twee zinnen.
- Motiefverwijzing "standaardfout van 2%" (twee keer) → gewone formulering; calque "in niveaus" weg.
- Replicatieblok: puntkomma-opsommingen omgezet in lijsten per bron, inhoud gelijk.
- 30 zinnen van 29–49 woorden gesplitst; jaartal-aan-zinseinde omzeild (prose_stats knipt
  "NN. " als lijstnummer weg en plakt dan zinnen aan elkaar).
- Twee getalsclaims gecorrigeerd naar de celuitvoer: "in alle rijen op één honderdste na"
  gold alleen voor de directe rijen (VAR-rijen tot 0,027 ernaast); "bijna een kwart groter"
  → "ruim een kwart" (12,6 tegen 10, +26%).

**nb_outputs-diff** (HEAD-ipynb tegen nu, 31+/24−): (1) toy-cel toont nu één tabel "met de
hand / code" in plaats van losse regels plus pad-tabel, getallen gelijk (0,120; 0,086; −0,148;
1,34; ±0,52; ±2,5769); (2) simulatiecel gesplitst in functies + run, daardoor verschuiven
celnummers 4–13 met één; (3) nieuwe oplossingscel oefening 1 (0,28; 0,028; 4,7857);
(4) PNG-groottes van twee figuren licht anders (hertekend, zelfde data). Geen getal dat de
tekst aanhaalt is veranderd; simulatie-, Cochrane-, CFO- en CAPE-uitvoer identiek.

**nb_numbers.** 8 meldingen, alle verklaard: 5,2 (handberekening toy), 15,3/14,0/7,5
(kalibratieconstanten in de code), −0,075 (afronding van −0,0745), 0,122/0,186/0,279
(handberekening oefening 2).

**Afvinklijst STYLE §11.9.** Voldoet, behalve lengte boven het doel van 5.500.

**Labels.** Niets verdwenen; `ex-fama-vs-shiller-4` is nieuw. `prop-fama-vs-shiller-equivalentie`
(aangehaald door 06_36) en de paginalabel staan er nog.

**Open punten voor de feitencontroleur.**
1. CAPE: "van alle decemberwaarden sinds 1881 lag alleen die van 1999 hoger" komt niet uit een cel.
2. Simulatie: meetfout van 4 procentpunt "ongeveer het dubbele van de spreiding van de
   herschaalde enquêtes bij Greenwood en Shleifer" is niet nagerekend.
3. Martins ondergrens "boven 20% in 2008" steunt op 05_29, niet op een cel hier.
4. `SantaClara2026` (Nobelprijs als weergave van het vak) en `CFOSurvey2026`: bib-entries en
   citaatinhoud controleren.
5. CFO-loader staat lokaal in het college (`# TODO: naar hap.data`); hoort in hap.

## F4

Feitenrijen:
- Rij 11 (Opties, Theorie): link naar 05_29 geschrapt; "boven 20% in 2008" steunt nu op {cite}`Martin2017`.
- Rij 16 (Overzicht): parafrase losgemaakt van `SantaClara2026`; de bron draagt alleen "goede weergave van het vak".
- Rij 17 (Simulatie): "dubbele van de GS-spreiding" geschrapt, vervangen door verwijzing naar oefening 4.
Lezerspunten:
1. Middenwegen, tabel: Nagel-Xu-rij vult nu dezelfde kolommen (corr vrijwel nul; geen vast teken, fouten voorspelbaar).
2. Replicatie (1): opent met Cochranes bewering en wat we toetsen.
3. Replicatie (2): opent met het teken dat elk kamp voorspelt.
4. Toy stap 3: tussenstap in woorden (ratio = premie + rho maal verwachte ratio, die phi maal ratio is).
5. Toy: zin na de tabel over het pad, zonder getallen.
6. Theorie, teken van een enquête: K=0,093 nu expliciet "in de simulatie van de volgende sectie, gekalibreerd op Cochranes VAR".
7. Replicatie (1) Geslaagd: sommen en VAR-gevoeligheid in minder getallen.
8. Replicatie (1) tot 2025: jaartal 1995 weg.
9. Replicatie (2): drie correlaties vervangen door verwijzing naar de tabel en -0,443.
10. Replicatie (2): helling en t-waarden uit de tekst; teken en conclusie blijven.
11. Replicatie (3): toets en fout in aparte zinnen. 12. Wat er brak: "feiten bewegen zelf" herschreven.
13. Overzicht: Nobelzin in tweeën. 14. Wat er brak: "Zo werd ... een meetprobleem" herschreven.
15. Oefening 2: "een laag opschuift" vervangen door wat terugkeert (mengsels, zelfde gemiddelde antwoord).
Navertel-toets: geen sectie week af van de bedoeling; Middenwegen verschoof na punt 1 van "tabel onvolledig" naar klopt.
Geschrapt voor lengte: Theorie-inleiding ingekort, dubbele uitleg van eq-equivalentie, tweede zin Middenwegen-inleiding,
laatste Samengevat-bullet (vraag, geen resultaat), herhaalde getallen in Wat er brak, herhaling na simulatiefiguur. 5905 -> 5839.

## R9-1 (F6b, ronde 9+)

- **Feit 1, snelheid φ**: gedaan; toy noemt φ "persistentie" (helft blijft naar verwachting over), ook bij het sentiment.
- **Feit 2, HJ-grens**: gedaan; nu een ondergrens, "noodzakelijk, niet voldoende", sluit alleen te vlakke SDF's uit.
- **Feit 3, Wat er brak**: gedaan; het sterkste bewijs is de significante enquêtehelling op dp; de rendementshelling heet hier niet significant.
- **Feit 4, oefening 4**: gedaan; bij 8 pp blijft de enquête twee keer zo snel als de rendementsregressie (80% pas bij 150 jaar, cel 5).
- **Feit 5, periode tabel III**: gedaan; code en tabel zeggen 1947–2009.
- **Feit 6, schaalfactor**: gedaan; "samen met m̃, op de schaalfactor c_t na".
- **Feit 7, SantaClara2026**: open; de LinkedIn-bron is niet opgehaald (geen webtoegang binnen het budget).
- **Helderheid**: p*_t benoemd als fundamentele prijs; θ bij eerste gebruik als gevoeligheid; "schema" → "decompositie" (3×), "restterm" → "eindterm", "uitkeringsgroei" → "dividendgroei"; tabelkop PD → −dp; bijzin bruto R → log r (constante variantie raakt alleen het intercept).
- **Opbouw**: overgang naar opties/flows/consumptie herschreven ("meten ξ of m apart, elk met een eigen aanname").
- **Taal**: routekaart in twee zinnen; komma r. 422 weg; "Langs dezelfde lijn" herschreven; zin over bijna honderd kwartalen herschreven; aslabel "Log prijs-dividendratio".
- **Toy**: stap 3 noemt verwachte dividendgroei nul (afwijking van gemiddelde) en dat het pad een realisatie met schokken is, geen AR(1)-verwachting.
- **Code en figuren**: regressiecel geeft één smalle tabel (regressie × regressor; b, t, R2, N); eenjaarsregressies als tabel hier/Cochrane tabel III; zin na de cel wijst naar −0,029 met t = −3,7. Berekening ongewijzigd, uitvoer na nbconvert (offline) getalsgewijs gelijk.
- **Replicatie**: admonition ingekort tot ~205 woorden (tijdschriftnaam, Graham-Harvey-bijzin, opblaasfactor, "te downloaden" weg); oordelen (1)–(3) verwijzen naar de verwachte afwijking en naar tabel/uitvoer; getallen uit de oordeelalinea's (1) en (3) naar de tabel; (3) noemt het niveauverschil expliciet "niet voorzien".
- **Oefeningen**: zie feit 4.
- Woorden: 5.985 (was 5.839); prose_stats PASS; nb_numbers: geen nieuwe meldingen (7 oude, toy/kalibratie/oefening 2).

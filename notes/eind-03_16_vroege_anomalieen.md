STATUS 03_16_vroege_anomalieen F6c words=5276 prose=PASS open=0 cijfer=8,9 min=8,5

# Eindbeoordeling F6: Basu, Banz en Rosenberg (03_16_vroege_anomalieen)

Cijfer van record volgens `plannen/rubriek-didactiek.md` en `plannen/kaart-rollen.md` §8.
Zelfde kalibratie als de beoordelingen van 03_10–03_12 en de eindbeoordelingen van
Deel II.

## De drie verbeteringen met het meeste effect

1. **Opbouw (8 → 8,5).** Eén simulatievraag en één empirische lijn. De Fama-MacBeth-
   variant van simulatie (a) en de formulecontrole van (b) naar een oefening of
   dropdown, en "Fama-MacBeth met bèta en marktwaarde" in de replicatie naar een
   oefening. De Rosenberg/Barra-alinea in Fama-MacBeth met kenmerken inkorten volgens
   de schraptoets.
2. **Replicatie (8 → 8,5).** In de verwachte afwijking ook het januari-effect en de
   richting na publicatie noemen, en de getallen na de januaritabel en de
   Fama-MacBeth-cel ("10,3%", "78%", "82%", "5,6%", "$-0{,}49\%$", "$t = -2{,}57$",
   "$-0{,}11\%$", "0,73%") vervangen door een verwijzing naar de tabel en één
   conclusie.
3. **Taal en code (8 → 8,5 elk).** De zin over Barra en de code-namen in de lopende
   tekst van simulatie (b) herschrijven, zeven puntkomma's splitsen; in de code de
   drievoudige dict-comprehensions (`rows`, `panels`, `january`) als lussen en de
   simulatieparameters in één dict.

Samen met de feitelijke fout: 2,55 + 1,70 + 1,275 + 0,90 + 0,85 + 0,85 + 0,45 =
8,575, dus 8,6.

## Eindcijfer: 8,3

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,55 + 1,60 + 1,20 + 0,90 + 0,80 + 0,80 + 0,45 = 8,30, dus 8,3.
Laagste deelcijfer 8. Lengte: 5.275 woorden volgens `prose_stats` (PASS); gemiddelde
zinslengte 16,1 woorden, één zin boven 40, veertien puntkomma's (waarvan zeven in
lopende tekst). Replicatieblok: 201 woorden.

## Feitelijke fouten

Nagerekend met de hand en tegen de celuitvoer (`tools/nb_outputs.py`; de notebook is
na de .md bijgewerkt). Correct: het toy (marktrendement 6,0%; marktbèta 1,000; alpha's
$-1{,}50$, 0,10, 1,50, 3,00, 6,25; H 0,675, 8,00, 3,375, 4,625; L 1,050, 4,55, 5,25,
$-0{,}70$; H − L $-0{,}375$, 3,45, 5,325); de Fama-MacBeth-gewichten
($-8, -4, -2, 4, 10$; kwadratensom 0,005); de standaardfout (Sharpe 0,11, correctie
1,01, $5/\sqrt{480} = 0{,}23\%$, 2,7% per jaar; veertien en twaalf jaar); het bewijs
van Berk (totale covariantie); Lo-MacKinlay ($\varphi(1{,}2816)/0{,}1 = 1{,}755$,
$\sqrt{200} \cdot 1{,}755 = 24{,}8$; $1 - 0{,}975^{20} = 0{,}40$); simulatie (a)
(12,6%; $-0{,}19$; 0,076 tegen 0,079; 18,6% en 2,4%; bijna 1 pp per jaar;
$-0{,}069$ met $t = -4{,}18$, $-0{,}031$ met $t = -2{,}24$); simulatie (b) (92,5%, 12%;
2,36 tegen 2,48; na de steekproef binnen 0,15); de replicatietabel (alle twaalf
alpha's en $t$-waarden, negatieve bèta's van E/P en B/M, 17% per jaar, 0,14% en
0,44); januari (10,3%; 78% en 82%; 1926–1962; 5,6%, $-0{,}49\%$, $t = -2{,}57$);
Fama-MacBeth van Banz ($-0{,}11\%$, $t = -1{,}55$; 0,73% → $-0{,}12\%$); de
oefeningen (0,75; 7,33%; 3,58%; 4,28%; covariantie en correlatie, factor 1,84;
65%, 67%, 24%, 45%; 0,78% met $t = 4{,}17$). Keim (bijna vijftig procent, meer dan
de helft in de eerste week) en Reinganum (twee jaar, misspecificatie) kloppen met hun
samenvattingen. Niet geverifieerd: Nicholsons "tien tegen één",
{cite:t}`AsnessFrazziniIsrael2018` met $t = 1{,}82$ en de CRSP-correcties, en dat
Bhandari zijn effect "vooral in januari" vond.

1. **Theorie → Het kernresultaat, na de stelling.** "E/P en B/M zijn betere
   thermometers, want hun noemer haalt een deel van die ruis weg." De noemer van E/P
   en B/M is de marktwaarde zelf. Wat de ruis van het kasstroomniveau weghaalt, is de
   teller (winst, boekwaarde), die met $C_i$ meeschaalt. Oefening 2 zegt het wel
   goed ("hoe minder ruis in het kasstroomniveau").

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- **Theorie, alle subsecties.** Elke `###` begint met haar conclusie ("Een
  portefeuillesortering schat het verwachte rendement als functie van een kenmerk,
  zonder die functie een vorm op te leggen"; "Een kenmerk dat in de data is gezocht,
  maakt in diezelfde data een grote $t$-waarde, ook als er niets is").
- **De alpha van een long-short-portefeuille.** De formule krijgt direct een getal
  met kalibratie (0,23% per maand na veertig jaar, bijna 3% per jaar) en de
  consequentie voor Basu en RRL.
- **Data snooping.** De formule wordt in één regel uitgerekend ($24{,}8\,\rho$) en in
  woorden gelezen ("één procent van de variantie [...] dan is de verwachte $t$ al
  2,5"), en de simulatie bevestigt haar.

*Aanmerkingen*
- Het kernresultaat: "want hun noemer haalt een deel van die ruis weg" (feitelijke
  fout 1).
- $h$ is in simulatie (a) de tweede factor ("een tweede beprijsde factor $h$") en in
  het bewijs van Berk de functie "$h(x) = \log(x - g)$". De botsing wordt niet
  gemeld.
- Intuïtie: "De antwoorden waren bijna tien tegen één in het voordeel van de dure
  aandelen. De latere literatuur citeert Nicholson als vroeg bewijs dat juist de
  goedkope het beter deden; zijn tabellen hebben we niet kunnen inzien." De lezer
  weet na de alinea niet wat Nicholson vond, en "Dat is het verhaal van Nicholsons
  analisten" verwijst naar een uitkomst die niet is vastgesteld.
- Simulatie (a), Fama-MacBeth: "De regressie krijgt de ware bèta, zonder meetfout,
  en de gestandaardiseerde $\log \mathrm{ME}$." Waarom de ware coëfficiënt op
  $\log \mathrm{ME}$ met $\delta$ erbij nul is (het verwachte rendement is lineair in
  $\beta$ en $\delta$), staat er niet.

*Beter uitleggen*
- Nicholson: één zin wat zijn onderzoek vaststelde (een enquête naar verwachtingen,
  geen rendementsstudie?) en wat de latere literatuur eraan toeschrijft, gescheiden.

*Voor een 9*
- Feitelijke fout 1 herstellen (Het kernresultaat).
- De tweede factor een andere letter geven of de botsing melden (Simulatie (a); bewijs
  van Berk).
- De Nicholson-alinea ondubbelzinnig maken (Intuïtie).

### 2. Opbouw en rode draad (8)

*Goed*
- De drie verwachtingen uit de intuïtie worden elk ingelost: de tweede bij Berk
  ("Dit lost de tweede verwachting uit de intuïtie in, met een verfijning"), de derde
  bij Lo-MacKinlay, de eerste in het replicatieoordeel.
- Het toy loopt door: stap 4 bij de long-short-alpha, de Fama-MacBeth-gewichten op
  dezelfde vijf aandelen, de simulatie ("Zoals in stap 4 van het toy-voorbeeld") en
  oefening 1.
- De naden kloppen: 03_15 eindigt met "Dat vonden Basu, Banz en Rosenberg in de
  cross-sectie", 03_17 begint met "[Basu, Banz en Rosenberg] vonden kenmerken die
  rendementen voorspelden buiten het CAPM om".

*Aanmerkingen*
- Simulatie: twee werelden, met in (a) een tweede analyse (Fama-MacBeth op losse
  aandelen) en in (b) een derde (de formulecontrole voor $\rho = 0$ tot 0,20). STYLE
  §11.7: "Simulatie beantwoordt één vraag over steekproeven."
- Replicatie: drie lijnen (long-short-alpha's met decielfiguur, het januari-effect,
  Fama-MacBeth van Banz), waarvan de laatste zonder oordeel eindigt ("Tien
  portefeuilles die op omvang zijn gesorteerd, kunnen bèta en omvang niet scheiden").
- Fama-MacBeth met kenmerken: de alinea over Rosenberg en Barra ("Met dezelfde
  kenmerken bouwde Rosenberg dus een instrument dat werkte") is een nevenlijn; ze
  draagt het motief, maar de lecture komt er niet op terug.

*Beter uitleggen*
- Geen.

*Voor een 9*
- Eén simulatie met één vraag; de Fama-MacBeth-variant en de formulecontrole naar
  een oefening of dropdown (Simulatie).
- De Fama-MacBeth van Banz naar een oefening (Replicatie).
- De Barra-alinea inkorten tot twee zinnen (Fama-MacBeth met kenmerken).

### 3. Taal (8)

*Goed*
- Geen u/je, geen calques of stopwoorden volgens `prose_stats`; de motieven zeggen ter
  plekke wat ze betekenen ("Dat is de standaardfout van 2% uit [](#00-01-rendementen),
  nu voor een alpha").
- *Window dressing* en *anomalie* krijgen een Nederlandse uitleg in dezelfde zin.

*Aanmerkingen*
- Fama-MacBeth met kenmerken: "Rosenbergs bedrijf Barra, dat in 1975 het eerste
  commerciële multifactor-risicomodel voor Amerikaanse aandelen uitbracht, nam hun
  covariantiematrix, een goed gemeten tweede moment: elke maand levert een nieuwe
  waarneming van de schommelingen zelf, terwijl de ruis in een gemiddelde pas over
  decennia uitmiddelt." Een stapelzin met drie gedachten.
- Simulatie (b): "In de cel trekt `rng.standard_normal((n_cand, n_sn))` de honderd
  ruiskenmerken, en `long_short_weights` zet [...] Kolom 0 (`t_in[0]`) is het vooraf
  gekozen kenmerk, `np.argmax(t_in)` het beste van honderd." Code in lopende tekst.
- Zeven puntkomma's in lopende tekst, onder meer "Of 5,3% toeval is, zegt één periode
  niet; daarvoor is een tijdreeks nodig." en "De benadering ligt dicht bij de
  steekproefwaarden; het verschil komt van de kromming van de logaritme."
- Gemiddelde zinslengte 16,1 woorden, hoger dan de 13,9–14,1 van 03_10–03_12.

*Beter uitleggen*
- Geen.

*Voor een 9*
- De Barra-zin in twee of drie zinnen splitsen; de code-namen uit de tekst van
  simulatie (b) halen (de cel mag ze in commentaar dragen); de puntkomma's splitsen.

### 4. Toy-voorbeeld (9)

*Goed*
- Opzet-tabel, één recept (de Jensen-alpha, geleend uit [](#02-08-capm) en herhaald),
  vier stappen met getallen die exact uitkomen, één cel, tabel hand/code en een zin
  "Wat we nu weten".
- Het toy draagt het mechanisme van de lecture (sortering levert alpha, maar niet
  welk kenmerk het werk doet) en de vraag van Reinganum.

*Aanmerkingen*
- Geen van gewicht.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8)

*Goed*
- `alpha_t` en `january_split` hebben een docstring en benoemde tussenresultaten; de
  steekproeflussen van de simulatie zijn zichtbaar.
- Elke figuur heeft een leeswijzer vooraf ("Let op de vorm: stijgt de alpha van
  deciel 1 naar deciel 10") en een bijschrift dat de uitkomst zegt.

*Aanmerkingen*
- Drievoudig geneste dict-comprehensions om tabellen te bouwen: "`rows = {(sort,
  label, w): capm_row(...) for sort, spans in periods.items() for label, (a, b) in
  spans.items() for w in (\"VW\", \"EW\")}`", en zo ook `panels`, `january` en de
  tabel in oefening 3.
- Simulatieparameters als losse globals: "`lam_m, sd_m, lam_h, sd_h, sd_eps = 0.005,
  0.045, 0.004, 0.030, 0.10`" (STYLE §11.8 vraagt een dict of dataclass).
- "`size_rank = stats.rankdata(log_me).astype(int) - 1`" met
  "`group = size_rank * n_groups // n_stocks`" en "`(is_long.astype(float) -
  is_short) / n_leg`": compacte trucs.
- "`out.attrs = {}`" twee keer, zonder uitleg.

*Beter uitleggen*
- Geen.

*Voor een 9*
- De tabellen met gewone lussen bouwen (Replicatie, januari, oefening 3); de
  parameters van simulatie (a) in een dict; de decielindeling met `pd.qcut` of een
  benoemde stap; `out.attrs = {}` toelichten of weghalen.

### 6. Replicatie en empirie (8)

*Goed*
- Replicatieblok van 201 woorden, eerlijk over wat niet is nagelezen ("Hun
  tabelwaarden per portefeuille hebben we niet in de primaire bronnen kunnen nalezen,
  dus we toetsen teken, orde van grootte en rangorde").
- Tabel origineel / oorspronkelijke steekproef / na publicatie; het oordeel begint met
  "Geslaagd", verwijst naar de verwachte afwijking en noemt drie patronen die met de
  bronnen kloppen.
- De decielfiguur met foutbalken laat zien waarom size in Banz' periode niet
  significant is.

*Aanmerkingen*
- Verwachte afwijking: alleen het teken van de long-short-alpha. Voor het
  januari-effect en de richting na publicatie is niets verwacht, en toch begint de
  januarisectie met "**Geslaagd.**"
- Getallen in lopende tekst: "verdiende de equal-weighted klein-min-groot-portefeuille
  in januari gemiddeld 10,3% [...] Januari draagt 78% van de jaarpremie,
  value-weighted 82%" en "Na 1980 levert januari equal-weighted nog 5,6% op, maar [...]
  ($-0{,}49\%$ per maand, $t = -2{,}57$)"; in de Fama-MacBeth-alinea vier getallen.
- Fama-MacBeth met bèta en marktwaarde: eindigt zonder oordeel en zonder origineel
  (Banz' eigen coëfficiënt).

*Beter uitleggen*
- Geen.

*Voor een 9*
- De verwachte afwijking uitbreiden met januari (het grootste deel van de size-premie
  in januari) en na publicatie (kleinere value-weighted alpha's).
- De januari- en Fama-MacBeth-getallen naar een verwijzing naar de tabel; de
  Fama-MacBeth-sectie schrappen of met een oordeel afsluiten.

### 7. Oefeningen (9)

*Goed*
- Oefening 1 varieert het toy (C in H, met de les over brede decielen), oefening 2
  leidt de orde van grootte van Berk af en controleert haar, oefening 3 breidt de
  januarisplitsing uit naar value; elke uitwerking eindigt met "Wat dit leert:".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

## Navertelling in vijf zinnen

In de oorspronkelijke steekproeven van Basu, Banz en Rosenberg hadden goedkope en
kleine aandelen een positieve CAPM-alpha, vooral equal-weighted, terwijl hun bèta niet
hoger was. Een sortering is een regressie zonder vorm, en een Fama-MacBeth-helling op
een kenmerk een long-short-portefeuille; beide meten dat er iets is, niet welk
kenmerk het werk doet. Berk laat zien dat marktwaarde het verwachte rendement
voorspelt zodra verwachte rendementen verschillen, ook bij correcte prijzen, en Lo en
MacKinlay dat een gezocht kenmerk een grote $t$-waarde maakt die buiten de steekproef
verdwijnt. De simulatie toont beide kanten: een echte premie blijft na veertig jaar
meestal onzichtbaar, en het beste van honderd ruiskenmerken is bijna altijd
significant. Na publicatie krimpen de value-weighted alpha's, en de size-premie bleek
grotendeels een januari-effect dat na 1980 buiten januari omsloeg.

Dit komt overeen met het Overzicht.

## Controle 1

Gecontroleerd tegen `notes/rapport-03_16_vroege_anomalieen.md` §F6-1, de lecture en de
nieuwe celuitvoer. `prose_stats`: 5.276 woorden, gemiddeld 16,0 woorden per zin, geen
zin boven 40, zeven puntkomma's (alleen lijsten, Bron-regel en tabellen), PASS.

**Proza tegen cel.** Simulatie (b): de cel geeft 93,2% ($t > 1{,}96$) en 13,8%
($t > 3$) voor het beste van honderd, gemiddelde 2,52; het vooraf gekozen kenmerk
0,03 met SD 1,00; erna 0,07. De tekst ("93,2%", "13,8%", "gemiddelde $t$ rond nul en
een standaarddeviatie rond één", "In de twintig jaar erna is er niets van over", en in
de inleiding "ruim negen op de tien") klopt met de cel. Simulatie (a) is ongewijzigd
($-0{,}19$; 0,076 tegen 0,079; 18,6%; 2,4%). Oefening 2 (4): $-0{,}027$ met
$t = -1{,}57$ en met $\delta$ 0,008 met $t = 0{,}54$, zoals de uitwerking zegt.
Oefening 4 (Banz): dezelfde getallen als voorheen, tekst klopt. Replicatie, januari en
oefening 3: uitvoer ongewijzigd.

| punt | status | vindplaats |
|---|---|---|
| Fout 1: "hun noemer" | opgelost | "hun teller (winst, boekwaarde) schaalt mee met het kasstroomniveau" |
| $h$ dubbel | opgelost | de functie heet $\psi$ in het bewijs van Berk en in oefening 2 |
| Nicholson | opgelost | "Bijna tien tegen één verwachtten ze meer van de dure aandelen. Meer stelde zijn enquête niet vast." |
| Waarom de ware coëfficiënt nul is | opgelost | oefening 2 (4): "lineair in bèta en $\delta$" |
| Eén simulatievraag | deels | Fama-MacBeth-variant naar oefening 2 (4), formulecontrole geschrapt; de twee werelden blijven, onder één vraag en één figuur (verweer aanvaard) |
| Fama-MacBeth van Banz | opgelost | oefening 4, met "Wat dit leert" |
| Barra-alinea | opgelost | drie zinnen |
| Verwachte afwijking: januari en na publicatie | opgelost | replicatieblok; beide oordelen verwijzen ernaar |
| Januari-getallen in lopende tekst | opgelost | "kolom bijdrage januari" en één conclusie |
| Barra-stapelzin | opgelost | gesplitst |
| Code-namen in de tekst van (b) | opgelost | naar commentaar in de cel |
| Puntkomma's in lopende tekst | opgelost | geen meer |
| Gemiddelde zinslengte | niet | 16,0; binnen de norm, geen "Voor een 9"-punt |
| Dict-comprehensions | opgelost | `panels`, `rows`, `january_rows` en oefening 3 als lussen |
| Simulatieparameters | opgelost | dict `sim` |
| Decielindeling, gewichten | opgelost | `pd.qcut`; `long_short_weights` in benoemde stappen |
| `out.attrs = {}` | opgelost | met commentaar |

Geen nieuwe feitelijke fouten, geen verslechteringen. Wat blijft:
- Replicatie: de alinea na het oordeel herhaalt nog vier tabelgetallen ("1,42% per
  maand, ongeveer 17% per jaar", "0,14%", "0,44").
- Opbouw: twee werelden in de simulatie en twee empirische lijnen (long-short-alpha's
  en januari); dezelfde aftrek als bij 03_10–03_12.

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8,5 | 9 |
| 2 | Opbouw | 8 | 8,5 |
| 3 | Taal | 8 | 9 |
| 4 | Toy | 9 | 9 |
| 5 | Code en figuren | 8 | 9 |
| 6 | Replicatie | 8 | 8,5 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,70 + 1,70 + 1,35 + 0,90 + 0,90 + 0,85 + 0,45 = 8,85, dus 8,9. **Eindcijfer
van record 8,9, laagste deelcijfer 8,5.** Streefcijfer gehaald.

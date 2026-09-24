STATUS 02_07_event_studies F6 words=4886 prose=PASS open=0 cijfer=8,6 min=8,5

# Eindbeoordeling F6: 02_07_event_studies (De event study)

Eindbeoordelaar A, Deel II. Cijfer van record volgens `plannen/rubriek-didactiek.md`.

## Eindcijfer: 8,6

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

8,5·0,30 + 8,5·0,20 + 8,5·0,15 + 9·0,10 + 8,5·0,10 + 8,5·0,10 + 9·0,05 = 8,575 → 8,6.
Laagste deelcijfer 8,5.

## Feitelijke fouten

Geen.

Nagerekend en correct: toy (α, β, residuen en $\hat\sigma^2$ van A, B en C; AR's en
CAR's 2,5/2,0/1,5; factor $3 + 9/5 + 1/10 = 4{,}9$; $J_1 = 2{,}509$, naïef 3,207;
28% te hoog); 8% en 50% extra variantie; $\delta = 2{,}24$ met kracht 61%, 1,29 met
25%; 0,024% per dag en $21^2 \approx 440$; $\sqrt{3{,}45} = 1{,}86$ en 29%; 15% over
750 dagen; $\E[J_1] = 0{,}17$ en 2,7; simulatie 62,9%, 99,2%, 94,7%, mist 82% bij
[−10,+10] en $N = 100$; nulfrequenties 3,5–6,0% met één cel buiten ±1,4 pp;
63% → 0,4%; 102 splitsingen, 50 aandelen, 6183 dagen; $L_1$ 495, bèta 1,08,
residuele volatiliteit 1,8%; CAAR 14,9% (SE 3,7), $J_1$ 4,0, BMP 4,7, KP 4,47;
ex-datum −0,08% en −0,40; [0,60] −2,9% (SE 1,6), −1,84 en −1,18; ρ ≤ 0,0012;
$\eta = -0{,}05\%$ per dag ≈ −12% per jaar; oefeningen (1,3, 1,9, 4,628; 9,2%, 7,1%,
6,0%; 4,3% en 69%).

## 1. Helderheid van de uitleg (8,5)

*Goed*
- **Het kernresultaat.** De variantieformule staat met benoemde termen ("fout in
  $\hat\alpha_i$", "fout in $\hat\beta_{i,m}$") en met getallen voor $L_2 = 21$ en voor
  het jaarvenster van de replicatie (8% en 50%).
- **De toets en zijn kracht.** Elke formule heeft een getal: 61% en 25% voor de
  kracht, 29% voor de te vaak verwerpende toets, 0,17 en 2,7 voor de lange horizon.
- Geleende toetsen (Patell, BMP, Kolari-Pynnönen) krijgen elk één zin met wat ze doen
  en waarom.

*Aanmerkingen*
- **Opzet.** "hier is het met {cite:t}`MacKinlay1997` het netto rendement". De
  afwijking van de notatie is aangekondigd, maar de setup vraagt om naar de reeksnotatie
  te vertalen (naad 1). Een lezer met $R$ = bruto in het hoofd leest $R_{i,\tau}$ in de
  toy als 1,5 in plaats van 1,5%.
- **De toets en zijn kracht.** "De toetsstatistiek (bij {cite:t}`MacKinlay1997` heet
  ze $\theta_1$)", terwijl $\boldsymbol{\theta}_i$ drie alinea's eerder de vector
  $(\alpha_i, \beta_{i,m})'$ is.
- **De toets en zijn kracht.** "Zonder zo'n verhoging is $s_{\text{SCAR}} \approx 1$ en
  liggen $J_1$ en BMP dicht bij elkaar: in de replicatie 4,0 en 4,7." Een verschil van
  0,7 in de $t$-waarde heet "dicht bij elkaar" zonder dat de lezer hoort waar het vandaan
  komt.
- **Intuïtie.** "Een premie van 6% per jaar is per dag 0,024%, tegen een dagelijkse
  marktruis van 1% [...] Een nieuwsfeit van 1% op een bekende dag staat tegen 2% ruis van
  één aandeel". Twee verschillende noemers (markt- en aandeelruis) in één vergelijking,
  zonder dat gezegd wordt waarom.

*Beter uitleggen*
- Eén zin waarom BMP hoger uitkomt dan $J_1$ (de SCAR's spreiden minder dan hun
  standaardfouten voorspellen).
- Noem de toetsstatistiek van MacKinlay in de tekst niet $\theta_1$, of zeg dat het een
  andere $\theta$ is.

## 2. Opbouw en rode draad (8,5)

*Goed*
- **Overzicht** geeft vraag en antwoord; de **Intuïtie** voorspelt precies het patroon
  dat de replicatie toetst (stijging vooraf, nul op de ex-datum, vlak erna) en de
  toetskracht die de simulatie meet.
- De toy-getallen keren terug: de CAAR van 2% als effectgrootte in de simulatie, de
  4,9 tegen 3 als maat voor de schattingsfout.
- **Simulatie** begint met haar uitkomst; de Samengevat-lijst eindigt met de vraag van
  de simulatie.

*Aanmerkingen*
- **Overzicht.** "Zo gemeten verwerken prijzen publiek nieuws snel, en grotendeels al
  vóór de publicatie." De replicatie meet rond de ex-datum en kan de aankondiging niet
  zien ("Voor aankondigingsdatums is er geen gratis bron"); het antwoord steunt op Ball
  en Brown, niet op de eigen meting.
- **De toets en zijn kracht, halfwaardetijd.** Een zijlijn met drie citaties en een
  Engels citaat in de Intuïtie, die de replicatie niet kan toetsen ("binnen een dag dus
  het scherpste antwoord").
- De Theorie telt zeven onderdelen (verdeling, CAR-variantie, $J_1$, BMP, kracht,
  halfwaardetijd, clustering met KP, lange horizon); de kern is goed te benoemen, maar
  het is veel.

*Beter uitleggen*
- In het Overzicht onderscheiden wat de literatuur zegt (vóór de publicatie) en wat de
  replicatie laat zien (vóór de ex-datum).

## 3. Taal (8,5)

*Goed*
- Natuurlijk Nederlands, gemiddeld 15,1 woorden per zin, geen zinnen boven 40.
- Engelse termen krijgen een vertaling of uitleg (*joint hypothesis* (gezamenlijke
  hypothese), *bad model problem*, *drift*).

*Aanmerkingen*
- **Wat er brak.** "een van de meest succesvolle instrumenten van de empirische
  financiering". Calque van *empirical finance*; "financiering" is *financing*. De
  setup schrijft "de empirische finance" (naad 9).
- Wisselend lidwoord bij één begrip: "het CAR stijgt", "Het CAR is de som" naast
  "de variantie van een CAR" en "de CAR's"; "de CAAR [...] haar standaardfout" naast
  "een CAAR dat" en "Het CAAR van −2,9%".

*Beter uitleggen*
- Kies één lidwoord voor CAR en CAAR.

## 4. Toy-voorbeeld (9)

*Goed*
- Drie aandelen met ronde getallen: alles is met de hand na te rekenen, en de tabel
  hand/code toont zeven identieke getallen.
- Eén mechanisme (de schattingsfout in de variantie), één nog niet afgeleide formule
  met een aankondiging dat de Theorie haar afleidt, en een slotzin met wat de lezer
  weet (28% te hoge $t$-waarde).

*Aanmerkingen*
- Vijf stappen met drie regressies kosten eerder tien dan vijf minuten.

*Beter uitleggen*
- Geen.

## 5. Code en figuren (8,5)

*Goed*
- De toy-code volgt de vijf stappen met commentaar per stap.
- Beide figuren hebben een leeswijzer ("Let op hoe de lijnen naar rechts verschuiven")
  en een bijschrift dat de vraag beantwoordt.
- `car_variance` wordt gekoppeld aan [](#eq-eventstudies-varcar) in matrixvorm.

*Aanmerkingen*
- **Simulatie, `simulate_events`.** Arrays met vorm `(r, 1, T)` en `(r, n_events, T)`,
  blokken van 250 en een `dict` van lijsten: correct en toegelicht, maar de lezer moet
  de broadcasting zelf volgen.
- **Replicatie, `split_tests`.** De gewogen correlatie (`overlap * np.nan_to_num(...)`,
  gedeeld door $n(n-1)$) is één zin toelichting ("daarmee wegen we haar") voor een
  eigen constructie die niet in de Theorie staat.

*Beter uitleggen*
- Eén zin vóór `split_tests` die de gewogen $\hat{\bar\rho}$ als formule geeft.

## 6. Replicatie en empirie (8,5)

*Goed*
- Het blok heeft bron, wat, data, verschil (maand tegen dag, selectie achteraf) en een
  verwachte afwijking met een drempel ($\lvert t \rvert < 2$).
- Tabel FFJR/verwachting/hier, oordeel "Geslaagd" dat de drie voorwaarden afloopt.
- De kanttekeningen (selectie, ex-datum in plaats van aankondiging, kleine $\rho$) en de
  tweede lezing van −2,9% als modelfout.

*Aanmerkingen*
- De kolom "FFJR" is kwalitatief ("stijgt gestaag"); het niveau wordt niet vergeleken.
  Eerlijk gemeld, maar de toets is daardoor zwak.
- **Replicatie, na de tabel.** "een modelfout van $\eta = -2{,}9\%/61 \approx -0{,}05\%$
  per dag, ruim 10% per jaar" staat in lopende tekst en niet in de tabel.

*Beter uitleggen*
- Geen.

## 7. Oefeningen (9)

*Goed*
- Instap op het toy, afleiding (constant-mean-model), uitbreiding van de replicatie
  (Brown en Warner op echte data): de drie soorten.
- Elke uitwerking eindigt met wat ze leert; oefening 3 legt uit waarom 69% boven 63% ligt.

*Aanmerkingen*
- **Uitwerking ex-eventstudies-1 (2).** Het antwoord ("Het signaal zat op dag 0")
  herhaalt de vraag; een getal (de factor 4,9 tegen 1,3 bij een signaal van 2,0 tegen
  1,9) zou het tonen.

*Beter uitleggen*
- Geen.

## De drie verbeteringen met het meeste effect

1. In het Overzicht scheiden wat Ball en Brown laten zien (vóór de publicatie) en wat
   de replicatie laat zien (vóór de ex-datum), en de halfwaardetijd inkorten tot één
   alinea (opbouw 8,5 → 9).
2. Notatie in lijn brengen met de setup ($r_{i,\tau}$ netto, of vertalen) en
   $\theta_1$ hernoemen; één zin over waarom BMP hoger is dan $J_1$ (helderheid 8,5 → 9).
3. "empirische financiering" vervangen en één lidwoord voor CAR en CAAR (taal 8,5 → 9).

## Navertelling in vijf zinnen

Een event study legt alle gebeurtenissen op tijd nul, trekt van elk rendement af wat
het marktmodel voorspelt en middelt de rest, zodat de ruis met de wortel van het aantal
events krimpt en het signaal blijft. De variantie van een CAR is de ruis van de
eventdagen plus de schattingsfout in alfa en bèta, en wie die fout vergeet overschat zijn
$t$-waarde. Met een bekende eventdag vindt de toets een effect van 1% al met twintig
events, maar een langer venster, events op dezelfde dag en vooral lange horizonnen maken
haar onbetrouwbaar, omdat een modelfout lineair groeit en de ruis met de wortel. Op 102
splitsingen uit 2004–2025 herhaalt zich het patroon van FFJR: de koers stijgt in het jaar
ervoor, op de ex-datum gebeurt niets, en daarna is er geen significante drift. Of een
resterende drift risico of vergissing is, kan de event study niet beslissen, omdat ze
een model voor het normale rendement nodig heeft. Dit komt overeen met het Overzicht,
behalve dat de replicatie zelf niet laat zien dat de prijs "vóór de publicatie"
reageert.

## Controle

STATUS 02_07_event_studies F6c words=4927 prose=PASS open=0 cijfer=8,9 min=8,5

Gecontroleerd tegen `rapport-02_07_event_studies.md` §F6-1 en de lecture zelf, ná de
omzetting van "alfa" naar "alpha".

| punt | status | toelichting |
|---|---|---|
| Verbetering 1a, Overzicht | opgelost | het replicatiepunt zegt nu "de koers stijgt vóór de ex-datum [...] Het moment van publicatie zelf meten we daar niet; dat bewijs komt van Ball en Brown" |
| Verbetering 1b, halfwaardetijd inkorten | deels | de Budish-zin is weg; de rest van de alinea en het Engelse citaat in de Intuïtie staan er nog |
| Verbetering 2a, notatie | opgelost | $r_{i,\tau}$ en $r_{m,\tau}$ zijn netto, ook in toy en oefeningen; één bijzin zegt dat MacKinlay $R$ schrijft |
| Verbetering 2b, $\theta$ | opgelost | de parametervector heet $\mathbf{b}_i$; $\theta_1$ is alleen de naam bij MacKinlay |
| Verbetering 2c, BMP hoger dan $J_1$ | opgelost | "Standaardiseren geeft bovendien de zeer volatiele aandelen minder gewicht, terwijl zij in $J_1$ de noemer domineren" |
| Verbetering 3, taal | opgelost | "empirische finance"; overal "het CAR" en "het CAAR", met "zijn" |
| Naad 1, $R$ netto | opgelost | zie 2a |
| Naad 2, $\alpha_i$ | opgelost | "hier een intercept op netto rendementen, geen pricing error of Jensen-alpha" |
| Naad 5, $\tau$ | opgelost | "Let wel: $\tau$ is hier eventtijd, niet het moment van schrappen" (in L5 heet dat nu $\theta$) |
| Naad 9, financiering | opgelost | zie 3 |
| Boekconventie "alpha" | opgelost | geen "alfa" meer in L5, L7 of de setup |

Geen verslechteringen en geen nieuwe feitelijke fouten. Volgens het rapport is de
code-uitvoer gelijk aan F5; de getallen in de gewijzigde zinnen (4,7 tegen 4,0) kloppen
met de tabel. Nog open, niet verplicht: de Intuïtie vergelijkt de premie van 6% met
marktruis en nieuws van 1% met de ruis van één aandeel, zonder te zeggen waarom de
noemers verschillen.

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid | 30% | 8,5 | 9 |
| 2 | Opbouw | 20% | 8,5 | 9 |
| 3 | Taal | 15% | 8,5 | 9 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 |
| 5 | Code en figuren | 10% | 8,5 | 8,5 |
| 6 | Replicatie | 10% | 8,5 | 8,5 |
| 7 | Oefeningen | 5% | 9 | 9 |

9·0,30 + 9·0,20 + 9·0,15 + 9·0,10 + 8,5·0,10 + 8,5·0,10 + 9·0,05 = 8,90 → **8,9**.
Laagste deelcijfer 8,5.

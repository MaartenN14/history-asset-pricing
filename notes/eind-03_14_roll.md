STATUS 03_14_roll F6c words=5419 prose=PASS open=0 cijfer=8,9 min=8,5

# Eindbeoordeling (F6): Roll, de critique en de R² (03_14_roll)

Cijfer van record, zelfde kalibratie als L13 en L15 (en het L12-anker van de
tweede beoordelaar). Bij twijfel het lagere cijfer.

## De drie verbeteringen met het meeste effect

1. **Opbouw** (8 → 8,5). Het $R^2$-deel in de eerste zin aan de vraag van de lecture
   koppelen (wat meet een toets als het meeste van de variantie niet systematisch
   is?), en de sinaasappelsap- en bid-ask-alinea's volgens de schraptoets schrappen
   of in een dropdown zetten. Bij de bijna-efficiënte proxy's het "Waarom" laten
   zeggen dat de helling eerst stijgt, of "Dat had de intuïtie voorspeld"
   aanpassen.
2. **Code** (8 → 9). In `tilt_to_corr` in één zin zeggen dat $c$ een wortel is van een
   kwadratische vergelijking, en de wortel kiezen zonder comprehension; de tabellen
   van de $R^2$-replicatie zonder geneste dict-comprehensions bouwen; in
   `adjusted_r2` de drievoudige ontkenning weg; de simulatiecel (30 regels)
   splitsen; kolomnamen voluit.
3. **Replicatie** (8,5 → 9). De getallen uit de alinea's na de tautologietabel en na
   de $R^2$-tabellen naar de tabellen verwijzen in plaats van ze te herhalen.

Samen: 2,55 + 1,70 + 1,35 + 0,90 + 0,90 + 0,90 + 0,45 = 8,75, dus 8,8.

## Eindcijfer: 8,5

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 9 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,55 + 1,60 + 1,35 + 0,90 + 0,80 + 0,85 + 0,45 = 8,50, dus 8,5.
Lengte: 5.404 woorden volgens `prose_stats` (PASS). Replicatieblok: 196 woorden.

## Feitelijke fouten

Nagerekend met de hand en tegen de celuitvoer (`tools/nb_outputs.py`). Correct: het
toy ($\boldsymbol{\Sigma}^{-1}$ met blokinverse; $A = 128{,}125$, $B = 7{,}0625$,
$C = 0{,}51125$, $D = 15{,}625$; $\lambda = 0{,}368$, $\delta = -0{,}01248$;
covarianties 0,02432, 0,03904, 0,00224; bèta's 1; 1,6053; 0,0921; $\mu_z = 3{,}39\%$,
helling 6,61%, 14,00% en 4,00%; gelijkgewogen 9,33%, bèta's 1; 1,8333; 0,1667,
helling $8{,}33/1{,}389 = 6{,}0\%$, intercept 3,33%, residuen, $R^2 = 1 - 0{,}67/50{,}67 = 0{,}9868$);
het bewijs van de stelling ($\sigma_p^2/\lambda_p = \mu_p - \mu_z$), van het lemma en
van propositie en gevolg ($\mathbf{1}'\mathbf{u} = 1$); de wereld van honderd activa
(0,66%, 4,69%, Sharpe 0,49, $\rho^* = 0{,}62$; hoogste helling 1,7 keer bij 0,75);
de simulatie (0,08% en $-0{,}34\%$, $12 \times 0{,}338 = 4{,}1\%$; band 0,22 tot 1,0;
$4{,}69/\sqrt{600} = 0{,}19$; sd 0,14 tot 0,20; mediaan 0,05 naar $-0{,}11$ en 0,14);
de replicatie (757 maanden; 2,34%; som van absolute gewichten 13,8; 0,89 en
$1{,}23/1{,}39 = 0{,}885$; $-0{,}37$, 1,16, 0,08; 0,60 met SE 0,16; 0,54, 0,62, 0,73;
25, 35, 40, 33 en 41%; SE rond 0,02; 0,349 en 0,411); oefening 1 (tangent
$(1/3, 2/9, 4/9)$ uit $\boldsymbol{\Sigma}^{-1}\boldsymbol{\mu}^e = (1{,}5;\ 1;\ 2)$;
$\mathbf{d}$ en $\boldsymbol{\Sigma}\mathbf{d}$; $c^* = 4{,}718$, $\rho^* = 0{,}785$,
$\mathbf{w}^*$), oefening 2 (0,15 in 2017 tot 0,56 in 2020; 24 tot 40%; 0,82),
oefening 3 (0,37; 0,74; 0,98; 2,55; 0,11; 0,88 tegen 0,62). Cross-refs naar
[](#01-04-markowitz) (A, B, C, $\lambda$, $\delta$, zelfde drie activa) en
[](#02-08-capm) kloppen. De getallen van Roll (1988) zijn niet tegen de bron
gecontroleerd.

Geen fouten gevonden. Twijfelachtig, niet geteld:
- Numerieke uitwerking, na de figuur: "Dat had de intuïtie voorspeld." Het "Waarom"
  van de bijna-efficiënte proxy's zei "de bèta's van de activa met een hoge premie
  dalen ... en de helling daalt". Het pad laat eerst een stijging tot 1,7 keer de
  premie zien. Wat de intuïtie voorspelde (de helling kan nul worden bij hoge
  correlatie), klopt; de richting onderweg niet.

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- **Toy-voorbeeld**: de geleende scalars $A$, $B$, $C$, $D$ en de randvorm van de
  gewichten worden in één regel herhaald met vergelijkingslabel, en elke stap heeft
  een getal. De slotzin geeft de les ("de $R^2$ van een cross-sectionele regressie
  zegt niet hoe ver de proxy van de rand ligt").
- **Opzet**: "Het subscript $m$ staat in deze lecture voor de marktportefeuille, niet
  voor de stochastic discount factor" voorkomt een botsing met de vorige lecture.
- **Bijna-efficiënte proxy's**: het lemma krijgt direct een getal ("correlatie 0,9
  ... 90% van haar Sharpe-ratio"), en $\rho^*$ krijgt het toy-getal 0,785 en het
  wereldgetal 0,62.

*Aanmerkingen*
- Numerieke uitwerking: "Dat had de intuïtie voorspeld." Zie twijfelachtig; de lezer
  krijgt een niet-monotoon pad na een intuïtie die een dalende helling beschreef.
- Simulatie: de proxy's hebben correlatie 1 tot 0,90. Daar is de ware helling juist
  *hoger* dan de premie (0,79 tegen 0,66 bij 0,90). De nulhelling bij 0,62, het punt
  van de propositie, komt in de simulatie niet voor; de tekst verschuift de vraag
  naar het intercept zonder dat te zeggen.
- Bijna-efficiënte proxy's: "Alleen een GLS-regressie ... blijft aan de positie van
  de proxy gebonden." Eén zin zonder uitleg of vervolg.
- De tweede vraag: "uit die correlatie schatte hij de spread". Geen formule en geen
  getal.

*Beter uitleggen*
- Waarom de simulatie $\rho \ge 0{,}90$ kiest en wat daar met de helling gebeurt:
  één zin bij de keuze van `rhos`.

*Voor een 9*
- De intuïtie of de conclusie na de padfiguur laten kloppen met het niet-monotone
  pad (Bijna-efficiënte proxy's; Numerieke uitwerking).
- In de simulatie $\rho^* = 0{,}62$ toevoegen of uitleggen waarom het ontbreekt
  (Simulatie, eerste alinea).
- De GLS-zin en de bid-ask-zin óf uitwerken met één getal óf schrappen.

### 2. Opbouw en rode draad (8)

*Goed*
- Overzicht met vraag en antwoord ("Alleen of de gebruikte index
  mean-variance-efficiënt is, en niet het model"), een lijst van vier punten en de
  geschiedenis.
- Toy, stelling, simulatie en replicatie voor de critique gebruiken dezelfde
  bouwstenen: de drie activa van [](#01-04-markowitz), `sml_fit` in elke laag, de
  $R^2$ van 0,9868 die aan het eind van de simulatie terugkomt.
- De drie verwachtingen van de intuïtie komen elk terug ("Dat is de eerste
  voorspelling van de intuïtie"; de nulhelling; "Zoals de intuïtie verwachtte, is
  het meeste dus niet systematisch").

*Aanmerkingen*
- Intuïtie: "Los van die kritiek stelde Roll later een tweede vraag, over
  varianties." De lecture heeft twee onderwerpen. Toy en simulatie gaan alleen over
  het eerste; het $R^2$-deel heeft geen toy en geen simulatie.
- De tweede vraag: de sinaasappelsap-alinea ("Die lezing ontlenen we aan ... want de
  primaire tekst hebben we niet kunnen inzien") en de bid-ask-alinea zijn
  nevenresultaten die de schraptoets niet halen.
- Het pad in de numerieke uitwerking weerspreekt het "Waarom" ervoor (zie
  criterium 1).

*Beter uitleggen*
- Geen.

*Voor een 9*
- Zie verbetering 1 (Intuïtie, vierde alinea; De tweede vraag).

### 3. Taal (9)

*Goed*
- Korte zinnen (gemiddeld 14,6 woorden, p90 23), vijf puntkomma's, geen
  gedachtestreepjes, geen u/je, geen stopwoorden of calques volgens `prose_stats`.
- Vaktermen krijgen een uitleg bij eerste gebruik (*marktportefeuille*, *proxy*,
  *joint hypothesis*, *minimum-variantierand*, *niet-synchrone handel*).
- Theorie of feit zegt wat het hier betekent ("het CAPM was een theorie met toetsen
  en werd een theorie waarvan de centrale grootheid niet te meten is").

*Aanmerkingen*
- Opzet: "niet voor de stochastic discount factor"; elders in de reeks
  "discontofactor" of SDF.
- De tweede vraag: "Die lezing ontlenen we aan ..., want de primaire tekst hebben we
  niet kunnen inzien." Een werknotitie in de lopende tekst.
- Presentatielabels in het Engels: "in-sample tangent", "max |resid|".

*Beter uitleggen*
- Geen.

### 4. Toy-voorbeeld (9)

*Goed*
- Opzet-tabel, recept dat de theorie als eerste afleidt, vijf genummerde stappen,
  één cel, tabel "met de hand"/"code" en één les.
- Eén mechanisme met twee portefeuilles, handrekenbaar (noemers tot 15,625), en de
  $R^2$ van 0,9868 is een scherp exemplaar van wat de lecture beweert.

*Aanmerkingen*
- Stap 1 neemt de formules voor $\lambda$ en $\delta$ over uit
  [](#01-04-markowitz) zonder label; de randvorm krijgt er wel een.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8)

*Goed*
- `sml_fit` en `make_world` lezen als de wiskunde, met benoemde tussenresultaten, en
  `sml_fit` wordt in toy, wereld, simulatie en replicatie hergebruikt.
- Elke figuur heeft een leeswijzer ("Let op de rode lijn tussen correlatie 1 en de
  plek waar ze de nullijn kruist"; "Let in de figuur op de spreiding rond de lijn in
  het rechterpaneel") en een bijschrift.

*Aanmerkingen*
- `tilt_to_corr`: "`roots = np.roots([a**2 - rho**2 * s * b, ...])`" en
  "`valid = [r.real for r in roots if abs(r.imag) < 1e-12 and ...]`". Een
  kwadratische vergelijking die de tekst niet noemt, en een comprehension die de
  wortel kiest.
- Simulatiecel: `tilt_to_corr` en de dubbele lus samen ongeveer dertig regels.
- $R^2$-replicatie: "`portfolio_r2 = {name: pd.Series({col: adjusted_r2(...) for col
  in panel.columns}) for name, panel in portfolio_sets.items()}`" en
  "`pd.DataFrame({name: {...} for name, r2 in portfolio_r2.items()})`". Geneste
  comprehensions om tabellen te bouwen (STYLE §11.8).
- `adjusted_r2`: "`1 - (1 - (1 - resid.var() / y.var())) * (n - 1) / (n - k)`", een
  drievoudige ontkenning in plaats van een benoemde $R^2$.
- Kolomnamen afgekort: "pop. helling", "helling q05", "sd intercept",
  "gem. excess (% p.m.)", "SE gem. (% p.m.)".

*Beter uitleggen*
- Geen.

*Voor een 9*
- Zie verbetering 2 (Simulatie; De $R^2$ van portefeuilles en aandelen).

### 6. Replicatie en empirie (8,5)

*Goed*
- Replicatieblok van 196 woorden met vijf onderdelen, een verwachte afwijking die de
  onzekere rangorde van dag en maand vooraf noemt, en een eindtabel
  origineel/hier.
- Het oordeel "Geslaagd voor de tautologie, gedeeltelijk geslaagd voor de $R^2$"
  verwijst naar de verwachte afwijking en verklaart de omgekeerde rangorde.
- De proxy met helling nul op echte data (correlatie 0,89, helling nul) maakt de
  propositie tastbaar.

*Aanmerkingen*
- Na de tautologietabel: "De CRSP-index geeft een helling van −0,37% en een
  intercept van 1,16% per maand, met $R^2 = 0{,}08$ ... 0,60% per maand, heeft een
  standaardfout van 0,16%." Vijf getallen uit de tabel in één alinea.
- Na de aandelentabel: "gemiddeld 25% ... 35% ... 40%. Dagelijks is het 33% ...
  41% ... rond 0,02". Zes getallen in één alinea.

*Beter uitleggen*
- Geen.

*Voor een 9*
- Zie verbetering 3 (De tautologie; De $R^2$ van portefeuilles en aandelen).

### 7. Oefeningen (9)

*Goed*
- Oefening 1 zet het toy om naar een wereld met risicovrije rente en rekent
  $\rho^* = 0{,}785$ uit; oefening 2 is een afleiding met een empirisch vervolg;
  oefening 3 breidt de replicatie uit buiten de steekproef. Elke uitwerking eindigt
  met "Wat dit leert:".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

## Navertelling in vijf zinnen

Een lijn tussen verwacht rendement en bèta bestaat dan en slechts dan als de
portefeuille waartegen de bèta's zijn gemeten op de minimum-variantierand ligt, en
dat geldt ook in elke steekproef. Een toets van het CAPM toetst dus alleen of de
gebruikte index efficiënt is, en de ware markt is niet waarneembaar. Een proxy die
sterk met de markt correleert, kan toch een helling van nul geven als hij in de
ongunstige richting afwijkt, en met vijftig jaar data ziet een onderzoeker dat
niet. Op de 25 size/BM-portefeuilles geeft de achteraf efficiënte portefeuille
$R^2 = 1$ en de CRSP-index 0,08. Los daarvan verklaren markt en industrie maar ongeveer
35 tot 40% van de maandelijkse variantie van grote aandelen.

Dit komt overeen met het Overzicht, dat het $R^2$-deel als vierde punt noemt.

## Controle 1

Gecontroleerd tegen `notes/rapport-03_14_roll.md` §F6-1, de lecture en de nieuwe
celuitvoer. Vergeleken met de uitvoer van F6 zijn alle waarden gelijk; alleen
kolom-, index- en celnummers verschillen. `prose_stats --check`: 5.419 woorden, PASS.

| punt | status | vindplaats |
|---|---|---|
| Verbetering 1: $R^2$-deel aan de vraag koppelen | opgelost | "Als de lijn niet te toetsen is, wat verklaren markt en industrie dan wel?" (Intuïtie en Theorie) |
| Verbetering 1: sinaasappelsap en bid-ask | opgelost | twee zinnen, werknotitie en secundaire bron weg; spread $2\sqrt{-\Cov(\Delta p_t, \Delta p_{t-1})}$ nagerekend als Rolls schatter |
| Verbetering 1 / twijfelpunt: intuïtie tegen pad | opgelost | "kan de helling eerst zelfs stijgen"; "De intuïtie voorspelde de eerste stijging en de nulhelling bij hoge correlatie" |
| Verbetering 2: `tilt_to_corr` | opgelost | zin over de kwadratische vergelijking; wortel via benoemde maskers; eigen cel |
| Verbetering 2: geneste comprehensions | opgelost | portefeuilletabel met gewone lussen |
| Verbetering 2: `adjusted_r2` | opgelost | benoemde `r2` |
| Verbetering 2: cel van dertig regels, kolomnamen | opgelost | simulatielus in een eigen cel; "populatie: helling", "helling: 5%-kwantiel", "% per maand" |
| Verbetering 3: getallen in proza | opgelost | de alinea's verwijzen naar rijen en kolommen; alleen het oordeel noemt de vergeleken waarden |
| Helderheid: waarom $\rho \ge 0{,}90$ | opgelost | "de nulhelling bij 0,62 valt buiten dit bereik, en de schade zit hier in het intercept" |
| Helderheid: GLS-zin | opgelost | geschrapt |
| Taal: "stochastic discount factor", werknotitie, Engelse labels | opgelost | "SDF"; notitie weg; "in-sample tangentportefeuille" |
| Toy: formules $\lambda$, $\delta$ zonder label | opgelost | zin dat [](#01-04-markowitz) ze afleidt uit [](#eq-markowitz-foc) en de restricties |
| Opbouw: geen toy of simulatie voor het $R^2$-deel | niet (afgewezen) | STYLE §11.7 (één mechanisme, één simulatievraag); oefening 2 draagt dat deel; reden aanvaard |

De nieuwe naadzin in "Waar we zijn" ("Het bezwaar dat de markt niet waarneembaar
is, dat in de APT-discussie terugkwam, begint hier") klopt: de toetsbaarheidsdiscussie
over de APT volgde na 1977.

Geen verslechteringen van betekenis en geen nieuwe feitelijke fouten. Kanttekening,
geen aftrek: twee nieuwe puntkomma's in lopende tekst (Toy, stap 1: "van het
minimum-variantieprobleem; [](#01-04-markowitz) leidt ..."; Simulatie: "boven de
premie; de nulhelling").

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8,5 | 9 |
| 2 | Opbouw | 8 | 8,5 |
| 3 | Taal | 9 | 9 |
| 4 | Toy | 9 | 9 |
| 5 | Code en figuren | 8 | 9 |
| 6 | Replicatie | 8,5 | 9 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,70 + 1,70 + 1,35 + 0,90 + 0,90 + 0,90 + 0,45 = 8,90. **Eindcijfer 8,9,
laagste deelcijfer 8,5.** Opbouw blijft 8,5: de lecture behandelt twee vragen, en
toy en simulatie dragen alleen de eerste.

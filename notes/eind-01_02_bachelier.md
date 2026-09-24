STATUS 01_02_bachelier F6c words=5460 prose=PASS open=0 cijfer=8,6 min=8,5

# Eindbeoordeling (F6): Regnault, Bachelier en de random walk

## Eindcijfer: 8,3

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,40 + 1,60 + 1,275 + 0,90 + 0,85 + 0,80 + 0,45 = 8,28, dus 8,3.
Lengte: 5.455 woorden, net onder de 5.500.

## Feitelijke fouten

Geen gevonden. Nagerekend: $\E|S_n|$ en de verhoudingen 1; 0,707; 0,866; 0,750;
$\sqrt{8/\pi} = 1{,}596$ (6% boven 1,50); raakkans 0,375 en $2(1-\Phi(0{,}5)) = 62\%$;
$20/\sqrt{2\pi} = 7{,}98$; de optietabel (hooguit 0,027 bij een maand, 0,336 bij een
jaar); de Lo-MacKinlay-standaardfouten 0,029; 0,054; 0,085; 0,126 bij $T = 1216$;
$T^*$ = 96, 1537, 9604 weken (1,8; 30; 185 jaar); 155 jaar Shiller; de
simulatieafwijking bij vijf jaar (hooguit 2,8 pp); $2{,}73\sqrt3 = 4{,}73$ en
$2{,}73\sqrt{12} = 9{,}46$; hellingen 0,511 en 0,577; 0,885 (ruim tien procent te
laag); MAD/SD 0,70 naar 0,73; $0{,}085^2 = 0{,}7\%$; VR-schattingen binnen 0,02 van
Lo-MacKinlay; kwintiel-rangorde; $(1{,}96/0{,}205)^2 = 91$ en
$(1{,}96/0{,}030)^2 = 4268$; oefeningen (3,84; 24 stappen; $1{,}1/0{,}9$; 4,51 en 3,29;
$\sqrt{1/280 + 1/487} = 0{,}075$; hoogste $t$ 1,28). Niet na te gaan met de
beschikbare bronnen: Kendalls gemiddelde van "ongeveer 0,13" en Regnaults 4,74 en
9,50.

## Per criterium

### 1. Helderheid van de uitleg (8)

*Goed*
- Toy-voorbeeld: $\E|\cdot|$ krijgt een vaste naam ("gemiddelde absolute
  afwijking") en "spreiding" een vaste betekenis.
- "Bacheliers optieprijs": $v$ krijgt een eenheid en een orde van grootte ("bij
  een aandeel van 100 met 20% volatiliteit ongeveer 20 euro"), en de formule een
  uitgerekend getal (7,98).
- "Wat het voorspelt: de kans om een niveau te raken": de verkooporder van 10 euro
  maakt de spiegeling concreet (31% tegen 62%).

*Aanmerkingen*
- "Opzet en aannames": "$T$ het aantal waarnemingen". In [](#00-01-rendementen) is
  $T$ het aantal jaren en $N$ het aantal waarnemingen; de wissel wordt niet
  genoemd.
- "Bacheliers optieprijs": "Dat is hier een gevolg van de aangenomen
  martingaalconditie. Waarom die aanname mag, lieten pas Black en Scholes zien."
  Een resultaat waarop de lezer moet vertrouwen zonder dat het in één regel wordt
  gegeven.
- "Wat het voorspelt: de kans om een niveau te raken": $\kappa$ is hier het eerste
  raaktijdstip; in de vorige lecture was $\kappa$ de kurtosis.
- Replicatie: "Regnault neemt die lage maandverhouding mee naar de jaarhorizon,
  waar ze hoger ligt." Het argument over MAD/SD bij dikke staarten is in drie
  zinnen samengeperst en vraagt herlezen.

*Beter uitleggen*
- Waarom de martingaalconditie hier de prijs vastlegt: één zin dat Bachelier
  termijnprijzen gebruikte en dat risiconeutraal prijzen pas later een argument
  kreeg, zonder de latere lecture nodig te hebben.
- De MAD/SD-uitleg: één getal (0,70 bij een maand tegen 0,80 bij normaal) vóór de
  conclusie zetten.

### 2. Opbouw en rode draad (8)

*Goed*
- Overzicht met vraag en antwoord, Intuïtie met drie voorspellingen die de theorie
  inlost (0,4; $\sqrt t$; autocorrelatie nul).
- Toy-getallen keren terug: $\E|S_4| = 1{,}50$ tegen 1,60, raakkans 0,375, $VR$
  lineair.
- De simulatie meet op de steekproefgrootte van Lo en MacKinlay, die de replicatie
  daarna gebruikt.

*Aanmerkingen*
- Stofdichtheid: Donsker, reflectieprincipe, Bachelier-optie, variance ratio,
  een power-simulatie en twee replicatieblokken, op 5.455 woorden. De raakkans
  wordt verder niet gebruikt en de optieformule niet getoetst.
- "Hoe het getoetst wordt": de variance ratio, de toets waar alles naartoe werkt,
  komt pas als vierde resultaat.

*Beter uitleggen*
- Eén zin in de routekaart die zegt welke twee resultaten de replicatie toetst en
  welke twee alleen gevolgen zijn.

### 3. Taal (8,5)

*Goed*
- Natuurlijk Nederlands, "onderscheidend vermogen" in plaats van *power*.
- Franse citaten staan als blokcitaat met inleiding.

*Aanmerkingen*
- Overzicht: "Zonder Bachelier was Regnaults regel een meting gebleven. Hij gaf als
  enige een model waaruit ze volgt." Het tweede "Hij" verwijst terug over een zin.

*Beter uitleggen*
- Geen.

### 4. Toy-voorbeeld (9)

*Goed*
- Zestien paden, vier handstappen, tabel hand/code, "We weten nu".
- De enige niet afgeleide formule ($\sqrt{2/\pi}$) is als recept aangekondigd.

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

### 5. Code en figuren (8,5)

*Goed*
- `ar1_paths` houdt de AR-lus zichtbaar; `deviation_scaling` leest als de definitie.
- Elke figuur heeft een "Let op" en een bijschrift.

*Aanmerkingen*
- Replicatie: de vergelijkingscel met `original`, `original_z`, `here`, `here_z`
  als losse lijsten is lang en kwetsbaar voor een verschoven rij.

*Beter uitleggen*
- Geen.

### 6. Replicatie en empirie (8)

*Goed*
- Twee volledige blokken met falsifieerbare eisen (factor twee; rangorde).
- Tabellen origineel/hier, oordelen met "Geslaagd ... gedeeltelijk geslaagd".

*Aanmerkingen*
- Regnault: "gedeeltelijk geslaagd op Regnaults eigen toets" beoordeelt iets (de
  overeenstemming van een half procent) waarover het blok geen verwachte
  afwijking gaf.
- Lo-MacKinlay: het blok verwachtte "$z$-waarden rond de twee"; gevonden 1,2 tot
  2,0. Het oordeel "Geslaagd voor de marktindex" gaat daar niet op in.
- De Kendall-vergelijking en de post-1985-bevinding staan in lopende tekst.

*Beter uitleggen*
- Geen.

### 7. Oefeningen (9)

*Goed*
- Scheve munt als instap, AR(1)-afleiding, uitbreiding van de replicatie na 1985;
  elke uitwerking eindigt met "Wat dit leert".

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Geen.

## De drie verbeteringen met het meeste effect

1. De raakkans of de Donsker-schets inkorten en de ruimte gebruiken om de
   variance ratio eerder als doel te noemen (opbouw 8 → 8,5).
2. De wissels van $T$ en $\kappa$ ten opzichte van de vorige lecture in één zin
   noemen, en de MAD/SD-uitleg met een getal openen (helderheid 8 → 8,5).
3. De verwachte afwijking van het Regnault-blok uitbreiden met zijn eigen
   verhouding, en de $z$-waarden in het Lo-MacKinlay-oordeel noemen (replicatie
   8 → 8,5).

## Navertelling in vijf zinnen

Regnault mat in 1863 dat de gemiddelde koersafwijking met de wortel van de tijd
groeit, en Bachelier gaf er in 1900 een model voor: de random walk die in de
limiet een Brownse beweging wordt. Uit dat model volgen de factor $\sqrt{2/\pi}$,
de raakkans als twee keer de eindkans, en een optieprijs van ongeveer
$0{,}4\,v\sqrt\tau$. De toets is de variance ratio, maar een kleine
autocorrelatie vraagt tientallen jaren data voordat ze zichtbaar is. Op
Amerikaanse data klopt de $\sqrt t$-wet (helling 0,51), en de variance ratios van
Lo en MacKinlay zijn na te bouwen, hoger bij kleine aandelen. Na 1985 is die
afwijking verdwenen, en of het een prijsfout of een handelseffect was, is met
gratis data niet te beslissen.

Dit komt overeen met het Overzicht.

## Controle

Gecontroleerd tegen `notes/rapport-01_02_bachelier.md` §F6-1 en de lecture.

| punt | status | vindplaats |
|---|---|---|
| Verbetering 1: opbouw (raakkans inkorten, variance ratio als doel) | opgelost | reflectiebewijs vervangen door een bewijsidee van drie zinnen; routekaart: "de variance ratio, de toets waar simulatie en replicatie om draaien. De replicatie toetst twee resultaten ... De raakkans en de optieprijs toetsen we niet op data." |
| Verbetering 2: wissels $T$ en $\kappa$; MAD/SD met getal | opgelost | Opzet: "In [](#00-01-rendementen) heette dat laatste $N$ en was $T$ het aantal jaren"; $\kappa$ weg; "0,70 bij één maand en 0,73 bij twaalf maanden, tegen 0,80" |
| Verbetering 3: Regnault-verwachting en $z$-waarden | opgelost | blok: "Regnaults eigen verhouding ... van bijna één verwachten we niet"; oordeel: "gedeeltelijk geslaagd voor de $z$-waarden" |
| Martingaalconditie in één regel | opgelost | "een optie die met aandeel en kas na te maken is, kost wat die portefeuille kost" |
| "Hij" in het Overzicht | opgelost | "Bachelier gaf als enige een model" |
| Vergelijkingscel met losse lijsten | opgelost | helper `compare()` per benoemde rij; uitvoer nagekeken en gelijk |
| Kendall en post-1985 in lopende tekst | niet, met reden afgewezen | aanvaard: de tekst noemt alleen de getallen die het oordeel dragen |
| Naadpunt 6 ($T$) | opgelost | zie verbetering 2 |
| Naadpunt 7 ($\kappa$) | opgelost | $\kappa$ komt niet meer voor |
| Naadpunten 1 en 2 | niet van toepassing, zin toegevoegd | "In de notatie van [](#00-00-setup) is $r$ het simpele rendement. In deze lecture is het dus een logrendement." |

Geen verslechteringen en geen nieuwe feitelijke fouten. De vergelijkingstabel is na
de herschrijving gelijk aan de vorige uitvoer.

| nr | criterium | was | nu |
|---|---|---|---|
| 1 | Helderheid | 8 | 8,5 |
| 2 | Opbouw | 8 | 8,5 |
| 3 | Taal | 8,5 | 8,5 |
| 4 | Toy | 9 | 9 |
| 5 | Code en figuren | 8,5 | 9 |
| 6 | Replicatie | 8 | 8,5 |
| 7 | Oefeningen | 9 | 9 |

Gewogen: 2,55 + 1,70 + 1,275 + 0,90 + 0,90 + 0,85 + 0,45 = 8,63. **Eindcijfer 8,6,
laagste deelcijfer 8,5.** Opbouw blijft onder 9 door de stofdichtheid (vier
resultaten en twee replicatieblokken op 5.460 woorden).

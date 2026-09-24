STATUS 01_03_williams_ddm F6b words=5470 prose=PASS open=0 cijfer=- min=-

# Rapport 01_03_williams_ddm

## F0

`prose_stats`: words=6838, sent_mean 14,6, sent_p90 23, sent_gt40 0, para_mean 45,
dash 0, semicol 14, stopw 0, calque 0, engquote 3. `--check`: FAIL words=6838 (max 5500).
`--where`: geen treffers.

Woorden per sectie: kop 116, Overzicht 323, Intuïtie 495, Toy 340, Theorie-inleiding 69,
Opzet 235, Van definitie naar contante waarde 344, Kernresultaat 482, Gordon 571,
PVGO 370, Hoe getoetst 580, Simulatie 786, Replicatie 935, Wat er brak 444,
Oefeningen 768.

**Vijf grootste problemen**
1. Lengte 6.838 (§11.11): Replicatie (935) en Simulatie (786) dragen herhalingen en
   zijpaden; Intuïtie (495) heeft een anekdote-note en een CAPM-uitweiding.
2. Feitelijke fouten (feitenlijst): Kendall in "Waar we zijn" spreekt L2 tegen;
   "factor drie" in Simulatie; tip "ruim 3% naar rond 1,5%" in Hoe het getoetst wordt;
   85,6 in december 1999 is niet het maximum; 03-15 en 03-16 worden beweringen
   toegedicht die daar niet staan (Wat er brak).
3. Onherleidbare getallen (§11.11 Feiten): 0,91 (warning Replicatie) en 26 (note
   Campbell-Shiller) komen uit geen cel.
4. Het "model van Williams" heeft één aanname (Theorie-inleiding, Opzet r. 297, Wat
   er brak) en elders twee (Overzicht, Opzet r. 255, Samengevat): H7.
5. Taal en presentatie (§11.3, §11.4, §11.8): calques "meer dan het krediet krijgt",
   "doet het meeste werk", "het werk doen", "neem verwachtingen", "vergeeflijk",
   "earnings yield"; "heet in deze reeks de standaardfout van 2%" als label; PVGO-cel
   met zeven `print`-regels; vergelijkingstabel Replicatie met de hand overgetypt.

**Controle eis 2 (grep in `lectures/`).** Van buiten aangehaald: paginalabel,
`eq-williams-ddm-ddm` (03_12), `eq-williams-ddm-pd` (04_20). Inhoudelijk aangehaald:
de iteratie naar de contante waarde (03_15), de PD-regressies (03_12, 03_15, 04_20),
het Gordon-model (03_16), de CAPE-regressie (05_33 §3, 08_39) en bubbels (08_39,
tabelrij "Bubbels"). Geen ander label van deze lecture wordt elders aangehaald.

**Schraplijst (schraptoets §11.11)**

| kopje | passage | ~woorden | eis niet gehaald |
|---|---|---|---|
| Intuïtie | note "Williams verkocht nauwelijks exemplaren" (feit 13, onbronneerbaar) | 70 | 1, 2, 3 |
| Intuïtie | CAPM-uitweiding "prijs van risico" inkorten tot één zin | 60 | 1 |
| Intuïtie | alinea "waar zonder iets te zeggen" inkorten | 30 | 1 (herhaalt Theorie) |
| Toy | zwaartepunt 22 jaar (tweede resultaat in toy) | 55 | 1 |
| Gordon | duration-afleiding en toepassing | 110 | 1 |
| Gordon | note dividend per aandeel en inkoop (staat ook in het replicatieblok) | 65 | 1 |
| Gordon | alinea "tweede vorm is in de praktijk de nuttigste" inkorten | 30 | 1 |
| Kernresultaat | warning transversaliteit is een aanname (vooruitverwijzingen) | 50 | 1 |
| Kernresultaat | 1999-internetalinea inkorten tot één zin | 30 | 1 |
| Hoe getoetst | note Campbell-Shiller (26 onherleidbaar; afleiding staat in 04-20) | 90 | 1, 2 |
| Hoe getoetst | tip dividendrendement sinds 1990 (feit 3 fout) | 70 | 1 |
| Hoe getoetst | dubbele uitleg identiteit/lineariseren | 60 | 1 |
| Simulatie | "Wat deze figuur over het vak zegt" | 40 | 1 |
| Simulatie | log/rekenkundige correctie tot twee zinnen | 50 | 1 |
| Simulatie | dubbele inleiding (twee alinea's over wat de simulatie isoleert) | 60 | 1 |
| Replicatie | alinea na het blok die het blok herhaalt + $R^2$-alinea | 110 | 1 |
| Replicatie | CAPE-tekst inkorten (cel blijft: eis 2, 05_33) | 90 | — (inkorten) |
| Replicatie | handgetypte vergelijkingstabel wordt celuitvoer | 0 | — |
| Wat er brak | scheefheid-als-verweer (feit 8), PVGO in 03-16 (feit 15), inkorten per element | 130 | 1 |
| Overzicht | lijst en geschiedenis inkorten | 80 | 1 |
| Oefeningen | ex-2 (2)/(3) vervangen door één richtingvraag; uitwerkingen korter | 150 | 1 |
| overal | taal, dubbele lees-zinnen, herhaling | 250 | — |

Som ≈ 1.770 woorden. Verwachte lengte na F1 ≈ 6.840 − 1.770 + ≈ 80 (toegevoegde
lees-zinnen en cel-zinnen) ≈ 5.150. Onder 6.000 zonder de kern te raken; geen split.

## F1

**Eindmeting.** words=5243, sent_mean 14,6, sent_p90 24, sent_gt40 1 (de Overzicht-lijst,
telartefact), para_mean 44, dash 0, semicol 7, calque 0, stopw 0, engquote 1: PASS.
`--where` leeg. Sync en `HAP_OFFLINE=1 --execute` foutloos, geen warnings in de uitvoer.

**Geschrapt** (reden: schraptoets eis 1, niet nodig voor de vraag, tenzij anders vermeld):
note "Williams verkocht nauwelijks" (onbronneerbaar, feit 13); CAPM-uitweiding (één zin
over); zwaartepunt 22 jaar in toy en de duration-afleiding in Gordon (tweede resultaat,
niet nodig); note dividend per aandeel en inkoop (staat in het replicatieblok);
warning transversaliteit is een aanname (vooruitverwijzingen); note Campbell-Shiller
(26 onherleidbaar, afleiding staat in 04-20; één zin blijft); tip dividendrendement
sinds 1990 (feit 3 fout); "Wat deze figuur over het vak zegt" (één zin over); dubbele
inleiding Simulatie; alinea's na het replicatieblok die het blok herhaalden en de
$R^2$-alinea; "Dat is geen programmeerfout"-alinea (ingekort); ex-2 deelvragen over het
optimale $b$ (rasterartefact, vervangen door één richtingvraag); scheefheid als verweer
in 03-15 en PVGO in 03-16 (feit 8 en 15, onjuist). CAPE ingekort, cel blijft (eis 2: 05_33, 08_39).

**nb_outputs-diff**, elk verschil bedoeld: cel 4 (PVGO) is nu een tabel hand/code in plaats
van zeven prints, zelfde getallen 0,05 / 2 / 40 / 30 / 10 / −2,73; cel 8 print twee nieuwe
regels (PD-uitersten 9,9 in 1917 en 86,2 in 2025; autocorrelatie 0,885); cel 9 bouwt de
resultatentabel zonder indexnaam, getallen gelijk; nieuwe cel 10 zet de vergelijkingstabel
Williams/verwacht/hier uit de regressie (was handgetypt markdown); cellen daarna een
nummer opgeschoven; ex-2-cel (nu 15) toont prijs bij $b = 0{,}6$ in plaats van optimale $b$
(0,94 / 0,745 / 2125 vervallen, ook uit de tekst). Figuren byte-gelijk. Geen aangehaald getal veranderd.

**Feitenlijst** (15 punten): verwerkt 1 (86,2 in 2025, uit cel), 2 ("tot een factor twee
naar boven", 40,8/19,5 = 2,1), 3 (tip geschrapt), 4 (Kendall zoals L2: samenhang te zwak
om mee te voorspellen), 5 (0,89 uit cel, panelsteekproef), 6 (note geschrapt), 7 (overal
12,5 en 40,8), 8 en 15 (bewering geschrapt), 9 (verwijzing naar 00-00-setup), 10 (orde
van grootte nu "ongeveer 8%", met 8,4% uit de simulatie), 11 ("zwakke, niet-significante
stijgende lijn"), 12 (model = identiteit + constante $r$; transversaliteit voor beide
opgelegd, overal zo), 13 (note weg; Overzicht zegt nu "brachten in de praktijk"),
14 ("schreef vrijwel niets" vervangen door "nam hem in zijn waarderingen als gegeven").
Afgewezen: geen.

**Afvinklijst §11.9, wat niet voldoet.** Geen. Overige: ok. Vooruitverwijzingen buiten
"Wat er brak": twee (03-15 bij de bel, 04-20 bij Campbell-Shiller).

**Labels.** Geen verdwenen of verhuisd; `eq-williams-ddm-ddm` en `eq-williams-ddm-pd`
ongewijzigd.

**Open punten.** (1) Niet te verifiëren met projectbronnen: Williams' boomgaardbeeld en
"honderden bladzijden, tabellen met de hand" (stonden er al; F2 kan Williams 1938 nalezen).
Rubriekronde: rating2-punten verwerkt (calques, label "standaardfout van 2%", simulatie
gekoppeld aan het hoofdargument, CAPE-oordeel, bel-uitwerking noemt jaar 30 en de ratio's).

## F4

**Meting.** words=5364 (was 5243), semicol 7, sent_gt40 1 (lijst, telartefact): PASS.
Sync en `HAP_OFFLINE=1 --execute` foutloos. nb_outputs-diff tegen de F0-uitvoer is gelijk
aan die van F1 (41+/21−, dezelfde bedoelde verschillen); in F4 is geen codecel gewijzigd.

**Feitenlijst F2 (5 fout, alle opgelost).** Tabellen: replicatieblok zegt nu "geen
tijdreekstoets die we kunnen herhalen". 8,4%: Opzet noemt 6,8% log (simulatie) en ≈ 8,4%
rekenkundig, plus dat het toy 10% gebruikt. Bel-verwijzing: 03-15 vervangen door 05-33
(Cochranes decompositie met de bel als restterm). $e$: "$20 \times 2{,}72$". Miller-Modigliani:
NCW-nul-argument, MM als verwant maar niet hetzelfde.

**Lezerspunten 1–10, alle gedaan.** 1 zie 8,4%. 2 identiteit gedeeld door $d_t$ over $K$
jaar toegevoegd in "Hoe het getoetst wordt", met lees-zin (groei, rendement of ratio op
$t+K$). 3 identiteit blijft eindig en neemt niets aan; transversaliteit hoort alleen bij het
model. 4 rest 0,47 log-punt genoemd, bij benadering, gekoppeld aan de identiteit.
5 standaardfout van 2% uitgerekend ($20/\sqrt{100}$) en onderscheiden van 0,93. 6 waarom
weglaten verdedigbaar is: elke $b_0$ geeft een andere prijs. 7 $R^2$ 0,05 in het oordeel.
8 waarom-alinea transversaliteit is nu een koper met een richting. 9 theorie-of-feit-vraag
eerst gesteld. 10 wat de variantiedecompositie ontleedt.
Ook: 13 ($\E_t$ uitgelegd), 15 (via MM-fix), H6 in Samengevat (lage ratio), H8
Theorie-inleiding. Niet gedaan: 11 (orde van grootte Stambaugh-bias vraagt een nieuwe
simulatie, buiten het woordbudget), 12 (dividendrendement is de vaste term uit §3), 14
(bbp-groei: getal zonder cel of bron).

**Betaling.** Geschrapt: "Een debat over de vraag of aandelen duur zijn" en de
log-kalibratie-bijzin in de simulatie (samen ≈ 40 woorden); netto +121, onder 5.500.

**Navertel-toets, afwijkingen.** "Hoe het getoetst wordt": stap identiteit → lage
rendementen ontbrak; nu staat de identiteit in PD-vorm met lees-zin. "Kernresultaat":
tegenspraak identiteit/transversaliteit; opgelost door de identiteit eindig te houden.
"Opzet": verwarring over $r$; opgelost met één zin over 10%, 6,8% en 8,4%.

**Labels.** Ongewijzigd. Vooruitverwijzingen buiten "Wat er brak": twee (05-33, 04-20).

## F5-1

**Meting.** words=5446, para_mean 45, semicol 7: PASS. Sync en `HAP_OFFLINE=1 --execute`
foutloos, geen warnings. nb_outputs-diff tegen F0: als F4, plus alleen presentatie
(kolomnamen kalibratie en simulatie voluit, "rond 10%" in de vergelijkingstabel, die cel
nu na de CAPE-cel). Geen getal veranderd.

**Feitelijke fout.** Gedaan: Opzet noemt nu 8,4% (gewoon gemiddelde) en 6,8% (log), geen bereik.

**Helderheid.** Stambaugh-schakel: gedaan (persistentie te laag geschat, schokken bewegen
samen, helling negatiever). 0,15 + 0,38 + 0,47 = 1: gedaan, met de identiteit in logs en
de drie hellingen. Dubbele $b$: gedaan, de bel heet nu $B_t$ (tekst en oefening 1; codenamen
ongewijzigd, Engelse code telt niet mee).
**Opbouw.** Simulatieconclusie komt terug in "Waar het breekt" (factor twee tegen een ratio
van 10 tot 86, en de beweging voorspelt rendementen). "Hoe het getoetst wordt" opent met de
conclusie. Replicatie herordend: regressies, figuur, CAPE, log-punt en identiteit, warning,
vergelijkingstabel, oordeel als slot. Lengte: 5.446, onder de grens.
**Taal.** "Die rij kiest $r$" wordt "Dat getal nemen we als $r$"; "definieert het tijdvak"
vervangen; stapelzin in drie zinnen; $b$ dubbel opgelost.
**Code en figuren.** "rond 10%": gedaan. Kolomnamen voluit: gedaan. Zin vóór de figuur over
drie waarden van $r$: gedaan.
**Replicatie.** Oordeel en CAPE-alinea verwijzen naar de tabel in plaats van getallen te
herhalen; "Wat er brak" houdt één getal per kanaal ($R^2$).
**Oefeningen.** Instap (2): eindwaarde daalt 17,5% (21,00 → 17,33), met beide oorzaken.
**Overig.** Boomgaard: het buurman-beeld is niet meer aan Williams toegeschreven.
Afgewezen: geen.

**Rubriekronde.** Nagelezen: elke cel heeft een zin ervoor en erna (de vergelijkingscel
wordt direct gevolgd door het oordeel); Samengevat en vooruitverwijzingen (twee) ongewijzigd.

## F6-1

**Meting.** words=5470, semicol 6: PASS. Sync en `HAP_OFFLINE=1 --execute` foutloos, geen
warnings. nb_outputs identiek aan F5 (codecellen lezen de helling nu als
`params["log_pd"]` / `["log_cape"]`, zelfde uitvoer).

**Fouten.** (1) "verklaart het grootste deel van de beweging" wordt "draagt ruim twee keer
zoveel van de beweging als de dividendgroei" (0,38 tegen 0,15). (2) "De simulatie meet
6,8%" wordt "Shillers data, waarop de simulatie kalibreert, geven 6,8%".

**Top drie.** (1) Log-identiteit: benadering benoemd (latere jaren wegen iets onder één,
kleine dividendrendementterm; 0,47 is een orde van grootte). (2) Vooruitverwijzingen van
vier naar twee (bel → 05-33 en $t$-waarden → 04-20 geschrapt; blijven: 04-20 bij
Campbell-Shiller, 05-33 bij risico of vergissing). PVGO had al de zin "waar $g$ vandaan
komt"; CAPE niet ingekort maar kreeg een verwachting en een oordeel. (3) Log-punt-uitsplitsing
in een tabel (0,15 / 0,38 / 0,47 / 1). Ook: puntkomma-zin in Theorie gesplitst, helling
benoemd in de code.

**Naadpunten.** 2: Opzet zegt in één zin dat $p_t$, $d_t$ niveaus zijn, met reden (de som telt
bedragen op) en de wissel ten opzichte van L2. Let wel: de setup zoals die nu in de werkmap
staat, gebruikt zelf $p_t$ en $d_t$ als niveaus ("Zonder aankondiging zijn alle grootheden
niveaus"); L3 volgt dus de setup en ik heb geen afwijking van de setup gemeld, omdat die
er niet is. Staat de setup straks op $P_t$, $D_{t+1}$, dan moet deze zin mee. 3: $R = 1 + r$
bruto, $r$ netto simpel staat expliciet; L3 gebruikt geen $R^f$. 9: "Wat er brak" zegt nu
dat het model pas na het CAPM zo getoetst werd, in lijn met de setup. 10: opgelost via
fout (1); L4 "vooral doordat $r$ beweegt" is niet van mij.

**Afgewezen.** Geen. Stambaugh-getal niet toegevoegd (geen cel; buiten de top drie).

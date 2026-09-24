STATUS 02_05_crsp_tape F6b words=5231 prose=PASS open=1 cijfer=- min=-

# Rapport 02_05_crsp_tape

## F0

`prose_stats`: words=5754, sent_mean 20,4, sent_p90 37, sent_gt40 22, para_mean 59, dash 26,
semicol 43, motief 2, deel 1, je_form 7, stopw 8, calque 3, engquote 10. `--check`: FAIL op
words, sent_mean, sent_p90, sent_gt40, para_mean, dash, semicol, motief, deel, je_form,
stopw, calque, engquote. `--where`: "Poor's" (r. 54), "epistemisch" (r. 60), "tot vandaag" (r. 90).

Woorden per sectie: kop 135, Overzicht 375, Intuïtie 304, Toy 331, Rendement in een
database 249, Delistings 365, Survivorship 408, Look-ahead 202, Weging 456, Simulatie 604,
Replicatie weging 514, Replicatie Shumway 742, Wat er brak 418, Oefeningen 671.

**Vijf grootste problemen**
1. Taal (§11.1, §11.2): gemiddelde zin 20,4 woorden, 22 zinnen boven 40, 43 puntkomma's,
   26 gedachtestreepjes, 7 keer "je" (Intuïtie, Toy, Theorie), alinea's van 59 woorden.
2. Overzicht (§11.7, §11.3): begint met de Engel-anekdote in plaats van vraag en antwoord,
   geen lijst, imports-cel aan het eind, "Deel II", "epistemische status" (r. 58–60).
3. Theorie (§11.6, H3): geen routekaart en geen Samengevat; vier resultaten plus een
   bid-ask-afleiding; open bewijzen boven zes regels (survivorship, rebalancing); de
   survivorship-stelling bevat drie beweringen; "Waarom" staat na de opzet.
4. Simulatie en replicatie (§11.5, §11.8): getallenalinea's (r. 735–753, 891–902,
   1061–1082); replicatieblok Shumway ruim 330 woorden met twaalf getallen; tabel
   `published` mengt origineel en voorspelling over de rijen; `size_deciles` gebruikt een
   argsort/put_along_axis-truc; cel met vier functies (52 regels); drie cellen zonder
   tekst ertussen; bijschrift noemt "het 2%-motief" en 7343/3193 uit geen cel.
5. Toy en oefeningen (§11.7): toy toont twee mechanismen (split én ontbrekende
   waarnemingen) en eindigt met `print` in plaats van een tabel hand/code; oefening 1 is
   geen instap; geen uitwerking eindigt met "Wat dit leert:".

**Controle eis 2 (grep in `lectures/`).** Van buiten aangehaald: alleen het paginalabel
(01_04, 02_06, 02_08, 03_16, 04_18, 04_24, 04_25, 08_38, 08_39). Inhoudelijk aangehaald:
survivorship bij fondsen met {cite}`BrownGoetzmannIbbotsonRoss1992` (02_06, 04_25, 04_24,
08_38); de size-premie per deelperiode (03_16 r. 838); bid-ask-bias en ontbrekende delisting
returns in equal-weighted portefeuilles (04_18 r. 239); het Compustat-selectie-effect van
{cite}`KothariShankenSloan1995` (04_18 r. 551); de size-premie die aan de constructie hangt
(03_16 r. 25). Die passages blijven, ingekort. Geen sublabel wordt elders aangehaald.

**Schraplijst (schraptoets §11.11)**

| kopje | passage | ~woorden | eis niet gehaald |
|---|---|---|---|
| Overzicht | Engel-anekdote inkorten, Compustat-zin, alinea "definieert het tijdvak" | 150 | 1 |
| Intuïtie | split-voorbeeld en vierde vraag inkorten (toy en Theorie dragen ze) | 60 | 1 |
| Toy | constructie "zonder split-aanpassing" (tweede mechanisme), dubbele handstappen | 90 | 1 |
| Rendement in een database | opslag in CRSP, reverse split, prijsrendement en index | 90 | 1 |
| Delistings | value-weighted uitbreiding van de stelling naar één zin | 40 | 1 |
| Survivorship | limiet als derde bewering (wordt één zin), BGIR-alinea inkorten (eis 2 blijft) | 90 | 1 |
| Look-ahead | formele $\mathcal{F}_t$-alinea; Kothari blijft (eis 2, 04_18) | 90 | 1 |
| Weging | rebalancing-stelling met bewijs wordt formule met citatie; bid-ask inkorten (eis 2) | 200 | 1 |
| Simulatie | tip over twee doorgangen, getallenalinea's, alinea "ruis kleiner" | 200 | 1 |
| Replicatie weging | blok en getallenalinea's inkorten | 180 | 1 |
| Replicatie Shumway | blok van 330 naar ~180, omgekeerde rekensom inkorten | 280 | 1 |
| Wat er brak | elk element onder 120 woorden | 90 | 1 |
| Oefeningen | Nasdaq-simulatie (ex-3) schrappen; uitwerkingen korter; nieuwe instap | 300 | 1 |

Som ≈ 1.960 woorden. Verwachte lengte na F1 ≈ 5.754 − 1.960 + ≈ 250 (routekaart,
Samengevat, lees-zinnen, zinnen rond cellen, instap-oefening) ≈ 4.950. Onder 6.000 zonder
de kern te raken; geen split.

## F1

**Eindmeting.** words=4650, sent_mean 14,6, sent_p90 22, sent_gt40 2 (Overzicht-lijst en
Samengevat, telartefact), para_mean 44, dash 4, semicol 10, stopw 3, calque 0, engquote 3:
PASS. `--where` leeg. `--sync` en `HAP_OFFLINE=1 --execute` foutloos, geen warnings.

**Geschrapt** (schraptoets eis 1, niet nodig voor de vraag, tenzij anders vermeld):
Engel-anekdote ingekort, Compustat-historie en "Deel II"-alinea; split-alinea en vierde
vraag in Intuïtie; toy-constructie "zonder split-aanpassing" (tweede mechanisme) en de
`print`-regels; CRSP-opslag, reverse split, prijsrendement en index bij de definitie; de
value-weighted uitbreiding als deel van de stelling (nu één zin); de limiet
$\sqrt{\pi/2}\,\sigma/\sqrt T$ als derde bewering (H3, nu één alinea) en de warning; de formele
$\mathcal{F}_t$-alinea bij look-ahead (Kothari en BGIR blijven, eis 2); rebalancing-stelling
met bewijs (nu formule met citatie en getal); bid-ask-afleiding ingekort (eis 2, 04_18);
tip over twee doorgangen (één zin); getallenalinea's in simulatie en replicatie; figuurgetallen
7343/3193 (uit geen cel); replicatieblokken ingekort; oefening Nasdaq-simulatie ($D=-55\%$).

**nb_outputs-diff**, elk verschil bedoeld: cel 2 (toy) is nu een tabel hand/code met drie
constructies (rij "zonder split-aanpassing" en de prints vervallen; −0,035/0,0025/0,03125 en
−0,14167/0,0098/0,12875 gelijk); cel 3 kolom- en rijnamen; cel 4 gesplitst in hulpfuncties
(4) en `simulate` (5), `size_deciles` met `stats.rankdata` in plaats van argsort/put_along_axis;
cel 6 toont een Series in plaats van prints (0,4758 en 0,0324 gelijk); replicatiecel gesplitst
in laden (11) en `describe` (12); cel 15 (`published`) heeft nu origineel/hier/verschil op twee
rijen (1,82/1,623 en 1,45/1,563 gelijk; 5,21 is nu tussenresultaat `h_shumway`); nieuwe cel 18
(instap, −0,2/0/0,2); Nasdaq-cel vervallen; celnummers verschoven. Alle overige tabellen en
beide figuren (119200 en 129356 bytes) gelijk. Geen aangehaald getal veranderd.

**Afvinklijst §11.9, wat niet voldoet.** Geen. Overige: ok. Vooruitverwijzingen buiten
"Wat er brak": nul. "De standaardfout van 2%" twee keer, beide naar `#00-01-rendementen`.

**Labels.** Vervallen (nergens anders aangehaald): `eq-crsp-tape-survivorlimiet`,
`thm-crsp-tape-rebalancing`. `cel-crsp-tape-simfuncties` staat nu op de `simulate`-cel.
Paginalabel en alle overige labels ongewijzigd.

**Open punten.** (1) H11: de simulatie kalibreert op Shumways $D = -30\%$, niet op een
toy-getal; de koppeling loopt via de formule $h(\mu_a - D)$. (2) Niet met projectbronnen te
verifiëren: de 50.000 dollar en de Engel-anekdote (stonden er al, "volgens CRSP"). De print
voor 1976 in cel 17 wordt in de tekst niet meer aangehaald.

## F4
**Meting.** words=4926 (+276; betaald met "Risico of vergissing" van 193 naar 115 woorden
en de geschrapte Santa-Clara-zin), para_mean 45, sent_gt40 2 (lijsten): PASS. `--where`
leeg; `--sync` en `HAP_OFFLINE=1` foutloos, geen warnings. Geen code veranderd: de
`nb_outputs`-diff tegen `voor` is dezelfde als in F1.

**Feitenlijst (5, alle opgelost).** (1) "vanaf het vijfde deciel kleiner dan 0,3 pp" (cel 8).
(2) "In 1956 10%, in 1976 ruim de helft en nu nog bijna 40%" (cel 17). (3) Random walk uit
Overzicht en "Wat de tape verklaart"; "Wat er daarna kwam": de tape gaf rendementen, Fama het
argument, zoals L6. (4) Stelling en bewijs netto ($r^{a}$, $\bar r$, $D$ over de hele periode);
bid-ask expliciet bruto. (5) Engel en 50.000 dollar geschrapt (bron niet in de bib); blijft
wat L0 bevestigt: vanaf 1960, geld van Merrill Lynch.

**Lezerspunten, alle vijftien verwerkt.** 1 simulatie is een Chicago-wereld met premie nul,
"kiest geen kant"; 2 meer jaren helpen, niet ten opzichte van de ruis (6,3% na een eeuw,
handberekening), meer aandelen niet, Intuïtie aangepast; 3 kader "over hun 35 jaar",
elders "een eeuw jaarrendementen met 20% volatiliteit"; 4 twee bronnen van de 3,1 pp,
blokverwachting aangepast; 5 $D$ tegenover $r^{\text{DL}}$ met het toy; 6 tabel VII per jaar,
daling bij $-100\%$ is $h(\mu_a+1) \approx h$, Nasdaq per maand; 7 bruto; 8 Chicago en Yale in
één zin, Santa-Clara geschrapt (lengte); 9 Banz; 10 zin over uitvoerbaarheid, kopje
"overlevers en look-ahead"; 11 $h \approx 3\%$ per maand, 1,6 pp; 12 6,9%; 13; 14
NYSE-breekpunten; 15 "steekproef die in 1962 begint".

**Navertel-toets.** Afwijkend waren Replicatie weging (nu de twee bronnen van de 3,1 pp) en
"Risico of vergissing" (nu de rol van de simulatie). Open: H11-kalibratie ($D=-30\%$).

## F5-1
words=5133, `--check` PASS; `--sync` en `HAP_OFFLINE=1` foutloos, geen warnings.
**Feitelijke fouten.** (1) Eeuw-waarde exact: $P = 0{,}159$, fout 5,3% (nieuwe rij "klein, na een
eeuw" in de survivorship-cel: 0,15852 / 0,05308). (2) "vierde" wordt "derde" deciel. Gedaan.
**Drie verbeteringen.** (1) Code: `simulate` gesplitst in `draw_universe` (genereert, als
generator), `last_delisting` en `measure`; de state-truc vervangen door `copy.deepcopy(rng)`
(één import erbij in de imports-cel) met een zin ervoor. `decile_mean` met een lus over tien
decielen, `size_deciles` met benoemde tussenresultaten en een zin ervoor. Dezelfde trekkingen in
dezelfde volgorde: alle simulatietabellen, beide figuren en oefening 2 byte-gelijk. (2) Engel
geschrapt (bron niet in de bib, zie F4); slotzin Intuïtie herschreven; Shumway getoetst met
$h(\mu_a - D)$: 1,734 tegen 1,82 en 1,627 tegen 1,45 (was 1,623 en 1,563 met $h|D|$; tekst,
tabel en Kernresultaat ($1{,}7$ pp) aangepast, oordeel blijft "Geslaagd"). (3) Weegblok "Wat"
koppelt de weging aan de delisting-fout; SE van het premieverschil uit de maandelijkse
verschilreeks (nieuwe kolommen; eeuw 3,93 pp, SE 0,76).
**Overige aanmerkingen.** Herbalanceringswinst als benadering ($g \approx \mu - \sigma^2/2$): gedaan.
Herbalanceringswinst en bid-ask komen terug in de replicatie (meetkundig 12,30 tegen 10,33;
bronnen van het decielverschil) en in Samengevat: gedaan. "men" wordt "we"; puntkomma-zinnen in
Replicatie geknipt; "Dat werk definieert het tijdvak" wordt "Met dat werk begint het tijdvak":
gedaan. Break-even-cel zonder `print`; aandeel kleinste deciel is een eigen tabel: gedaan.
Oefening 2.1 met de richting bij positieve drift: gedaan. Toy: dividend en split samengevoegd
tot één stap "recept"; niet verwijderd, want STYLE §11.7 wil dat het toy de ene niet-afgeleide
formule gebruikt die Theorie als eerste afleidt ([](#eq-crsp-tape-totaal)).
**nb_outputs-diff tegen F4.** Alleen: derde rij survivorship-cel, Shumway-kolom
"hier: h (mu_a - D)", twee kolommen in de premietabel, prints vervangen door een tabel.
Open: H11-kalibratie ($D=-30\%$).
Controle 1: "de herbalanceringswinst" geschrapt uit de bronnen van het decielverschil (Replicatie weging), in lijn met eq-crsp-tape-bonus; geen code gewijzigd, words=5131, PASS.

## F6-1
words=5231, `--check` PASS; `--sync` en `HAP_OFFLINE=1` foutloos, geen warnings.
**Fouten.** (1) "veertien" wordt "vijftien". (2) "hangt alleen af van de overleefkans" wordt
"$z_0/T$ maal kans op schrappen gedeeld door kans op overleven". (3) EW > VW binnen deciel 1
niet meer toegeschreven: volgens eq-ewvw zelf een size-premie; bid-ask en delisting kunnen
bijdragen, maar de data scheiden dat niet.
**Meer data.** Eén zin, gelijk in Overzicht, Intuïtie en "Wat er brak": meer data halen de
fout niet onder de ruis; de delisting-fout blijft, die van overlevenden krimpt hoogstens even
snel als de ruis.
**Top drie.** (2) Weegblok en oordeel: 3,77 pp als bovengrens (als de andere bronnen niet
negatief zijn); Shumway: Nasdaq-rij onafhankelijk, tweede rij toetst alleen lineariteit in $r^{\text{s}}$.
(3) Toy terug tot aandeel C: A en B zonder dividend en split (A 40/44/44/44/48,40; B 60/60/66/66/
59,40, dezelfde rendementen); de dividend- en splitvoorbeelden (0% en +10%) staan nu in de Opzet.
**Naad.** (7) kader: "rekenkundig gemiddelde 11,7%, SE 3,9 pp" naast de meetkundige 9,0%.
(3) $X, x_0$ worden $Z, z_0$; $x_{i,t}$ wordt $s_{i,t}$. (4) $D$ wordt $r^{\text{s}}$. (5) $\tau$ wordt $\theta$.
(8) "overlevers" wordt overal "overlevenden". Ook: Jensen-regel bij bid-ask, `last_delisting`
zonder one-liner, "delisting-fout" wordt "fout door ontbrekende delisting returns".
**nb_outputs-diff tegen F5.** Alleen labels (overlevenden, z0, r_s) en de simulatiefiguur
(legendatekst, 119320 bytes); alle getallen gelijk. Open: H11-kalibratie.
Diffcontrole: codecommentaar r. 927 gebruikt nu r_s in plaats van D; alleen sync, uitvoer ongewijzigd.

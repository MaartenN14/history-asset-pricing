# Rapport L3 01_03_williams_ddm (taak 0, A, B; niet gecommit, niet gebouwd)

1. **prose_stats** (words sent_mean p90 gt40 para dash semicol motief Lnum deel u je taboo stopw calque engquote)
   - vóór: `5123 19.5 34 11 64 50 24 0 0 0 39 4 0 19 6 4` FAIL op 10 metrieken
   - ná:   `5478 14.0 22 0 44 0 8 0 0 0 0 0 0 0 0 2` PASS; `--where`: geen treffers

2. **Top-5 uit taak 0, en wat ermee gebeurde**
   - Aanspreekvorm 39x "u", 4x "je", overal (§3.2). Alles naar "we", onpersoonlijk of de koper/analist als onderwerp.
   - Lange zinnen, 50 gedachtestreepjes, alinea's van 64 woorden, vooral in Intuïtie, Theorie en Replicatie (§3.1). Gesplitst; nu 0 streepjes, 0 zinnen boven 40.
   - Overzicht begon met geschiedenis, imports-cel stond in Overzicht, "epistemische status" (§3.13, §3.3). Nu vraag/antwoord, lijst, één alinea geschiedenis. Imports-cel staat aan het begin van het toy. "theorie of feit" onder die naam.
   - Toy: prints en een dividendtabel in plaats van hand/code-tabel. De gevoeligheidscel was een tweede mechanisme met een eigen `###` (§3.7). Nu opzet-tabel, zes stappen, één cel, tabel "met de hand / code". Eén recept ($d/(r-g)$), dat Theorie afleidt.
   - Theorie zonder routekaart of Samengevat. Gordon-bewijs open, 5 vooruitverwijzingen, "2%-motief" 2x, calques ("Onthoud dat", "Twee dingen", "Dat is de reden dat", "Noteer", "Merk op") (§3.6, §3.3, §3.12). Routekaart, Samengevat en `###` in de vaste volgorde toegevoegd. Gordon-bewijs in dropdown, lees-zin bij elke genummerde vergelijking, calques weg.

3. **Verplaatst (niets geschrapt)**
   - De `###` "De gevoeligheid die alles bepaalt" ging van het toy naar Theorie, onder Gordon. De handgetallen staan nu in een tabel.
   - Het Gordon-bewijs staat in een `{prf:proof}` met dropdown.
   - Verwijzing naar vroege anomalieën (PVGO): naar "Wat het model verklaart".
   - Verwijzing naar voorspelbaarheid in de Stambaugh-waarschuwing: naar "Waar het breekt".
   - Verwijzing naar Shiller (scheefheid, einde Simulatie): naar "Risico of vergissing". In de hoofdtekst staan nu 2 vooruitverwijzingen (bel naar 03-15, Campbell-Shiller naar 04-20).
   - Replicatieblok ingekort van ongeveer 330 naar 165 woorden. Over Gordon (1959) en de $R^2$-verwachting staat nu een alinea onder het blok. De reeksnamen staan als commentaar in de panelcel. De opmerking over Newey-West staat in de zin vóór de regressiecel.
   - De slotalinea over "epistemische status" staat nu als alinea "theorie of feit" vóór "Wat er daarna kwam". Het Nobelprijs-zinnetje staat daar ook, zodat "Risico of vergissing" onder de 120 woorden blijft.
   - Nieuw: oefening `ex-williams-ddm-instap` (toy met 4% in plaats van 5% eindgroei), vóór de bestaande drie. De labels ex-1/2/3 zijn ongewijzigd, maar de weergegeven nummering schuift één op.

4. **nb_outputs-diff** (vóór = HEAD tegen ná). Alleen bedoelde verschillen, geen enkel getal veranderd, figuren byte-gelijk:
   - cel 2 (toy): de drie prints en de dividendtabel zijn vervangen door de tabel "met de hand / code", met dezelfde getallen (27.951, 24.0, 0.875, 1.39755, d_1..d_3).
   - cel 3: drie prints weg (21.00, 26.25, 26.50). Die getallen staan in het rooster, dat identiek is gebleven. Het rooster wordt nu met een zichtbare lus gebouwd in plaats van een geneste comprehension.
   - cel 8: de eerste regel is nu een commentaarregel; de uitvoer is identiek.
   - nieuwe cel 12 (instap): 17.3333 / 20.3333 / 0.8525 / -0.1528. Daardoor schuiven de volgende celnummers één op.
   - PVGO-cel: de inline-berekening heeft nu een eigen naam (`p_low_roe`); de uitvoer is identiek. De volgorde van de rng-trekkingen is ongewijzigd.
   - Na A is gelijk aan na B.
   - Execute-log (laatste regels): `Executing notebook with kernel python3` / `Warning: Notebook is not trusted` / `Writing lectures/01_03_williams_ddm.ipynb`. Exit 0, 0 stderr- of error-outputs.

5. **Afvinklijst §11.9**, wat niet volledig voldoet:
   - `words` = 5478, net onder 5500.
   - Het toy gebruikt twee dingen die nog niet zijn afgeleid: de som van de verdisconteerde dividenden (de intuïtie van Williams) en het recept $d/(r-g)$. Theorie leidt eerst de som af en daarna het recept als propositie.
   - De replicatie heeft geen "origineel" om mee te vergelijken. De tabel zet "onder constante $r$ (Williams)" naast "hier". Het oordeel luidt "Niet geslaagd voor Williams' lezing, zoals het blok verwachtte".
   - De CAPE-variant blijft in de hoofdtekst: geen lecture zet codecellen in een `{note}`-dropdown, dus dat is niet getest zonder build.
   - Overige: ok.
   - Kleine correctie in het bijschrift van de hyperboolfiguur. "rechts ervan explodeert hij" is nu "vlak ervoor explodeert hij", omdat rechts van $g = r$ geen curve staat.

8. **Open punten**
   - Niet gebouwd (volgens opdracht), dus MyST-warnings zijn niet gecontroleerd. Dat geldt met name voor de tabel met lege cel onder Gordon en voor de losse lijsten (lege regel tussen de items, nodig voor de zinsmeting van prose_stats).
   - Tijdens mijn werk wijzigden andere agents 01_02 en 01_04 (git status). De aansluiting is gecontroleerd tegen hun stand van dat moment. 01_04 "Wat we al weten" klopt nog (niveau, $r$, replicatie: vooral $r$).
   - prose_stats telt "2%-motief" niet als `motief`. Hier handmatig opgelost; aanpassen van de regex valt buiten mijn bevoegdheid.

## Lezersronde (taak C)

**Per H-regel: 33 punten opgelost, 0 afgewezen.**
- H1 1/0: het waarom bij Gordon is nu een handeling (een analist kiest $g$ en $r$), met richting.
- H2 8/0:
  - de standaardfout van 2% wordt in de Simulatie en in oefening 3 in één zin uitgelegd;
  - $e_1$ wordt vóór gebruik gedefinieerd;
  - $\rho$ krijgt zijn betekenis;
  - Newey-West wordt uitgelegd, met de reden voor negen vertragingen;
  - variantiegrens en decompositie worden in de warning benoemd;
  - Miller-Modigliani wordt in één regel herhaald;
  - $b$ tegen $b_t$: er staat nu een opmerking. De letter is niet gewijzigd, omdat oefening 2 en de code ook $b$ gebruiken.
- H4 2/0:
  - $\sigma_g = 11{,}5\%$ staat nu in de tekst;
  - de groeisnelheid van de bel staat er nu ook: verdubbeling in ruim 7 jaar bij $r = 10\%$, tegen 14 jaar voor 5% dividendgroei.
- H5 2/0: het bewijs van de DDM noemt nu niet-negatieve dividenden en een eindige prijs. Ze staan in het bewijs, niet in de stelling.
- H6 2/0: Samengevat geeft de reden achter de richting van $r$ en $g$, en het effect van een hogere $b$ bij ROE > r en ROE < r.
- H7 4/0:
  - "discontovoet" overal. Alleen bij de eerste invoering staan nog "tarief" en "*interest rate*".
  - "eindwaarde" = verwachte verkoopprijs op $t=3$; "staart" en "restterm" zijn weg.
  - "inhoudingspercentage" overal.
  - "fundamentele waarde" in de tekst. De kolomnaam "fundamenteel" in oefening 1 blijft, anders verandert de uitvoer.
- H8 5/0: noot, slot van het toy-voorbeeld, CAPE-overgang, "probleem met de noemer" (nu uitgelegd: uitkeringsbeleid en inkoop) en oefening 3.
- H9 5/0: de conclusie staat nu vooraan na het rooster, vóór de figuur, na de regressie, na CAPE en bij PVGO. PVGO opent nu met de bewering.
- H10 4/0:
  - de identiteit krijgt een voorbeeld ("bezit is schuld plus eigen vermogen");
  - persistentie wordt concreet: autocorrelatie 0,91 van de log-PD. Die is buiten de lecture berekend en staat alleen in de tekst;
  - bij de warning worden de voorbeelden genoemd;
  - Newey-West, zie H2.

**Navertel-afwijking.** In "Wat er brak" wist de lezer niet welke "identiteit" bedoeld was: onder transversaliteit, of zonder aanname over $r$. Dit viel samen met spoor 1: [](#eq-williams-ddm-pd) bevat een constante $r$ en is toch "de identiteit".
- Na het DDM-bewijs staat nu een alinea met de identiteit zonder aanname over $r$, als ongenummerde vergelijking: $p_t = \sum_j d_{t+j}/(R_{t+1}\cdots R_{t+j})$, met gerealiseerde rendementen. Daarbij staat dat [](#eq-williams-ddm-ddm) het bijzondere geval met constante verwachte $r$ is.
- Dezelfde verduidelijking staat nu in "Hoe het getoetst wordt", in de conclusie van de replicatie, in "Wat het model verklaart" ("geschreven met gerealiseerde rendementen, en onder de transversaliteitsvoorwaarde") en in "Waar het breekt" ("de aanname van constante $r$").
- Andere secties weken niet af.

**Waar de lezer het spoor kwijtraakte.**
- Spoor 1 is opgelost zoals hierboven.
- Spoor 2: de tekst zegt nu dat de rendementsrij $r$ kalibreert. $r$ is daarna in de simulatie bekend, dus de werkelijke onzekerheid is groter dan de simulatie laat zien. Ook staat erbij waar de standaardfout van 2% vandaan komt.
- Spoor 3: de tekst zegt nu waarom CAPE winst gebruikt: het dividend hangt af van het uitkeringsbeleid, inkoop van eigen aandelen telt niet mee, en de winst wordt over tien jaar gemiddeld.

**Verificatie.**
- `prose_stats --check`: `6010 14.4 22 0 45 0 11 0 0 0 0 0 0 0 0 3`, met alleen FAIL op words (6010 > 5500).
  - Reden: de ruim 530 woorden erbij zijn de verduidelijkingen waar de lezer om vroeg. Verplaatsen naar een dropdown verlaagt de telling niet, en schrappen mag niet.
- `--where`: geen treffers.
- sync en execute: exit 0, geen stderr- of error-uitvoer. Log eindigt met `Writing lectures/01_03_williams_ddm.ipynb`.
- nb_outputs-diff tegen de tussenstand na taak A: leeg.

## Lezersronde 2 (tweede koude lezer)

**Twee vaste namen.**
- *De boekhoudkundige identiteit*: de som met gerealiseerde rendementen, direct uit de definitie van rendement. Ze neemt niets aan en kan niet worden verworpen.
- *Het model van Williams*: dezelfde som met een constante verwachte discontovoet (`eq-williams-ddm-eindig`, `eq-williams-ddm-ddm`). Het model kan wel door de data worden verworpen.

Wat er in de tekst veranderde:
- "Van de definitie" leidt nu eerst de identiteit af (eindig, ongenummerd) en daarna het model. Bij de eerste keer staat in één alinea wat het verschil is en waarom het ertoe doet: de replicatie toetst het model, niet de identiteit.
- De losse alinea "Welk deel hiervan is een identiteit" na het DDM-bewijs is opgegaan in die afleiding.
- Elke "identiteit" is nagelopen met grep en vervangen door een van de twee namen. Dat geldt voor het Overzicht, de routekaart, "Hoe het getoetst wordt", Campbell-Shiller (loglinearisatie *van de identiteit*), Samengevat, de conclusie van de replicatie, CAPE en "Wat er brak".
- De labels staan er allemaal nog en de vergelijkingen hebben dezelfde inhoud.

**Per H-regel: 27 opgelost, 3 afgewezen.**
- H1 3/0:
  - "Van de definitie" heeft nu een richting: hogere dividenden geven een hogere prijs, een hogere discontovoet een lagere.
  - Het waarom bij het kernresultaat begint nu met een koper die een aandeel koopt om het door te verkopen.
  - Bij Gordon is de reeks-reden uit het waarom gehaald; die staat nu alleen in het bewijsidee.
- H2 4/0:
  - Cowles en Kendall krijgen elk een bijzin.
  - De $R$/$r$-notatie wordt ter plekke uitgelegd.
  - De standaardfout van 2% wordt in de Simulatie en in oefening 3 in de zin zelf uitgelegd.
- H3 1/0: de tweede vorm van Gordon heet nu "dezelfde bewering, omgeschreven naar $r$". De propositie zelf is niet gewijzigd, omdat label en nummering blijven.
- H4 0/2, afgewezen: hoe groot het Newey-West-tekort en de Stambaugh-bias zijn, vraagt een eigen simulatie. Die hoort bij de lecture over voorspelbaarheid, en een getal zonder codecel verzin ik niet. Wel toegevoegd: de richting en het mechanisme van de Stambaugh-bias.
- H5 4/0:
  - Niet-negatieve dividenden en een eindige prijs staan nu in de opzet.
  - "Eén aanname" is "twee aannames" geworden (constante $r$ en transversaliteit).
  - Bij $r > 0$ staat nu waar het nodig is.
  - De aannames achter $g = b\cdot\mathrm{ROE}$ worden genoemd.
- H6 2/0: Samengevat geeft nu de reden voor het effect van $b$, en de richting bij een hoge prijs-dividend-ratio.
- H7 4/1:
  - "discontovoet": in de opzet vastgelegd als gelijk aan het verwachte rendement, en "rendement eist" vervangen;
  - "eindwaarde" overal, "staart" en "laatste term" zijn weg;
  - "prijs-dividend-ratio" in plaats van "de ratio". De kolomnaam "PD-ratio" in oefening 1 blijft, omdat de uitvoer gelijk moet blijven;
  - "identiteit": zie de twee vaste namen hierboven.
  - Afgewezen: $b$ voor bel én inhoudingspercentage. Oefening 2 en de code gebruiken $b$, en de dubbele betekenis staat al aangekondigd.
- H8 3/0: "Die oneindige waarde", de standaardfout van 2% (geen "dat" meer over een alineagrens), en "Dezelfde steile hyperbool".
- H9 3/0: Opzet en "Van de definitie" openen nu met een bewering. Na de scatterfiguur staat eerst wat de figuur laat zien.
- H10 3/0:
  - "prijs van risico" krijgt een voorbeeld;
  - de loglinearisatie wordt concreet: benadering rond een gemiddelde prijs-dividend-ratio van ongeveer 26, buiten de lecture berekend;
  - de variantiedecompositie wordt in een bijzin uitgelegd;
  - de Stambaugh-bias krijgt een voorbeeld.

**Navertel-afwijkingen.**
- "Van de definitie": het "eindige versie van de identiteit" bevatte een constante $r$. Opgelost: die vergelijking heet nu "eindige versie van het model van Williams", en de identiteit gaat eraan vooraf.
- "Kernresultaat": het was onduidelijk wat eerder "identiteit" heette. Opgelost met de twee vaste namen.

**Sporen.**
- Spoor 1 (de formule kwam onverwacht): opgelost door de nieuwe volgorde.
- Spoor 2 (PVGO): PVGO heet nu in één zin een zijstap die simulatie en replicatie niet gebruiken.
- Spoor 3 (Simulatie):
  - de tekst zegt nu expliciet dat de simulatie alleen de onzekerheid in $g$ isoleert;
  - de belofte in het toy luidt nu "hoe zwaar een schattingsfout in de groeivoet weegt".

**Verificatie.**
- `prose_stats --check`: `6351 14.5 22 1 44 0 14 0 0 0 0 0 0 0 0 3`, met alleen FAIL op words.
  - Reden: de twee lezersrondes hebben verduidelijkingen toegevoegd. Verplaatsen naar een dropdown verlaagt de telling niet, en schrappen mag niet.
- `--where`: geen treffers.
- sync en execute: exit 0, geen stderr- of error-uitvoer.
- nb_outputs-diff tegen de tussenstand na taak A: leeg.

## Naar een 9 (beoordeling 7,2)

**1. Helderheid (was 6).**

Gedaan:
- **Rekenfout hersteld.** De dividendcoëfficiënt 0,015 staat nu als 1,5 procentpunt per jaar, over tien jaar 0,15 log-punt. Daarnaast staat 0,38 log-punt minder rendement: het rendement draagt ruim twee keer zoveel.
- **Notatiewissel benoemd.** De Opzet zegt nu dat in [](#01-02-bachelier) kleine letters logs waren en hier niveaus zijn, en dat $r$ hier de discontovoet is.
- **Verwijzing standaardfout van 2%.** Die wijst nu naar [](#00-01-rendementen), in de Simulatie en in oefening 3.
- **"verderop in deze lecture"** is geschrapt.
- **Log-kalibratie benoemd.** Rekenkundige verwachtingen liggen een halve variantie hoger: $g \approx 2{,}3\%$, $r \approx 8{,}4\%$, $r - g$ 6,1 in plaats van 5,2, ware ratio ongeveer 17. De tekst zegt waarom de log-kalibratie blijft.
- **"twintig tot dertig jaar" vervangen** door de duration $(1+r)/(r-g) = 22$ jaar. De afleiding in één regel staat bij Gordon, het toy noemt alleen het getal.
- **"25%" vervangen** door de percentielen: −36% en +109% bij $T = 50$.
- **PVGO:** de algebraïsche tussenstap staat erbij.
- **Identiteit naar verwachtingen:** de zin die de identiteit in gerealiseerde rendementen vertaalt naar verwachtingen ("neem $\E_t$ aan beide kanten") staat in "Hoe het getoetst wordt".

Niet gedaan: niets.

**2. Opbouw (was 8).**

Gedaan:
- Het Overzicht geeft nu ook het antwoord: de data verwerpen de vaste discontovoet.
- Kernresultaat en Gordon openen met hun conclusie.
- Na de simulatie staat de overgang naar de replicatie: $g$ onzeker, nu de vraag of $r$ beweegt.
- De Campbell-Shiller-details ($\rho$, decompositie) staan nu in een dropdown-note.
- PVGO is ingebed als "waar komt $g$ vandaan", in plaats van "zijstap".

Niet gedaan:
- Samengevat blijft aan het eind van Theorie (STYLE §11.6, op instructie).
- PVGO blijft op zijn plek. Verplaatsen naar achter "Hoe het getoetst wordt" breekt de vaste `###`-volgorde van §11.7.

**3. Taal (was 7).**

Gedaan:
- De stapelzin in "Waar we zijn" is gesplitst.
- Het jargon barst/gat is vervangen door "een theorie van koersveranderingen, geen theorie van het koersniveau".
- "Wat rekenwerk geeft" is weg.
- "Neem dat verschil niet te serieus" is nu "Dat sterkere verband zegt weinig".
- De zin met de rekenfout is herschreven.

**4. Toy (was 8).**

Gedaan:
- Er staat nu een slotzin over wat de lezer weet: de prijs komt vooral uit de eindwaarde, en die hangt af van $r - g$.
- Het getal 22 jaar is onderbouwd. De formule ervoor staat in Theorie, zodat het toy bij één niet-afgeleide formule blijft.

**5. Code en figuren (was 8).**

Gedaan:
- `next(...)` is een gewone lus met `break` geworden.
- `b, a = np.polyfit` heet nu `slope, intercept`.
- Nederlandse variabelenamen zijn Engels geworden: `calibration`, `results`, `column`, `title`, `bubble`, `g_early`/`g_late`, `g_late_alt`.
- De simulatiefiguur trekt geen nieuwe steekproeven meer, maar hergebruikt `pd_hat_by_T[50]` uit de tabel. Er wordt verder nergens meer uit `rng` getrokken, dus de tabellen blijven gelijk.

Niet gedaan: niets.

**6. Replicatie (was 7).**

Gedaan:
- De verwachte afwijking is nu een verwachting: dividendcoëfficiënt niet significant, rendementscoëfficiënt negatief en significant, $R^2$ rond 0,10.
- De tabel heeft drie kolommen: Williams, verwacht, hier.
- Het oordeel is gesplitst: "**Geslaagd**" als replicatie, en daarna de verwerping van het model van Williams.
- De CAPE-getallen staan niet meer in proza. De tekst zegt nu "steilere helling, twee keer zo hoge $R^2$".

**7. Oefeningen (was 8).**

Gedaan:
- De instap legt nu uit dat de factor 1,331 wegvalt.
- Bij oefening 2 staat dat de 0,94 bij ROE = r betekenisloos is.

Niet gedaan: in de tabel van oefening 2 die 0,94 door NaN vervangen. Dat verandert de uitvoer.

**Zelf nagelezen met de rubriek.**
- Het Overzicht gaf het antwoord nog niet; toegevoegd.
- Het toy gebruikte met de duration een tweede niet-afgeleide formule; die afleiding staat nu bij Gordon.
- "Dat verschil" was dubbelzinnig; opgelost.

**Verificatie.**
- `prose_stats --check`: `6838 14.6 23 0 45 0 14 0 0 0 0 0 0 0 0 3`, met alleen FAIL op words (geen grens meer). `--where`: geen treffers.
- sync en execute: exit 0, geen stderr- of error-uitvoer.
- nb_outputs-diff tegen de stand na taak A: geen enkel getal veranderd. De diff is niet leeg, maar alle verschillen zijn bedoeld:
  - drie celkopregels, door de hernoemde variabelen (cellen 2, 9 en 12);
  - de simulatie-png (71404 → 71276 bytes), omdat de histogram nu dezelfde steekproeven toont als de tabel.

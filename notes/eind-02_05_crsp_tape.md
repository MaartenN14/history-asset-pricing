STATUS 02_05_crsp_tape F6 words=5131 prose=PASS open=3 cijfer=8,1 min=8

# Eindbeoordeling F6: 02_05_crsp_tape (De CRSP-tape: data als machine)

Eindbeoordelaar A, Deel II. Cijfer van record volgens `plannen/rubriek-didactiek.md`.

## Eindcijfer: 8,1

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 30% | 8 |
| 2 | Opbouw en rode draad | 20% | 8 |
| 3 | Taal | 15% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 8 |
| 5 | Code en figuren | 10% | 8 |
| 6 | Replicatie en empirie | 10% | 8 |
| 7 | Oefeningen | 5% | 9 |

8·0,30 + 8·0,20 + 8,5·0,15 + 8·0,10 + 8·0,10 + 8·0,10 + 9·0,05 = 8,125 → 8,1.
Laagste deelcijfer 8. Streefcijfer 8,5 niet gehaald.

## Feitelijke fouten

1. **Simulatie, openingsalinea.** "[...] en een database van overlevers een van
   veertien." De tabel geeft 0,1454, dus 14,5 procentpunt; afgerond is dat vijftien, en
   drie alinea's later staat zelf "14,5 procentpunt".
2. **Theorie → Wat het voorspelt, na de stelling.** "In woorden: de fout hangt alleen
   af van de overleefkans." Volgens [](#eq-crsp-tape-survivorship) is de fout
   $(x_0/T)(1/P - 1)$: ze hangt ook van $x_0/T$ af. Met $x_0 = 2$, $\sigma = 100\%$ en
   $T = 20$ is $P$ gelijk aan het kleine bedrijf van de tekst (0,345), maar de fout
   19% in plaats van 9,5%.
3. **Replicatie → Wat weging met een eeuw doet, tweede "Geslaagd".** "Binnen dat
   deciel doet equal-weighted het bovendien nog eens beter, door de bid-ask bias en de
   ontbrekende delisting returns." De lecture zegt elders dat dit niet vast te stellen
   is ("Hoe die met nog ontbrekende delisting returns omgaan, hebben we niet kunnen
   verifiëren"; "Of de huidige data die rendementen bevatten, is zonder CRSP niet vast
   te stellen"). Bovendien is volgens [](#eq-crsp-tape-ewvw) het verschil EW − VW binnen
   een deciel zelf een size-premie binnen dat deciel. De oorzaak is dus een bewering
   zonder grond.

Nagerekend en correct: toy (2,0; −1,0; −15,0; 0,0 → −3,50%; +0,25%; +3,13%;
cumulatief −14,17%, +0,98%, +12,88%; −4,55% en −45%); $0{,}0295 \times 0{,}588 = 1{,}7$;
$2\Phi(0{,}447) - 1 = 0{,}345$ en 9,5%; $e^1 = 2{,}7$; 0,012%; $\sqrt{\pi/2} = 1{,}25$;
$2\Phi(0{,}2) - 1 = 0{,}159$ en 5,3%; herbalanceringswinst 10%; bid-ask 3 pp per jaar;
$-N\Cov_{\text{cs}}$ klopt; 3,2% schrappingen per jaar; 5,5 pp (5,7 SD); 1,44% en 5,43
pp; deciel 5 onder 0,3 pp; 11,97% → 12,00%; 11,63% tegen 11,55%; 3,1 pp; factor 5,9 in
eindwaarde; 12,30% tegen 10,33%; 3,77 pp met $t = 5{,}2$; 5,21, 1,77%, 5,12%; 1,73 tegen
1,82 en 1,63 tegen 1,45; 18,6 tegen 10,3; 3,9 pp met SE 0,76; 0,31% en 0,57%; 10%,
54% en 39%; kleinste deciel EW eindigt 25 keer boven VW; aantal bedrijven piekt in juli
1997 (22.029); oefeningen (−20%, 0,368/0,345, 9,3/9,5%, 8,0 → 3,1 → 0,6 met SE 1,1).

## 1. Helderheid van de uitleg (8)

*Goed*
- **Het kernresultaat.** De stelling $h(\mu_a - D)$ krijgt meteen het toy-getal (15
  pp) en een Nasdaq-getal (1,7 pp per maand), met de bron.
- **Wat het voorspelt.** De survivorship-formule wordt met twee concrete bedrijven
  doorgerekend (9,5% tegen 0,012%) en de asymptotiek met een getal na een eeuw (5,3%).
- **Weging.** De herbalanceringswinst en de bid-ask bias krijgen elk een uitgerekend
  getal (10% en 3 pp per jaar).

*Aanmerkingen*
- **Overzicht.** "[...] wie ze weglaat, meet een te hoog gemiddelde, vooral bij kleine
  aandelen, en die fout krimpt niet met meer data." De theorie laat zien dat de
  survivorship-fout wél krimpt, als $\sigma\sqrt{\pi/2}/\sqrt{T}$; alleen de
  delisting-fout blijft staan. De Intuïtie ("De vertekening blijft staan, of krimpt
  hoogstens even snel als de ruis") en "Wat er brak" ("Anders dan die ruis verdwijnt ze
  niet met meer jaren") zeggen elk iets anders.
- **Wat het voorspelt.** "de fout hangt alleen af van de overleefkans" (feitelijke
  fout 2).
- **Weging, bid-ask.** "is het gemeten bruto rendement gemiddeld ongeveer
  $\E[R](1 + s^2)$." Geleend resultaat zonder de regel die het verklaart (Jensen:
  $\E[1/(1+\delta)] \approx 1 + s^2$).
- **Shumway-replicatie, alinea vóór de cel.** "Daaruit volgt $12\,h = 5{,}21/1{,}0177 =
  5{,}12\%$ per jaar, en die $h$ gaat met $D = -30\%$ opnieuw de stelling in." Vier
  getallen, twee frequenties en een terugrekening in drie zinnen; de lezer moet zelf
  zien dat $h$ uit dezelfde tabel komt als de toets.
- **Waar we zijn.** "de 9,0% per jaar van Fisher en Lorie. Over hun 35 jaar data had
  dat gemiddelde een standaardfout van bijna vier procentpunt." De 3,9 pp in L1 hoort
  bij het rekenkundige gemiddelde van 11,7%, de 9,0% is meetkundig (naad 7).

*Beter uitleggen*
- Eén zin in het Overzicht die de twee fouten scheidt: de delisting-fout blijft, de
  survivorship-fout krimpt, maar niet ten opzichte van de ruis.
- Bij de Shumway-toets: zeg vooraf dat $h$ uit de kolom met −100% wordt teruggerekend
  en dat de toets dus de lineariteit in $D$ controleert.

## 2. Opbouw en rode draad (8)

*Goed*
- **Intuïtie** voorspelt drie dingen (te hoog, vooral klein, meer data helpt weinig);
  theorie, simulatie en replicatie lossen de eerste twee in.
- De toy-getallen ($h = 1/5$, $D = -75\%$) keren terug in de stelling, en Shumways
  $D = -30\%$ verbindt simulatie en replicatie.
- **Simulatie** begint met de uitkomst (vijf en veertien procentpunt tegen één pp ruis).

*Aanmerkingen*
- Stofdichtheid: delisting, survivorship, look-ahead, backfill, fondsen, EW/VW,
  herbalanceringswinst en bid-ask bias in één lecture, plus twee replicaties. De kern
  (de stelling) moet concurreren met zes nevenmechanismen.
- **Replicatie, eerste blok.** "De weging is de meetbare schaduw van de
  delisting-fout: die fout zit in het kleinste deciel, en alleen equal-weighted geeft
  dat deciel gewicht." De replicatie meet de weging, niet de delisting-fout; de link
  met de kernstelling is een analogie, geen toets.
- De tegenspraak over "krimpt niet met meer data" (zie criterium 1) raakt de
  voorspelling van de Intuïtie.

*Beter uitleggen*
- Laat de eerste replicatie expliciet de *bovengrens* van de delisting-fout meten
  (alles wat EW − VW in deciel 1 is, kan hoogstens die fout zijn), of maak de
  Shumway-replicatie de hoofdreplicatie.

## 3. Taal (8,5)

*Goed*
- Natuurlijk Nederlands, korte zinnen (gemiddeld 14,5 woorden), geen u/je.
- Engelse vaktermen (*delisting return*, *look-ahead bias*) cursief met een uitleg
  tussen haakjes.

*Aanmerkingen*
- Twee namen voor één begrip: "schrapping"/"geschrapt" naast "delisting" ("de
  schrappingskans" en "de delisting-fout" voor dezelfde $h$ en hetzelfde mechanisme).
- **Intuïtie** tegenover de setup: "overlevers" hier, "overlevenden" in de setup
  (naad 8).

*Beter uitleggen*
- Kies "schrapping" in lopende tekst en reserveer *delisting return* voor het
  CRSP-veld.

## 4. Toy-voorbeeld (8)

*Goed*
- Vijf aandelen en vier perioden, alle stappen met de hand, tabel hand/code met
  identieke getallen.
- Eén zin wat de lezer nu weet: "de markt verloor 14% of won 13%, afhankelijk van één
  beslissing".

*Aanmerkingen*
- Drie mechanismen in één toy: het totaalrendement (dividend en split), de ontbrekende
  delisting return en survivorship. De rubriek vraagt één mechanisme.
- Twintig rendementen en drie gemiddelden over vier perioden: eerder vijftien dan vijf
  minuten.

*Beter uitleggen*
- Dividend en split kunnen naar de Opzet van de Theorie, waar $k_{t+1}$ toch wordt
  ingevoerd; het toy houdt dan alleen C.

## 5. Code en figuren (8)

*Goed*
- Elke cel heeft een zin ervoor en erna; de drie hulpfuncties van de simulatie worden
  vooraf één voor één beschreven.
- Beide figuren hebben een leeswijzer ("Let links op het kleine eind van de lijnen")
  en een bijschrift dat de vraag beantwoordt.

*Aanmerkingen*
- **Simulatie.** `twin = copy.deepcopy(rng)` en twee doorgangen van dezelfde generator
  om de laatste schrapping te vinden: correct en uitgelegd, maar een truc die de lezer
  moet ontcijferen.
- **Simulatie, `size_deciles`.** `np.where(in_sample, size, np.inf)` met ordinale
  rangen en `np.minimum(rank * 10 // ..., 9)` is compact en niet de wiskunde.
- **Simulatie, `last_delisting`.** `np.where(delisted, t, -1 if last is None else
  last)` in één regel.

*Beter uitleggen*
- Eén zin bij `size_deciles` dat aandelen buiten de steekproef rang oneindig krijgen
  en dus nooit in een deciel vallen.

## 6. Replicatie en empirie (8)

*Goed*
- Twee volledige replicatieblokken met een toetsbare verwachte afwijking (0,1 pp;
  0,2 pp).
- **Shumway.** Tabel origineel/hier/verschil, oordeel "Geslaagd" met verwijzing naar de
  aangekondigde 0,2 pp.
- De break-even-schrappingskans (0,57% per maand bij −55%) koppelt de stelling aan de
  size-premie.

*Aanmerkingen*
- **Wat weging met een eeuw doet.** Geen tabel origineel/hier: de 9,0% van Fisher en
  Lorie staat in L1 en komt in deze replicatie niet terug.
- Feitelijke fout 3: de oorzaak van EW > VW binnen deciel 1 wordt toegeschreven zonder
  grond.
- **Shumway, tweede rij.** $h$ wordt teruggerekend uit dezelfde tabel VII die de toets
  levert; de overeenkomst toetst alleen de lineariteit in $D$. Het blok zegt dat niet.
- Veel getallen in lopende tekst die ook in de tabel staan ("11,63% per jaar uit
  decielen tegen 11,55% [...] 12,30% tegen 10,33%").

*Beter uitleggen*
- Zeg bij de tweede Shumway-rij dat het een consistentietoets is, geen onafhankelijke.

## 7. Oefeningen (9)

*Goed*
- Instap op het toy, afleiding (drift en maandelijkse waarneming), uitbreiding van de
  replicatie: precies de drie soorten.
- Elke uitwerking eindigt met "Wat dit leert"; oefening 2 verklaart het teken van het
  verschil.

*Aanmerkingen*
- **Uitwerking ex-crsp-tape-2 (1).** "Bij positieve drift raken minder paden de
  drempel: de fout blijft positief, maar wordt kleiner." Wordt beweerd, niet getoond.

*Beter uitleggen*
- Geen.

## De drie verbeteringen met het meeste effect

1. De drie feitelijke fouten herstellen en de uitspraak over "krimpt niet met meer
   data" in Overzicht, Intuïtie en "Wat er brak" gelijktrekken (helderheid 8 → 8,5;
   opbouw 8 → 8,5).
2. De eerste replicatie expliciet als bovengrens van de delisting-fout formuleren en de
   Shumway-terugrekening vooraf aankondigen als lineariteitstoets (replicatie 8 → 9).
3. Het toy terugbrengen tot één mechanisme (aandeel C) en dividend en split naar de
   Opzet verplaatsen; dat maakt ook ruimte (toy 8 → 9).

## Navertelling in vijf zinnen

Vanaf 1960 bouwde CRSP de eerste database van alle NYSE-rendementen sinds 1926, en elke
keuze in die bouw heeft een voorspelbaar teken. Een ontbrekende delisting return maakt
het gemiddelde $h(\mu_a - D)$ te hoog, en die fout zit waar schrappingen vaak zijn: bij
kleine aandelen. Een steekproef van overlevers maakt uit een universum zonder premie een
size-premie van vijftien procentpunt, en look-ahead draait het teken om. Op echte data
verschuift de weging alleen het marktrendement van een eeuw met 3,1 procentpunt, bijna
geheel via het kleinste deciel, en de gepubliceerde correcties van Shumway volgen de
formule tot op 0,2 procentpunt. De size-premie is na 1981 weg, en een onopvallende
schrappingskans van een half procent per maand zou haar sinds 1963 volledig kunnen
verklaren. Dit komt overeen met het Overzicht, behalve dat het Overzicht de indruk wekt
dat geen van de fouten met meer data krimpt.

## Controle

STATUS 02_05_crsp_tape F6c words=5231 prose=PASS open=0 cijfer=8,5 min=8

Gecontroleerd tegen `rapport-02_05_crsp_tape.md` §F6-1 en de lecture zelf.

| punt | status | toelichting |
|---|---|---|
| Fout 1, "veertien" | opgelost | "een van vijftien" (Simulatie, eerste alinea) |
| Fout 2, "alleen af van de overleefkans" | opgelost | "de beginafstand per jaar, $z_0/T$, maal de kans op schrappen gedeeld door de kans op overleven" = $(z_0/T)(1-P)/P$, klopt |
| Fout 3, oorzaak EW > VW in deciel 1 | opgelost | nu een size-premie binnen het deciel volgens eq-ewvw; bid-ask en delisting "kunnen bijdragen", de data scheiden het niet |
| Verbetering 1, feiten en "krimpt niet met meer data" | opgelost | Overzicht, Intuïtie en "Wat er brak" zeggen nu hetzelfde: de delisting-fout blijft, die van overlevenden krimpt hoogstens even snel als de ruis |
| Verbetering 2, bovengrens en lineariteitstoets | deels | Shumway: nu vooraf gezegd dat de Nasdaq-rij onafhankelijk is en de tweede rij alleen de lineariteit in $r^{\text{s}}$ toetst. Weging: onder "Geslaagd" staat de bovengrens correct als voorwaarde ("Zijn de andere bronnen niet negatief [...] wat de weging via ontbrekende delisting returns in dit deciel kan doen"). In het replicatieblok ("Wat") staat ze zonder voorwaarde en te ruim: "Het weegverschil in het kleinste deciel is een bovengrens voor de fout door ontbrekende delisting returns". Het is hoogstens een bovengrens voor het *verschil* in die fout tussen EW en VW. Bij de weging staat nog geen tabel origineel/hier. |
| Verbetering 3, toy tot één mechanisme | opgelost | A en B zonder dividend en split, met dezelfde rendementen (nagerekend: A +10/0/0/+10, B 0/+10/0/−10); de voorbeelden van dividend (0% in plaats van −4,55%) en split (+10% in plaats van −45%) staan nu in de Opzet |
| Naad 3, $x$ | opgelost | $Z_t$, $z_0$ en $s_{i,t}$ |
| Naad 4, $D$ | opgelost | $r^{\text{s}}$ |
| Naad 5, $\tau$ | opgelost | de stoptijd heet nu $\theta$ |
| Naad 7, SE bij 9,0% | opgelost | "Het rekenkundige gemiddelde over dezelfde 35 jaar, 11,7%, had een standaardfout van 3,9 procentpunt" |
| Naad 8, overlevenden | opgelost | nergens meer "overlevers" |
| Aanmerking: bid-ask zonder reden | opgelost | Jensen-regel $\E[1/(1+\delta)] \approx 1 + s^2$ toegevoegd |

Geen verslechteringen en geen nieuwe feitelijke fouten. De code heeft nog steeds de
tweede doorgang met `copy.deepcopy(rng)`; `last_delisting` leest nu beter.

| nr | criterium | gewicht | was | nu |
|---|---|---|---|---|
| 1 | Helderheid | 30% | 8 | 8,5 |
| 2 | Opbouw | 20% | 8 | 8,5 |
| 3 | Taal | 15% | 8,5 | 8,5 |
| 4 | Toy-voorbeeld | 10% | 8 | 9 |
| 5 | Code en figuren | 10% | 8 | 8 |
| 6 | Replicatie | 10% | 8 | 8,5 |
| 7 | Oefeningen | 5% | 9 | 9 |

8,5·0,30 + 8,5·0,20 + 8,5·0,15 + 9·0,10 + 8·0,10 + 8,5·0,10 + 9·0,05 = 8,525 → **8,5**.
Laagste deelcijfer 8 (code). Voor een hoger cijfer blijven open: de bovengrens zonder
voorwaarde in het replicatieblok, een tabel origineel/hier bij de weging, en de
stofdichtheid (zes nevenmechanismen naast de kernstelling).

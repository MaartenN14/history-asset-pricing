# Rapport L1 00_01_rendementen (taak 0, A, B; niet gecommit, niet gebouwd)

**1. Meting (prose_stats --check)**
- Vóór: `words 5767 | sent_mean 18.1 | p90 31 | gt40 11 | para 54 | dash 48 | semicol 26 | deel 6 | u 33 | stopw 14 | calque 5 | engquote 13` → FAIL op 12 metrieken.
- Ná: `words 5886 | sent_mean 13.0 | p90 21 | gt40 0 | para 37 | dash 0 | semicol 9 | motief/L/deel/u/je/taboo/stopw/calque/engquote 0` → alleen `words` FAIL.
- Reden voor words: het plan voegt ongeveer 700 woorden toe (routekaart, Samengevat, lees-zin bij elke genummerde vergelijking, zinnen rond elke cel, oordeeltabel, instapoefening). Verplaatsen naar een dropdown verlaagt de telling niet, en schrappen mag niet. De resterende tekst is al met ongeveer 600 woorden ingekort.
- `--where`: geen treffers.

**2. Top-5 uit taak 0, en wat ermee gebeurde**
1. Aanspreekvorm "u" 33× (Intuïtie, Overzicht, Theorie, Wat er brak; §3.2). Nu 0: "we", onpersoonlijke vorm, "een onderzoeker die …".
2. Stapelzinnen: 48 gedachtestreepjes, 26 puntkomma's, 11 zinnen >40 woorden, alinea's van gemiddeld 54 woorden (overal; §3.1). Nu 0 / 9 / 0 / 37.
3. Overzicht: vijf alinea's geschiedenis, "het 2%-motief", "de epistemische status", en de imports-cel onderaan (§3.3, §3.13). Nu vraag en antwoord, een lijst van zes punten en één alinea geschiedenis, plus drie zinnen onder de naam "theorie of feit". De imports-cel staat aan het begin van het toy-voorbeeld.
4. Projectjargon en vooruitverwijzingen: "Deel I/II/III/IV/V" en "Delen II tot VI" (§3.3). Vervangen door omschrijvingen. Er blijven twee vooruitverwijzingen over: [](#01-02-bachelier) bij de variance ratio, en "latere lectures" in de uitwerking van oefening 2.
5. Didactiek (§3.6–3.10). Theorie had zeven subsecties, geen routekaart en geen Samengevat, en twee lange bewijzen stonden open. Het toy-voorbeeld had geen opzet-tabel en geen tabel hand/code. Het replicatieblok telde ongeveer 330 woorden, zonder tabel origineel/hier en zonder oordeel. Oefening 1 was geen instap. Alles is aangepakt:
   - Theorie heeft nu zes subsecties, een routekaart en een Samengevat-blok.
   - Het toy-voorbeeld heeft een opzet-tabel, een recept en vijf stappen, en eindigt met een tabel hand/code.
   - Het replicatieblok telt ongeveer 170 woorden en wordt gevolgd door een tabel origineel/hier/verschil en een oordeel dat begint met "Geslaagd".
   - Oefening `ex-rendementen-instap` is nieuw. Elke uitwerking eindigt met "Wat dit leert:".

De standaardfout van 2% wordt letterlijk benoemd en uitgelegd in "Het kernresultaat: de standaardfout van 2%" ($20/\sqrt{100}=2$, met terugverwijzing naar de 13 procentpunt uit het toy-voorbeeld). De naam komt ook terug in het Overzicht, de routekaart, Samengevat en de Simulatie. "Risico of vergissing" en "theorie of feit" komen alleen onder die namen voor.

**3. Verplaatst (niets geschrapt)**
- Bewijzen van de stellingen over variance drag en Merton gaan naar `{prf:proof}` met `:class: dropdown`. In de hoofdtekst staat nu een lees-zin plus het bewijsidee.
- "Autocorrelatie" en "Dikke staarten" zijn samengevoegd tot één subsectie ("Wanneer de aannames niet gelden").
- Details uit het replicatieblok gaan naar het commentaar van de codecel: de reekscodes, `Mkt = Mkt-RF + RF`, 414 in plaats van 420 maanden, en bid-ask bounce met de rebalanceringspremie.
- De uitleg van drift en kwadratische variatie gaat van het Overzicht naar de lijst en de Merton-sectie.
- De Fisher-Lorie-cel is gesplitst: data laden, en daarna functie plus tabel.
- Twee onduidelijke zinnen heb ik geïnterpreteerd:
  - "in de negentig jaar … drie keer verdubbeld" is nu "sinds Fisher en Lorie is de steekproef bijna drie keer zo lang".
  - "en u hebt er drie" is nu "een crisis duurt er hooguit een paar".

**4. nb_outputs-diff (HEAD tegen eind; na-A en eind zijn identiek)**
- Toy-cel: de kolom `waarde` is nu `met de hand` en `code`. De getallen zijn gelijk. In de tekst staat de handwaarde voor de standaardfout nu als 0,132288 (was 0,132289, een afrondingsfout; de code gaf al 0.132288).
- Fisher-Lorie: er is een cel zonder output bijgekomen (door de splitsing). De tabel is identiek. De nieuwe tabel origineel/hier/verschil geeft VW 0.0946 (+0.0046) en EW 0.1291 (+0.0391).
- Nieuwe instap-cel: 0.016667 / -0.012660 / 0.026944 / 0.029326. Die cel gebruikt `rng` niet.
- Verder verschuiven alleen de celnummers. Alle overige getallen zijn identiek, ook de simulatie en de uitkomsten van oefening 1 die van `rng` afhangen.

**5. Afvinklijst: wat niet voldoet**
- words 5886 > 5500 (reden onder punt 1).
- Het Overzicht heeft na de alinea geschiedenis nog een korte alinea "theorie of feit".
- De volgorde in Theorie is niet Opzet → Kern → Voorspelt → Getoetst. Dit is een meetlecture: Opzet, drag, wortel-t, kernresultaat, Merton, aannames.
- Het eerste element van "Wat er brak" heet nog steeds "Wat de meetlat oplevert".
- De drie extra datachecks onder Replicatie staan nog in de hoofdtekst: maand/dag, clustering en variance ratios, en Shiller 150 jaar.
- Overige: ok.

**8. Open punten**
- In twee presentatietabellen staan Engelse kolomnamen uit `hap`: `nobs`, `mean_ann`, … uit `hap.summary_stats`, en `vr`, `z2`, `pvalue` uit `hap.variance_ratio`. Hernoemen verandert de uitvoer; oplossen in `hap` of expliciet toestaan.
- STYLE §1, §2, §5 en §10 noemen nog "2%-motief", "motief 1/2/3" en de imports-cel in het Overzicht. §11 gaat voor, maar de tekst is tegenstrijdig.
- Er is geen `jupyter book build` gedraaid (afspraak). Nieuwe labels en cross-refs zijn dus niet door MyST gecontroleerd.

**Execute-log (laatste regels)**
```
[jupytext] Executing notebook with kernel python3
[jupytext] Warning: Notebook is not trusted
[jupytext] Writing lectures/00_01_rendementen.ipynb (destination file replaced [use --update to preserve cell outputs and ids])
```
Exit 0, geen stderr- of error-outputs in het notebook.

## Lezersronde

Van de 37 vindplaatsen zijn er 37 opgelost en 0 afgewezen; één daarvan maar gedeeltelijk (H7, volatiliteit).

**Per H-regel (opgelost/afgewezen)**
- H1 3/0: handelende belegger met richting in "Opzet", "Wortel-t" en "Autocorrelatie" ("lineair" is weg).
- H2 9/0: uitleg toegevoegd bij $\sigma$ tegenover $\sigma_\ell$, $m$ en $x$, $W_t$, kurtosis (de alinea is verhuisd, zie hieronder), staartindex, "theorie of feit", equity premium puzzle en factor zoo, alpha, en Chicago/Yale.
- H3 2/0: de convergentie bij de drag en $T^*$ bij de standaardfout staan nu als "Een gevolg" buiten de stelling. Labels en bewijs zijn intact.
- H4 2/0: VR ≈ 1,18, dus een standaardfout van 2,0 naar 2,2 procentpunt; bij Merton $\sqrt{2/100}=14\%$ tegen 0,9%.
- H5 2/0: normaliteit genoemd bij $\chi^2$, en i.i.d. bij de wet van de grote aantallen.
- H6 0/0.
- H7 5/0:
  - alinea "Over de namen" (meetkundig gemiddelde, samengesteld, $\mu_g$, $\nu$, drift);
  - de drift van 8% heet een totaalrendement, geen premie;
  - excess kurtosis gedefinieerd;
  - "kijkrooster", "onrust" en "tweede moment" vervangen.
  - Gedeeltelijk: "spreiding" (muntworp) en "ruis" (signaal/ruis) blijven als gewone woorden, niet als apart begrip.
- H8 3/0: de note, "het vroege waarschuwing" en "het patroon" verwijzen nu naar iets expliciets.
- H9 5/0: een conclusiezin na de toy-tabel en vóór de Fisher-Lorie-figuur, en een vraag als eerste zin van de drag-sectie en de wortel-t-sectie.
- H10 4/0: voorbeelden bij variance ratio, factor, ARCH/GARCH/RV/VIX en bid-ask bounce.
- H11 1/0: de 23% uit het toy-voorbeeld in de simulatie genoemd.
- H12 1/0: de Merton-sectie verwijst terug naar de windmeter en de eerste voorspelling.

**Navertel-afwijkingen**
- Overzicht.
  - De lezer wist niet welke vraag "theorie of feit" is.
  - Bedoeld: de vaste vraag van de reeks, waarop deze lecture een uitzondering is omdat ze alleen wiskunde bevat.
  - Veranderd: de vraag staat er nu voluit, met "Deze lecture is daarop een uitzondering".
- Replicatie.
  - De lezer twijfelde tussen "vier tot vijf procentpunt" en "3,9".
  - Bedoeld: 3,9 voor value-weighted en 5,5 voor equal-weighted.
  - Veranderd: beide getallen staan er nu expliciet.
- Spoorverlies 2 (dikke staarten al in Merton): de alinea "Bij dikke staarten … benaderingen" is naar de subsectie Dikke staarten verhuisd.
- Spoorverlies 3 (autocorrelatie te klein of toch zichtbaar): de VR-berekening laat 2,0 → 2,2 procentpunt zien, en de maand/dag-sectie noemt het verschil "van dezelfde orde: klein, maar zichtbaar".

**Verificatie**
- prose_stats --check: `words 6382 | sent_mean 13.3 | p90 21 | gt40 0 | para 40 | dash 0 | semicol 12 | rest 0`.
  - FAIL alleen op words. Reden: de lezersronde vroeg om uitleg ter plekke (H2, H4, H7, H10), ongeveer 500 woorden.
- --where: geen treffers.
- sync en execute (HAP_OFFLINE=1): exit 0; laatste regel `Writing lectures/00_01_rendementen.ipynb`.
- nb_outputs-diff tegen de stand na taak A: leeg.

## Lezersronde 2

Van de 22 vindplaatsen zijn er 22 opgelost en 0 afgewezen.

**Per H-regel (opgelost/afgewezen)**
- H1 1/0: de bewijsschets over covarianties is uit de waarom-alinea gehaald en staat nu vóór en na [](#eq-rendementen-vr).
- H2 5/0: uitleg toegevoegd bij $\kappa$, Chicago/Yale (de scholen van Fama en Shiller), `z2`/`pvalue`, CRSP en delistings.
- H3 1/0: de stelling van Merton bevat alleen nog de formules. Eronder staat één bewering in één zin.
- H5 2/0: de drag-stelling zegt nu "onafhankelijk en gelijk verdeeld". Bij de 3,9 staat erbij dat hij i.i.d. aanneemt; met autocorrelatie 0,09 is hij ongeveer 9% groter.
- H7 5/0:
  - Overzicht: "verwacht rendement" in plaats van "drift"; bij de simulatie staat uitgelegd dat het gemiddelde daar de drift is.
  - "Samengesteld" betekent alleen nog meetkundig; bij het logrendement is die alias weg.
  - 11,6% heet overal het rekenkundig gemiddelde.
  - $f$ is $n$ geworden, zoals bij Merton.
  - "Spreiding" is vervangen door standaardfout of volatiliteit.
  - Kolom- en aslabels in de code ("SD(gemiddelde)", "Geschatte drift") zijn ongewijzigd gelaten om de uitvoer gelijk te houden; de tekst legt ze uit.
- H8 2/0: "hele literatuur" en "asymmetrie" verwijzen nu naar iets expliciets.
- H9 2/0: een conclusiezin na de simulatiefiguur, en de sectie Honderdvijftig jaar opent met het antwoord.
- H10 4/0: voorbeelden van $x$ en $m$, bèta's en mean-variance uitgelegd, en de rebalanceringspremie benoemd.

**Waar de lezer het spoor kwijtraakte**
- Factor zeven tegenover tien: de intuïtie zegt nu "bij 20% volatiliteit een factor zeven", gelijk aan de theorie. Dat is een inhoudelijke correctie; 1,02^100 = 7,2.
- "Slimmere schatter": vervangen door de conclusie over de drift.

**Navertel-afwijking Replicatie**
- De lezer begreep dat de 9,0% van Fisher en Lorie over gelijke bedragen gaat, en dus bij de equal-weighted reeks hoort. Daardoor snapte hij "Geslaagd" voor de value-weighted reeks niet.
- Bedoeld: buy-and-hold met gelijke bedragen zonder herbalanceren gaat door de winnaars op een value-weighted markt lijken. Value-weighted is dus de replicatie; equal-weighted controleert alleen het teken.
- Veranderd: er staat nu een alinea die dat uitlegt, direct vóór de tabel origineel/hier.

**Verificatie**
- prose_stats --check: `words 6641 | sent_mean 13.6 | p90 22 | gt40 0 | para 42 | dash 0 | semicol 13 | rest 0`.
  - FAIL alleen op words. Reden: er is uitleg ter plekke toegevoegd voor H2, H7 en H10.
- --where: geen treffers.
- sync en execute (HAP_OFFLINE=1): exit 0.
- nb_outputs-diff tegen de stand na taak A: leeg.

## Naar een 9

Uitgangspunt: `notes/rating-00_01_rendementen.md` (7,4). Alle aanmerkingen en punten onder "Beter uitleggen" zijn doorgevoerd, op de uitzonderingen hieronder na.

**1. Helderheid**
- Factor zeven uitgerekend ($0{,}20^2/2 = 2$ pp; $1{,}02^{100} \approx 7{,}2$), in Intuïtie en bij de drag.
- $\sigma$ tegenover $\sigma_\ell$ vastgelegd:
  - in Opzet: $\sigma$ is simpel, $\sigma_\ell$ is log;
  - bij de stelling van Merton: daar is $\sigma$ de logvolatiliteit, en waarom de index wegvalt.
- Sharpe-ratio gedefinieerd, met 0,04 per dag en 0,6 per jaar.
- In de warning over log en simpel is "honderden procenten" vervangen door een factor $e^{0{,}0047 \cdot 1200} \approx 280$.
- $VR(T)$: gezegd dat $T$, $\sigma$ en $VR$ op één frequentie staan. Getal voor een maandreeks van een eeuw.
- $\sigma^4(\kappa-1)/N$ in één regel afgeleid; $\kappa$ als formule gedefinieerd.
- Interval rond de replicatie:
  - staat nu rond het rekenkundig gemiddelde (11,7%, dus 4% tot 19%);
  - het meetkundige 9,0% is even onzeker (ongeveer ±8 pp).
  - Dit corrigeert de inhoud: de oude tekst zei 2% tot 17% rond het meetkundige getal.
- Overzicht: "op twee procentpunt na bekend" is nu "standaardfout van twee procentpunt, 95%-interval ongeveer ±4". Idem in de lijst.
- Kernresultaat: de naam "de standaardfout van 2%" wordt uitgelegd als twee procentpunt; het interval als twee standaardfouten.

**2. Opbouw**
- De empirische subsecties (maand/dag, clustering) en "Wanneer de aannames niet gelden" openen met hun conclusie.
- Intuïtie doet nu drie voorspellingen; de derde is dat het gemiddelde na een eeuw onzeker blijft.
- De toy-getallen worden gebruikt, niet alleen genoemd:
  - 23% toy geeft een standaardfout van 2,3 pp tegen 2,0 (Simulatie);
  - de volatiliteit van de VW-replicatie is 22,9%, met drag van ongeveer $0{,}229^2/2$ (Replicatie).
- Label `(sec-rendementen-standaardfout)=` staat voor de kernsubsectie. Elke vermelding van "de standaardfout van 2%" buiten die subsectie linkt ernaar: Overzicht, routekaart, Aannames, Samengevat, Simulatie.
- **Niet gedaan:** Samengevat verplaatsen naar het eind van de lecture (op aanwijzing; STYLE §11.6).

**3. Taal**
- CRSP uit de zin gehaald en een eigen zin gegeven.
- "Als meting was de eerste … meting" herschreven.
- Emmerbeeld vervangen door "De data zijn alleen te dun om tussen hen te kiezen".
- "Verliest een alpha" vervangen door "vindt een alpha die er niet is, of mist er een".
- Windbeeld klopt nu: de totale hoeveelheid lucht hoort bij de totale koersverandering.
- Eén naam per begrip:
  - "lag" in plaats van "vertraging" (zoals in de tabel);
  - "meetkundig gemiddelde" in de tekst; de kolom "samengesteld (meetk.)" wordt één keer uitgelegd;
  - "spreiding" is standaarddeviatie of volatiliteit geworden.

**4. Toy**
- Het mechanisme is expliciet één ongelijkheid (stap 1 tot 4).
- Stap 5 heet nu "een voorproef: de standaardfout". Er staat een zin bij waarom de drag door $T$ deelt en de standaardfout door $T-1$.
- **Niet gedaan:** de standaardfout uit het toy-voorbeeld halen. De rijen zitten in de tabel hand/code, en weglaten verandert de uitvoer. De formule $s/\sqrt T$ is daarom gemarkeerd als geleend uit [](#00-00-setup) en bewezen in [](#thm-rendementen-se).

**5. Code**
- Commentaarregel bij de `reshape` in de simulatie.
- De kolommen van `hap.summary_stats` en van `vr`/`z2`/`pvalue` staan in één zin uitgelegd.
- In oefening 3 heet `rows` nu `by_horizon`, met commentaar dat $\kappa - 1$ gelijk is aan excess + 2.
- De VR-tabel heeft nu een eigen leeszin.
- Uitvoer ongewijzigd: in elke gewijzigde cel is de eerste regel gelijk gebleven.

**6. Replicatie**
- Bij 6,9% staat nu "repliceren we niet".
- Het interval is gecorrigeerd (zie 1).
- Het oordeel verwijst nu letterlijk naar beide verwachtingen uit het blok (≤ 1 pp; EW hoger).
- In de alinea's met getallen staan er hooguit drie per alinea. De halve variantie bij Shiller verwijst naar de tabel.

**7. Oefeningen**
- Oefening 1(2) vult nu [](#eq-rendementen-jaren) in (400 en 225 jaar).
- Oefening 3 zegt dat de rij voor 252 dagen een ruwe schatting is en dat de conclusie rust op 1 en 5 dagen.

**Verificatie**
- prose_stats --check: `words 7160 | sent_mean 13.7 | p90 22 | gt40 0 | para 43 | dash 0 | semicol 11 | rest 0`. Words heeft geen grens meer.
- --where: geen treffers.
- sync en execute (HAP_OFFLINE=1): exit 0.
- nb_outputs-diff tegen de stand na taak A: leeg.

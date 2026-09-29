STATUS 04_20_voorspelbaarheid F4T words=5620 prose=PASS open=0 cijfer=- min=-

# Rapport 04_20_voorspelbaarheid (L20)

**Kern.** Vraag: zijn rendementen op de aandelenmarkt voorspelbaar, en kan een belegger
er iets mee? Antwoord: ja, want de dividend-prijsratio beweegt vrijwel alleen door
verwachte rendementen (dividendgroei is niet voorspelbaar), maar de voorspelling is
statistisch zwak en verslaat buiten de steekproef het gemiddelde zelden zolang de
helling geschat moet worden.

## F0

`prose_stats` (voor): words 5507, sent_mean 21,0, p90 37, >40 18, para_mean 62,
semicol 40, motief 3, je_form 9, calque 29, engquote 16, colon_mid 12,0, para_one 21,
telegram 1, tmpl 8 (8x "Waarom zou"). FAIL op 13 drempels; words PASS.

Vijf grootste problemen:
1. Taal overal: 40 puntkomma's, 18 zinnen boven 40 woorden, 16 Engelse citaten in de
   lopende tekst (r. 102, 450, 549, 815), calques "Cochrane's" en "de nul" (29x), "je"
   (9x), "Neem nu de data" (r. 98), "Twee dingen staan er ook" (r. 949).
2. Notatie en naad (Theorie, r. 225-307): $r_{t+1}$ als logrendement in plaats van
   $\ell$ uit de setup, en de Campbell-Shiller-afleiding herhaalt
   [](#eq-shiller-excess-volatility-cs) en de decompositie uit 03_15.
3. Structuur: Overzicht zonder vraag/antwoord en lijst, imports-cel in Overzicht (r. 76),
   geen routekaart en geen Samengevat in Theorie, acht keer "Waarom zou dit waar zijn",
   "Motief 1", "2%-motief", "Epistemisch", "lecture" (r. 68-72, 600, 813).
4. Toy (r. 125-221): twee mechanismen (identiteit én lange-horizonhelling), geen
   opzet-tabel, geen tabel hand/code.
5. Replicatie: blok ~330 woorden (> 250), getallenbrij in proza (r. 946-959, 1016-1035,
   1103-1112, 1187-1197), geen oordeel Geslaagd/Gedeeltelijk; oefening 1 is geen instap;
   "Wat we al weten" verwijst naar vier colleges.

Schraplijst (schraptoets §11.11; eis 2 met grep: extern aangehaald zijn eq-…-cs-rendement,
-cs-pv (05_27), -stambaugh (05_28), -lr (05_33), -oos en -ct (06_35)):

| passage | woorden | eis die ze niet haalt | actie |
|---|---|---|---|
| Theorie, bewijs CS-identiteit (dropdown) + deel "Drie opmerkingen" | ~300 | 1 (afleiding staat in 03_15); labels blijven | naar verwijzing 03_15 |
| Theorie, afleiding variantiedecompositie | ~130 | 1 (herhaling 03_15) | ingekort, vergelijkingen blijven |
| Standaardfouten: Hansen-Hodrick-alinea, Valkanov-alinea | ~150 | 1 | tot één zin elk |
| Toy, lange horizon (b_r^(k)) | ~150 | tweede mechanisme | naar Theorie "Wat het voorspelt" |
| Theorie, Campbell-Thompson-restricties als eigen alinea | ~70 | 1 | samengevoegd |
| Replicatieblok | ~330 → 240 | vorm §11.7 | getallen naar tabellen/cellen |
| Replicatieproza met getallen | ~150 | §11.5 | tabel + oordeel |
| Wat er brak, "Risico of vergissing" | ~210 → 120 | lengte §5 taak B | ingekort |
| Overzicht, tweede geschiedenisalinea | ~100 | §11.7 (één alinea) | samengevoegd |

Toevoegingen: routekaart (~70), Samengevat (~110), lijst in Overzicht (~80), instap-oefening
(~150), oordeelzinnen (~60). Verwachte lengte: 5507 − ~1300 + ~470 ≈ 4.700–5.100 woorden.
Geen splitsing nodig.

## F1

Eindmeting: words 5551, sent_mean 16,6, p90 25, >40 0, para_mean 51, semicol 3, calque 0,
engquote 2, colon_mid 0,2, para_one 11, tmpl 1: PASS. rewrap 1256 -> 1343 regels; sync en
nbconvert offline zonder fouten.

Geschrapt of verplaatst:
- Bewijs CS-identiteit (dropdown) en "drie opmerkingen": afleiding staat in 03_15; nu
  verwijzing naar eq-shiller-excess-volatility-cs. Propositie en labels blijven.
- Afleiding decompositie ingekort tot verwijzing naar eq-shiller-excess-volatility-decompositie.
- Lange-horizonhelling uit het toy naar Theorie "Wat het voorspelt" (één mechanisme in toy).
- Hansen-Hodrick- en Valkanov-alinea tot één zin elk; Stambaugh-p-waarden geschrapt (nevenfeit).
- Replicatieblok van ~330 naar ~200 woorden; FF-helling 15,35 en GW-getallen alleen in tabellen.
- Tweede geschiedenisalinea in het Overzicht samengevoegd; "Risico of vergissing" ingekort.
Toegevoegd: vraag/antwoord + lijst, routekaart, Samengevat, opzet-tabel en tabel hand/code in
het toy, tabel Cochrane/nulhypothese in Theorie, instap-oefening (nieuw ex-…-1).

Notatie (naad): $\ell$ voor het logrendement en "vanaf hier zijn kleine letters logs" zoals
03_15; $dp_t = d_t - p_t$ blijft (tekenconventie Cochrane, expliciet gekoppeld aan
$pd_t = -dp_t$ van 03_15), want $pd$ zou het teken van elk aangehaald getal omdraaien.

nb_outputs-diff (geen aangehaald getal veranderd):
- cel 2 (toy): print-regels vervangen door tabel "met de hand / code", zelfde waarden;
  b_r^(k) (0,4435; 0,7690) en 1,0246 zijn nu handberekening in Theorie.
- cel 3: kolom "hier (simulatie)", index "kans op …"; waarden gelijk.
- figuren: alleen PNG-grootte (legenda/assen "nulhypothese", "buiten de steekproef").
- nieuwe cel 17 (oefening 1); cellen 17-18 schuiven naar 18-19; print "onder de nul" ->
  "onder de nulhypothese".
nb_numbers: 34 meldingen (was 30); nieuw zijn alleen getoonde handberekeningen (0,093;
0,1536; 0,232; 0,4435; 0,768; 0,7690; 1,0246).

Afvinklijst §11.9, niet voldaan:
- Simulatie heeft twee `###` (nulhypothese en echte voorspelbaarheid) onder één vraag;
  de tweede draagt "Waar het breekt", dus niet naar oefening verplaatst.
- Oplossingscel oefening 3 heeft geen zin ervoor; imports-cel staat zonder aankondiging.
- overige: ok.

Labels: geen verdwenen. Oefeningen hernummerd (oud 1 -> ex-voorspelbaarheid-2, oud 2 -> -3,
nieuw -1); nergens aangehaald (grep).

Open punten voor de feitencontroleur:
1. Docstrings Engels gelaten (STYLE §3, "Wat niet meetelt" 3), tegen de prompt in
   ("Nederlandse docstrings"); besluit orchestrator.
2. Getallen uit bronnen zonder cel: Campbell-Thompson NBER 11468 (S = 0,108; R² 0,25%),
   Ferreira-Santa-Clara Sharpe-winst 0,3, Cochrane "30 tot 40%" slechte OOS in simulaties,
   Fama-French "minder dan 5% / meer dan 25%", Cochrane SE 0,047 en 0,44.
3. Keuze $dp$ in plaats van $pd$ (zie Notatie) ter bevestiging bij de naadcontrole.

## F4

Feiten (4 open, alle opgelost): 31 Theorie/Wat het voorspelt, "minder dan 5%" wordt "maar
een klein deel"; 32 Simulatie/echte voorspelbaarheid, "30 tot 40%" geschrapt; 33 Theorie/
buiten de steekproef, 0,25% niet meer aan e/p toegeschreven maar als rekensom; 34
Replicatie/Goyal-Welch, "twee jaar later" geschrapt, negatief teken steunt op cel 13.
Lezer 1-15 (alle gedaan): 1 Theorie (dubbele "is"); 2 Wat er brak (komma); 3 buiten de
steekproef, $\gamma$ zonder getal (valt uit de verhouding, getal zonder bron niet opgenomen);
4 Theorie en Replicatie/Cochrane ("vrijwel volledig uit"); 5 $S$ krijgt direct "rond de 0,1
per maand"; 6 Replicatie, FF/Cochrane/GW openen met de bewering; 7 CT "verslaat het
gemiddelde niet" (cel 14: alle vier negatief); 8 Simulatie/nulhypothese; 9 Toy; 10 Wat er
brak/Risico of vergissing; 11 Replicatie/De data; 12 Intuïtie (definitie rendement); 13
Ferreira-Santa-Clara ("te voorspellen grootheid"); 14 Intuïtie ("die hele periode"); 15 =
feit 34. Spoor 3 (overgang naar mean-variance) opgelost in de bestaande zin.
Navertel-toets: geen sectie week af (lezer: overal "klopt"). Geen code gewijzigd, dus geen
nbconvert; nb_numbers: geen nieuwe meldingen (alleen regelverschuiving en de CT-zin).

## R9-1 (F6b, ronde 9+)

- **Fout 1 (wolk schuin, :675)** gedaan: de gedeelde dividendschok via $\varepsilon^r = \varepsilon^d - \rho\varepsilon^{dp}$ legt de wolk schuin, en een lage $\hat\phi$ schuift hem alleen naar rechts (Stambaugh-bias).
- **Fout 2 (60 tot 80 jaar, :1180)** gedaan: de echte toets schat vanaf de jaren 1870 (ongeveer 150 jaar), en de kans op verlies is dan een kwart (cel 6, 0,262). De pensioenzin is aangepast.
- **Fout 3 (:1183)** gedaan: "Dat de discontovoet beweegt, is dus uitstekend gemeten, maar de helling ... niet."
- **Fout 4 (bijschrift hond)** gedaan: "vat $\hat b_r$ en $\hat\phi$ samen in één getal" in plaats van "telt precies die hoek".
- **Fout 5 (Sharpe 0,3)** geschrapt, want er is geen cel of paginaverwijzing.
- **Helderheid**: VAR benoemd bij de eerste keer (vectorautoregressie); de reden waarom Hansen-Hodrick te vaak verwerpt (geschatte autocovarianties te klein) en waarom 1B het juiste niveau heeft; de correctie van Goyal-Welch in één zin uitgelegd, en de proza zegt nu expliciet dat de 15 van 16 over de gecorrigeerde waarde gaat.
- **Opbouw ($R^2(1)$ 4% tegen 5%)**: in de simulatiezin opgelost ("5%, iets meer dan de 4% die intuïtie en theorie met ronde getallen aannamen"). Intuïtie en theorie zijn niet op 5% gezet, omdat 15,7% en 23,7% dan nieuwe getallen zonder cel zouden worden (kaart §6).
- **Taal**: één naam (dividend-prijsratio; "dividendopbrengst" en "dividendrendement" weg); de schrijfwijze is overal "logrendement", en overrendementen heten "overrendement in logs". Hardop-zinnen 1 (γ valt nu weg in de factor), 2 ("heeft geen last van ... waardoor de regressie zo vaak verloor") en 3 ("ergens vandaan komen ... één bron aan") herschreven.
- **Toy**: stap 1 zegt nu dat het recept zonder $\kappa$ afwijkingen geeft, en dat alle drie de rendementen negatief zijn omdat $dp$ elk jaar stijgt (de markt werd goedkoper).
- **Code**: in `oos_r2_sim` is de lambda vervangen door `mean_up_to_t` met docstring en commentaar ("OLS slope on data up to t"); de berekening is dezelfde. Tabelkoppen: "OOS R2 1965-2005, gecorrigeerd", "Goyal-Welch, gecorrigeerd" en "som van de delen, maand/jaar" (was SOP). Vóór de import-cel staat nu een zin. Met nbconvert offline uitgevoerd, en de uitvoer verschilt alleen in de labels.
- **Replicatie**: "Geslaagd" plus een verwijzing naar de vooraf gestelde verwachting bij Fama-French, Cochrane, Goyal-Welch en de som van de delen. Getallen die al in de tabel staan, zijn uit de proza gehaald (0,16; −4,2%; 1,32%), en de alinea's over Goyal-Welch en de som van de delen zijn elk in tweeën gesplitst.
- Afgewezen: niets.
- Woorden: 5.853 (prose_stats PASS); nb_numbers: geen nieuwe meldingen; rewrap en jupytext --sync gedraaid.

STATUS 04_24_microstructuur F4T words=5667 prose=PASS open=1 cijfer=- min=-

Kern: hoe komt private informatie via de handel in de prijs, en wordt de kost daarvan in
rendementen beloond? Een market maker tegenover beter geïnformeerde handelaren rekent een
spread (Glosten-Milgrom) en een prijsimpact (Kyle), de prijs neemt de informatie geleidelijk
op, en illiquiditeit gaat samen met lage gelijktijdige en hogere verwachte rendementen, al is
de premie op liquiditeitsrisico na publicatie niet meer zichtbaar.

## F0

`words=6235 sent_mean=21.6 sent_p90=35 sent_gt40=19 para_mean=63 semicol=56 motief=3
je_form=5 calque=16 engquote=12 colon_mid=9.0 para_one=15 tmpl=7` (FAIL op 13 drempels).

Vijf grootste problemen:

1. Lengte en stofdichtheid (Theorie r.243–700, ca. 2.900 woorden, negen `###`):
   nevenresultaten als Hasbrouck (r.543), de werkversiegetallen van Amihud (r.594–600,
   r.614–627) en de PS-alpha's per model (r.654–661).
2. Drie simulaties (r.702–984): Kyle over vele rondes is een numerieke oplossing en hoort
   in Theorie; de Glosten-Milgrom-sessie is een tweede simulatie; alleen de Roll-schatter
   stelt een steekproefvraag.
3. Getallenbrij in lopende tekst (r.614–627, r.654–661, r.681–686, r.1257–1264); de
   replicatie heeft geen tabel origineel/hier en geen oordeel "Geslaagd/Gedeeltelijk";
   het replicatieblok telt ca. 330 woorden.
4. Taal: 56 puntkomma's, 19 zinnen boven 40 woorden, 16 calques (Kyle's, Amihud's, Roll's,
   "lecture", "asset pricing", "geprijsd"), 12 Engelse citaten midden in zinnen, 5x "je"
   (r.93, 553, 982, 1418), 7x "Waarom zou dit waar zijn", "motief 1" en "2%-motief"
   (r.829, 981, 1261).
5. Opbouw: imports-cel in Overzicht (r.74), Overzicht zonder vraag-antwoord en lijst, geen
   routekaart en geen Samengevat in Theorie, toy eindigt met prints in plaats van een tabel
   hand/code, intuïtie eindigt zonder voorspelling, "Wat er brak" zonder de vier
   vetgedrukte elementen.

Schraptoets (eis 2 gecontroleerd met grep: buiten dit college wordt alleen het paginalabel
aangehaald; inhoudelijk gebruikt elders: Budish-Cramton-Shim (07_37 r.504), het citaat
"should not assume he can sell" (08_38 r.831), PS-alpha 3,6% en −0,8% (08_38 r.956), de
PS-cache (08_38 r.307), taxatie geen verkoopprijs (08_39 r.921), Kyles lambda (04_25 r.135)):

| passage | kopje | woorden | eis niet gehaald | actie |
|---|---|---|---|---|
| Hasbrouck-alinea | Roll | 55 | 1, 2, 3 | schrappen |
| werkversiegetallen Amihud-Kyle, "tijdschriftversies niet ingezien" | Amihud | 70 | 1 (werkmelding) | tot één zin, melding naar rapport |
| tweede deel propositie Amihud-Kyle (publiek nieuws) + bewijs | Amihud | 80 | 1 | inkorten tot één zin |
| FM-coëfficiënt zonder januari, AR-hellingen, decielen | Liquiditeit in de prijs | 140 | 1 | schrappen; kerngetal naar replicatietabel |
| PS-alpha's CAPM/FF, paginaverwijzingen | Liquiditeit als risico | 120 | 1 | naar replicatietabel, rest schrappen |
| AP-decompositie in vijf getallen | Liquiditeit als risico | 60 | 1 | tot twee getallen |
| homogeniteitsalinea, bewijs vele rondes | Kyle vele rondes | 110 | 1 | inkorten, bewijs blijft dropdown |
| GM-sessie als eigen simulatie | Simulatie | 150 | 1 (tweede simulatie) | dropdown in Theorie, figuurlabel weg |
| dubbele intuïtie-uitleg, Santa-Clara-citaten | Overzicht, Intuïtie | 230 | 1 | parafraseren en inkorten |
| replicatieblok boven 250 woorden | Replicatie | 110 | §11.7 | inkorten |
| getallen in replicatieproza | Replicatie | 150 | §11.5 | tabel origineel/hier |

Som van de schrappingen ca. 1.275 woorden; nieuw: routekaart, Samengevat, tabel en
vetgedrukte elementen ca. +250. Verwachte lengte ca. 5.200 woorden. Geen splitsing nodig.

## F1

Eindmeting: `words=5617 sent_mean=19.2 sent_p90=28 sent_gt40=0 para_mean=53 semicol=1
calque=0 engquote=2 colon_mid=0.9 para_one=8 tmpl=1 wie_open=1` PASS (nul: 6235, 13x FAIL).

Geschrapt of verplaatst:
- Hasbrouck-alinea (Roll): nevenresultaat, nergens aangehaald.
- Werkversiegetallen Amihud-Kyle en de melding "tijdschriftversies niet ingezien": één zin
  (R² 0,30) blijft; melding naar open punten.
- Tweede deel van de Amihud-Kyle-propositie (publiek nieuws, bruto omzet): één zin.
- FM-getallen zonder januari, AR-hellingen en decielgetallen Amihud: geschrapt, AR 0,764
  naar de tabel origineel/hier.
- PS-alpha's t.o.v. CAPM en FF, paginaverwijzingen, NBER-nummers: geschrapt; 7,5% blijft.
- AP-decompositie (0,08/0,16/0,82/4,6%): tot 1,1% en "het grootste deel via Cov(c_i,r_m)";
  bèta-opsomming tot één zin.
- Bewijs Kyle vele ronden (dropdown) en homogeniteitsalinea: één alinea bewijsidee.
- GM-sessie: van eigen simulatie naar dropdown-note in Theorie; `{figure}` en label
  `fig-microstructuur-gm-spread` weg (nergens aangehaald), cel-label blijft.
- Kyle vele ronden (recursie en 20.000 markten) als "### Numerieke oplossing" naar Theorie.
- Vijf Santa-Clara/Engelse citaten geparafraseerd of geschrapt; twee blijven (stelling 9 als
  blokcitaat, "should not assume" omdat 08_38 r.831 het aanhaalt).
- Toegevoegd: vraag-antwoord en lijst in Overzicht, voorspelling aan eind Intuïtie,
  opzet-tabellen en stappen in toy, routekaart, Samengevat, tabel origineel/hier met oordeel
  "Gedeeltelijk geslaagd", vier vetgedrukte elementen in "Wat er brak", onderdeel **Wat.**
  in het replicatieblok, hand-/codetabel, H4-getallen (spread 0,77 uit de formule, kans
  0,17 op onbruikbare Roll-schatting), H11-verwijzingen naar toy-getallen.

nb_outputs-diff (19+/17−): (1) toy-cel geeft nu de tabel "met de hand / code" i.p.v. prints,
zelfde getallen; (2) PS-figuur en alpha-cel van volgorde gewisseld (cel 15/16). Alle
gesimuleerde en gerepliceerde getallen identiek (rng-volgorde behouden). Codewijzigingen:
variabele `hand_vs_code`, `while`-lus in oefening 1 zonder `np.subtract(*...[::-1])`-truc,
docstring "value-weighted" → "cap-weighted". nb_numbers: 22 → 8 meldingen, alle 8
handberekeningen in de tekst (0,9984; 1,32; −0,121; −0,94) of bron (7,5; 0,764).

Afvinklijst §11.9, niet voldaan: `import requests`/`io` en de download in de PS-loader
blijven (STYLE §5: downloads alleen via hap.data; cache maakt het offline, zie open punt).
Overig: ok.

Labels: verdwenen `fig-microstructuur-gm-spread` (alleen binnen dit college). Geen label
verhuisd; paginalabel en alle eq/thm-labels blijven.

Open punten voor de feitencontroleur:
1. Amihud werkversie 2000: R² 0,30 (ILLIQ op Kyle-λ en vaste kosten) en AR(1) 0,764 per
   jaar (p. 19); tijdschriftversie niet ingezien.
2. Pástor-Stambaugh: "7,5% per jaar" (samenvatting) en de periode 1966–1999 in de tabel.
3. Acharya-Pedersen: 1,1% per jaar over 1963–1999 met grootste deel via Cov(c_i, r_m)
   (werkversie NBER w10814, p. 4–5).
4. `hap.data` mist een loader voor de Pástor-Stambaugh-reeks (lokale loader met
   `requests` blijft staan, TODO in de cel).

## F4

Feitenrijen (alleen onzeker; geen fout of niet herleidbaar):
- Rij 8 (R² 30% werkversie Amihud), Amihud: prijsimpact uit dagdata: gedaan, claim geschrapt;
  de alinea zegt nu waarom ILLIQ bruikbaar is (ruis middelt uit over een jaar, rangorde blijft).
- Rij 15 (AR(1) 0,764), Origineel en hier: gedaan, getal geschrapt, rij zegt "hoog, jaarlijkse AR(1)".
- Rij 17 (AP 1,1%), Liquiditeit als risico: afgewezen, bron geciteerd en getal blijft (voorstel
  feitencontroleur); een verificatiemelding is regeltaal (STYLE §11.12). Open=1.
Lezerspunten (alle vijftien gedaan):
1 Wat er brak: "Het model breekt niet in zijn logica, maar bij de meting." 2 en 3: zie rij 8 en 15.
4 Pástor-Stambaugh: alinea geknipt na "het jaar van publicatie", nieuwe alinea met post-2004-getallen.
5 Numerieke oplossing: "de continue limiet uit de propositie" met constante impact en lineaire daling.
6 Wat er brak: reden erbij ("omdat ze alle negatieve autocorrelatie als spread leest").
7 Toy (Kyle): "recept" weg, evenwicht overgenomen zonder afleiding. 8 Overzicht: "zette" niet meer dubbel.
9 Kyle één ronde: "omdat de verliezen van de noise traders het verzamelen van informatie betalen".
10 Amihud en Roll per aandeel: openingszin zonder inversie. 11 Liquiditeit als risico: "min het voorspelbare deel".
12 Liquiditeit als risico: λ_m krijgt uitleg (marktpremie min handelskosten, enkele procenten per jaar).
13 Na fig-microstructuur-kyle-pad: overgangszin (figuur toont gemiddelden, spreiding zegt de propositie niet).
14 Zelfde alinea: "iemand met echte informatie kan zijn voordeel moeilijk bewijzen". 15 Opzet: "zet" i.p.v. "noemt".
Verder: Kyle 1985 "stelling 2 en 3"; figuurzin na Kyle-simulatie zegt wat de figuur vergelijkt; motief
standaardfout van 2% niet meer als handelend onderwerp; sjabloon "De oefening laat zien" (2x) weg.
Navertel-toets: geen sectie week af van de bedoeling; Kyle vele ronden/Numerieke oplossing had een
krappe aansluiting ("die limiet"), nu opgelost. Code ongewijzigd, dus geen herberekening; nb_numbers 8 -> 7
meldingen (0,764 weg), geen nieuwe.

## R9-1 (F6b, ronde 9+)

- Feitelijke fouten 1 (Kyle-positie, :313 en :390): gedaan; de insider koopt de helft van $(v-p_0)/\lambda$, de positie waarbij de prijs tot $v$ stijgt, met de monopolist-vergelijking.
- Feitelijke fouten 2 (middenkoers): gedaan; tekst "pad van de verwachte waarde", codevariabele `mid` -> `value_path`, figuurtitel "Verwachte waarde in zes sessies". Uitvoer gelijk op de figuur na.
- Feitelijke fouten 3 (Roll-figuur): gedaan; "in het grijze gebied nauwelijks, pas bij grotere spreads zichtbaar dalend".
- Feitelijke fouten 4 (:1197 "orde van grootte", :1160 Stambaugh-bestand): gedaan; "opgeblazen" met reden (alle negatieve autocorrelatie, selectie-effect), bewering over Stambaughs bestand geschrapt.
- Feitelijke fouten 5 (Acharya-Pedersen 1,1%): open; bron geciteerd, niet in te zien zonder pdf.
- Helderheid: :311 "helft van de onzekerheid, gemeten als variantie"; herkomst 5% (nu "een premie als die van vóór 2003"); :1213 "een risicopremie vergoedt verliezen in crises"; regel over $\alpha_n$ vóór de recursie (zin "geen alpha's" uit de latere alinea verplaatst).
- Opbouw: routekaart noemt nu marktontwerp; Roll-spreads 60–170 bp gekoppeld aan het selectie-effect uit de simulatie.
- Taal: :305–307, figuurtekst :1064, :1205 en de Engelse quote (nu parafrase) herschreven.
- Toy: stap 4 toont $0{,}6\cdot0{,}6+0{,}4\cdot0{,}4=0{,}52$ en $0{,}36$; slotalinea duidt nu ook $\lambda$ voor de insider.
- Code: tekst noemt de derdegraadsvergelijking, de wortelkeuze $\alpha_n\lambda_n<\tfrac12$ en de terugschaling met $k$; `resid_var / 1.0` -> `resid_var`.
- Replicatie: verwachte afwijking voor $g_1$ en de alpha toegevoegd; getallen uit :1030, :1107 en :1163 naar de tabel; tabel met rijen vóór (5,4, t=2,72) en na publicatie (−0,81, se 3,03, t=−0,27); oordeel zegt welke afwijkingen binnen de verwachting vallen.
- Oefeningen: ex-2 verklaart 2,6 tegenover 4,1 (vijftig ronden, informatie gespreid).
- Checks: prose_stats PASS (5865 woorden), nb_numbers geen nieuwe meldingen (7 bekende), rewrap en jupytext --sync gedraaid, notebook offline uitgevoerd.

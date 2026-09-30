STATUS 04_25_industrie F4T words=5566 prose=PASS open=0 cijfer=- min=-

Kern: verliest actief beheer omdat niemand vaardig is? Nee: Sharpes rekenkunde laat de
gemiddelde actieve dollar vóór kosten precies de markt halen en na kosten achterblijven, en
in het evenwicht van Berk en Green gaat de vaardigheid die wel bestaat via fondsgrootte naar
de beheerder, zodat ze alleen in de cross-sectie (bootstrap, FDR) te zoeken is, en daar
nauwelijks zichtbaar.

## F0

prose_stats (gemeld): `words=3112 sent_mean=21.4 sent_p90=37 sent_gt40=10 para_mean=76
semicol=14 motief=4 je_form=2 calque=4 engquote=17 para_one=13 tmpl=4` FAIL.
Let wel: 3112 was een meetfout. `\$2 million` (Berk-Van Binsbergen) brak de `$`-paring, zodat
prose_stats daarna tekst als wiskunde wegstreepte. Zonder die escape: words=5652,
sent_gt40=19, semicol=36, calque=9, engquote=24, para_one=15, tmpl=6 (Waarom zou 6).

Vijf grootste problemen:
1. Taal, hele college: 19 zinnen > 40 woorden, 36 puntkomma's, 24 Engelse citaten midden in
   Nederlandse zinnen (Overzicht, Theorie, Replicatie), calques ("de nul", "Noteer", "short",
   "beprijsd", "Bogle's"), "je"-vorm, "motief 2/3", "epistemische status", "lecture".
2. Opbouw Theorie: geen routekaart en geen Samengevat; volgorde Sharpe → SE → Carhart →
   Berk-Green → bootstrap → FDR mengt kern, voorspelling en toets; zes keer "Waarom zou".
3. Toy: twee mechanismen (Sharpe én Berk-Green), geen tabel hand/code; imports-cel in Overzicht.
4. Simulatie: twee vragen (FDR-terugvinden én persistentie); Replicatie: blok ~330 woorden,
   geen tabel origineel/hier, geen oordeel "Geslaagd/Gedeeltelijk/Niet".
5. Regeltaal/werkmelding in de tekst ("hebben we niet kunnen raadplegen: betaalmuur"),
   "Waar we zijn" met vier cross-refs; Overzicht zonder vraag-en-antwoord vooraan.

Schraplijst (schraptoets STYLE §11.11; grep: alleen `thm-industrie-bh` wordt elders
aangehaald, in 06_34; de paginalabel door acht colleges):
| passage | kopje | ~woorden | eis niet gehaald |
|---|---|---|---|
| Renaissance/Simons-zin | Intuïtie | 25 | 1, 2, 3 (kleur) |
| Samuelson/Bogle-anekdote (11 mln, "Bogle's folly") | Intuïtie | 75 | 1, 3 (kleur); 2019-feit blijft |
| Grinblatt-Titman-alinea | Theorie, prestaties | 70 | 1, 2 |
| Kosowski e.a. met Engels citaat | Theorie, bootstrap | 50 | 1, 2 |
| betaalmuur-melding FF 2010 | Theorie, bootstrap | 35 | werkmelding hoort in rapport |
| persistentiesimulatie (top-kwintiel) + cel | Simulatie | 130 | tweede simulatievraag; persistentie zit in replicatie |
| VFINX-zin over grote ondernemingen | Replicatie | 30 | 1 |
| inkorten replicatieblok, Wat er brak (risico/vergissing ~190) | div. | 120 | lengtegrenzen §11.7 |
Verwacht: 5652 − ~535 + ~350 (voegwoorden, routekaart, Samengevat, oordeel) ≈ 5.450. Geen split.

## F1

Eindmeting: `words=5520 sent_mean=17.8 sent_p90=26 sent_gt40=0 para_mean=55 semicol=6 motief=0
je_form=0 calque=0 engquote=3 colon_mid=1.6 para_one=10 tmpl=1` PASS. Sync en offline
executie foutloos (nbconvert), geen CacheMissError.

Geschrapt of verplaatst (reden):
- Renaissance-zin, Samuelson/Bogle-anekdote: alleen kleur; het 2019-feit staat nu in Intuïtie.
- Grinblatt-Titman, Kosowski e.a., VFINX-zin: niet nodig voor de vraag (KosowskiTimmermannWermersWhite2006,
  Samuelson1974, Bogle2007 worden niet meer geciteerd; bib ongewijzigd).
- Betaalmuur-melding: werkmelding, uit de tekst.
- Persistentiesimulatie (cel `top_quintile_persistence`): tweede simulatievraag; gebruikt geen
  rng, dus de latere trekkingen zijn ongewijzigd.
- Berk-Green-rekenvoorbeeld + cel verhuisd van Toy naar Theorie (§Berk en Green), zodat het toy
  één mechanisme heeft; celvolgorde gelijk gebleven.
- Theorie herordend: Sharpe → Berk-Green → wat het voorspelt (Carhart, Berk-Van Binsbergen) →
  SE van alpha → bootstrap → FDR; routekaart en Samengevat toegevoegd; bewijzen Sharpe en SE
  naar dropdown; stelling Berk-Green ingekort, leerregel ervoor, bewijsstappen met kop.
- Engelse citaten geparafraseerd; tabel origineel/hier + oordeel "Gedeeltelijk geslaagd".

nb_outputs-diff (22+/32−): toy-cel toont nu tabel "met de hand / code" i.p.v. prints en
vermogen/bruto/netto (zelfde getallen 4,00; 7,50; −1,25; 3,00; 0,90); persistentiecel weg
(cellen daarna één nummer lager); rijnamen "EW-portefeuille actief" → "gelijkgewogen actief"
(zelfde waarden); figuurtitel bootstrap-echt gewijzigd. Geen enkel aangehaald getal veranderd.

Afvinklijst §11.9, wat niet voldoet: niets bekend. Hardop-toets per sectie gedaan.
Labels: geen verdwenen of verhuisd; alle eq-/thm-/fig-/cel-labels bestaan nog.

Open punten voor de feitencontroleur:
1. Jensen −1,1% per jaar na kosten (Overzicht, tabel): uit bron, geen cel.
2. French 0,67% per jaar 1980–2006 en Berk-Van Binsbergen ~2 miljoen dollar per jaar (NBER
   2012), BSW 75% nul-alpha, Berk-Green 80%: geparafraseerd uit citaten, niet opnieuw nagelezen.
3. "Sharpe-ratio ongeveer 0,14 per maand → 1,02" (SE-alinea): handberekening, geen cel.
4. Samuelson1974, Bogle2007, KosowskiTimmermannWermersWhite2006 niet meer geciteerd; ICI 2020
   (15%, eind 2019) blijft de enige bron voor het jaartal 2019.

## F4

Feiten: rijen 1–8 en 10–14 juist, niets te doen. Rij 9 (BSW 75%) wordt "ongeveer driekwart" (Theorie, FDR). open=0.
Lezerspunten, alle vijftien gedaan:
1. Berk en Green: "precies zoals de intuïtie verwachtte" herschreven, de zaak als onderwerp.
2. Replicatie: "die we ... voorspelden" wordt "die de selectie op overleven meebrengt".
3. Intuïtie: "tegen hem in" wordt "tegen het fonds in".
4. Berk en Green, bewijsstap 2: multiplicatoren als schaduwprijzen benoemd (zin herschreven).
5. Berk en Green: 78% gekoppeld aan de 4,5 miljard.
6. Wat het model voorspelt: 2012 als eerdere werkversie van hetzelfde onderzoek; citaat 2015 naar zinseinde.
7. Wat er brak: "de oprichters van DFA en AQR" in plaats van drie niet eerder genoemde namen.
8. Berk en Green: reden bij $f$ (de belegger houdt al bij een kleiner fonds niets over).
9. Sharpes rekenkunde: twee "Volgens"-zinnen tot één zin.
10. Overzicht: Santa-Clara-zin gesplitst, "wie"-constructie weg.
11. Overzicht: "die bij die bevinding hoort" wordt "de bijbehorende industrie".
12. Wat er brak: dubbele bijzin weg.
13. Overzicht: "mengt een stelling met feiten" wordt bewezen versus gemeten, met reden.
14. Simulatie: "ruim een kwart" wordt "iets meer dan een kwart".
15. Overzicht: driedelige zin gesplitst.
Navertel-toets: geen sectie week af (lezer: alle twaalf klopt).
Verder: laatste Samengevat-bullet (over de simulatie) geschrapt; de motieflink bij de SE van
alpha zegt nu wat het motief hier betekent; nb_numbers: dezelfde 6 meldingen als vóór; code ongewijzigd.

## R9-1 (F6b, ronde 9+)

- **Feitelijke fout 1 / verbetering 2 (French 0,67%)**: gedaan. Replicatiezin vergelijkt nu met Jensens −1,1% na kosten ("ruim anderhalf procentpunt"); tabelcel alleen "−1,1% per jaar (Jensen)". French blijft correct in Theorie (van de marktwaarde).
- **Eén ijkpunt (r. 874, 1038)**: gedaan. Admonition noemt nu "de −1,1% van Jensen" in plaats van "−0,5 tot −1%" (die range had geen bron).
- **Feitelijke fout 2 / verbetering 1 (stelling Berk-Green)**: gedaan. Stelling: E_t[r]=0 algemeen, C'(q_a)=phi_t "zolang het fonds een indexdeel heeft". Stap 2: Lagrangiaan uitgeschreven, eerste-ordevoorwaarden voor q_a en q, lambda^f=0 door complementariteit, lambda^p=1>0; randgeval lambda^f>0 en C'<phi_t. Bijzin bij lim C'>1: het fonds blijft eindig groot.
- **Verbetering 3 (naam vaardigheid)**: gedaan. Code `a`→`phi`, `a_new`→`phi_new`, benoemde `q_active_new`; label "naar phi = 4%". Tekst: "verwachte vaardigheid ... op phi = 4%" en "verwachte vaardigheid van drie procent". Uitvoer vóór/na: alleen commentaar en label verschillen, offline uitgevoerd zonder fout.
- **Growth-index (r. 946–950)**: gedaan; dezelfde reden werkt bij negatieve HML-lading de andere kant op.
- **Getallen in lopende tekst (r. 952–958)**: gedaan; "+0,5%" en t=1,36 weg, verwijzing naar de tabel.
- **Overzicht r. 41–42 (waarneming)**: gedaan; verwijst nu naar Carhart (factoren en kosten verklaren de persistentie).
- **Hardop r. 43, 45–46, 1072**: gedaan (herschreven volgens voorstel).
- **r. 786 "Als teller"**: gedaan ("Om vaardige fondsen te tellen").
- **r. 419–422 werkversie 2012**: deels. Zin herschreven ("Volgens de werkversie ... op die manier ongeveer 2 miljoen"), "zo ongeveer" weg. Het gepubliceerde getal uit 2015 niet opgenomen: niet geverifieerd (kaart §6).
- **ex-industrie-2 (2)**: gedaan; "van 4,5 naar 5,1 miljard dollar" uit de celuitvoer.
- **Simulatie r. 621 (dunne toy-draad)**: niet gewijzigd; H11 formeel vervuld, geen "Voor een 9"-punt.
- Woorden 5679 (was 5566), prose_stats PASS; nb_numbers 4 meldingen, alle vier bestaand (3,9; 0,67; 0,167; 1,67). Rewrap en sync gedraaid.

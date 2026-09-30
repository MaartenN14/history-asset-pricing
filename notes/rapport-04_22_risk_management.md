STATUS 04_22_risk_management F4T words=5717 prose=PASS open=0 cijfer=- min=-

**Kern.** Kan een bank met een voorspelbaar tweede moment haar kans op grote verliezen meten
en begrenzen, en waarom was dat in 1998 niet genoeg? Voor de gewone slechte dag wel, want een
VaR op een snel aangepaste volatiliteit werkt redelijk, maar het getal zegt niets over wat
voorbij het kwantiel ligt, is met een jaar data niet te toetsen, en ziet niet dat hefboom,
dagelijkse waardering en onderpand een trade met positieve verwachting in een verliesspiraal
kunnen dwingen.

## F0

`words=5066 sent_mean=21.1 sent_p90=35 sent_gt40=18 para_mean=55 semicol=44 motief=1 je_form=2 calque=4 engquote=16 colon_mid=9.3 para_one=31 tmpl=5 connect=19` — FAIL op sent_mean, sent_p90, sent_gt40, semicol, motief, je_form, calque, engquote, colon_mid, para_one, tmpl, connect. Words binnen de grens.

Vijf grootste problemen:
1. **Overzicht** (r. 34–76): geen vraag en antwoord, geen lijst, drie alinea's geschiedenis met
   vier Engelse citaten, "Epistemisch" (r. 47); de imports-cel staat in Overzicht.
2. **Taal, hele college**: 16 Engelse citaten (Santa-Clara r. 43, 57, 87, 107, 1076; BCBS
   r. 266, 346, 427; RiskMetrics r. 280, 306; PWG r. 986, 1074), 44 puntkomma's, 18 zinnen
   boven 40 woorden, 31 eenzinsalinea's, je-vorm (r. 90, 98), "motief 1" (r. 469), calques
   (r. 80, 311, 351, 1085).
3. **Theorie** (r. 207–602): geen routekaart en geen Samengevat; het kernresultaat (VaR niet
   coherent) staat pas als vijfde subsectie; de horizon-propositie is een nevenresultaat; $a$
   betekent zowel GARCH-coëfficiënt als spiraalfactor (H7).
4. **Toy-voorbeeld** (r. 111–205): geen opzet-tabel, uitvoer via `print` in plaats van een
   tabel hand/code, geen slotzin; de intuïtie eindigt zonder voorspelling (H12).
5. **Replicatie en oefeningen** (r. 824–1225): getallenbrij in proza (r. 956–974, 1045–1061),
   geen tabel verwacht/hier, geen oordeel "Geslaagd"; regeltaal (r. 1060); cellen zonder tekst
   ertussen (r. 722–783, 853–896); oefening 1 is geen instap.

Schraplijst (eis 2 met grep: buiten dit college worden alleen `04-22-risk-management`,
`prop-risk-management-drempel`, `prop-risk-management-spiraal` en `eq-risk-management-spiraal`
aangehaald):

| passage | woorden | eis die ze niet haalt |
|---|---|---|
| Theorie, variantie over $k$ dagen: propositie, bewijs, cel, alinea (r. 322–372) | ~230 | 1, 2, 3; één zin over de tiendagenregel gaat naar toy (a) |
| Overzicht, tweede en derde alinea geschiedenis (r. 43–61) | ~120 | 1 (dubbel met intuïtie en theorie) |
| Replicatie, "twee op honderd miljard" (r. 1049) | ~20 | niet herleidbaar tot een cel |
| Replicatie, meldzin over 4,6 miljard (r. 1060) | ~30 | regeltaal; naar open punten |
| Oefening 2, tabel 1 van Bazel (r. 1147–1180) | ~130 | 1; de kracht staat al in figuur en tabel |

De tweede simulatie (convergence trade) blijft om eis 1 (tweede helft van de open vraag).
Verwachte lengte ≈ 5.300 woorden. Geen splitsing nodig.

## F1

**Eindmeting.** `words=5606 sent_mean=16.9 sent_p90=26 sent_gt40=0 para_mean=49 semicol=1 engquote=0 colon_mid=0.7 para_one=5 tmpl=2 connect=33` — PASS. Iets boven het doel van 5.500, onder de grens.
Notebook draait offline zonder fout.

**Geschrapt of verplaatst.** Horizon-propositie met cel (nevenresultaat); dubbele
geschiedenis in Overzicht; oefening over tabel 1 van Bazel (kracht staat in figuur en
simulatietekst); de "twee op honderd miljard" en het niet-geverifieerde totaalverlies van 4,6
miljard (Lowenstein) uit de tekst; het derivatenbedrag uit Edwards (1999), de tabellen 5.7/5.8
van RiskMetrics en de optimum-range 0,835–0,995 (getallenlast); alle 16 Engelse citaten zijn
parafrasen geworden. Imports-cel naar het toy-voorbeeld. Nieuw: vraag/antwoord en lijst,
routekaart, Samengevat, opzet-tabel en hand/code-tabel, verwachtingen in de intuïtie met
inlossing in theorie en simulatie, tabel verwacht/hier plus "Geslaagd", instapoefening.

**nb_outputs-diff.** (1) Toy-cel: `print`-regels vervangen door tabel hand/code, zelfde
getallen. (2) Horizon-cel weg. (3) Simulatietabel: kolommen heten "fractie
overschrijdingen" en "rood na een jaar"; waarden ongewijzigd (zelfde `rng`-volgorde). (4)
Nieuwe cel bij oefening 1 (drempels 93,3/133,3 en 60/100 bp, hoogste hefboom 16,1). (5) Cel
tabel 1 Bazel en 1070 dagen weg. Alle overige uitvoer gelijk; celnummers verschoven.

**§11.9, niet voldaan.** Simulatie heeft twee `###`-delen onder één vraag (fondssimulatie
kan niet naar Theorie zonder de `rng`-volgorde en dus de getallen te veranderen).

**Labels.** Weg (nergens anders aangehaald): `def-risk-management-es` (samengevoegd in
`def-risk-management-var`), `prop-risk-management-horizon`, `eq-risk-management-horizon`,
`ex-risk-management-4`. Oefeningen hernummerd: oude 1 → 2, oude 3 → 3 (FHS), nieuwe 1. In
de spiraal heet de factor nu $\theta$ in plaats van $a$; labels ongewijzigd.

**Open punten voor de feitencontroleur.**
1. "Het Comité schreef ... beperkt onderscheiden (p. 5)": BCBS1996a of BCBS1996b?
2. Parafrasen Santa-Clara (dagen voorbij de grens; recept voor ruïne) tegen SantaClara2026.
3. PWG-rapport: p. 12 (premies stegen, verliezen boven modellen), p. 16 (weddenschap), p.
   12–14 (4,1 mld, 1,8 mld, 23 september, veertien instellingen, 3,6 mld, 90%).
4. Jorion2000 omschreven als analyse van de risicobeheersing van LTCM.
5. "Eind augustus 1998 ... 125 miljard ... 4,8 miljard" (was 31 augustus) tegen PWG.
6. `Edwards1999` wordt niet meer geciteerd (bib-entry ongebruikt).
7. Markdown-tabel in de replicatie herhaalt afgeronde celwaarden (3,26/1,63/1,98/2,15; 27,3/23,9/6,0/4,2).

## F4

**Feitenrijen.** Nr. 10 (Replicatie, VaR-backtest): 2020 herschreven, statisch model ook rood met 23. Nr. 11 (bijschrift jaren-figuur): elf van de 36 rode jaren genoemd. Nr. 16 (Intuïtie): "Op 31 augustus 1998". BCBS p. 5 (Theorie, toetsen): citatie apart aan BCBS1996b. Nr. 8 afgewezen: de tabel hier/juist model is door rubriek criterium 6 en STYLE §10 verplicht. Edwards1999: geen actie.

**Lezerspunten.**
1. gedaan (Replicatie, VaR-backtest), zie feitenrij 10.
2. gedaan (Theorie, gehefboomde arbitrageur): zin "Vanaf hier staat $L$ voor de hefboom en niet meer voor het verlies"; ander symbool zou de wiskunde en labels raken.
3. gedaan (Simulatie, vier goede jaren): derde verwachting expliciet ingelost na de fire-sale-tabel.
4. gedaan (Overzicht): brugzin "Al die regels en toetsen gaan over een meetinstrument".
5. afgewezen: tabel origineel/hier verplicht (rubriek criterium 6); alleen de aankondiging ingekort.
6. gedaan (Simulatie): aankondiging `run_fund` noemt nu het maandelijks herstellen van de hefboom; het wegebben van de prijsdruk staat vóór de tweede run.
7. gedaan (Theorie, kernresultaat): ES-stap in het bewijs eindigt met 101,26 tegen $2 	imes 79{,}6$.
8. gedaan (Replicatie), zie feitenrij 11.
9. gedaan (Overzicht): leerboek en afdelingen in één lijn.
10. gedaan (Intuïtie): "Het slecht meetbare verwachte rendement telt dus niet mee".
11. gedaan (Theorie, kernresultaat): drie axioma's in twee zinnen met eigen werkwoord.
12. gedaan (Theorie): richting en $1/L$ in de propositie, herhaling eronder geschrapt.
13. afgewezen: de oplossing zegt al "dus 60 basispunten".
14. gedaan, zie feitenrij 16.
15. gedaan (Replicatie): "waarvoor $a + b$ precies 1 is".

**Navertel-toets.** Afwijkend vóór F4: Simulatie (derde verwachting niet ingelost) en Replicatie VaR-backtest (2020 onvolledig); na F4 dekken beide de bedoeling.

## R9-1 (F6b, ronde 9+)

Woorden: 5.926 (was 5.717); prose_stats PASS; nb_numbers 38 meldingen, geen nieuwe; celuitvoer ongewijzigd na herdraaien (alleen commentaar toegevoegd).

- **Feitelijke fout 1 / verbetering 1 (fire sale, theta)** gedaan: nieuwe alinea na de fire-sale-tabel met $\kappa$ = 2 bp per eenheid beginvermogen (twee keer het toy), $\theta \approx 0{,}05\,L$, dus 0,5 bij hefboom 10 (plus margin call 0,9%, cel 8), 1 bij hefboom 20 en groter dan 1 bij 25; foute reden geschrapt.
- **Feitelijke fout 2 (FHS 2020)** gedaan: "iets vaker overschreden dan verwacht, maar blijft daar groen".
- **Verbetering 2 (genummerde verwachtingen)** gedaan: alle vier rangtelwoorden vervangen door wat er voorspeld werd (kernresultaat, arbitrageur, backtest, fire sale); hardop-zinnen 1–3 herschreven zoals voorgesteld.
- **Verbetering 3 (spreiding)** gedaan: in de Intuïtie "volatiliteit" voor dispersie; "spreiding" betekent nu overal diversificatie.
- **Santa-Clara** gedaan: punt toegeschreven aan Artzner e.a. (1999), Santa-Clara als auteur van de terugblik die de reeks volgt.
- **Notatie $\ell$ en $m$** gedaan: $x$ in de VaR-definitie en toy (b), $k$ in translatie-invariantie.
- **Samengevat, wortelregel** gedaan: de standaardfout in Theorie staat nu als functie van $T$ en daalt met de wortel van $T$.
- **Toy intro** gedaan: zegt wat (a), (b) en (c) elk laten zien. Eén mechanisme in plaats van drie niet doorgevoerd: de drie delen dragen elk een deel van het college (H11) en herstructureren valt buiten F6b.
- **Toy (c), rondes** gedaan: elke ronde kost minder dan de helft van de vorige, de rest voegt 1,3 toe (22,0 − 12,5 − 5,86 − 2,32).
- **Code**: commentaar bij `tail_mass` en bij de inline Kupiec-statistiek in paneel (b) (kupiec_lr verwacht een hitreeks, paneel b rekent per aantal); berekening ongewijzigd.
- **Replicatie VaR** gedaan: "met wat we vooraf verwachtten"; figuurtekst "in de rustige jaren meestal groen".
- **Spreads 1998** gedaan: getallenopsomming ingekort, zin toegevoegd waarom er geen origineel getal naast staat.

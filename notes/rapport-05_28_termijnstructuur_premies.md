STATUS 05_28_termijnstructuur_premies F4T words=5552 prose=PASS open=1 cijfer=- min=-

# Rapport 05_28_termijnstructuur_premies

**Kern.** Is het extra rendement op lange obligaties constant, zoals de expectations
hypothesis zegt? Nee: de vorm van de curve voorspelt het rendement en niet de rente (Fama-Bliss,
Campbell-Shiller, één tentfactor van Cochrane-Piazzesi), en de correlaties tussen looptijden
vragen meer dan een handvol factoren (het string-model).

## F0

`05_28_termijnstructuur_premies  5849  20.9  35  16  57  0  55  3  0  0  0  3  0  0  14  16  12.8  21  1  8  5  20  0  2/8`
FAIL: sent_mean 20,9, sent_p90 35, sent_gt40 16, semicol 55, motief 3, je_form 3, calque 14,
engquote 16, colon_mid 12,8, para_one 21, telegram 1, tmpl 8 ("Waarom zou"), wie_open 5.

### Vijf grootste problemen

1. Taal (hele college): 16 zinnen boven 40 woorden, 55 puntkomma's (vooral Replicatie r.862–866,
   r.940–943), 12,8 dubbele punten per 1000 woorden, 16 Engelse citaten midden in zinnen
   (Overzicht r.39, Theorie r.399, 430, 464, 536, 581, Wat er brak r.1227, 1238).
2. Structuur: Overzicht opent met een citaat in plaats van vraag en antwoord (r.39), de
   imports-cel staat in het Overzicht (r.72), Theorie heeft geen routekaart en geen Samengevat.
3. Twee simulaties (r.589 affien model, r.761 strings tegen factoren); de tweede beantwoordt
   een andere vraag.
4. Toy (r.165): uitvoer met `print` in plaats van een tabel met de hand / code; de intuïtie
   eindigt zonder voorspelling die de theorie inlost (H12); Oefeningen zonder instap.
5. Regeltaal en werknotities: "motief 3" (r.59), "motief 1" (r.755, r.945), "Epistemisch",
   "lecture" (r.59), "hebben we niet kunnen inzien" (r.397), "staat niet in de abstracts"
   (r.585); acht keer "Waarom zou dit waar zijn"; ex-labels als link (r.1128, r.1225);
   "term premium" (r.235) waar 03_17 "termijnpremie" invoerde.

### Schraplijst (STYLE §11.11)

Eis 2 gecontroleerd met grep: van buiten dit college wordt alleen het paginalabel
`05-28-termijnstructuur-premies` aangehaald (03_17, 05_27, 05_29, 08_38). 08_38 r.955 citeert de
Fama-Bliss-hellingen 0,72–1,20 en $t$ 2,6–2,9 (1964–2026) en r.777 de simulatie van de
Hansen-Hodrick-toets; die blijven.

| passage | kopje | woorden | reden |
|---|---|---|---|
| citaat Santa-Clara en Fisher/Hicks/Lutz-detail | Overzicht | −60 | geen eis; geschiedenis wordt één alinea |
| HAC-formule, keuze $w_j$ en $L$, $\chi^2$ 811/105 | Theorie, overlappende waarnemingen | −110 | eis 1–3 niet; één alinea blijft voor de simulatie |
| "billion dollars" en "staat niet in de abstracts" | Theorie, caps en swaptions | −60 | werknotitie, geen eis |
| "oorspronkelijke tabel niet kunnen inzien" | Theorie, Cochrane-Piazzesi | −35 | werknotitie, naar rapport |
| tabel 5 (vertraagde forwards, $R^2$ 0,44) | Theorie, Cochrane-Piazzesi | −60 | alleen nodig in de oefening |
| tweede simulatie (strings tegen factoren) | Simulatie | −150 netto | tweede steekproefvraag; wordt oefening 4 |
| replicatieblok 380 → 250 | Replicatie | −130 | §11.7; gepubliceerde getallen staan in de tabellen |
| getallen in lopende tekst | Replicatie | −150 | staan in de tabellen |
| "Waar het breekt" en "Risico of vergissing" | Wat er brak | −100 | elk ≤ 120 woorden |
| bewijzen EH en CS-FB | Theorie | 0 | naar dropdown (> 6 regels) |
| routekaart, Samengevat, instapoefening | | +290 | vereist |

Verwachte lengte: 5849 − 855 + 290 ≈ 5.280 woorden. Geen splitsing nodig.

## F1

Eindmeting: `words 5507, sent_mean 17.7, p90 27, gt40 0, para_mean 44, semicol 5, colon_mid 0.5,
para_one 7, tmpl 1, wie_open 2` — PASS. (Eerste herschrijving kwam op 6473 woorden; de meting
telt uitwerkingen en dropdowns mee, daarom is daarna extra geschrapt.)

Geschrapt of verplaatst, bovenop de schraplijst van F0:
- HJM-driftstelling met bewijs (`thm-…-hjm`, `eq-…-drift`) en gevolg `cor-…-rang`: niet nodig
  voor de vraag; twee zinnen over de drift onder $\mathbb Q$ blijven.
- Stringsimulatie en haar figuur (`cel-/fig-…-string`) → oefening 4 (zonder figuur); cel staat
  achteraan, dus de rng-stroom en alle uitvoer zijn gelijk.
- Gepubliceerde standaardfouten van Campbell-Shiller, $\chi^2$ 811/105/15,1, "som 0,39", de
  Newey-West-alinea bij de tent en de Litterman-Scheinkman-zin: getallenbrij of niet herleidbaar.
- Citaat van Longstaff e.a. 2001b ("billion dollars") en de cite `LongstaffSantaClaraSchwartz2001b`.
- Imports-cel naar het begin van het toy-voorbeeld; bewijzen EH en CS-FB in dropdown.

Toegevoegd: routekaart, Samengevat, intuïtie met voorspelling (ingelost bij Campbell-Shiller),
toy-tabel met de hand / code, oefening 1 (instap), oordelen Geslaagd / Gedeeltelijk / Niet
geslaagd per deelreplicatie, 'termijnpremie' als vaste term (03_17 r.316).

nb_outputs-diff (alle aangehaalde getallen gelijk):
- cel toy: `print`-regels → tabel "met de hand / code"; rx^(2) vervalt (niet aangehaald).
- cel CS jaarlijks: kolommen `start` en `SE` vervangen door `t (b = 1)`; hellingen gelijk.
- nieuwe cel oefening 1 (rx3 2,8749; verandering −0,5525; identiteit 1,7700).
- stringcel verhuisd van cel 5 naar cel 18 (oefening 4), uitvoer identiek; stringfiguur weg.
- oefening 3: rijlabel "vertragingen" → "lags".
- nb_numbers: 18 meldingen, allemaal tussenstappen van de handberekening (log-prijzen).

Afvinklijst §11.9: woorden 5507, net boven het doel van 5.500 (grens 6.000); overige: ok.

Labels verdwenen (nergens buiten dit college aangehaald, grep): `thm-termijnstructuur-premies-hjm`,
`eq-termijnstructuur-premies-drift`, `cor-termijnstructuur-premies-rang`,
`eq-termijnstructuur-premies-hac`, `cel-/fig-termijnstructuur-premies-string`. Nieuw:
`ex-termijnstructuur-premies-4`; de ex-labels 1–3 hebben nieuwe inhoud (oud 1 → 2, oud 2 → 3).

Open punten voor de feitencontroleur:
1. Getallen uit artikelen zonder cel: CP tabel 7 (sd 1,9–6,0 pp), CP tabel 1/2/4 ($R^2$ 0,35,
   9–18%, 0,26), CS 1952–1987 ($-1{,}8$ tot $-5{,}0$), Duffee "bijna de helft", LSS 2001a (vier
   factoren, lagere geïmpliceerde correlaties), Bauer-Hamilton (bootstrap).
2. Santa-Clara stelling 8 is nu geparafraseerd (`SantaClara2026`); formulering nakijken.
3. "Standaardfout van ongeveer een derde" (Simulatie) is afgeleid uit het 95%-interval
   0,45–1,76: (1,76 − 0,45)/3,92 ≈ 0,33.
4. De oorspronkelijke tabel van Fama en Bliss (1987) is niet ingezien; vergelijking loopt via
   CP tabel 2 (werknotitie uit de tekst gehaald).
5. Toy stap 3: $-0{,}4773 + 2 \times 1{,}1236 = 1{,}7699$ op afgeronde getallen; de tekst zegt
   "op onafgeronde getallen" (code: 1,7700).

## F4

Feitenrijen:
- 2, 3 (Toy stap 3, Oefeningen 1): gedaan, "op de onafgeronde getallen is ... = 1,7700%", afwijking in de vierde decimaal benoemd.
- 6 (Theorie, Cochrane en Piazzesi): gedaan, periode weg, "geen enkele afzonderlijke Fama-Bliss-regressie komt boven 18%".
- 8, 9, 10 (Theorie, Duffee / LSS 2001a / Bauer-Hamilton): juist volgens de abstracts; tekst blijft, Duffee als "Volgens ...".
- 11 (Simulatie, CP tabel 7): gedaan, getallen 1,9–6,0 pp en 20% geschrapt, zin kwalitatief.
- 12 (Overzicht, Santa-Clara 2026): afgewezen, ruime parafrase met citatie, bron niet publiek; open.

Lezerspunten:
1, 2 als rij 2 en 3. 3 als rij 6. 4 (Wat er brak): gedaan, "Waar het breekt" in twee alinea's, robuust en minder robuust.
5 (Theorie, string): gedaan, openingszin zegt waarom de curve nu in continue tijd moet bewegen.
6 (Theorie, overlappende waarnemingen): gedaan, de drie regressies bij naam.
7 (Theorie, verborgen factor): gedaan, deel (ii) gekoppeld aan het recessievoorbeeld met "een kwart daarvan" (geen nieuwe getallen).
8 (Replicatie, correlaties): gedaan, terugverwijzing naar de verwachting uit de intuïtie.
9 (Samengevat): gedaan, reden bij $b_n$ (langere obligatie verliest of wint meer koers bij dezelfde renteschok).
10 (Overzicht): gedaan, slotzin "Sindsdien staat vast dat de termijnpremie beweegt, maar waarom ..."
11, 12: bron bevestigd (rij 8, 9); LSS geeft geen getal, dus geen toevoeging.
13 (Waar we zijn): gedaan, twee zinnen met gevolg. 14: dubbele spaties en spaties aan regeleinde weg.
15 (Oefeningen 1): gedaan, waarom één jaar premie en renteschok niet scheidt.

Betaald met: HJM-driftalinea ingekort, "De theorie leidt deze identiteit als eerste af", Svensson-bijzin in CS-intro,
figuurzin bij de correlaties. Woorden 5507 -> 5552. Code en celuitvoer ongewijzigd (nb_outputs identiek, nb_numbers zonder nieuwe meldingen).
Navertel-toets: geen sectie week af; alleen de stringsubsectie miste een overgang (punt 5).

## R9-1 (F6b, ronde 9+)

Woorden 5.735 (was 5.552), prose_stats PASS (zin > 40: 0), nb_numbers 18 meldingen, alle al bestaand (toy-tussenwaarden).
- **Feit 1, :551 volatiliteit identiek**: gedaan, nu "de schokken in de toestand zijn identiek", en via $\Phi^{\mathbb Q}$ veranderen prijzen en yieldladingen.
- **Feit 2, :793 binnen één SE van één**: gedaan, "op de tweejaarsobligatie tot 2026 na" (0,721, SE 0,274; de andere elf wel binnen één SE, nagekeken in de celuitvoer).
- **Feit 3, :1087 tent hoog**: gedaan, "als de factor hoog staat" (H7).
- **Feit 4, SantaClara2026**: open; de bron is een LinkedIn-post die offline niet te controleren is.
- **:1019 0,08 uit de theorie**: gedaan, "de 0,08 die de Theorie ter illustratie koos".
- **:836 midden positief**: gedaan, "dat op $f^{(2)}$ en $f^{(3)}$ positief" (3,80 en 0,15).
- **Taal :136, :434, :652, :708**: herschreven volgens de hardop-toets; :708 zonder nieuw getal (0,33 zou niet herleidbaar zijn), nu "de band uit de vorige alinea is breder dan de ware helling zelf".
- **:434 waarom continue tijd**: regressies geven alleen een verwachting, een optieprijs hangt af van hoe de hele curve tot de uitoefendatum kan bewegen.
- **:479 normaal model**: model van Bachelier genoemd; de swaprente is dan normaal en een at-the-money-prijs evenredig met haar standaardafwijking.
- **:701 Stambaugh in één bijzin**: persistente spread, schokken die met het rendement samenhangen.
- **Opbouw, derde verwachting**: intuïtie voorspelt nu ook de verborgen vorm; ingelost (negatief) in het oordeel bij de PCA-tabel.
- **Code :754**: `(100 * yields).describe()`, count nu 783. **:953**: `lags=steps`. **:982**: kolommen "SE t/m 1987" en "SE t/m 2026". Uitvoer voor/na: alleen deze labels en de count verschillen.
- **Leeswijzer correlatiefiguur**: gedaan, eigen alinea vóór de figuur.
- **Bronregels**: rewrap.py plus reflow van 21 rafelige prozaalinea's buiten fences; gerenderde tekst onveranderd.

STATUS 00_00_setup F6b words=5034 prose=PASS open=1 cijfer=- min=-

# Rapport 00_00_setup (L0)

## F0

Nulmeting `prose_stats`:

```
00_00_setup.md  words 3972  sent_mean 20.5  sent_p90 34  sent_gt40 12  para_mean 55  dash 37
semicol 16  motief 2  Lnum 0  deel 1  u_form 18  je_form 2  taboo 0  stopw 6  calque 2  engquote 5
```

`--where`: "epistemische status" (r. 57), "Shiller's" (r. 303).
Voor-uitvoer: `$TEMP/voor-00_00_setup.txt` (25 cellen; `git show` via Bash, want PowerShell `>`
schrijft een BOM die `nb_outputs.py` weigert).

Vijf grootste problemen:

1. **Motieven niet volgens STYLE §11.3** (De rode draad, r. 88–114): "Risico versus
   vergissing" en "Van theorie-met-tests naar feiten-met-concurrerende-theorieën" in plaats
   van de vaste namen; "het 2%-motief" (r. 140), "epistemische status" (r. 57). De
   introducerende zin zegt niet wat de drie motieven betekenen; waarom de standaardfout "2%"
   heet terwijl de tekst 18% en 1,8 gebruikt, wordt niet uitgelegd.
2. **Aanspreekvorm en zinsbouw** (overal): 18× "u", 2× "je", 37 gedachtestreepjes, 16
   puntkomma's, 12 zinnen boven 40 woorden, alinea's gemiddeld 55 woorden.
3. **Beschrijving van de lecture-opbouw klopt niet meer** (De didactische trap, r. 62,
   121–155): "in drie treden" gevolgd door vier punten; imports-cel "in elke lecture
   bovenaan" (nu bij het toy-voorbeeld, §11.7); "Samengevat" en de routekaart ontbreken;
   "zevenendertig" andere lectures (er zijn er 39); "Deel IV" (r. 625).
4. **Codecellen zonder tekst ertussen** (De data, alle zeven bronnen): data- en figuurcel
   staan telkens direct achter elkaar (§11.8). Imports-cel staat in het Overzicht (§11.7:
   geen code in Overzicht). Overzicht mist vraag-en-antwoord en de lijst.
5. **Getallen niet herleidbaar of fout**: 83,7% (fig-setup-french), 2,2% in februari 2009
   (fig-setup-hkm, aangehaald in `05_32_intermediaries`), mediane $t$ 4,0 (fig-setup-osap) en
   $R^2$ "iets meer dan één procent" komen uit geen enkele zichtbare uitvoer (nagerekend:
   83,65%; 2,23% op 2009-02-28; 3,995; 0,0118). Uitwerking oefening 1 zegt dat de aanname van
   nulcorrelatie de standaardfout "te klein" maakt; bij positieve correlatie (0,44) is ze te
   groot (gepaard 2,8 tegen 3,7 procentpunt). Engels citaat midden in een zin (r. 116).

Schraplijst (schraptoets §11.11; de lecture zit onder 5.500, dus alleen wat de toets zegt):

| passage | woorden | eis die ze niet haalt |
|---|---|---|
| Overzicht, alinea "epistemische status ... gereedschapskist" | ~55 | geen van drie; herhaalt de vorige alinea |
| Notatie, lijst Engelse vaktermen (r. 204–210) | ~30 | 1; staat al in index en STYLE, één zin volstaat |
| "Hoe u zelf werkt", `jupyter book start/build`-commando's | ~15 | 1; bouwen van de site is geen vraag van de lecture |
| De gereedschapskist, $R^2$-bijzin | ~10 | niet herleidbaar |

Eis 2: grep in `lectures/` vindt alleen het lecturelabel `00-00-setup` (L1, L3, L4, L32)
en de getallen 11,6% / 1,8 procentpunt (L1), 2,2% (L32), het citaat van Santa-Clara (L4) en
de notatie $R$ bruto, $r$ netto, kleine letters log (L1, L3). Geen figuur-, cel-, vergelijkings-
of oefeningslabel wordt elders aangehaald. Verwachte lengte na schrappen ~3.850, plus
aanvullingen (Overzicht-lijst, motiefzin, zinnen rond cellen) ~4.000–4.300. Geen splitsing.

## F1

Eindmeting: words 4213, sent_mean 14.0, p90 22, gt40 0, para 41, dash 0, semicol 6,
u/je/motief/deel/calque/taboo/stopw 0, engquote 1 (blokcitaat Santa-Clara). `--check` PASS,
`--where` leeg. Sync en offline-uitvoering zonder fouten.

Kopjes ongewijzigd, behalve "Hoe u zelf werkt" → "Werken met de code". Imports-cel van het
Overzicht naar het begin van "De data" (Overzicht zonder code, §11.7); celvolgorde gelijk.

Geschrapt: alinea "epistemische status/gereedschapskist" (herhaling); lijst Engelse vaktermen
(staat in index en STYLE); `jupyter book start/build`-regels (geen vraag van de lecture);
$R^2$-bijzin (niet herleidbaar); "Deel IV"-vooruitverwijzing.

Wijzigingen: Overzicht met vraag, antwoord (11,6%, SE 1,8), lijst van vijf, alinea herkomst.
Motieven onder hun vaste namen, met één zin vooraf die zegt wat elk betekent, en uitleg waarom
de naam "2%" is (20/√100) terwijl de markt 1,8 geeft. Citaat als blokcitaat met Nederlandse
inleiding. De trap nu drie treden (toy, simulatie, replicatie), theorie ertussen, met
routekaart, Samengevat en imports-cel bij het toy-voorbeeld; "39 andere lectures" (was 37).
Leeszin bij `eq-setup-euler`. Elke codecel heeft een zin ervoor en erna; elke figuur een
leeswijzer ervoor. Intuïtie van de eerste meting als handeling met voorspelling (H1, H12).
Oefeningen eindigen met "Wat dit leert:".

`nb_outputs`-diff tegen HEAD (alle aangehaalde getallen gelijk, 11,6% / 1,8 ongewijzigd):
- cel 3 (fig-setup-french): figuur met annotatie diepste terugval 83,7% (06-1932), maakt het
  getal in het bijschrift herleidbaar.
- cel 13 (fig-setup-osap): legenda "212 signalen, mediane t-waarde 4,0", idem.
- cel 15 (fig-setup-hkm): annotatie laagste punt 2,2% (02-2009); getal aangehaald in L32.
- cel 23 (ex-setup-1): twee rijen erbij, standaardfout en $t$ uit de verschilreeks (0,0276;
  0,9883); kolomnamen "ongecorreleerd". Herstelt een fout: de oude uitwerking zei dat de
  nulcorrelatie-aanname de standaardfout te klein maakt; bij correlatie 0,44 is ze te groot.
- Alle andere cellen identiek.

§11.9 niet van toepassing (opdracht): toy/theorie/Samengevat/simulatie/replicatie-structuur.
Labels: geen verdwenen of verhuisd; elders wordt alleen `00-00-setup` aangehaald.

Open: (1) de annotatie in fig-setup-french raakt de lijn rond 1940 licht; cosmetisch.
Nieuwe getallen in de tekst (18,5/40,2 en 4,3%/1,1% CAPE en dp; VIX 9266, 17,6, 82,7; HKM
~7,5%; simulatie 8,5%, 4,5–12,4%; oefeningen 2,7/3,7/2,8, 3,0/2,2, 1350/675) komen alle uit
getoonde celuitvoer.

## F4
Eindmeting: words 4505 (was 4213), gt40 1, dash 0, semicol 6, overige 0; `--check` PASS,
`--where` leeg. Sync en offline-uitvoering zonder fouten.
Feiten (7 open, alle opgelost): "veertig jaar" weg ("zijn loopbaan"); motieven, opbouw,
Samengevat en imports-cel als opzet van de reeks geformuleerd; data "in de regel" via `hap.data`,
twee lectures halen zelf een bestand op; `hap.fred`: maanddata op begin van de maand en rentes
in procenten; notatie: $r$ netto simpel, $R^f$ netto (0,02), $R^e = r - R^f$, logrendement eigen
symbool ($\ell$), logs met aankondiging; "acht" nu "acht bronnen van `hap.data`" (klopt met
`src/hap`; index.md noemt er zeven, buiten mijn grenzen).
Lezerspunten: 1–14 opgelost. 1 dagdata: één regel (gemiddelde hangt alleen van begin- en
eindkoers af, variantie wordt scherper per waarneming); 2 Overzicht belooft nu "hoe slecht een
eeuw het gemiddelde meet"; 3 drie gevolgen als lijst, elk met schakel; 4 de 8% is excess,
dicht bij `Mkt-RF` (8,3%, 18,4%); 5 `dp`: Shiller $D/P$ niveau, Goyal-Welch log, één naam
"(log) dividendrendement"; 6 verhouding $\sigma/\mu$ (2,5); 7 $\sigma/\sqrt{2T}$ = 1,4 pp in tekst;
8 helling 0,042 en de stap hoge D/P = lage prijs; 9 bias omhoog, geldt ook voor $t$ = 0,95;
10 opbouw als lijst van kopjes; 11 `hap.X` = `hap_data.X` = `hap.stats.X`; 12 ratio i.p.v.
balans, "verklaren"; 13 Fama/Shiller en "goedkoop" = lage prijs t.o.v. dividend; 14 long-short
uitgelegd, signaal = voorspeller = anomalie. Afgewezen: 15 (eindwaarde en meetkundig gemiddelde
zijn het onderwerp van de volgende lecture). Ook let-op-zinnen vóór figuren Shiller, OSAP, Yahoo.
Betaald met schrappen: marge-zin French, Yahoo-limieten, slot "De volgorde is een keuze".
Navertel-toets: "De rode draad" (Santa-Clara nu expliciet geen vierde motief maar de kant van
risico of vergissing die een belegger voelt; keten asymmetrie → drie gevolgen uitgeschreven) en
"Een eerste meting" (belofte Overzicht aangepast; mechanisme fijnere data in één regel).
`nb_outputs`-diff: als F1, plus cel 7 (figuurtitel "Log dividendrendement"). Aangehaalde
getallen 11,6%, 1,8 en 2,2% ongewijzigd. Open: annotatie fig-setup-french (cosmetisch).

## F5-1
Eindmeting: words 4998, gt40 1, semicol 8, dash 0, overige 0; `--check` PASS, `--where` leeg; sync en offline-uitvoering zonder fouten.
Feitelijke fouten: (1) Yahoo gedaan: datacel toont nu gemiddelde, volatiliteit en SE per ETF (2005–); figuurtekst: SE 3–5 pp, QQQ–TLT 12,5 steekt uit, SPY/GLD/IWM binnen één pp. (2) Begin-/eindkoers gedaan: geldt voor het gemiddelde logrendement, rekenkundig ligt een halve variantie hoger.
Top 3: (1) replicatie gedaan: replicatieblok (vijf onderdelen), tabel simulatie/data op `Mkt-RF` (formule 1,84; Newey-West 12 mnd 1,97), oordeel "Geslaagd", zin dat `Mkt` dezelfde SE 1,8 heeft. (2) Helderheid gedaan: notatie noemt bruto $R$ en netto $R^f$ expliciet, $R^e = R-(1+R^f) = r-R^f$; Stambaugh-bias met mechanisme en cite; equity premium puzzle in één zin (MehraPrescott1985); T=100 uitgelegd. (3) Yahoo-leeswijzer sluit aan; Nederlandse kolomnamen in alle `summary_stats`-tabellen.
Opbouw: open vraag in "Waar we zijn" gelijk aan Overzicht (gedaan); slotalinea "De data" met wat de acht figuren leren (gedaan); GSW en HKM gekoppeld aan risico of vergissing (gedaan); terugverwijzing naar de regressie vanuit "Een eerste meting" (gedaan).
Taal: "De standaard is niveaus" → "Zonder aankondiging zijn alle grootheden niveaus"; opzet-zin herschreven; "Let op" van 7 naar 1; "waar gemiddelde" → "werkelijk gemiddelde" (alle gedaan).
Toy: tabel formule/simulatie (2,00/2,00; 1,41/1,42); herkomst $\sigma/\sqrt{2T}$ in oefening 2.3 (deltamethode); zin "wat we nu weten" (gedaan).
Code: kommaopmaak één benoemde helper `number_nl`; `maturities` naar de figuurcel; kolomnamen Nederlands (gedaan).
Oefeningen: 2.3 is nu een afleiding; uitwerking met maanddata ≈ 56 jaar (gedaan).
Afgewezen: geen.
`nb_outputs`-diff tegen HEAD, extra t.o.v. F4: cel 2 kolomnamen; cel 11 begint met `maturities`; cel 16 ETF-statistieken i.p.v. eerste/laatste koers; cel 19 labels; cel 20 tabel formule/simulatie; nieuwe cel 22 replicatie; celnummers oefeningen +1; cel 26 rij "idem, met maanddata" 56,3. Getallen 11,6%, 1,8, 2,2%, 83,7%, 4,0 ongewijzigd.
Open: annotatie fig-setup-french raakt de lijn licht (cosmetisch).
Controle 1 (8,9): `number_nl` van de verborgen cel `cel-setup-french` naar de zichtbare imports-cel, met één zin uitleg erna; uitvoer identiek (alleen de celkop van cel 3 in `nb_outputs` verschuift).
`fig-setup-gsw`: dubbele slotzin herschreven tot "Ook daar is de vraag risico of vergissing."; `--check` PASS, 4997 woorden.
Diffcontrole (1): equity premium puzzle koppelt nu 6,18% aan {cite:t}`MehraPrescott1985` en 8,3% aan de eigen French-data; de oude "ongeveer 8%" met die citatie is weg.
Diffcontrole (2): kalibratie simulatie: 8% dicht bij 8,3% van `Mkt-RF`, 20% een ronde kalibratie iets boven de gemeten 18,4%. Geen code gewijzigd; `--check` PASS (5014 woorden), sync gedaan.

## F6-1
Eindmeting: words 5028, `--check` PASS, `--where` leeg; sync en offline-uitvoering zonder fouten; `nb_outputs` identiek aan vóór F6 (11,6%, 1,8 en 2,2% ongewijzigd).
Fout 1 / naad 6 (Yahoo-cache): zin herschreven naar de werkelijke cache: vijf ETF's, vijftig afzonderlijke aandelen (L7), enkele beleggingsfondsen en indexreeksen, twee optie-snapshots van SPY; "na 1993" vervangen door "dagkoersen van afzonderlijke effecten". Klopt met de negen `yahoo*`-bestanden in `data/cache/`.
Fout 2 (oefening 2): "na de oorlog" → "tussen de eerste en de tweede halve eeuw", passend bij de splitsing 1926–1975 / 1976–2026.
Naad 8: setup gebruikt nu "overlevers", zoals L5. STYLE §3 schrijft geen vorm voor; gekozen voor de vorm die de reeks al het vaakst gebruikt.
Naad 9: setup houdt "empirische finance"; STYLE §3 houdt vaktermen Engels waar vertaling gekunsteld is, en "financiering" betekent *financing* (calque, §11.4). De correctie hoort in L7 r. 1008, buiten mijn grenzen.
Naden 1–5 en 7: de setup-regels kloppen; de afwijkingen staan in L5 en L7, en moeten daar opgelost worden. Niet in de setup gewijzigd.
Naad 8, bijgesteld: L5 gebruikt nu "overlevenden"; de setup is daarop gelijkgezet. `--check` PASS, sync gedaan.
Diffcontrole Yahoo-zin: "enkele beleggingsfondsen" → "twee groepen beleggingsfondsen (59 en 8 fondsen)", nageteld in de twee cachebestanden; `--check` PASS, sync gedaan.
Eindcontrole: "De cache begint in 1993" → "De ETF-reeks begint in 1993" (eerste datum 1993-01-29 in het ETF-cachebestand); `--check` PASS, sync gedaan.

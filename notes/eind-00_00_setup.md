STATUS 00_00_setup F6c words=5424 prose=PASS open=0 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: Vorig: 8,6. Ronde 9+: T, F6 8,9 (3 feitfouten) -> F6c 9,0. Het cijfer onder de kop "F6, vóór herstel" is dus niet het eindcijfer.

# Ronde 9+

Vorige ronde: 8,6

Eindbeoordeling F6 van `lectures/00_00_setup.md` (Opzet, data en conventies), met verse ogen
na de taalredactie. `prose_stats --check`: PASS (5366 woorden, zinnen gemiddeld 17,3, p90 28,
2 zinnen > 40, alinea gemiddeld 47, dubbele punt 2,2 per 1000, `wie_open` 1, `tmpl` 1).
Criterium 4 heeft in de setup geen eigen kopje; het wordt beoordeeld op het equivalent: de
ronde rekensom $20/\sqrt{100}$ (r. 78–82) en de ene gesimuleerde eeuw (r. 832–856).
Onderzoeken: alleen onderzoek A noemt dit college; B–E niet. De A-punten bij r. 66–71,
104–105, 368–369 en 1120 zijn door de redactie opgelost; de punten hieronder gelden nog.

## De drie verbeteringen met het meeste effect

1. **Taal: het leeswijzersjabloon en vier hardop-zinnen herschrijven** (8,7 → 9,0). "Het
   gaat erom" / "gaat het erom/om" staat vier keer als leeswijzer (r. 371–372, 421–422,
   611–612, 675–676) [onderzoek A, P2]; daarnaast de zinnen op r. 116–118, 645–646, 821 en
   1063 (zie hardop-toets onderaan).
2. **Helderheid: de Stambaugh-stap en twee kleine slordigheden** (8,8 → 9,0). In het
   bijschrift r. 444–446 ontbreekt de schakel waarom onderschatte persistentie de helling
   omhoog trekt; r. 829 schrijft $0{,}20/\sqrt{200} = 1{,}4$ procentpunt (eenhedenwissel);
   r. 95 zegt "boven 1,96" waar $|t| > 1{,}96$ bedoeld is.
3. **Replicatie: getallen uit het oordeel naar de tabel** (8,8 → 9,0). Het oordeel
   (r. 974–979) bevat zes getallen in één alinea, waarvan 11,6% niet in de tabel staat, en
   de tabelrij "standaardfout, spreiding of Newey-West" (r. 970) stopt twee verschillende
   grootheden in één rij.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,9

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,8 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 8,7 |
| 4 | Toy-voorbeeld (equivalent) | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 8,8 |
| 7 | Oefeningen | 5% | 9,0 |

0,25·8,8 + 0,20·9,0 + 0,20·8,7 + 0,10·9,0 + 0,10·9,0 + 0,10·8,8 + 0,05·9,0 = 8,87 → **8,9**.
Laagste deelcijfer 8,7 (taal). Geen deelcijfer onder 8,5; taal ≥ 8, dus niet blokkerend.
Doel 9,0 niet gehaald. (Zonder criterium 4, herwogen over 90%: 8,86 → 8,9; zelfde cijfer.)

## 1. Helderheid van de uitleg (8,8)

*Goed*
- **De rode draad → De standaardfout van 2%.** Het motief krijgt meteen zijn rekensom
  ($20/\sqrt{100} = 2$) en drie gevolgen met getallen (6,18% en 8,3%; één op de twintig).
- **Notatie.** De dubbele conventie ($R$ bruto, $R^f$ netto) krijgt 1,08 en 0,02, en de
  tijdsindexregel krijgt een reden (vooruitkijken, "veel te mooie resultaten").
- **Een eerste meting.** De asymmetrie gemiddelde/variantie wordt verklaard met
  $\sigma/\mu = 2{,}5$ en met het logverschil tussen eind- en beginkoers (r. 915–923).

*Aanmerkingen*
- **Goyal-Welch, bijschrift.** "Omdat de persistentie in een korte steekproef te laag
  wordt geschat, is de helling naar boven vertekend en de $t$-waarde te groot." De
  negatieve correlatie staat er nu (r. 443–444), maar de schakel van onderschatte
  persistentie naar een opwaartse helling niet.
- **Een eerste meting.** "$\SD(\hat\sigma) \approx \sigma/\sqrt{2T} = 0{,}20/\sqrt{200}
  = 1{,}4$ procentpunt" — links een decimaal, rechts procentpunten.
- **De rode draad.** "omdat van twintig nutteloze factoren er gemiddeld één toevallig een
  $t$-waarde boven 1,96 haalt." Eén op twintig geldt voor $|t| > 1{,}96$.

*Beter uitleggen*
- De Stambaugh-bias: één bijzin dat de regressie de te lage persistentie "corrigeert" via
  de negatief gecorreleerde schok, zodat de helling omhoog schuift.
- "Niet cumulatief" (r. 66) zegt de lezer weinig; een voorbeeld (het CAPM verdwijnt niet
  als de factor zoo komt) maakt het concreet.

*Voor een 9*
- `lectures/00_00_setup.md:444-446` Stambaugh-schakel in één bijzin.
- `lectures/00_00_setup.md:829` eenheden gelijk trekken ($0{,}20/\sqrt{200} = 0{,}014$).
- `lectures/00_00_setup.md:95` "in absolute waarde boven 1,96".

## 2. Opbouw en rode draad (9,0)

*Goed*
- **Overzicht** stelt de vraag en geeft meteen het antwoord (11,6%, standaardfout 1,8).
- **Een eerste meting** voorspelt ("Waarom zou een eeuw data zo weinig zeggen?") en lost
  in met dezelfde getallen (8%, 20%, 18,4%) in formule, simulatie en data; de regressie uit
  de gereedschapskist keert terug (r. 925–927).
- **De data** sluit af met drie lessen uit de acht figuren (r. 736–740); lengte 5366 woorden.

*Aanmerkingen*
- **Waar we zijn / Overzicht.** "Hoe is de reeks opgebouwd? Hoe goed meten we met de data
  van de reeks het gemiddelde rendement op aandelen?" staat vrijwel woordelijk opnieuw in
  de eerste zin van het Overzicht (r. 37–38) [onderzoek A].

*Beter uitleggen*
- Geen inhoudelijk gat; het Overzicht kan de vraag parafraseren in plaats van herhalen.

## 3. Taal (8,7)

*Goed*
- **De data.** De bronbeschrijvingen lezen als gesproken tekst, met voegwoorden en zonder
  telegramzinnen; ritme 17,3 woorden met afwisseling.
- **Wat er daarna komt.** Korte, natuurlijke overgang met een concrete vraag voor het
  volgende college.

*Aanmerkingen*
- **De data (leeswijzers).** "Het gaat erom hoe lang de reeks boven of onder die lijn
  blijft." (r. 371–372); "In de figuur gaat het erom of `dp` over jaren of over decennia
  beweegt." (r. 421–422); "daarin gaat het om het laagste punt en de recessie waarin dat
  punt valt." (r. 612); "gaat het erom welke verschillen tussen de lijnen groter zijn dan
  de standaardfouten." (r. 675–676) — vier keer dezelfde wending (§11.12) [onderzoek A, P2].
- **De rode draad.** "Zijn blijvende winst kwam uit het dragen van risico waarvoor de markt
  een premie betaalde, terwijl zijn verliezen kwamen uit de gedachte iets te weten wat de
  prijs niet wist." "Zijn" kan op "een belegger" (r. 115) slaan [onderzoek A, 113–116].
- **He-Kelly-Manela.** "Zo leest de risicokant een crash, terwijl de vergissingskant in
  dezelfde lage prijzen paniek ziet." Kampen als "kant" die leest, dicht bij motief als
  handelend onderwerp.
- **Oefeningen (ex-setup-1).** "Wie een rangorde van gemiddelde rendementen serieus neemt,
  neemt dus vooral ruis serieus." Engelse chiasme [onderzoek A, 1057–1058].
- **Een eerste meting.** "Hoe fijn de onderzoeker binnen een jaar kijkt, helpt voor het
  gemiddelde niet." en "2 procentpunt, de naam van het motief." (regeltaal-achtig).
- **Motiefnaam.** "de standaardfout van 2%" staat vier keer bij naam (r. 74, 78, 933, 978);
  de setup mag ze invoeren, maar r. 933 en 978 kunnen zonder naam.

*Beter uitleggen*
- Niet van toepassing buiten de zinnen hierboven; de redactie heeft de grote knippen en
  dubbele punten weggewerkt.

*Voor een 9*
- `lectures/00_00_setup.md:371,421,612,675` leeswijzers elk anders formuleren (vraag,
  "let op", of de bewering zelf).
- `lectures/00_00_setup.md:116-118,645-646,821,1063` de vier hardop-zinnen herschrijven.
- `lectures/00_00_setup.md:828,978` motiefnaam en "de naam van het motief" vervangen door
  wat er gemeten is.

## 4. Toy-voorbeeld, equivalent (9,0)

*Goed*
- **De rode draad.** $20/\sqrt{100} = 2$ is in tien seconden na te rekenen, één mechanisme.
- **Een eerste meting.** De ene eeuw (8,5%, 2,0, interval 4,5–12,4) en de tabel
  formule/simulatie werken als hand/code-controle; dezelfde getallen keren terug in de data.

*Aanmerkingen*
- Geen.

*Beter uitleggen*
- Niets nodig.

## 5. Code en figuren (9,0)

*Goed*
- Elke cel heeft een zin ervoor en erna; vóór elke figuur staat waarop te letten.
- De simulatiecode leest als de wiskunde (`se_mean_formula`, `se_sd_formula`).
- `number_nl` zorgt voor Nederlandse decimalen in figuren.

*Aanmerkingen*
- **Een eerste meting.** `fig-setup-se` heeft als enige figuur geen `:width:` (r. 906–908)
  [onderzoek A].
- **Gürkaynak-Sack-Wright.** "De figuur tekent voor dezelfde drie dagen de hele curve tot
  dertig jaar" — voor 1981 ontbreken de lange looptijden, en `range(1, len(curve) + 1)`
  veronderstelt stilzwijgend dat alleen het staartstuk ontbreekt.

*Beter uitleggen*
- Eén bijzin bij de GSW-figuur dat de curve van 1981 korter is.

## 6. Replicatie en empirie (8,8)

*Goed*
- Admonition compleet (bron, wat, data, verschil, verwachte afwijking) en kort.
- Oordeel begint met **Geslaagd** en verwijst naar "enkele tienden".
- Twee standaardfouten (formule en Newey-West) naast de simulatie.

*Aanmerkingen*
- **Replicatie (oordeel).** "Op de data geeft de formule 1,8 procentpunt en Newey-West 2,0,
  binnen de verwachte afwijking van enkele tienden. Het gemiddelde overrendement van 8,3%
  is dus op ongeveer 2 procentpunt na bekend. Het totale marktrendement `Mkt` heeft
  dezelfde standaardfout, 1,8 procentpunt bij 11,6%, ..." Zes getallen in lopende tekst.
- **Replicatie (tabel).** Rij "standaardfout, spreiding of Newey-West": in de ene kolom de
  spreiding over simulaties, in de andere Newey-West.

*Beter uitleggen*
- De lezer moet uit de rijnaam afleiden welke grootheid in welke kolom staat.

*Voor een 9*
- `lectures/00_00_setup.md:969-970` twee aparte rijen (spreiding simulatie; Newey-West), eventueel een rij voor `Mkt`.
- `lectures/00_00_setup.md:974-979` oordeel terugbrengen tot hoogstens drie getallen.

## 7. Oefeningen (9,0)

*Goed*
- ex-setup-2 varieert op de rekensom (jaren voor 0,5 pp) en bevat de afleiding van
  $\sigma/\sqrt{2T}$; ex-setup-1 breidt de data-meting uit.
- Beide uitwerkingen eindigen met wat ze leren (r. 1062–1064, 1137–1140).

*Aanmerkingen*
- **ex-setup-1, uitwerking.** Taalpunt r. 1063 (zie criterium 3); de $t$-waarde uit de
  verschilreeks is 0,99, "onder één" klopt maar nipt.

*Beter uitleggen*
- Niets nodig.

## Feitelijke fouten

Nagerekend met `HAP_OFFLINE=1` op de cache (script `$TEMP/F6-00_00_setup-check.py`).

1. **r. 94–95** "een $t$-waarde boven 1,96": bij één op twintig hoort $|t| > 1{,}96$
   (tweezijdig); eenzijdig is het één op veertig.
2. **r. 510–512** "de hele curve tot dertig jaar": op 30-09-1981 is `SVENY30` leeg, dus die
   curve stopt eerder.
3. **r. 829** "$0{,}20/\sqrt{200} = 1{,}4$ procentpunt": uitkomst is 0,014 (= 1,4 pp);
   notatiefout, geen rekenfout.

Nagerekend en juist: `Mkt` 11,6% / 18,3% / SE 1,8 pp over 1201 maanden; interval 8–15%;
`Mkt-RF` 8,3% / 18,4%; RF-standaardfout 0,09 pp; terugval 83,7% in juni 1932; CAPE 18,5 →
40,2 (40,15), gemiddelde 17,8; `dp` 4,3% → 1,1%; GW-`dp` −4,2 tot −4,5; helling 0,042, SE
0,044, $t$ 0,95, 100 waarnemingen, 155 jaar, `equity_premium` vanaf 1926; VIX 9266 dagen,
mediaan 17,6, max 82,7; GSW 15,7% en 0,13%; OSAP 212 signalen, mediane $t$ 4,0, eerste 1973;
HKM ~7,5% voorjaar 2025, minimum 2,2% februari 2009; alle vijf ETF's vanaf november 2004;
ETF-standaardfouten 3,1–5,2 ("3 tot 5" is afgerond); SPY/GLD/IWM binnen 0,9 pp; QQQ−TLT
12,5 pp; eeuw 8,5%, 2,0, [4,5; 12,4]; simulatie 2,0 en 1,4; Newey-West 2,0; Energie−Telecom
2,7 pp, SE 3,7 en 2,8, $t$ 0,99; helften SE 3,0 en 2,2, $t$ −0,2; 1350, 675 en 56 jaar.
De twee fouten uit de vorige ronde (Yahoo-cache, "na de oorlog") zijn opgelost.

## Navertelling in vijf zinnen

1. De reeks vertelt de geschiedenis van asset pricing als een opeenvolging van theorie,
   nieuwe data en een feit dat de theorie niet aankan, met drie terugkerende motieven.
2. Alle colleges delen één notatie ($R$ bruto, $R^f$ netto, $m_{t+1}$, tijdsindex $t+1$ voor
   payoffs) en één vaste opbouw van toy via theorie en simulatie naar replicatie.
3. Acht gratis bronnen, offline uit een cache, dekken de data; CRSP en Compustat ontbreken,
   zodat de reeks op French- en OSAP-portefeuilles en op simulatie leunt.
4. Het `hap`-pakket levert de standaardschatters en figuurhulpjes, en een eerste regressie
   laat zien dat een juist teken met een te grote standaardfout niets bewijst.
5. Na een eeuw is het gemiddelde overrendement (8,3%) maar op ongeveer 2 procentpunt na
   bekend en de volatiliteit veel scherper, wat formule, simulatie en data alle drie bevestigen.

Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft gewerkt: de telegramzinnen en dubbele punten als lijm uit de vorige ronde
zijn weg, de meeste alinea's lezen hardop als een college. Wat overblijft is een
sjabloonwending in de leeswijzers ("het gaat erom", vier keer) en een handvol zinnen die
geschreven klinken.

Hardop-toets (drie zinnen die nog niet natuurlijk klinken):

1. r. 116–118 "Zijn blijvende winst kwam uit het dragen van risico waarvoor de markt een
   premie betaalde, terwijl zijn verliezen kwamen uit de gedachte iets te weten wat de prijs
   niet wist." → "Santa-Clara verdiende blijvend aan risico waarvoor de markt een premie
   betaalde, en hij verloor telkens wanneer hij dacht iets te weten wat nog niet in de prijs
   zat."
2. r. 821 "Hoe fijn de onderzoeker binnen een jaar kijkt, helpt voor het gemiddelde niet."
   → "Voor het gemiddelde helpt het niet om binnen een jaar vaker te meten."
3. r. 645–646 "Zo leest de risicokant een crash, terwijl de vergissingskant in dezelfde lage
   prijzen paniek ziet." → "In die lezing is een crash een moment waarop risico duurder
   wordt, terwijl Shiller in dezelfde lage prijzen paniek ziet."

## Controle 1

Controle F6c op R9-1 (notes/rapport-00_00_setup.md), na lezing van het hele college.

**Feitelijke fouten (3/3 opgelost)**
1. r. 94–95 "boven 1,96" → **opgelost**: "een $t$-waarde ... die in absolute waarde boven 1,96 ligt."
2. r. 510–512 GSW-curve "tot dertig jaar" → **opgelost**: tekst zegt nu "tot dertig jaar in 2020 en 2026 maar tot twintig jaar in 1981"; code leest de looptijd uit de kolomnaam (`years = [int(name[-2:]) for name in curve.index]`) in plaats van `range(1, len(curve)+1)`, dus de figuur telt niet langer stilzwijgend door bij ontbrekende lange looptijden.
3. r. 829 eenheden "$= 1{,}4$ procentpunt" → **opgelost**: "$= 0{,}014$, dus 1,4 procentpunt".

**Verbetering 1, taal — leeswijzersjabloon en hardop-zinnen (opgelost)**
De vier "het gaat erom"-leeswijzers (Shiller, Goyal-Welch, HKM, Yahoo) zijn elk anders
geformuleerd (geen sjabloon meer). De vier hardop-zinnen (Santa-Clara r. 123–125,
HKM r. 664, "Een eerste meting" r. 850–851, ex-setup-1 r. 1096–1097) zijn woordelijk
herschreven zoals de hardop-toets voorstelde. Geen nieuw sjabloon zichtbaar (`prose_stats`
`tmpl=0`); `sent_gt40=2`, ongewijzigd t.o.v. F6.

**Verbetering 2, helderheid — Stambaugh-schakel en twee slordigheden (opgelost)**
Het GW-bijschrift legt nu de schakel expliciet: "Door die tegengestelde beweging valt de
geschatte helling juist te hoog uit in steekproeven waarin de persistentie te laag uitvalt."
r. 829 en r. 95 zijn opgelost (zie Feitelijke fouten 1 en 3, die met deze twee samenvallen).

**Verbetering 3, replicatie — getallen uit het oordeel naar de tabel (opgelost)**
Tabelrij "standaardfout, spreiding of Newey-West" is gesplitst in twee rijen (spreiding
over simulaties; Newey-West, elk met `NaN` waar niet van toepassing). Het oordeel noemt nu
drie getallen (1,8; 2,0; 2 procentpunt) in plaats van zes, en verwijst niet meer naar 11,6%.

**Overige aanmerkingen/Beter uitleggen (alle opgelost)**
- Criterium 1: "niet cumulatief" heeft nu het CAPM/factor-zoo-voorbeeld in dezelfde zin.
- Criterium 2: Overzicht herhaalt de vraag uit "Waar we zijn" niet meer letterlijk, maar
  parafraseert ("laat zien hoe de reeks in elkaar zit" / "doet meteen de eerste meting").
- Criterium 3: Santa-Clara-zin, He-Kelly-Manela-zin, ex-setup-1-chiasme en de twee zinnen bij
  "Een eerste meting" zijn herschreven; motiefnaam weg uit Bron en oordeel van de replicatie
  (blijft twee keer in de definiërende alinea's van De rode draad, vrijgesteld).
- Criterium 5: `fig-setup-se` heeft nu `:width: 90%`; de GSW-figuurcode is root-cause gefixt
  (kolomnaam i.p.v. `range`), zie Feitelijke fout 2.
- Criterium 6: zie Verbetering 3.
- Criterium 7: ex-setup-1 zegt nu "net onder één" i.p.v. "onder één".

Geen nieuwe punten: geen verslechtering en geen nieuwe feitelijke fout aangetroffen bij het
navertellen en de hardop-toets. `prose_stats --check`: PASS, 5424 woorden.

**Eindcijfer: 9,0**

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld (equivalent) | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |

Alle deelcijfers 9,0 → gewogen eindcijfer **9,0**. Geen deelcijfer onder 8,5; taal 9,0, niet
blokkerend. Doel 9,0 gehaald.

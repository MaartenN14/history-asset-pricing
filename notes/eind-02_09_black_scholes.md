STATUS 02_09_black_scholes F6c words=5870 prose=PASS open=0 cijfer=9,0 min=9,0

# Ronde 9+

Vorige ronde: 8,7

Eindbeoordeling (F6) van `lectures/02_09_black_scholes.md` na de taalredactie. Gelezen:
alleen de .md, één keer volledig. `prose_stats --check`: PASS (5.717 woorden, zinnen
gemiddeld 17,3, één zin boven 40, `colon_mid` 1,4, `wie_open` 2). Doel (9,0, niets onder
8,5) niet gehaald: het eindcijfer blijft 8,7. Er zijn geen feitelijke fouten; wat
ontbreekt is afwerking op helderheid, taal, code en replicatie.

## De drie verbeteringen met het meeste effect

1. **Taal: de drie resterende stroeve zinnen herschrijven en de sjabloonzin "niet tegen
   de bron te houden" (drie keer) vervangen door wat er echt vergeleken wordt**
   (`02_09_black_scholes.md:66`, `:723`, `:855`, `:1024`, `:1115`), en daarnaast "euro"
   door "dollar" waar het om Amerikaanse opties gaat (`:74`, `:543`, `:797`). Taal van
   8,5 naar 9. [onderzoek E]
2. **Helderheid: de kernzin van de delta-hedge corrigeren en de factor $\sqrt{\pi/2}$
   verklaren.** "Met de schok verdwijnt ook de verwachting van de schok, en daarmee
   $\mu$" (`:307`) klopt niet: de schok $\mathrm{d}W$ heeft verwachting nul, en wat
   verdwijnt is de verwachte koersstijging $\mu S\,\mathrm{d}t$ van de aandelen die
   tegenover de optie staan. Daarnaast ontbreekt bij `:668` één bijzin over waar
   $\sqrt{\pi/2}$ vandaan komt. Helderheid van 8,5 naar 9. [onderzoek E]
3. **Replicatie: zeggen wat wel en niet vergeleken is, in plaats van "hun getallen zijn
   niet tegen de bron te houden".** Bij de VRP (`:1024`) en de smirk (`:855`) in één
   zin zeggen waarom niveaus niet vergelijkbaar zijn (andere periode, ander instrument),
   zodat de verwachte afwijking een reden krijgt en geen werkmelding lijkt. Replicatie
   van 8,5 naar 9.

Met deze drie wordt het gewogen cijfer 0,25·9 + 0,2·9 + 0,2·9 + 0,1·9 + 0,1·8,5 +
0,1·9 + 0,05·9 = 8,95, dus 9,0; met ook de codepunten (criterium 5) 9,0 zonder
afronding.

## Eindcijfer: 8,7

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 9 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 8,5 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,125 + 1,80 + 1,70 + 0,90 + 0,85 + 0,85 + 0,45 = 8,675, dus 8,7. Laagste
deelcijfer 8,5; taal blokkeert niet.

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- Opzet en aannames: de vier afwijkingen van de notatietabel ($S_t$, $R^f$ bruto per
  stap, $r$ continu, $d$ als daalfactor en $\delta$ als dividend) staan nu samen in één
  alinea; de aanmerking uit de vorige ronde over $d$ is opgelost.
- Wat het voorspelt: de risiconeutrale kansmaat wordt nu teruggekoppeld aan de maat $Q$
  uit [](#thm-efficiente-markten-martingaal) en aan $q = 0{,}6$ uit de boom; de lezer
  hoeft niets opnieuw te leren.
- Wat een hedger verdient: de benadering vega maal $\sigma_i - \sigma_g$ krijgt een
  afleiding in één zin en een getal (0,99), dat in oefening 2 terugkomt.

*Aanmerkingen*
- Het kernresultaat: de delta-hedge: "Met de schok verdwijnt ook de verwachting van de
  schok, en daarmee $\mu$." De verwachting van $\mathrm{d}W$ is nul; $\mu$ is de drift
  van het aandeel, niet de verwachting van de schok. [onderzoek E]
- Simulatie: "Maal de vega is die standaardfout, op een factor $\sqrt{\pi/2}$ na, de
  spreiding van de P&L." De factor wordt genoemd, niet verklaard (al aanmerking in de
  vorige ronde).
- Het kernresultaat (note): "met "mkt" de markt (de letter $m$ is in de reeks de SDF)".
  "SDF" wordt pas in het slot (`:1143`) uitgelegd, en daar als Engelse *stochastic
  discount factor*, terwijl de reeks "stochastische discontofactor" gebruikt.
  [onderzoek E]
- Intuïtie: "Uit deze redenering volgen drie verwachtingen." In dit vak betekent
  "verwachting" een verwachte waarde; "voorspellingen" is eenduidig. [onderzoek E]

*Beter uitleggen*
- Waarom $\mu$ verdwijnt: één bijzin dat de verkochte $\Delta$ aandelen precies de
  verwachte stijging $\mu S C_S\,\mathrm{d}t$ van de optie tegenover zich hebben.
- De factor $\sqrt{\pi/2}$: de handelaar verdient of verliest per interval met
  $|\mathrm{schok}|$, en $\E|Z| = \sqrt{2/\pi}$ voor een standaardnormale $Z$; één
  bijzin volstaat.

*Voor een 9*
- `02_09_black_scholes.md:307` de zin over "de verwachting van de schok" corrigeren.
  [onderzoek E]
- `02_09_black_scholes.md:666-669` de oorsprong van $\sqrt{\pi/2}$ in een bijzin.
- `02_09_black_scholes.md:344` "SDF" vervangen door "stochastische discontofactor", en
  `:1143` dezelfde term gebruiken. [onderzoek E]
- `02_09_black_scholes.md:94` "verwachtingen" wordt "voorspellingen". [onderzoek E]

### 2. Opbouw en rode draad (9)

*Goed*
- Overzicht stelt de vraag en geeft meteen het antwoord (namaken, afhankelijk van
  volatiliteit, niet van verwacht rendement of risicoaversie).
- De drie voorspellingen uit de Intuïtie worden elk ingelost: $\mu$ ontbreekt in de PDE
  (`:335`), de P&L is gemiddeld vrijwel nul en daalt met $1/\sqrt{N}$ (`:819`), en de
  implied volatility is niet vlak (`:945`).
- Getallen reizen mee: $\Delta_0 = 0{,}624$ en $0{,}648$ uit de boom in de formule, de
  call van 4,49 van de theorie naar de simulatie en oefening 2; 5.717 woorden, onder de
  6.000.

*Aanmerkingen*
- Overzicht: "Met dit werk begint een nieuw tijdvak, omdat hun formule de eerste
  waarderingsregel is ..." De tijdvakformule klinkt als projectsjabloon. [onderzoek E]
- Wat er daarna kwam: "In 1973 leidde hij er het evenwicht van de hele markt mee af, in
  [](#03-10-merton-icapm)." Het slot eindigt op een link in plaats van op een zin over
  wat er openstaat.

*Beter uitleggen*
- Niets wezenlijks; de rode draad (replicatie, $\mu$ verdwijnt, volatiliteit als enige
  onbekende, en waar dat breekt) is na één lezing te benoemen.

### 3. Taal (8,5)

*Goed*
- De taalredactie heeft de meeste punten van onderzoek E opgelost: "waarderen" in plaats
  van "prijzen", "lags", "correctie van Osborne", "Uit de formule is af te lezen",
  "aandelenpremie", "de variantie in de optieprijs"; "De lezer weet nu" en "Stap 5: ...
  Nergens." zijn weg.
- Intuïtie en "Wat een hedger verdient" lezen hardop als gesproken academisch
  Nederlands, met voegwoorden in plaats van knippen.
- "In woorden:" staat nog twee keer (`:275`, `:413`), binnen de norm.

*Aanmerkingen*
- Overzicht: "Op de vraag theorie of feit luidt het antwoord dat Black-Scholes een
  theorie is die getoetst wordt, maar wel een relatieve theorie." Motief als aangeplakte
  vraag. [onderzoek E]
- Simulatie: "Dit is wel een controle van de code en geen replicatie, omdat de getallen
  van Derman en Kamal niet tegen de bron te houden zijn." Dezelfde formule staat ook in
  het replicatieblok ("de getallen van de bronnen zijn niet tegen de bron te houden",
  `:855`) en bij de VRP ("Hun getallen zijn niet tegen de bron te houden", `:1024`): een
  sjabloonzin met de klank van een werkmelding (STYLE §11.12). [onderzoek E]
- Wat er brak: "Het model gaf de eerste prijs zonder voorkeuren, want uit één argument,
  dat wat zonder risico is de rente verdient, volgt een formule met vier waarneembare
  invoergrootheden en één te schatten getal." [onderzoek E]
- Intuïtie: "vijftig cent ... een euro" (`:74`), en "0,99 euro" (`:543`), "euro per
  optie" (`:797`) bij Amerikaanse opties en Black 1989. [onderzoek E]
- Toy: "We beginnen met de cel die de pakketten laadt, de enige cel van die soort in dit
  college." Restant van regeltaal ("de imports-cel"). [onderzoek E]
- Note bij de delta-hedge: "op elk moment van het leven van de optie" (calque van *life
  of the option*; "looptijd").
- "wij" naast "we": "maar wij volgen" (`:657`), "terwijl wij één dag hebben" (`:852`),
  "wij vergelijken" (`:1030`). [onderzoek E]
- "Itô's lemma" (kop `:253`, stelling `:262`) naast "het lemma van Itô" in de tekst.
  [onderzoek E]
- Simulatie: "de volatiliteit in feite uit $N$ waarnemingen meet" (stopwoord).

*Beter uitleggen*
- Niet van toepassing (taal); zie de hardop-toets onderaan.

*Voor een 9*
- `02_09_black_scholes.md:66`, `:1115`, `:723` herschrijven (zie hardop-toets).
  [onderzoek E]
- `02_09_black_scholes.md:855` en `:1024`: "niet tegen de bron te houden" vervangen door
  wat we vergelijken ("we vergelijken geen niveaus, alleen teken en vorm") met de reden.
  [onderzoek E]
- `02_09_black_scholes.md:74`, `:543`, `:797`: dollar bij Amerikaanse opties.
  [onderzoek E]
- `02_09_black_scholes.md:102` "De eerste cel laadt de pakketten voor het hele
  college." [onderzoek E]
- `02_09_black_scholes.md:345` "gedurende de hele looptijd van de optie".
- `02_09_black_scholes.md:253`, `:262` "Het lemma van Itô". [onderzoek E]
- `02_09_black_scholes.md:657`, `:852`, `:1030` "we". [onderzoek E]

### 4. Toy-voorbeeld (9)

*Goed*
- Toy-voorbeeld: vijf knopen met $\Delta$ en $B$ per stap, met de hand na te rekenen,
  en een tabel hand/code die tot vier decimalen gelijk is.
- Stap 5 en 6 maken het punt scherp: onder $q$ dezelfde prijs, onder $p = 0{,}5$ en
  $p = 0{,}8$ een andere discontovoet per $p$.
- De slotzin zegt wat het getal betekent (10,3603 volgt uit namaken, los van het
  verwachte rendement).

*Aanmerkingen*
- Stap 4: "$C_0 = 0{,}62399 \cdot 100 - 52{,}0388$" naast "$\Delta_0 = \ldots =
  0{,}6240$" in de zin ervoor: twee precisies voor hetzelfde getal.

*Beter uitleggen*
- Niets; de boom is binnen vijf minuten na te rekenen.

### 5. Code en figuren (8,5)

*Goed*
- `delta_hedge_pnl` leest als de boekhouding (premie, delta, financiering, payoff) met
  een zichtbare lus over de hedgemomenten.
- De controlecel na de Greeks (pariteitsresidu, PDE-residu, teruggevonden $\sigma$)
  toetst de theorie in code.
- Elke figuur heeft een leeswijzer ervoor (`:783-785`, `:975`) en een onderschrift dat
  zegt wat te zien is.

*Aanmerkingen*
- Toy-voorbeeld, code: "S0, u, d, R_f, K, n = toy.values()" en in de theorie
  "S_ex, K_ex, T_ex, r_ex, sigma_ex = example.values()": uitpakken op volgorde van een
  dict is een truc.
- Hoe het getoetst wordt: na de cel met `bs_price` en `bs_greeks` volgt geen zin over die
  cel; "De inverse zoekt $\sigma$ met bisectie" gaat al over de volgende cel.
- Replicatie: "De figuur toont vijf looptijden en het hele oppervlak, en daarin loopt
  geen enkele kromme horizontaal." Dat is wat te zien is, niet waarop te letten (hoogte
  en helling per looptijd).

*Beter uitleggen*
- `bs_price` rekent de put via `np.where(kind == "call", call, call - S + K e^{-rT})`;
  één zin dat dit de pariteit is, staat er (`:563`), maar niet dat de functie daardoor
  arrays van soorten aankan, wat de replicatie gebruikt.

*Voor een 9*
- `02_09_black_scholes.md:178`, `:619` de parameters bij naam uitpakken.
- `02_09_black_scholes.md:591` één zin na de Greeks-cel (wat de functies teruggeven).
- `02_09_black_scholes.md:975-976` vóór de smirkfiguur zeggen waarop te letten.

### 6. Replicatie en empirie (8,5)

*Goed*
- Beide replicatieblokken hebben bron, wat, data, verschil en verwachte afwijking,
  elk ruim onder 250 woorden.
- De uitkomst staat in een tabel verwacht/hier, en elk oordeel begint met
  **Geslaagd.** en verwijst naar de verwachting uit het blok.
- Newey-West met 42 lags wordt gemotiveerd door de overlap van 20 van de 21 dagen.

*Aanmerkingen*
- Replicatie (VRP), Wat: "Hun getallen zijn niet tegen de bron te houden, dus we
  toetsen teken en vorm." Whaley en Carr en Wu publiceren niveaus; de reden om ze niet
  te vergelijken (andere periode, S&P 500 tegen de hele markt, variantieswaps tegen de
  VIX) staat er niet.
- Replicatie (smirk), Verwachte afwijking: "want de niveaus hangen van de dag af en de
  getallen van de bronnen zijn niet tegen de bron te houden." De eerste reden volstaat;
  de tweede is een werkmelding. [onderzoek E]
- Geslaagd (VRP): "met een $t$-waarde ver boven twee en op de meeste dagen, maar in 2008
  en 2020 slaat het verschil om." "op de meeste dagen" hangt los.

*Beter uitleggen*
- De eerlijkheid van de simulatie na het schrappen van "Hun tabellen hebben we niet
  kunnen raadplegen": die blijft intact. De tekst beweert nergens dat er met Boyle en
  Emanuel is vergeleken; zij worden alleen historisch genoemd ("analyseerden die
  spreiding als eersten ... maar wij volgen de latere analyse van Derman en Kamal"). De
  enige vergelijking, simulatie tegen de vuistregel van Derman en Kamal, heet expliciet
  "een controle van de code en geen replicatie" (`:723`). Wat nog ontbreekt is de
  positieve formulering: er is vergeleken met hun formule, niet met hun tabel.

*Voor een 9*
- `02_09_black_scholes.md:1024` de reden noemen waarom niveaus niet vergeleken worden.
- `02_09_black_scholes.md:855` alleen "de niveaus hangen van de dag af" laten staan.
  [onderzoek E]
- `02_09_black_scholes.md:723-725` zeggen dat de simulatie met de vuistregel is
  vergeleken en niet met de getallen uit het artikel. [onderzoek E]
- `02_09_black_scholes.md:1078` "op de meeste dagen" als eigen zinsdeel ("en ligt op de
  meeste dagen erboven").

### 7. Oefeningen (9)

*Goed*
- Instap (boom met $K = 110$ en CRR-convergentie), afleiding (verkopen tegen de
  verkeerde volatiliteit) en uitbreiding van de replicatie (VRP in twee periodes): de
  drie rollen volgens de rubriek.
- Elke uitwerking eindigt met wat ze leert (formule is de limiet van de boom; een
  gehedgde optie is een weddenschap op variantie; het meetprobleem geldt niet voor
  tweede momenten).
- Oefening 2 hergebruikt 0,99 en 0,43 uit de theorie en de simulatie.

*Aanmerkingen*
- Oefening 1, uitwerking: "De fout blijft binnen de stippellijnen $\pm 1/n$, want ze
  daalt ongeveer als $1/n$". Het verband is omgekeerd: omdat de fout als $1/n$ daalt,
  blijft ze binnen de lijnen is geen bewijs, alleen een waarneming.

*Beter uitleggen*
- Niets wezenlijks.

## Feitelijke fouten

Geen. Nagerekend: $q = 0{,}6$, $0{,}216$ en $0{,}432$, $C_0 = 10{,}994/1{,}061208 =
10{,}3603$, $q^3 + 3q^2(1-q) = 0{,}648$; de ATM-call ($d_1 = 0{,}15$, $d_2 = 0{,}05$,
$C = 4{,}49$, vega $= 100\,\varphi(0{,}15)\cdot 0{,}5 = 19{,}7$, 0,20 per punt,
$19{,}7 \cdot 0{,}05 = 0{,}99$); de vuistregel ($0{,}886 \cdot 19{,}7 \cdot 0{,}2 /
\sqrt{63} = 0{,}44$; bij Derman en Kamal vega 11,46 en $0{,}4432$; $0{,}4295/0{,}4432$
is 3,1% en $0{,}2190/0{,}2216$ 1,2% eronder; $0{,}4295/0{,}2190 = 1{,}96$); de
hedgetabel ($0{,}43/\sqrt{50\,000} = 0{,}002$; $1{,}86/\sqrt{50\,000} = 0{,}0083$ en
$-0{,}019/0{,}0083 = -2{,}3$; $0{,}019/4{,}49 = 0{,}4\%$; $3{,}25/4{,}49 = 72\%$;
$1{,}86/4{,}49 = 41\%$); tien jaar opties ($0{,}197/(0{,}43/\sqrt{120}) = 5{,}0$;
$1{,}86/\sqrt{120} = 0{,}17$); $\log 0{,}9 = -0{,}105$; oefening 1 ($0{,}216 \cdot
23{,}1/1{,}061208 = 4{,}7018$); oefening 3 ($(1{,}96 \cdot 0{,}2/0{,}06)^2 = 42{,}7$);
Itô-bewijs ($\Var(Q_n) = n \cdot 2h^2 = 2th$). De celuitvoer is niet opnieuw gelezen
(geen .ipynb); een vergelijking van alle getallen in de tekst met de versie van de
vorige ronde (`git show HEAD`) laat zien dat de taalredactie geen getal heeft veranderd
(alleen één "2%" minder, een motiefnaam), zodat de controle tegen de celuitvoer uit de
vorige ronde (smirk: 19 van 19, 21/9/3 punten; VRP: $t = 12{,}8$, vier slechtste
maandeinden; oefening 2 en 3) blijft gelden. Historie klopt: CBOE april 1973, Merton
1969 en 1973, CRR 1979, Rubinstein 1994 met SPX-opties rond de crash.

## Navertelling in vijf zinnen

Een optie is evenveel waard als de portefeuille van aandeel en obligatie die haar
namaakt, en daarom komt het verwachte rendement van het aandeel niet in de prijs voor.
In continue tijd levert de delta-hedge via het lemma van Itô een PDE zonder $\mu$, met
als oplossing de Black-Scholes-formule, die de verwachting van Bachelier is onder
risiconeutrale kansen. Een handelaar die tegen de verkeerde volatiliteit verkoopt, wint
of verliest het variantieverschil gewogen met gamma, en bij discreet hedgen daalt de
spreiding van zijn P&L met $1/\sqrt{N}$, zonder spoor van de drift. Op echte data breekt
het model op één punt: de implied volatility van SPY-opties hangt af van uitoefenprijs en
looptijd (de smirk), en de VIX ligt gemiddeld scherp gemeten boven de gerealiseerde
volatiliteit. Of die dure bescherming een beloning voor crashrisico of een vergissing
is, valt met deze data niet te beslissen. Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het college duidelijk soepeler gemaakt: de calques uit onderzoek E zijn
weg, de toy-stappen zijn zakelijk, en Intuïtie en Theorie lezen hardop goed. Wat blijft
is een handvol zinnen met te veel ingebedde delen, één sjabloonformule die drie keer
terugkomt ("niet tegen de bron te houden") en kleine inconsistenties (euro/dollar,
wij/we, twee namen voor het lemma van Itô). Taal 8,5, niet blokkerend.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. `:66` "Op de vraag theorie of feit luidt het antwoord dat Black-Scholes een theorie is
   die getoetst wordt, maar wel een relatieve theorie."
   Herschrijving: "Black-Scholes is een theorie die zich laat toetsen, maar een relatieve,
   want ze zegt niet wat een aandeel waard is, alleen wat een optie waard is *gegeven*
   het aandeel."
2. `:1115` "Het model gaf de eerste prijs zonder voorkeuren, want uit één argument, dat
   wat zonder risico is de rente verdient, volgt een formule met vier waarneembare
   invoergrootheden en één te schatten getal."
   Herschrijving: "Het model gaf de eerste optieprijs waarin de voorkeuren van beleggers
   niet voorkomen. Alles volgt uit het argument dat een positie zonder risico de rente
   verdient, en de formule vraagt vier grootheden die op het scherm staan en één die
   geschat moet worden."
3. `:723` "Dit is wel een controle van de code en geen replicatie, omdat de getallen van
   Derman en Kamal niet tegen de bron te houden zijn."
   Herschrijving: "Dit controleert de code en is geen replicatie, want we vergelijken de
   simulatie met de vuistregel van Derman en Kamal en niet met de getallen in hun
   artikel."

## Controle 1

Controle van record (F6c) na verwerking van F6 (8,7) in R9-1. Gelezen: `plannen/kaart-rollen.md`
§4-§8, dit bestand volledig, `notes/rapport-02_09_black_scholes.md` sectie R9-1, en het
college één keer volledig.

**Drie verbeteringen met het meeste effect (F6).**
1. Taal (sjabloonzin + euro/dollar). Opgelost: "niet tegen de bron te houden" komt nergens
   meer voor; r. 730-731, r. 860-861, r. 1031-1034 zeggen nu wat wel en niet vergeleken
   is. "Euro" is overal "dollar" (r. 74, 543, 832).
2. Helderheid ($\mu$-zin + $\sqrt{\pi/2}$). Opgelost: r. 307-309 zegt dat de verkochte
   aandelen de verwachte stijging $\mu S C_S\,\mathrm{d}t$ van de optie tegenover zich
   hebben; r. 668-676 verklaart $\sqrt{\pi/2}$ nu via de gammaweging (zie de aparte
   controle hieronder), niet via $\E|Z|$.
3. Replicatie (reden voor "alleen teken en vorm"). Opgelost: smirkblok (r. 860-861) en
   VRP-blok (r. 1031-1034) geven elk een reden (andere periode, ander instrument).

**Per criterium.**
- Helderheid: $\mu$-zin (opgelost), $\sqrt{\pi/2}$ (opgelost), SDF-term overal
  "stochastische discontofactor" (opgelost, r. 344-345, r. 1154), "verwachtingen" →
  "voorspellingen" (opgelost, r. 93).
- Opbouw: tijdvakzin weg (opgelost), slot eindigt niet meer op een link maar op wat
  openstaat (opgelost, r. 1158-1162).
- Taal: de drie hardop-zinnen herschreven zoals voorgesteld (opgelost, r. 65-66, r.
  729-731, r. 1125-1127); sjabloonzin, euro/dollar, toy-cel (r. 101), looptijd-calque (r.
  345), "wij" en "Itô's lemma" naast "lemma van Itô": geen van deze vier komt nog voor
  (opgelost).
- Toy: twee precisies in Stap 4 opgelost (r. 156-158: $\Delta_0 = 0{,}62399$ en
  $C_0 = 100\,\Delta_0 + B_0 = 62{,}3991 - 52{,}0388$, consistent).
- Code en figuren: uitpakken bij naam (opgelost, r. 176-177, r. 622), zin na de
  Greeks-cel (opgelost, r. 591-592, inclusief de "Beter uitleggen"-opmerking over de
  array-soort die de replicatie gebruikt), leeswijzer smirkfiguur (opgelost, r. 981-983:
  helling per looptijd links, vlakke strook rechts).
- Replicatie: VRP-reden (opgelost), smirk-reden ingekort tot alleen "de niveaus hangen
  van de dag af" (opgelost, r. 860-861), "op de meeste dagen" als eigen zinsdeel
  (opgelost, r. 1088).
- Oefeningen: het omgekeerde verband in Stap 1.2 is herschreven van "want" naar "en ...
  dus" (r. 1218); de twee waarnemingen (blijft binnen $\pm1/n$, daalt als $1/n$) staan nu
  naast elkaar in plaats van de ene als bewijs van de andere te presenteren. Deels: de
  nieuwe formulering suggereert met "dus" nog steeds een logisch verband in één richting.
  Zonder effect op het deelcijfer, dat al op het plafond van 9 stond.

**Feitelijke fouten.** Geen nieuwe. Nagerekend: $\sqrt{\pi/4}\cdot 19{,}7\cdot
0{,}20/\sqrt{63} = 0{,}4399 \approx 0{,}44$ dollar (r. 675-676, ongewijzigd); de term
$\mu S C_S\,\mathrm{d}t$ klopt met de afleiding van $\mathrm{d}\Pi$, waar de twee
$\mu$-termen bij $\Delta = C_S$ elkaar precies opheffen.

**Controle $\sqrt{\pi/2}$ (r. 668-676).** De schrijver verklaart de factor nu via de
gammaweging langs het pad, niet via $\E|Z| = \sqrt{2/\pi}$. Nagerekend tegen de
vuistregel van Derman en Kamal, [](#eq-black-scholes-dk): de gelijk gewogen schatter
("de volatiliteit uit $N$ waarnemingen", standaardfout $\sigma/\sqrt{2N}$) maal vega geeft
$\sigma\,\nu/\sqrt{2N}$, en $\sqrt{\pi/4}\,\big/\,(1/\sqrt2) = \sqrt{\pi/2} = 1{,}2533$ is
precies de factor waarmee dat getal naar de vuistregel $\sqrt{\pi/4}\,\nu\sigma/\sqrt N$
gaat. De richting van de bewering ("een ongelijk gewogen schatting is onnauwkeuriger dan
een gelijk gewogen") is een juiste algemene statistische uitspraak: bij i.i.d. grootheden
met gelijke variantie minimaliseert gelijke weging de variantie van het gewogen
gemiddelde, en ongelijke weging (hier met de gamma van dat moment) vergroot ze. Geen
onjuiste bewering gevonden; de uitleg is consistent met de vuistregel en blijft, zoals
gevraagd, tot één bijzin beperkt.

**Zeven deelcijfers (F6c), plafondregel toegepast.**

| nr | criterium | gewicht | F6 | plafond | F6c |
|---|---|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 | 9 | 9 |
| 2 | Opbouw en rode draad | 20% | 9 | 9 | 9 |
| 3 | Taal | 20% | 8,5 | 9 | 9 |
| 4 | Toy-voorbeeld | 10% | 9 | 9 | 9 |
| 5 | Code en figuren | 10% | 8,5 | 9 | 9 |
| 6 | Replicatie en empirie | 10% | 8,5 | 9 | 9 |
| 7 | Oefeningen | 5% | 9 | 9 | 9 |

Gewogen: 0,25·9 + 0,2·9 + 0,2·9 + 0,1·9 + 0,1·9 + 0,1·9 + 0,05·9 = 9,0. Laagste
deelcijfer 9,0; taal blokkeert niet.

## Eindcijfer (F6c): 9,0

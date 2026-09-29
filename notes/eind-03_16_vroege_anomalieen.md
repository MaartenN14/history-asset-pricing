STATUS 03_16_vroege_anomalieen F6c words=5584 prose=PASS open=0 cijfer=9,0 min=9,0

**Eindcijfer van record: 9,0** (F6c). Verloop: Vorig: 8,9. Ronde 9+: T, F6 8,6 (5 feitpunten) -> F6c 9,0. Het cijfer onder de kop "F6, vóór herstel" is dus niet het eindcijfer.

# Ronde 9+

Vorige ronde: 8,9

Eindbeoordeling F6 van `lectures/03_16_vroege_anomalieen.md` na de taalredactie, volgens
`plannen/rubriek-didactiek.md` (streef 9,0, geen deelcijfer onder 8,5), `plannen/kaart-rollen.md`
§8 en STYLE §11.12. `prose_stats --check`: 5.456 woorden, gemiddeld 16,4 woorden per zin,
twee zinnen boven 40 (tabel of lijst), para_one 8, colon_mid 4,4, PASS. Replicatieblok 215
woorden. Getallen nagerekend tegen `tools/nb_outputs.py` (16 cellen) en met de hand.

Vakterm-controle na de taalredactie (word-diff tegen HEAD): geen vakterm van betekenis
veranderd. "excess rendement" werd overal "overrendement", "beprijsde factor" werd "factor
met een risicopremie", "correct beprijsd verschil" werd "verschil dat een correcte
risicopremie is". Die vervangingen zijn inhoudelijk juist. Wel heeft de redactie een
bewijsschets aangevuld met een deelstap die een factor $\sqrt 2$ mist (feitelijke fout 1).

## De drie verbeteringen met het meeste effect

1. **Taal (8,5 → 9).** De drie meldingen over het eigen werk uit de lopende tekst halen
   (`03_16:79–80`, `:477–478`, `:848–849`; STYLE §11.12 "Meldingen over het werk ... horen in
   het rapport"), één keer in het replicatieblok (`:767–768`) volstaat. De formule
   "Daarmee klopt (ook) de ... verwachting uit de intuïtie" staat drie keer (`:462`, `:535`,
   `:858`) plus "zoals we vooraf verwachtten" en "eveneens zoals verwacht" in dezelfde
   alinea (`:857–860`); elk inlossen anders verwoorden en in de replicatiealinea één
   verwijzing laten staan. De tic "maar dan" (`:70`, `:82`, `:283`, `:306`) en "men"
   (`:504`) vervangen.
2. **Helderheid (8,5 → 9).** Feitelijke fouten 1, 2 en 5 herstellen (factor $\sqrt 2$ in de
   bewijsschets, "positieve alpha" in de stelling van Berk zonder $\E[\alpha_i] = 0$,
   "net als de size-premie voor ongeveer twee derde"), en "B/P" (`:388`) wordt "B/M".
3. **Opbouw en replicatie (8,5 → 9 elk).** De genummerde verwachtingen in de Intuïtie
   (`:99–108`) omzetten in een doorlopende voorspelling met richting (H12 verbiedt
   genummerde verwachtingen), de openingsvraag niet letterlijk herhalen in het Overzicht
   (`:29–31` en `:36–37`), en in de replicatie de misleidende zin over "voor size niet van
   nul te onderscheiden" en de januari-datamining-zin in "Wat er brak" rechtzetten
   (feitelijke fouten 3 en 4); de alinea `:865–868` zonder tabelgetallen.

## Cijfer F6, vóór herstel (niet het eindcijfer): 8,6

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 8,5 |
| 2 | Opbouw en rode draad | 20% | 8,5 |
| 3 | Taal | 20% | 8,5 |
| 4 | Toy-voorbeeld | 10% | 9 |
| 5 | Code en figuren | 10% | 9 |
| 6 | Replicatie en empirie | 10% | 8,5 |
| 7 | Oefeningen | 5% | 9 |

Gewogen: 2,125 + 1,70 + 1,70 + 0,90 + 0,90 + 0,85 + 0,45 = 8,625, dus 8,6. Laagste
deelcijfer 8,5; taal blokkeert niet. Het verschil met 8,9 komt van de nieuwe toetsen uit
§11.12 en H12 (werkmeldingen, vaste inlosformule, genummerde verwachtingen) en van vijf
inhoudelijke onnauwkeurigheden die bij verse lezing boven kwamen.

## Per criterium

### 1. Helderheid van de uitleg (8,5)

*Goed*
- **Theorie, Opzet en De alpha van een long-short-portefeuille.** Elke `###` opent met de
  bewering, en bij [](#eq-vroege-anomalieen-se) staat het getal (Sharpe 0,11, correctie
  1,01, $5/\sqrt{480} \approx 0{,}23\%$ per maand) met de gevolgtrekking voor Basu en RRL.
- **Het kernresultaat.** De stelling van Berk krijgt een economisch verhaal vooraf, een
  bewijs met stapkoppen en daarna de orde van grootte ($-0{,}19$) met de reden (ruis in
  het kasstroomniveau) en de thermometer-vergelijking met E/P en B/M.
- **Data snooping.** $\E[t] \approx 24{,}8\,\rho$ en "$\rho = 0{,}1$ geeft al 2,5" maken de
  formule tastbaar.

*Aanmerkingen*
- **Het kernresultaat, stelling.** "kleine bedrijven hebben gemiddeld een positieve alpha
  ten opzichte van het model, ook al is elke prijs correct." Uit $\Cov < 0$ volgt alleen
  een hogere alpha dan gemiddeld; positief vraagt $\E[\alpha_i] = 0$.
- **Data snooping, na de propositie.** "Deelt men die afstand door de standaardfout van een
  gemiddelde over $n$ aandelen, dan volgt de $t$-waarde." Dat geeft $\rho\sqrt{n}\,\varphi/p$,
  niet $\rho\sqrt{2n}\,\varphi/p$.
- **Fama-MacBeth met kenmerken.** "Het nam van de maandelijkse hellingen op bedrijfstak,
  omvang, B/P en schuldgraad ..." B/P is elders B/M (H7).
- **Fama-MacBeth met kenmerken.** "De gewichten stijgen lineair met E/P, zodat de uitersten
  zwaarder wegen dan in een sortering." Zwaarder dan wat, bij welke schaal? In het toy
  hebben H − L en de FM-gewichten een andere normering.

*Beter uitleggen*
- Bij de gewichten $(-8, -4, -2, 4, 10)$ ontbreekt de vergelijking met H − L op dezelfde
  schaal (blootstelling één): H − L heeft E/P-blootstelling 0,065, dus gewichten
  $\pm 0{,}5/0{,}065 \approx \pm 7{,}7$ op vier aandelen. Eén zin met dat getal maakt
  "zwaarder in de uitersten" concreet.
- De markt heet $R^{e}_{m,t+1}$ in [](#eq-vroege-anomalieen-ls) en $f_{m,t+1}$ in simulatie
  (a); één zin dat $f_m$ het overrendement van de markt is.

*Voor een 9*
- `03_16:427–428`: "positieve alpha" → "hogere alpha dan het gemiddelde", of $\E[\alpha_i] = 0$
  in de aannames.
- `03_16:503–505`: de deelstap met het verschil van twee poten (tweemaal de afstand, gedeeld
  door $\sqrt{2/n}$).
- `03_16:388`: B/P → B/M.
- `03_16:1131–1132`: de size-premie zat in Keims periode voor vier vijfde in januari
  (`:944`), niet voor twee derde; de zin moet dat onderscheid maken.

### 2. Opbouw en rode draad (8,5)

*Goed*
- **Overzicht.** Vraag, antwoord ("In de steekproeven van de eerste onderzoekers wel") en de
  drie lezingen (risico, vergissing, toeval) in de eerste alinea; de lijst van vijf
  handelingen is een bruikbare routekaart.
- **Toy → Theorie → Simulatie.** Stap 4 van het toy (5,325% als verschil van twee alpha's)
  keert terug in de long-short-regressie en in simulatie (a); de inleiding van de
  simulatie zegt nu vooraf waarom de twee werelden samen horen (minder dan een op de
  vijf, ruim negen op de tien).
- 5.456 woorden, ruim onder de grens.

*Aanmerkingen*
- **Intuïtie.** "We verwachten dus drie dingen: 1. ... 2. ... 3. ..." H12 vraagt een
  voorspelling met teken en richting zonder genummerde verwachtingen; daardoor ontstaan
  later "de tweede verwachting", "de derde verwachting", "de eerste verwachting".
- **Waar we zijn / Overzicht.** "Voorspellen eenvoudige kenmerken van een aandeel ... beter
  dan bèta?" en "Voorspellen kenmerken als de winst-koersverhouding ... het rendement beter
  dan bèta?" Dezelfde vraag twee keer achter elkaar [onderzoek B].
- **Intuïtie.** "Zijn tabellen hebben we niet kunnen inzien, zodat we die uitkomst niet
  overnemen." Het onderbreekt het verhaal over Nicholson [onderzoek B].
- **Simulatie.** Twee werelden onder één vraag; aanvaard in de vorige ronde, blijft een
  kleine aftrek.

*Beter uitleggen*
- De simulatie (b) meet data snooping met "beste van 100", terwijl de theorie
  $\rho$ gebruikt; één zin die de twee verbindt (het beste van honderd heeft een impliciete
  $\rho$ van ongeveer $2{,}5/24{,}8$ bij deze $n$) sluit de cirkel.

*Voor een 9*
- `03_16:97–108`: de drie genummerde verwachtingen omzetten in twee of drie zinnen met
  richting; de inlossingen `:462`, `:535`, `:858` dan zonder rangtelwoord.
- `03_16:36–37`: het Overzicht laten openen met het antwoord [onderzoek B].
- `03_16:79–81`: de werkmelding over Nicholsons tabellen weg; "Meer stelde zijn enquête
  niet vast" draagt de inhoud al [onderzoek B].
- `03_16:58–67`: zes artikelen met zes citaties in één alinea van ruim 80 woorden; een
  kleine tabel (jaar, auteur, kenmerk) of twee alinea's [onderzoek B].

### 3. Taal (8,5)

*Goed*
- **Theorie.** De redactie heeft de sjabloonopeningen ("*Waarom zou dit waar zijn?*",
  "In woorden:", "bewijsidee:") vervangen door gewone zinnen ("Stel dat", "Denk aan",
  "Het bewijs berust erop dat"), en "haar" voor zaken is overal weg.
- **Overal.** "overrendement", "waardegewogen", "gelijkgewogen" consequent in de proza;
  geen puntkomma's of gedachtestreepjes als lijm; dubbele punten onder de norm.
- **Wat er brak.** "Het CAPM verklaart nog steeds veel." is nu een hele zin [onderzoek B,
  opgelost].

*Aanmerkingen*
- **Het kernresultaat / Data snooping / Replicatie.** "Daarmee klopt de tweede verwachting
  uit de intuïtie, zij het met een verfijning." — "Daarmee klopt ook de derde verwachting
  uit de intuïtie." — "zoals we vooraf verwachtten, en daarmee klopt ook de eerste
  verwachting uit de intuïtie." Vaste wending drie keer (§11.12: hoogstens twee), en in
  `:857–860` staan er drie verwachtingsformules in één alinea ("eveneens zoals verwacht").
- **Intuïtie / Data snooping / Replicatie.** "Zijn tabellen hebben we niet kunnen inzien",
  "Hun eigen formules hebben we niet in de primaire bron kunnen nalezen.", "omdat we hun
  tabelwaarden niet konden nalezen." Werkmeldingen in de lezerstekst (§11.12).
- **Overzicht, Intuïtie, Theorie.** "maar dan met een lijst afwijkingen", "maar dan met
  bèta's", "maar dan op één reeks", "maar dan voor een alpha". De redactie verving vier
  keer "nu" door dezelfde wending; het wordt een tic.
- **Data snooping.** "Deelt men die afstand ..." "men" valt uit het register (overal
  elders "we").
- **Fama-MacBeth met kenmerken.** "Barra draaide het probleem van slecht gemeten
  gemiddelden zo om, want covarianties zijn met maanddata wel nauwkeurig te schatten."
- **Wat er brak.** "Het CAPM verklaart nog steeds veel. Over de volle eeuw verklaart het de
  waardegewogen B/M-premie grotendeels" — twee keer "verklaart" achter elkaar.

*Beter uitleggen*
- "dus" staat 22 keer in de proza, deels door de redactie toegevoegd (`:218`, `:282`,
  `:299`, `:523`); in oefening 2 (4) twee keer in twee zinnen (`:1097–1099`). Waar het geen
  gevolgtrekking is, kan het weg.

*Voor een 9*
- `03_16:462`, `:535`, `:857–860`: elk inlossen anders verwoorden, hoogstens twee keer
  "verwachting uit de intuïtie".
- `03_16:79–80`, `:477–478`, `:848–849`: werkmeldingen weg; de beperking staat al in het
  replicatieblok (`:767–768`).
- `03_16:70`, `:82`, `:283`, `:306`: "maar dan" variëren of schrappen.
- `03_16:504`, `:389–391`, `:958–959`: zie de hardop-toets onderaan.

### 4. Toy-voorbeeld (9)

*Goed*
- **Toy-voorbeeld.** Vijf aandelen, één mechanisme, stappen 1–4 met de hand, en een
  hand/code-tabel die exact overeenkomt (6,0%; 1,000; 4,625%; −0,700%; 5,325%).
- **Slotalinea.** Zegt wat het getal betekent (sortering meet de alpha van een kenmerk,
  niet welk) en waarom 5,3% uit één periode niets over toeval zegt.
- De getallen keren terug in de FM-gewichten, de long-short-regressie en oefening 1.

*Aanmerkingen*
- **Toy-cel.** `print("zelfde portefeuilles bij sortering op ME:", ...)` naast de tabel;
  een extra tabelrij leest rustiger [onderzoek B].

*Beter uitleggen*
- Geen.

### 5. Code en figuren (9)

*Goed*
- **Simulatie.** Parameters in één dict `sim`, `alpha_t` en `long_short_weights` met
  benoemde tussenstappen, zichtbare lussen over steekproeven.
- **Figuren.** Vóór elke figuur staat waarop te letten ("links om de afstand tussen de
  twee verdelingen"; "stijgt de alpha van deciel 1 naar deciel 10"), erna een bijschrift
  met wat te zien is.

*Aanmerkingen*
- **Replicatie, figuur.** `ax.set_title(f"CAPM-alpha per {sort}-deciel (value-weighted)")`
  en in de simulatiefiguur "(a) Klein min groot in een wereld zonder mispricing": Engels in
  figuurteksten (rubriek: figuurteksten zijn Nederlands).
- **Toy-cel, oefening 1.** De rij "excess H - L" en de kolom "excess" in presentatietabellen,
  terwijl de proza "overrendement" zegt.

*Beter uitleggen*
- Geen.

### 6. Replicatie en empirie (8,5)

*Goed*
- **Replicatieblok.** Bron, wat, data, verschil en verwachte afwijking in 215 woorden, met
  een eerlijke keuze voor teken, orde van grootte en rangorde.
- **Tabel origineel/hier.** Twaalf alpha's met $t$-waarden, alle gelijk aan de cel; het
  oordeel begint met **Geslaagd** en verwijst naar de verwachting.
- **Januari-effect.** Eigen verwachting, tabel, oordeel en een institutionele verklaring.

*Aanmerkingen*
- **Replicatie, oordeel.** "Na publicatie zijn de waardegewogen alpha's kleiner, en voor
  size niet van nul te onderscheiden, eveneens zoals verwacht." Ook E/P ($t = 1{,}58$) en
  B/M ($t = 0{,}40$) zijn na publicatie waardegewogen niet van nul te onderscheiden.
- **Replicatie, na het oordeel.** "De B/M-alpha van 1,42% per maand, ongeveer 17% per jaar,
  ... met een alpha van 0,14% en een long-short-bèta van 0,44." Vier getallen in lopende
  tekst, waarvan twee niet in de tabel staan.
- **Wat er brak, Risico of vergissing?** "Het januari-effect en het verdwijnen na
  publicatie passen slecht bij een risicopremie, maar wel bij datamining." De eigen
  januaritabel toont het patroon ook in 1926–1962, vóór Keims steekproef.

*Beter uitleggen*
- Waarom E/P en B/M bij gelijke weging na publicatie blijven ($t = 4{,}64$ en $5{,}98$) en
  waardegewogen niet: één zin die dat aan kleine aandelen koppelt, sluit aan op "het
  sterkst bij kleine aandelen".

*Voor een 9*
- `03_16:859–860`: "na publicatie zijn de waardegewogen alpha's kleiner en nergens
  significant".
- `03_16:865–868`: de volle-eeuwrij als regel in de tabel of weg; de alinea met één
  conclusie.
- `03_16:979`: januari-effect en datamining scheiden (feitelijke fout 4).

### 7. Oefeningen (9)

*Goed*
- Instap (C erbij), afleiding (orde van grootte van Berk, met code en factor 1,84) en
  uitbreiding van de replicatie (januari voor value, Fama-MacBeth van Banz).
- Elke uitwerking eindigt met een les ("een cross-sectie die op één kenmerk is gesorteerd,
  heeft maar één dimensie").

*Aanmerkingen*
- **Oefening 3 (2).** "zit de waardegewogen waarde-premie net als de size-premie voor
  ongeveer twee derde in januari" (zie fout 5).
- **Oefening 2 (4).** "Zonder $\delta$ neemt marktwaarde dus ... Een kenmerk verklaart dus
  ..." twee keer "dus".

*Beter uitleggen*
- Geen.

## Feitelijke fouten

Nagerekend tegen de celuitvoer en met de hand. Correct: toy (6,0%; 1,000; alpha's
$-1{,}50$/0,10/1,50/3,00/6,25; H, L, H − L); FM-gewichten ($-8, -4, -2, 4, 10$; 0,005);
standaardfout (0,11; 1,01; 0,23%; bijna 3% per jaar); $\varphi(1{,}2816)/0{,}1 = 1{,}755$,
$24{,}8\rho$, 2,5; $1 - 0{,}975^{20} = 0{,}40$; 12,6%; $-0{,}19$; 0,076 tegen 0,079;
18,6%; 2,4%; 93,2%; 13,8%; replicatietabel (twaalf alpha's en $t$'s, negatieve bèta's
E/P en B/M, 17%, 0,14%, 0,44); januari (0,82 en 0,78; 1926–1962 0,90 en 0,64; na 1980
feb–dec negatief); oefeningen (0,75; 7,33%; 3,58%; 4,28%; factor 1,84; $-0{,}027$ met
$t = -1{,}57$, $t = 0{,}54$; 65%, 67%, 24%, 45%; 0,78% met $t = 4{,}17$; Banz $-0{,}106$
met $t = -1{,}55$, bèta 0,73 → $-0{,}12$, na 1982 0,038). Niet geverifieerd: Nicholsons
"bijna tien tegen één", Barra 1975, Asness-Frazzini-Israel $t = 1{,}82$, Bhandari "vooral
in januari".

1. **Data snooping, bewijsschets (`03_16:503–505`).** Eén poot ligt $\rho\varphi/p$ van nul;
   gedeeld door de standaardfout van één gemiddelde ($1/\sqrt n$ in dezelfde eenheid) geeft
   dat $\rho\sqrt{n}\,\varphi/p$. De formule [](#eq-vroege-anomalieen-snooping) heeft
   $\sqrt{2n}$: tweemaal de afstand gedeeld door $\sqrt{2/n}$. De redactie voegde deze
   deelstap in een vorige ronde toe. De dropdown zelf klopt.
2. **Stelling van Berk (`03_16:427–428`).** "kleine bedrijven hebben gemiddeld een
   positieve alpha" volgt niet uit de aannames; zonder $\E[\alpha_i] = 0$ volgt alleen een
   hogere alpha dan gemiddeld.
3. **Replicatie, oordeel (`03_16:859–860`).** "voor size niet van nul te onderscheiden"
   suggereert dat E/P en B/M na publicatie waardegewogen wel significant zijn; cel 9:
   $t = 1{,}58$ en $0{,}40$.
4. **Wat er brak (`03_16:978–979`).** Het januari-effect past volgens de eigen cel 11 niet
   bij datamining: januari draagt ook in 1926–1962 het grootste deel (0,90 en 0,64), en na
   1980 is januari nog positief met $t = 3{,}4$ en $5{,}3$. Alleen het verdwijnen van de
   jaarpremie na publicatie past bij datamining.
5. **Oefening 3 (`03_16:1131–1132`).** "net als de size-premie voor ongeveer twee derde":
   de size-premie zat in Keims periode voor 0,82 en 0,78 in januari (`:944`, vier vijfde).

## Navertelling in vijf zinnen

Tussen 1977 en 1985 vonden Basu, Banz, Reinganum en Rosenberg c.s. dat goedkope en kleine
aandelen een positieve CAPM-alpha hadden, zonder hogere bèta. Een sortering is een
regressie zonder vorm en een Fama-MacBeth-helling een long-short-portefeuille, en beide
meten een alpha met een standaardfout van ongeveer $\sigma_\varepsilon/\sqrt T$, zodat alleen
grote effecten in korte steekproeven significant worden. Berk laat zien dat marktwaarde
een alpha voorspelt zodra het toetsmodel een risico mist, ook bij correcte prijzen, terwijl
Lo en MacKinlay laten zien dat een gezocht kenmerk een grote $t$ in de eigen steekproef
geeft. De simulatie toont beide kanten: een echte premie die meestal onzichtbaar blijft en
een onechte die in ruim negen op de tien steekproeven verschijnt. Op echte data kloppen de
tekens in de oorspronkelijke steekproeven, de waardegewogen effecten krimpen na publicatie,
en of het risico of vergissing was, bleef onbeslist. Dit komt overeen met het Overzicht.

## Taal na de redactie

De redactie heeft het college duidelijk natuurlijker gemaakt: de sjabloonopeningen zijn
weg, "haar" voor zaken is weg, en de Engelse wegingstermen zijn vertaald. Wat overblijft
is een nieuwe laag vaste wendingen die de redactie zelf aanbracht ("maar dan", "Daarmee
klopt ... verwachting uit de intuïtie", veel "dus") en drie werkmeldingen die §11.12 uit
de tekst weert. Geen vakterm is van betekenis veranderd.

Hardop-toets, drie zinnen die nog niet natuurlijk klinken:

1. `03_16:389–391` "Barra draaide het probleem van slecht gemeten gemiddelden zo om, want
   covarianties zijn met maanddata wel nauwkeurig te schatten."
   → "Zo omzeilde Barra het probleem van de slecht gemeten gemiddelden, want covarianties
   zijn met maanddata wel nauwkeurig te schatten."
2. `03_16:663–664` "Een verschil van bijna een procentpunt per jaar dat een correcte
   risicopremie is, blijft na veertig jaar dus meestal onzichtbaar."
   → "Een correcte risicopremie van bijna een procentpunt per jaar blijft na veertig jaar
   dus meestal onzichtbaar."
3. `03_16:504–505` "Deelt men die afstand door de standaardfout van een gemiddelde over $n$
   aandelen, dan volgt de $t$-waarde."
   → "Het verschil tussen de twee poten ligt dan tweemaal zo ver van nul, en gedeeld door
   de standaardfout van dat verschil geeft dat de $t$-waarde."

Bij volledige oplossing van alle punten: 9,0

## Controle 1

Nagerekend tegen `uv run python tools/nb_outputs.py lectures/03_16_vroege_anomalieen.ipynb`
(16 cellen, exit 0) en met de hand; `prose_stats --check`: 5.584 woorden, PASS.

**Feitelijke fouten (F6), status**

1. **Bewijsschets snooping (`:503–513`) — opgelost.** De nieuwe deelstap zegt: twee poten
   geven een verschil $2\rho\,\varphi(q_p)/p$ standaarddeviaties, gedeeld door de
   standaardfout van dat verschil $\sqrt{2/n}\,\sigma/\sqrt T$. Nagerekend:
   $2/\sqrt{2/n} = \sqrt{2n}$, dus $t \approx \rho\sqrt{2n}\,\varphi(q_p)/p$, gelijk aan
   [](#eq-vroege-anomalieen-snooping). De factor $\sqrt 2$ komt kloppend uit "tweemaal
   de afstand" gedeeld door "$\sqrt{2/n}$", en de hardop-toets-herformulering
   (`:511–513`) is vrijwel letterlijk de voorgestelde tekst.
2. **Stelling van Berk (`:427–434`) — opgelost.** "hogere alpha ten opzichte van het
   model dan grote" volgt direct uit $\Cov < 0$, zonder $\E[\alpha_i]=0$ nodig te hebben.
3. **Replicatie-oordeel (`:875–877`) — opgelost.** "kleiner en nergens significant" klopt
   tegen cel 9 (VW: $t=1{,}58$ E/P, $0{,}40$ B/M, $-0{,}68$ size, alle $< 1{,}96$); EW
   E/P/B/M blijven significant, $t=4{,}64$ en $5{,}98$ tegen celuitvoer $4{,}644$ en
   $5{,}983$. Klopt.
4. **Wat er brak, januari/datamining (`:994–997`) — opgelost.** Januari-effect nu apart
   van het verdwijnen na publicatie; cel 11 bevestigt bijdrage januari 1926–1962 (VW
   0,895, EW 0,642), dus het patroon zat er al vóór Keim.
5. **Oefening 3 (`:1149–1152`) — opgelost.** "ongeveer twee derde" nu concreet 65%
   (E/P) en 67% (B/M), tegen cel 15 (0,647 en 0,670); vergeleken met de "vier vijfde"
   van de size-premie uit cel 11 (0,817 VW, 0,782 EW). Klopt en is nu ondubbelzinnig.

**Getallencontrole van de drie gevraagde punten**

- $t=4{,}64$ en $t=5{,}98$ (`:876`): cel 9, EW na publicatie, E/P $t=4{,}644$ en B/M
  $t=5{,}983$. Klopt.
- $\pm 7{,}7$ (`:371–373`): H − L heeft bij gewicht $\pm 0{,}5$ een blootstelling
  $0{,}5\cdot(0{,}09+0{,}12) - 0{,}5\cdot(0{,}03+0{,}05) = 0{,}065$ aan E/P; herschaald
  naar blootstelling één geeft $0{,}5/0{,}065 = 7{,}69 \approx 7{,}7$, tegen 10 voor
  E in cel 3. Klopt.
- Toy-handberekening $6{,}5$ (`:371`): $H = 10{,}5\%$ ($=(9+12)/2$), $L = 4\%$
  ($=(3+5)/2$) uit de toy-tabel, dus $10{,}5-4=6{,}5$ procentpunt. Herleidbaar uit de
  tabelwaarden in de tekst (E/P van D, E, A, B). Klopt.

**Drie verbeteringen en overige Voor-een-9-punten**

- **Taal — opgelost.** "verwachting uit de intuïtie" 0×, "maar dan" 0×, "men" 0×,
  dubbel "verklaart" weg, werkmelding nog 1× (alleen replicatieblok, regel 785); de drie
  hardop-toetszinnen (Barra, risicopremie, bewijsschets) zijn nagenoeg letterlijk
  volgens voorstel herschreven.
- **Helderheid — opgelost.** Alle vier Voor-een-9-punten (Berk, deelstap, B/M, vier
  vijfde/twee derde) opgelost; als bonus ook de FM-gewichten-vergelijking ($\pm 7{,}7$)
  toegevoegd en correct.
- **Opbouw — opgelost.** Genummerde verwachtingen vervangen door doorlopende
  voorspelling, Overzicht opent met het antwoord, zes citaten nu in een tabel,
  Nicholson-werkmelding weg.
- **Replicatie — opgelost.** Alle drie Voor-een-9-punten opgelost, inclusief de
  vier-getallenalinea (bèta 0,44 verplaatst met één conclusie).
- Code en figuren, toy en oefeningen hadden geen Voor-een-9; de losse aanmerkingen
  (Engelse figuurteksten, "excess"-labels, print naast tabel) zijn wel verwerkt, zonder
  dat dat een deelcijfer verhoogt (geen punt in het vooruitzicht gesteld).

**Nieuwe punten:** geen. Bij het nalezen is geen nieuwe feitelijke fout en geen
verslechtering gevonden.

## Eindcijfer van record (F6c): 9,0

| nr | criterium | gewicht | deelcijfer |
|---|---|---|---|
| 1 | Helderheid van de uitleg | 25% | 9,0 |
| 2 | Opbouw en rode draad | 20% | 9,0 |
| 3 | Taal | 20% | 9,0 |
| 4 | Toy-voorbeeld | 10% | 9,0 |
| 5 | Code en figuren | 10% | 9,0 |
| 6 | Replicatie en empirie | 10% | 9,0 |
| 7 | Oefeningen | 5% | 9,0 |

Gewogen: 2,25 + 1,80 + 1,80 + 0,90 + 0,90 + 0,90 + 0,45 = 9,00.

Plafondregel (§11.3): helderheid, opbouw, taal en replicatie stegen naar het cijfer dat
F6 daar in het vooruitzicht stelde (9), omdat alle daar genoemde punten zijn opgelost.
Toy, code en figuren en oefeningen hadden geen Voor-een-9 en blijven op hun F6-waarde
9. Het eindcijfer is 9,0, gelijk aan het maximum dat F6 noemde "bij volledige
oplossing van alle punten".

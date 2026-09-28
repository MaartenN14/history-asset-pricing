# Rolkaart voor F23 (feiten + koude lezer) en de eindbeoordelaar

Samenvatting van STYLE.md, plannen/rubriek-didactiek.md, plannen/workflow-herziening.md
en de notatie van lectures/00_00_setup.md. Bij twijfel geldt STYLE. Versie 2026-09-25.

## 1. Doel

Elke lecture haalt eindcijfer ≥ 8,5 met geen deelcijfer onder 8 (rubriek: helderheid 30%,
opbouw 20%, taal 15%, toy 10%, code en figuren 10%, replicatie 10%, oefeningen 5%).
Lengte ≤ 5.500 woorden proza (`uv run python tools/prose_stats.py --check lectures/<slug>.md`
moet PASS geven). Bij twijfel tussen twee cijfers geldt het lagere.

## 2. Statusregel (eerste regel van elk bestand dat je schrijft, en van je eindbericht)

`STATUS <slug> <fase> words=<n> prose=<PASS|FAIL> open=<n> cijfer=<x,x|-> min=<n|->`
Fase F23 gebruikt `STATUS <slug> F23 open=<onjuist+onzeker> punten=15`.

## 3. Notatie (uit de setup) en vaste termen

- Niveaus in kleine letters: prijs $p_t$, dividend $d_t$. Logs van prijzen worden
  aangekondigd met "vanaf hier zijn kleine letters logs".
- $r$ is het netto simpele rendement, $R = 1 + r$ bruto, $R^f$ de netto risicovrije
  rente, $\ell$ het log rendement, $m$ de stochastische discontofactor. De markt krijgt
  een ander symbool of een zin die zegt dat het subscript $m$ hier de markt is.
- Vaste termen: "alpha" (niet alfa), "overlevenden", "standaardfout van 2%" altijd met
  link naar `#00-01-rendementen`. Drie motieven onder hun vaste namen: "de standaardfout
  van 2%", "risico of vergissing", "theorie of feit".
- Acht vaste kopjes: Overzicht, Toy-voorbeeld, Intuïtie, Theorie, Simulatie,
  Replicatie, Oefeningen, Wat er brak (en wat daarna kwam). "Samengevat" sluit Theorie af.
- Oefeningslabels (`ex-*`) zijn geen linkdoel; verwijzingen naar oefeningen zijn tekst.

## 4. Wat niet meetelt (geen aftrek, geen aanmerking)

1. "Samengevat" aan het eind van Theorie; geen tweede samenvatting aan het eind.
2. De vaste namen van de drie motieven (wel aftrek als de zin niet zegt wat het motief
   hier betekent).
3. Engelse code, variabelen, functies en docstrings. Tabellen en figuurteksten zijn
   Nederlands.
4. De acht vaste kopjes en de replicatie-admonition.
5. Het weglaten van een vooruitverwijzing naar een latere lecture.
6. `# TODO: naar hap.stats` bij een lokale implementatie (STYLE §5 schrijft dat voor).

## 5. Helderheidsregels H1–H12 (controlevraag per regel)

- H1 Het waarom is een handeling met een richting (iemand doet iets, een prijs stijgt
  of daalt). Controle: handelend onderwerp en richting aanwezig?
- H2 Elk symbool krijgt bij de eerste keer naam, betekenis en orde van grootte; een
  geleend resultaat wordt in één regel herhaald. Controle: waarvoor moet de lezer een
  andere lecture openen?
- H3 Eén stelling, één bewering; bewijsstappen hebben een kop die zegt wat de stap
  oplevert. Controle: is elke stelling in één zin samen te vatten?
- H4 Het getal staat naast de formule (bias, standaardfout, premie, $R^2$). Controle:
  welke formule pakt onduidelijk groot of klein uit?
- H5 Aannames worden genoemd waar ze werken. Controle: bij welke stap is de aanname niet
  te noemen?
- H6 Elk vergelijkend resultaat in beide richtingen, met economische reden. Controle:
  per parameter in "Samengevat": wat als hij stijgt, en waarom?
- H7 Eén naam per begrip per lecture; alias één keer tussen haakjes. Controle: welke
  woorden betekenen hetzelfde?
- H8 "Dat", "dit", "die vorm" verwijzen naar de vorige zin of worden het ding zelf.
  Controle: bij elke "Dat is": wat is "dat"?
- H9 De conclusie staat vooraan: eerste zin na tabel of figuur zegt wat erin staat;
  eerste zin van elke `###` is de vraag of de bewering. Controle: per `###` en per tabel.
- H10 Abstracties krijgen een exemplaar in dezelfde zin. Controle: abstracte termen
  zonder voorbeeld.
- H11 Toy-getallen keren terug in Theorie (illustratie) en Simulatie (kalibratie).
  Controle: welke, en waar?
- H12 De intuïtie voorspelt (teken, richting) en de theorie zegt waar dat wordt ingelost.
  Controle: wat voorspelde de intuïtie, waar ingelost?
- Navertel-toets: na elke `##` (en in Theorie elke `###`) in twee of drie zinnen wat de
  sectie beweert; afwijking van de bedoeling is een helderheidsgebrek.

Taal (STYLE §11.1–11.5): zinnen gemiddeld ≤ 17 woorden, geen zin > 40, alinea ≤ 45
woorden gemiddeld, geen gedachtestreepjes, weinig puntkomma's, geen "u"/"je", geen
stopwoorden (precies, eigenlijk, natuurlijk, simpelweg), geen calques uit het Engels,
Engelse citaten geparafraseerd (≤ 5), hoogstens drie getallen per alinea.

## 6. Feitenregel en het bestand `notes/feiten-<slug>.md`

Een getal dat in de proza wordt aangehaald is gelijk aan de celuitvoer, of aan een
bron met citatie. Een getal zonder cel en zonder bron is "niet herleidbaar" en moet
worden geschrapt of gesourced. Jaartallen in "Waar we zijn" zijn verankerd in de tekst.
Bestand: statusregel, dan een tabel met kolommen nr | regel | bewering | oordeel
(juist / onjuist / onzeker / niet herleidbaar) | bron of cel | voorgestelde correctie.
Juiste rijen mogen per sectie worden samengevat. `open` = onjuist + onzeker + niet
herleidbaar.

## 7. Het bestand `notes/lezer-<slug>.md`

Statusregel; navertel-toets per sectie; H1–H12 met vindplaatsen (leeg waar niets is);
drie plekken waar het spoor kwijtraakte; vijftien gerangschikte punten, elk met
regelnummer, letterlijk citaat, probleem, concreet voorstel en het label
*herformuleren* of *toevoegen*. Belangrijkste eerst: een fout in een afleiding of toy
gaat vóór een stijlpunt.

## 8. Het bestand `notes/eind-<slug>.md` (eindbeoordelaar)

Statusregel (fase F6); de drie verbeteringen met het meeste effect met verwacht nieuw
deelcijfer; eindcijfer en tabel met zeven deelcijfers; per criterium *Goed*,
*Aanmerkingen* (kopje en zin letterlijk), *Beter uitleggen* en, onder 9, *Voor een 9*
met vindplaats; lijst "Feitelijke fouten" (nagerekend); navertelling in vijf zinnen.
Controle na F6b: sectie "Controle 1" onderaan met per punt opgelost / deels / niet /
verslechterd, nieuwe punten alleen bij verslechtering of feitelijke fout, opnieuw de
zeven deelcijfers, statusregel F6c bijgewerkt.

## 9. Praktisch (Windows)

Redirects via Bash, niet PowerShell (`>` schrijft een BOM). `PYTHONIOENCODING=utf-8`
als een script op de console crasht. Tempbestanden alleen met slug in de naam.
Uitvoeren met `HAP_OFFLINE=1`. Wijzig nooit een lecture in de rol van lezer of
beoordelaar.

## 10. Zuinig (workflow §10)

Je hebt een beurtbudget (staat in je opdracht). Lees het college één keer volledig
en daarna alleen `grep -n` of `sed -n` van hoogstens 40 regels. Nooit `.ipynb`,
nooit een pdf volledig, nooit bestanden uit de tool-results-map. Lange uitvoer
naar `$TEMP/<rol>-<slug>-*.txt` en daarvan alleen `head`/`grep` lezen. Wijzigingen
gebundeld (één script of één Write per sectie). Eindbericht: statusregel plus
hoogstens acht regels.

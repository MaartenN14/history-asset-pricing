# Werkstroom herziening: van 7,5 naar 8,5 tot 9 per lecture

Stand 2026-09-23, na de pilot L1 tot L4. Dit plan vervangt de werkorder in
`plannen/verbeterplan-didactiek.md` §5 voor alle volgende rondes. Wat daar staat over
nulmeting, verificatiecommando's en rapport blijft geldig, tenzij het hieronder anders
staat. Maatstaf: `plannen/rubriek-didactiek.md`, inclusief de sectie "Wat niet meetelt".
Regels: STYLE.md §11, inclusief §11.11 (lengte, schrappen en splitsen). Een volgende
sessie volgt dit plan letterlijk; de orkestrator vult alleen de plaatshouders van §2 in.

## 1. Fasen per lecture

F2 en F3 lopen parallel. F5 is een lus van hoogstens twee iteraties. S is een beslisstap
die alleen met de eigenaar wordt genomen.

| fase | rol | levert op | stopcriterium |
|---|---|---|---|
| F0 | schrijver | lengteplan in `notes/rapport-<slug>.md` | plan komt op ≤ 5.500 woorden, of splitsvoorstel |
| F1 | schrijver | lecture + rapport §F1 | `prose_stats --check` PASS inclusief words |
| F2 | feitencontroleur | `notes/feiten-<slug>.md` | elk getal en elke cross-ref heeft een status |
| F3 | koude lezer | `notes/lezer-<slug>.md` | één ronde, hoogstens 15 punten gerangschikt |
| F4 | schrijver | lecture + rapport §F4 | feitenlijst leeg, PASS, top tien lezerspunten afgehandeld |
| F5 | beoordelaar deel + schrijver | `notes/rating-<slug>.md` | ≥ 8,5 en geen deelcijfer < 8, of twee iteraties op |
| F6 | eindbeoordelaar | `notes/eind-<slug>.md` | cijfer van record |
| F7 | orkestrator | commit (§3.4) | alle criteria van §4.1 |
| S | schrijver + eigenaar | `notes/split-<slug>.md` | besluit eigenaar |

**F0. Nulmeting en lengteplan.** De schrijver meet, noemt de vijf grootste problemen en
maakt een schraplijst volgens de schraptoets van STYLE §11.11, met per passage het
geschatte aantal woorden. Hij wijzigt nog niets. Komt de lijst niet onder 6.000 woorden
zonder de kern te raken, dan fase S.
*Waarom:* in de pilot kwam lengte pas aan het eind ter sprake, toen elke lezer al om meer
had gevraagd; de lectures groeiden van 5.100 tot 6.700 naar 6.800 tot 8.100 woorden. Een
plan vooraf maakt elke latere toevoeging een ruil.

**F1. Herschrijven.** Dezelfde schrijver, in hetzelfde bericht: eerst schrappen, dan
plan §5 taak A en B, dan H1 tot H12. Doel 4.500 tot 5.300 woorden, zodat F4 en F5
ruimte houden. Aangehaalde getallen blijven gelijk, presentatie mag veranderen.
*Waarom:* één schrijver die zijn context houdt was goedkoper dan een verse agent.
"Uitvoer identiek" blokkeerde in de pilot kolomnamen, figuurtitels en `tail(3)`.

**F2. Feitencontrole.** Een nieuwe agent herleidt elk getal in de tekst tot een cel,
een handberekening of een citatie, controleert elke cross-ref en de consistentie met de
buurlectures. Hij wijzigt niets en geeft geen didactisch oordeel.
*Waarom:* de fouten uit de pilot (L1 "factor tien" en een fout interval, L2 "veertig
jaar" en 21/22 reeksen, L3 "anderhalve tiende procentpunt", L4 A,B,C,D dubbel) ontstonden
bij herschrijven. Lezers vonden ze niet; beoordelaars wel, ten koste van de didactiek.

**F3. Eén koude lezer.** Navertel-toets, H1 tot H12, drie sporen, en de vijftien
belangrijkste punten gerangschikt, elk *herformuleren* of *toevoegen*.
*Waarom:* verse lezers convergeren niet (L1 37 → 22, L2 41 → 29, L3 33 → 30, L4 63 → 37);
een tweede lezer kostte 100k tokens, verlengde de tekst en gaf geen meetbare cijferwinst.

**F4. Herstel.** De schrijver lost elke fout uit F2 op en minstens de eerste tien
lezerspunten, of wijst ze af met reden. Elk *toevoegen* wordt betaald met schrappen
elders.
*Waarom:* in de pilot sneuvelde de woordgrens als eerste.

**F5. Gesloten beoordelingslus.**
1. F5a: de beoordelaar van het deel beoordeelt met de rubriek, met per criterium onder 9
   wat nodig is voor een 9. Eindcijfer ≥ 8,5 en geen deelcijfer < 8: door naar F6.
2. F5b: anders lost de schrijver de punten op. De orkestrator bewaart vooraf een kopie
   van de lecture als ijkpunt.
3. F5c, parallel: de beoordelaar controleert alleen zijn eigen punten en geeft een nieuw
   cijfer; de feitencontroleur controleert alleen de diff tegen het ijkpunt.
4. Hoogstens twee iteraties van F5b en F5c. Daarna F6 bij ≥ 8,5, anders §4.3.

Bij de controle geeft de beoordelaar geen nieuwe punten, behalve verslechteringen en
feitelijke fouten. Anders wordt hij de verse lezer die niet convergeert.
*Waarom:* twee verschillende beoordelaars (L1 7,4 en 7,4; L2 7,0 en 7,4; L3 7,2 en 7,9;
L4 7,7 en 7,9) waren niet vergelijkbaar, dus verbetering was niet meetbaar. Dezelfde
beoordelaar meet wel verschil, en één beoordelaar per deel gaf consistente kalibratie.

**F6. Onafhankelijke eindbeoordeling.** Een nieuwe agent per deel beoordeelt alle
lectures van het deel zonder eerdere beoordelingen te zien, en schrijft een naadcontrole
over tegenspraken tussen lectures. Dit is het cijfer van record. Fouten en naadpunten
lost de schrijver op, de feitencontroleur controleert de diff, het cijfer blijft.
*Waarom:* een beoordelaar die zijn eigen punten ziet verdwijnen is niet onafhankelijk.
De naadcontrole vangt fouten zoals het Kendall-kader in L3 dat L2 tegensprak.

**S. Splitsen.** Wanneer: F0 komt niet onder 6.000 woorden, of na twee lus-iteraties
blijft het cijfer onder 8,5 met lengte of stofdichtheid als oorzaak. Procedure:
1. De schrijver schrijft `notes/split-<slug>.md` (hoogstens 30 regels): de naad volgens
   §11.11, de vraag van elke helft, welke stellingen, cellen en oefeningen waarheen, een
   voorstel voor slug en nummering, verhuisde labels, geschatte woorden per helft.
2. De orkestrator legt dat voor aan de eigenaar. Na akkoord splitst de schrijver, en de
   orkestrator werkt `myst.yml` en de cross-refs elders bij (grep op verhuisde labels).
3. De oude slug blijft bij de oude schrijver en gaat terug naar F1; de nieuwe helft
   krijgt een eigen schrijver, vanaf F1.
*Waarom:* splitsen raakt de nummering van het hele boek; dat beslist de eigenaar.

## 2. Prompts

Alle agents zijn verse Opus-agents (`general-purpose`, model `opus`), nooit een fork: een
fork erft de context van de orkestrator en kost daardoor meer. Vervolgberichten gaan met
`SendMessage` naar het agent-ID dat de orkestrator bij de start noteert.

Plaatshouders: `<slug>` (bijvoorbeeld `01_03_williams_ddm`), `<nr>` (3), `<kern>` (de vraag
en het antwoord uit het Overzicht, in één zin), `<vorige>` en `<volgende>` (slugs van de
buurlectures), `<deel>` (de lectures van het deel, als lijst van slugs), `<ijkpunt>` (pad
van de kopie die de orkestrator voor F5b maakte).

Elk bestand dat een agent schrijft, begint met één statusregel die de orkestrator leest
met `head -1`:

```
STATUS <slug> <fase> words=<n> prose=<PASS|FAIL> open=<n> cijfer=<x,x|-> min=<n|->
```

### 2.1 Schrijver, eerste bericht (F0 en F1)

> Je herziet `lectures/<slug>.md` (L<nr>). De kern van de lecture: <kern>.
>
> Lees eerst: `plannen/workflow-herziening.md` §1 en §2, STYLE.md volledig (vooral §11 en
> §11.11), `plannen/rubriek-didactiek.md` inclusief "Wat niet meetelt",
> `lectures/_template.md`, de lecture zelf, en van `lectures/<vorige>.md` en
> `lectures/<volgende>.md` alleen "Waar we zijn" en "Wat er brak". Bestaat
> `notes/rating2-<slug>.md`, lees dan ook die.
>
> **F0, nulmeting.** Wijzig nog niets. Draai:
> ```powershell
> uv run python tools/prose_stats.py lectures/<slug>.md
> uv run python tools/prose_stats.py --where lectures/<slug>.md
> git show HEAD:lectures/<slug>.ipynb > "$env:TEMP/voor-<slug>.ipynb"
> uv run python tools/nb_outputs.py "$env:TEMP/voor-<slug>.ipynb" > "$env:TEMP/voor-<slug>.txt"
> ```
> Schrijf in `notes/rapport-<slug>.md` (overschrijf het bestaande) de sectie "F0": de
> `prose_stats`-regel, de vijf grootste problemen met kopje en regel, en een schraplijst
> volgens de schraptoets van STYLE §11.11: per passage kopje, geschatte woorden, welke
> eis ze niet haalt. Tel op tot een verwachte lengte. Controleer eis 2 met grep op de
> labels in `lectures/`. Komt de lengte niet onder 6.000 zonder de kern te raken: schrijf
> `notes/split-<slug>.md` volgens `workflow-herziening.md` §1 fase S, stop, en meld dat.
>
> **F1, herschrijven.** Werk in deze volgorde: schrappen, dan plan §5 taak A (stappen 2
> tot en met 10), dan taak B, en pas H1 tot H12 toe. Doel 4.500 tot 5.300 woorden.
>
> Grenzen:
> - Alleen `lectures/<slug>.md`, `.ipynb` en je eigen `notes/rapport-<slug>.md` en
>   `notes/split-<slug>.md`. Niet committen, niet `jupyter book build` draaien.
> - Aangehaalde getallen blijven gelijk; kolomnamen, figuurtitels, celvolgorde mogen
>   veranderen. Een label dat ergens in `lectures/` wordt aangehaald, blijft bestaan.
> - Elk nieuw getal in de tekst komt uit een codecel of een getoonde handberekening.
>   Reken het na. Ontbreekt iets in `hap` of de bib: melden, niet oplossen.
>
> Verificatie, uitvoer samengevat in het rapport:
> ```powershell
> uv run python tools/prose_stats.py --check lectures/<slug>.md
> uv run jupytext --sync lectures/<slug>.md
> $env:HAP_OFFLINE = "1"
> uv run jupytext --execute --to ipynb lectures/<slug>.md
> uv run python tools/nb_outputs.py lectures/<slug>.ipynb > "$env:TEMP/na-<slug>.txt"
> git diff --no-index "$env:TEMP/voor-<slug>.txt" "$env:TEMP/na-<slug>.txt"
> ```
> `--check` moet PASS geven, ook op words. Een veranderd getal in de diff dat de tekst
> aanhaalt, is een fout.
>
> Rapport §F1, hoogstens 40 regels: eindmeting, geschrapte passages met één regel reden,
> de `nb_outputs`-diff met elk verschil benoemd, afvinklijst STYLE §11.9 (alleen wat niet
> voldoet), verdwenen of verhuisde labels, open punten. Zet bovenaan het rapport de
> statusregel uit `workflow-herziening.md` §2. Lees tot slot je eigen lecture één keer
> met de rubriek ernaast en los op wat je vindt. Eindbericht: hoogstens acht regels,
> beginnend met de statusregel.

### 2.2 Feitencontroleur (F2)

> Je controleert de feiten in `lectures/<slug>.md`. Je wijzigt niets.
>
> Lees de lecture, de uitvoer van `lectures/<slug>.ipynb` (via
> `uv run python tools/nb_outputs.py lectures/<slug>.ipynb`), `lectures/<vorige>.md` en
> `lectures/<volgende>.md` volledig, en van elke andere lecture waarnaar een cross-ref
> wijst alleen de aangehaalde plek.
>
> Schrijf `notes/feiten-<slug>.md`. Eerste regel: de statusregel uit
> `plannen/workflow-herziening.md` §2, met `open=` het aantal fout plus niet herleidbaar.
> Daarna één tabel met een rij per controle:
>
> | vindplaats (kopje) | bewering, letterlijk | bron | status | correct |
>
> Controleer:
> 1. elk getal in lopende tekst, bijschriften, admonitions en uitwerkingen: komt het uit
>    een celuitvoer, een getoonde handberekening of een citatie, en klopt het? Reken
>    omrekeningen na (procent, procentpunt, log-punt, jaren, factoren);
> 2. elk getal in een tabel in de tekst tegen de celuitvoer;
> 3. elke cross-ref: bestaat het label, en zegt de doellecture wat hier wordt beweerd?
> 4. consistentie met `<vorige>` en `<volgende>`: notatie, namen, jaartallen, aantallen
>    reeksen, wat daar over deze lecture of over hetzelfde onderwerp staat;
> 5. symbolen die in deze lecture twee betekenissen krijgen.
>
> Rijen met status ok per sectie samenvatten tot één regel. Geen stijladvies, geen
> didactisch oordeel. Eindbericht: de statusregel.

Vervolgbericht in F5c en F6:

> De schrijver heeft de lecture aangepast. Controleer alleen de wijzigingen:
> `git diff --no-index <ijkpunt> lectures/<slug>.md`, met dezelfde vijf controles. Voeg
> onderaan `notes/feiten-<slug>.md` een sectie "Diff <n>" toe en werk de statusregel bij.

### 2.3 Koude lezer (F3)

> Lees `lectures/<slug>.md` van voren naar achteren als een eerstejaars PhD-student die
> de eerdere lectures heeft gelezen maar niet paraat heeft. Lees verder alleen STYLE.md
> §11.10. Je wijzigt niets. Schrijf `notes/lezer-<slug>.md` met vier delen.
>
> 1. **Navertel-toets.** Na elke `##`-sectie, en in Theorie na elke `###`, twee of drie
>    zinnen: wat beweert de sectie en wat heb ik geleerd? Schrijf op wat je begreep, niet
>    wat er staat.
> 2. **De twaalf controles** H1 tot H12. Per regel de vindplaatsen: kopje en de zin,
>    letterlijk. Een lege lijst is ook een antwoord.
> 3. **Waar ik het spoor kwijtraakte.** Drie plekken, met de zin waar dat begon.
> 4. **De vijftien belangrijkste punten**, gerangschikt naar hoeveel ze het begrip
>    hinderen. Markeer elk punt als *herformuleren* (de informatie staat er, maar is niet
>    te volgen) of *toevoegen* (er ontbreekt een getal, naam of stap). Zeg bij *toevoegen*
>    in één regel wat precies ontbreekt.
>
> Geen stijlopmerkingen, geen wiskundige correcties, geen herschrijfvoorstellen. De tekst
> heeft een woordbudget; vraag niet om meer uitleg waar een betere zin volstaat.
> Eerste regel van het bestand: `STATUS <slug> F3 punten=<n>`. Eindbericht: die regel.

### 2.4 Schrijver, vervolgbericht F4

> F2 en F3 zijn klaar: `notes/feiten-<slug>.md` en `notes/lezer-<slug>.md`. Los elke
> rij met status fout of niet herleidbaar op. Los van de vijftien lezerspunten minstens
> de eerste tien op, of wijs ze af met één regel reden. Elk *toevoegen* betaal je met
> schrappen elders volgens de schraptoets; words blijft ≤ 5.500. Meld van de
> navertel-toets elke sectie die afweek en wat je veranderde. Zelfde verificatie en
> grenzen als F1. Rapport §F4, hoogstens 25 regels. Verwijder `notes/lezer-<slug>.md`
> niet; de orkestrator doet dat bij de commit. Eindbericht: statusregel, hoogstens acht
> regels.

### 2.5 Beoordelaar van het deel (F5a en F5c)

Eerste bericht, voor de eerste lecture van het deel:

> Je beoordeelt de lectures van dit deel volgens `plannen/rubriek-didactiek.md`,
> inclusief "Wat niet meetelt". Je krijgt ze één voor één. Houd je kalibratie gelijk:
> hetzelfde gebrek krijgt in elke lecture dezelfde aftrek. Bij twijfel geldt het lagere
> cijfer. Je wijzigt niets.
>
> Nu: `lectures/<slug>.md`. Lees van `<vorige>` en `<volgende>` alleen "Waar we zijn" en
> "Wat er brak". Schrijf `notes/rating-<slug>.md` in de vorm van de rubriek, met twee
> toevoegingen:
> 1. per criterium onder 9: "*Voor een 9*": wat er concreet moet veranderen, met
>    vindplaats;
> 2. een aparte lijst "Feitelijke fouten" (reken wat je tegenkomt na).
>
> Eerste regel: de statusregel uit `plannen/workflow-herziening.md` §2 met `cijfer=` en
> `min=` (het laagste deelcijfer). Eindbericht: die regel en de drie verbeteringen met
> het meeste effect, samen hoogstens tien regels.

Vervolgbericht voor de volgende lecture van de groep:
> Volgende lecture: `lectures/<slug>.md`, buren `<vorige>` en `<volgende>`. Zelfde
> opdracht en kalibratie.

Vervolgbericht voor de controle (F5c, iteratie <n>):

> De schrijver heeft `lectures/<slug>.md` aangepast op jouw punten; zijn verantwoording
> staat in `notes/rapport-<slug>.md` §F5-<n>. Controleer alleen je eigen punten: per punt
> opgelost / deels / niet / verslechterd. Nieuwe punten alleen bij een verslechtering of
> een feitelijke fout. Geef dan opnieuw de zeven deelcijfers en het eindcijfer. Voeg
> onderaan `notes/rating-<slug>.md` de sectie "Controle <n>" toe en werk de statusregel
> bij. Eindbericht: de statusregel en wat nog ontbreekt voor 8,5, hoogstens tien regels.

### 2.6 Schrijver, vervolgbericht F5b

> De beoordeling staat in `notes/rating-<slug>.md` (lees de laatste sectie). Los elke
> feitelijke fout op en elk punt onder "Aanmerkingen" en "Voor een 9", te beginnen bij de
> drie verbeteringen met het meeste effect. Wijs een punt alleen af met een regel uit
> STYLE of "Wat niet meetelt". Words blijft ≤ 5.500. Lees tot slot je lecture één keer
> met de rubriek ernaast. Zelfde verificatie en grenzen. Rapport §F5-<n>, hoogstens 25
> regels, per punt: gedaan of afgewezen met reden. Eindbericht: statusregel.

### 2.7 Eindbeoordelaar (F6)

> Je geeft het cijfer van record voor de lectures <deel>, volgens
> `plannen/rubriek-didactiek.md`, inclusief "Wat niet meetelt". Je hebt geen eerdere
> beoordeling gezien; lees ook geen bestanden in `notes/`, behalve om te schrijven.
> Je wijzigt niets. Bij twijfel geldt het lagere cijfer.
>
> Lees de lectures in volgorde. Lees van de lecture vóór en na het deel alleen "Waar we
> zijn" en "Wat er brak". Schrijf per lecture `notes/eind-<slug>.md` in de vorm van de
> rubriek, met een lijst "Feitelijke fouten" en een navertelling in vijf zinnen. Eerste
> regel: de statusregel uit `plannen/workflow-herziening.md` §2.
>
> Schrijf daarna `notes/eind-deel-<n>.md`: elke tegenspraak tussen lectures (een getal,
> een naam, notatie, een bewering over een andere lecture), met beide vindplaatsen.
> Houd één kalibratie voor het hele deel. Eindbericht: per lecture één regel met
> eindcijfer en laagste deelcijfer, en het aantal naadpunten.

Bij een deel met meer dan vijf lectures krijgt de tweede eindbeoordelaar er een zin bij:

> Lees als kalibratie-anker eerst `notes/eind-<a>.md` en `notes/eind-<b>.md` van de vorige
> groep, alleen de cijfertabel en de aanmerkingen.

## 3. Wat de orkestrator doet, en niets meer

De orkestrator leest geen lectures of volledige rapporten, alleen statusregels,
eindberichten en zijn eigen controles. Doel: hoogstens 40k tokens per lecture.

### 3.1 Starten en hervatten

1. Per lecture: `<kern>` bepalen uit de eerste 30 regels van het Overzicht, of voor een
   lecture uit de pilot uit de navertelling in `notes/rating2-<slug>.md`.
2. F0/F1 starten met prompt 2.1; het agent-ID noteren in een tabel in zijn eigen context.
3. Na F1: controles 3.2, dan F2 en F3 tegelijk starten.
4. Na F2 en F3: prompt 2.4 als vervolgbericht aan de schrijver.
5. Na F4: controles 3.2; F5a starten of de beoordelaar een vervolgbericht sturen.
6. Lus: vóór elk F5b `Copy-Item lectures/<slug>.md <scratchpad>/<slug>-ijk-<n>.md`, dan
   2.6 aan de schrijver; na F5b controles 3.2, dan 2.5 (controle) en 2.2 (diff) tegelijk.
7. Wanneer alle lectures van de groep F5 hebben verlaten: build (3.3), dan F6.

Een vastgelopen agent wordt vervangen door een nieuwe met dezelfde prompt en de zin
"Lees eerst `notes/rapport-<slug>.md`; je gaat verder bij fase <fase>."

### 3.2 Controles na elke schrijversfase

```bash
uv run python tools/prose_stats.py --check lectures/<slug>.md
head -1 notes/rapport-<slug>.md
# labels die verdwenen zijn, en of ze elders worden aangehaald
comm -23 <(git show HEAD:lectures/<slug>.md | grep -oE '^\([^)]+\)=|:label: *[^ ]+' | sed -E 's/^\(|\)=$|:label: *//g' | sort -u) \
         <(grep -oE '^\([^)]+\)=|:label: *[^ ]+' lectures/<slug>.md | sed -E 's/^\(|\)=$|:label: *//g' | sort -u) \
  | while read l; do echo "weg: $l"; grep -rln -- "$l" lectures/ ; done
# getallen in de uitvoer: alleen tellen
uv run python tools/nb_outputs.py lectures/<slug>.ipynb > "$TEMP/na-<slug>.txt"
git diff --no-index --stat "$TEMP/voor-<slug>.txt" "$TEMP/na-<slug>.txt"
```

- FAIL in `prose_stats`: de schrijver krijgt de regel terug, niets anders.
- Een verdwenen label dat elders wordt aangehaald: terug naar de schrijver.
- Een niet-lege `nb_outputs`-diff: alleen de sectie `nb_outputs` van het rapport lezen.
  Staat elk verschil daar als bedoeld, dan door.

### 3.3 Build, één per deel

Nulmeting vóór de groep, echte build na F5. Alleen de orkestrator bouwt (geheugenfouten).
```powershell
uv run jupyter book build --html 2>&1 | Select-String -Pattern "⛔|⚠" | Out-File -Encoding utf8 "$env:TEMP/warn-voor-<n>.txt"
uv run jupyter book build --html 2>&1 | Select-String -Pattern "⛔|⚠" | Out-File -Encoding utf8 "$env:TEMP/warn-na-<n>.txt"
git diff --no-index "$env:TEMP/warn-voor-<n>.txt" "$env:TEMP/warn-na-<n>.txt"
```

Een nieuwe warning gaat met de regel zelf naar de schrijver van die lecture. Een tweede
build alleen als F6 tot wijzigingen leidde.

### 3.4 Commit en push

Per lecture, na F6 en eventueel herstel, met expliciete paden (andere agents werken nog):

```powershell
git rm -q --ignore-unmatch notes/rating2-<slug>.md notes/lezer-<slug>.md
git add lectures/<slug>.md lectures/<slug>.ipynb notes/rapport-<slug>.md notes/feiten-<slug>.md notes/rating-<slug>.md notes/eind-<slug>.md
git commit -m "L<nr> <slug>: herzien volgens workflow-herziening (eindcijfer <x,x>)" -m "<prose_stats-regel>`nLus: <cijfer F5a> -> <cijfer laatste controle>. Eind: <x,x>, laagste deelcijfer <n>."
```

Onder het bericht de Co-Authored-By-regel die de sessie voorschrijft. Na de laatste
lecture van het deel: `notes/eind-deel-<n>.md` en eventueel `myst.yml` apart committen,
dan `git push`. Nooit `git add -A`.

### 3.5 Voorleggen aan de eigenaar

Alleen deze vier gevallen, elk in hoogstens vijf regels met de opties. De andere
lectures lopen intussen door.

1. een splitsvoorstel (fase S);
2. na twee lus-iteraties < 8,5 zonder lengte als oorzaak (§4.3);
3. een schrijver of beoordelaar die een regel uit STYLE of de rubriek aanwijst als
   oorzaak van een aftrek die hij niet kan oplossen (regelconflict);
4. een budget boven het plafond van §4.4.

## 4. Stopcriteria en budget

### 4.1 Een lecture is klaar als

1. het eindcijfer van F6 ≥ 8,5 is;
2. geen deelcijfer in F6 onder 8 ligt;
3. `prose_stats --check` PASS geeft, inclusief words ≤ 5.500;
4. de build van het deel geen nieuwe warning voor deze lecture geeft;
5. `notes/feiten-<slug>.md` `open=0` heeft, ook na de laatste diff;
6. geen naadpunt uit `notes/eind-deel-<n>.md` voor deze lecture openstaat.

### 4.2 F6 lager dan F5

Dan telt F6. De schrijver lost de drie verbeteringen uit `notes/eind-<slug>.md` op
(prompt 2.6 met dat bestand); de eindbeoordelaar controleert alleen die punten (prompt
2.5, controle). Eén keer. Blijft het onder 8,5: §4.3.

### 4.3 Na twee iteraties onder 8,5

De orkestrator kijkt naar de laatste controle van de beoordelaar:
- noemt die lengte, stofdichtheid of twee modellen in één lecture: fase S;
- noemt die een projectkeuze of regel: voorleggen als regelconflict;
- anders: voorleggen met het cijfer, de drie resterende punten en de keuze tussen
  accepteren en één derde iteratie.
In alle gevallen wordt de lecture gecommit als "... (tussenstand <x,x>)".

### 4.4 Budget per lecture

| rol | fasen | tokens | tijd |
|---|---|---|---|
| schrijver | F0, F1, F4, F5b ×2 | 0,9 tot 1,3M | 90 tot 120 min |
| feitencontroleur | F2 + 2 diffs | 130 tot 180k | 25 min |
| koude lezer | F3 | 90 tot 105k | 20 min |
| beoordelaar deel | F5a + 2 controles | 120 tot 140k | 30 min |
| eindbeoordelaar | F6, per lecture | 60 tot 70k | 15 min |
| orkestrator | alles | ≤ 40k | |
| **totaal** | | **1,3 tot 1,8M** | **3 tot 3,5 uur doorlooptijd** |

Richtbudget 1,5M per lecture, plafond 2M. De pilot kostte 1,5 tot 2,1M (vier
schrijversrondes, twee lezers, twee beoordelaars) en leverde geen 8,5. Per groep van vier
of vijf lectures, parallel: 6 tot 9M tokens en 4 tot 5 uur, inclusief build en F6.

## 5. Volgorde voor het boek

| groep | lectures | eindbeoordelaar |
|---|---|---|
| 1 | L1 tot L4 (Deel 0 en I, opnieuw) | één |
| 2 | L5 tot L9 (Deel II) | één |
| 3a, 3b | L10 tot L13, L14 tot L17 (Deel III) | twee, 3b met anker uit 3a |
| 4a, 4b | L18 tot L21, L22 tot L25 (Deel IV) | twee, 4b met anker |
| 5a, 5b | L26 tot L29, L30 tot L33 (Deel V) | twee, 5b met anker |
| 6 | L34 tot L37 (Deel VI en VII) | één |
| 7 | L38, L39 (synthese, verwijzen naar alles) | één |

L0 (setup) valt buiten de rubriek, tenzij de eigenaar anders beslist. Per groep:
- **Parallel:** F0 tot en met F4 voor alle lectures; F2 en F3 per lecture tegelijk;
  F5b van de ene lecture naast F5a van een andere.
- **Serieel:** de beoordelaar van de groep neemt de lectures één voor één (één agent,
  één kalibratie). De build na F5 wacht op alle lectures. F6 leest het hele deel.
- **Tussen groepen:** de volgende groep start pas na de push, zodat `<vorige>` van de
  eerste lecture de herziene versie is. Elke groep heeft een eigen beoordelaar (F5).
- **Na groep 1:** de eigenaar bekijkt de vier eindcijfers en de budgetten vóór groep 2
  start. Wijkt het budget meer dan 30% af, dan wordt §4.4 bijgesteld.

## 6. Wat anders is dan in de pilot, en waarom

| pilot | nieuw | waarom |
|---|---|---|
| Geen lengteplan; schrappen verboden | F0 met schraptoets; words ≤ 5.500 bindend; splitsen boven 6.000 | Lectures groeiden naar 6.800 tot 8.100 woorden; QuantEcon zit op 2.000 tot 3.500 |
| Twee verse koude lezers | Eén lezer, vijftien punten gerangschikt, *toevoegen* kost woorden | Verse lezers convergeren niet: 20 tot 30 nieuwe punten per ronde |
| Geen feitencontrole | F2 als aparte rol, plus controle van elke diff | Fouten ontstonden bij herschrijven; alleen beoordelaars vonden ze |
| Twee losse beoordelaars | Gesloten lus met één beoordelaar, dan één onafhankelijke eindbeoordeling | Twee beoordelaars waren niet vergelijkbaar; verbetering was niet meetbaar |
| Aftrek voor projectkeuzes | Rubriek "Wat niet meetelt" | Kostte in alle vier ongeveer een half punt |
| Uitvoer identiek | Aangehaalde getallen gelijk, presentatie vrij (§11.11) | Blokkeerde kolomnamen, figuurtitels, `tail(3)` en een overbodige toy-stap |
| "Naar een 9" pas na de beoordeling | "Voor een 9" per criterium in elke beoordeling | De schrijver weet vanaf F5a waar het punt zit |
| Geen naadcontrole | Eindbeoordelaar leest het hele deel en meldt tegenspraken | L3 sprak L2 tegen over Kendall |
| Vaste namen `voor.txt`, `na.txt` | `voor-<slug>.txt`, `na-<slug>.txt` | Parallelle schrijvers konden elkaars bestand overschrijven |
| Rapport lezen om de stand te kennen | Statusregel bovenaan elk bestand | Houdt de orkestrator onder 40k tokens per lecture |

Blijft: één schrijver per lecture met vervolgberichten, vier of vijf lectures parallel,
`prose_stats` en `nb_outputs` als harde poort, de schrijver die zijn werk met de rubriek
naleest, en een orkestrator die alleen meet, bouwt en commit.

## 7. Eerste doorloop van Deel I: wat al klaarligt

Voor L1 tot L4 bestaan al `notes/feiten-<slug>.md` (feitencontrole van 2026-09-23 op de
gepushte versie, 16 / 23 / 15 / 18 punten) en `notes/rating2-<slug>.md`. De schrijver
krijgt die lijsten in F0 als invoer en verwerkt ze in F1, samen met het schrappen. F2 draait
daarna opnieuw op de nieuwe tekst en overschrijft `notes/feiten-<slug>.md`; de oude lijst
is dan verwerkt en hoeft niet bewaard te blijven.

## 8. Modelkeuze per rol (besluit 2026-09-24)

Schrijver, beoordelaar en eindbeoordelaar draaien op Opus. Koude lezer (F3) en
diff-controles (F5c, F6, mini-rondes) draaien op Sonnet: lezen en mechanisch nakijken
verliezen daar geen kwaliteit, en het ontlast de Opus-sessielimiet. De volledige
feitencontrole (F2) gaat vanaf Deel III op proef naar Sonnet; de beoordelaar houdt zijn
eigen lijst "Feitelijke fouten". Vindt hij vanaf dan meer feitelijke fouten dan in Deel I
en II, dan gaat F2 terug naar Opus.

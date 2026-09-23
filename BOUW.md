# BOUW.md — instructie voor bouw-agents

Je bouwt precies één lecture uit `PLAN.md` §3. Andere agents bouwen tegelijkertijd andere lectures in
dezelfde repo. Werk daarom uitsluitend in je eigen bestanden en volg de regels hieronder letterlijk.

**Herzie je een bestaande lecture** (taal en didactiek), dan geldt de werkorder in
`plannen/verbeterplan-didactiek.md` §5 in plaats van §1 en §4 hieronder. STYLE.md §11 is daarbij bindend;
`uv run python tools/prose_stats.py --check lectures/<slug>.md` moet PASS geven vóór oplevering.

## 0. Omgeving

- Project: `C:\Users\Maarten\Desktop\projects\history-asset-pricing` (Windows). Alle Python/Jupyter-commando's via `uv run ...`.
- Lees vóór je begint, volledig: `PLAN.md` (inhoud en rode draad), `STYLE.md` (vorm — bindend), `lectures/_template.md`
  (kopieer dit als startpunt), `data/README.md` (databronnen) en de docstrings van `hap`:
  `uv run python -c "import hap, inspect; print(inspect.getsource(hap.data))"` en idem voor `hap.stats`, `hap.plotting`.
- Lees ook `lectures/index.md` en, als ze al bestaan, de lecture vóór en na de jouwe (voor aansluiting van de rode draad).

## 1. Inhoudelijke eisen

- Taal: Nederlands (zie STYLE.md §3 voor Engelse vaktermen). Code en docstrings Engels.
- Niveau: PhD-wiskunde, intuïtie voorop. Elke afleiding begint met "*Waarom zou dit waar zijn?*".
- Didactische trap verplicht: toy-voorbeeld (handrekenbaar, code reproduceert exact dezelfde getallen) → theorie →
  simulatie op schaal (met figuur, over steekproeven) → replicatie op echte data (met replicatieblok, STYLE.md §6).
- Bronpapers: lees vóór het schrijven de abstracts/inleidingen van de kernpapers (WebFetch/WebSearch: SSRN, NBER,
  auteurspagina's, JSTOR-abstracts, Wikipedia als laatste redmiddel) zodat je de gepubliceerde getallen (tabellen,
  t-waarden, steekproefperiodes) correct citeert. Noem gepubliceerde getallen letterlijk en zeg waar ze staan.
  Verzin geen getallen of citaten; als je iets niet kunt verifiëren, zeg dat in de tekst.
- Elke geciteerde bron heeft een key in `references.bib`. Ontbreekt een entry: voeg hem **onderaan** toe volgens
  STYLE.md §8 (DOI via Crossref geverifieerd; nooit verzonnen). Lees het bestand opnieuw vlak voor je het bewerkt —
  andere agents voegen ook entries toe. Verwijder of herschrijf nooit bestaande entries (behalve het weghalen van
  een `TODO verify`-note nadat je die entry hebt geverifieerd).
- Cross-refs naar de vorige/volgende lecture gebruiken de paginalabels uit STYLE.md §4 (`<deel>-<nr>-<slug>`,
  bijv. `02-08-capm`), ook als die lecture nog niet bestaat. Een build-warning over zo'n nog-niet-bestaand label is
  toegestaan; meld hem in je rapport.
- Rode draad: het blok "Waar we zijn in het verhaal" en "Wat er brak, en wat daarna kwam" sluiten aan op de
  buurlectures in PLAN.md §3 en op de motieven in PLAN.md §2 / STYLE.md §2.

## 2. Bestanden die je mag aanraken

| Bestand | Wat |
|---|---|
| `lectures/<slug>.md` en `lectures/<slug>.ipynb` | jouw lecture (gepaard via jupytext) |
| `myst.yml` | **alleen** het commentaarteken weghalen voor jouw `- file:`-regel (en het `- title:`-blok van jouw deel als dat nog uitgecommentarieerd is). Geen andere wijzigingen. Lees het bestand opnieuw vlak voor je het bewerkt. |
| `references.bib` | alleen entries toevoegen onderaan (zie §1) |
| `data/cache/` | nieuwe parquet-bestanden die jouw loader-aanroepen aanmaken; verwijder of overschrijf nooit bestaande |

Raak **niet** aan: `src/hap/`, `STYLE.md`, `PLAN.md`, `BOUW.md`, `lectures/_template.*`, `lectures/index.md`,
andermans lectures, `pyproject.toml`, `tests/`. Mis je een loader of statistiekfunctie: lokale implementatie in je
lecture met `# TODO: naar hap.stats` en meld het in je rapport. Installeer geen pakketten.

## 3. Data

- Uitsluitend via `hap.data.*`. Eerste keer online draaien mag (vult de cache); daarna moet de lecture volledig
  draaien met `HAP_OFFLINE=1`. Kijk eerst of wat je nodig hebt al in `data/cache/` staat (`hap.cache`).
- Geen CRSP/Compustat/WRDS. Waar de data niet gratis is: simulatie, expliciet benoemd in het replicatieblok.
- Elke cel < 60 s.

## 4. Verificatie vóór oplevering (verplicht, in deze volgorde)

```bash
uv run jupytext --sync lectures/<slug>.md
set HAP_OFFLINE=1   # PowerShell: $env:HAP_OFFLINE="1" ; bash: HAP_OFFLINE=1 uv run ...
uv run jupytext --execute --to ipynb lectures/<slug>.md     # foutloos, geen warnings in de output
uv run jupyter book build --execute --html                   # voert Python-cellen uit en toont hun uitvoer in de HTML
Copy-Item custom.css _build\html\myst-theme.css -Force      # QuantEcon-thema neemt custom CSS nog niet zelf over
Copy-Item THIRD_PARTY_NOTICES.md _build\html\THIRD_PARTY_NOTICES.md -Force
uv run python -m http.server 8080 --bind 127.0.0.1 --directory _build\html  # open http://localhost:8080, niet via file:///...
```

Faalt de build door een bestand van een andere agent, negeer dat en meld het. Loop daarna STYLE.md §10
(de afvinklijst) zelf langs en herstel wat niet klopt. Tel de woorden lopende tekst (excl. code/output).

## 5. Oplevering

Commit niets. Rapporteer beknopt (max ~40 regels):
1. bestand(en) en woordenaantal;
2. welke paperresultaten je hebt gerepliceerd en hoe dicht je erbij zat (met de getallen);
3. de ingevulde afvinklijst van STYLE.md §10 (alleen de punten die NIET voldoen uitschrijven, plus "overige: ok");
4. toegevoegde bib-entries en TODO's;
5. build-warnings die overblijven (met reden);
6. ontbrekende `hap`-functionaliteit.

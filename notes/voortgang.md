# Voortgang lectures (stand 2026-09-13)

## Status

Alle 40 lectures (L0–L39) zijn geschreven, offline uitgevoerd (`HAP_OFFLINE=1`) en gecommit, elk met de
cachebestanden die ze gebruiken.

## Openstaande punten

- **Inhoudsopgave `.md` vs `.ipynb`.** `myst.yml` verwijst voor L0–L22 naar `.ipynb` en vanaf L23 naar `.md`.
  Met `.ipynb` breken verwijzingen naar oefeningen waarvan de uitwerking codecellen bevat. Advies: overal `.md`.
  Beslissing gebruiker nodig.
- **Volledige build.** Aan het eind één keer `jupyter book build --execute --html` draaien en warnings nalopen;
  parallelle builds gaven MemoryErrors.
- **Lengte.** Diverse lectures liggen boven 6000 woorden als tabellen, bijschriften en oefeningen meetellen.
- **Achteraf aangepaste verwachting.** L25 (indexfondsen): de "verwachte afwijking" is na de eerste run herschreven;
  advies: oorspronkelijke voorspelling terugzetten en VFINX als afwijking bespreken. L36: verwachting van de
  S&P 500-inclusie-event-study geschreven na een prototype-run.
- **Citaten Santa-Clara.** In L37–L39 deels via samenvattende WebFetch geverifieerd; controleer tegen de post.
- **Kandidaten voor `hap`.** `hap.stats`: runs-test (L2), event-study-toetsen (L7, L37), VAR (L10), Sharpe-SE en
  rollende backtest (L4, L30, L29), Shanken-correctie en lineaire SDF-GMM (L8, L26, L32), Hodrick-SE (L20, L32),
  Kupiec/Christoffersen (L22), multiple testing en empirical Bayes (L25, L34), panel met vaste effecten (L30, L34),
  OOS R²/Diebold-Mariano (L35). Snellere `fama_macbeth`. `hap.data`: splits/dividenden via yahoo (L7),
  Pástor-Stambaugh-liquiditeit (L24), CFO-enquête (L33), Svensson-helper bij `gsw` (L28).
- **Onderzoeksnotities** in `notes/` (L4, L34, L35) zijn verwerkt en kunnen weg.

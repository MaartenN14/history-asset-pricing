# Databronnen

Alle data in dit project is **gratis en publiek**. Elke bron wordt gedownload door een
loader in `src/hap/data.py` en als parquet-snapshot weggeschreven naar `data/cache/`.
Die snapshots zijn **gecommit**: een verse clone kan elke lecture draaien zonder netwerk.

```python
import hap
ff3 = hap.french("F-F_Research_Data_Factors")   # leest data/cache/
```

| Variabele | Effect |
|---|---|
| `HAP_OFFLINE=1` | Nooit downloaden; ontbrekende snapshot geeft `hap.CacheMissError`. De testsuite draait zo. |
| `HAP_REFRESH=1` | Altijd opnieuw downloaden en de snapshot overschrijven. |
| *(niets gezet)* | Download alleen als het parquet-bestand ontbreekt. Snapshots verlopen dus nooit vanzelf. |

**Conventies (gelden voor alle loaders).** `DatetimeIndex` met naam `date`; maanddata op
**maandeinde**, kwartaal op kwartaaleinde, jaar op jaareinde, dagdata op de handelsdatum.
Rendementen én yields zijn **decimalen, geen procenten** (1,5% = `0.015`). Niveaureeksen
(prijzen, indices, CPI, aantallen bedrijven) houden hun eigen eenheid. Bronsentinels
(`-99.99`, `-999`, `.`) worden `NaN`.

**Uitzondering:** `hap.fred()` geeft FRED's eigen eenheden terug (rentes dus in procenten),
omdat de eenheid per serie verschilt. Deel zelf door 100 waar nodig.

Snapshotdatum van alles hieronder: **2026-09-07**. Cachegrootte: **~18 MB** over 72 parquet-bestanden.

---

## Kenneth French Data Library — `hap.french(name, freq, table, percent)`

* **URL** `https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/<name>[_daily]_CSV.zip`
* **Homepage** <https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>
* **Licentie** Vrij te gebruiken voor onderzoek en onderwijs; bronvermelding gevraagd.
  Onderliggende returns komen uit CRSP/Compustat; alleen de geaggregeerde portefeuilles zijn publiek.
* **Automatisch?** Ja, volledig.
* **Periode** 1926-07 – 2026-07 (maandelijks), 1926-07-01 – 2026-07-31 (dagelijks);
  FF5 vanaf 1963-07, E-P vanaf 1951-07, momentum vanaf 1927-01, LT reversal vanaf 1931-01.

Een French-CSV bevat **meerdere tabellen achter elkaar** (value weighted, equal weighted,
jaarlijks, aantal bedrijven, gemiddelde marktkap, BE/ME). Tabel `0` is altijd de
value-weighted maand-/dagtabel en is de default. Gebruik `hap.french_tables(name, freq)`
om de titels te zien en `table="Equal Weight"` (substring) of `table=4` (index) om te kiezen.
De `percent`-vlag wordt afgeleid uit de titel: returntabellen worden door 100 gedeeld,
tabellen met aantallen/marktkap/BE-ME niet. Overschrijf met `percent=True/False`.

Snapshots in de cache (maandelijks value- én equal-weighted; `F-F_*` alleen value-weighted):

`F-F_Research_Data_Factors` (Mkt-RF, SMB, HML, RF) · `F-F_Research_Data_5_Factors_2x3`
(+RMW, CMA) · `F-F_Momentum_Factor` (Mom) · `F-F_ST_Reversal_Factor` · `F-F_LT_Reversal_Factor` ·
`25_Portfolios_5x5` (size × BE/ME) · `Portfolios_Formed_on_ME` · `Portfolios_Formed_on_BE-ME` ·
`Portfolios_Formed_on_E-P` · `10_Industry_Portfolios` · `6_Portfolios_ME_Prior_12_2` (momentum) ·
`6_Portfolios_ME_Prior_60_13` (long-term reversal).
Daily: `F-F_Research_Data_Factors`, `F-F_Momentum_Factor`, `F-F_Research_Data_5_Factors_2x3`.

Gemak: `hap.market_monthly()` en `hap.market_daily()` geven `Mkt-RF`, `RF` en `Mkt`.

## Robert Shiller — `hap.shiller()`

* **URL** <https://shillerdata.com/> (`ie_data.xls`; de link wordt van de pagina gescrapet,
  want het bestand staat achter een wisselende CDN-URL). Fallback:
  <http://www.econ.yale.edu/~shiller/data/ie_data.xls> — die kopie loopt achter (t/m 2023).
* **Licentie** Vrij beschikbaar gesteld door Shiller bij *Irrational Exuberance*.
* **Automatisch?** Ja. Vereist `xlrd` (legacy `.xls`).
* **Periode** 1871-01 – 2026-09 (1869 maanden, 21 kolommen).
* **Kolommen** `price`, `dividend`, `earnings`, `cpi`, `long_rate` (GS10, decimaal),
  `real_price`, `real_dividend`, `real_earnings`, `real_total_return_price`,
  `real_tr_scaled_earnings`, `cape`, `tr_cape`, `excess_cape_yield`,
  `monthly_total_bond_return`, `real_total_bond_return`, `stock_real_return_10y`,
  `bond_real_return_10y`, `excess_real_return_10y`, plus afgeleid `pd_ratio`, `dp`, `ep`.
* **Let op** De laatste één à twee maanden zijn voorlopig (Shiller gebruikt de slotkoers van
  de eerste van de maand) en `dividend`/`earnings` ontbreken daar.

## Goyal-Welch predictors — `hap.goyal_welch(freq)`

* **URL** <https://docs.google.com/spreadsheets/d/1qwpl2R_DNujpU5YUkk8lacP1tTeMb9iJ/export?format=xlsx>
  (de Google-Sheets-link van Amit Goyals pagina met `/edit…` vervangen door `/export?format=xlsx`).
* **Homepage** <https://sites.google.com/view/agoyal145>
* **Licentie** Vrij voor academisch gebruik; citeer Welch & Goyal (2008, RFS) en de update.
* **Automatisch?** Ja. Als de export-URL ooit breekt: download het werkboek handmatig van de
  homepage en zet het neer als `data/raw/PredictorData.xlsx`; de loader pakt het dan op.
* **Periode** monthly 1871-01 – 2025-12 (1860 rijen), quarterly 1871Q1 – 2025Q4, annual 1871 – 2025.
* **Ruwe kolommen** `Index`, `D12`, `E12`, `b/m`, `tbl`, `AAA`, `BAA`, `lty`, `ntis`, `Rfree`,
  `infl`, `ltr`, `corpr`, `svar`, `csp`, `CRSP_SPvw`, `CRSP_SPvwx` (rentes al als decimalen).
* **Afgeleid** `dp` = log D12 − log Index · `dy` = log D12 − log Index(t−1) · `ep` = log E12 − log Index ·
  `de` = log D12 − log E12 · `tms` = lty − tbl · `dfy` = BAA − AAA · `dfr` = corpr − ltr ·
  `equity_premium` = log(1+CRSP_SPvw) − log(1+Rfree).

## FRED — `hap.fred(series, start=None)`

* **URL** `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<series>` — geen API-key.
* **Licentie** Grotendeels publiek domein; sommige series hebben beperkingen van de
  oorspronkelijke aanbieder (zie de FRED-pagina per serie).
* **Automatisch?** Ja. Eén parquet per serie.
* **Eenheden** FRED's eigen: rentes en yields in **procenten**.
* **Gecachte series** `USREC` (NBER-recessies, 1854–), `VIXCLS`, `CPIAUCSL`, `PCECC96`, `PCEC96`,
  `GDPC1`, `DGS10`, `DGS1`, `DGS3MO`, `TB3MS`, `FEDFUNDS`, `BAA`, `AAA`, `BAA10Y`, `T10Y2Y`,
  `TEDRATE`, `DEXUSEU`, `DEXJPUS`, `DEXUSUK`, `DTWEXBGS`, `UNRATE`, `INDPRO`, `M2SL`,
  `NCBEILQ027S` (flow of funds, huishoudens aandelenbezit).
  Elke andere serie werkt ook, maar vereist één keer online zijn.

## Gürkaynak-Sack-Wright zero-coupon yields — `hap.gsw()`

* **URL** <https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv>
  (pagina: <https://www.federalreserve.gov/data/yield-curve-tables/feds200628_1.html>)
* **Licentie** Publiek domein (Federal Reserve Board). Citeer Gürkaynak, Sack & Wright (2007, JME).
* **Automatisch?** Ja.
* **Periode** 1961-06-14 – 2026-08-28, dagelijks, 99 kolommen.
* **Kolommen** `SVENYnn` zero-coupon yield op nn jaar · `SVENFnn` instantane forward ·
  `SVENPYnn` par yield · `SVEN1Fnn` 1-jaars forward · `BETA0`–`BETA4`, `TAU1`, `TAU2`
  (Svensson-parameters).
* **Eenheden** `SVEN*` en `BETA*` zijn door 100 gedeeld (dus decimalen), zodat de
  Svensson-formule de yields nog steeds reproduceert. `TAU1`/`TAU2` staan in jaren.
  Vroege jaren: lange looptijden zijn `NaN`.

## Open Source Asset Pricing — `hap.osap(kind)`

* **Homepage** <https://www.openassetpricing.com/data/> (Chen & Zimmermann)
* **URL's** Google Drive, maar downloadbaar met een gewone GET:
  * portfolios: `https://drive.google.com/uc?export=download&id=10sOryk_ddjkXagaajTKUk1nwJs2ZLRiI` (`PredictorLSretWide.csv`)
  * signaldoc: `https://drive.google.com/uc?export=download&id=1Sev9s6cPFUGgxp1pFiej0lGzpsMqJCI2` (`SignalDoc.csv`)
* **Licentie** Open source (MIT-achtig); citeer Chen & Zimmermann (2022, *Critical Finance Review*).
* **Automatisch?** Ja. **Fallback als Drive ooit een bevestigingspagina serveert:** download
  de twee CSV's handmatig van de homepage en zet ze in `data/raw/` onder precies die namen.
* **`kind="portfolios"`** 1926-01 – 2024-12, 1188 maanden × 212 signalen, long-short returns als
  decimalen, opgeslagen als `float32` om de snapshot klein te houden (~1 MB).
  Extreme waarden zijn echt (bv. `IO_ShortInterest` +321% in 2021-01, de GameStop-maand).
* **`kind="signaldoc"`** 331 rijen, geïndexeerd op publicatiejaar (jaareinde). Kolommen o.a.
  `signal`, `Authors`, `Year`, `Journal`, `SampleStartYear`, `SampleEndYear`, `Cat.Signal`
  (Predictor/Placebo/Indirect), `Sign`, `Return`, `T-Stat`, `LS Quantile`, `Stock Weight`.
  Precies wat je nodig hebt voor McLean-Pontiff-stijl post-publicatiedecay.

## He-Kelly-Manela intermediary capital — `hap.hkm(freq)`

* **Homepage/URL** <https://zhiguohe.net/data-and-empirical-patterns/intermediary-capital-ratio-and-risk-factor/>.
  De bestandsnaam draagt een versiestempel (`He_Kelly_Manela_Factors_monthly_250627.csv`), dus
  de loader **scrapet de pagina** voor de actuele link in plaats van hem hard te coderen.
  De oude `voices.uchicago.edu`- en `asafmanela.github.io`-URL's zijn dood respectievelijk 403.
* **Licentie** Vrij voor academisch gebruik; citeer He, Kelly & Manela (2017, JFE).
* **Automatisch?** Ja. Fallback: leg `He_Kelly_Manela_Factors_monthly.csv` (of `_quarterly`) in `data/raw/`.
* **Periode** monthly 1970-01 – 2025-05 (665 rijen), quarterly 1970Q1 – 2025Q1.
* **Kolommen** `intermediary_capital_ratio`, `intermediary_capital_risk_factor`,
  `intermediary_value_weighted_investment_return`, `intermediary_leverage_ratio_squared`.
* **Let op** Het gepubliceerde bestand bevat een dubbele maand (2025-01) met twee verschillende
  waarden; de loader houdt de laatste rij.

## Yahoo Finance — `hap.yahoo(...)`, `hap.yahoo_options(...)`

* **Bron** yfinance (unofficial Yahoo API).
* **Licentie** Yahoo's gebruiksvoorwaarden: persoonlijk/niet-commercieel gebruik. Niet
  herdistribueren als dataset; wij committen alleen kleine snapshots voor reproduceerbaarheid.
* **Automatisch?** Ja, maar Yahoo is onbetrouwbaar (rate limits, incidentele lege downloads).
  Controleer na een refresh altijd `frame.notna().sum()`.
* **Gecacht** `hap.yahoo(["SPY","TLT","GLD","QQQ","IWM"], "1993-01-01")` — dagelijkse
  split- en dividend-gecorrigeerde slotkoersen (**niveaus**, geen returns), 1993-01-29 – 2026-09-04.
* **Gecacht** `hap.yahoo_options("SPY")` — optieketen-**momentopname** van de snapshotdatum
  (Yahoo levert alleen de huidige keten). Kolommen o.a. `expiry`, `kind`, `strike`, `bid`, `ask`,
  `lastPrice`, `volume`, `openInterest`, `impliedVolatility` (decimaal), `spot`, `snapshot`.

---

## `data/raw/`

Git-ignored. Alleen nodig als een automatische download ooit breekt; de foutmelding van de
loader noemt dan het exacte bestandspad en de handmatige stap. Op de snapshotdatum was
**geen enkele** bron handmatig: alle acht loaders draaien volledig automatisch.

## Een snapshot verversen

```bash
HAP_REFRESH=1 uv run python -c "import hap; hap.shiller()"   # één bron
uv run pytest -q                                            # controleer offline
```

Werk daarna de snapshotdatum en de periodes hierboven bij.

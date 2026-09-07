"""Data loaders for the *history of asset pricing* lectures.

Every loader returns a :class:`pandas.DataFrame` with a
:class:`pandas.DatetimeIndex` and is wrapped by :func:`hap.cache.cached`, so the
first call downloads and every later call reads the committed parquet snapshot
in ``data/cache/``.

Conventions
-----------
Index
    ``DatetimeIndex`` named ``date``.  Monthly data is stamped at **month end**,
    quarterly at quarter end, annual at year end, daily at the trading date.
Units
    **Returns and yields are decimals, not percent.**  A monthly excess return
    of 1.5% is stored as ``0.015``; a 10-year yield of 4.2% as ``0.042``.  Level
    series (prices, indices, CPI, firm counts) keep their native units.
Missing values
    Source sentinels (``-99.99``, ``-999``, ``.``) are converted to ``NaN``.

Set ``HAP_OFFLINE=1`` to forbid downloads and ``HAP_REFRESH=1`` to force them;
see :mod:`hap.cache`.
"""

from __future__ import annotations

import io
import re
import zipfile
from typing import Literal

import pandas as pd
import requests

from .cache import RAW_DIR, CacheMissError, cached, require_raw

__all__ = [
    "FRENCH_DATASETS",
    "french",
    "french_tables",
    "fred",
    "goyal_welch",
    "gsw",
    "hkm",
    "market_daily",
    "market_monthly",
    "osap",
    "shiller",
    "yahoo",
    "yahoo_options",
]

_TIMEOUT = 180
_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; hap-lectures/0.1)"}

FRENCH_BASE = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/"

FRENCH_DATASETS: tuple[str, ...] = (
    "F-F_Research_Data_Factors",
    "F-F_Research_Data_5_Factors_2x3",
    "F-F_Momentum_Factor",
    "F-F_ST_Reversal_Factor",
    "F-F_LT_Reversal_Factor",
    "25_Portfolios_5x5",
    "Portfolios_Formed_on_ME",
    "Portfolios_Formed_on_BE-ME",
    "Portfolios_Formed_on_E-P",
    "10_Industry_Portfolios",
    "6_Portfolios_ME_Prior_12_2",
    "6_Portfolios_ME_Prior_60_13",
)
"""Kenneth French datasets kept as committed snapshots."""

# Tables whose numbers are counts or levels rather than percent returns.
_FRENCH_LEVEL_TABLE = re.compile(
    r"number of firms|firm size|market cap|be/?me|sum of be", re.IGNORECASE
)


def _get(url: str) -> bytes:
    response = requests.get(url, timeout=_TIMEOUT, headers=_HEADERS)
    response.raise_for_status()
    return response.content


# --------------------------------------------------------------------------
# Kenneth French Data Library
# --------------------------------------------------------------------------


def _french_url(name: str, freq: str) -> str:
    suffix = {"monthly": "", "daily": "_daily", "weekly": "_weekly"}[freq]
    return f"{FRENCH_BASE}{name}{suffix}_CSV.zip"


def _french_text(name: str, freq: str) -> str:
    payload = _get(_french_url(name, freq))
    archive = zipfile.ZipFile(io.BytesIO(payload))
    return archive.read(archive.namelist()[0]).decode("latin-1")


def _split_french_tables(text: str) -> list[tuple[str, str, list[str]]]:
    """Split a French CSV into ``(title, header, rows)`` blocks.

    French files stack several tables in one CSV (value weighted, equal
    weighted, annual, number of firms, ...).  A data row starts with a 4-, 6- or
    8-digit date; a header row starts with a comma; anything else is prose, of
    which the last line before a block is used as its title.
    """
    blocks: list[tuple[str, str, list[str]]] = []
    title, header, rows = "", "", []
    for line in text.splitlines():
        stripped = line.strip()
        first = stripped.split(",")[0].strip()
        if re.fullmatch(r"\d{4}|\d{6}|\d{8}", first):
            rows.append(line)
            continue
        if rows:
            blocks.append((title, header, rows))
            rows, title = [], ""
        if stripped.startswith(","):
            header = line
        elif stripped:
            title = stripped.rstrip(", ")
    if rows:
        blocks.append((title, header, rows))
    return [
        (t if 0 < len(t) <= 70 and not t.endswith(".") else f"Table {i}", h, r)
        for i, (t, h, r) in enumerate(blocks)
    ]


def _french_index(tokens: pd.Series) -> pd.DatetimeIndex:
    width = int(tokens.str.len().max())
    if width == 8:
        index = pd.to_datetime(tokens, format="%Y%m%d")
    elif width == 6:
        index = pd.to_datetime(tokens, format="%Y%m") + pd.offsets.MonthEnd(0)
    else:
        index = pd.to_datetime(tokens, format="%Y") + pd.offsets.YearEnd(0)
    return pd.DatetimeIndex(index, name="date")


def _french_frame(block: tuple[str, str, list[str]], percent: bool | None) -> pd.DataFrame:
    title, header, rows = block
    columns = [c.strip() for c in header.split(",")[1:]]
    frame = pd.read_csv(
        io.StringIO("\n".join(rows)),
        header=None,
        names=["date", *columns],
        usecols=range(len(columns) + 1),
        dtype={"date": str},
    )
    frame.index = _french_index(frame.pop("date").str.strip())
    frame = frame.apply(pd.to_numeric, errors="coerce")
    frame = frame.mask(frame <= -99.0)
    if percent is None:
        percent = not _FRENCH_LEVEL_TABLE.search(title)
    if percent:
        frame = frame / 100.0
    frame.attrs["table"] = title
    return frame


@cached("french_tables")
def french_tables(name: str, freq: str = "monthly") -> pd.DataFrame:
    """List the tables contained in a Kenneth French CSV file.

    Parameters
    ----------
    name : str
        Dataset name, e.g. ``"25_Portfolios_5x5"``.
    freq : {"monthly", "daily", "weekly"}
        Which file variant to read.

    Returns
    -------
    pandas.DataFrame
        Indexed by a dummy date, with columns ``table`` (index of the block),
        ``title`` and ``nobs``.  The index carries no meaning; it exists only
        because the cache stores parquet frames with a ``DatetimeIndex``.
    """
    blocks = _split_french_tables(_french_text(name, freq))
    frame = pd.DataFrame(
        {
            "table": range(len(blocks)),
            "title": [t for t, _, _ in blocks],
            "nobs": [len(r) for _, _, r in blocks],
        }
    )
    frame.index = pd.DatetimeIndex(
        pd.to_datetime(["2000-01-01"] * len(frame)), name="date"
    )
    return frame


@cached("french")
def french(
    name: str,
    freq: str = "monthly",
    table: int | str = 0,
    percent: bool | None = None,
) -> pd.DataFrame:
    """Load a dataset from the Kenneth French Data Library.

    Source: <https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html>.
    The zip archive is parsed directly; French stacks several tables in one CSV
    (value weighted, equal weighted, annual, number of firms, ...).  Table ``0``
    is always the primary monthly/daily **value-weighted return** table, which
    is why it is the default.

    Parameters
    ----------
    name : str
        Dataset name as it appears in the library, e.g.
        ``"F-F_Research_Data_Factors"`` or ``"25_Portfolios_5x5"``.  See
        :data:`FRENCH_DATASETS` for the snapshots kept in the cache.
    freq : {"monthly", "daily", "weekly"}, default "monthly"
        Which file variant to download.  ``"monthly"`` files also contain the
        annual tables.
    table : int or str, default 0
        Table index, or a case-insensitive substring of the table title (e.g.
        ``"Equal Weighted"``).  Use :func:`french_tables` to see the options.
    percent : bool, optional
        Whether the numbers are percentages that must be divided by 100.
        ``None`` (default) infers it from the table title: return tables yes,
        firm counts / average size / BE-ME tables no.

    Returns
    -------
    pandas.DataFrame
        Month-end (or daily) ``DatetimeIndex``; returns as **decimals**.
        ``-99.99`` and ``-999`` sentinels become ``NaN``.  The selected table
        title is available as ``frame.attrs["table"]``.

    Examples
    --------
    >>> ff3 = french("F-F_Research_Data_Factors")  # doctest: +SKIP
    >>> ff3.columns.tolist()  # doctest: +SKIP
    ['Mkt-RF', 'SMB', 'HML', 'RF']
    """
    blocks = _split_french_tables(_french_text(name, freq))
    if isinstance(table, str):
        matches = [i for i, (t, _, _) in enumerate(blocks) if table.lower() in t.lower()]
        if not matches:
            titles = [t for t, _, _ in blocks]
            raise KeyError(f"No table matching {table!r} in {name}; have {titles}")
        index = matches[0]
    else:
        index = table
    return _french_frame(blocks[index], percent)


def market_monthly() -> pd.DataFrame:
    """Monthly market excess return and risk-free rate (French FF3 file).

    Returns
    -------
    pandas.DataFrame
        Columns ``Mkt-RF``, ``RF`` and ``Mkt`` (= ``Mkt-RF + RF``), decimals,
        month-end index, 1926-07 onwards.
    """
    frame = french("F-F_Research_Data_Factors", "monthly")[["Mkt-RF", "RF"]].copy()
    frame["Mkt"] = frame["Mkt-RF"] + frame["RF"]
    return frame


def market_daily() -> pd.DataFrame:
    """Daily market excess return and risk-free rate (French FF3 daily file).

    Returns
    -------
    pandas.DataFrame
        Columns ``Mkt-RF``, ``RF`` and ``Mkt``, decimals, daily index,
        1926-07-01 onwards.
    """
    frame = french("F-F_Research_Data_Factors", "daily")[["Mkt-RF", "RF"]].copy()
    frame["Mkt"] = frame["Mkt-RF"] + frame["RF"]
    return frame


# --------------------------------------------------------------------------
# Robert Shiller
# --------------------------------------------------------------------------

SHILLER_FALLBACK_URL = "http://www.econ.yale.edu/~shiller/data/ie_data.xls"

_SHILLER_COLUMNS = [
    "date_raw",
    "price",
    "dividend",
    "earnings",
    "cpi",
    "date_fraction",
    "long_rate",
    "real_price",
    "real_dividend",
    "real_total_return_price",
    "real_earnings",
    "real_tr_scaled_earnings",
    "cape",
    "_blank1",
    "tr_cape",
    "_blank2",
    "excess_cape_yield",
    "monthly_total_bond_return",
    "real_total_bond_return",
    "stock_real_return_10y",
    "bond_real_return_10y",
    "excess_real_return_10y",
]


def _shiller_url() -> str:
    """Find the current ``ie_data.xls`` link on shillerdata.com."""
    try:
        html = _get("https://shillerdata.com/").decode("utf-8", "replace")
        match = re.search(r'href="(//[^"]*ie_data\.xls[^"]*)"', html)
        if match:
            return "https:" + match.group(1)
    except requests.RequestException:  # pragma: no cover - network fallback
        pass
    return SHILLER_FALLBACK_URL


@cached("shiller")
def shiller() -> pd.DataFrame:
    """Robert Shiller's monthly US stock market data, 1871 onwards.

    Source: <https://shillerdata.com/> (``ie_data.xls``, the dataset behind
    *Irrational Exuberance*), with <http://www.econ.yale.edu/~shiller/data/ie_data.xls>
    as fallback.

    Returns
    -------
    pandas.DataFrame
        Month-end ``DatetimeIndex`` from 1871-01.  Columns:

        ``price``, ``dividend``, ``earnings``
            Nominal S&P Composite index level and 12-month trailing dividend
            and earnings per index unit.
        ``cpi``, ``long_rate``
            Consumer price index and the long (GS10) nominal rate, **decimal**.
        ``real_price``, ``real_dividend``, ``real_earnings``
            Deflated by the most recent CPI.
        ``real_total_return_price``, ``real_tr_scaled_earnings``
            Cum-dividend real total return index and its scaled earnings.
        ``cape``, ``tr_cape``, ``excess_cape_yield``
            Cyclically adjusted PE, its total-return variant, and the excess
            CAPE yield (decimal).
        ``monthly_total_bond_return``, ``real_total_bond_return``
            Shiller's 10-year bond total return series.
        ``pd_ratio``, ``dp``, ``ep``
            Derived: price/dividend, dividend yield and earnings yield
            (decimals), computed here rather than by Shiller.

    Notes
    -----
    Shiller stores dates as ``YYYY.MM`` floats where October is ``.1``; these
    are converted to month-end timestamps.  The final one or two months are
    provisional (Shiller uses the first-of-month close).
    """
    raw = pd.read_excel(io.BytesIO(_get(_shiller_url())), sheet_name="Data", header=None)
    header_row = int(raw.index[raw[0].astype(str).str.strip() == "Date"][0])
    frame = raw.iloc[header_row + 1 :].reset_index(drop=True)
    frame = frame.iloc[:, : len(_SHILLER_COLUMNS)]
    frame.columns = _SHILLER_COLUMNS[: frame.shape[1]]
    frame = frame.apply(pd.to_numeric, errors="coerce")
    frame = frame[frame["date_raw"].notna()]

    year = frame["date_raw"].astype(int)
    month = (frame["date_raw"] * 100).round().astype(int) - year * 100
    frame.index = pd.DatetimeIndex(
        pd.to_datetime({"year": year, "month": month, "day": 1}) + pd.offsets.MonthEnd(0),
        name="date",
    )
    frame = frame.drop(columns=[c for c in frame.columns if c.startswith(("_", "date_"))])

    frame["long_rate"] = frame["long_rate"] / 100.0
    frame["excess_cape_yield"] = frame["excess_cape_yield"]
    frame["pd_ratio"] = frame["price"] / frame["dividend"]
    frame["dp"] = frame["dividend"] / frame["price"]
    frame["ep"] = frame["earnings"] / frame["price"]
    return frame


# --------------------------------------------------------------------------
# FRED
# --------------------------------------------------------------------------


@cached("fred")
def fred(series: str, start: str | None = None) -> pd.DataFrame:
    """Download one FRED series as CSV (no API key needed).

    Source: ``https://fred.stlouisfed.org/graph/fredgraph.csv?id=<series>``.

    Parameters
    ----------
    series : str
        FRED series id, e.g. ``"USREC"``, ``"VIXCLS"``, ``"PCECC96"``.
    start : str, optional
        ISO date; observations before it are dropped.

    Returns
    -------
    pandas.DataFrame
        Single column named ``series``, ``DatetimeIndex`` at the FRED
        observation date (period start for monthly/quarterly series).  FRED's
        ``"."`` missing marker becomes ``NaN``.  Units are FRED's own: rates
        and yields are **percent**, so divide by 100 for decimals.
    """
    payload = _get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}")
    frame = pd.read_csv(io.BytesIO(payload), na_values=["."])
    frame.index = pd.DatetimeIndex(pd.to_datetime(frame.iloc[:, 0]), name="date")
    frame = frame.iloc[:, 1:]
    frame.columns = [series]
    frame[series] = pd.to_numeric(frame[series], errors="coerce")
    if start is not None:
        frame = frame.loc[start:]
    return frame


# --------------------------------------------------------------------------
# Gurkaynak-Sack-Wright
# --------------------------------------------------------------------------

GSW_URL = "https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv"


@cached("gsw")
def gsw() -> pd.DataFrame:
    """Gurkaynak-Sack-Wright US zero-coupon nominal yield curve, 1961 onwards.

    Source: <https://www.federalreserve.gov/data/yield-curve-tables/feds200628_1.html>,
    file ``feds200628.csv``.  Updated by the Federal Reserve Board; the paper is
    Gurkaynak, Sack and Wright (2007, JME).

    Returns
    -------
    pandas.DataFrame
        Daily ``DatetimeIndex``.  Column groups:

        ``SVENYnn``
            Continuously compounded zero-coupon yield, maturity ``nn`` years.
        ``SVENFnn``
            Instantaneous forward rate ``nn`` years ahead.
        ``SVENPYnn``
            Par yield, maturity ``nn`` years.
        ``SVEN1F..``, ``BETA0``-``BETA4``, ``TAU1``, ``TAU2``
            One-year forward rates and the Svensson curve parameters.

        Yields, forwards and the ``BETA`` parameters are **decimals** (the
        source publishes percent; both are divided by 100 so that the Svensson
        formula still reproduces the yields).  ``TAU1``/``TAU2`` are in years
        and left untouched.  Early sample: only short maturities are populated;
        maturities beyond the traded curve are ``NaN``.
    """
    text = _get(GSW_URL).decode("latin-1")
    lines = text.splitlines()
    header = next(i for i, line in enumerate(lines) if line.lower().startswith("date,"))
    frame = pd.read_csv(io.StringIO("\n".join(lines[header:])), na_values=["NA", ""])
    frame.index = pd.DatetimeIndex(pd.to_datetime(frame.pop("Date")), name="date")
    frame = frame.apply(pd.to_numeric, errors="coerce")
    scale = [c for c in frame.columns if c.startswith(("SVEN", "BETA"))]
    frame[scale] = frame[scale] / 100.0
    return frame


# --------------------------------------------------------------------------
# Goyal-Welch predictors
# --------------------------------------------------------------------------

GOYAL_WELCH_URL = (
    "https://docs.google.com/spreadsheets/d/1qwpl2R_DNujpU5YUkk8lacP1tTeMb9iJ/"
    "export?format=xlsx"
)


def _goyal_welch_raw(freq: str) -> pd.DataFrame:
    sheet = {"monthly": "Monthly", "quarterly": "Quarterly", "annual": "Annual"}[freq]
    try:
        return pd.read_excel(io.BytesIO(_get(GOYAL_WELCH_URL)), sheet_name=sheet)
    except Exception as exc:  # noqa: BLE001 - fall back to a manual download
        local = RAW_DIR / "PredictorData.xlsx"
        if not local.exists():
            raise CacheMissError(
                "Could not download the Goyal-Welch predictor file "
                f"({exc}).\nDownload 'Updated data' (PredictorData*.xlsx) from "
                f"https://sites.google.com/view/agoyal145 and save it as {local}."
            ) from exc
        return pd.read_excel(local, sheet_name=sheet)


@cached("goyal_welch")
def goyal_welch(freq: str = "monthly") -> pd.DataFrame:
    """Amit Goyal's updated Welch-Goyal (2008) equity premium predictors.

    Source: <https://sites.google.com/view/agoyal145> ("Updated data",
    ``PredictorData*.xlsx``, sheets ``Monthly`` / ``Quarterly`` / ``Annual``).
    If the direct download fails, place the workbook at
    ``data/raw/PredictorData.xlsx`` (see ``data/README.md``).

    Parameters
    ----------
    freq : {"monthly", "quarterly", "annual"}, default "monthly"
        Which sheet to read.

    Returns
    -------
    pandas.DataFrame
        Period-end ``DatetimeIndex`` (1871 onwards for annual, 1871-01 for
        monthly).  The raw columns of the workbook (``Index``, ``D12``, ``E12``,
        ``b/m``, ``tbl``, ``AAA``, ``BAA``, ``lty``, ``ntis``, ``Rfree``,
        ``infl``, ``ltr``, ``corpr``, ``svar``, ``csp``, ``CRSP_SPvw``, ...)
        plus the standard Welch-Goyal transformations:

        ``dp``
            log(D12) - log(Index), log dividend-price ratio.
        ``dy``
            log(D12) - log(Index lagged one period), log dividend yield.
        ``ep``
            log(E12) - log(Index), log earnings-price ratio.
        ``de``
            log(D12) - log(E12), log dividend payout ratio.
        ``tms``
            ``lty - tbl``, term spread.
        ``dfy``
            ``BAA - AAA``, default yield spread.
        ``dfr``
            ``corpr - ltr``, default return spread.
        ``equity_premium``
            ``log(1 + CRSP_SPvw) - log(1 + Rfree)``, the standard left-hand
            side of Welch-Goyal (2008).

        Interest rates (``tbl``, ``lty``, ``AAA``, ``BAA``) are stored by Goyal
        as decimals already and are passed through unchanged.
    """
    raw = _goyal_welch_raw(freq)
    raw.columns = [str(c).strip() for c in raw.columns]
    stamp = raw.columns[0]
    tokens = raw.pop(stamp).astype(str).str.replace(r"\.0$", "", regex=True)
    if freq == "monthly":
        index = pd.to_datetime(tokens, format="%Y%m") + pd.offsets.MonthEnd(0)
    elif freq == "quarterly":
        index = pd.PeriodIndex(
            [f"{t[:4]}Q{t[4:]}" for t in tokens], freq="Q"
        ).to_timestamp(how="end").normalize()
    else:
        index = pd.to_datetime(tokens, format="%Y") + pd.offsets.YearEnd(0)
    frame = raw.apply(pd.to_numeric, errors="coerce")
    frame.index = pd.DatetimeIndex(index, name="date")

    import numpy as np

    def col(name: str) -> pd.Series:
        return frame[name] if name in frame else pd.Series(np.nan, index=frame.index)

    price, div, earn = col("Index"), col("D12"), col("E12")
    frame["dp"] = np.log(div) - np.log(price)
    frame["dy"] = np.log(div) - np.log(price.shift(1))
    frame["ep"] = np.log(earn) - np.log(price)
    frame["de"] = np.log(div) - np.log(earn)
    frame["tms"] = col("lty") - col("tbl")
    frame["dfy"] = col("BAA") - col("AAA")
    frame["dfr"] = col("corpr") - col("ltr")
    frame["equity_premium"] = np.log1p(col("CRSP_SPvw")) - np.log1p(col("Rfree"))
    return frame


# --------------------------------------------------------------------------
# Open Source Asset Pricing (Chen & Zimmermann)
# --------------------------------------------------------------------------

OSAP_DRIVE = "https://drive.google.com/uc?export=download&id="
OSAP_PORTFOLIO_URL = OSAP_DRIVE + "10sOryk_ddjkXagaajTKUk1nwJs2ZLRiI"
OSAP_SIGNALDOC_URL = OSAP_DRIVE + "1Sev9s6cPFUGgxp1pFiej0lGzpsMqJCI2"


def _osap_manual(filename: str, what: str) -> str:
    return (
        f"Download {what} from https://www.openassetpricing.com/data/ and save the "
        f"file as data/raw/{filename}. Google Drive blocks scripted downloads of "
        "large files, so this step is manual; see data/README.md."
    )


@cached("osap")
def osap(kind: str = "portfolios") -> pd.DataFrame:
    """Open Source Asset Pricing (Chen & Zimmermann) predictor data.

    Source: <https://www.openassetpricing.com/data/>.  The files live on Google
    Drive but download fine over plain HTTP, so no manual step is normally
    needed.  Should Drive ever start serving a confirmation page instead, the
    loader falls back to a manually downloaded copy in ``data/raw/``
    (``PredictorLSretWide.csv`` / ``SignalDoc.csv``; see ``data/README.md``).

    Parameters
    ----------
    kind : {"portfolios", "signaldoc"}, default "portfolios"
        ``"portfolios"``
            Monthly equal- or value-weighted **long-short** returns of the
            published predictors (``PredictorLSretWide.csv``).
        ``"signaldoc"``
            Signal documentation (``SignalDoc.csv``): acronym, long name,
            authors, publication year and journal, sample start/end, category
            (``Predictor`` / ``Placebo`` / ``Indirect``) and the reported
            t-statistic.

    Returns
    -------
    pandas.DataFrame
        ``"portfolios"``: month-end ``DatetimeIndex``, one column per signal
        acronym, long-short returns as **decimals**.
        ``"signaldoc"``: indexed by the publication year (year end) so it fits
        the parquet cache convention, with the acronym in column ``signal``.
    """
    if kind == "portfolios":
        return _osap_portfolios()
    if kind == "signaldoc":
        return _osap_signaldoc()
    raise ValueError(f"kind must be 'portfolios' or 'signaldoc', got {kind!r}")


def _osap_csv(url: str, filename: str, what: str) -> pd.DataFrame:
    try:
        payload = _get(url)
        if payload[:20].lstrip().lower().startswith(b"<!doctype"):
            raise requests.RequestException("Google Drive returned an HTML page")
        return pd.read_csv(io.BytesIO(payload))
    except Exception:  # noqa: BLE001 - fall back to a manual download
        return pd.read_csv(require_raw(filename, _osap_manual(filename, what)))


def _osap_portfolios() -> pd.DataFrame:
    raw = _osap_csv(
        OSAP_PORTFOLIO_URL, "PredictorLSretWide.csv", "the long-short portfolio returns"
    )
    stamp = raw.columns[0]
    index = pd.to_datetime(raw.pop(stamp)) + pd.offsets.MonthEnd(0)
    frame = raw.apply(pd.to_numeric, errors="coerce")
    frame.index = pd.DatetimeIndex(index, name="date")
    # OSAP publishes long-short returns in percent.
    return (frame / 100.0).astype("float32")


def _osap_signaldoc() -> pd.DataFrame:
    raw = _osap_csv(OSAP_SIGNALDOC_URL, "SignalDoc.csv", "the signal documentation")
    raw.columns = [str(c).strip() for c in raw.columns]
    acronym = next(c for c in raw.columns if c.lower() in ("acronym", "signalname"))
    raw = raw.rename(columns={acronym: "signal"})
    year = pd.to_numeric(raw.get("Year"), errors="coerce").fillna(1900).astype(int)
    raw.index = pd.DatetimeIndex(
        pd.to_datetime(year.astype(str), format="%Y") + pd.offsets.YearEnd(0),
        name="date",
    )
    return raw.astype({c: str for c in raw.columns if raw[c].dtype == object})


# --------------------------------------------------------------------------
# He-Kelly-Manela intermediary capital
# --------------------------------------------------------------------------

HKM_PAGE = (
    "https://zhiguohe.net/data-and-empirical-patterns/"
    "intermediary-capital-ratio-and-risk-factor/"
)


def _hkm_url(freq: str) -> str:
    """Scrape Zhiguo He's data page for the current factor CSV.

    The published filenames carry a version stamp (``..._monthly_250627.csv``)
    that changes at every update, so the link is looked up rather than pinned.
    """
    html = _get(HKM_PAGE).decode("utf-8", "replace")
    pattern = rf'https?://[^"\'\s]*He_Kelly_Manela_Factors_{freq}[^"\'\s]*\.csv'
    matches = re.findall(pattern, html)
    if not matches:
        raise requests.RequestException(f"No {freq} HKM factor CSV found on {HKM_PAGE}")
    return sorted(set(matches))[-1]


@cached("hkm")
def hkm(freq: str = "monthly") -> pd.DataFrame:
    """He-Kelly-Manela intermediary capital ratio and risk factor.

    Source: <https://zhiguohe.net/data-and-empirical-patterns/intermediary-capital-ratio-and-risk-factor/>
    (He, Kelly and Manela, 2017, JFE).  The exact filename carries a version
    stamp, so the loader scrapes the page for the current link.  If that fails,
    save ``He_Kelly_Manela_Factors_monthly.csv`` (or the quarterly file) in
    ``data/raw/``; see ``data/README.md``.

    Parameters
    ----------
    freq : {"monthly", "quarterly"}, default "monthly"
        Which factor file to read.

    Returns
    -------
    pandas.DataFrame
        Period-end ``DatetimeIndex`` from 1970.  Key columns:

        ``intermediary_capital_ratio``
            Aggregate market equity / (market equity + book debt) of primary
            dealer holding companies.
        ``intermediary_capital_risk_factor``
            AR(1) innovation to the capital ratio, scaled by lagged capital
            ratio; the traded intermediary factor.
        ``intermediary_value_weighted_investment_return``
            Value-weighted equity return of the primary dealers.
        ``intermediary_leverage_ratio_squared``
            Squared inverse capital ratio.

        All returns and ratios are **decimals**.
    """
    try:
        raw = pd.read_csv(io.BytesIO(_get(_hkm_url(freq))))
    except Exception:  # noqa: BLE001 - fall back to a manual download
        path = require_raw(
            f"He_Kelly_Manela_Factors_{freq}.csv",
            f"Download the {freq} factor CSV from {HKM_PAGE} and save it as "
            f"data/raw/He_Kelly_Manela_Factors_{freq}.csv; see data/README.md.",
        )
        raw = pd.read_csv(path)
    raw.columns = [str(c).strip() for c in raw.columns]
    tokens = raw.pop(raw.columns[0]).astype(str).str.replace(r"\.0$", "", regex=True)
    if freq == "monthly":
        index = pd.to_datetime(tokens, format="%Y%m") + pd.offsets.MonthEnd(0)
    else:  # 'yyyyq', e.g. 19701 for 1970Q1
        index = pd.PeriodIndex(
            [f"{t[:4]}Q{t[4:]}" for t in tokens], freq="Q"
        ).to_timestamp(how="end").normalize()
    frame = raw.apply(pd.to_numeric, errors="coerce")
    frame.index = pd.DatetimeIndex(index, name="date")
    # The published file has shipped a duplicated month (2025-01); keep the last
    # row, which is the corrected one.
    return frame[~frame.index.duplicated(keep="last")]


# --------------------------------------------------------------------------
# Yahoo Finance
# --------------------------------------------------------------------------


@cached("yahoo")
def yahoo(
    tickers: str | list[str],
    start: str = "1990-01-01",
    end: str | None = None,
    field: Literal["Close", "Open", "High", "Low", "Volume"] = "Close",
) -> pd.DataFrame:
    """Daily Yahoo Finance prices via :mod:`yfinance`.

    Parameters
    ----------
    tickers : str or list of str
        One or more Yahoo tickers, e.g. ``"SPY"`` or ``["SPY", "TLT"]``.
    start, end : str
        ISO dates.  ``end=None`` means "today at snapshot time".
    field : {"Close", "Open", "High", "Low", "Volume"}, default "Close"
        Which OHLCV field to keep.  ``"Close"`` is split- and dividend-adjusted
        (yfinance's ``auto_adjust=True``).

    Returns
    -------
    pandas.DataFrame
        Daily ``DatetimeIndex`` (timezone-naive), one column per ticker, price
        **levels** (not returns).  Take ``.pct_change()`` for simple returns.
    """
    import yfinance as yf

    names = [tickers] if isinstance(tickers, str) else list(tickers)
    raw = yf.download(
        names, start=start, end=end, auto_adjust=True, progress=False, actions=False
    )
    frame = raw[field] if isinstance(raw.columns, pd.MultiIndex) else raw[[field]]
    frame = pd.DataFrame(frame)
    if list(frame.columns) == [field]:
        frame.columns = names[:1]
    frame.index = pd.DatetimeIndex(
        pd.to_datetime(frame.index).tz_localize(None), name="date"
    )
    return frame.astype("float64")


@cached("yahoo_options")
def yahoo_options(ticker: str, n_expiries: int = 6) -> pd.DataFrame:
    """Option chain snapshot for ``ticker`` via :mod:`yfinance`.

    Yahoo only serves the *current* chain, so this is a point-in-time snapshot
    frozen at the cache date; set ``HAP_REFRESH=1`` for a fresh one.

    Parameters
    ----------
    ticker : str
        Underlying Yahoo ticker, e.g. ``"SPY"``.
    n_expiries : int, default 6
        How many of the nearest expiries to download.

    Returns
    -------
    pandas.DataFrame
        Indexed by ``lastTradeDate``.  Columns include ``expiry`` (datetime),
        ``kind`` (``"call"``/``"put"``), ``strike``, ``bid``, ``ask``,
        ``lastPrice``, ``volume``, ``openInterest`` and ``impliedVolatility``
        (decimal), plus ``spot`` and ``snapshot`` (the download date).
    """
    import yfinance as yf

    handle = yf.Ticker(ticker)
    spot = float(handle.fast_info["last_price"])
    parts = []
    for expiry in list(handle.options)[:n_expiries]:
        chain = handle.option_chain(expiry)
        for kind, table in (("call", chain.calls), ("put", chain.puts)):
            table = table.copy()
            table["expiry"] = pd.Timestamp(expiry)
            table["kind"] = kind
            parts.append(table)
    frame = pd.concat(parts, ignore_index=True)
    frame["spot"] = spot
    frame["snapshot"] = pd.Timestamp.utcnow().tz_localize(None).normalize()
    frame.index = pd.DatetimeIndex(
        pd.to_datetime(frame.pop("lastTradeDate"), utc=True).dt.tz_localize(None),
        name="date",
    )
    frame["contractSymbol"] = frame["contractSymbol"].astype(str)
    return frame

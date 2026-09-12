"""Offline tests for the loaders in :mod:`hap.data`.

Every test runs with ``HAP_OFFLINE=1`` (set by ``conftest.py``), so the suite
exercises the committed parquet snapshots and never touches the network.
"""

from __future__ import annotations

import pandas as pd
import pytest

import hap
from hap.data import FRENCH_DATASETS


def _check_frame(frame: pd.DataFrame, min_rows: int = 100) -> None:
    assert isinstance(frame.index, pd.DatetimeIndex)
    assert frame.index.is_monotonic_increasing
    assert not frame.index.has_duplicates
    assert len(frame) >= min_rows


@pytest.mark.parametrize("name", FRENCH_DATASETS)
def test_french_datasets_cached(name):
    frame = hap.french(name)
    _check_frame(frame, 700)
    assert frame.index.min().year <= 1963
    assert frame.index.max().year >= 2024
    # Month-end stamps.
    assert (frame.index == frame.index + pd.offsets.MonthEnd(0)).all()
    # Decimals, not percent: no monthly return above 200%.
    assert frame.abs().max().max() < 2.0


def test_french_factor_columns():
    ff3 = hap.french("F-F_Research_Data_Factors")
    assert list(ff3.columns) == ["Mkt-RF", "SMB", "HML", "RF"]
    assert ff3.index.min() == pd.Timestamp("1926-07-31")
    # Equity premium of roughly 0.5-0.9% per month over the full sample.
    assert 0.004 < ff3["Mkt-RF"].mean() < 0.010

    ff5 = hap.french("F-F_Research_Data_5_Factors_2x3")
    assert list(ff5.columns) == ["Mkt-RF", "SMB", "HML", "RMW", "CMA", "RF"]
    assert ff5.index.min() == pd.Timestamp("1963-07-31")


def test_french_daily():
    daily = hap.french("F-F_Research_Data_Factors", "daily")
    _check_frame(daily, 20000)
    assert list(daily.columns) == ["Mkt-RF", "SMB", "HML", "RF"]
    assert daily["Mkt-RF"].min() < -0.15  # 19 October 1987


def test_french_table_selection():
    titles = hap.french_tables("25_Portfolios_5x5")["title"].tolist()
    assert any("Value Weight" in t for t in titles)
    vw = hap.french("25_Portfolios_5x5")
    ew = hap.french("25_Portfolios_5x5", table="Equal Weight")
    assert vw.shape == ew.shape == (len(vw), 25)
    assert not vw.equals(ew)
    assert vw.columns[0] == "SMALL LoBM"


def test_market_wrappers():
    monthly = hap.market_monthly()
    assert list(monthly.columns) == ["Mkt-RF", "RF", "Mkt"]
    assert (monthly["Mkt"] - monthly["Mkt-RF"] - monthly["RF"]).abs().max() < 1e-12
    assert list(hap.market_daily().columns) == ["Mkt-RF", "RF", "Mkt"]


def test_shiller():
    frame = hap.shiller()
    _check_frame(frame, 1800)
    assert frame.index.min() == pd.Timestamp("1871-01-31")
    for column in ("price", "dividend", "earnings", "cpi", "long_rate", "cape", "dp"):
        assert column in frame.columns
    # Long rate as a decimal, never above 20%.
    assert frame["long_rate"].max() < 0.20
    # CAPE peaked above 40 in 1999-2000.
    assert frame.loc["1999-12-31", "cape"] > 40


def test_goyal_welch():
    monthly = hap.goyal_welch()
    _check_frame(monthly, 1800)
    for column in ("Index", "D12", "E12", "tbl", "dp", "dy", "ep", "tms", "dfy"):
        assert column in monthly.columns
    assert monthly.index.min() == pd.Timestamp("1871-01-31")
    # Log dividend-price ratio between roughly -4.6 and -2.5.
    assert -5.0 < monthly["dp"].mean() < -2.5
    assert len(hap.goyal_welch("annual")) > 140


def test_fred():
    usrec = hap.fred("USREC")
    assert list(usrec.columns) == ["USREC"]
    assert set(usrec["USREC"].dropna().unique()) <= {0.0, 1.0}
    # 2008-2009 recession.
    assert usrec.loc["2009-01-01", "USREC"] == 1.0
    assert hap.fred("VIXCLS")["VIXCLS"].max() > 60  # March 2020 / 2008


def test_gsw():
    frame = hap.gsw()
    _check_frame(frame, 10000)
    assert frame.index.min().year == 1961
    assert {"SVENY01", "SVENY10", "SVENF10", "BETA0", "TAU1"} <= set(frame.columns)
    # Yields as decimals: the 1981 peak is around 15%.
    assert 0.10 < frame["SVENY10"].max() < 0.20
    assert frame["TAU1"].max() > 1.0  # a duration in years, not rescaled


def test_osap_portfolios():
    frame = hap.osap()
    _check_frame(frame, 900)
    assert frame.shape[1] > 150
    assert "Accruals" in frame.columns
    # Decimals: the median signal moves a few percent a month, but the tail is
    # real (IO_ShortInterest returned 321% in the GameStop month of 2021-01).
    assert frame.abs().median().median() < 0.05
    assert frame.abs().max().max() < 5.0


def test_osap_signaldoc():
    doc = hap.osap("signaldoc")
    assert {"signal", "Year", "SampleStartYear", "SampleEndYear"} <= set(doc.columns)
    assert len(doc) > 200
    # Every portfolio column is documented.
    portfolios = set(hap.osap().columns)
    assert portfolios <= set(doc["signal"])


def test_hkm():
    frame = hap.hkm()
    _check_frame(frame, 500)
    assert frame.index.min() == pd.Timestamp("1970-01-31")
    assert "intermediary_capital_ratio" in frame.columns
    assert "intermediary_capital_risk_factor" in frame.columns
    ratio = frame["intermediary_capital_ratio"]
    assert ratio.min() > 0.0 and ratio.max() < 1.0
    # The 2008 crash drove the capital ratio to its historical low.
    assert ratio.idxmin().year in (2008, 2009)


def test_yahoo():
    prices = hap.yahoo(["SPY", "TLT", "GLD", "QQQ", "IWM"], "1993-01-01")
    _check_frame(prices, 5000)
    assert list(prices.columns) == ["GLD", "IWM", "QQQ", "SPY", "TLT"]
    assert prices["SPY"].dropna().iloc[-1] > 100


def test_yahoo_options():
    chain = hap.yahoo_options("SPY")
    assert {"strike", "kind", "expiry", "impliedVolatility", "spot"} <= set(chain.columns)
    assert set(chain["kind"]) == {"call", "put"}
    assert (chain["impliedVolatility"] > 0).any()


def test_offline_cache_miss_is_explicit():
    with pytest.raises(hap.CacheMissError, match="HAP_OFFLINE"):
        hap.fred("NO_SUCH_SERIES_XYZ")


def test_french_multiline_titles_and_level_tables():
    from hap.data import _french_frame, _split_french_tables

    text = "\n".join([
        "This file was created using the CRSP database.",
        "",
        "  Average Value Weighted Returns -- Monthly",
        ",SMALL,BIG",
        "202601,1.00,2.00",
        "",
        "  For portfolios formed in June of year t",
        "  Value Weight Average of BE/ME Calculated for June of t to June of t+1 as: ",
        "  Sum[ME(Mth) * BE(Fiscal Year t-1) / ME(Dec t-1)] / Sum[ME(Mth)]",
        "  Where Mth is a month from June of t to June of t+1",
        ",SMALL,BIG",
        "202601,0.80,0.40",
    ])
    blocks = _split_french_tables(text)
    assert blocks[0][0] == "Average Value Weighted Returns -- Monthly"
    assert blocks[1][0].startswith("Value Weight Average of BE/ME")
    assert _french_frame(blocks[0], None).iloc[0, 0] == 0.01
    assert _french_frame(blocks[1], None).iloc[0, 0] == 0.80

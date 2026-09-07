"""``hap`` - shared toolkit for the *history of asset pricing* lectures.

Three modules:

:mod:`hap.data`
    Cached loaders for free data: Kenneth French, Shiller, Goyal-Welch, FRED,
    Gurkaynak-Sack-Wright, Open Source Asset Pricing, He-Kelly-Manela and Yahoo
    Finance.  Every loader returns a :class:`pandas.DataFrame` with a
    :class:`pandas.DatetimeIndex` (month end for monthly data) and returns as
    **decimals**, not percent.
:mod:`hap.stats`
    Newey-West regressions, Fama-MacBeth, the GRS test, long-horizon
    regressions, variance ratios, Hansen-Jagannathan bounds and summary
    statistics.
:mod:`hap.plotting`
    A quiet matplotlib style plus year-axis and NBER-recession helpers.

Caching is handled by :mod:`hap.cache`: snapshots live in ``data/cache/`` and
are committed.  ``HAP_OFFLINE=1`` forbids downloads, ``HAP_REFRESH=1`` forces
them.

Examples
--------
>>> import hap  # doctest: +SKIP
>>> ff3 = hap.french("F-F_Research_Data_Factors")  # doctest: +SKIP
>>> hap.summary_stats(ff3[["Mkt-RF"]], "monthly")  # doctest: +SKIP
"""

from __future__ import annotations

from . import cache, data, plotting, stats
from .cache import CACHE_DIR, RAW_DIR, REPO_ROOT, CacheMissError, cached
from .data import (
    fred,
    french,
    french_tables,
    goyal_welch,
    gsw,
    hkm,
    market_daily,
    market_monthly,
    osap,
    shiller,
    yahoo,
    yahoo_options,
)
from .stats import (
    drawdowns,
    fama_macbeth,
    grs_test,
    hansen_jagannathan_bound,
    long_horizon_regression,
    newey_west,
    sharpe,
    summary_stats,
    variance_ratio,
)

__version__ = "0.1.0"

__all__ = [
    "CACHE_DIR",
    "RAW_DIR",
    "REPO_ROOT",
    "CacheMissError",
    "cache",
    "cached",
    "data",
    "drawdowns",
    "fama_macbeth",
    "french",
    "french_tables",
    "fred",
    "goyal_welch",
    "grs_test",
    "gsw",
    "hansen_jagannathan_bound",
    "hkm",
    "long_horizon_regression",
    "market_daily",
    "market_monthly",
    "newey_west",
    "osap",
    "plotting",
    "sharpe",
    "shiller",
    "stats",
    "summary_stats",
    "variance_ratio",
    "yahoo",
    "yahoo_options",
]

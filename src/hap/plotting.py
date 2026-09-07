"""Matplotlib style and figure helpers for the lectures.

Call :func:`setup` once at the top of a lecture notebook; every later figure
then inherits the same quiet, QuantEcon-like look: white background, light
grid, ``figsize=(9, 5)``, ``dpi=110`` and a fixed colour cycle.
"""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.dates import AutoDateLocator, DateFormatter, YearLocator

__all__ = ["COLORS", "recession_shading", "setup", "timeline_axis"]

COLORS: tuple[str, ...] = (
    "#1f4e79",  # deep blue     - main series
    "#c0504d",  # brick red     - contrast / model
    "#4f8a5b",  # green         - third series
    "#e0a458",  # ochre         - fourth
    "#7a6a9b",  # muted purple
    "#5b8ea6",  # steel blue
    "#8c6d4f",  # brown
    "#8c8c8c",  # grey          - auxiliary
)
"""Fixed colour cycle; index 0 is the primary series in every figure."""

RECESSION_COLOR = "#b0b0b0"

_RC = {
    "figure.figsize": (9.0, 5.0),
    "figure.dpi": 110,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "savefig.bbox": "tight",
    "axes.facecolor": "white",
    "axes.edgecolor": "#4d4d4d",
    "axes.linewidth": 0.8,
    "axes.grid": True,
    "axes.axisbelow": True,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 12,
    "axes.titleweight": "normal",
    "axes.titlelocation": "left",
    "axes.labelsize": 10,
    "axes.prop_cycle": mpl.cycler(color=list(COLORS)),
    "grid.color": "#d9d9d9",
    "grid.linewidth": 0.6,
    "grid.alpha": 0.9,
    "lines.linewidth": 1.6,
    "lines.solid_capstyle": "round",
    "legend.frameon": False,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "font.size": 10,
    "font.family": "sans-serif",
    "mathtext.fontset": "dejavusans",
}


def setup(**overrides: object) -> None:
    """Apply the lecture matplotlib style.

    Parameters
    ----------
    **overrides
        Extra ``matplotlib.rcParams`` entries applied after the defaults, e.g.
        ``setup(**{"figure.figsize": (9, 3)})``.

    Examples
    --------
    >>> setup()
    >>> mpl.rcParams["figure.dpi"]
    110.0
    """
    plt.rcParams.update(_RC)
    if overrides:
        plt.rcParams.update(overrides)


def timeline_axis(ax: Axes, every: int | None = None) -> Axes:
    """Format the x-axis of ``ax`` as a calendar-year timeline.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes with dates on the x-axis.
    every : int, optional
        Tick every ``every`` years.  ``None`` lets matplotlib choose.

    Returns
    -------
    matplotlib.axes.Axes
        The same axes, for chaining.
    """
    ax.xaxis.set_major_locator(
        YearLocator(every) if every else AutoDateLocator(minticks=4, maxticks=9)
    )
    ax.xaxis.set_major_formatter(DateFormatter("%Y"))
    ax.set_xlabel("")
    ax.margins(x=0.01)
    return ax


def recession_shading(
    ax: Axes, color: str = RECESSION_COLOR, alpha: float = 0.25
) -> Axes:
    """Shade NBER recessions using the FRED ``USREC`` indicator.

    ``USREC`` is 1 in every month from the peak to the trough (inclusive).
    Consecutive months are merged into one shaded band, clipped to the current
    x-limits so the axes do not expand.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes with dates on the x-axis.
    color : str, default light grey
        Fill colour of the bands.
    alpha : float, default 0.25
        Fill transparency.

    Returns
    -------
    matplotlib.axes.Axes
        The same axes, for chaining.

    Notes
    -----
    Reads the cached FRED snapshot via :func:`hap.data.fred`, so it also works
    with ``HAP_OFFLINE=1``.  Recessions before 1854 are not in ``USREC``.
    """
    from .data import fred

    flag = fred("USREC")["USREC"].dropna()
    change = flag.diff().fillna(flag.iloc[0])
    starts = flag.index[change == 1]
    ends = flag.index[change == -1]
    if len(ends) < len(starts):
        ends = ends.append(pd.DatetimeIndex([flag.index[-1]]))

    left, right = ax.get_xlim()
    for start, end in zip(starts, ends, strict=False):
        ax.axvspan(start, end, color=color, alpha=alpha, lw=0, zorder=0)
    ax.set_xlim(left, right)
    return ax

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class LogLogTimeTransform(Enum):
    """Enum of the time axis transform of a log-log plot.

    The choices are between different ways of dealing with superposition
    effects from variable flowrates.
    """
    AGARWAL_TIME = "agarwal time"
    DELTA_TIME = "delta time"
    EQUIVALENT_TIME_CUMULATIVE_FLOWRATE = "equivalent time cumulative/flowrate"
    SUPERPOSITION_TIME = "superposition time"

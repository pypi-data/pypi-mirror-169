from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class DataConditioning(Enum):
    """
    The possible values for conditioning of data during PTA pre-processing.
    """
    DATA_OUTLIERS_REMOVED = "data outliers removed"
    DATA_REDUCED = "data reduced"
    DATA_SMOOTHED = "data smoothed"
    DATA_TIME_SHIFTED = "data time shifted"
    TIDE_CORRECTED = "tide corrected"
    TREND_REMOVAL = "trend removal"
    DATA_VALUE_SHIFTED = "data value shifted"
    FLOW_TO_VOLUME = "flow to volume"
    FLUID_LEVEL_TO_PRESSURE = "fluid level to pressure"
    FLUID_LEVEL_TO_VOLUME = "fluid level to volume"
    GAUGE_TO_DATUM_PRESSURE = "gauge to datum pressure"
    PRESSURE_TO_FLOW = "pressure to flow"
    VOLUME_TO_FLOW = "volume to flow"
    DATA_DIFFERENCE = "data difference"
    DATA_CHANNEL_SPLICED = "data channel spliced"
    DATA_CHANNELS_AVERAGED = "data channels averaged"
    RATE_REALLOCATION = "rate reallocation"
    TOTAL_RATE_CALCULATION_FROM_PHASE_RATES = "total rate calculation from phase rates"

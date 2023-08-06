from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class TimeSeriesPointRepresentation(Enum):
    """
    The representation of the points in the time series data: Point By Point
    meaning instantaneous measurements, or Stepwise Value At End Of Period
    meaning that the value reported has applied from the previous point up to
    the time reported.
    """
    POINT_BY_POINT = "point by point"
    STEPWISE_VALUE_AT_END_OF_PERIOD = "stepwise value at end of period"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class SaturationPointKind(Enum):
    """
    Specifies the kinds of saturation points.

    :cvar BUBBLE_POINT: bubble point
    :cvar DEW_POINT: dew point
    :cvar RETROGRADE_DEW_POINT: retrograde dew point
    :cvar CRITICAL_POINT: critical point
    """
    BUBBLE_POINT = "bubble point"
    DEW_POINT = "dew point"
    RETROGRADE_DEW_POINT = "retrograde dew point"
    CRITICAL_POINT = "critical point"

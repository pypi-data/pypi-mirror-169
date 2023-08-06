from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class LogLogPressureTransform(Enum):
    """Enum of the pressure axis transform of a log-log plot.

    "Pressure Function" refers to the pressure as transformed according
    to the choice of pseudo pressure.  See enum
    PressureNonLinearTransformType in the pvtForPTA section for details
    on this choice.

    :cvar DELTA_PRESSURE_FUNCTION: X axis is delta pressure function
        (which may be a pseudo pressure function).
    :cvar DELTA_PRESSURE_FUNCTION_RATE: X axis is delta pressure
        function (which may be a pseudo pressure function) divided by
        flowrate.
    :cvar INTEGRAL_RATE_NORMAL_DELTA_P_FUNCT_TIME: X axis is integral of
        rate normalized delta pressure function (which may be a pseudo
        pressure function) divided by time.
    :cvar RATE_NORMALIZED_DELTA_P_FUNCTION_RATE: X axis is rate
        normalized delta pressure function (which may be a pseudo
        pressure function) divided by rate.
    :cvar OTHER:
    """
    DELTA_PRESSURE_FUNCTION = "delta pressure function"
    DELTA_PRESSURE_FUNCTION_RATE = "delta pressure function/rate"
    INTEGRAL_RATE_NORMAL_DELTA_P_FUNCT_TIME = "integral rate normal delta p funct/time"
    RATE_NORMALIZED_DELTA_P_FUNCTION_RATE = "rate normalized delta p function/rate"
    OTHER = "other"

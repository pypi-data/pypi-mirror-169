from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class TemperatureIntervalPerTimeUom(Enum):
    """
    :cvar DELTA_C_H: delta Celsius per hour
    :cvar DELTA_C_MIN: delta Celsius per minute
    :cvar DELTA_C_S: delta Celsius per second
    :cvar DELTA_F_H: delta Fahrenheit per hour
    :cvar DELTA_F_MIN: delta Fahrenheit per minute
    :cvar DELTA_F_S: delta Fahrenheit per second
    :cvar DELTA_K_S: delta kelvin per second
    """
    DELTA_C_H = "deltaC/h"
    DELTA_C_MIN = "deltaC/min"
    DELTA_C_S = "deltaC/s"
    DELTA_F_H = "deltaF/h"
    DELTA_F_MIN = "deltaF/min"
    DELTA_F_S = "deltaF/s"
    DELTA_K_S = "deltaK/s"

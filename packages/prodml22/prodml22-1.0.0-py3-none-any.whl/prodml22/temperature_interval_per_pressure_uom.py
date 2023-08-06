from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class TemperatureIntervalPerPressureUom(Enum):
    """
    :cvar DELTA_C_K_PA: delta Celsius per kilopascal
    :cvar DELTA_F_PSI: delta Fahrenheit per psi
    :cvar DELTA_K_PA: delta kelvin per Pascal
    """
    DELTA_C_K_PA = "deltaC/kPa"
    DELTA_F_PSI = "deltaF/psi"
    DELTA_K_PA = "deltaK/Pa"

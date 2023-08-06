from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class IsothermalCompressibilityUom(Enum):
    """
    :cvar DM3_K_W_H: cubic decimetre per kilowatt hour
    :cvar DM3_MJ: cubic decimetre per megajoule
    :cvar M3_K_W_H: cubic metre per kilowatt hour
    :cvar M3_J: cubic metre per joule
    :cvar MM3_J: cubic millimetre per joule
    :cvar PT_UK_HP_H: UK pint per horsepower hour
    """
    DM3_K_W_H = "dm3/(kW.h)"
    DM3_MJ = "dm3/MJ"
    M3_K_W_H = "m3/(kW.h)"
    M3_J = "m3/J"
    MM3_J = "mm3/J"
    PT_UK_HP_H = "pt[UK]/(hp.h)"

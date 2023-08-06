from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ElectricCurrentDensityUom(Enum):
    """
    :cvar A_CM2: ampere per square centimetre
    :cvar A_FT2: ampere per square foot
    :cvar A_M2: ampere per square metre
    :cvar A_MM2: ampere per square millimetre
    :cvar M_A_CM2: milliampere per square centimetre
    :cvar M_A_FT2: milliampere per square foot
    :cvar U_A_CM2: microampere per square centimetre
    :cvar U_A_IN2: microampere per square inch
    """
    A_CM2 = "A/cm2"
    A_FT2 = "A/ft2"
    A_M2 = "A/m2"
    A_MM2 = "A/mm2"
    M_A_CM2 = "mA/cm2"
    M_A_FT2 = "mA/ft2"
    U_A_CM2 = "uA/cm2"
    U_A_IN2 = "uA/in2"

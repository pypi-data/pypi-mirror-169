from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ElectricFieldStrengthUom(Enum):
    """
    :cvar M_V_FT: millivolt per foot
    :cvar M_V_M: millivolt per metre
    :cvar U_V_FT: microvolt per foot
    :cvar U_V_M: microvolt per metre
    :cvar V_M: volt per metre
    """
    M_V_FT = "mV/ft"
    M_V_M = "mV/m"
    U_V_FT = "uV/ft"
    U_V_M = "uV/m"
    V_M = "V/m"

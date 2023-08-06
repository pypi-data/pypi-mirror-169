from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LengthPerPressureUom(Enum):
    """
    :cvar FT_PSI: foot per psi
    :cvar M_K_PA: metre per kilopascal
    :cvar M_PA: metre per Pascal
    """
    FT_PSI = "ft/psi"
    M_K_PA = "m/kPa"
    M_PA = "m/Pa"

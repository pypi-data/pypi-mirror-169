from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ElectricConductivityUom(Enum):
    """
    :cvar K_S_M: kilosiemens per metre
    :cvar M_S_CM: millisiemens per centimetre
    :cvar M_S_M: millisiemens per metre
    :cvar S_M: siemens per metre
    """
    K_S_M = "kS/m"
    M_S_CM = "mS/cm"
    M_S_M = "mS/m"
    S_M = "S/m"

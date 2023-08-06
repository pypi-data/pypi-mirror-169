from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PermeabilityRockUom(Enum):
    """
    :cvar D: darcy
    :cvar D_API: darcy-API
    :cvar M_D: millidarcy
    :cvar TD_API: teradarcy-API
    """
    D = "D"
    D_API = "D[API]"
    M_D = "mD"
    TD_API = "TD[API]"

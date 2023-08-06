from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MagneticVectorPotentialUom(Enum):
    """
    :cvar WB_M: weber per metre
    :cvar WB_MM: weber per millimetre
    """
    WB_M = "Wb/m"
    WB_MM = "Wb/mm"

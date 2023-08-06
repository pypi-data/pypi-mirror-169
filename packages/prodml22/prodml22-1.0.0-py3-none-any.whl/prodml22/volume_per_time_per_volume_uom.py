from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerTimePerVolumeUom(Enum):
    """
    :cvar BBL_D_ACRE_FT: barrel per day acre foot
    :cvar M3_S_M3: cubic metre per time cubic metre
    """
    BBL_D_ACRE_FT = "bbl/(d.acre.ft)"
    M3_S_M3 = "m3/(s.m3)"

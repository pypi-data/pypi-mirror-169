from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PressureTimePerVolumeUom(Enum):
    """
    :cvar PA_S_M3: pascal second per cubic metre
    :cvar PSI_D_BBL: psi day per barrel
    """
    PA_S_M3 = "Pa.s/m3"
    PSI_D_BBL = "psi.d/bbl"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MassPerVolumePerLengthUom(Enum):
    """
    :cvar G_CM4: gram per centimetre to the fourth power
    :cvar KG_DM4: kilogram per decimetre to the fourth power
    :cvar KG_M4: kilogram per metre to the fourth power
    :cvar LBM_GAL_UK_FT: pound-mass per UK gallon foot
    :cvar LBM_GAL_US_FT: pound-mass per US gallon foot
    :cvar LBM_FT4: pound-mass per foot to the fourth power
    :cvar PA_S2_M3: pascal second squared per cubic metre
    """
    G_CM4 = "g/cm4"
    KG_DM4 = "kg/dm4"
    KG_M4 = "kg/m4"
    LBM_GAL_UK_FT = "lbm/(gal[UK].ft)"
    LBM_GAL_US_FT = "lbm/(gal[US].ft)"
    LBM_FT4 = "lbm/ft4"
    PA_S2_M3 = "Pa.s2/m3"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ForceAreaUom(Enum):
    """
    :cvar DYNE_CM2: dyne square centimetre
    :cvar KGF_M2: thousand gram-force square metre
    :cvar K_N_M2: kilonewton square metre
    :cvar LBF_IN2: pound-force square inch
    :cvar M_N_M2: millinewton square metre
    :cvar N_M2: newton square metre
    :cvar PDL_CM2: poundal square centimetre
    :cvar TONF_UK_FT2: UK ton-force square foot
    :cvar TONF_US_FT2: US ton-force square foot
    """
    DYNE_CM2 = "dyne.cm2"
    KGF_M2 = "kgf.m2"
    K_N_M2 = "kN.m2"
    LBF_IN2 = "lbf.in2"
    M_N_M2 = "mN.m2"
    N_M2 = "N.m2"
    PDL_CM2 = "pdl.cm2"
    TONF_UK_FT2 = "tonf[UK].ft2"
    TONF_US_FT2 = "tonf[US].ft2"

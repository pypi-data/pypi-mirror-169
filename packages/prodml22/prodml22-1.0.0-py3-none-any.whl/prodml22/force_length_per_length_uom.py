from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ForceLengthPerLengthUom(Enum):
    """
    :cvar KGF_M_M: thousand gram-force metre per metre
    :cvar LBF_FT_IN: foot pound-force per inch
    :cvar LBF_IN_IN: pound-force inch per inch
    :cvar N_M_M: newton metre per metre
    :cvar TONF_US_MI_FT: US ton-force mile per foot
    """
    KGF_M_M = "kgf.m/m"
    LBF_FT_IN = "lbf.ft/in"
    LBF_IN_IN = "lbf.in/in"
    N_M_M = "N.m/m"
    TONF_US_MI_FT = "tonf[US].mi/ft"

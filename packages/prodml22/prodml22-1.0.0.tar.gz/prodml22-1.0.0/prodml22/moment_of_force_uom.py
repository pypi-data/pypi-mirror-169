from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MomentOfForceUom(Enum):
    """
    :cvar VALUE_1000_LBF_FT: thousand foot pound-force
    :cvar DA_N_M: dekanewton metre
    :cvar D_N_M: decinewton metre
    :cvar J: joule
    :cvar KGF_M: thousand gram-force metre
    :cvar K_N_M: kilonewton metre
    :cvar LBF_FT: foot pound-force
    :cvar LBF_IN: inch pound-force
    :cvar LBM_FT2_S2: pound-mass square foot per second squared
    :cvar N_M: newton metre
    :cvar PDL_FT: foot poundal
    :cvar TONF_US_FT: US ton-force foot
    :cvar TONF_US_MI: US ton-force mile
    """
    VALUE_1000_LBF_FT = "1000 lbf.ft"
    DA_N_M = "daN.m"
    D_N_M = "dN.m"
    J = "J"
    KGF_M = "kgf.m"
    K_N_M = "kN.m"
    LBF_FT = "lbf.ft"
    LBF_IN = "lbf.in"
    LBM_FT2_S2 = "lbm.ft2/s2"
    N_M = "N.m"
    PDL_FT = "pdl.ft"
    TONF_US_FT = "tonf[US].ft"
    TONF_US_MI = "tonf[US].mi"

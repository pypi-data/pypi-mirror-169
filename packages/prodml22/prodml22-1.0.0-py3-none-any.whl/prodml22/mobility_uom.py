from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MobilityUom(Enum):
    """
    :cvar D_PA_S: darcy per pascal second
    :cvar D_C_P: darcy per centipoise
    :cvar M_D_FT2_LBF_S: millidarcy square foot per pound-force second
    :cvar M_D_IN2_LBF_S: millidarcy square inch per pound-force second
    :cvar M_D_PA_S: millidarcy per pascal second
    :cvar M_D_C_P: millidarcy per centipoise
    :cvar TD_API_PA_S: teradarcy-API per pascal second
    """
    D_PA_S = "D/(Pa.s)"
    D_C_P = "D/cP"
    M_D_FT2_LBF_S = "mD.ft2/(lbf.s)"
    M_D_IN2_LBF_S = "mD.in2/(lbf.s)"
    M_D_PA_S = "mD/(Pa.s)"
    M_D_C_P = "mD/cP"
    TD_API_PA_S = "TD[API]/(Pa.s)"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class PureComponentKind(Enum):
    """
    Specifies the kinds of pure components.

    :cvar VALUE_1_2_4_TRIMETHYLBENZENE:
    :cvar VALUE_2_DIMETHYLBUTANE:
    :cvar VALUE_3_DIMETHYLBUTANE:
    :cvar AR:
    :cvar C1:
    :cvar C2:
    :cvar C3:
    :cvar CO2:
    :cvar COS: Carbonyl sulfide with molecular structure OCS.
    :cvar H2:
    :cvar H2O:
    :cvar H2S:
    :cvar HE:
    :cvar HG:
    :cvar I_C4:
    :cvar I_C5:
    :cvar N2:
    :cvar N_C10:
    :cvar N_C4:
    :cvar N_C5:
    :cvar N_C6:
    :cvar N_C7:
    :cvar N_C8:
    :cvar N_C9:
    :cvar NEO_C5:
    :cvar RA: Radon
    :cvar BENZENE: benzene
    :cvar VALUE_2_METHYLPENTANE:
    :cvar VALUE_3_METHYLPENTANE:
    :cvar VALUE_2_METHYLHEXANE:
    :cvar VALUE_3_METHYLHEXANE:
    :cvar VALUE_2_METHYLHEPTANE:
    :cvar VALUE_3_METHYLHEPTANE:
    :cvar CYCLOHEXANE:
    :cvar ETHYLBENZENE:
    :cvar ETHYLCYCLOHEXANE:
    :cvar METHYLCYCLOHEXANE:
    :cvar METHYLCYCLOPENTANE:
    :cvar TOLUENE:
    :cvar M_XYLENE:
    :cvar O_XYLENE:
    :cvar P_XYLENE:
    """
    VALUE_1_2_4_TRIMETHYLBENZENE = "1-2-4-trimethylbenzene"
    VALUE_2_DIMETHYLBUTANE = "2-dimethylbutane"
    VALUE_3_DIMETHYLBUTANE = "3-dimethylbutane"
    AR = "ar"
    C1 = "c1"
    C2 = "c2"
    C3 = "c3"
    CO2 = "co2"
    COS = "cos"
    H2 = "h2"
    H2O = "h2o"
    H2S = "h2s"
    HE = "he"
    HG = "hg"
    I_C4 = "i-c4"
    I_C5 = "i-c5"
    N2 = "n2"
    N_C10 = "n-c10"
    N_C4 = "n-c4"
    N_C5 = "n-c5"
    N_C6 = "n-c6"
    N_C7 = "n-c7"
    N_C8 = "n-c8"
    N_C9 = "n-c9"
    NEO_C5 = "neo-c5"
    RA = "ra"
    BENZENE = "benzene"
    VALUE_2_METHYLPENTANE = "2-methylpentane"
    VALUE_3_METHYLPENTANE = "3-methylpentane"
    VALUE_2_METHYLHEXANE = "2-methylhexane"
    VALUE_3_METHYLHEXANE = "3-methylhexane"
    VALUE_2_METHYLHEPTANE = "2-methylheptane"
    VALUE_3_METHYLHEPTANE = "3-methylheptane"
    CYCLOHEXANE = "cyclohexane"
    ETHYLBENZENE = "ethylbenzene"
    ETHYLCYCLOHEXANE = "ethylcyclohexane"
    METHYLCYCLOHEXANE = "methylcyclohexane"
    METHYLCYCLOPENTANE = "methylcyclopentane"
    TOLUENE = "toluene"
    M_XYLENE = "m-xylene"
    O_XYLENE = "o-xylene"
    P_XYLENE = "p-xylene"

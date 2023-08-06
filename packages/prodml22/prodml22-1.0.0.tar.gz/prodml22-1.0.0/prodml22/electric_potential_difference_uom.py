from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ElectricPotentialDifferenceUom(Enum):
    """
    :cvar C_V: centivolt
    :cvar D_V: decivolt
    :cvar F_V: femtovolt
    :cvar GV: gigavolt
    :cvar K_V: kilovolt
    :cvar M_V: millivolt
    :cvar MV_1: megavolt
    :cvar N_V: nanovolt
    :cvar P_V: picovolt
    :cvar TV: teravolt
    :cvar U_V: microvolt
    :cvar V: volt
    """
    C_V = "cV"
    D_V = "dV"
    F_V = "fV"
    GV = "GV"
    K_V = "kV"
    M_V = "mV"
    MV_1 = "MV"
    N_V = "nV"
    P_V = "pV"
    TV = "TV"
    U_V = "uV"
    V = "V"

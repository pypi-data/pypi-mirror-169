from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PressurePerPressureUom(Enum):
    """
    :cvar ATM_ATM: standard atmosphere per standard atmosphere
    :cvar BAR_BAR: bar per bar
    :cvar EUC: euclid
    :cvar K_PA_K_PA: kilopascal per kilopascal
    :cvar MPA_MPA: megapascal per megapascal
    :cvar PA_PA: pascal per pascal
    :cvar PSI_PSI: psi per psi
    """
    ATM_ATM = "atm/atm"
    BAR_BAR = "bar/bar"
    EUC = "Euc"
    K_PA_K_PA = "kPa/kPa"
    MPA_MPA = "MPa/MPa"
    PA_PA = "Pa/Pa"
    PSI_PSI = "psi/psi"

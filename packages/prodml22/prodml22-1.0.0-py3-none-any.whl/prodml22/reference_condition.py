from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReferenceCondition(Enum):
    """Combinations of standard temperature and pressure including "ambient".

    The list of standard values is contained in the enumValuesProdml.xml
    file.

    :cvar VALUE_0_DEG_C_1_ATM: 0 degC and 1 standard atmosphere
    :cvar VALUE_0_DEG_C_1_BAR:
    :cvar VALUE_15_DEG_C_1_ATM: 15 degC and 1 standard atmosphere
    :cvar VALUE_15_DEG_C_1_BAR:
    :cvar VALUE_20_DEG_C_1_ATM:
    :cvar VALUE_20_DEG_C_1_BAR:
    :cvar VALUE_25_DEG_C_1_BAR:
    :cvar VALUE_60_DEG_F_1_ATM: 60 degF and 1 standard atmosphere
    :cvar VALUE_60_DEG_F_30_IN_HG:
    :cvar AMBIENT:
    """
    VALUE_0_DEG_C_1_ATM = "0 degC 1 atm"
    VALUE_0_DEG_C_1_BAR = "0 degC 1 bar"
    VALUE_15_DEG_C_1_ATM = "15 degC 1 atm"
    VALUE_15_DEG_C_1_BAR = "15 degC 1 bar"
    VALUE_20_DEG_C_1_ATM = "20 degC 1 atm"
    VALUE_20_DEG_C_1_BAR = "20 degC 1 bar"
    VALUE_25_DEG_C_1_BAR = "25 degC 1 bar"
    VALUE_60_DEG_F_1_ATM = "60 degF 1 atm"
    VALUE_60_DEG_F_30_IN_HG = "60 degF 30 in Hg"
    AMBIENT = "ambient"

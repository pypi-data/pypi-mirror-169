from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReciprocalAreaUom(Enum):
    """
    :cvar VALUE_1_FT2: per square foot
    :cvar VALUE_1_KM2: per square kilometre
    :cvar VALUE_1_M2: per square metre
    :cvar VALUE_1_MI2: per square mile
    """
    VALUE_1_FT2 = "1/ft2"
    VALUE_1_KM2 = "1/km2"
    VALUE_1_M2 = "1/m2"
    VALUE_1_MI2 = "1/mi2"

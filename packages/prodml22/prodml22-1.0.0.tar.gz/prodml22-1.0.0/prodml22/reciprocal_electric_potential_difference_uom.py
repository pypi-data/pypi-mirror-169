from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ReciprocalElectricPotentialDifferenceUom(Enum):
    """
    :cvar VALUE_1_U_V: per microvolt
    :cvar VALUE_1_V: per volt
    """
    VALUE_1_U_V = "1/uV"
    VALUE_1_V = "1/V"

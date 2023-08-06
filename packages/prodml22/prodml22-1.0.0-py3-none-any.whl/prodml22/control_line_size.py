from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ControlLineSize(Enum):
    """
    Specifies the control line sizes.

    :cvar DIAMETER_0_25_IN_WEIGHT_0_028_LB_FT: diameter 0.25 in weight
        0.028 lb/ft
    :cvar DIAMETER_0_25_IN_WEIGHT_0_035_LB_FT: diameter 0.25 in weight
        0.035 lb/ft
    :cvar DIAMETER_0_375_IN_WEIGHT_0_048_LB_FT: diameter 0.375 in weight
        0.048 lb/ft
    """
    DIAMETER_0_25_IN_WEIGHT_0_028_LB_FT = "diameter 0.25 in weight 0.028 lb/ft"
    DIAMETER_0_25_IN_WEIGHT_0_035_LB_FT = "diameter 0.25 in weight 0.035 lb/ft"
    DIAMETER_0_375_IN_WEIGHT_0_048_LB_FT = "diameter 0.375 in weight 0.048 lb/ft"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ControlLineMaterial(Enum):
    """
    Specifies the types of control line material.

    :cvar INC_825: inc 825
    :cvar SS_316: ss 316
    """
    INC_825 = "inc 825"
    SS_316 = "ss 316"

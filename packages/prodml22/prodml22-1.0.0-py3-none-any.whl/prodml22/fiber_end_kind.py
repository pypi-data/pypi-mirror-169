from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FiberEndKind(Enum):
    """
    Specifies the types of fiber end.

    :cvar ANGLE_POLISHED: angle polished
    :cvar FLAT_POLISHED: flat polished
    """
    ANGLE_POLISHED = "angle polished"
    FLAT_POLISHED = "flat polished"

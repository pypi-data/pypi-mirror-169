from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class SaturationKind(Enum):
    """
    Specifies the kinds of saturation.

    :cvar SATURATED: The fluid is saturated.
    :cvar UNDERSATURATED: The fluid is under-saturated.
    """
    SATURATED = "saturated"
    UNDERSATURATED = "undersaturated"

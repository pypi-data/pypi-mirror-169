from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class CableKind(Enum):
    """
    Specifies the types of cable.

    :cvar ELECTRICAL_FIBER_CABLE: electrical-fiber-cable
    :cvar MULTI_FIBER_CABLE: multi-fiber-cable
    :cvar SINGLE_FIBER_CABLE: single-fiber-cable
    """
    ELECTRICAL_FIBER_CABLE = "electrical-fiber-cable"
    MULTI_FIBER_CABLE = "multi-fiber-cable"
    SINGLE_FIBER_CABLE = "single-fiber-cable"

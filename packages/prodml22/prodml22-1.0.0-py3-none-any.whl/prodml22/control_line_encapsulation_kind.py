from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ControlLineEncapsulationKind(Enum):
    """
    Specifies the control line encapsulation types.

    :cvar ROUND: round
    :cvar SQUARE: square
    """
    ROUND = "round"
    SQUARE = "square"

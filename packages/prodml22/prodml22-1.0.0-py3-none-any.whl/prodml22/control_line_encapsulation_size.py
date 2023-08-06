from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ControlLineEncapsulationSize(Enum):
    """
    Specifies the control line encapsulation sizes.

    :cvar VALUE_11X11: 11x11
    :cvar VALUE_23X11: 23x11
    """
    VALUE_11X11 = "11x11"
    VALUE_23X11 = "23x11"

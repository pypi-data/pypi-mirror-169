from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class Otdrdirection(Enum):
    """
    Specifies the OTDR directions.

    :cvar BACKWARD: backward
    :cvar FORWARD: forward
    """
    BACKWARD = "backward"
    FORWARD = "forward"

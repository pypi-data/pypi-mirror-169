from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class BalanceDestinationType(Enum):
    """
    Specifies the types of destinations.

    :cvar HARBOR: Defines the name of the destination harbor.
    :cvar TERMINAL: Defines the name of the destination terminal.
    :cvar UNKNOWN: Unknown.
    """
    HARBOR = "harbor"
    TERMINAL = "terminal"
    UNKNOWN = "unknown"

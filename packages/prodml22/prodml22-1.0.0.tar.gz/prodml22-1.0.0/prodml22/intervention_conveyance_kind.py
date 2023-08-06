from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class InterventionConveyanceKind(Enum):
    """
    Specifies the types of intervention conveyance.
    """
    COILED_TUBING = "coiled tubing"
    ROD = "rod"
    SLICKLINE = "slickline"
    WIRELINE = "wireline"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FiberConnectorKind(Enum):
    """
    Specifies the types of fiber connector.

    :cvar DRY_MATE: dry mate
    :cvar WET_MATE: wet mate
    """
    DRY_MATE = "dry mate"
    WET_MATE = "wet mate"

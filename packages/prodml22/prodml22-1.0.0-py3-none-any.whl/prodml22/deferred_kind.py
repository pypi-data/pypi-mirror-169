from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class DeferredKind(Enum):
    """
    Specifies the deferment status of the event.
    """
    PLANNED = "planned"
    UNPLANNED = "unplanned"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FiberSpliceKind(Enum):
    """
    Specifies the type of fiber splice.
    """
    CABLE_SPLICE = "cable splice"
    H_SPLICE = "h splice"
    USER_CUSTOM = "user-custom"

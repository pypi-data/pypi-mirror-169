from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FiberMode(Enum):
    """
    Specifies the modes of a distributed temperature survey (DTS) fiber.
    """
    MULTIMODE = "multimode"
    OTHER = "other"
    SINGLEMODE = "singlemode"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class CompressibilityKind(Enum):
    AVERAGE = "average"
    POINT = "point"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class PathDefectKind(Enum):
    """
    Specifies the types of fiber zone that can be reported on.

    :cvar DARKENED_FIBER: darkened fiber
    :cvar OTHER: other
    """
    DARKENED_FIBER = "darkened fiber"
    OTHER = "other"

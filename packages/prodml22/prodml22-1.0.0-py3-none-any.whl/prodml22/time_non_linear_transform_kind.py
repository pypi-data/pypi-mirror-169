from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class TimeNonLinearTransformKind(Enum):
    """
    Optional enum for gas pseudo time analyses using time transforms.
    """
    MATERIAL_BALANCE_PSEUDO_TIME = "material balance pseudo-time"
    PSEUDO_TIME_TRANSFORM = "pseudo-time transform"
    TIME_UN_TRANSFORMED = "time (un-transformed)"

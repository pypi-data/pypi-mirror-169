from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class CalculationMethod(Enum):
    """
    Specifies the calculation methods available for "filling in" values in an
    indexed set.

    :cvar NONE: No calculations are performed to create data where none
        exists at index points within an existing set of data.
    :cvar STEP_WISE_CONSTANT: The value is held constant until the next
        index point.
    :cvar UNKNOWN: Unknown.
    """
    NONE = "none"
    STEP_WISE_CONSTANT = "step wise constant"
    UNKNOWN = "unknown"

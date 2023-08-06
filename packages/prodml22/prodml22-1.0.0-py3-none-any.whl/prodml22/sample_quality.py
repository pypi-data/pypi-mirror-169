from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class SampleQuality(Enum):
    """
    Specifies the values for the quality of data.

    :cvar INVALID: The sample quality is invalid.
    :cvar UNKNOWN: The sample quality is unknown.
    :cvar VALID: The sample quality is valid.
    """
    INVALID = "invalid"
    UNKNOWN = "unknown"
    VALID = "valid"

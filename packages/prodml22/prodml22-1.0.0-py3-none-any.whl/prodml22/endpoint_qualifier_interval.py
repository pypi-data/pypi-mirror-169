from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class EndpointQualifierInterval(Enum):
    """
    Specifies the meaning of the endpoint for a simple interval.

    :cvar EXCLUSIVE: The value is excluded.
    :cvar INCLUSIVE: The value is included.
    :cvar UNKNOWN: The value is unknown.
    """
    EXCLUSIVE = "exclusive"
    INCLUSIVE = "inclusive"
    UNKNOWN = "unknown"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class TraceProcessingType(Enum):
    """
    Specifies the types of facility that can be mapped to for a given length of
    fiber measurement.

    :cvar AS_ACQUIRED: as acquired
    :cvar RECALIBRATED: recalibrated
    """
    AS_ACQUIRED = "as acquired"
    RECALIBRATED = "recalibrated"

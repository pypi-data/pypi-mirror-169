from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FlowSubQualifier(Enum):
    """
    Specifies specializations of a flow qualifier.
    """
    DECLINE_CURVE = "decline curve"
    DIFFERENCE = "difference"
    FISCAL = "fiscal"
    FIXED = "fixed"
    MAXIMUM = "maximum"
    MINIMUM = "minimum"
    RAW = "raw"
    RECALIBRATED = "recalibrated"
    STANDARD = "standard"

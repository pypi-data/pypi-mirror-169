from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class BusinessUnitKind(Enum):
    """
    Specifies the types of business units.
    """
    BUSINESSAREA = "businessarea"
    COMPANY = "company"
    FIELD = "field"
    LICENSE = "license"
    PLATFORM = "platform"
    TERMINAL = "terminal"
    UNKNOWN = "unknown"

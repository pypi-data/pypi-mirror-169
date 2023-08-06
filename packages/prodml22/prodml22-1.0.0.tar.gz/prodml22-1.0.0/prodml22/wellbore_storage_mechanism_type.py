from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class WellboreStorageMechanismType(Enum):
    CLOSED_CHAMBER = "closed chamber"
    FULL_WELL = "full well"
    RISING_LEVEL = "rising level"

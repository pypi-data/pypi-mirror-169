from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ReservoirLifeCycleState(Enum):
    """
    Specifies the states of the reservoir lifecycle.
    """
    ABANDONED = "abandoned"
    PRIMARY_PRODUCTION = "primary production"
    PROSPECT = "prospect"
    TERTIARY_PRODUCTION = "tertiary production"
    UNDEVELOPED = "undeveloped"
    SECONDARY_RECOVERY = "secondary recovery"

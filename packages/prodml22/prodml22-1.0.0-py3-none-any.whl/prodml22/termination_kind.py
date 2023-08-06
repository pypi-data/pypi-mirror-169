from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class TerminationKind(Enum):
    """
    Specifies the types of fiber terminations.
    """
    LOOPED_BACK_TO_INSTRUMENT_BOX = "looped back to instrument box"
    TERMINATION_AT_CABLE = "termination at cable"

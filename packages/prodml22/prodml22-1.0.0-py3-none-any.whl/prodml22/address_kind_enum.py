from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AddressKindEnum(Enum):
    """
    Specifies the kinds of company addresses.

    :cvar BOTH:
    :cvar MAILING:
    :cvar PHYSICAL: physical
    """
    BOTH = "both"
    MAILING = "mailing"
    PHYSICAL = "physical"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class MixingRule(Enum):
    """
    Specifies the kinds of mixing rules.

    :cvar ASYMMETRIC: The mixing rule kind is asymmetric.
    :cvar CLASSICAL: The mixing rule kind is classical.
    """
    ASYMMETRIC = "asymmetric"
    CLASSICAL = "classical"

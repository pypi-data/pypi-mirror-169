from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PotentialDifferencePerPowerDropUom(Enum):
    """
    :cvar V_B: volt per bel
    :cvar V_D_B: volt per decibel
    """
    V_B = "V/B"
    V_D_B = "V/dB"

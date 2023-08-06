from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class NormalizedPowerUom(Enum):
    """
    :cvar B_W: bel watt
    :cvar D_B_M_W: decibel milliwatt
    :cvar D_B_MW_1: decibel megawatt
    :cvar D_B_W: decibel watt
    """
    B_W = "B.W"
    D_B_M_W = "dB.mW"
    D_B_MW_1 = "dB.MW"
    D_B_W = "dB.W"

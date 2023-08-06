from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AttenuationPerFrequencyIntervalUom(Enum):
    """
    :cvar B_O: bel per octave
    :cvar D_B_O: decibel per octave
    """
    B_O = "B/O"
    D_B_O = "dB/O"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class DataTransferSpeedUom(Enum):
    """
    :cvar BIT_S: bit per second
    :cvar BYTE_S: byte per second
    """
    BIT_S = "bit/s"
    BYTE_S = "byte/s"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VerticalCoordinateUom(Enum):
    """
    The units of measure that are valid for vertical gravity based coordinates
    (i.e., elevation or vertical depth).

    :cvar M: meter
    :cvar FT: International Foot
    :cvar FT_US: US Survey Foot
    :cvar FT_BR_65: British Foot 1865
    """
    M = "m"
    FT = "ft"
    FT_US = "ftUS"
    FT_BR_65 = "ftBr(65)"

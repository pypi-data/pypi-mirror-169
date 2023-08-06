from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class LengthPerVolumeUom(Enum):
    """
    :cvar FT_BBL: foot per barrel
    :cvar FT_FT3: foot per cubic foot
    :cvar FT_GAL_US: foot per US gallon
    :cvar KM_DM3: kilometre per cubic decimetre
    :cvar KM_L: kilometre per litre
    :cvar M_M3: metre per cubic metre
    :cvar MI_GAL_UK: mile per UK gallon
    :cvar MI_GAL_US: mile per US gallon
    """
    FT_BBL = "ft/bbl"
    FT_FT3 = "ft/ft3"
    FT_GAL_US = "ft/gal[US]"
    KM_DM3 = "km/dm3"
    KM_L = "km/L"
    M_M3 = "m/m3"
    MI_GAL_UK = "mi/gal[UK]"
    MI_GAL_US = "mi/gal[US]"

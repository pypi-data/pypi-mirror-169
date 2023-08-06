from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerTimePerTimeUom(Enum):
    """
    :cvar BBL_D2: (barrel per day) per day
    :cvar BBL_H2: (barrel per hour) per hour
    :cvar DM3_S2: (cubic decimetre per second) per second
    :cvar FT3_D2: (cubic foot per day) per day
    :cvar FT3_H2: (cubic foot per hour) per hour
    :cvar FT3_MIN2: (cubic foot per minute) per minute
    :cvar FT3_S2: (cubic foot per second) per second
    :cvar GAL_UK_H2: (UK gallon per hour) per hour
    :cvar GAL_UK_MIN2: (UK gallon per minute) per minute
    :cvar GAL_US_H2: (US gallon per hour) per hour
    :cvar GAL_US_MIN2: (US gallon per minute) per minute
    :cvar L_S2: (litre per second) per second
    :cvar M3_D2: (cubic metre per day) per day
    :cvar M3_S2: cubic metre per second squared
    """
    BBL_D2 = "bbl/d2"
    BBL_H2 = "bbl/h2"
    DM3_S2 = "dm3/s2"
    FT3_D2 = "ft3/d2"
    FT3_H2 = "ft3/h2"
    FT3_MIN2 = "ft3/min2"
    FT3_S2 = "ft3/s2"
    GAL_UK_H2 = "gal[UK]/h2"
    GAL_UK_MIN2 = "gal[UK]/min2"
    GAL_US_H2 = "gal[US]/h2"
    GAL_US_MIN2 = "gal[US]/min2"
    L_S2 = "L/s2"
    M3_D2 = "m3/d2"
    M3_S2 = "m3/s2"

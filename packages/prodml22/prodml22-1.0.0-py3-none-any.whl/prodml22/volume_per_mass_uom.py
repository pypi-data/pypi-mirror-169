from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class VolumePerMassUom(Enum):
    """
    :cvar VALUE_0_01_L_KG: litre per hundred kilogram
    :cvar BBL_TON_UK: barrel per UK ton-mass
    :cvar BBL_TON_US: barrel per US ton-mass
    :cvar CM3_G: cubic centimetre per gram
    :cvar DM3_KG: cubic decimetre per kilogram
    :cvar DM3_T: cubic decimetre per ton
    :cvar FT3_KG: cubic foot per kilogram
    :cvar FT3_LBM: cubic foot per pound-mass
    :cvar FT3_SACK_94LBM: cubic foot per 94-pound-sack
    :cvar GAL_UK_LBM: UK gallon per pound-mass
    :cvar GAL_US_LBM: US gallon per pound-mass
    :cvar GAL_US_SACK_94LBM: US gallon per 94-pound-sack
    :cvar GAL_US_TON_UK: US gallon per UK ton-mass
    :cvar GAL_US_TON_US: US gallon per US ton-mass
    :cvar L_KG: litre per kilogram
    :cvar L_T: litre per tonne
    :cvar L_TON_UK: litre per UK ton-mass
    :cvar M3_G: cubic metre per gram
    :cvar M3_KG: cubic metre per kilogram
    :cvar M3_T: cubic metre per tonne
    :cvar M3_TON_UK: cubic metre per UK ton-mass
    :cvar M3_TON_US: cubic metre per US ton-mass
    """
    VALUE_0_01_L_KG = "0.01 L/kg"
    BBL_TON_UK = "bbl/ton[UK]"
    BBL_TON_US = "bbl/ton[US]"
    CM3_G = "cm3/g"
    DM3_KG = "dm3/kg"
    DM3_T = "dm3/t"
    FT3_KG = "ft3/kg"
    FT3_LBM = "ft3/lbm"
    FT3_SACK_94LBM = "ft3/sack[94lbm]"
    GAL_UK_LBM = "gal[UK]/lbm"
    GAL_US_LBM = "gal[US]/lbm"
    GAL_US_SACK_94LBM = "gal[US]/sack[94lbm]"
    GAL_US_TON_UK = "gal[US]/ton[UK]"
    GAL_US_TON_US = "gal[US]/ton[US]"
    L_KG = "L/kg"
    L_T = "L/t"
    L_TON_UK = "L/ton[UK]"
    M3_G = "m3/g"
    M3_KG = "m3/kg"
    M3_T = "m3/t"
    M3_TON_UK = "m3/ton[UK]"
    M3_TON_US = "m3/ton[US]"

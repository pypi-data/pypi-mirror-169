from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class EnergyPerVolumeUom(Enum):
    """
    :cvar BTU_IT_BBL: BTU per barrel
    :cvar BTU_IT_FT3: BTU per cubic foot
    :cvar BTU_IT_GAL_UK: BTU per UK gallon
    :cvar BTU_IT_GAL_US: BTU per US gallon
    :cvar CAL_TH_CM3: calorie per cubic centimetre
    :cvar CAL_TH_M_L: calorie per millilitre
    :cvar CAL_TH_MM3: calorie per cubic millimetre
    :cvar ERG_CM3: erg per cubic centimetre
    :cvar ERG_M3: erg per cubic metre
    :cvar HP_H_BBL: horsepower hour per barrel
    :cvar J_DM3: joule per cubic decimetre
    :cvar J_M3: joule per cubic metre
    :cvar KCAL_TH_CM3: thousand calorie per cubic centimetre
    :cvar KCAL_TH_M3: thousand calorie per cubic metre
    :cvar K_J_DM3: kilojoule per cubic decimetre
    :cvar K_J_M3: kilojoule per cubic metre
    :cvar K_W_H_DM3: kilowatt hour per cubic decimetre
    :cvar K_W_H_M3: kilowatt hour per cubic metre
    :cvar LBF_FT_BBL: foot pound-force per barrel
    :cvar LBF_FT_GAL_US: foot pound-force per US gallon
    :cvar MJ_M3: megajoule per cubic metre
    :cvar MW_H_M3: megawatt hour per cubic metre
    :cvar TONF_US_MI_BBL: US ton-force mile per barrel
    """
    BTU_IT_BBL = "Btu[IT]/bbl"
    BTU_IT_FT3 = "Btu[IT]/ft3"
    BTU_IT_GAL_UK = "Btu[IT]/gal[UK]"
    BTU_IT_GAL_US = "Btu[IT]/gal[US]"
    CAL_TH_CM3 = "cal[th]/cm3"
    CAL_TH_M_L = "cal[th]/mL"
    CAL_TH_MM3 = "cal[th]/mm3"
    ERG_CM3 = "erg/cm3"
    ERG_M3 = "erg/m3"
    HP_H_BBL = "hp.h/bbl"
    J_DM3 = "J/dm3"
    J_M3 = "J/m3"
    KCAL_TH_CM3 = "kcal[th]/cm3"
    KCAL_TH_M3 = "kcal[th]/m3"
    K_J_DM3 = "kJ/dm3"
    K_J_M3 = "kJ/m3"
    K_W_H_DM3 = "kW.h/dm3"
    K_W_H_M3 = "kW.h/m3"
    LBF_FT_BBL = "lbf.ft/bbl"
    LBF_FT_GAL_US = "lbf.ft/gal[US]"
    MJ_M3 = "MJ/m3"
    MW_H_M3 = "MW.h/m3"
    TONF_US_MI_BBL = "tonf[US].mi/bbl"

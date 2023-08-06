from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MassPerEnergyUom(Enum):
    """
    :cvar KG_K_W_H: kilogram per kilowatt hour
    :cvar KG_J: kilogram per joule
    :cvar KG_MJ: kilogram per megajoule
    :cvar LBM_HP_H: pound-mass per horsepower hour
    :cvar MG_J: milligram per joule
    """
    KG_K_W_H = "kg/(kW.h)"
    KG_J = "kg/J"
    KG_MJ = "kg/MJ"
    LBM_HP_H = "lbm/(hp.h)"
    MG_J = "mg/J"

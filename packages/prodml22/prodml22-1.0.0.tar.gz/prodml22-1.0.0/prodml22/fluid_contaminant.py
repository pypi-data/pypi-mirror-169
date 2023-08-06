from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FluidContaminant(Enum):
    """
    Specifies the kinds of contaminating fluid present in a fluid sample.

    :cvar CEMENT_FLUIDS: The fluid contaminant is cement fluids.
    :cvar COMPLETION_FLUID: The fluid contaminant is completion fluid.
    :cvar DRILLING_MUD: The fluid contaminant is drilling mud.
    :cvar EXTRANEOUS_GAS: The fluid contaminant is extraneous gas.
    :cvar EXTRANEOUS_OIL: The fluid contaminant is extraneous oil.
    :cvar EXTRANEOUS_WATER: The fluid contaminant is extraneous water.
    :cvar FORMATION_WATER: The fluid contaminant is formation water.
    :cvar TREATMENT_CHEMICALS: The fluid contaminant is treatment
        chemicals.
    :cvar SOLID: The fluid contaminant is solid.
    :cvar UNKNOWN: The fluid contaminant is unknown.
    """
    CEMENT_FLUIDS = "cement fluids"
    COMPLETION_FLUID = "completion fluid"
    DRILLING_MUD = "drilling mud"
    EXTRANEOUS_GAS = "extraneous gas"
    EXTRANEOUS_OIL = "extraneous oil"
    EXTRANEOUS_WATER = "extraneous water"
    FORMATION_WATER = "formation water"
    TREATMENT_CHEMICALS = "treatment chemicals"
    SOLID = "solid"
    UNKNOWN = "unknown"

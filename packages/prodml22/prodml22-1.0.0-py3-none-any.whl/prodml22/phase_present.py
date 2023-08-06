from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class PhasePresent(Enum):
    """Specifies the values for phase present.

    It can be water, gas or oil;  each combination of any two phases; or
    all three phases.

    :cvar GAS_AND_OIL_AND_WATER: All three phases--gas and oil and water
        --are present.
    :cvar WATER: The phase present is water.
    :cvar GAS: The phase present is gas.
    :cvar OIL: The phase present is oil.
    :cvar OIL_AND_GAS: The phases present are oil and gas.
    :cvar OIL_AND_WATER: The phases present are oil and water.
    :cvar GAS_AND_WATER: The phases present are gas and water.
    """
    GAS_AND_OIL_AND_WATER = "gas and oil and water"
    WATER = "water"
    GAS = "gas"
    OIL = "oil"
    OIL_AND_GAS = "oil and gas"
    OIL_AND_WATER = "oil and water"
    GAS_AND_WATER = "gas and water"

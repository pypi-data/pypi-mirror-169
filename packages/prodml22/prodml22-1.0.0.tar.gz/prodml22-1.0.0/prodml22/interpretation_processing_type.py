from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class InterpretationProcessingType(Enum):
    """
    Specifies the types of mnemonics.

    :cvar AVERAGED: averaged
    :cvar DENORMALIZED: denormalized
    :cvar DEPTH_CORRECTED: depth-corrected
    :cvar MANUFACTURER_GENERATED: manufacturer-generated
    :cvar TEMPERATURE_SHIFTED: temperature-shifted
    :cvar USER_CUSTOM: user-custom
    """
    AVERAGED = "averaged"
    DENORMALIZED = "denormalized"
    DEPTH_CORRECTED = "depth-corrected"
    MANUFACTURER_GENERATED = "manufacturer-generated"
    TEMPERATURE_SHIFTED = "temperature-shifted"
    USER_CUSTOM = "user-custom"

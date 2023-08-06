from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ProductFluidKind(Enum):
    """
    Specifies the kinds of product in a fluid system.
    """
    CONDENSATE = "condensate"
    CONDENSATE_GROSS = "condensate - gross"
    CONDENSATE_NET = "condensate - net"
    CRUDE_STABILIZED = "crude - stabilized"
    GAS_COMPONENT_IN_OIL = "gas - component in oil"
    GAS_DRY = "gas - dry"
    GAS_RICH = "gas - rich"
    GAS_WET = "gas - wet"
    LIQUEFIED_NATURAL_GAS = "liquefied natural gas"
    LIQUEFIED_PETROLEUM_GAS = "liquefied petroleum gas"
    LIQUID = "liquid"
    NAPHTHA = "naphtha"
    NATURAL_GAS_LIQUID = "natural gas liquid"
    NGL_COMPONENT_IN_GAS = "NGL - component in gas"
    OIL_COMPONENT_IN_WATER = "oil - component in water"
    OIL_GROSS = "oil - gross"
    OIL_NET = "oil - net"
    OIL_AND_GAS = "oil and gas"
    PETROLEUM_GAS_LIQUID = "petroleum gas liquid"
    VAPOR = "vapor"
    SAND = "sand"
    WATER_DISCHARGE = "water - discharge"
    WATER_PROCESSED = "water - processed"

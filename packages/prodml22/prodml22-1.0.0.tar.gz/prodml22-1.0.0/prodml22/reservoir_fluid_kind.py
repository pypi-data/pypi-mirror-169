from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ReservoirFluidKind(Enum):
    """
    Specifies the kinds of reservoir hydrocarbon fluid, in broad terms, by
    their phase behavior.

    :cvar BLACK_OIL: black oil
    :cvar CRITICAL_OR_NEAR_CRITICAL: critical or near critical
    :cvar DRY_GAS: dry gas
    :cvar HEAVY_OIL: heavy oil
    :cvar WET_GAS_OR_CONDENSATE: wet gas or condensate
    :cvar VOLATILE_OIL: volatile oil
    :cvar UNKNOWN: unknown
    """
    BLACK_OIL = "black oil"
    CRITICAL_OR_NEAR_CRITICAL = "critical or near critical"
    DRY_GAS = "dry gas"
    HEAVY_OIL = "heavy oil"
    WET_GAS_OR_CONDENSATE = "wet gas or condensate"
    VOLATILE_OIL = "volatile oil"
    UNKNOWN = "unknown"

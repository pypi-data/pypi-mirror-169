from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class WellOperationMethod(Enum):
    """
    Specifies the lift methods for producing a well.

    :cvar CONTINUOUS_GAS_LIFT: continuous gas lift
    :cvar ELECTRIC_SUBMERSIBLE_PUMP_LIFT: electric submersible pump lift
    :cvar FOAM_LIFT: foam lift
    :cvar HYDRAULIC_PUMP_LIFT: hydraulic pump lift
    :cvar INTERMITTENT_GAS_LIFT: intermittent gas lift
    :cvar JET_PUMP_LIFT: jet pump lift
    :cvar NATURAL_FLOW: natural flow
    :cvar PLUNGER_GAS_LIFT: plunger gas lift
    :cvar PROGRESSIVE_CAVITY_PUMP_LIFT: progressive cavity pump lift
    :cvar SUCKER_ROD_PUMP_LIFT: sucker rod pump lift
    :cvar UNKNOWN: unknown
    """
    CONTINUOUS_GAS_LIFT = "continuous gas lift"
    ELECTRIC_SUBMERSIBLE_PUMP_LIFT = "electric submersible pump lift"
    FOAM_LIFT = "foam lift"
    HYDRAULIC_PUMP_LIFT = "hydraulic pump lift"
    INTERMITTENT_GAS_LIFT = "intermittent gas lift"
    JET_PUMP_LIFT = "jet pump lift"
    NATURAL_FLOW = "natural flow"
    PLUNGER_GAS_LIFT = "plunger gas lift"
    PROGRESSIVE_CAVITY_PUMP_LIFT = "progressive cavity pump lift"
    SUCKER_ROD_PUMP_LIFT = "sucker rod pump lift"
    UNKNOWN = "unknown"

from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FluidAnalysisStepCondition(Enum):
    """
    Specifies the conditions of a fluid analysis step.

    :cvar CURRENT_RESERVOIR_CONDITIONS: The fluid analysis step is at
        current reservoir conditions.
    :cvar INITIAL_RESERVOIR_CONDITIONS: The fluid analysis step is at
        initial reservoir conditions.
    :cvar INITIAL_SATURATION_CONDITIONS: The fluid analysis step is at
        initial saturation conditions.
    :cvar STOCK_TANK_CONDITIONS: The fluid analysis step is at stock
        tank conditions.
    """
    CURRENT_RESERVOIR_CONDITIONS = "current reservoir conditions"
    INITIAL_RESERVOIR_CONDITIONS = "initial reservoir conditions"
    INITIAL_SATURATION_CONDITIONS = "initial saturation conditions"
    STOCK_TANK_CONDITIONS = "stock tank conditions"

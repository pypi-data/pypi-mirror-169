from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class QuantityMethod(Enum):
    """
    Specifies the available methods for deriving a quantity or volume.

    :cvar ALLOCATED: allocated
    :cvar ALLOWED: allowed
    :cvar ESTIMATED: estimated
    :cvar TARGET: target
    :cvar MEASURED: measured
    :cvar BUDGET: budget
    :cvar CONSTRAINT: constraint
    :cvar FORECAST: forecast
    """
    ALLOCATED = "allocated"
    ALLOWED = "allowed"
    ESTIMATED = "estimated"
    TARGET = "target"
    MEASURED = "measured"
    BUDGET = "budget"
    CONSTRAINT = "constraint"
    FORECAST = "forecast"

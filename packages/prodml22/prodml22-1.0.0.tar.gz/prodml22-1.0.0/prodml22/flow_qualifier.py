from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FlowQualifier(Enum):
    """
    Specifies qualifiers for the type of flow.
    """
    ALLOCATED = "allocated"
    BUDGET = "budget"
    CONSTRAINT = "constraint"
    DERIVED = "derived"
    DIFFERENCE = "difference"
    ESTIMATE = "estimate"
    FORECAST = "forecast"
    MASS_ADJUSTED = "mass adjusted"
    MEASURED = "measured"
    METERED = "metered"
    METERED_FISCAL = "metered - fiscal"
    NOMINATED = "nominated"
    POTENTIAL = "potential"
    PROCESSED = "processed"
    QUOTA = "quota"
    RECOMMENDED = "recommended"
    SIMULATED = "simulated"
    TARGET = "target"
    TARIFF_BASIS = "tariff basis"
    VALUE_ADJUSTED = "value adjusted"

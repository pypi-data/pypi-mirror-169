from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class EstimationMethod(Enum):
    """
    Specifies the methods for estimating deferred production.

    :cvar ANALYTICS_MODEL: analytics model
    :cvar DECLINE_CURVE: decline curve
    :cvar EXPERT_RECOMMENDATION: recommendation text
    :cvar FLOWING_MATERIAL_BALANCE: flowing material balance
    :cvar FROM_LAST_ALLOCATED_VOLUME: from last allocated volume
    :cvar NUMERICAL_RESERVOIR_SIMULATION: numerical reservoir simulation
    :cvar PRODUCTION_PROFILE: production profile
    :cvar RATE_TRANSIENT_ANALYSIS: rate transient analysis
    :cvar RATIO_ANALYSIS: ration analysis
    :cvar RESERVOIR_MODEL: reservoir model
    :cvar WELL_MODEL: well model
    """
    ANALYTICS_MODEL = "analytics model"
    DECLINE_CURVE = "decline curve"
    EXPERT_RECOMMENDATION = "expert recommendation"
    FLOWING_MATERIAL_BALANCE = "flowing material balance"
    FROM_LAST_ALLOCATED_VOLUME = "from last allocated volume"
    NUMERICAL_RESERVOIR_SIMULATION = "numerical reservoir simulation"
    PRODUCTION_PROFILE = "production profile"
    RATE_TRANSIENT_ANALYSIS = "rate transient analysis"
    RATIO_ANALYSIS = "ratio analysis"
    RESERVOIR_MODEL = "reservoir model"
    WELL_MODEL = "well model"

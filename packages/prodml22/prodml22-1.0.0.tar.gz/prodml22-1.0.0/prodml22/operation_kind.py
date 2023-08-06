from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class OperationKind(Enum):
    """
    Specifies the types of production operations for which general comments can
    be defined.

    :cvar AIR_TRAFFIC: air traffic
    :cvar CONSTRUCTION: construction
    :cvar DEVIATIONS: deviations
    :cvar MAINTENANCE: maintenance
    :cvar OTHER: other
    :cvar POWER_STATION_FAILURE: power station failure
    :cvar PRODUCTION: production
    :cvar WELL: well
    """
    AIR_TRAFFIC = "air traffic"
    CONSTRUCTION = "construction"
    DEVIATIONS = "deviations"
    MAINTENANCE = "maintenance"
    OTHER = "other"
    POWER_STATION_FAILURE = "power station failure"
    PRODUCTION = "production"
    WELL = "well"

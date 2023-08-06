from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AngularVelocityUom(Enum):
    """
    :cvar DEGA_H: angular degree per hour
    :cvar DEGA_MIN: angular degree per minute
    :cvar DEGA_S: angular degree per second
    :cvar RAD_S: radian per second
    :cvar REV_S: revolution per second
    :cvar RPM: revolution per minute
    """
    DEGA_H = "dega/h"
    DEGA_MIN = "dega/min"
    DEGA_S = "dega/s"
    RAD_S = "rad/s"
    REV_S = "rev/s"
    RPM = "rpm"

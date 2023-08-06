from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class OpticalPathConfiguration(Enum):
    """
    Specifies the types of configuration of an optical path.

    :cvar ACCURATE_SINGLE_ENDED_DUAL_LASER: accurate single-ended/dual
        laser
    :cvar DIFFERENTIAL_LOSS_CALIBRATED: differential loss calibrated
    :cvar DOUBLE_ENDED: double-ended
    :cvar SINGLE_ENDED: single-ended
    """
    ACCURATE_SINGLE_ENDED_DUAL_LASER = "accurate single-ended/dual laser"
    DIFFERENTIAL_LOSS_CALIBRATED = "differential loss calibrated"
    DOUBLE_ENDED = "double-ended"
    SINGLE_ENDED = "single-ended"

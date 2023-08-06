from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ValueStatus(Enum):
    """Specifies the indicators of the quality of a value.

    This is designed for a SCADA or OPC style of value status.

    :cvar ACCESS_DENIED: access denied
    :cvar BAD: bad
    :cvar BAD_CALIBRATION: bad calibration
    :cvar CALCULATION_FAILURE: calculation failure
    :cvar COMM_FAILURE: comm failure
    :cvar DEVICE_FAILURE: device failure
    :cvar FROZEN: frozen
    :cvar NOT_AVAILABLE: not available
    :cvar OVERFLOW: overflow
    :cvar QUESTIONABLE: questionable
    :cvar RANGE_LIMIT: range limit
    :cvar SENSOR_FAILURE: sensor failure
    :cvar SUBSTITUTED: substituted
    :cvar TIMEOUT: timeout
    """
    ACCESS_DENIED = "access denied"
    BAD = "bad"
    BAD_CALIBRATION = "bad calibration"
    CALCULATION_FAILURE = "calculation failure"
    COMM_FAILURE = "comm failure"
    DEVICE_FAILURE = "device failure"
    FROZEN = "frozen"
    NOT_AVAILABLE = "not available"
    OVERFLOW = "overflow"
    QUESTIONABLE = "questionable"
    RANGE_LIMIT = "range limit"
    SENSOR_FAILURE = "sensor failure"
    SUBSTITUTED = "substituted"
    TIMEOUT = "timeout"

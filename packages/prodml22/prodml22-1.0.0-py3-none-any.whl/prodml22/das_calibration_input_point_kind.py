from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class DasCalibrationInputPointKind(Enum):
    """The kind of calibration point.

    This is an extensible enumeration type. Current enum values are ‘tap
    test’ and ‘other calibration point’. Other commonly used calibration
    points are understood to be packers, sub surface safety valves,
    perforations, all of which give recognizable noise signals observed
    in the DAS data.  At the time of issue of this standard there is not
    a consensus regarding which other values should be regarded as
    standard kinds of calibration input points.

    :cvar OTHER_CALIBRATION_POINT: A Calibration Input Point which is of
        any kind other than a Tap Test.
    :cvar TAP_TEST: A tap test Calibration Input Point.
    """
    OTHER_CALIBRATION_POINT = "other calibration point"
    TAP_TEST = "tap test"

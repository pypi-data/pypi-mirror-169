from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OrientationWellTrajectory(AbstractParameter):
    """For a slant wellbore or horizontal wellbore model, the azimuth of the
    wellbore in the horizontal plane, represented in the local CRS.

    This is intended to be a value representative of the azimuth for the
    purposes of PTA. It is not necessarily the azimuth which would be
    recorded in a survey of the wellbore trajectory.
    """
    abbreviation: str = field(
        init=False,
        default="OrientationWellTrajectory",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FractureAngleToWellbore(AbstractParameter):
    """For a multiple fractured horizontal wellbore model, the angle at which
    fractures intersect the wellbore.

    A value of 90 degrees indicates the fracture plane is normal to the
    wellbore trajectory.
    """
    abbreviation: str = field(
        init=False,
        default="FractureAngleToWellbore",
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

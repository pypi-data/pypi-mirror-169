from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WellboreDeviationAngle(AbstractParameter):
    """
    The angle of deviation from vertical of the wellbore, generally used for
    estimations of wellbore storage when the tubing is filling up.
    """
    abbreviation: str = field(
        init=False,
        default="Deviation",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    plane_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "PlaneAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

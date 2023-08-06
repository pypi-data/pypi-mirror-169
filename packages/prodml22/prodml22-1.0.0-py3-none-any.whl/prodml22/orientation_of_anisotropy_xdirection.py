from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OrientationOfAnisotropyXdirection(AbstractParameter):
    """In the case where there is horizontal anisotropy, the orientation of the
    x direction represented in the local CRS.

    Optional since many models do not account for this parameter.
    """
    class Meta:
        name = "OrientationOfAnisotropyXDirection"

    abbreviation: str = field(
        init=False,
        default="OrientationOfAnisotropy_XDirection",
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

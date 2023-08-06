from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract3d_position import Abstract3DPosition
from prodml22.geocentric3d_crs import Geocentric3DCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Geocentric3DPosition(Abstract3DPosition):
    class Meta:
        name = "Geocentric3dPosition"

    coordinate1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    coordinate2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    coordinate3: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate3",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    geocentric3d_crs: Optional[Geocentric3DCrs] = field(
        default=None,
        metadata={
            "name": "Geocentric3dCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

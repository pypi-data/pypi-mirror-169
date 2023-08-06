from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LocationIn2D:
    """
    A location expressed in terms of X,Y coordinates of some part of a PTA
    object.

    :ivar coordinate_x: X coordinate of a point.
    :ivar coordinate_y: Y coordinate of a point.
    """
    coordinate_x: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "CoordinateX",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    coordinate_y: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "CoordinateY",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

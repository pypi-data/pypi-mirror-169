from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_reference_point import AbstractReferencePoint
from prodml22.data_object_reference import DataObjectReference
from prodml22.horizontal_coordinates import HorizontalCoordinates

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReferencePointInAlocalEngineeringCompoundCrs(AbstractReferencePoint):
    """A reference point which is defined in the context of a compound (2D
    horizontal + 1D vertical) CRS.

    Note that a 2D compound CRS can be transferred  by omitting the
    vertical Coordinate3
    """
    class Meta:
        name = "ReferencePointInALocalEngineeringCompoundCrs"
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    horizontal_coordinates: Optional[HorizontalCoordinates] = field(
        default=None,
        metadata={
            "name": "HorizontalCoordinates",
            "type": "Element",
        }
    )
    vertical_coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "VerticalCoordinate",
            "type": "Element",
        }
    )
    crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Crs",
            "type": "Element",
            "required": True,
        }
    )

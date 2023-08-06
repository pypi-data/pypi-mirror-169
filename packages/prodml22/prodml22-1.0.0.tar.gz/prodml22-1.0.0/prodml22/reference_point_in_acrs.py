from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_horizontal_coordinates import AbstractHorizontalCoordinates
from prodml22.abstract_reference_point import AbstractReferencePoint
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReferencePointInAcrs(AbstractReferencePoint):
    """
    A reference point which is defined in the context of a compound (2d
    horizontal + 1D vertical) CRS.
    """
    class Meta:
        name = "ReferencePointInACrs"
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    vertical_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "VerticalCrs",
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
    horizontal_coordinates: Optional[AbstractHorizontalCoordinates] = field(
        default=None,
        metadata={
            "name": "HorizontalCoordinates",
            "type": "Element",
        }
    )

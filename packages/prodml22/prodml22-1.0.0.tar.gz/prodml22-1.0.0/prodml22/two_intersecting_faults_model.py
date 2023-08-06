from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.angle_between_boundaries import AngleBetweenBoundaries
from prodml22.boundary1_type import Boundary1Type
from prodml22.boundary2_type import Boundary2Type
from prodml22.boundary_base_model import BoundaryBaseModel
from prodml22.distance_to_boundary1 import DistanceToBoundary1
from prodml22.distance_to_boundary2 import DistanceToBoundary2
from prodml22.orientation_of_normal_to_boundary1 import OrientationOfNormalToBoundary1

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class TwoIntersectingFaultsModel(BoundaryBaseModel):
    """Two intersecting faults boundary model.

    Two linear non-parallel boundaries run along adjacent sides of the
    reservoir and intersect at an arbitrary angle.
    """
    distance_to_boundary1: Optional[DistanceToBoundary1] = field(
        default=None,
        metadata={
            "name": "DistanceToBoundary1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    distance_to_boundary2: Optional[DistanceToBoundary2] = field(
        default=None,
        metadata={
            "name": "DistanceToBoundary2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    orientation_of_normal_to_boundary1: Optional[OrientationOfNormalToBoundary1] = field(
        default=None,
        metadata={
            "name": "OrientationOfNormalToBoundary1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    angle_between_boundaries: Optional[AngleBetweenBoundaries] = field(
        default=None,
        metadata={
            "name": "AngleBetweenBoundaries",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    boundary1_type: Optional[Boundary1Type] = field(
        default=None,
        metadata={
            "name": "Boundary1Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    boundary2_type: Optional[Boundary2Type] = field(
        default=None,
        metadata={
            "name": "Boundary2Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.boundary_base_model import BoundaryBaseModel
from prodml22.distance_to_pinch_out import DistanceToPinchOut
from prodml22.orientation_of_normal_to_boundary1 import OrientationOfNormalToBoundary1

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PinchOutModel(BoundaryBaseModel):
    """Pinch Out boundary model.

    The upper and lower bounding surfaces of the reservoir are sub-
    parallel and intersect some distance from the wellbore. Other
    directions are unbounded.
    """
    orientation_of_normal_to_boundary1: Optional[OrientationOfNormalToBoundary1] = field(
        default=None,
        metadata={
            "name": "OrientationOfNormalToBoundary1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    distance_to_pinch_out: Optional[DistanceToPinchOut] = field(
        default=None,
        metadata={
            "name": "DistanceToPinchOut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

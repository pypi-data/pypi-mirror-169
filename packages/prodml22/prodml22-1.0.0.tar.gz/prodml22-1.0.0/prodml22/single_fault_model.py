from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.boundary1_type import Boundary1Type
from prodml22.boundary_base_model import BoundaryBaseModel
from prodml22.distance_to_boundary1 import DistanceToBoundary1
from prodml22.orientation_of_normal_to_boundary1 import OrientationOfNormalToBoundary1

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SingleFaultModel(BoundaryBaseModel):
    """Single fault boundary model.

    A single linear boundary runs along one side of the reservoir.
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
    orientation_of_normal_to_boundary1: Optional[OrientationOfNormalToBoundary1] = field(
        default=None,
        metadata={
            "name": "OrientationOfNormalToBoundary1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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

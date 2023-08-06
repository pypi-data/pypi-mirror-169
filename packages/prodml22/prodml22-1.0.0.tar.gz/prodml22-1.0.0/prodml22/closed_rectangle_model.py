from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.boundary1_type import Boundary1Type
from prodml22.boundary2_type import Boundary2Type
from prodml22.boundary3_type import Boundary3Type
from prodml22.boundary4_type import Boundary4Type
from prodml22.boundary_base_model import BoundaryBaseModel
from prodml22.distance_to_boundary1 import DistanceToBoundary1
from prodml22.distance_to_boundary2 import DistanceToBoundary2
from prodml22.distance_to_boundary3 import DistanceToBoundary3
from prodml22.distance_to_boundary4 import DistanceToBoundary4
from prodml22.drainage_area_measured import DrainageAreaMeasured
from prodml22.orientation_of_normal_to_boundary1 import OrientationOfNormalToBoundary1
from prodml22.pore_volume_measured import PoreVolumeMeasured

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ClosedRectangleModel(BoundaryBaseModel):
    """Closed rectangle boundary model.

    Four faults bound the reservoir in a rectangular shape.
    """
    drainage_area_measured: Optional[DrainageAreaMeasured] = field(
        default=None,
        metadata={
            "name": "DrainageAreaMeasured",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pore_volume_measured: Optional[PoreVolumeMeasured] = field(
        default=None,
        metadata={
            "name": "PoreVolumeMeasured",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
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
    distance_to_boundary3: Optional[DistanceToBoundary3] = field(
        default=None,
        metadata={
            "name": "DistanceToBoundary3",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    distance_to_boundary4: Optional[DistanceToBoundary4] = field(
        default=None,
        metadata={
            "name": "DistanceToBoundary4",
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
    boundary2_type: Optional[Boundary2Type] = field(
        default=None,
        metadata={
            "name": "Boundary2Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    boundary3_type: Optional[Boundary3Type] = field(
        default=None,
        metadata={
            "name": "Boundary3Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    boundary4_type: Optional[Boundary4Type] = field(
        default=None,
        metadata={
            "name": "Boundary4Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.distance_fracture_to_bottom_boundary import DistanceFractureToBottomBoundary
from prodml22.fracture_conductivity import FractureConductivity
from prodml22.fracture_radius import FractureRadius
from prodml22.near_wellbore_base_model import NearWellboreBaseModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FracturedHorizontalFiniteConductivityModel(NearWellboreBaseModel):
    """Fracture model, with  horizontal fracture (sometimes called "pancake
    fracture") flow.

    Finite Conductivity Model.
    """
    fracture_conductivity: Optional[FractureConductivity] = field(
        default=None,
        metadata={
            "name": "FractureConductivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    fracture_radius: Optional[FractureRadius] = field(
        default=None,
        metadata={
            "name": "FractureRadius",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    distance_fracture_to_bottom_boundary: Optional[DistanceFractureToBottomBoundary] = field(
        default=None,
        metadata={
            "name": "DistanceFractureToBottomBoundary",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

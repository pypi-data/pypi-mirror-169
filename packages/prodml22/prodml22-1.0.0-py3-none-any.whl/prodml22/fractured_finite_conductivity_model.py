from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.distance_mid_fracture_height_to_bottom_boundary import DistanceMidFractureHeightToBottomBoundary
from prodml22.fracture_conductivity import FractureConductivity
from prodml22.fracture_face_skin import FractureFaceSkin
from prodml22.fracture_half_length import FractureHalfLength
from prodml22.fracture_height import FractureHeight
from prodml22.near_wellbore_base_model import NearWellboreBaseModel
from prodml22.orientation_of_fracture_plane import OrientationOfFracturePlane
from prodml22.skin_layer2_relative_to_total_thickness import SkinLayer2RelativeToTotalThickness

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FracturedFiniteConductivityModel(NearWellboreBaseModel):
    """Fracture model, with vertical fracture flow.

    Finite Conductivity Model.
    """
    skin_layer2_relative_to_total_thickness: Optional[SkinLayer2RelativeToTotalThickness] = field(
        default=None,
        metadata={
            "name": "SkinLayer2RelativeToTotalThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fracture_half_length: Optional[FractureHalfLength] = field(
        default=None,
        metadata={
            "name": "FractureHalfLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    fracture_face_skin: Optional[FractureFaceSkin] = field(
        default=None,
        metadata={
            "name": "FractureFaceSkin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    orientation_of_fracture_plane: Optional[OrientationOfFracturePlane] = field(
        default=None,
        metadata={
            "name": "OrientationOfFracturePlane",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fracture_conductivity: Optional[FractureConductivity] = field(
        default=None,
        metadata={
            "name": "FractureConductivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    distance_mid_fracture_height_to_bottom_boundary: Optional[DistanceMidFractureHeightToBottomBoundary] = field(
        default=None,
        metadata={
            "name": "DistanceMidFractureHeightToBottomBoundary",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fracture_height: Optional[FractureHeight] = field(
        default=None,
        metadata={
            "name": "FractureHeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )

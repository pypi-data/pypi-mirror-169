from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.convergence_skin_relative_to_total_thickness import ConvergenceSkinRelativeToTotalThickness
from prodml22.distance_mid_fracture_height_to_bottom_boundary import DistanceMidFractureHeightToBottomBoundary
from prodml22.distance_wellbore_to_bottom_boundary import DistanceWellboreToBottomBoundary
from prodml22.fracture_angle_to_wellbore import FractureAngleToWellbore
from prodml22.fracture_conductivity import FractureConductivity
from prodml22.fracture_face_skin import FractureFaceSkin
from prodml22.fracture_half_length import FractureHalfLength
from prodml22.fracture_height import FractureHeight
from prodml22.fracture_model_type import FractureModelType
from prodml22.fracture_storativity_ratio import FractureStorativityRatio
from prodml22.length_horizontal_wellbore_flowing import LengthHorizontalWellboreFlowing
from prodml22.mechanical_skin_relative_to_total_thickness import MechanicalSkinRelativeToTotalThickness
from prodml22.near_wellbore_base_model import NearWellboreBaseModel
from prodml22.number_of_fractures import NumberOfFractures
from prodml22.orientation_well_trajectory import OrientationWellTrajectory

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class HorizontalWellboreMultipleEqualFracturedModel(NearWellboreBaseModel):
    """
    Horizontal wellbore model with wellbore positioned at arbitary distance
    from lower surface of reservoir layer, containing a number "n" of equally
    spaced identical vertical fractures.
    """
    convergence_skin_relative_to_total_thickness: Optional[ConvergenceSkinRelativeToTotalThickness] = field(
        default=None,
        metadata={
            "name": "ConvergenceSkinRelativeToTotalThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mechanical_skin_relative_to_total_thickness: Optional[MechanicalSkinRelativeToTotalThickness] = field(
        default=None,
        metadata={
            "name": "MechanicalSkinRelativeToTotalThickness",
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
    fracture_conductivity: Optional[FractureConductivity] = field(
        default=None,
        metadata={
            "name": "FractureConductivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    orientation_well_trajectory: Optional[OrientationWellTrajectory] = field(
        default=None,
        metadata={
            "name": "OrientationWellTrajectory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    length_horizontal_wellbore_flowing: Optional[LengthHorizontalWellboreFlowing] = field(
        default=None,
        metadata={
            "name": "LengthHorizontalWellboreFlowing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    distance_wellbore_to_bottom_boundary: Optional[DistanceWellboreToBottomBoundary] = field(
        default=None,
        metadata={
            "name": "DistanceWellboreToBottomBoundary",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
    number_of_fractures: Optional[NumberOfFractures] = field(
        default=None,
        metadata={
            "name": "NumberOfFractures",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
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
    fracture_angle_to_wellbore: Optional[FractureAngleToWellbore] = field(
        default=None,
        metadata={
            "name": "FractureAngleToWellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    fracture_storativity_ratio: Optional[FractureStorativityRatio] = field(
        default=None,
        metadata={
            "name": "FractureStorativityRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fracture_model_type: Optional[FractureModelType] = field(
        default=None,
        metadata={
            "name": "FractureModelType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

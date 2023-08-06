from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.convergence_skin_relative_to_total_thickness import ConvergenceSkinRelativeToTotalThickness
from prodml22.distance_wellbore_to_bottom_boundary import DistanceWellboreToBottomBoundary
from prodml22.length_horizontal_wellbore_flowing import LengthHorizontalWellboreFlowing
from prodml22.mechanical_skin_relative_to_total_thickness import MechanicalSkinRelativeToTotalThickness
from prodml22.near_wellbore_base_model import NearWellboreBaseModel
from prodml22.orientation_well_trajectory import OrientationWellTrajectory

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class HorizontalWellboreModel(NearWellboreBaseModel):
    """
    Horizontal wellbore model with wellbore positioned at arbitary distance
    from lower surface of reservoir layer.
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
            "required": True,
        }
    )

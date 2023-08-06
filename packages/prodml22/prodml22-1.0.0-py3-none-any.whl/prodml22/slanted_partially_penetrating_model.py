from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.convergence_skin_relative_to_total_thickness import ConvergenceSkinRelativeToTotalThickness
from prodml22.distance_mid_perforations_to_bottom_boundary import DistanceMidPerforationsToBottomBoundary
from prodml22.mechanical_skin_relative_to_total_thickness import MechanicalSkinRelativeToTotalThickness
from prodml22.near_wellbore_base_model import NearWellboreBaseModel
from prodml22.orientation_well_trajectory import OrientationWellTrajectory
from prodml22.perforated_length import PerforatedLength
from prodml22.skin_layer2_relative_to_total_thickness import SkinLayer2RelativeToTotalThickness
from prodml22.wellbore_deviation_angle import WellboreDeviationAngle

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SlantedPartiallyPenetratingModel(NearWellboreBaseModel):
    """
    Slanted wellbore model, with flowing length of wellbore less than total
    thickness of reservoir layer (as measured along wellbore).
    """
    wellbore_deviation_angle: Optional[WellboreDeviationAngle] = field(
        default=None,
        metadata={
            "name": "WellboreDeviationAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    skin_layer2_relative_to_total_thickness: Optional[SkinLayer2RelativeToTotalThickness] = field(
        default=None,
        metadata={
            "name": "SkinLayer2RelativeToTotalThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
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
    perforated_length: Optional[PerforatedLength] = field(
        default=None,
        metadata={
            "name": "PerforatedLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    distance_mid_perforations_to_bottom_boundary: Optional[DistanceMidPerforationsToBottomBoundary] = field(
        default=None,
        metadata={
            "name": "DistanceMidPerforationsToBottomBoundary",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
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

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.distance_to_mobility_interface import DistanceToMobilityInterface
from prodml22.orientation_of_linear_front import OrientationOfLinearFront
from prodml22.region2_thickness import Region2Thickness
from prodml22.reservoir_base_model import ReservoirBaseModel
from prodml22.transmissibility_reduction_factor_of_linear_front import TransmissibilityReductionFactorOfLinearFront

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class LinearCompositeWithChangingThicknessAcrossLeakyFaultModel(ReservoirBaseModel):
    """Linear Composite reservoir model in which the producing wellbore is in a
    homogeneous reservoir, infinite in all directions except one where the
    reservoir and/or fluid characteristics change across a linear front.

    On the farther side of the interface the reservoir is homogeneous
    and infinite but with a different mobility and/or storativity and
    thickness.  There is a fault or barrier at the interface between the
    two zones, but this is "leaky", allowing flow across it.
    """
    distance_to_mobility_interface: Optional[DistanceToMobilityInterface] = field(
        default=None,
        metadata={
            "name": "DistanceToMobilityInterface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    orientation_of_linear_front: Optional[OrientationOfLinearFront] = field(
        default=None,
        metadata={
            "name": "OrientationOfLinearFront",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    transmissibility_reduction_factor_of_linear_front: Optional[TransmissibilityReductionFactorOfLinearFront] = field(
        default=None,
        metadata={
            "name": "TransmissibilityReductionFactorOfLinearFront",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    region2_thickness: Optional[Region2Thickness] = field(
        default=None,
        metadata={
            "name": "Region2Thickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.distance_to_mobility_interface import DistanceToMobilityInterface
from prodml22.inner_to_outer_zone_diffusivity_ratio import InnerToOuterZoneDiffusivityRatio
from prodml22.inner_to_outer_zone_mobility_ratio import InnerToOuterZoneMobilityRatio
from prodml22.reservoir_base_model import ReservoirBaseModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class RadialCompositeModel(ReservoirBaseModel):
    """Radial Composite reservoir model, in which the wellbore is at the center
    of a circular homogeneous zone, communicating with an infinite homogeneous
    reservoir.

    The inner and outer zones have different reservoir and/or fluid
    characteristics. There is no pressure loss at the interface between
    the two zones.
    """
    inner_to_outer_zone_mobility_ratio: Optional[InnerToOuterZoneMobilityRatio] = field(
        default=None,
        metadata={
            "name": "InnerToOuterZoneMobilityRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    inner_to_outer_zone_diffusivity_ratio: Optional[InnerToOuterZoneDiffusivityRatio] = field(
        default=None,
        metadata={
            "name": "InnerToOuterZoneDiffusivityRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    distance_to_mobility_interface: Optional[DistanceToMobilityInterface] = field(
        default=None,
        metadata={
            "name": "DistanceToMobilityInterface",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

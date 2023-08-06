from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_model_section import AbstractModelSection
from prodml22.pore_volume_of_investigation import PoreVolumeOfInvestigation
from prodml22.radius_of_investigation import RadiusOfInvestigation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class BoundaryBaseModel(AbstractModelSection):
    """
    Abstract boundary model from which the other types are derived.
    """
    radius_of_investigation: Optional[RadiusOfInvestigation] = field(
        default=None,
        metadata={
            "name": "RadiusOfInvestigation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pore_volume_of_investigation: Optional[PoreVolumeOfInvestigation] = field(
        default=None,
        metadata={
            "name": "PoreVolumeOfInvestigation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )

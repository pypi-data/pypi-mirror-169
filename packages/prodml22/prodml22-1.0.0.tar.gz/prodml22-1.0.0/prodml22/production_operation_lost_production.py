from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.lost_volume_and_reason import LostVolumeAndReason
from prodml22.production_operation_third_party_processing import ProductionOperationThirdPartyProcessing

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationLostProduction:
    """
    Lost Production Schema.
    """
    volume_and_reason: List[LostVolumeAndReason] = field(
        default_factory=list,
        metadata={
            "name": "VolumeAndReason",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    third_party_processing: List[ProductionOperationThirdPartyProcessing] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProcessing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.volume_per_time_uom_with_legacy import VolumePerTimeUomWithLegacy

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerTimeMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumePerTimeUomWithLegacy] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

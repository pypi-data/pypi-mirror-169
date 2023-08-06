from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.volume_per_time_length_uom import VolumePerTimeLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerTimeLengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumePerTimeLengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

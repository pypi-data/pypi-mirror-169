from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.legacy_volume_per_time_uom import LegacyVolumePerTimeUom
from prodml22.volume_per_time_uom import VolumePerTimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerTimeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[VolumePerTimeUom, str, LegacyVolumePerTimeUom]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )

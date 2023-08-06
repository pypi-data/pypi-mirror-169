from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.legacy_volume_per_volume_uom import LegacyVolumePerVolumeUom
from prodml22.volume_per_volume_uom import VolumePerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumePerVolumeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[VolumePerVolumeUom, str, LegacyVolumePerVolumeUom]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.legacy_volume_uom import LegacyVolumeUom
from prodml22.volume_uom import VolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[VolumeUom, str, LegacyVolumeUom]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )

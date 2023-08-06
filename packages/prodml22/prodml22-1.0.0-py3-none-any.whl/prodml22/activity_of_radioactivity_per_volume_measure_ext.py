from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.activity_of_radioactivity_per_volume_uom import ActivityOfRadioactivityPerVolumeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ActivityOfRadioactivityPerVolumeMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ActivityOfRadioactivityPerVolumeUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".*:.*",
        }
    )

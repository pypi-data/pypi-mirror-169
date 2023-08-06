from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.activity_of_radioactivity_uom import ActivityOfRadioactivityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ActivityOfRadioactivityMeasureExt:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ActivityOfRadioactivityUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.time_per_length_uom import TimePerLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class TimePerLengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[TimePerLengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

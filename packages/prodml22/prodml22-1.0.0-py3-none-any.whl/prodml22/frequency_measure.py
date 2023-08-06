from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.frequency_uom import FrequencyUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FrequencyMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[FrequencyUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

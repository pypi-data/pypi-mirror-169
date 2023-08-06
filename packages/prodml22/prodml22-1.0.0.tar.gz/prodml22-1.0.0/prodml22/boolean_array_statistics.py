from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class BooleanArrayStatistics:
    mode_percentage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ModePercentage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    values_mode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ValuesMode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )

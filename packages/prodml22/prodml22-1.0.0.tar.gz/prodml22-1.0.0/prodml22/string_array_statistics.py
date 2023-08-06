from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class StringArrayStatistics:
    mode_percentage: Optional[float] = field(
        default=None,
        metadata={
            "name": "ModePercentage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    values_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValuesMode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )

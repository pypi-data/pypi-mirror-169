from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.abstract_floating_point_array import AbstractFloatingPointArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class FloatingPointXmlArray(AbstractFloatingPointArray):
    count_per_value: int = field(
        default=1,
        metadata={
            "name": "CountPerValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    values: List[float] = field(
        default_factory=list,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "tokens": True,
        }
    )

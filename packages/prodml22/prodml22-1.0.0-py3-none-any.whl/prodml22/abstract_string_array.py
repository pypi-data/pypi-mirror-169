from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.abstract_value_array import AbstractValueArray
from prodml22.string_array_statistics import StringArrayStatistics

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractStringArray(AbstractValueArray):
    statistics: List[StringArrayStatistics] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.abstract_numeric_array import AbstractNumericArray
from prodml22.integer_array_statistics import IntegerArrayStatistics

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractIntegerArray(AbstractNumericArray):
    """Generic representation of an array of integer values.

    Each derived element provides specialized implementation to allow
    specific optimization of the representation.
    """
    statistics: List[IntegerArrayStatistics] = field(
        default_factory=list,
        metadata={
            "name": "Statistics",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )

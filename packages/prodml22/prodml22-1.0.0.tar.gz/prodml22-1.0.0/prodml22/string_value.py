from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_value import AbstractValue
from prodml22.time_series_string_sample import TimeSeriesStringSample

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class StringValue(AbstractValue):
    """
    A single string value in the time series.

    :ivar string_value: A single string value in the time series.
    """
    string_value: Optional[TimeSeriesStringSample] = field(
        default=None,
        metadata={
            "name": "StringValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

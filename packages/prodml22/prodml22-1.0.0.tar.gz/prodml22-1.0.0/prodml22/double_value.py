from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_value import AbstractValue
from prodml22.time_series_double_sample import TimeSeriesDoubleSample

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DoubleValue(AbstractValue):
    """
    A single double value in the time series.

    :ivar double_value: A single double value in the time series.
    """
    double_value: Optional[TimeSeriesDoubleSample] = field(
        default=None,
        metadata={
            "name": "DoubleValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.value_status import ValueStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class TimeSeriesDoubleSample:
    """
    A single double value in a time series.

    :ivar value:
    :ivar d_tim: The date and time at which the value applies. If no
        time is specified then the value is static and only one sample
        can be defined. Either dTim or value or both must be specified.
        If the status attribute is absent and the value is not "NaN",
        the data value can be assumed to be good with no restrictions.
    :ivar status: An indicator of the quality of the value.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    d_tim: Optional[str] = field(
        default=None,
        metadata={
            "name": "dTim",
            "type": "Attribute",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    status: Optional[ValueStatus] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

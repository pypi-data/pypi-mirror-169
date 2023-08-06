from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.endpoint_quantity import EndpointQuantity
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class TimeSeriesThreshold:
    """
    Defines a value threshold window and the cumulative time duration that the
    data was within that window.

    :ivar threshold_minimum: The lower bound of the threshold for
        testing whether values are within a specific range.The element
        "unit" defines the unit of measure of this value. At least one
        of minimumValue and maximumValue must be specified. The
        thresholdMinimum must be less than thresholdMaximum. If
        thresholdMinimum is not specified then the minimum shall be
        assumed to be minus infinity.
    :ivar threshold_maximum: The upper bound of the threshold for
        testing whether values are within a specific range. Element
        "unit" defines the unit of measure of this value. At least one
        of minimumValue and maximumValue must be specified. The
        thresholdMaximum must be greater than thresholdMinimum. If
        thresholdMaximum is not specified then the maximum shall be
        assumed to be plus infinity.
    :ivar duration: The sum of the time intervals over the range of
        dTimMin to dTimMax during which the values were within the
        specified threshold range.
    """
    threshold_minimum: Optional[EndpointQuantity] = field(
        default=None,
        metadata={
            "name": "ThresholdMinimum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    threshold_maximum: Optional[EndpointQuantity] = field(
        default=None,
        metadata={
            "name": "ThresholdMaximum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.time_series_point_representation import TimeSeriesPointRepresentation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractFlowTestData:
    """
    The abstract class of flow test data from which all flow data components
    inherit.

    :ivar channel_set: A grouping of channels with a compatible index,
        for some purpose. Each channel has its own index. A ‘compatible’
        index simply means that all of the channels are either in time
        or in depth using a common datum.
    :ivar time_channel: The Channel containing the Time data.
    :ivar time_series_point_representation: .The representation of the
        points in the time series data: Point By Point meaning
        instantaneous measurements, or Stepwise Value At End Of Period
        meaning that the value reported has applied from the previous
        point up to the time reported.
    :ivar remark: Textual description about the value of this field.
    :ivar uid: The unique identifier of this Flow Test Data.
    """
    channel_set: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChannelSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    time_channel: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TimeChannel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    time_series_point_representation: Optional[TimeSeriesPointRepresentation] = field(
        default=None,
        metadata={
            "name": "TimeSeriesPointRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )

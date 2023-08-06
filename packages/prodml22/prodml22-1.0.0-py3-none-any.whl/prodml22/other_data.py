from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_flow_test_data import AbstractFlowTestData
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OtherData(AbstractFlowTestData):
    """
    Other flow data measurements.

    :ivar data_channel: The Channel containing the Data.
    """
    data_channel: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DataChannel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

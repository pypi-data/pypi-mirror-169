from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.flow_test_activity import FlowTestActivity
from prodml22.flow_test_measurement_set import FlowTestMeasurementSet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class VerticalInterferenceTest(FlowTestActivity):
    """
    Performed on multiple intervals in the same wellbore, where one interval is
    flowing and one or more intervals are observing the interfering pressure.

    :ivar tie_in_log: References a log containing a wireline formation
        test  tie-in (e.g. gamma ray curve) vs. depth data.
    :ivar interval_measurement_set:
    """
    tie_in_log: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TieInLog",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    interval_measurement_set: List[FlowTestMeasurementSet] = field(
        default_factory=list,
        metadata={
            "name": "IntervalMeasurementSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )

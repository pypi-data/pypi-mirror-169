from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.flow_test_activity import FlowTestActivity
from prodml22.flow_test_measurement_set import FlowTestMeasurementSet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InterwellTest(FlowTestActivity):
    """
    Performed on multiple  wellbores, where an interval in one wellbore is
    flowing and one or more intervals in other wellbores are observing the
    interfering pressure.
    """
    interval_measurement_set: List[FlowTestMeasurementSet] = field(
        default_factory=list,
        metadata={
            "name": "IntervalMeasurementSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )

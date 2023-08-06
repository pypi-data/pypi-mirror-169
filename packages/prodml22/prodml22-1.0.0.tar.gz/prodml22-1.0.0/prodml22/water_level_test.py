from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.flow_test_activity import FlowTestActivity
from prodml22.flow_test_measurement_set import FlowTestMeasurementSet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WaterLevelTest(FlowTestActivity):
    """The test to monitor the water level, sometimes required for regulatory
    purpose.

    For example, see TxRRC H-15.
    """
    interval_measurement_set: Optional[FlowTestMeasurementSet] = field(
        default=None,
        metadata={
            "name": "IntervalMeasurementSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

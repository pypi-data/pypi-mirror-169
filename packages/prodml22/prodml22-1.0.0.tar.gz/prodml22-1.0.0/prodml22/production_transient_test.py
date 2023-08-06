from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.flow_test_activity import FlowTestActivity
from prodml22.flow_test_measurement_set import FlowTestMeasurementSet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionTransientTest(FlowTestActivity):
    """
    Typically performed using the well's permanent production string,  one
    interval at a time.
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

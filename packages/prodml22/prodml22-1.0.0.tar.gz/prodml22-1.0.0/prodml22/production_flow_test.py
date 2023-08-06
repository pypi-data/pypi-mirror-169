from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.flow_test_activity import FlowTestActivity
from prodml22.flow_test_measurement_set import FlowTestMeasurementSet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionFlowTest(FlowTestActivity):
    """Regularly  performed using the well's permanent production string,  as a
    steady-state test to assess long-term well performance and as an input to
    production allocation.

    This is NOT expected to be a transient test.

    :ivar validated: A flag which is to be set if this test is validated
        and therefore able to used in processes such as production
        allocation.
    :ivar well_test_method: Description or name of the method used to
        conduct the well test.
    :ivar effective_date: The date and time from which this well test is
        used in production allocation processes as representative of the
        well’s performance
    :ivar interval_measurement_set:
    """
    validated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Validated",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    well_test_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellTestMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    effective_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    interval_measurement_set: Optional[FlowTestMeasurementSet] = field(
        default=None,
        metadata={
            "name": "IntervalMeasurementSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

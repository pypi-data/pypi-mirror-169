from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.flow_test_activity import FlowTestActivity
from prodml22.flow_test_measurement_set import FlowTestMeasurementSet

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FormationTesterStation(FlowTestActivity):
    """Performed using formation tester tools conveyed on wireline, one
    interval at a time.

    A normal job would consist of multiple interval tests, each is
    represented by its own Flow Test Activity, which are collected in
    the Flow Test Job.

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
    interval_measurement_set: Optional[FlowTestMeasurementSet] = field(
        default=None,
        metadata={
            "name": "IntervalMeasurementSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

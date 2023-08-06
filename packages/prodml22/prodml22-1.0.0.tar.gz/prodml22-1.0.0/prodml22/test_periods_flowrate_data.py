from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.abstract_rate_history import AbstractRateHistory

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class TestPeriodsFlowrateData(AbstractRateHistory):
    """
    :ivar test_period_ref: Choice available for rate history where the
        test period(s) used to form the rate history are referenced (by
        uid).
    """
    test_period_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TestPeriodRef",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
            "max_length": 64,
        }
    )

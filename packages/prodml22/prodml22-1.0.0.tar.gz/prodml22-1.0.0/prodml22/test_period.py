from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.product_rate import ProductRate
from prodml22.test_period_kind import TestPeriodKind
from prodml22.well_flowing_condition import WellFlowingCondition

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class TestPeriod:
    """
    Test conditions for a production well test.

    :ivar start_time: The date and time when the test  began.
    :ivar end_time: The date and time when the test  began.
    :ivar test_period_kind: The duration of the test.
    :ivar well_flowing_condition: The duration of the test.
    :ivar remark: Remarks and comments about this data item.
    :ivar product_rate: The production rate of the product.
    :ivar uid: Unique identifier for this instance of the object.
    """
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    test_period_kind: Optional[TestPeriodKind] = field(
        default=None,
        metadata={
            "name": "TestPeriodKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    well_flowing_condition: Optional[WellFlowingCondition] = field(
        default=None,
        metadata={
            "name": "WellFlowingCondition",
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
    product_rate: List[ProductRate] = field(
        default_factory=list,
        metadata={
            "name": "ProductRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )

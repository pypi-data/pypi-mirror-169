from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.abstract_simple_product_volume import AbstractSimpleProductVolume
from prodml22.data_object_reference import DataObjectReference
from prodml22.reporting_duration_kind import ReportingDurationKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionWellTests(AbstractSimpleProductVolume):
    """
    This is the collection of ProductionWellTests.

    :ivar nominal_period_kind: Validate.
    :ivar start_date: Description or name of the method used to conduct
        the well test.
    :ivar end_date: Validate.
    :ivar flow_test_activity: BUSINESS RULE: In this usage, this link is
        expected to be a  type of  Production Flow Test or Injection
        Flow Test. The Production Flow Test has  validation and
        effective date for allocation purposes. Flow Test Location is
        expected to be a Reporting Entity (same as a volume, etc) in
        standard SPVR usage
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    nominal_period_kind: Optional[Union[ReportingDurationKind, str]] = field(
        default=None,
        metadata={
            "name": "NominalPeriodKind",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    flow_test_activity: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "FlowTestActivity",
            "type": "Element",
            "min_occurs": 1,
        }
    )

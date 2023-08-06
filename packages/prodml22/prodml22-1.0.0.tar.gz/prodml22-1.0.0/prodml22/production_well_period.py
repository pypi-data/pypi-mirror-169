from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.product_rate import ProductRate
from prodml22.time_measure import TimeMeasure
from prodml22.well_flowing_condition import WellFlowingCondition
from prodml22.well_status import WellStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionWellPeriod:
    """
    Period during which the well choke did not vary.

    :ivar start_time: The start time at a given choke setting.
    :ivar duration: The duration at the given choke setting.
    :ivar well_status: The status of the well.
    :ivar well_flowing_condition: The status of the well.
    :ivar remark: A descriptive remark relating to any significant
        events during this period.
    :ivar reporting_entity:
    :ivar product_rate: The production rate of the product.
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
    duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    well_status: Optional[WellStatus] = field(
        default=None,
        metadata={
            "name": "WellStatus",
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
    reporting_entity: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReportingEntity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    product_rate: List[ProductRate] = field(
        default_factory=list,
        metadata={
            "name": "ProductRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate
from prodml22.abstract_simple_product_volume import AbstractSimpleProductVolume
from prodml22.production_well_period import ProductionWellPeriod
from prodml22.reporting_duration_kind import ReportingDurationKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WellProductionParameters(AbstractSimpleProductVolume):
    """
    Captures well production parameters associated with a well reporting
    entity.

    :ivar start_date: The starting date of the reporting period.
    :ivar end_date: The ending date of the reporting period.
    :ivar nominal_period: Name or identifier for the reporting period to
        which the well production parameters apply.
    :ivar production_period: Details of production at a specific choke
        setting.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
        }
    )
    nominal_period: Optional[Union[ReportingDurationKind, str]] = field(
        default=None,
        metadata={
            "name": "NominalPeriod",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    production_period: List[ProductionWellPeriod] = field(
        default_factory=list,
        metadata={
            "name": "ProductionPeriod",
            "type": "Element",
            "min_occurs": 1,
        }
    )

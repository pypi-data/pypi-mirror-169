from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_date_time_class import AbstractDateTimeType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class StartEndDate(AbstractDateTimeType):
    """
    The start and end date for a reporting period.

    :ivar date_start: The beginning date that the period represents.
    :ivar date_end: The ending date that the period represents.
    """
    date_start: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    date_end: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )

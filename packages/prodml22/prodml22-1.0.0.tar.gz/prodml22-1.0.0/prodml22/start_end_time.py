from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_date_time_class import AbstractDateTimeType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class StartEndTime(AbstractDateTimeType):
    """
    Start and end time of a reporting period.

    :ivar dtim_start: The beginning date and time that the period
        represents.
    :ivar dtim_end: The ending date and time that the period represents.
    """
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )

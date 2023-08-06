from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractDateTimeType:
    """A reporting period that is different from the overall report period.

    For example, a particular day within a monthly report. This period
    must conform to the kind of interval. If one value from a pair are
    given, then both values must be given.

    :ivar dtime: DTime.
    :ivar date: Date.
    :ivar month: Month.
    """
    class Meta:
        name = "AbstractDateTimeClass"

    dtime: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    month: Optional[str] = field(
        default=None,
        metadata={
            "name": "Month",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
            "pattern": r"([1-9][0-9][0-9][0-9])-(([0][0-9])|([1][0-2]))",
        }
    )

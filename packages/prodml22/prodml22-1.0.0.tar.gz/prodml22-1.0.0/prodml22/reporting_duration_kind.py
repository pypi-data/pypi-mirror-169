from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ReportingDurationKind(Enum):
    """
    Specifies the time periods for a report.
    """
    DAY = "day"
    LIFE_TO_DATE = "life to date"
    MONTH = "month"
    MONTH_TO_DATE = "month to date"
    TOTAL_CUMULATIVE = "total cumulative"
    WEEK = "week"
    YEAR = "year"
    YEAR_TO_DATE = "year to date"

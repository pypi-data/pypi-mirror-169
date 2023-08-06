from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ReportVersionStatus(Enum):
    """
    Specifies the statuses of a version of a report.

    :cvar FINAL: Final, the report is approved.
    :cvar PRELIMINARY: Preliminary, the report has not yet been
        approved.
    """
    FINAL = "final"
    PRELIMINARY = "preliminary"

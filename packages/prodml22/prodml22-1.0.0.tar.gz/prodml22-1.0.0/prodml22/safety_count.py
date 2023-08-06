from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.reporting_duration_kind import ReportingDurationKind
from prodml22.safety_type import SafetyType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SafetyCount:
    """
    A zero-based count of a type of safety item.

    :ivar value:
    :ivar type: The type of safety issue for which a count is being
        defined.
    :ivar period: The type of period being reported by this count.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 1,
        }
    )
    type: Optional[SafetyType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    period: Optional[ReportingDurationKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

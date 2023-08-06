from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.dated_comment import DatedComment
from prodml22.safety_count import SafetyCount
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationSafety:
    """
    Safety Information Schema.

    :ivar meantime_incident: The mean time between safety incidents.
    :ivar safety_count: A zero-based count of a type of safety item.
    :ivar comment: Safety related comment.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    meantime_incident: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "MeantimeIncident",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    safety_count: List[SafetyCount] = field(
        default_factory=list,
        metadata={
            "name": "SafetyCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    comment: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )

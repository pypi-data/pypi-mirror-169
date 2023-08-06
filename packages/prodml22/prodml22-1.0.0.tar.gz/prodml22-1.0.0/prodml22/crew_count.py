from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.crew_type import CrewType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CrewCount:
    """
    A one-based count of personnel on a type of crew.

    :ivar value:
    :ivar type: The type of crew for which a count is being defined.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 0,
        }
    )
    type: Optional[CrewType] = field(
        default=None,
        metadata={
            "type": "Attribute",
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

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_growing_object_part import AbstractGrowingObjectPart

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractTimeGrowingPart(AbstractGrowingObjectPart):
    """
    :ivar time: STORE MANAGED. This is populated by a store on read.
        Customer provided values are ignored on write
    """
    time: Optional[str] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_active_object import AbstractActiveObject
from prodml22.growing_object_index import GrowingObjectIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractGrowingObject(AbstractActiveObject):
    """
    :ivar index: Information about the growing object's index.
    """
    index: Optional[GrowingObjectIndex] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

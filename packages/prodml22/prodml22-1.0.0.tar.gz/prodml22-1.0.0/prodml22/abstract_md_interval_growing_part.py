from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_growing_object_part import AbstractGrowingObjectPart
from prodml22.md_interval import MdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractMdIntervalGrowingPart(AbstractGrowingObjectPart):
    """
    :ivar md_interval: The measured depth interval which contains this
        object growing part. STORE MANAGED. This is populated by a store
        on read. Customer provided values are ignored on write
    """
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

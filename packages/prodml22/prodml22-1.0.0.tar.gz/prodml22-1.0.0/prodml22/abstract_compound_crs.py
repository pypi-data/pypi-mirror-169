from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractCompoundCrs(AbstractObject):
    vertical_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "VerticalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

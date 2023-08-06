from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Vector:
    component1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Component1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    component2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Component2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    component3: Optional[float] = field(
        default=None,
        metadata={
            "name": "Component3",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

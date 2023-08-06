from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.apigravity_uom import ApigravityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ApigravityMeasure:
    class Meta:
        name = "APIGravityMeasure"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ApigravityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

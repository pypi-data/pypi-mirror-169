from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.apigravity_uom import ApigravityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ApigravityMeasureExt:
    class Meta:
        name = "APIGravityMeasureExt"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ApigravityUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )

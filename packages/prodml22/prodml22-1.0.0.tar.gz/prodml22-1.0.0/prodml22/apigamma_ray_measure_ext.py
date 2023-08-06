from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.apigamma_ray_uom import ApigammaRayUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ApigammaRayMeasureExt:
    class Meta:
        name = "APIGammaRayMeasureExt"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[Union[ApigammaRayUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )

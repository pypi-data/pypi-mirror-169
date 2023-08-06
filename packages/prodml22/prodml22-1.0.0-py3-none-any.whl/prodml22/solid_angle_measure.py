from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.solid_angle_uom import SolidAngleUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class SolidAngleMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[SolidAngleUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

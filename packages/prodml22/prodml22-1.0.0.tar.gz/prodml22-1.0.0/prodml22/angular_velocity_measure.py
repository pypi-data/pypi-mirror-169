from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.angular_velocity_uom import AngularVelocityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AngularVelocityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[AngularVelocityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

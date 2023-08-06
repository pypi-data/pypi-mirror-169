from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.power_uom import PowerUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PowerMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PowerUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.electric_current_uom import ElectricCurrentUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectricCurrentMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ElectricCurrentUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

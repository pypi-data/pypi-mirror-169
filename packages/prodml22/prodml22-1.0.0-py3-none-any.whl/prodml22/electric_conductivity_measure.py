from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.electric_conductivity_uom import ElectricConductivityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ElectricConductivityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ElectricConductivityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

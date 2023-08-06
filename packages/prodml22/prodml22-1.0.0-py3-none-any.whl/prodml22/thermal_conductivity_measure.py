from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.thermal_conductivity_uom import ThermalConductivityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ThermalConductivityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ThermalConductivityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

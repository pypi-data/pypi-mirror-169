from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.thermal_conductance_uom import ThermalConductanceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ThermalConductanceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ThermalConductanceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

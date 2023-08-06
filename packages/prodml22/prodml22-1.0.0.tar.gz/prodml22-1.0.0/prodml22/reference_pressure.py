from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.pressure_uom import PressureUom
from prodml22.reference_pressure_kind import ReferencePressureKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReferencePressure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[PressureUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    reference_pressure_kind: Optional[ReferencePressureKind] = field(
        default=None,
        metadata={
            "name": "referencePressureKind",
            "type": "Attribute",
        }
    )

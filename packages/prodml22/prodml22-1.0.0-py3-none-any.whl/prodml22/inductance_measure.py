from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.inductance_uom import InductanceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class InductanceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[InductanceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

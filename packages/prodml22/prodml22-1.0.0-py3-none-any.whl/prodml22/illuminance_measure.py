from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.illuminance_uom import IlluminanceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IlluminanceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[IlluminanceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.radiant_intensity_uom import RadiantIntensityUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class RadiantIntensityMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[RadiantIntensityUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

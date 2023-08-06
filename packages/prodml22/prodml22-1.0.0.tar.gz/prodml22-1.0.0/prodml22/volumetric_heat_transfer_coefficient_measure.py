from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.volumetric_heat_transfer_coefficient_uom import VolumetricHeatTransferCoefficientUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VolumetricHeatTransferCoefficientMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VolumetricHeatTransferCoefficientUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

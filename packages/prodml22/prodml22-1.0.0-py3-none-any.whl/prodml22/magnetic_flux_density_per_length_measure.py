from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.magnetic_flux_density_per_length_uom import MagneticFluxDensityPerLengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class MagneticFluxDensityPerLengthMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[MagneticFluxDensityPerLengthUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

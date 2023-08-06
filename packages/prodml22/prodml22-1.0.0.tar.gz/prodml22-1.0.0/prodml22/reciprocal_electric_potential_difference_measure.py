from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.reciprocal_electric_potential_difference_uom import ReciprocalElectricPotentialDifferenceUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReciprocalElectricPotentialDifferenceMeasure:
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[ReciprocalElectricPotentialDifferenceUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ConvergenceSkinRelativeToTotalThickness(AbstractParameter):
    """Dimensionless value, characterizing the restriction to flow (+ve value,
    convergence) or additional capacity for flow (-ve value, fractured or
    horizontal wellbore) owing to the geometry of the wellbore connection to
    reservoir.

    This value is stated with respect to radial flow using the full
    reservoir thickness (h), ie the radial flow or middle time region of
    a pressure transient. It therefore can be added to
    "MechancialSkinRelativeToTotalThickness" to yield the
    "SkinRelativeToTotalThickness".
    """
    abbreviation: str = field(
        init=False,
        default="Sconv",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    value: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

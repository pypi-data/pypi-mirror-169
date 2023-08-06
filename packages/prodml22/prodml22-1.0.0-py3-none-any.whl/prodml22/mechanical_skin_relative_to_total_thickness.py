from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class MechanicalSkinRelativeToTotalThickness(AbstractParameter):
    """Dimensionless value, characterizing the restriction to flow (+ve value,
    damage) or additional capacity for flow (-ve value, eg acidized) due to
    effective permeability around the wellbore.

    This value is stated with respect to radial flow using the full
    reservoir thickness (h), ie the radial flow or middle time region of
    a pressure transient. It therefore can be added to
    "ConvergenceSkinRelativeToTotalThickness" skin to yield
    "SkinRelativeToTotalThickness".
    """
    abbreviation: str = field(
        init=False,
        default="Smech",
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

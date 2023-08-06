from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SkinRelativeToTotalThickness(AbstractParameter):
    """Dimensionless value, characterizing the restriction to flow (+ve value)
    or extra capacity for flow (-ve value) into the wellbore.

    This value is stated with respect to radial flow using the full
    layer thickness (h), ie the "reservoir radial flow" or "middle time
    region" of a pressure transient. It comprises the sum of
    "MechanicalSkinRelativeToTotalThickness" and
    "ConvergenceSkinRelativeToTotalThickness" both of which also are
    expressed in terms of h.
    """
    abbreviation: str = field(
        init=False,
        default="S",
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

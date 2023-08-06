from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.dimensionless_measure import DimensionlessMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SkinLayer2RelativeToTotalThickness(AbstractParameter):
    """In a two-layer model with both layers flowing into the wellbore, the
    skin factor of the second layer.

    This value is stated with respect to radial flow using the full
    layer thickness (h), ie the "reservoir radial flow" or "middle time
    region" of a pressure transient.
    """
    abbreviation: str = field(
        init=False,
        default="S2",
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

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.permeability_length_measure_ext import PermeabilityLengthMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PermeabilityThicknessProduct(AbstractParameter):
    """The product of the radial permeability of the reservoir layer in the horizontal plane * the total thickness of the layer."""
    abbreviation: str = field(
        init=False,
        default="k.h",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    permeability_length: Optional[PermeabilityLengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "PermeabilityLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

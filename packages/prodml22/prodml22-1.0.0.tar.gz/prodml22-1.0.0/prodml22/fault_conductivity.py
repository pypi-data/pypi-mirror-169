from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.permeability_length_measure_ext import PermeabilityLengthMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FaultConductivity(AbstractParameter):
    """
    In a Linear Composite model where the boundary of the inner and outer zones
    is a leaky and conductive fault, the fault conductivity (ie along the face
    of the fault).
    """
    abbreviation: str = field(
        init=False,
        default="Fc",
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

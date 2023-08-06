from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class TransmissibilityReductionFactorOfLinearFront(AbstractParameter):
    """The transmissibility reduction factor of a fault in a Linear Composite
    model where the boundary of the inner and outer zones is a leaky fault.

    If T is the complete transmissibility which would be computed without any fault between point A and point B (T is a function of permeability, etc), then Tf = T * leakage. Therefore: leakage = 1 implies that the fault is not a barrier to flow at all, leakage = 0 implies that the fault is sealing (no transmissibility anymore at all between points A and B).
    """
    abbreviation: str = field(
        init=False,
        default="Leakage",
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

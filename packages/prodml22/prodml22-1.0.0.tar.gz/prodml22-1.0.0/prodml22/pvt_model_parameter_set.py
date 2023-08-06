from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.pvt_model_parameter import PvtModelParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PvtModelParameterSet:
    """
    A collection of parameters.
    """
    coefficient: List[PvtModelParameter] = field(
        default_factory=list,
        metadata={
            "name": "Coefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )

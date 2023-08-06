from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.binary_interaction_coefficient import BinaryInteractionCoefficient

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class BinaryInteractionCoefficientSet:
    """
    Binary interaction coefficient set.

    :ivar binary_interaction_coefficient: Binary interaction
        coefficient.
    """
    binary_interaction_coefficient: List[BinaryInteractionCoefficient] = field(
        default_factory=list,
        metadata={
            "name": "BinaryInteractionCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )

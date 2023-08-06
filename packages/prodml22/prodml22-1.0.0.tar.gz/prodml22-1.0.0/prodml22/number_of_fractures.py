from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class NumberOfFractures(AbstractParameter):
    """For a multiple fractured horizontal wellbore model, the number of
    fractures which originate from the wellbore.

    In a "HorizontalWellboreMultipleEqualFracturedModel" these fractures
    are identical and equally spaced, including one fracture at each end
    of the length represented by "LengthHorizontalWellboreFlowing".
    """
    abbreviation: str = field(
        init=False,
        default="Nf",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

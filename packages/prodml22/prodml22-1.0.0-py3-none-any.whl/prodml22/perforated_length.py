from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PerforatedLength(AbstractParameter):
    """
    For a partial penetration (a vertical or slant well with less than full
    layer thickness open to flow) or a hydraulically fractured model, the
    length of the perforated section of the wellbore.
    """
    abbreviation: str = field(
        init=False,
        default="hp",
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

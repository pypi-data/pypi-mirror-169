from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FractureHeight(AbstractParameter):
    """In any vertical hydraulic fracture model (including the cases where the
    wellbore can be vertical or horizontal), the height of the fractures.

    In the case of a vertical wellbore, the fractures are assumed to
    extend an equal distance above and below the mid perforations depth,
    given by the parameter "DistanceMidPerforationsToBottomBoundary". In
    the case of a horizontal wellbore, the fractures are assumed to
    extend an equal distance above and below the wellbore.
    """
    abbreviation: str = field(
        init=False,
        default="Hf",
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

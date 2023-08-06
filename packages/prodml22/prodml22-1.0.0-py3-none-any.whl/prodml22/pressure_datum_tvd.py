from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PressureDatumTvd(AbstractParameter):
    """The depth TVD of the datum at which reservoir pressures are reported for
    this layer.

    Note, this depth may not exist inside the layer at the Test Location
    but it is the reference depth to which pressures will be corrected.
    """
    class Meta:
        name = "PressureDatumTVD"

    abbreviation: str = field(
        init=False,
        default="datum",
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

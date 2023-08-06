from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FractureRadius(AbstractParameter):
    """
    For a horizontal ("pancake") induced hydraulic fracture, which is assumed
    to be circular in shape in the horizontal plane, the radius of the
    fracture.
    """
    abbreviation: str = field(
        init=False,
        default="Rf",
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    length: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

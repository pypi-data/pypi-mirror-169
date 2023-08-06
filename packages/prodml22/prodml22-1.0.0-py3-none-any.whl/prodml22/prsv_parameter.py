from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PrsvParameter:
    """
    PRSV parameter.

    :ivar a1: The parameter a1.
    :ivar a2: The parameter a2.
    :ivar b1: The parameter b1.
    :ivar b2: The parameter b2.
    :ivar c2: The parameter c2.
    :ivar fluid_component_reference: The fluid component to which this
        PRSV parameter set applies.
    """
    a1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    a2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    b1: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    b2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    c2: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    fluid_component_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fluidComponentReference",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )

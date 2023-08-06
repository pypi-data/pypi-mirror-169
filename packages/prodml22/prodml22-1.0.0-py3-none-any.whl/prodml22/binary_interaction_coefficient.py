from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class BinaryInteractionCoefficient:
    """
    Binary interaction coefficient.

    :ivar value:
    :ivar fluid_component1_reference: Reference to the first fluid
        component for this binary interaction coefficient.
    :ivar fluid_component2_reference: Reference to the second fluid
        component for this binary interaction coefficient.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    fluid_component1_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fluidComponent1Reference",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    fluid_component2_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fluidComponent2Reference",
            "type": "Attribute",
            "max_length": 64,
        }
    )

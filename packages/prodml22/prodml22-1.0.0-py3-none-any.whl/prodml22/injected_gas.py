from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.vapor_composition import VaporComposition

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InjectedGas:
    """The composition of a single injected gas used in the swelling test.

    This type of gas has a uid which is used to refer to this gas being
    injected, in each Swelling Test Step.

    :ivar vapor_composition: The composition of injected gas (vapor) for
        this test.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    vapor_composition: Optional[VaporComposition] = field(
        default=None,
        metadata={
            "name": "VaporComposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )

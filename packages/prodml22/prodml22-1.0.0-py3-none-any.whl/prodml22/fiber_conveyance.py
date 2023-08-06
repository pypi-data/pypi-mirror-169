from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_cable import AbstractCable

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberConveyance:
    """The means by which this fiber segment is conveyed into the well.

    Choices: permanent, intervention, or control line conveyance method.
    """
    cable: Optional[AbstractCable] = field(
        default=None,
        metadata={
            "name": "Cable",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

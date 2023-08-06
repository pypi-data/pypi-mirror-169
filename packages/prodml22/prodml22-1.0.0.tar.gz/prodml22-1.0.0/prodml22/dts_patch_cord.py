from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DtsPatchCord:
    """
    Information regarding the patch cord used to connect the instrument box to
    the start of the optical fiber path.

    :ivar fiber_length: Optical distance between the instrument and the
        end of the patch cord that will be attached to the rest of the
        optical path from which a measurement will be taken.
    :ivar description: A textual description of the patch cord.
    """
    fiber_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FiberLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 2000,
        }
    )

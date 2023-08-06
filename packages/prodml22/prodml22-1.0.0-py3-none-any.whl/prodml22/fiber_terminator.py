from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.fiber_common import FiberCommon
from prodml22.termination_kind import TerminationKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberTerminator(FiberCommon):
    """The terminator of the optical path.

    This may be a component (in the case of a single ended fiber
    installation), or it may be a connection back into the instrument
    box in the case of a double ended fiber installation.

    :ivar termination_type: Information about the termination used for
        the fiber.
    """
    termination_type: Optional[TerminationKind] = field(
        default=None,
        metadata={
            "name": "TerminationType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

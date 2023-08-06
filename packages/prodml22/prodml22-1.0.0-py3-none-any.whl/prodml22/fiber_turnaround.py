from __future__ import annotations
from dataclasses import dataclass
from prodml22.fiber_common import FiberCommon

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberTurnaround(FiberCommon):
    """
    A turnaround component within the optical path.
    """

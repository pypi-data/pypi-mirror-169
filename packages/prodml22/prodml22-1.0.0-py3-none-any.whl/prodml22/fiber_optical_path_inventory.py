from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fiber_connection import FiberConnection
from prodml22.fiber_optical_path_segment import FiberOpticalPathSegment
from prodml22.fiber_splice import FiberSplice
from prodml22.fiber_terminator import FiberTerminator
from prodml22.fiber_turnaround import FiberTurnaround

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberOpticalPathInventory:
    """The list of equipment used in the optical path.

    Equipment may be used in the optical path for different periods of
    time, so this inventory contains all items of equipment that are
    used at some period of time.

    :ivar splice: A splice component within the optical path.
    :ivar connection: A connection component within the optical path.
    :ivar turnaround: A turnaround component within the optical path.
    :ivar segment: A single segment of the optical fiber used for
        distributed temperature surveys. Multiple such segments may be
        connected by other types of component including connectors,
        splices and fiber turnarounds.
    :ivar terminator: The terminator of the optical path. This may be a
        component (in the case of a single ended fiber installation), or
        it may be a connection back into the instrument box in the case
        of a double ended fiber installation.
    """
    splice: List[FiberSplice] = field(
        default_factory=list,
        metadata={
            "name": "Splice",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    connection: List[FiberConnection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    turnaround: List[FiberTurnaround] = field(
        default_factory=list,
        metadata={
            "name": "Turnaround",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    segment: List[FiberOpticalPathSegment] = field(
        default_factory=list,
        metadata={
            "name": "Segment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
    terminator: Optional[FiberTerminator] = field(
        default=None,
        metadata={
            "name": "Terminator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.length_per_length_measure import LengthPerLengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class RelativeCoordinate:
    """
    Relative xyz location offset.

    :ivar x: Defines the relative from-left-to-right location on a
        display screen. The display origin (0,0) is the upper left-hand
        corner of the display as viewed by the user.
    :ivar y: Defines the relative from-top-to-bottom location on a
        display screen. The display origin (0,0) is the upper left-hand
        corner of the display as viewed by the user.
    :ivar z: Defines the relative from-front-to-back location in a 3D
        system. The unrotated display origin (0,0) is the upper left-
        hand corner of the display as viewed by the user. The "3D
        picture" may be rotated on the 2D display.
    """
    x: Optional[LengthPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    y: Optional[LengthPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    z: Optional[LengthPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )

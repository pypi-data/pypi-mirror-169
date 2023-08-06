from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.vertical_coordinate_uom import VerticalCoordinateUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class MeasuredDepthCoord:
    """A measured depth coordinate in a wellbore.

    Positive moving from the reference datum toward the bottomhole. All
    coordinates with the same datum (and same UOM) can be considered to
    be in the same coordinate reference system (CRS) and are thus
    directly comparable.

    :ivar value:
    :ivar uom: The unit of measure of the measured depth coordinate.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    uom: Optional[VerticalCoordinateUom] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

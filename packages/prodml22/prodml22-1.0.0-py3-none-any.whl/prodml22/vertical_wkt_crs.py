from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_vertical_crs import AbstractVerticalCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalWktCrs(AbstractVerticalCrs):
    """
    ISO 19162-compliant well-known text for the vertical CRS.

    :ivar well_known_text: ISO 19162 compliant well known text of the
        CRS
    """
    well_known_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellKnownText",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

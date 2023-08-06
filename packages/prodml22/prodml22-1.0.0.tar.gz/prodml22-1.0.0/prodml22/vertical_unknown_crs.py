from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_vertical_crs import AbstractVerticalCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalUnknownCrs(AbstractVerticalCrs):
    """This class is used in a case where the coordinate reference system is
    either unknown or is intentionally not being transferred.

    In this case, the uom and Direction need to be provided on the
    VerticalCrs class.
    """
    unknown: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unknown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )

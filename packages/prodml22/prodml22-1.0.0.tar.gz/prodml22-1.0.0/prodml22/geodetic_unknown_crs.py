from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_geographic2d_crs import AbstractGeographic2DCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeodeticUnknownCrs(AbstractGeographic2DCrs):
    """
    This class is used in a case where the coordinate reference system is
    either unknown or is intentionally not being transferred.
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

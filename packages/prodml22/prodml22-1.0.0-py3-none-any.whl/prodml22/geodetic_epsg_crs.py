from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_geographic2d_crs import AbstractGeographic2DCrs

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeodeticEpsgCrs(AbstractGeographic2DCrs):
    """
    This class contains the EPSG code for a geodetic CRS.
    """
    epsg_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "EpsgCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 1,
        }
    )

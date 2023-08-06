from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_projected_crs import AbstractProjectedCrs
from prodml22.axis_order2d import AxisOrder2D
from prodml22.cartesian2d_crs import Cartesian2DCrs
from prodml22.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ProjectedCrs(Cartesian2DCrs):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    axis_order: Optional[AxisOrder2D] = field(
        default=None,
        metadata={
            "name": "AxisOrder",
            "type": "Element",
            "required": True,
        }
    )
    abstract_projected_crs: Optional[AbstractProjectedCrs] = field(
        default=None,
        metadata={
            "name": "AbstractProjectedCrs",
            "type": "Element",
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".*:.*",
        }
    )

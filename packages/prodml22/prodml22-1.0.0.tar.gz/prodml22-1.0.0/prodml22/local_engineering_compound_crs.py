from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_compound_crs import AbstractCompoundCrs
from prodml22.data_object_reference import DataObjectReference
from prodml22.vector import Vector
from prodml22.vertical_axis import VerticalAxis

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class LocalEngineeringCompoundCrs(AbstractCompoundCrs):
    """
    A local Engineering compound CRS is based on a LocalEngineering2dCRS + a
    vertical CRS.

    :ivar origin_vertical_coordinate: Vertical coordinate of the origin
        of the local engineering CRS in the base vertical CRS
        (consequently in the uom of the base vertical CRS)
    :ivar vertical_axis:
    :ivar origin_uncertainty_vector_at_one_sigma:
    :ivar local_engineering2d_crs:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    origin_vertical_coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "OriginVerticalCoordinate",
            "type": "Element",
            "required": True,
        }
    )
    vertical_axis: Optional[VerticalAxis] = field(
        default=None,
        metadata={
            "name": "VerticalAxis",
            "type": "Element",
            "required": True,
        }
    )
    origin_uncertainty_vector_at_one_sigma: Optional[Vector] = field(
        default=None,
        metadata={
            "name": "OriginUncertaintyVectorAtOneSigma",
            "type": "Element",
        }
    )
    local_engineering2d_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalEngineering2dCrs",
            "type": "Element",
            "required": True,
        }
    )

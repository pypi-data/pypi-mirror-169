from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_fiber_facility import AbstractFiberFacility
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberFacilityMappingPart:
    """
    Relates distances measured along the optical path to specific lengths along
    facilities (wellbores or pipelines).

    :ivar optical_path_distance_start: Distance between the beginning of
        the optical path to the distance where the mapping with the
        facility takes place.
    :ivar optical_path_distance_end: Distance between the beginning of
        the optical path to the distance where the mapping with the
        facility ends.
    :ivar facility_length_start: Distance between the facility datum and
        the distance where the mapping with the optical path takes
        place.
    :ivar facility_length_end: Distance between the facility datum and
        the distance where the mapping with the optical path ends.
    :ivar comment: A descriptive remark about the facility mapping.
    :ivar fiber_facility:
    :ivar uid: Unique identifier or this object.
    """
    optical_path_distance_start: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OpticalPathDistanceStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    optical_path_distance_end: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OpticalPathDistanceEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    facility_length_start: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FacilityLengthStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    facility_length_end: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FacilityLengthEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    fiber_facility: Optional[AbstractFiberFacility] = field(
        default=None,
        metadata={
            "name": "FiberFacility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )

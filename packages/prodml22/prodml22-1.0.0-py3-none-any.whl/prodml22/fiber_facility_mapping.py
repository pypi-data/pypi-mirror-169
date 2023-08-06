from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fiber_facility_mapping_part import FiberFacilityMappingPart

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberFacilityMapping:
    """Relates lengths of fiber to corresponding lengths of facilities
    (probably wellbores or pipelines).

    The facilityMapping also contains the datum from which the
    InterpretedData is indexed.

    :ivar time_start: Date when the mapping between the facility and the
        optical path becomes effective.
    :ivar time_end: Date when the mapping between the facility and the
        optical path is no longer valid.
    :ivar comment: A descriptive remark about the facility mapping.
    :ivar fiber_facility_mapping_part: Relates distances measured along
        the optical path to specific lengths along facilities (wellbores
        or pipelines).
    :ivar uid: Unique identifier of this object.
    """
    time_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    time_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
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
    fiber_facility_mapping_part: List[FiberFacilityMappingPart] = field(
        default_factory=list,
        metadata={
            "name": "FiberFacilityMappingPart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
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

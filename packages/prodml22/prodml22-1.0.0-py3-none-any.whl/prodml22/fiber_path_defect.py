from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.length_measure import LengthMeasure
from prodml22.path_defect_kind import PathDefectKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberPathDefect:
    """
    A zone of the fiber that has defective optical properties (e.g.,
    darkening).

    :ivar optical_path_distance_start: Starting point of the detected
        defect as distance in the optical path from the lightbox.
    :ivar optical_path_distance_end: Ending point of the detected defect
        as distance in the optical path from the lightbox. if the defect
        is found at a specific location rather than a segment, then it
        can have the same value as the opticalPathDistanceStart.
    :ivar defect_type: Enum. The type of defect on the optical path.
    :ivar time_start: Date when the defect was detected.
    :ivar time_end: Date when the defect was no longer detected (or was
        corrected).
    :ivar comment: A descriptive remark about the defect found on this
        location.
    :ivar defect_id: The unique identifier of this object.
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
        }
    )
    defect_type: Optional[PathDefectKind] = field(
        default=None,
        metadata={
            "name": "DefectType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    time_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
    defect_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "defectID",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.das_calibration_input_point_kind import DasCalibrationInputPointKind
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasCalibrationInputPoint:
    """This object contains, for a given parent Calibration, the inputs to the
    calibration process.

    Each such point is represented by an instance of this object. Each
    such instance represents a place where a physical feature of the
    fiber optical path or the facility can be observed as a signal in
    the DAS data.  For example, a tap test is where a noise (tapping) is
    generated at a known place (a known location in the facility), and
    can be seen in the DAS signal at a specific locus.  This fact is
    recorded in one instance of this object.  Over time it is expected
    that other commonly used noise generating locations will be listed
    in the enum for InputPointType. Business Rule: Note that it is
    possible to have a valid Calibration comprising only a collection of
    DasCalibrationInputPoint. It is not a requirement to also have the
    corresponding "look up table" of a collection of
    FiberLocusDepthPoint.  If the receiving application can create its
    own interpolation of locus depth points then the collection of
    DasCalibrationInputPoint is all that is needed.

    :ivar remark: A brief meaningful description of the type of
        calibration point. This is an extensible enumeration type.
        Current reserved keywords are ‘locus calibration’, ‘tap test’
        and ‘last locus to end of fiber’ for commonly used calibration
        points.
    :ivar locus_index: The locus index for the calibration point. Where
        ‘Locus Index 0’ is generally understood to mean, the acoustic
        sample point at the connector of the measurement instrument.
    :ivar optical_path_distance: The optical path distance (ie, the
        distance along the fiber) from the connector of the measurement
        instrument to the acoustic sample point (with the given locus
        index) of the calibration point. Mandatory since any Calibration
        Input Point must have a known optical oath distance.
    :ivar facility_length: The ‘facility length’ corresponding to the
        locus. The ‘facility length’ is the length along the physical
        facility (eg measured depth if the facility is a wellbore). This
        length corrects the optical path distance for the offset from
        previous facilities on the same fiber optical path, surface
        patch cord lengths, overstuffing, additional fiber in
        turnaround-subs or H-splices that increase the optical path
        length on the OTDR, but not the actual facility length. Facility
        length is the value which is required to associate the DAS data
        at a locus with a physical location, but at the time of the
        Calibration this may not be known and so this element is
        optional.
    :ivar input_point_kind: The kind of calibration point. This is an
        extensible enumeration type. Current enum values are ‘tap test’
        and ‘other calibration point’. Other commonly used calibration
        points are understood to be packers, sub surface safety valves,
        perforations, all of which give recognizable noise signals
        observed in the DAS data.  At the time of issue of this standard
        there is not a consensus regarding which other values should be
        regarded as standard kinds of calibration input points.
    """
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    locus_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "LocusIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    optical_path_distance: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OpticalPathDistance",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    facility_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FacilityLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    input_point_kind: Optional[Union[DasCalibrationInputPointKind, str]] = field(
        default=None,
        metadata={
            "name": "InputPointKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )

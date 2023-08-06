from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.calibration import Calibration
from prodml22.data_object_reference import DataObjectReference
from prodml22.facility_kind import FacilityKind
from prodml22.length_uom import LengthUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FacilityCalibration:
    """This object contains, for a single facility, details of the calibration
    process and results whereby each locus (an acquired data point along the
    fiber optical path) is mapped to a physical location in the facility.

    This object should repeat for each distinct facility along the fiber
    optical path. Eg, a fiber optical path which runs along a flowline
    and then down a wellbore spans two facilities (flowline and
    wellbore), and each of these will have an instance of this object.

    :ivar remark: Textual description about the value of this field.
    :ivar facility_name: This element contains the facility name.
    :ivar facility_kind: The facility kind, (for example, wellbore,
        pipeline, etc).
    :ivar wellbore: If the facility is a wellbore then optionally this
        can be used to define a Data Object Reference to a WITSML
        Wellbore object.
    :ivar optical_path_distance_unit: Unit of measurement of
        OpticalPathDistance values in DasCalibrationInputPoint and
        FiberLocusDepthPoint elements. Required for the HDF5 file
        attributes since HDF5 files do not include units of measure as
        standard Energistics XML does. This element is a duplication
        therefore, in the XML files.
    :ivar facility_length_unit: Unit of measurement of FacilityLength
        values in DasCalibrationInputPoint and FiberLocusDepthPoint
        elements. Required for the HDF5 file attributes since HDF5 files
        do not include units of measure as standard Energistics XML
        does. This element is a duplication therefore, in the XML files.
    :ivar calibration:
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
    facility_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    facility_kind: Optional[FacilityKind] = field(
        default=None,
        metadata={
            "name": "FacilityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    optical_path_distance_unit: Optional[LengthUom] = field(
        default=None,
        metadata={
            "name": "OpticalPathDistanceUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    facility_length_unit: Optional[LengthUom] = field(
        default=None,
        metadata={
            "name": "FacilityLengthUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    calibration: List[Calibration] = field(
        default_factory=list,
        metadata={
            "name": "Calibration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )

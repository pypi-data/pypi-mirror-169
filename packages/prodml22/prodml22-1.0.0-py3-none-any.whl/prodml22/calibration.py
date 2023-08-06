from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.compound_external_array import CompoundExternalArray
from prodml22.das_calibration_input_point import DasCalibrationInputPoint
from prodml22.data_object_reference import DataObjectReference
from prodml22.length_measure import LengthMeasure
from prodml22.reference_point_kind import ReferencePointKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Calibration:
    """This object contains, for a single facility (defined by its parent
    Facility Calibration), a single Calibration, ie, details of the calibration
    process and results whereby each locus (an acquired data point along the
    fiber optical path) is mapped to a physical location in the facility.

    It is common in DAS processing for such calibrations to be refined
    over time as further data become available.  Each such successive
    calibration can be described using an instance of this object.

    :ivar remark: Textual description about the value of this field.
    :ivar last_locus_to_end_of_fiber: This element records the length,
        which can be observed in the DAS data, between the last locus in
        a fiber optical path, and the end of the fiber. As such, this
        distance is a useful input to the calibration process. There
        will only be one such measurement along a fiber optical path,
        that on the last facility before the end of the fiber (eg at the
        bottom a wellbore, in the event that say a flowline and then a
        wellbore are being measured using the same fiber optical path).
        For this reason this element is optional.
    :ivar otdr: If a OTDR (optical time domain reflectometry) survey is
        carried out, a top level object called OTDR Acquisition can be
        created to report the results.  In the event that such a survey
        is used as the input to a Calibration, then a Data Object
        Reference to that object can be inserted with this element.
    :ivar wellbore_datum: In the event that the facility kind is a
        wellbore, this element is used to record the datum from which
        measured depth is referenced.  The type is
        WellboreDatumReference, an enum in the Energistics Common
        package (example value, kelly bushing).
    :ivar pipeline_datum: In the event that the facility kind is a
        pipeline, this element is used to record the datum from which
        facility (pipeline) length is referenced.  The type is a string
        since there is currently no standard enum for this type of data.
        It is expected that the value would be a string to describe, eg
        one end of the pipe from which measurement is made.
    :ivar originator: Name (or other human-readable identifier) of the
        person who initially originated the Calbration. If that
        information is not available, then this is the user who created
        the format file. The originator remains the same as the object
        is subsequently edited. This is the equivalent in ISO 19115 to
        the CI_Individual.name or the CI_Organization.name of the
        citedResponsibleParty whose role is "originator". Legacy DCGroup
        - author
    :ivar creation: Date and time the Calibration was created in the
        source application or, if that information is not available,
        when it was saved to the file. This is the equivalent of the ISO
        19115 CI_Date where the CI_DateTypeCode = "creation" Format:
        YYYY-MM-DDThh:mm:ssZ[+/-]hh:mm Legacy DCGroup - created
    :ivar editor: Name (or other human-readable identifier) of the last
        person who updated the Calibration. This is the equivalent in
        ISO 19115 to the CI_Individual.name or the CI_Organization.name
        of the citedResponsibleParty whose role is "editor". Legacy
        DCGroup - contributor
    :ivar last_update: Date and time the Calibration was last modified
        in the source application or, if that information is not
        available, when it was last saved to the format file. This is
        the equivalent of the ISO 19115 CI_Date where the
        CI_DateTypeCode = "lastUpdate" Format: YYYY-MM-
        DDThh:mm:ssZ[+/-]hh:mm Legacy DCGroup - modified
    :ivar locus_depth_point: This array must have a compound data type
        consisting of three data types: LocusIndex (int64),
        OpticalPathDistance (float64), FacilityLength (float64)
    :ivar calibration_input_point:
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
    last_locus_to_end_of_fiber: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LastLocusToEndOfFiber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    otdr: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "OTDR",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wellbore_datum: Optional[ReferencePointKind] = field(
        default=None,
        metadata={
            "name": "WellboreDatum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pipeline_datum: Optional[str] = field(
        default=None,
        metadata={
            "name": "PipelineDatum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    originator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Originator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    creation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    editor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Editor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    last_update: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastUpdate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    locus_depth_point: Optional[CompoundExternalArray] = field(
        default=None,
        metadata={
            "name": "LocusDepthPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    calibration_input_point: List[DasCalibrationInputPoint] = field(
        default_factory=list,
        metadata={
            "name": "CalibrationInputPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )

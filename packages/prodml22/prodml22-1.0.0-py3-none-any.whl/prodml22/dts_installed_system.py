from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.dts_calibration import DtsCalibration
from prodml22.facility_identifier import FacilityIdentifier
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DtsInstalledSystem(AbstractObject):
    """
    The group of elements corresponding to a DTS installed system.

    :ivar date_min: The minimum date index contained within the object.
        The minimum and maximum indexes are server query parameters and
        are populated with valid values in a "get" result. That is, all
        measurements for a well in the specified period defined by the
        min/max. For a description of the behavior related to this
        parameter in WITSML v1.4.1, see the WITSML API Specification
        appendix on "Special Handling" of growing objects.
    :ivar date_max: The maximum date index contained within the object.
        The minimum and maximum indexes are server query parameters and
        are populated with valid values in a "get" result. For a
        description of the behavior related to this parameter in WITSML
        v1.4.1, see the WITSML API Specification appendix on "Special
        Handling" of growing objects.
    :ivar optical_path_length: The length of the fiber installed in the
        wellbore.
    :ivar optical_budget: Total light budget available for the
        installation. This is generally measured in decibels, and
        indicates the total power loss for two-way travel of the light
        in the installed fiber.
    :ivar optical_path: A reference to the optical path data object that
        is used in this installed system.
    :ivar instrument_box: A reference to the instrument box data object
        used in this installed system.
    :ivar comment: Comment about this installed system.
    :ivar facility_identifier: Contains details about the facility being
        surveyed, such as name, geographical data, etc.
    :ivar dts_calibration: Calibration parameters vary from vendor to
        vendor, depending on the calibration method being used. This is
        a general type that allows a calibration date, business
        associate, and many  name/value pairs.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    date_min: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateMin",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    date_max: Optional[str] = field(
        default=None,
        metadata={
            "name": "DateMax",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    optical_path_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OpticalPathLength",
            "type": "Element",
        }
    )
    optical_budget: Optional[float] = field(
        default=None,
        metadata={
            "name": "OpticalBudget",
            "type": "Element",
        }
    )
    optical_path: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "OpticalPath",
            "type": "Element",
            "required": True,
        }
    )
    instrument_box: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "InstrumentBox",
            "type": "Element",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "max_length": 2000,
        }
    )
    facility_identifier: Optional[FacilityIdentifier] = field(
        default=None,
        metadata={
            "name": "FacilityIdentifier",
            "type": "Element",
        }
    )
    dts_calibration: List[DtsCalibration] = field(
        default_factory=list,
        metadata={
            "name": "DtsCalibration",
            "type": "Element",
        }
    )

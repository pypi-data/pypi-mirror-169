from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.dts_calibration import DtsCalibration
from prodml22.dts_patch_cord import DtsPatchCord
from prodml22.extension_name_value import ExtensionNameValue
from prodml22.facility_identifier import FacilityIdentifier
from prodml22.instrument import Instrument
from prodml22.length_measure import LengthMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DtsInstrumentBox(AbstractObject):
    """
    The group of elements corresponding to a DTS instrument box.

    :ivar serial_number: An identification tag for the instrument box. A
        serial number is a type of identification tag; however, some
        tags contain many pieces of information. This structure only
        identifies the tag and does not describe the contents.
    :ivar internal_oven_location_near: Near distance of the oven from
        the beginning of the fiber.
    :ivar internal_oven_location_far: Far distance of the oven from the
        beginning of the fiber.
    :ivar reference_coil_temperature: The temperature of the oven.
    :ivar parameter: Additional parameters to define the instrument box
        as a piece of equipment. These should not be parameters to
        define the installation or use of the box in the wellbore or
        other system. Only use this element if an appropriate parameter
        is not available as an element or in the calibration operation.
    :ivar warmup_time: The duration of time starting from the initiation
        of the first temperature measurement until the unit complies
        with the stated values of the main measurement specifications.
    :ivar startup_time: The duration of time from the initial powering
        on of the instrument until the first temperature measurement is
        permitted.
    :ivar facility_identifier: Contains details about the facility being
        surveyed, such as name, geographical data, etc.
    :ivar instrument_calibration: Calibration parameters vary from
        vendor to vendor, depending on the calibration method being
        used. This is a general type that allows a calibration date,
        business associate, and many  name/value pairs.
    :ivar dts_patch_cord: Information regarding the patch cord used to
        connect the instrument box to the start of the optical fiber
        path.
    :ivar instrument:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SerialNumber",
            "type": "Element",
            "max_length": 64,
        }
    )
    internal_oven_location_near: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "InternalOvenLocationNear",
            "type": "Element",
        }
    )
    internal_oven_location_far: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "InternalOvenLocationFar",
            "type": "Element",
        }
    )
    reference_coil_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "ReferenceCoilTemperature",
            "type": "Element",
        }
    )
    parameter: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
        }
    )
    warmup_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "WarmupTime",
            "type": "Element",
        }
    )
    startup_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "StartupTime",
            "type": "Element",
        }
    )
    facility_identifier: Optional[FacilityIdentifier] = field(
        default=None,
        metadata={
            "name": "FacilityIdentifier",
            "type": "Element",
        }
    )
    instrument_calibration: List[DtsCalibration] = field(
        default_factory=list,
        metadata={
            "name": "InstrumentCalibration",
            "type": "Element",
        }
    )
    dts_patch_cord: Optional[DtsPatchCord] = field(
        default=None,
        metadata={
            "name": "DtsPatchCord",
            "type": "Element",
        }
    )
    instrument: Optional[Instrument] = field(
        default=None,
        metadata={
            "name": "Instrument",
            "type": "Element",
            "required": True,
        }
    )

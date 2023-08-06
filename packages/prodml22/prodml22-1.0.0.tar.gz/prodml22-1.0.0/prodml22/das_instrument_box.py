from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.dts_patch_cord import DtsPatchCord
from prodml22.extension_name_value import ExtensionNameValue
from prodml22.facility_identifier import FacilityIdentifier
from prodml22.instrument import Instrument

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasInstrumentBox(AbstractObject):
    """
    The group of elements corresponding to a DAS instrument box.

    :ivar serial_number: An identification tag for the instrument box. A
        serial number is a type of identification tag however some tags
        contain many pieces of information. This structure just
        identifies the tag and does not describe the contents.
    :ivar parameter: Additional parameters to define the instrument box
        as a piece of equipment. These should not be parameters to
        define the installation or use of the box in the wellbore, or
        other system. This element should be used only if an appropriate
        parameter is not available as an element, or in the calibration
        operation.
    :ivar facility_identifier: Identifies the facility to which an
        instrument is attached.  Type is the PRODML Common Facility
        Identifier.
    :ivar instrument: The general data of an instrument, including
        vendor information, in the installed system.
    :ivar firmware_version: Firmware version of the DAS Instrument box.
        If not known, set to "UNKNOWN".
    :ivar patch_cord: Description of the patch cord connecting the fiber
        optic path to the DAS instrument box connector.
    :ivar instrument_box_description: An identification tag for the
        instrument box. A serial number is a type of identification tag
        however some tags contain many pieces of information. This
        structure just identifies the tag and does not describe the
        contents.
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
    parameter: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
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
    instrument: Optional[Instrument] = field(
        default=None,
        metadata={
            "name": "Instrument",
            "type": "Element",
            "required": True,
        }
    )
    firmware_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirmwareVersion",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    patch_cord: Optional[DtsPatchCord] = field(
        default=None,
        metadata={
            "name": "PatchCord",
            "type": "Element",
        }
    )
    instrument_box_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrumentBoxDescription",
            "type": "Element",
            "max_length": 2000,
        }
    )

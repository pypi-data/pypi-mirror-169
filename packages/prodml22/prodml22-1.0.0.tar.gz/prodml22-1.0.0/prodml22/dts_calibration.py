from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from prodml22.calibration_parameter import CalibrationParameter
from prodml22.extension_name_value import ExtensionNameValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DtsCalibration:
    """Calibration parameters vary from vendor to vendor, depending on the
    calibration method being used.

    This is a general type that allows a calibration date, business
    associate, and many name/value pairs.

    :ivar dtim_calibration: The date of the calibration.
    :ivar calibrated_by: The business associate that performed the
        calibration.
    :ivar calibration_protocol: This may be a standard protocol or a
        software application.
    :ivar parameter: Attribute name is the name of the parameter.
        Optional attribute uom is the unit of measure of the parameter.
        The value of the element is the value of the parameter. Note
        that a string value may appear as a parameter.
    :ivar remark: Any remarks that may be useful regarding the
        calibration information.
    :ivar extension_name_value: WITSML - Extension values Schema. The
        intent is to allow standard WITSML "named" extensions without
        having to modify the schema. A client or server can ignore any
        name that it does not recognize but certain meta data is
        required in order to allow generic clients or servers to process
        the value.
    :ivar uid: A  unique identifier (UID) of an instance of
        DtsCalibration.
    """
    dtim_calibration: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DTimCalibration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    calibrated_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "CalibratedBy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    calibration_protocol: Optional[str] = field(
        default=None,
        metadata={
            "name": "CalibrationProtocol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    parameter: List[CalibrationParameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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

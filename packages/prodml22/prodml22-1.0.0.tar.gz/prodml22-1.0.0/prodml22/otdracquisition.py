from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.fiber_otdrinstrument_box import FiberOtdrinstrumentBox
from prodml22.length_measure import LengthMeasure
from prodml22.otdrdirection import Otdrdirection
from prodml22.otdrreason import Otdrreason

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Otdracquisition(AbstractObject):
    """Records the result arrays along with context information for an optical
    time domain reflectometry (OTDR) survey.

    The arrays define the relative scattered power from the Rayleigh
    scattering vs. distance along the fiber. The actual data values are
    recorded in an OTDR file and/or image file, which are referenced in
    sub-elements.

    :ivar name: The name of this object.
    :ivar reason_for_run: The reason the OTDR test was run. Reasons
        include: - pre-installation, which is before the installation of
        the fiber - post-installation, which is used to validate a
        successful fiber installation - DTS run, a quality check of the
        fiber before a DTS run - Other
    :ivar dtim_run: The dateTime of the run.
    :ivar data_in_otdrfile: A reference to the external file used to
        record the OTDR data. Note this file will not be in an
        Energistics format but likely in a special OTDR format.
    :ivar otdrimage_file: A reference to the well log used to record the
        table of data.
    :ivar optical_path_distance_start: The point measured along the
        optical path at which this OTDR survey starts.
    :ivar optical_path_distance_end: The point measured along the
        optical path at which this OTDR survey ends.
    :ivar direction: Enum. The direction of the OTDR survey. "Forward"
        means "in the same direction as the positive direction along the
        optical path".
    :ivar wavelength: The wavelength at which this OTDR survey was
        carried out.
    :ivar measurement_contact: Contact for the person who performed the
        OTDR reading
    :ivar fiber_otdrinstrument_box: Information about an OTDR instrument
        box taht is used to perform OTDR surveys on the optical path.
    """
    class Meta:
        name = "OTDRAcquisition"
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    reason_for_run: Optional[Otdrreason] = field(
        default=None,
        metadata={
            "name": "ReasonForRun",
            "type": "Element",
        }
    )
    dtim_run: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimRun",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    data_in_otdrfile: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataInOTDRFile",
            "type": "Element",
            "max_length": 64,
        }
    )
    otdrimage_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "OTDRImageFile",
            "type": "Element",
            "max_length": 64,
        }
    )
    optical_path_distance_start: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OpticalPathDistanceStart",
            "type": "Element",
            "required": True,
        }
    )
    optical_path_distance_end: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OpticalPathDistanceEnd",
            "type": "Element",
            "required": True,
        }
    )
    direction: Optional[Otdrdirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "required": True,
        }
    )
    wavelength: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Wavelength",
            "type": "Element",
            "required": True,
        }
    )
    measurement_contact: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "MeasurementContact",
            "type": "Element",
        }
    )
    fiber_otdrinstrument_box: Optional[FiberOtdrinstrumentBox] = field(
        default=None,
        metadata={
            "name": "FiberOTDRInstrumentBox",
            "type": "Element",
        }
    )

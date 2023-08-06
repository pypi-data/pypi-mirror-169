from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.dts_interpretation_log_set import DtsInterpretationLogSet
from prodml22.dts_measurement_trace import DtsMeasurementTrace
from prodml22.facility_identifier import FacilityIdentifier
from prodml22.optical_path_configuration import OpticalPathConfiguration
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DtsMeasurement(AbstractObject):
    """
    The group of elements corresponding to a DTS measurement.

    :ivar bad_set_flag: Set to 'true' when a measurement is included but
        is known to be bad (i.e., all the values are null). Use this
        flag in situations when you want to keep track of the fact that
        a measurement was generated/received, however the measurement
        was bad.
    :ivar empty_set_flag: Set to 'true' when the measurement set is
        empty (only the header is provided). Use this flag for
        situations when the instrument box attempts to get a reading,
        but nothing is generated (fiber is disconnected, for example).
    :ivar time_start: Time when the installed system began taking the
        measurement.
    :ivar time_end: Time when the installed system finished taking the
        measurement.
    :ivar time_since_instrument_startup: Length of time that the
        instrument box has been up and running since its last power up.
    :ivar measurement_tags: This supports user-defined "tags" (in the
        form of text strings) to be attached to the measurement.
        Example: to indicate other operations under way at the time
        (e.g., start of injection).
    :ivar installed_system: Reference to the installed system used to
        take the measurement (combination of instrument box and optical
        path).
    :ivar measurement_configuration: Enum. The configuration of the
        optical path. This may be varied from measurement to
        measurement, independent of the fiber path network.
    :ivar facility_identifier: Contains details about the facility being
        surveyed, such as name, geographical data, etc.
    :ivar interpretation_log:
    :ivar measurement_trace: Header data for raw (measured) traces
        collections
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    bad_set_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BadSetFlag",
            "type": "Element",
            "required": True,
        }
    )
    empty_set_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EmptySetFlag",
            "type": "Element",
            "required": True,
        }
    )
    time_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeStart",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    time_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    time_since_instrument_startup: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "TimeSinceInstrumentStartup",
            "type": "Element",
        }
    )
    measurement_tags: List[str] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementTags",
            "type": "Element",
            "max_length": 64,
        }
    )
    installed_system: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "InstalledSystem",
            "type": "Element",
            "required": True,
        }
    )
    measurement_configuration: Optional[OpticalPathConfiguration] = field(
        default=None,
        metadata={
            "name": "MeasurementConfiguration",
            "type": "Element",
            "required": True,
        }
    )
    facility_identifier: Optional[FacilityIdentifier] = field(
        default=None,
        metadata={
            "name": "FacilityIdentifier",
            "type": "Element",
            "required": True,
        }
    )
    interpretation_log: Optional[DtsInterpretationLogSet] = field(
        default=None,
        metadata={
            "name": "InterpretationLog",
            "type": "Element",
        }
    )
    measurement_trace: List[DtsMeasurementTrace] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementTrace",
            "type": "Element",
        }
    )

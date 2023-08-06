from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.das_custom import DasCustom
from prodml22.das_processed import DasProcessed
from prodml22.das_raw import DasRaw
from prodml22.data_object_reference import DataObjectReference
from prodml22.facility_calibration import FacilityCalibration
from prodml22.frequency_measure import FrequencyMeasure
from prodml22.length_measure import LengthMeasure
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasAcquisition(AbstractObject):
    """
    Contains metadata about the DAS acquisition common to the various types of
    data acquired during the acquisition, which includes DAS measurement
    instrument data, fiber optical path, time zone, and core acquisition
    settings like pulse rate and gauge length, measurement start time and
    whether or not this was a triggered measurement.

    :ivar acquisition_id: A UUID that identifies the DAS acquisition
        job, which IS NOT the same as the UUID that identifies an
        instance of a DasAcquisition data object. For example, an
        acquisition job initially has a raw data set. When you transfer
        that data, the DAS acquisition data object (consisting of the
        raw data) has a UUID to identify it, and it has the acquisition
        job number (AcquistionId, which is also a UUID).  Later, an FBE
        data set is derived from the raw data; the DAS acquisition data
        object for the FBE data will have a different UUID than the DAS
        acquisition data object raw data set, but it will have the SAME
        AcquistionId, because the FBE data is derived from the raw data
        of the same acquisition job.
    :ivar acquisition_description: Free format description of the
        acquired DAS data.
    :ivar optical_path: Description of the fiber optical path. A fiber
        optical path consists of a series of fibers, connectors, etc.
        together forming the path for the light pulse emitted from the
        measurement instrument. If no optical path description is
        available, then the service provider should supply an optical
        path with a single segment of sufficient length to fit the
        optical data acquired. The length of the segment should be able
        to fit all the acquired loci.
    :ivar das_instrument_box: Description of the measurement instrument.
        Often referred to as interrogator unit or IU. If the instrument
        box is not known, the name and title of the box may be set to
        "UNKNOWN".
    :ivar facility_id: This is a human-readable name for the facility or
        facilities that this acquisition is measuring. If the facility
        name is not available, set one facility with the name "UNKNOWN".
    :ivar service_company_details: Description of the vendor providing
        the DAS data acquisition service.
    :ivar pulse_rate: The rate at which the interrogator unit
        interrogates the fiber sensor. For most interrogators, this
        element is informally known as the ‘pulse rate’.
    :ivar pulse_width: The width of the ‘pulse’ sent down the fiber.
    :ivar gauge_length: The distance (length along the fiber) between
        pair of pulses used in a dual-pulse or multi-pulse system. This
        is a distance that the DAS interrogator unit manufacturer
        designs and implements by hardware or software to affect the
        interrogator unit spatial resolution.
    :ivar spatial_sampling_interval: The separation between two
        consecutive ‘spatial sample’ points on the fiber at which the
        signal is measured. Not to be confused with ‘spatial
        resolution’.
    :ivar minimum_frequency: The minimum signal frequency a measurement
        instrument can provide as specified by the vendor. If the
        minimum frequency of the instrument is not known, the value
        should match the minimum frequency in the related raw, FBE,
        and/or spectrum data arrays.
    :ivar maximum_frequency: The maximum signal frequency a measurement
        instrument can provide as specified by the vendor. This is the
        Nyquist frequency (or some fraction thereof) of PulseRate. If
        the maximum frequency of the instrument is not known, the value
        should match the maximum frequency in the related raw, FBE
        and/or spectrum data arrays.
    :ivar number_of_loci: The total number of ‘loci’ (acoustic sample
        points) acquired by the measurement instrument in a single
        ‘scan’ of the fiber. If the total number of loci of the
        instrument is not known, it should be set to a value such that
        all related raw, FBE, and spectra data can be accommodated.
    :ivar start_locus_index: The first ‘locus’ acquired by the
        interrogator unit, where ‘Locus Index 0’ is the acoustic sample
        point at the connector of the measurement instrument. Set this
        value to accommodate all related raw, FBE, and spectrum data
        arrays. If an offset is applied such that the first acoustic
        sample point is not located at the connector of the measurement
        instrument, then set this to the locus corresponding to the
        offset.
    :ivar measurement_start_time: The time-date specification of the
        beginning of a data ‘sample’ in a ‘time series’ in ISO 8601
        compatible format. Time zone should be included. Sub-second
        precision should be included where applicable but not zero-
        padded. ­This is typically a GPS-locked time measurement. If
        this is not known, use the earliest timestamp in the related
        raw, FBE and/or spectrum data arrays. In very rare situations
        where there is no data array, use
        1970-01-01T00;00;00.000000+00:00.
    :ivar triggered_measurement: Measurement for an acquisition that
        requires synchronization between a transmitting source (Tx) and
        a recording (Rx) measurement system. It must be recorded for
        every measurement regardless of what application it will serve.
        If set to true, then the DasRaw group should contain 1 or more
        RawDataTriggerTime. If set to false, then no such
        RawDataTriggerTime is expected.
    :ivar raw:
    :ivar custom:
    :ivar facility_calibration:
    :ivar processed:
    :ivar service_company_name:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    acquisition_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcquisitionId",
            "type": "Element",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    acquisition_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcquisitionDescription",
            "type": "Element",
            "max_length": 2000,
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
    das_instrument_box: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "DasInstrumentBox",
            "type": "Element",
            "required": True,
        }
    )
    facility_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FacilityId",
            "type": "Element",
            "min_occurs": 1,
            "max_length": 64,
        }
    )
    service_company_details: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ServiceCompanyDetails",
            "type": "Element",
        }
    )
    pulse_rate: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "PulseRate",
            "type": "Element",
        }
    )
    pulse_width: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "PulseWidth",
            "type": "Element",
        }
    )
    gauge_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "GaugeLength",
            "type": "Element",
        }
    )
    spatial_sampling_interval: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SpatialSamplingInterval",
            "type": "Element",
            "required": True,
        }
    )
    minimum_frequency: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "MinimumFrequency",
            "type": "Element",
            "required": True,
        }
    )
    maximum_frequency: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "MaximumFrequency",
            "type": "Element",
            "required": True,
        }
    )
    number_of_loci: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfLoci",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
        }
    )
    start_locus_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartLocusIndex",
            "type": "Element",
            "required": True,
        }
    )
    measurement_start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "MeasurementStartTime",
            "type": "Element",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    triggered_measurement: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TriggeredMeasurement",
            "type": "Element",
            "required": True,
        }
    )
    raw: List[DasRaw] = field(
        default_factory=list,
        metadata={
            "name": "Raw",
            "type": "Element",
        }
    )
    custom: Optional[DasCustom] = field(
        default=None,
        metadata={
            "name": "Custom",
            "type": "Element",
        }
    )
    facility_calibration: List[FacilityCalibration] = field(
        default_factory=list,
        metadata={
            "name": "FacilityCalibration",
            "type": "Element",
        }
    )
    processed: Optional[DasProcessed] = field(
        default=None,
        metadata={
            "name": "Processed",
            "type": "Element",
        }
    )
    service_company_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceCompanyName",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )

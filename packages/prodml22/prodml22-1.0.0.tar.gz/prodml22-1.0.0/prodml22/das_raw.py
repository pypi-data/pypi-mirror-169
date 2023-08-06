from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.das_custom import DasCustom
from prodml22.das_raw_data import DasRawData
from prodml22.das_time_array import DasTimeArray
from prodml22.frequency_measure import FrequencyMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasRaw:
    """This object contains the attributes of raw data acquired by the DAS
    measurement instrument.

    This includes the raw data unit, the location of the raw data
    acquired along the fiber optical path, and information about times
    and (optional) triggers. Note that the actual raw data samples,
    times and trigger times arrays are not present in the XML files but
    only in the HDF5 files because of their size. The XML files only
    contain references to locate the corresponding HDF files, which
    contain the actual raw samples, times, and (optional) trigger times.

    :ivar raw_index: The nth (zero-based) count of this Raw instance in
        the Acquisition.  Recommended if there is more than 1 Raw
        instance in this Acquisition.  This index corresponds to the Raw
        array number in the HDF5 file.
    :ivar raw_description: Free format description of the raw DAS data
        acquired.
    :ivar raw_data_unit: Data unit for the DAS measurement instrument.
    :ivar output_data_rate: The rate at which the spectra data is
        provided for all ‘loci’ (spatial samples). This is typically
        equal to the interrogation rate/pulse rate of the DAS
        measurement system or an integer fraction thereof. This
        attribute is optional in the Raw Data object. If present, it
        overrides the Acquisition PulseRate. If not present, then
        OutputDataRate is assumed equal to the PulseRate.
    :ivar start_locus_index: The first ‘locus’ acquired by the
        interrogator unit. Where ‘Locus Index 0’ is the acoustic sample
        point at the connector of the measurement instrument.
    :ivar number_of_loci: The total number of ‘loci’ (acoustic sample
        points) acquired by the measurement instrument in a single
        ‘scan’ of the fiber.
    :ivar raw_data: A DAS array object containing the raw DAS data.
    :ivar raw_data_time: A DAS array object containing the sample times
        corresponding to a single ‘scan’ of the fiber. In a single
        ‘scan’, the DAS measurement system acquires raw data samples for
        all the loci specified by StartLocusIndex. The ‘scan’ frequency
        is equal to the DAS Acquisition Pulse Rate.
    :ivar raw_data_trigger_time: A DAS array object containing the times
        of the triggers in a triggered measurement. Multiple times may
        be stored to indicate multiple triggers within a single DAS raw
        data recording. This array contains only valid data if
        TriggeredMeasurement is set to ‘true’ in DAS Acquisition.
    :ivar custom:
    :ivar uuid: A universally unique identifier (UUID) for an instance
        of raw DAS data.
    """
    raw_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RawIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
        }
    )
    raw_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "RawDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    raw_data_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "RawDataUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    output_data_rate: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "OutputDataRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    start_locus_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartLocusIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    number_of_loci: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfLoci",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    raw_data: Optional[DasRawData] = field(
        default=None,
        metadata={
            "name": "RawData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    raw_data_time: Optional[DasTimeArray] = field(
        default=None,
        metadata={
            "name": "RawDataTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    raw_data_trigger_time: Optional[DasTimeArray] = field(
        default=None,
        metadata={
            "name": "RawDataTriggerTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    custom: Optional[DasCustom] = field(
        default=None,
        metadata={
            "name": "Custom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )

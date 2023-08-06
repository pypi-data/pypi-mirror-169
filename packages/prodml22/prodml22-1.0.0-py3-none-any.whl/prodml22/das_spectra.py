from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.das_custom import DasCustom
from prodml22.das_spectra_data import DasSpectraData
from prodml22.das_time_array import DasTimeArray
from prodml22.frequency_measure import FrequencyMeasure
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasSpectra:
    """This object contains the attributes of spectra processed data.

    This includes the spectra data unit, location of the spectra data
    along the fiber optical path, information about times, (optional)
    filter related parameters, and UUIDs of the original raw from which
    the spectra file was processed and/or the UUID of the FBE files that
    were processed from the spectra files. Note that the actual spectrum
    data samples and times arrays are not present in the XML files but
    only in the HDF5 files because of their size. The XML files only
    contain references to locate the corresponding HDF files containing
    the actual spectrum samples and times.

    :ivar spectra_index: The nth (zero-based) count of this Spectra
        instance in the acquisition. Recommended if there is more than 1
        Spectra instance in this acquisition.  This index corresponds to
        the Spectra array number in the HDF5 file.
    :ivar spectra_description: Description of the spectra data.
    :ivar spectra_data_unit: Data unit for the spectra data.
    :ivar output_data_rate: The rate at which the spectra data is
        provided for all ‘loci’ (spatial samples). This is typically
        equal to the interrogation rate/pulse rate of the DAS
        measurement system or an integer fraction thereof. Note this
        attribute is mandatory for FBE and spectrum data. For raw data
        this attribute is optional.
    :ivar start_locus_index: The first ‘locus’ acquired by the
        interrogator unit, where ‘Locus Index 0’ is the acoustic sample
        point at the connector of the measurement instrument.
    :ivar number_of_loci: The total number of ‘loci’ (acoustic sample
        points) acquired by the measurement instrument in a single
        ‘scan’ of the fiber.
    :ivar spatial_sampling_interval: The separation between two
        consecutive ‘spatial sample’ points on the fiber at which the
        signal is measured. It should not be confused with ‘spatial
        resolution’. If this data element is present in the DasSpectrum
        object, then it overwrites the SpatialSamplingInterval value
        described in DasAcquistion.
    :ivar spatial_sampling_interval_unit: Only required in an HDF5 file
        to record the unit of measure of the sampling interval of the
        spectra.
    :ivar filter_type: A string describing the type of filter applied by
        the vendor. Important frequency type filter classes are:
        frequency response filters (low-pass, high-pass, band-pass,
        notch filters) and butterworth, chebyshev and bessel filters.
        The filter type and characteristics applied to the acquired or
        processed data is important information for end-user
        applications.
    :ivar window_size: The number of samples in the filter window
        applied.
    :ivar window_overlap: The number of sample overlaps between
        consecutive filter windows applied.
    :ivar window_function: A string describing the window function
        applied by the vendor. Examples are "Hamming" or "Hanning".
    :ivar transform_type: A string describing the type of mathematical
        transformation applied by the vendor. Typically this is some
        type of discrete fast Fourier transform (often abbreviated as
        DFT, DFFT or FFT).
    :ivar transform_size: The number of samples used in the
        TransformType.
    :ivar raw_reference: Unique identifier for the HDF5 file containing
        the raw data.
    :ivar fbe_reference: A universally unique identifier (UUID) of an
        instance of DAS FBE data.
    :ivar spectra_data: A DAS array object containing the spectra DAS
        data.
    :ivar spectra_data_time: A DAS array object containing the sample
        times corresponding to a single ‘scan’ of the fiber. In a single
        ‘scan’, the DAS measurement system acquires raw data samples for
        all the loci specified by StartLocusIndex and NumberOfLoci. The
        ‘scan’ frequency is equal to the DAS acquisition pulse rate.
    :ivar custom:
    :ivar uuid: A universally unique identifier (UUID) for an instance
        of spectra DAS data.
    """
    spectra_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpectraIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
        }
    )
    spectra_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpectraDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    spectra_data_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpectraDataUnit",
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
            "required": True,
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
    spatial_sampling_interval: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SpatialSamplingInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    spatial_sampling_interval_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpatialSamplingIntervalUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    filter_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FilterType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    window_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "WindowSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
        }
    )
    window_overlap: Optional[int] = field(
        default=None,
        metadata={
            "name": "WindowOverlap",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
        }
    )
    window_function: Optional[str] = field(
        default=None,
        metadata={
            "name": "WindowFunction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    transform_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransformType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    transform_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "TransformSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    raw_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "RawReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    fbe_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "FbeReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    spectra_data: Optional[DasSpectraData] = field(
        default=None,
        metadata={
            "name": "SpectraData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    spectra_data_time: Optional[DasTimeArray] = field(
        default=None,
        metadata={
            "name": "SpectraDataTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
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

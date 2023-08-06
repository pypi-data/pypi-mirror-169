from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_numeric_array import AbstractNumericArray
from prodml22.das_dimensions import DasDimensions
from prodml22.frequency_measure import FrequencyMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasSpectraData:
    """Three-dimensional array (loci, time, transform) containing spectrum data
    samples.

    Spectrum data is processed data obtained by applying a mathematical
    transformation function to the DAS raw data acquired by the
    acquisition system. The array is 3D and contains TransformSize
    points for each locus and time for which the data is provided. For
    example, many service providers will provide Fourier transformed
    versions of the raw data to customers, but other transformation
    functions are also allowed.

    :ivar start_frequency: Start frequency in a DAS spectra data set.
        This value typically is set to the minimum frequency present in
        the spectra data set.
    :ivar end_frequency: End frequency in a DAS spectra data set. This
        value is typically set to the maximum frequency present in the
        spectra data set.
    :ivar dimensions: An array of three elements describing the ordering
        of the raw data array. The fastest running index is stored in
        the last element. For example {‘time’, ‘locus’, ‘frequency’}
        indicates that the frequency is the fastest running index. Note
        that vendors may deliver data with different orderings.
    :ivar spectra_data_array:
    """
    start_frequency: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "StartFrequency",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    end_frequency: Optional[FrequencyMeasure] = field(
        default=None,
        metadata={
            "name": "EndFrequency",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    dimensions: List[DasDimensions] = field(
        default_factory=list,
        metadata={
            "name": "Dimensions",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 3,
            "max_occurs": 3,
        }
    )
    spectra_data_array: Optional[AbstractNumericArray] = field(
        default=None,
        metadata={
            "name": "SpectraDataArray",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

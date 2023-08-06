from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_numeric_array import AbstractNumericArray
from prodml22.das_dimensions import DasDimensions
from prodml22.frequency_measure import FrequencyMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasFbeData:
    """Two dimensional (loci &amp; time) array containing processed frequency
    band extracted data samples.

    This processed data type is obtained by applying a frequency band
    filter to the raw data acquired by the DAS acquisition system. For
    each frequency band provided, a separate DASFbeData array object is
    created.

    :ivar fbe_data_index: The nth (zero-based) count of this DasFbeData
        in the DasFbe.  Recommended if there is more than 1 dataset in
        this FBE.  This index corresponds to the FbeData array number in
        the HDF5 file.
    :ivar start_frequency: Start of an individual frequency band in a
        DAS FBE data set. This typically corresponds to the frequency of
        the 3dB point of the filter.
    :ivar end_frequency: End of an individual frequency band in a DAS
        FBE data set. This typically corresponds to the frequency of the
        3dB point of the filter.
    :ivar dimensions: An array of two elements describing the ordering
        of the FBE data array. The fastest running index is stored in
        the second element. For example the {‘time’, ‘locus’} indicates
        that ‘locus’ is the fastest running index. Note that vendors may
        deliver data with different orderings.
    :ivar fbe_data_array:
    """
    fbe_data_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "FbeDataIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
        }
    )
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
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )
    fbe_data_array: Optional[AbstractNumericArray] = field(
        default=None,
        metadata={
            "name": "FbeDataArray",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

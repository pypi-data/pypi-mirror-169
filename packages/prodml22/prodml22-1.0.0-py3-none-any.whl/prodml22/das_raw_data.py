from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_numeric_array import AbstractNumericArray
from prodml22.das_dimensions import DasDimensions

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasRawData:
    """Two- dimensional array containing raw data samples acquired by the DAS acquisition system.

    :ivar dimensions: An array of two elements describing the ordering
        of the raw data array. The fastest running index is stored in
        the second element. For the DAS measurement instrument, the
        ordering is typically {‘time’, ‘locus’} indicating that the
        locus is the fastest running index, but in some cases the order
        may be reversed.
    :ivar raw_data_array:
    """
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
    raw_data_array: Optional[AbstractNumericArray] = field(
        default=None,
        metadata={
            "name": "RawDataArray",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

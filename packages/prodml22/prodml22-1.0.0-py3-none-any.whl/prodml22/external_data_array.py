from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.external_data_array_part import ExternalDataArrayPart

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ExternalDataArray:
    """A concatenation of ExternalDataArrayParts, which are pointers to a whole
    or to a sub-selection of an existing array that is in a different file
    (than the Energistics data object).

    It generally and historically points to an HDF5 dataset in an
    Energistics Packaging Conventions (EPC) context. It is common to
    have only 1 ExternalDataArrayPart in an ExternalDataArray.
    """
    external_data_array_part: List[ExternalDataArrayPart] = field(
        default_factory=list,
        metadata={
            "name": "ExternalDataArrayPart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
        }
    )

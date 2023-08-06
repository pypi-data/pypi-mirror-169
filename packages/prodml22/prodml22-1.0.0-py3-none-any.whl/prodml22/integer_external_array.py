from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_integer_array import AbstractIntegerArray
from prodml22.external_data_array import ExternalDataArray
from prodml22.integer_type import IntegerType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IntegerExternalArray(AbstractIntegerArray):
    """Array of integer values provided explicitly by an HDF5 dataset.

    The null value must be  explicitly provided in the NullValue
    attribute of this class.

    :ivar array_integer_type:
    :ivar null_value:
    :ivar count_per_value:
    :ivar values: Reference to an HDF5 array of integers or doubles.
    """
    array_integer_type: Optional[IntegerType] = field(
        default=None,
        metadata={
            "name": "ArrayIntegerType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    null_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "NullValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    count_per_value: int = field(
        default=1,
        metadata={
            "name": "CountPerValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    values: Optional[ExternalDataArray] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )

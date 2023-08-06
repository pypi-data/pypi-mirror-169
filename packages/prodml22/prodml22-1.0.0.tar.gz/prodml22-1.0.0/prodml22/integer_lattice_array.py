from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_integer_array import AbstractIntegerArray
from prodml22.integer_constant_array import IntegerConstantArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IntegerLatticeArray(AbstractIntegerArray):
    """Represents an array of integers based on an origin and a multi-
    dimensional offset.

    The offset is based on a linearization of a multi-dimensional offset.
    If count(i) is the number of elements in the dimension i and offset(i) is the offset in the dimension i, then:
    globalOffsetInNDimension = startValue+ ni*offset(n) + n_1i*count(n)*offset(n-1) + .... + 0i*count(n)*count(n-1)*....count(1)*offset(0)

    :ivar start_value: Value representing the global start for the
        lattice: i.e., iStart + jStart*ni + kStart*ni*nj
    :ivar offset:
    """
    start_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    offset: List[IntegerConstantArray] = field(
        default_factory=list,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "min_occurs": 1,
        }
    )

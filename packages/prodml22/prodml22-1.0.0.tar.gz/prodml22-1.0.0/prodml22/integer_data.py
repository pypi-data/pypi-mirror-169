from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_measure_data import AbstractMeasureData
from prodml22.integer_qualified_count import IntegerQualifiedCount

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class IntegerData(AbstractMeasureData):
    """
    Integer data.

    :ivar integer_value: The value of a dependent (data) variable in a
        row of the curve table. The units of measure are specified in
        the curve definition. The first value corresponds to order=1 for
        columns where isIndex is false. The second to order=2. And so
        on. The number of index and data values must match the number of
        columns in the table.
    """
    integer_value: Optional[IntegerQualifiedCount] = field(
        default=None,
        metadata={
            "name": "IntegerValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

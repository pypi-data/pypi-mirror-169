from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_measure_data import AbstractMeasureData
from prodml22.kind_qualified_string import KindQualifiedString

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class StringData(AbstractMeasureData):
    """
    String data.

    :ivar string_value: The value of a dependent (data) variable in a
        row of the curve table. The units of measure are specified in
        the curve definition. The first value corresponds to order=1 for
        columns where isIndex is false. The second to order=2. And so
        on. The number of index and data values must match the number of
        columns in the table.
    """
    string_value: Optional[KindQualifiedString] = field(
        default=None,
        metadata={
            "name": "StringValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )

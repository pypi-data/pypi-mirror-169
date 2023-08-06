from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_measure_data import AbstractMeasureData

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CurveData(AbstractMeasureData):
    """
    The data of a curve.

    :ivar index: The value of an independent (index) variable in a row
        of the curve table. The units of measure are specified in the
        curve definition. The first value corresponds to order=1 for
        columns where isIndex is true. The second to order=2. And so on.
        The number of index and data values must match the number of
        columns in the table.
    :ivar value: The value of a dependent (data) variable in a row of
        the curve table. The units of measure are specified in the curve
        definition. The first value corresponds to order=1 for columns
        where isIndex is false. The second to order=2. And so on. The
        number of index and data values must match the number of columns
        in the table.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    index: List[int] = field(
        default_factory=list,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
            "min_inclusive": 1,
        }
    )
    value: List[float] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )

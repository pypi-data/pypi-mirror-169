from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.abstract_object import AbstractObject
from prodml22.abstract_value import AbstractValue
from prodml22.keyword_value_struct import KeywordValueStruct
from prodml22.legacy_unit_of_measure import LegacyUnitOfMeasure
from prodml22.measure_class import MeasureType
from prodml22.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class TimeSeriesData(AbstractObject):
    """
    Defines the time series data being transferred.

    :ivar key: A keyword value pair which characterizes the underlying
        nature of this value. The key value may provide part of the
        unique identity of an instance of a concept or it may
        characterize the underlying concept. The key value is defined
        within the specified keyword-naming system. This is essentially
        a classification of the data in the specified system (keyword).
    :ivar uom: If the time series is a measure, then this specifies the
        unit of measure. The unit acronym must be chosen from the list
        that is valid for the measure class. If this is specified,  then
        the measure class must be specified.
    :ivar measure_class: Defines the type of measure that the time
        series represents. If this is specified then unit must be
        specified. This may be redundant to some information in the
        keys, but it is important for allowing an application to
        understand the nature of a measure value, even if it does not
        understand all of the underlying nature.
    :ivar comment: A comment about the time series.
    :ivar data_value:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    key: List[KeywordValueStruct] = field(
        default_factory=list,
        metadata={
            "name": "Key",
            "type": "Element",
        }
    )
    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    measure_class: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "MeasureClass",
            "type": "Element",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "max_length": 2000,
        }
    )
    data_value: List[AbstractValue] = field(
        default_factory=list,
        metadata={
            "name": "DataValue",
            "type": "Element",
        }
    )

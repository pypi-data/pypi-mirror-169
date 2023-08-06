from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.abstract_value_array import AbstractValueArray
from prodml22.data_object_reference import DataObjectReference
from prodml22.legacy_unit_of_measure import LegacyUnitOfMeasure
from prodml22.object_alias import ObjectAlias
from prodml22.property_kind_facet import PropertyKindFacet
from prodml22.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Column:
    """
    Defines one column in a column-based table.

    :ivar description: A free text description for this column.
    :ivar title: The title of the column. It is optional because the
        property kind already provides information about the content in
        a column.
    :ivar uom: If present, this value overrides the default UOM of the
        associated property kind.
    :ivar value_count_per_row: The count of values in each row of this
        column. If this value is greater than 1, then the fastest
        dimension of the column Values array must be this value.
        EXAMPLE: If this value is 3 for a column of 10 rows, then the
        corresponding array would be [10, 3] (C array notation where 3
        is fastest and 10 slowest).
    :ivar property_kind:
    :ivar values:
    :ivar aliases:
    :ivar facet:
    """
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".*:.*",
        }
    )
    value_count_per_row: int = field(
        default=1,
        metadata={
            "name": "ValueCountPerRow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    values: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    aliases: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "Aliases",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    facet: List[PropertyKindFacet] = field(
        default_factory=list,
        metadata={
            "name": "Facet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )

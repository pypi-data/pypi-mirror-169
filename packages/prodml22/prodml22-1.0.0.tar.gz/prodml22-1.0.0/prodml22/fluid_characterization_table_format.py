from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fluid_characterization_table_column import FluidCharacterizationTableColumn

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterizationTableFormat:
    """
    Fluid characterization table format.

    :ivar null_value: The null value for this fluid characterization
        table format.
    :ivar delimiter: The delimiter for this fluid characterization table
        format.
    :ivar table_column:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    null_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "NullValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    delimiter: Optional[str] = field(
        default=None,
        metadata={
            "name": "Delimiter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    table_column: List[FluidCharacterizationTableColumn] = field(
        default_factory=list,
        metadata={
            "name": "TableColumn",
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

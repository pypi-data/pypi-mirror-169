from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fluid_characterization_parameter import FluidCharacterizationParameter
from prodml22.fluid_characterization_table_row import FluidCharacterizationTableRow

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterizationTable:
    """
    Fluid characterization table.

    :ivar table_constant: A constant associated with this fluid
        characterization table.
    :ivar remark: Remarks and comments about this data item.
    :ivar table_row:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    :ivar table_format: The uid reference of the table format for this
        table.
    :ivar name: The name of this table.
    """
    table_constant: List[FluidCharacterizationParameter] = field(
        default_factory=list,
        metadata={
            "name": "TableConstant",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    table_row: List[FluidCharacterizationTableRow] = field(
        default_factory=list,
        metadata={
            "name": "TableRow",
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
    table_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "tableFormat",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )

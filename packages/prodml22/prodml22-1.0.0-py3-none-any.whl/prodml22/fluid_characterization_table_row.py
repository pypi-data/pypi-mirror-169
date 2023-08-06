from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.saturation_kind import SaturationKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterizationTableRow:
    """A string containing the contents of a row of the table, as a sequence of
    values, one per Fluid Characterization Table Column which has been defined.

    Values are separated by the Delimiter specified in the Table Format,
    and use Null Values when required, also as specified in the Table
    Format.

    :ivar value:
    :ivar row: The ID (index) of this row of data in the Table Row.
    :ivar kind: This type characteristic describes the row of data as
        either saturated or under-saturated at the conditions defined
        for the row.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    row: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    kind: Optional[SaturationKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

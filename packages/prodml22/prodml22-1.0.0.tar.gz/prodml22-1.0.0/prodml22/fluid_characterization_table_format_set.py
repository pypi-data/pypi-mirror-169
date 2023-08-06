from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.fluid_characterization_table_format import FluidCharacterizationTableFormat

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterizationTableFormatSet:
    """
    A set of table format definitions.

    :ivar fluid_characterization_table_format: Fluid characterization
        table format.
    """
    fluid_characterization_table_format: List[FluidCharacterizationTableFormat] = field(
        default_factory=list,
        metadata={
            "name": "FluidCharacterizationTableFormat",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )

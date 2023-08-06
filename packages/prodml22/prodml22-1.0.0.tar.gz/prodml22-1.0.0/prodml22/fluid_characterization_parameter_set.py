from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.fluid_characterization_parameter import FluidCharacterizationParameter

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterizationParameterSet:
    """
    The constant definition used in the table.

    :ivar fluid_characterization_parameter: The constant definition used
        in the table.
    """
    fluid_characterization_parameter: List[FluidCharacterizationParameter] = field(
        default_factory=list,
        metadata={
            "name": "FluidCharacterizationParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fluid_component_fraction import FluidComponentFraction

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OverallComposition:
    """
    Overall composition.

    :ivar remark: Remarks and comments about this data item.
    :ivar fluid_component_fraction: Fluid component.
    """
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    fluid_component_fraction: List[FluidComponentFraction] = field(
        default_factory=list,
        metadata={
            "name": "FluidComponentFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
